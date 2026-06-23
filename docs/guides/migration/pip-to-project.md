---
subtitle: From pip to a uv project
description: 本指南将讨论如何从以 `requirements` 文件为中心的 `pip` 和 `pip-tools` 工作流转换为使用 `pyproject.toml` 和 `uv.lock` 文件的 uv 项目工作流。
---

# 从 pip 迁移到 uv 项目 {#migrating-from-pip-to-a-uv-project}

本指南将讨论如何从以 `requirements` 文件为中心的 `pip` 和 `pip-tools` 工作流转换为使用 `pyproject.toml` 和 `uv.lock` 文件的 uv 项目工作流。

!!! note

    如果您正在寻找从 `pip` 和 `pip-tools` 迁移到 uv 的平替（drop-in）接口，或者从已经在使用 `pyproject.toml` 的现有工作流迁移，这些指南尚未编写。请参阅 [#5200](https://github.com/astral-sh/uv/issues/5200) 跟踪进展。

我们首先概述使用 `pip` 进行开发的方式，然后讨论如何迁移到 uv。

!!! tip

    如果您熟悉相关生态，可以直接跳转到[导入 requirements 文件](#importing-requirements-files)说明。

## 理解 pip 工作流 {#understanding-pip-workflows}

### 项目依赖 {#project-dependencies}

当您想在项目中使用某个包时，首先需要安装它。`pip` 支持命令式安装包，例如：

```console
$ pip install fastapi
```

这会将包安装到 `pip` 所在的运行环境中。这个环境可能是虚拟环境，也可能是系统 Python 安装的全局环境。

然后，您可以运行需要该包的 Python 脚本：

```python title="example.py"
import fastapi
```

最佳实践是为每个项目创建虚拟环境，以避免包之间的混用。例如：

```console
$ python -m venv
$ source .venv/bin/activate
$ pip ...
```

我们将在下面的[项目环境](#project-environments)部分中再次讨论这个主题。

### Requirements 文件 {#requirements-files}

在与他人共享项目时，提前声明所有需要的包是很有用的。`pip` 支持从文件中安装依赖项，例如：

```python title="requirements.txt"
fastapi
```

```console
$ pip install -r requirements.txt
```

请注意，上面的 `fastapi` 并没有被"锁定"到特定版本——每个参与项目的人可能安装了不同版本的 `fastapi`。`pip-tools` 正是为了改善这种体验而创建的。

使用 `pip-tools` 时，requirements 文件既指定项目的依赖项，又将依赖项锁定到特定版本——文件扩展名用于区分两者的用途。例如，如果您需要 `fastapi` 和 `pydantic`，可以在 `requirements.in` 文件中指定：

```python title="requirements.in"
fastapi
pydantic>2
```

请注意，`pydantic` 有一个版本约束——这意味着只能使用 `2.0.0` 之后的版本。相比之下，`fastapi` 没有版本约束——可以使用任何版本。

这些依赖项可以编译为 `requirements.txt` 文件：

```console
$ pip-compile requirements.in -o requirements.txt
```

```python title="requirements.txt"
annotated-types==0.7.0
    # via pydantic
anyio==4.8.0
    # via starlette
fastapi==0.115.11
    # via -r requirements.in
idna==3.10
    # via anyio
pydantic==2.10.6
    # via
    #   -r requirements.in
    #   fastapi
pydantic-core==2.27.2
    # via pydantic
sniffio==1.3.1
    # via anyio
starlette==0.46.1
    # via fastapi
typing-extensions==4.12.2
    # via
    #   fastapi
    #   pydantic
    #   pydantic-core
```

这里，所有版本约束都是_精确的_。每个包只能使用一个特定版本。上面的示例是使用 `uv pip compile` 生成的，但也可以使用 `pip-tools` 的 `pip-compile` 生成。

虽然不太常见，`requirements.txt` 也可以使用 `pip freeze` 生成，方法是先将输入依赖项安装到环境中，然后导出已安装的版本：

```console
$ pip install -r requirements.in
$ pip freeze > requirements.txt
```

```python title="requirements.txt"
annotated-types==0.7.0
anyio==4.8.0
fastapi==0.115.11
idna==3.10
pydantic==2.10.6
pydantic-core==2.27.2
sniffio==1.3.1
starlette==0.46.1
typing-extensions==4.12.2
```

将依赖项编译为锁定的版本集后，这些文件会被提交到版本控制中并随项目分发。

然后，当有人想使用该项目时，他们从 requirements 文件安装：

```console
$ pip install -r requirements.txt
```

<!--- TODO: 讨论 `uv pip compile` 和 `pip compile` 的等效命令 -->

### 开发依赖 {#development-dependencies}

Requirements 文件格式一次只能描述一组依赖项。这意味着如果您有额外的依赖项_分组_，例如开发依赖项，它们需要单独的文件。例如，我们创建一个 `-dev` 依赖文件：

```python title="requirements-dev.in"
-r requirements.in
-c requirements.txt

pytest
```

请注意，基础依赖项通过 `-r requirements.in` 包含在内。这确保了您的开发环境同时考虑_所有_依赖项。`-c requirements.txt` _约束_包版本，以确保 `requirements-dev.txt` 使用与 `requirements.txt` 相同的版本。

!!! note

    直接使用 `-r requirements.txt` 而不是同时使用 `-r requirements.in` 和 `-c requirements.txt` 也是常见的做法。最终得到的包版本没有区别，但使用两个文件会产生注释，让您能够区分哪些是_直接_依赖项（由 `-r requirements.in` 注释）和哪些是_间接_依赖项（仅由 `-c requirements.txt` 注释）。

编译后的开发依赖项如下所示：

```python title="requirements-dev.txt"
annotated-types==0.7.0
    # via
    #   -c requirements.txt
    #   pydantic
anyio==4.8.0
    # via
    #   -c requirements.txt
    #   starlette
fastapi==0.115.11
    # via
    #   -c requirements.txt
    #   -r requirements.in
idna==3.10
    # via
    #   -c requirements.txt
    #   anyio
iniconfig==2.0.0
    # via pytest
packaging==24.2
    # via pytest
pluggy==1.5.0
    # via pytest
pydantic==2.10.6
    # via
    #   -c requirements.txt
    #   -r requirements.in
    #   fastapi
pydantic-core==2.27.2
    # via
    #   -c requirements.txt
    #   pydantic
pytest==8.3.5
    # via -r requirements-dev.in
sniffio==1.3.1
    # via
    #   -c requirements.txt
    #   anyio
starlette==0.46.1
    # via
    #   -c requirements.txt
    #   fastapi
typing-extensions==4.12.2
    # via
    #   -c requirements.txt
    #   fastapi
    #   pydantic
    #   pydantic-core
```

与基础依赖文件一样，这些文件会被提交到版本控制中并随项目分发。当有人想参与项目开发时，他们从 requirements 文件安装：

```console
$ pip install -r requirements-dev.txt
```

### 平台特定依赖 {#platform-specific-dependencies}

使用 `pip` 或 `pip-tools` 编译依赖项时，结果只能在其生成的平台上使用。这对于需要在多个平台（如 Windows 和 macOS）上使用的项目来说是一个问题。

例如，以一个简单的依赖项为例：

```python title="requirements.in"
tqdm
```

在 Linux 上，编译结果为：

```python title="requirements-linux.txt"
tqdm==4.67.1
    # via -r requirements.in
```

而在 Windows 上，编译结果为：

```python title="requirements-win.txt"
colorama==0.4.6
    # via tqdm
tqdm==4.67.1
    # via -r requirements.in
```

`colorama` 是 `tqdm` 仅在 Windows 上需要的依赖项。

使用 `pip` 和 `pip-tools` 时，项目需要为每个支持的平台声明一个 requirements 锁定文件。

!!! note

    uv 的解析器可以同时为多个平台编译依赖项（参见["通用解析"](../../concepts/resolution.md#universal-resolution)），
    允许您为所有平台使用单个 `requirements.txt`：

    ```console
    $ uv pip compile --universal requirements.in
    ```

    ```python title="requirements.txt"
    colorama==0.4.6 ; sys_platform == 'win32'
        # via tqdm
    tqdm==4.67.1
        # via -r requirements.in
    ```

    这种解析模式也用于使用 `pyproject.toml` 和 `uv.lock` 的场景。

## 迁移到 uv 项目 {#migrating-to-a-uv-project}

### `pyproject.toml` {#the-pyprojecttoml}

`pyproject.toml` 是 Python 项目元数据的标准化文件。它替代了 `requirements.in` 文件，允许您表示任意分组的项目依赖项。它还提供了一个集中的位置来存放项目元数据，例如构建系统或工具设置。

<!-- TODO: 链接到官方文档或撰写更多内容 -->

例如，上面的 `requirements.in` 和 `requirements-dev.in` 文件可以转换为如下的 `pyproject.toml`：

```toml title="pyproject.toml"
[project]
name = "example"
version = "0.0.1"
dependencies = [
    "fastapi",
    "pydantic>2"
]

[dependency-groups]
dev = ["pytest"]
```

我们将在下面讨论自动化这些导入所需的命令。

### uv 锁文件 {#the-uv-lockfile}

uv 使用锁文件（`uv.lock`）来锁定包版本。该文件的格式是 uv 特有的，使 uv 能够支持高级功能。它替代了 `requirements.txt` 文件。

锁文件会在添加依赖项时自动创建和填充，但您也可以使用 `uv lock` 显式创建它。

与 `requirements.txt` 文件不同，`uv.lock` 文件可以表示任意分组的依赖项，因此不需要多个文件来锁定开发依赖项。

uv 锁文件始终是[通用](../../concepts/resolution.md#universal-resolution)的，因此不需要多个文件来[为每个平台锁定依赖项](#platform-specific-dependencies)。这确保了所有开发者无论使用什么机器，都使用一致的、已锁定的依赖项版本。

uv 锁文件还支持诸如[将包固定到特定索引](../../concepts/indexes.md#pinning-a-package-to-an-index)等概念，这些在 `requirements.txt` 文件中是无法表示的。

!!! tip

    如果您只需要为部分平台锁定依赖项，请使用 [`tool.uv.environments`](../../concepts/resolution.md#limited-resolution-environments) 设置来限制解析范围和锁文件。

要了解更多信息，请参阅[锁文件](../../concepts/projects/layout.md#the-lockfile)文档。

### 导入 requirements 文件 {#importing-requirements-files}

首先，如果您还没有 `pyproject.toml`，请创建一个：

```console
$ uv init
```

然后，导入 requirements 的最简单方法是使用 `uv add`：

```console
$ uv add -r requirements.in
```

然而，这种转换有一些细微之处需要注意。请注意，我们使用的是 `requirements.in` 文件，它没有将包固定到精确版本，因此 uv 会为这些包解析新的版本。您可能希望继续使用 `requirements.txt` 中先前锁定的版本，这样在切换到 uv 时，依赖项版本不会发生变化。

解决方案是将您已锁定的版本作为_约束_添加。uv 支持在 `add` 时使用这些约束来保留已锁定的版本：

```console
$ uv add -r requirements.in -c requirements.txt
```

在生成 `uv.lock` 文件时，您现有的版本将被保留。

#### 导入平台特定约束 {#importing-platform-specific-constraints}

如果您的平台特定依赖项已编译到单独的文件中，您仍然可以过渡到通用锁文件。但是，您不能直接使用 `-c` 从现有平台特定的 `requirements.txt` 文件指定约束，因为它们不包含描述运行环境的标记，因此会发生冲突。

要添加必要的标记，请使用 `uv pip compile` 转换现有文件。例如，给定以下内容：

```python title="requirements-win.txt"
colorama==0.4.6
    # via tqdm
tqdm==4.67.1
    # via -r requirements.in
```

可以使用以下命令添加标记：

```console
$ uv pip compile requirements.in -o requirements-win.txt --python-platform windows --no-strip-markers
```

请注意，结果输出中 `colorama` 包含了 Windows 标记：

```python title="requirements-win.txt"
colorama==0.4.6 ; sys_platform == 'win32'
    # via tqdm
tqdm==4.67.1
    # via -r requirements.in
```

使用 `-o` 时，uv 会尽可能将版本约束为与现有输出文件匹配。

可以通过为每个需要导入的 requirements 文件更改 `--python-platform` 和 `-o` 的值（例如改为 `linux` 和 `macos`）来为其他平台添加标记。

每个 `requirements.txt` 文件转换完成后，可以使用 `uv add` 将依赖项导入到 `pyproject.toml` 和 `uv.lock` 中：

```console
$ uv add -r requirements.in -c requirements-win.txt -c requirements-linux.txt
```

#### 导入开发依赖文件 {#importing-development-dependency-files}

正如[开发依赖](#development-dependencies)部分所讨论的，为开发目的设置依赖项分组是常见的做法。

要导入开发依赖项，请在 `uv add` 中使用 `--dev` 标志：

```console
$ uv add --dev -r requirements-dev.in -c requirements-dev.txt
```

如果 `requirements-dev.in` 通过 `-r` 包含了父级 `requirements.in`，则需要将其剥离，以避免将基础依赖项添加到 `dev` 依赖组中。以下示例使用 `sed` 剥离以 `-r` 开头的行，然后将结果通过管道传递给 `uv add`：

```console
$ sed '/^-r /d' requirements-dev.in | uv add --dev -r - -c requirements-dev.txt
```

除了 `dev` 依赖组，uv 还支持任意组名。例如，如果您还有一组专门用于构建文档的依赖项，可以将它们导入到 `docs` 组中：

```console
$ uv add -r requirements-docs.in -c requirements-docs.txt --group docs
```

#### 导入依赖项来源 {#importing-dependency-sources}

当导入本地路径或 Git 仓库上的依赖项时，例如：

```python title="requirements.in"
./path-dep
-e ./editable-path-dep
git-dep @ git+https://github.com/astral-sh/git-dep
```

uv 会将它们映射到 `pyproject.toml` 中 `[tool.uv.sources]` 表的[依赖项来源](../../concepts/projects/dependencies.md#dependency-sources)：

```toml title="pyproject.toml"
[project]
dependencies = [
    "path-dep",
    "editable-path-dep",
    "git-dep",
]

[tool.uv.sources]
path-dep = { path = "./path-dep" }
editable-path-dep = { path = "./editable-path-dep", editable = true }
git-dep = { git = "https://github.com/astral-sh/git-dep" }
```

### 项目环境 {#project-environments}

与 `pip` 不同，uv 不以"激活"虚拟环境的概念为中心。相反，uv 为每个项目在 `.venv` 目录中使用专用的虚拟环境。此环境会自动管理，因此当您运行命令（如 `uv add`）时，环境会与项目依赖项同步。

在环境中执行命令的首选方式是使用 `uv run`，例如：

```console
$ uv run pytest
```

在每次 `uv run` 调用之前，uv 会验证锁文件是否与 `pyproject.toml` 保持同步，以及环境是否与锁文件保持同步，从而保持项目的一致性，无需手动干预。`uv run` 保证您的命令在一致、锁定的环境中运行。

项目环境也可以使用 `uv sync` 显式创建，例如供编辑器使用。

!!! note

    在项目模式下，uv 默认会优先使用项目目录中的 `.venv`，并忽略由 `VIRTUAL_ENV` 变量声明的活动环境。您可以通过 `--active` 标志选择使用活动环境。

要了解更多信息，请参阅[项目环境](../../concepts/projects/layout.md#the-project-environment)文档。

## 下一步 {#next-steps}

现在您已经迁移到 uv，请查看[项目概念](../../concepts/projects/index.md)页面，了解有关 uv 项目的更多详细信息。