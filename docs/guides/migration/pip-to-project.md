---
subtitle: From pip to a uv project
---

# 从 pip 迁移到 uv 项目

本指南将讨论如何从以 `requirements` 文件为中心的 `pip` 和 `pip-tools` 工作流转换为使用 `pyproject.toml` 和 `uv.lock` 文件的 uv 项目工作流。

!!! note

    如果你希望从 `pip` 和 `pip-tools` 迁移到 uv 的直接替代接口，或者从一个已经在使用 `pyproject.toml` 的现有工作流迁移，这些指南尚未编写。请参阅 [#5200](https://github.com/astral-sh/uv/issues/5200) 跟踪进展。

我们将首先概述使用 `pip` 进行开发，然后讨论迁移到 uv。

!!! tip

    如果你熟悉这个生态系统，可以直接跳转到[导入 requirements 文件](#importing-requirements-files)的说明。

## 了解 pip 工作流

### 项目依赖

当你想在项目中使用一个包时，你需要先安装它。`pip` 支持命令式安装包，例如：

```console
$ pip install fastapi
```

这将把包安装到 `pip` 所在的环境中。这可能是一个虚拟环境，也可能是你系统 Python 安装的全局环境。

然后，你可以运行一个需要该包的 Python 脚本：

```python title="example.py"
import fastapi
```

最佳实践是为每个项目创建一个虚拟环境，以避免项目之间的包混淆。例如：

```console
$ python -m venv
$ source .venv/bin/activate
$ pip ...
```

我们将在下面的[项目环境](#project-environments)部分重新讨论这个主题。

### Requirements 文件

与他人共享项目时，预先声明所有需要的包是很有用的。`pip` 支持从文件安装依赖，例如：

```python title="requirements.txt"
fastapi
```

```console
$ pip install -r requirements.txt
```

注意上面 `fastapi` 并没有“锁定”到特定版本——每个参与项目的人安装的 `fastapi` 版本可能都不同。`pip-tools` 的出现就是为了改善这种体验。

使用 `pip-tools` 时，requirements 文件同时指定项目依赖和将依赖锁定到特定版本——通过文件扩展名来区分两者。例如，如果你需要 `fastapi` 和 `pydantic`，你可以在 `requirements.in` 文件中指定它们：

```python title="requirements.in"
fastapi
pydantic>2
```

注意 `pydantic` 有一个版本约束——这意味着只能使用 `2.0.0` 以上版本的 `pydantic`。相比之下，`fastapi` 没有版本约束——任何版本都可以使用。

这些依赖可以被编译成一个 `requirements.txt` 文件：

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

在这里，所有的版本约束都是_精确的_。每个包只能使用一个特定版本。上面的例子是用 `uv pip compile` 生成的，但也可以用 `pip-tools` 的 `pip-compile` 生成。

虽然不太常见，`requirements.txt` 也可以通过 `pip freeze` 生成，方法是先将输入依赖安装到环境中，然后导出已安装的版本：

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

将依赖编译成一组锁定的版本后，这些文件会被提交到版本控制并随项目分发。

然后，当有人想使用这个项目时，他们从 requirements 文件安装：

```console
$ pip install -r requirements.txt
```

<!--- TODO: Discuss equivalent commands for `uv pip compile` and `pip compile` -->

### 开发依赖

requirements 文件格式一次只能描述一组依赖。这意味着如果你有额外的依赖_组_，比如开发依赖，它们需要单独的文件。例如，我们创建一个 `-dev` 依赖文件：

```python title="requirements-dev.in"
-r requirements.in
-c requirements.txt

pytest
```

注意基础依赖是通过 `-r requirements.in` 包含进来的。这确保你的开发环境会考虑_所有_的依赖。`-c requirements.txt` _约束_了包的版本，以确保 `requirements-dev.txt` 使用与 `requirements.txt` 相同的版本。

!!! note

    直接使用 `-r requirements.txt` 而不是同时使用 `-r requirements.in` 和 `-c requirements.txt` 是很常见的。在最终的包版本上没有区别，但同时使用两个文件会产生注释，让你能够确定哪些是_直接_依赖（用 `-r requirements.in` 注释）和哪些是_间接_依赖（只用 `-c requirements.txt` 注释）。

编译后的开发依赖如下所示：

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

与基础依赖文件一样，这些文件也被提交到版本控制并随项目分发。当有人想在项目上工作时，他们会从 requirements 文件安装：

```console
$ pip install -r requirements-dev.txt
```

### 平台特定依赖

当使用 `pip` 或 `pip-tools` 编译依赖时，结果只在生成它的同一平台上可用。这给需要在多个平台（如 Windows 和 macOS）上使用的项目带来了问题。

例如，看一个简单的依赖：

```python title="requirements.in"
tqdm
```

在 Linux 上，它编译为：

```python title="requirements-linux.txt"
tqdm==4.67.1
    # via -r requirements.in
```

而在 Windows 上，它编译为：

```python title="requirements-win.txt"
colorama==0.4.6
    # via tqdm
tqdm==4.67.1
    # via -r requirements.in
```

`colorama` 是 `tqdm` 的一个仅限 Windows 的依赖。

当使用 `pip` 和 `pip-tools` 时，项目需要为每个支持的平台声明一个 requirements lock 文件。

!!! note

    uv 的解析器可以一次性为多个平台编译依赖（参见[“通用解析”](../../concepts/resolution.md#universal-resolution)），允许你为所有平台使用单个 `requirements.txt`：

    ```console
    $ uv pip compile --universal requirements.in
    ```

    ```python title="requirements.txt"
    colorama==0.4.6 ; sys_platform == 'win32'
        # via tqdm
    tqdm==4.67.1
        # via -r requirements.in
    ```

    当使用 `pyproject.toml` 和 `uv.lock` 时，也会使用此解析模式。

## 迁移到 uv 项目

### `pyproject.toml`

`pyproject.toml` 是一个用于 Python 项目元数据的标准化文件。它取代了 `requirements.in` 文件，允许你表示任意的项目依赖组。它还为你的项目元数据（如构建系统或工具设置）提供了一个集中的位置。

<!-- TODO: Link to the official docs on this or write more -->

例如，上面的 `requirements.in` 和 `requirements-dev.in` 文件可以像下面这样转换为一个 `pyproject.toml`：

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

### uv lockfile

uv 使用一个 lockfile (`uv.lock`) 文件来锁定包版本。该文件的格式是 uv 特有的，允许 uv 支持高级功能。它取代了 `requirements.txt` 文件。

在添加依赖时，lockfile 会被自动创建和填充，但你也可以用 `uv lock` 显式创建它。

与 `requirements.txt` 文件不同，`uv.lock` 文件可以表示任意的依赖组，因此不需要多个文件来锁定开发依赖。

uv lockfile 始终是[通用的](../../concepts/resolution.md#universal-resolution)，因此不需要多个文件来为[每个平台锁定依赖](#platform-specific-dependencies)。这确保了所有开发者无论使用什么机器，都在使用一致的、锁定的依赖版本。

uv lockfile 还支持诸如[将包固定到特定索引](../../concepts/indexes.md#pinning-a-package-to-an-index)之类的概念，这在 `requirements.txt` 文件中是无法表示的。

!!! tip

    如果你只需要为一部分平台锁定，请使用 [`tool.uv.environments`](../../concepts/resolution.md#limited-resolution-environments) 设置来限制解析和 lockfile。

要了解更多信息，请参阅 [lockfile](../../concepts/projects/layout.md#the-lockfile) 文档。

### 导入 requirements 文件

首先，如果你还没有 `pyproject.toml`，请创建一个：

```console
$ uv init
```

然后，导入 requirements 最简单的方法是使用 `uv add`：

```console
$ uv add -r requirements.in
```

然而，这个转换过程有一些细微之处。注意我们使用的是 `requirements.in` 文件，它没有将包固定到确切的版本，所以 uv 会为这些包解析新的版本。你可能希望继续使用 `requirements.txt` 中先前锁定的版本，这样在切换到 uv 时，你的依赖版本都不会改变。

解决方案是将你锁定的版本添加为_约束_。uv 支持在 `add` 时使用这些约束来保留锁定的版本：

```console
$ uv add -r requirements.in -c requirements.txt
```

在生成 `uv.lock` 文件时，你现有的版本将被保留。

#### 导入平台特定的约束

如果你的平台特定依赖已经被编译到单独的文件中，你仍然可以转换到一个通用的 lockfile。但是，你不能仅仅使用 `-c` 来指定来自现有平台特定 `requirements.txt` 文件的约束，因为它们不包含描述环境的标记，因此会产生冲突。

要添加必要的标记，请使用 `uv pip compile` 来转换你现有的文件。例如，给定以下内容：

```python title="requirements-win.txt"
colorama==0.4.6
    # via tqdm
tqdm==4.67.1
    # via -r requirements.in
```

可以通过以下方式添加标记：

```console
$ uv pip compile requirements.in -o requirements-win.txt --python-platform windows --no-strip-markers
```

注意，生成的输出在 `colorama` 上包含一个 Windows 标记：

```python title="requirements-win.txt"
colorama==0.4.6 ; sys_platform == 'win32'
    # via tqdm
tqdm==4.67.1
    # via -r requirements.in
```

当使用 `-o` 时，如果可能，uv 会约束版本以匹配现有的输出文件。

可以通过为每个需要导入的 requirements 文件更改 `--python-platform` 和 `-o` 的值来为其他平台添加标记，例如，改为 `linux` 和 `macos`。

一旦每个 `requirements.txt` 文件都已转换，就可以使用 `uv add` 将依赖项导入到 `pyproject.toml` 和 `uv.lock` 中：

```console
$ uv add -r requirements.in -c requirements-win.txt -c requirements-linux.txt
```

#### 导入开发依赖文件

正如在[开发依赖](#development-dependencies)部分所讨论的，为开发目的设置依赖组是很常见的。

要导入开发依赖，请在 `uv add` 期间使用 `--dev` 标志：

```console
$ uv add --dev -r requirements-dev.in -c requirements-dev.txt
```

如果 `requirements-dev.in` 通过 `-r` 包含了父 `requirements.in`，则需要将其剥离，以避免将基础依赖项添加到 `dev` 依赖组中。以下示例使用 `sed` 剥离以 `-r` 开头的行，然后将结果通过管道传递给 `uv add`：

```console
$ sed '/^-r /d' requirements-dev.in | uv add --dev -r - -c requirements-dev.txt
```

除了 `dev` 依赖组，uv 还支持任意组名。例如，如果你还有一组专门用于构建文档的依赖，可以将其导入到 `docs` 组：

```console
$ uv add -r requirements-docs.in -c requirements-docs.txt --group docs
```

### 项目环境

与 `pip` 不同，uv 并不以“活动”虚拟环境的概念为中心。相反，uv 为每个项目在 `.venv` 目录中使用一个专用的虚拟环境。这个环境是自动管理的，所以当你运行一个命令，比如 `uv add`，环境会与项目依赖同步。

在环境中执行命令的首选方法是使用 `uv run`，例如：

```console
$ uv run pytest
```

在每次调用 `uv run` 之前，uv 会验证 lockfile 是否与 `pyproject.toml` 同步，以及环境是否与 lockfile 同步，从而使你的项目保持同步，无需手动干预。`uv run` 保证你的命令在一个一致的、锁定的环境中运行。

项目环境也可以用 `uv sync` 显式创建，例如，供编辑器使用。

!!! note

    在项目中时，uv 会优先使用项目目录中的 `.venv`，并默认忽略由 `VIRTUAL_ENV` 变量声明的活动环境。你可以使用 `--active` 标志选择使用活动环境。

要了解更多信息，请参阅[项目环境](../../concepts/projects/layout.md#_2)文档。

## 后续步骤

现在你已经迁移到 uv，可以看看[项目概念](../../concepts/projects/index.md)页面，了解有关 uv 项目的更多详细信息。
