---
title: 管理项目依赖
subtitle: Managing dependencies
description: 学习如何使用 uv 管理 Python 项目的依赖项。涵盖添加、移除、更改依赖项，配置平台特定依赖、可选依赖（extras）、开发依赖组、依赖项源（Git/URL/Path/工作空间）、可编辑安装、虚拟依赖项以及依赖项说明符语法的完整中文指南。
---

# 管理依赖项 {#managing-dependencies}

## 依赖项字段 {#dependency-fields}

项目的依赖项定义在以下几个字段中：

- [`project.dependencies`](#project-dependencies)：已发布的依赖项。
- [`project.optional-dependencies`](#optional-dependencies)：已发布的可选依赖项，或称为
  "extras"。
- [`dependency-groups`](#dependency-groups)：用于开发的本地依赖项。
- [`tool.uv.sources`](#dependency-sources)：开发过程中依赖项的替代源。

!!! note

    `project.dependencies` 和 `project.optional-dependencies` 字段即使项目不打算发布也可以使用。`dependency-groups` 是最近才标准化的功能，可能尚未被所有工具支持。

uv 支持通过 `uv add` 和 `uv remove` 修改项目的依赖项，但也可以通过直接编辑 `pyproject.toml` 来更新依赖项元数据。

## 添加依赖项 {#adding-dependencies}

要添加依赖项：

```console
$ uv add httpx
```

将在 `project.dependencies` 字段中添加一条记录：

```toml title="pyproject.toml" hl_lines="4"
[project]
name = "example"
version = "0.1.0"
dependencies = ["httpx>=0.27.2"]
```

可以使用 [`--dev`](#development-dependencies)、[`--group`](#dependency-groups) 或
[`--optional`](#optional-dependencies) 标志将依赖项添加到其他字段。

依赖项将包含一个约束条件，例如 `>=0.27.2`，表示该包最新兼容版本。约束条件的类型可以通过
[`--bounds`](../../reference/settings.md#add-bounds) 调整，也可以直接提供约束条件：

```console
$ uv add "httpx>=0.20"
```

当从包注册表之外的源添加依赖项时，uv 会在 sources 字段中添加一条记录。例如，从 GitHub 添加 `httpx`：

```console
$ uv add "httpx @ git+https://github.com/encode/httpx"
```

`pyproject.toml` 将包含一个 [Git 源条目](#git)：

```toml title="pyproject.toml" hl_lines="8-9"
[project]
name = "example"
version = "0.1.0"
dependencies = [
    "httpx",
]

[tool.uv.sources]
httpx = { git = "https://github.com/encode/httpx" }
```

如果依赖项无法使用，uv 将显示错误：

```console
$ uv add "httpx>9999"
  × No solution found when resolving dependencies:
  ╰─▶ Because only httpx<=1.0.0b0 is available and your project depends on httpx>9999,
      we can conclude that your project's requirements are unsatisfiable.
```

### 从 requirements 文件导入依赖项 {#importing-dependencies-from-requirements-files}

在 `requirements.txt` 文件中声明的依赖项可以使用 `-r` 选项添加到项目中：

```
uv add -r requirements.txt
```

有关更多详细信息，请参阅 [pip 迁移指南](../../guides/migration/pip-to-project.md#importing-requirements-files)。

## 移除依赖项 {#removing-dependencies}

要移除依赖项：

```console
$ uv remove httpx
```

可以使用 `--dev`、`--group` 或 `--optional` 标志从特定表中移除依赖项。

如果为已移除的依赖项定义了[源](#dependency-sources)，并且没有其他对该依赖项的引用，则该源也会被移除。

## 更改依赖项 {#changing-dependencies}

要更改现有依赖项，例如为 `httpx` 使用不同的约束条件：

```console
$ uv add "httpx>0.1.0"
```

!!! note

    在此示例中，我们正在更改 `pyproject.toml` 中依赖项的约束条件。
    依赖项的锁定版本只有在需要满足新约束条件时才会更改。要强制将包版本更新到约束条件内的最新版本，请使用 `--upgrade-package <name>`，例如：

    ```console
    $ uv add "httpx>0.1.0" --upgrade-package httpx
    ```

    有关升级包的更多详细信息，请参阅[锁文件](./sync.md#upgrading-locked-package-versions)文档。

请求不同的依赖项源将更新 `tool.uv.sources` 表，例如在开发期间使用本地路径中的 `httpx`：

```console
$ uv add "httpx @ ../httpx"
```

## 平台特定依赖项 {#platform-specific-dependencies}

要确保依赖项仅在特定平台或特定 Python 版本上安装，请使用
[环境标记（environment markers）](https://peps.python.org/pep-0508/#environment-markers)。

例如，在 Linux 上安装 `jax`，但在 Windows 或 macOS 上不安装：

```console
$ uv add "jax; sys_platform == 'linux'"
```

生成的 `pyproject.toml` 将在依赖项定义中包含环境标记：

```toml title="pyproject.toml" hl_lines="6"
[project]
name = "project"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = ["jax; sys_platform == 'linux'"]
```

类似地，在 Python 3.11 及更高版本上包含 `numpy`：

```console
$ uv add "numpy; python_version >= '3.11'"
```

有关可用标记和运算符的完整列表，请参阅 Python 的[环境标记](https://peps.python.org/pep-0508/#environment-markers)文档。

!!! tip

    依赖项源也可以[按平台更改](#platform-specific-sources)。

## 项目依赖项 {#project-dependencies}

`project.dependencies` 表表示上传到 PyPI 或构建 wheel 时使用的依赖项。每个依赖项使用
[依赖项说明符（dependency specifiers）](https://packaging.python.org/en/latest/specifications/dependency-specifiers/)
语法指定，该表遵循 [PEP 621](https://packaging.python.org/en/latest/specifications/pyproject-toml/) 标准。

`project.dependencies` 定义了项目所需的包列表，以及安装时应使用的版本约束条件。每个条目包含依赖项名称和版本。条目可以包含 extras 或用于平台特定包的环境标记。例如：

```toml title="pyproject.toml"
[project]
name = "albatross"
version = "0.1.0"
dependencies = [
  # 此范围内的任何版本
  "tqdm >=4.66.2,<5",
  # 精确的 torch 版本
  "torch ==2.2.2",
  # 安装带有 torch extra 的 transformers
  "transformers[torch] >=4.39.3,<5",
  # 仅在较旧的 Python 版本上安装此包
  # 有关更多信息，请参阅"环境标记"
  "importlib_metadata >=7.1.0,<8; python_version < '3.10'",
  "mollymawk ==0.1.0"
]
```

## 依赖项源 {#dependency-sources}

`tool.uv.sources` 表通过替代依赖项源扩展了标准依赖项表，这些源在开发过程中使用。

依赖项源添加了对 `project.dependencies` 标准不支持的常见模式的支持，例如可编辑安装和相对路径。例如，从相对于项目根目录的目录安装 `foo`：

```toml title="pyproject.toml" hl_lines="7"
[project]
name = "example"
version = "0.1.0"
dependencies = ["foo"]

[tool.uv.sources]
foo = { path = "./packages/foo" }
```

uv 支持以下依赖项源：

- [索引（Index）](#index)：从特定包索引解析的包。
- [Git](#git)：一个 Git 仓库。
- [URL](#url)：一个远程 wheel 或源码分发包。
- [路径（Path）](#path)：一个本地 wheel、源码分发包或项目目录。
- [工作空间（Workspace）](#workspace-member)：当前工作空间的成员。

!!! important

    源仅由 uv 识别。如果使用其他工具，则只会使用标准项目表中的定义。如果使用其他工具进行开发，源表中提供的任何元数据都需要以该工具的格式重新指定。

### 索引 {#index}

要从特定索引添加 Python 包，请使用 `--index` 选项：

```console
$ uv add torch --index pytorch=https://download.pytorch.org/whl/cpu
```

uv 会将索引存储在 `[[tool.uv.index]]` 中，并添加一个 `[tool.uv.sources]` 条目：

```toml title="pyproject.toml"
[project]
dependencies = ["torch"]

[tool.uv.sources]
torch = { index = "pytorch" }

[[tool.uv.index]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cpu"
```

!!! tip

    由于 PyTorch 索引的特定性，上述示例仅适用于 x86-64 Linux。
    有关设置 PyTorch 的更多信息，请参阅 [PyTorch 指南](../../guides/integration/pytorch.md)。

使用 `index` 源会将包_固定_到给定的索引——它不会从其他索引下载。

定义索引时，可以包含 `explicit` 标志，以指示该索引_仅_用于在 `tool.uv.sources` 中显式指定它的包。如果未设置 `explicit`，其他包也可能从该索引解析（如果在其他地方找不到）。

```toml title="pyproject.toml" hl_lines="4"
[[tool.uv.index]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cpu"
explicit = true
```

### Git {#git}

要添加 Git 依赖项源，请在 Git 兼容的 URL 前加上 `git+`。

例如：

```console
$ # 通过 HTTP(S) 安装。
$ uv add git+https://github.com/encode/httpx

$ # 通过 SSH 安装。
$ uv add git+ssh://git@github.com/encode/httpx
```

```toml title="pyproject.toml" hl_lines="5"
[project]
dependencies = ["httpx"]

[tool.uv.sources]
httpx = { git = "https://github.com/encode/httpx" }
```

可以请求特定的 Git 引用，例如标签（tag）：

```console
$ uv add git+https://github.com/encode/httpx --tag 0.27.0
```

```toml title="pyproject.toml" hl_lines="7"
[project]
dependencies = ["httpx"]

[tool.uv.sources]
httpx = { git = "https://github.com/encode/httpx", tag = "0.27.0" }
```

或者分支（branch）：

```console
$ uv add git+https://github.com/encode/httpx --branch main
```

```toml title="pyproject.toml" hl_lines="7"
[project]
dependencies = ["httpx"]

[tool.uv.sources]
httpx = { git = "https://github.com/encode/httpx", branch = "main" }
```

或者修订版本（commit）：

```console
$ uv add git+https://github.com/encode/httpx --rev 326b9431c761e1ef1e00b9f760d1f654c8db48c6
```

```toml title="pyproject.toml" hl_lines="7"
[project]
dependencies = ["httpx"]

[tool.uv.sources]
httpx = { git = "https://github.com/encode/httpx", rev = "326b9431c761e1ef1e00b9f760d1f654c8db48c6" }
```

如果包不在仓库根目录中，可以指定 `subdirectory`：

```console
$ uv add git+https://github.com/langchain-ai/langchain#subdirectory=libs/langchain
```

```toml title="pyproject.toml"
[project]
dependencies = ["langchain"]

[tool.uv.sources]
langchain = { git = "https://github.com/langchain-ai/langchain", subdirectory = "libs/langchain" }
```

对 [Git LFS](https://git-lfs.com) 的支持也可以按源配置。默认情况下，不会获取 Git LFS 对象。

```console
$ uv add --lfs git+https://github.com/astral-sh/lfs-cowsay
```

```toml title="pyproject.toml"
[project]
dependencies = ["lfs-cowsay"]

[tool.uv.sources]
lfs-cowsay = { git = "https://github.com/astral-sh/lfs-cowsay", lfs = true }
```

- 当 `lfs = true` 时，uv 将始终为此 Git 源获取 LFS 对象。
- 当 `lfs = false` 时，uv 将永远不会为此 Git 源获取 LFS 对象。
- 省略时，对于所有没有显式 `lfs` 配置的 Git 源，将使用 `UV_GIT_LFS` 环境变量。

!!! important

    在尝试安装使用 Git LFS 的源之前，请确保系统上已安装并配置了 Git LFS，否则可能会发生构建失败。

### URL {#url}

要添加 URL 源，请提供一个指向 wheel（以 `.whl` 结尾）或源码分发包（通常以 `.tar.gz` 或 `.zip` 结尾；所有支持的格式请参见[此处](../../concepts/resolution.md#source-distribution)）的 `https://` URL。

例如：

```console
$ uv add "https://files.pythonhosted.org/packages/5c/2d/3da5bdf4408b8b2800061c339f240c1802f2e82d55e50bd39c5a881f47f0/httpx-0.27.0.tar.gz"
```

将在 `pyproject.toml` 中生成：

```toml title="pyproject.toml" hl_lines="5"
[project]
dependencies = ["httpx"]

[tool.uv.sources]
httpx = { url = "https://files.pythonhosted.org/packages/5c/2d/3da5bdf4408b8b2800061c339f240c1802f2e82d55e50bd39c5a881f47f0/httpx-0.27.0.tar.gz" }
```

URL 依赖项也可以在 `pyproject.toml` 中使用 `{ url = <url> }` 语法手动添加或编辑。如果源码分发包不在归档根目录中，可以指定 `subdirectory`。

### 路径 {#path}

要添加路径源，请提供 wheel（以 `.whl` 结尾）、源码分发包（通常以 `.tar.gz` 或 `.zip` 结尾；所有支持的格式请参见[此处](../../concepts/resolution.md#source-distribution)）或包含 `pyproject.toml` 的目录的路径。

例如：

```console
$ uv add /example/foo-0.1.0-py3-none-any.whl
```

将在 `pyproject.toml` 中生成：

```toml title="pyproject.toml"
[project]
dependencies = ["foo"]

[tool.uv.sources]
foo = { path = "/example/foo-0.1.0-py3-none-any.whl" }
```

路径也可以是相对路径：

```console
$ uv add ./foo-0.1.0-py3-none-any.whl
```

或者指向项目目录的路径：

```console
$ uv add ~/projects/bar/
```

!!! important

    当使用目录作为路径依赖项时，uv 默认会尝试将目标构建并安装为包。有关详细信息，请参阅[虚拟依赖项](#virtual-dependencies)文档。

默认情况下，路径依赖项不会使用[可编辑安装](#editable-dependencies)。对于项目目录，可以请求可编辑安装：

```console
$ uv add --editable ../projects/bar/
```

将在 `pyproject.toml` 中生成：

```toml title="pyproject.toml"
[project]
dependencies = ["bar"]

[tool.uv.sources]
bar = { path = "../projects/bar", editable = true }
```

!!! tip

    对于同一仓库中的多个包，[_工作空间_](./workspaces.md)可能是更好的选择。

### 工作空间成员 {#workspace-member}

要声明对工作空间成员的依赖，请使用 `{ workspace = true }` 添加成员名称。所有工作空间成员必须显式声明。工作空间成员始终是[可编辑的](#editable-dependencies)。有关工作空间的更多详细信息，请参阅[工作空间](./workspaces.md)文档。

```toml title="pyproject.toml"
[project]
dependencies = ["foo==0.1.0"]

[tool.uv.sources]
foo = { workspace = true }

[tool.uv.workspace]
members = [
  "packages/foo"
]
```

### 平台特定源 {#platform-specific-sources}

你可以通过为源提供与[依赖项说明符](https://packaging.python.org/en/latest/specifications/dependency-specifiers/)兼容的环境标记，将源限制在给定平台或 Python 版本上。

例如，仅在 macOS 上从 GitHub 拉取 `httpx`，使用以下配置：

```toml title="pyproject.toml" hl_lines="8"
[project]
dependencies = ["httpx"]

[tool.uv.sources]
httpx = { git = "https://github.com/encode/httpx", tag = "0.27.2", marker = "sys_platform == 'darwin'" }
```

通过在源上指定标记，uv 仍会在所有平台上包含 `httpx`，但会在 macOS 上从 GitHub 下载源，并在所有其他平台上回退到 PyPI。

### 多个源 {#multiple-sources}

你可以通过提供源列表为单个依赖项指定多个源，并使用与 [PEP 508](https://peps.python.org/pep-0508/#environment-markers) 兼容的环境标记来区分它们。

例如，在 macOS 和 Linux 上拉取不同的 `httpx` 标签：

```toml title="pyproject.toml" hl_lines="6-7"
[project]
dependencies = ["httpx"]

[tool.uv.sources]
httpx = [
  { git = "https://github.com/encode/httpx", tag = "0.27.2", marker = "sys_platform == 'darwin'" },
  { git = "https://github.com/encode/httpx", tag = "0.24.1", marker = "sys_platform == 'linux'" },
]
```

此策略也适用于基于环境标记使用不同索引。例如，基于平台从不同的 PyTorch 索引安装 `torch`：

```toml title="pyproject.toml" hl_lines="6-7"
[project]
dependencies = ["torch"]

[tool.uv.sources]
torch = [
  { index = "torch-cpu", marker = "platform_system == 'Darwin'"},
  { index = "torch-gpu", marker = "platform_system == 'Linux'"},
]

[[tool.uv.index]]
name = "torch-cpu"
url = "https://download.pytorch.org/whl/cpu"
explicit = true

[[tool.uv.index]]
name = "torch-gpu"
url = "https://download.pytorch.org/whl/cu130"
explicit = true
```

### 禁用源 {#disabling-sources}

要指示 uv 忽略 `tool.uv.sources` 表（例如，模拟使用包的已发布元数据进行解析），请使用 `--no-sources` 标志：

```console
$ uv lock --no-sources
```

使用 `--no-sources` 也会阻止 uv 发现任何可能满足给定依赖项的[工作空间成员](#workspace-member)。

## 可选依赖项 {#optional-dependencies}

对于作为库发布的项目，通常会通过将某些功能设为可选来减少默认依赖树。例如，Pandas 有一个
[`excel` extra](https://pandas.pydata.org/docs/getting_started/install.html#excel-files) 和一个
[`plot` extra](https://pandas.pydata.org/docs/getting_started/install.html#visualization)，以避免在没有人明确需要它们时安装 Excel 解析器和 `matplotlib`。Extras 使用 `package[<extra>]` 语法请求，例如 `pandas[plot, excel]`。

可选依赖项在 `[project.optional-dependencies]` 中指定，这是一个 TOML 表，将 extra 名称映射到其依赖项，遵循[依赖项说明符](#dependency-specifiers)语法。

可选依赖项可以在 `tool.uv.sources` 中有条目，与普通依赖项相同。

```toml title="pyproject.toml"
[project]
name = "pandas"
version = "1.0.0"

[project.optional-dependencies]
plot = [
  "matplotlib>=3.6.3"
]
excel = [
  "odfpy>=1.4.1",
  "openpyxl>=3.1.0",
  "python-calamine>=0.1.7",
  "pyxlsb>=1.0.10",
  "xlrd>=2.0.1",
  "xlsxwriter>=3.0.5"
]
```

要添加可选依赖项，请使用 `--optional <extra>` 选项：

```console
$ uv add httpx --optional network
```

!!! note

    如果你有相互冲突的可选依赖项，解析将失败，除非你显式[将它们声明为冲突依赖项](./config.md#conflicting-dependencies)。

源也可以声明为仅适用于特定的可选依赖项。例如，基于可选的 `cpu` 或 `gpu` extra 从不同的 PyTorch 索引拉取 `torch`：

```toml title="pyproject.toml"
[project]
dependencies = []

[project.optional-dependencies]
cpu = [
  "torch",
]
gpu = [
  "torch",
]

[tool.uv.sources]
torch = [
  { index = "torch-cpu", extra = "cpu" },
  { index = "torch-gpu", extra = "gpu" },
]

[[tool.uv.index]]
name = "torch-cpu"
url = "https://download.pytorch.org/whl/cpu"

[[tool.uv.index]]
name = "torch-gpu"
url = "https://download.pytorch.org/whl/cu130"
```

## 开发依赖项 {#development-dependencies}

与可选依赖项不同，开发依赖项仅限本地使用，_不会_包含在发布到 PyPI 或其他索引时的项目需求中。因此，开发依赖项不包含在 `[project]` 表中。

开发依赖项可以在 `tool.uv.sources` 中有条目，与普通依赖项相同。

要添加开发依赖项，请使用 `--dev` 标志：

```console
$ uv add --dev pytest
```

uv 使用 `[dependency-groups]` 表（如 [PEP 735](https://peps.python.org/pep-0735/) 中定义）来声明开发依赖项。上述命令将创建一个 `dev` 组：

```toml title="pyproject.toml"
[dependency-groups]
dev = [
  "pytest >=8.1.1,<9"
]
```

`dev` 组是特殊处理的；有 `--dev`、`--only-dev` 和 `--no-dev` 标志用于切换其依赖项的包含或排除。另请参阅 `--no-default-groups` 以禁用所有默认组。此外，`dev` 组[默认会被同步](#default-groups)。

### 依赖项组 {#dependency-groups}

开发依赖项可以使用 `--group` 标志分为多个组。

例如，在 `lint` 组中添加开发依赖项：

```console
$ uv add --group lint ruff
```

这将生成以下 `[dependency-groups]` 定义：

```toml title="pyproject.toml"
[dependency-groups]
dev = [
  "pytest"
]
lint = [
  "ruff"
]
```

定义组后，可以使用 `--all-groups`、`--no-default-groups`、`--group`、`--only-group` 和
`--no-group` 选项来包含或排除它们的依赖项。

!!! tip

    `--dev`、`--only-dev` 和 `--no-dev` 标志分别等同于 `--group dev`、
    `--only-group dev` 和 `--no-group dev`。

uv 要求所有依赖项组彼此兼容，并在创建锁文件时一起解析所有组。

如果一个组中声明的依赖项与另一个组中的依赖项不兼容，uv 将无法解析项目需求并报错。

!!! note

    如果你有相互冲突的依赖项组，解析将失败，除非你显式[将它们声明为冲突依赖项](./config.md#conflicting-dependencies)。

### 嵌套组 {#nesting-groups}

一个依赖项组可以包含其他依赖项组，例如：

```toml title="pyproject.toml"
[dependency-groups]
dev = [
  {include-group = "lint"},
  {include-group = "test"}
]
lint = [
  "ruff"
]
test = [
  "pytest"
]
```

被包含组的依赖项不能与组中声明的其他依赖项冲突。

### 默认组 {#default-groups}

默认情况下，uv 会在环境中包含 `dev` 依赖项组（例如在 `uv run` 或 `uv sync` 期间）。要包含的默认组可以使用 `tool.uv.default-groups` 设置进行更改。

```toml title="pyproject.toml"
[tool.uv]
default-groups = ["dev", "foo"]
```

要默认启用所有依赖项组，请使用 `"all"` 代替列出组名：

```toml title="pyproject.toml"
[tool.uv]
default-groups = "all"
```

!!! tip

    要在 `uv run` 或 `uv sync` 期间禁用此行为，请使用 `--no-default-groups`。
    要排除特定的默认组，请使用 `--no-group <name>`。

### 组 `requires-python` {#group-requires-python}

默认情况下，依赖项组必须与项目的 `requires-python` 范围兼容。

如果依赖项组需要与项目不同范围的 Python 版本，可以在 `[tool.uv.dependency-groups]` 中为该组指定 `requires-python`，例如：

```toml title="pyproject.toml" hl_lines="9-10"
[project]
name = "example"
version = "0.0.0"
requires-python = ">=3.10"

[dependency-groups]
dev = ["pytest"]

[tool.uv.dependency-groups]
dev = {requires-python = ">=3.12"}
```

### 旧版 `dev-dependencies` {#legacy-dev-dependencies}

在 `[dependency-groups]` 标准化之前，uv 使用 `tool.uv.dev-dependencies` 字段来指定开发依赖项，例如：

```toml title="pyproject.toml"
[tool.uv]
dev-dependencies = [
  "pytest"
]
```

在此部分中声明的依赖项将与 `dependency-groups.dev` 中的内容合并。最终，`dev-dependencies` 字段将被弃用并移除。

!!! note

    如果存在 `tool.uv.dev-dependencies` 字段，`uv add --dev` 将使用现有部分，而不是添加新的 `dependency-groups.dev` 部分。

## 构建依赖项 {#build-dependencies}

如果项目结构为 [Python 包](./config.md#build-systems)，它可以声明构建项目所需但运行时不需要的依赖项。这些依赖项在 `[build-system]` 表中的 `build-system.requires` 下指定，遵循
[PEP 518](https://peps.python.org/pep-0518/)。

例如，如果项目使用 `setuptools` 作为构建后端，它应该将 `setuptools` 声明为构建依赖项：

```toml title="pyproject.toml"
[project]
name = "pandas"
version = "0.1.0"

[build-system]
requires = ["setuptools>=42"]
build-backend = "setuptools.build_meta"
```

默认情况下，uv 在解析构建依赖项时会遵循 `tool.uv.sources`。例如，要使用本地版本的 `setuptools` 进行构建，请将源添加到 `tool.uv.sources`：

```toml title="pyproject.toml"
[project]
name = "pandas"
version = "0.1.0"

[build-system]
requires = ["setuptools>=42"]
build-backend = "setuptools.build_meta"

[tool.uv.sources]
setuptools = { path = "./packages/setuptools" }
```

发布包时，我们建议运行 `uv build --no-sources` 以确保在 `tool.uv.sources` 被禁用时包能正确构建，就像使用其他构建工具（如 [`pypa/build`](https://github.com/pypa/build)）时的情况一样。

## 可编辑依赖项 {#editable-dependencies}

对包含 Python 包的目录进行常规安装时，会先构建一个 wheel，然后将该 wheel 安装到虚拟环境中，复制所有源文件。当包源文件被编辑时，虚拟环境将包含过时的版本。

可编辑安装通过向虚拟环境中添加一个指向项目的链接（一个 `.pth` 文件）来解决此问题，该链接指示解释器直接包含源文件。

可编辑安装有一些限制（主要是：构建后端需要支持它们，并且原生模块在导入前不会重新编译），但它们对于开发非常有用，因为虚拟环境将始终使用包的最新更改。

uv 默认对工作空间包使用可编辑安装。

要添加可编辑依赖项，请使用 `--editable` 标志：

```console
$ uv add --editable ./path/foo
```

或者，要在工作空间中退出使用可编辑依赖项：

```console
$ uv add --no-editable ./path/foo
```

## 虚拟依赖项 {#virtual-dependencies}

uv 允许依赖项是"虚拟的"，即依赖项本身不作为[包](./config.md#project-packaging)安装，但其依赖项会被安装。

默认情况下，依赖项永远不会是虚拟的。

具有 [`path` 源](#path)的依赖项如果显式设置了
[`tool.uv.package = false`](../../reference/settings.md#package)，则可以是虚拟的。如果没有此设置，uv 会将路径依赖项视为普通包，并尝试构建它，即使项目没有声明[构建系统](./config.md#build-systems)。

要将依赖项视为虚拟的，请在源上设置 `package = false`：

```toml title="pyproject.toml"
[project]
dependencies = ["bar"]

[tool.uv.sources]
bar = { path = "../projects/bar", package = false }
```

如果依赖项设置了 `tool.uv.package = false`，可以通过在源上声明 `package = true` 来覆盖：

```toml title="pyproject.toml"
[project]
dependencies = ["bar"]

[tool.uv.sources]
bar = { path = "../projects/bar", package = true }
```

类似地，具有 [`workspace` 源](#workspace-member)的依赖项如果显式设置了
[`tool.uv.package = false`](../../reference/settings.md#package)，则也可以是虚拟的。如果没有此设置，即使未声明[构建系统](./config.md#build-systems)，工作空间成员也会被构建。

_不是_依赖项的工作空间成员可以默认是虚拟的，例如，如果父 `pyproject.toml` 是：

```toml title="pyproject.toml"
[project]
name = "parent"
version = "1.0.0"
dependencies = []

[tool.uv.workspace]
members = ["child"]
```

而子 `pyproject.toml` 排除了构建系统：

```toml title="pyproject.toml"
[project]
name = "child"
version = "1.0.0"
dependencies = ["anyio"]
```

那么 `child` 工作空间成员不会被安装，但传递依赖项 `anyio` 会被安装。

相反，如果父项目声明了对 `child` 的依赖：

```toml title="pyproject.toml"
[project]
name = "parent"
version = "1.0.0"
dependencies = ["child"]

[tool.uv.sources]
child = { workspace = true }

[tool.uv.workspace]
members = ["child"]
```

那么 `child` 将被构建并安装。

## 依赖项说明符 {#dependency-specifiers}

uv 使用标准的
[依赖项说明符（dependency specifiers）](https://packaging.python.org/en/latest/specifications/dependency-specifiers/)，
最初在 [PEP 508](https://peps.python.org/pep-0508/) 中定义。依赖项说明符按顺序由以下部分组成：

- 依赖项名称
- 你需要的 extras（可选）
- 版本说明符
- 环境标记（可选）

版本说明符以逗号分隔并叠加使用，例如 `foo >=1.2.3,<2,!=1.4.0` 被解释为"`foo` 的版本至少为 1.2.3，但小于 2，且不是 1.4.0"。

说明符在需要时会用尾随零填充，因此 `foo ==2` 也匹配 foo 2.0.0。

星号可以用于等号匹配的最后一位，例如 `foo ==2.1.*` 将接受 2.1 系列的任何版本。类似地，`~=` 匹配最后一位相等或更高的版本，例如 `foo ~=1.2` 等同于 `foo >=1.2,<2`，而 `foo ~=1.2.3` 等同于 `foo >=1.2.3,<1.3`。

Extras 在名称和版本之间用方括号中的逗号分隔，例如
`pandas[excel,plot] ==2.2`。extra 名称之间的空格会被忽略。

某些依赖项仅在特定环境中需要，例如特定的 Python 版本或操作系统。例如，要为 `importlib.metadata` 模块安装 `importlib-metadata` 回退包，请使用 `importlib-metadata >=7.1.0,<8; python_version < '3.10'`。要在 Windows 上安装 `colorama`（但在其他平台上省略），请使用
`colorama >=0.4.6,<5; platform_system == "Windows"`。

标记使用 `and`、`or` 和括号组合，例如
`aiohttp >=3.7.4,<4; (sys_platform != 'win32' or implementation_name != 'pypy') and python_version >= '3.10'`。
请注意，标记内的版本必须用引号括起来，而标记_外部_的版本_不能_用引号括起来。
