---
title: 配置项目
subtitle: Configuring projects
description: 学习如何配置 Python 项目，包括设置 Python 版本要求、定义入口点（如命令行界面和图形用户界面），管理项目依赖项，以及构建系统配置。完整指南帮助您确保项目在不同 Python 环境中正确运行。
---

# 配置项目

## Python 版本要求 {#python-version-requirement}

项目可以在 `pyproject.toml` 的 `project.requires-python` 字段中声明项目支持的 Python 版本。

建议设置 `requires-python` 值：

```toml title="pyproject.toml" hl_lines="4"
[project]
name = "example"
version = "0.1.0"
requires-python = ">=3.12"
```

Python 版本要求决定了项目中允许使用的 Python 语法，并影响依赖项版本的选择（这些依赖项必须支持相同的 Python 版本范围）。

## 入口点 {#entry-points}

[入口点](https://packaging.python.org/en/latest/specifications/entry-points/#entry-points)（Entry Points）是已安装包对外暴露接口的官方术语。包括：

- [命令行界面](#command-line-interfaces)
- [图形用户界面](#graphical-user-interfaces)
- [插件入口点](#plugin-entry-points)

!!! important

    使用入口点表格需要先定义[构建系统](#build-systems)。

### 命令行界面 {#command-line-interfaces}

项目可以在 `pyproject.toml` 的 `[project.scripts]` 表格中为项目定义命令行界面（CLI）。

例如，要声明一个名为 `hello` 的命令，调用 `example` 模块中的 `hello` 函数：

```toml title="pyproject.toml"
[project.scripts]
hello = "example:hello"
```

然后，可以在控制台中运行该命令：

```console
$ uv run hello
```

### 图形用户界面 {#graphical-user-interfaces}

项目可以在 `pyproject.toml` 的 `[project.gui-scripts]` 表格中为项目定义图形用户界面（GUI）。

!!! important

    这些仅在 Windows 上与[命令行界面](#command-line-interfaces)有所不同，在 Windows 上它们由 GUI 可执行文件包装，因此可以在没有控制台的情况下启动。在其他平台上，它们的行为相同。

例如，要声明一个名为 `hello` 的命令，调用 `example` 模块中的 `app` 函数：

```toml title="pyproject.toml"
[project.gui-scripts]
hello = "example:app"
```

### 插件入口点 {#plugin-entry-points}

项目可以在 `pyproject.toml` 的 [`[project.entry-points]`](https://packaging.python.org/en/latest/guides/creating-and-discovering-plugins/#using-package-metadata) 表格中定义用于插件发现的入口点。

例如，要将 `example-plugin-a` 包注册为 `example` 的插件：

```toml title="pyproject.toml"
[project.entry-points.'example.plugins']
a = "example_plugin_a"
```

然后，在 `example` 中，可以通过以下方式加载插件：

```python title="example/__init__.py"
from importlib.metadata import entry_points

for plugin in entry_points(group='example.plugins'):
    plugin.load()
```

!!! note

    `group` 键可以是任意值，不需要包含包名或 "plugins"。但是，建议使用包名作为键的命名空间，以避免与其他包冲突。

## 构建系统 {#build-systems}

构建系统决定项目应如何打包和安装。项目可以在 `pyproject.toml` 的 `[build-system]` 表格中声明和配置构建系统。

uv 通过是否存在构建系统来判断项目是否包含应安装到项目虚拟环境中的包。如果未定义构建系统，uv 将不会尝试构建或安装项目本身，仅安装其依赖项。如果定义了构建系统，uv 将构建项目并将其安装到项目环境中。

可以在 `uv init` 时使用 `--build-backend` 选项来创建具有适当布局的打包项目。可以在 `uv init` 时使用 `--package` 选项来创建使用默认构建系统的打包项目。

!!! note

    虽然 uv 在没有构建系统定义的情况下不会构建和安装当前项目，但其他包并不要求必须有 `[build-system]` 表格。出于历史原因，如果未定义构建系统，则使用 `setuptools.build_meta:__legacy__` 来构建包。您依赖的包可能没有显式声明其构建系统，但仍然可以安装。同样，如果您[添加了对本地项目的依赖](./dependencies.md#path)或使用 `uv pip` 安装它，无论是否存在 `[build-system]` 表格，uv 都会尝试构建和安装它。

构建系统用于支持以下功能：

- 在分发中包含或排除文件
- 可编辑安装行为
- 动态项目元数据
- 原生代码编译
- 内置共享库

要配置这些功能，请参阅您所选构建系统的文档。

## 项目打包 {#project-packaging}

正如[构建系统](#build-systems)中所述，Python 项目必须先构建才能安装。这个过程通常被称为"打包"。

如果您想要以下功能，可能需要一个包：

- 为项目添加命令
- 将项目分发给他人
- 使用 `src` 和 `test` 布局
- 编写库

如果您正在进行以下操作，可能*不需要*包：

- 编写脚本
- 构建简单应用程序
- 使用扁平布局

虽然 uv 通常通过[构建系统](#build-systems)的声明来判断项目是否应打包，但 uv 也允许通过 [`tool.uv.package`](../../reference/settings.md#package) 设置来覆盖此行为。

设置 `tool.uv.package = true` 将强制项目被构建并安装到项目环境中。如果未定义构建系统，uv 将使用 setuptools 的旧版后端。

设置 `tool.uv.package = false` 将强制项目包*不*被构建和安装到项目环境中。uv 在与项目交互时将忽略已声明的构建系统；但是，uv 仍会响应显式的构建项目请求，例如调用 `uv build`。

## 项目环境路径 {#project-environment-path}

`UV_PROJECT_ENVIRONMENT` 环境变量可用于配置项目虚拟环境路径（默认为 `.venv`）。

如果提供相对路径，它将相对于工作区根目录进行解析。如果提供绝对路径，将按原样使用，即不会为环境创建子目录。如果提供的路径上不存在环境，uv 将创建它。

此选项可用于写入系统 Python 环境，但不推荐这样做。`uv sync` 默认会从环境中移除多余的包，因此可能导致系统处于损坏状态。

要定位系统环境，请将 `UV_PROJECT_ENVIRONMENT` 设置为 Python 安装的前缀。例如，在基于 Debian 的系统上，通常是 `/usr/local`：

```console
$ python -c "import sysconfig; print(sysconfig.get_config_var('prefix'))"
/usr/local
```

要定位此环境，您可以导出 `UV_PROJECT_ENVIRONMENT=/usr/local`。

!!! important

    如果提供绝对路径且该设置在多个项目中使用，则每个项目的调用都会覆盖该环境。此设置仅建议在 CI 或 Docker 镜像中用于单个项目。

!!! note

    默认情况下，uv 在项目操作期间不会读取 `VIRTUAL_ENV` 环境变量。如果 `VIRTUAL_ENV` 设置为与项目环境不同的路径，将显示警告。可以使用 `--active` 标志来选择遵循 `VIRTUAL_ENV`。可以使用 `--no-active` 标志来消除警告。

## 构建隔离 {#build-isolation}

默认情况下，uv 根据 [PEP 517](https://peps.python.org/pep-0517/) 的规定，在隔离的虚拟环境中构建所有包，并附带其声明的构建依赖项。

有些包与此构建隔离方式不兼容，无论是有意还是无意。

例如，[`flash-attn`](https://pypi.org/project/flash-attn/) 和 [`deepspeed`](https://pypi.org/project/deepspeed/) 等包需要基于项目环境中安装的相同 PyTorch 版本来构建；在隔离环境中构建它们时，可能会无意中基于不同版本的 PyTorch 构建，从而导致运行时错误。

在其他情况下，包可能在其声明的构建依赖项列表中意外遗漏了必要的依赖项。例如，[`cchardet`](https://pypi.org/project/cchardet/) 在安装前需要项目环境中已安装 `cython`，但未将其声明为构建依赖项。

为解决这些问题，uv 支持两种独立的方法来修改构建隔离行为：

1. **扩充构建依赖项列表**：这允许您通过 [`extra-build-dependencies`](../../reference/settings.md#extra-build-dependencies) 设置在隔离环境中安装包，但附带包本身未声明的额外构建依赖项。对于 `flash-attn` 等包，您甚至可以强制要求这些构建依赖项（如 `torch`）与项目环境中已安装或将安装的包版本匹配。

1. **为特定包禁用构建隔离**：这允许您安装包时不在隔离环境中构建它。

在可能的情况下，我们建议扩充构建依赖项而非完全禁用构建隔离，因为后一种方法要求在安装包*之前*将构建依赖项安装到项目环境中，这可能导致更复杂的安装步骤、项目环境中包含多余的包，以及在其他环境中难以重现项目环境。

### 扩充构建依赖项 {#augmenting-build-dependencies}

要为特定包扩充构建依赖项列表，请将其添加到 `pyproject.toml` 中的 [`extra-build-dependencies`](../../reference/settings.md#extra-build-dependencies) 列表。

例如，要构建 `cchardet` 并添加 `cython` 作为额外的构建依赖项，请在 `pyproject.toml` 中包含以下内容：

```toml title="pyproject.toml"
[project]
name = "project"
version = "0.1.0"
description = "..."
readme = "README.md"
requires-python = ">=3.12"
dependencies = ["cchardet"]

[tool.uv.extra-build-dependencies]
cchardet = ["cython"]
```

要确保构建依赖项与项目环境中已安装或将安装的包版本匹配，请在 `extra-build-dependencies` 表格中设置 `match-runtime = true`。例如，要构建 `deepspeed` 并添加 `torch` 作为额外的构建依赖项，请在 `pyproject.toml` 中包含以下内容：

```toml title="pyproject.toml"
[project]
name = "project"
version = "0.1.0"
description = "..."
readme = "README.md"
requires-python = ">=3.12"
dependencies = ["deepspeed", "torch"]

[tool.uv.extra-build-dependencies]
deepspeed = [{ requirement = "torch", match-runtime = true }]
```

这将确保 `deepspeed` 使用与项目环境中安装的相同版本的 `torch` 进行构建。

同样，要构建 `flash-attn` 并添加 `torch` 作为额外的构建依赖项，请在 `pyproject.toml` 中包含以下内容：

```toml title="pyproject.toml"
[project]
name = "project"
version = "0.1.0"
description = "..."
readme = "README.md"
requires-python = ">=3.12"
dependencies = ["flash-attn", "torch"]

[tool.uv.extra-build-dependencies]
flash-attn = [{ requirement = "torch", match-runtime = true }]

[tool.uv.extra-build-variables]
flash-attn = { FLASH_ATTENTION_SKIP_CUDA_BUILD = "TRUE" }
```

!!! note

    `FLASH_ATTENTION_SKIP_CUDA_BUILD` 环境变量使 `flash-attn` 能够从预构建的 wheel 中解析，而不是尝试从源代码构建，后者需要访问 CUDA 开发工具包。

    如果在解析期间 CUDA 工具包可用，我们建议省略 `FLASH_ATTENTION_SKIP_CUDA_BUILD` 变量，因为将 `FLASH_ATTENTION_SKIP_CUDA_BUILD` 设置为 `TRUE` 时，如果没有针对目标 PyTorch 版本、GPU 版本和平台的兼容预构建 wheel，可能导致安装不兼容。

同样，[`deep_gemm`](https://github.com/deepseek-ai/DeepGEMM) 遵循相同的模式：

```toml title="pyproject.toml"
[project]
name = "project"
version = "0.1.0"
description = "..."
readme = "README.md"
requires-python = ">=3.12"
dependencies = ["deep_gemm", "torch"]

[tool.uv.sources]
deep_gemm = { git = "https://github.com/deepseek-ai/DeepGEMM" }

[tool.uv.extra-build-dependencies]
deep_gemm = [{ requirement = "torch", match-runtime = true }]
```

`extra-build-dependencies` 和 `extra-build-variables` 的使用会被 uv 缓存跟踪，因此对这些设置的更改将触发受影响包的重新安装和重新构建。例如，在 `flash-attn` 的情况下，升级项目中使用的 `torch` 版本将随后触发使用新版本 `torch` 重新构建 `flash-attn`。

#### 动态元数据 {#dynamic-metadata}

`match-runtime = true` 仅适用于声明了静态元数据的包，如 `flash-attn`。如果静态元数据不可用，uv 需要在依赖项解析阶段构建包；因此，uv 无法确定最终将安装到项目环境中的构建依赖项版本。

换句话说，如果 `flash-attn` 没有声明静态元数据，uv 将无法确定将安装到项目环境中的 `torch` 版本，因为它需要在解析 `torch` 版本之前构建 `flash-attn`。

举一个具体的例子，[`axolotl`](https://pypi.org/project/axolotl/) 是一个流行的包，需要扩充构建依赖项，但没有声明静态元数据，因为该包的依赖项会根据项目环境中安装的 `torch` 版本而变化。在这种情况下，用户应指定他们打算在项目中使用的确切 `torch` 版本，然后用该版本扩充构建依赖项。

例如，要基于 `torch==2.6.0` 构建 `axolotl`，请在 `pyproject.toml` 中包含以下内容：

```toml title="pyproject.toml"
[project]
name = "project"
version = "0.1.0"
description = "..."
readme = "README.md"
requires-python = ">=3.12"
dependencies = ["axolotl[deepspeed, flash-attn]", "torch==2.6.0"]

[tool.uv.extra-build-dependencies]
axolotl = ["torch==2.6.0"]
deepspeed = ["torch==2.6.0"]
flash-attn = ["torch==2.6.0"]
```

同样，旧版本的 `flash-attn` 没有声明静态元数据，因此开箱即用不支持 `match-runtime = true`。但与 `axolotl` 不同的是，`flash-attn` 不会根据构建环境的动态属性来改变其依赖项。因此，用户可以通过 [`dependency-metadata`](../../reference/settings.md#dependency-metadata) 设置预先提供 `flash-attn` 元数据，从而避免在依赖项解析阶段构建包。例如，要预先提供 `flash-attn` 元数据：

```toml title="pyproject.toml"
[[tool.uv.dependency-metadata]]
name = "flash-attn"
version = "2.6.3"
requires-dist = ["torch", "einops"]
```

!!! tip

    要确定 `flash-attn` 等包的包元数据，请导航到相应的 Git 仓库，或在 [PyPI](https://pypi.org/project/flash-attn) 上查找并下载包的源代码分发版。包的要求通常可以在 `setup.py` 或 `setup.cfg` 文件中找到。

    （如果包包含构建分发版，您可以解压它以找到 `METADATA` 文件；但是，构建分发版的存在本身就意味着不需要预先提供元数据，因为 uv 已经可以使用它。）

    `tool.uv.dependency-metadata` 中的 `version` 字段对于基于注册表的依赖项是可选的（省略时，uv 将假定元数据适用于包的所有版本），但对于直接 URL 依赖项（如 Git 依赖项）是*必需的*。

### 禁用构建隔离 {#disabling-build-isolation}

在不禁用构建隔离的情况下安装包要求在构建包*之前*将包的构建依赖项安装到项目环境中。

例如，历史上，要在不禁用构建隔离的情况下安装 `cchardet`，您首先需要在项目环境中安装 `cython` 和 `setuptools` 包，然后单独调用以在不禁用构建隔离的情况下安装 `cchardet`：

```console
$ uv venv
$ uv pip install cython setuptools
$ uv pip install cchardet --no-build-isolation
```

uv 通过允许您通过 `pyproject.toml` 中的 `no-build-isolation-package` 设置和命令行中的 `--no-build-isolation-package` 标志来指定不应在隔离环境中构建的包，从而简化了此过程。此外，当某个包被标记为禁用构建隔离时，uv 将执行两阶段安装，首先安装支持构建隔离的包，然后安装不支持构建隔离的包。因此，如果项目的构建依赖项包含在项目依赖项中，uv 将在安装需要禁用构建隔离的包之前自动安装它们。

例如，要在不禁用构建隔离的情况下安装 `cchardet`，请在 `pyproject.toml` 中包含以下内容：

```toml title="pyproject.toml"
[project]
name = "project"
version = "0.1.0"
description = "..."
readme = "README.md"
requires-python = ">=3.12"
dependencies = ["cchardet", "cython", "setuptools"]

[tool.uv]
no-build-isolation-package = ["cchardet"]
```

运行 `uv sync` 时，uv 将首先在项目环境中安装 `cython` 和 `setuptools`，然后安装 `cchardet`（不使用构建隔离）：

```console
$ uv sync --extra build
 + cchardet==2.1.7
 + cython==3.1.3
 + setuptools==80.9.0
```

同样，要在不禁用构建隔离的情况下安装 `flash-attn`，请在 `pyproject.toml` 中包含以下内容：

```toml title="pyproject.toml"
[project]
name = "project"
version = "0.1.0"
description = "..."
readme = "README.md"
requires-python = ">=3.12"
dependencies = ["flash-attn", "torch"]

[tool.uv]
no-build-isolation-package = ["flash-attn"]
```

运行 `uv sync` 时，uv 将首先在项目环境中安装 `torch`，然后安装 `flash-attn`（不使用构建隔离）。由于 `torch` 既是项目依赖项又是构建依赖项，因此 `torch` 的版本在构建和运行时环境之间保证一致。

上述方法的一个缺点是它要求将构建依赖项安装到项目环境中，这对 `flash-attn`（在构建时和运行时都需要 `torch`）来说是合适的，但对 `cchardet`（仅在构建时需要 `cython`）来说不合适。

为避免将构建依赖项包含在项目环境中，uv 支持两步安装过程，允许您将构建依赖项与需要它们的包分开。

例如，`cchardet` 的构建依赖项可以隔离到一个可选的 `build` 组中，如下所示：

```toml title="pyproject.toml"
[project]
name = "project"
version = "0.1.0"
description = "..."
readme = "README.md"
requires-python = ">=3.12"
dependencies = ["cchardet"]

[project.optional-dependencies]
build = ["setuptools", "cython"]

[tool.uv]
no-build-isolation-package = ["cchardet"]
```

基于上述配置，用户首先使用 `build` 可选组进行同步，然后不带该组同步以移除构建依赖项：

```console
$ uv sync --extra build
 + cchardet==2.1.7
 + cython==3.1.3
 + setuptools==80.9.0
$ uv sync
 - cython==3.1.3
 - setuptools==80.9.0
```

有些包（如 `cchardet`）仅在 `uv sync` 的*安装*阶段需要构建依赖项。而其他包甚至在*解析*阶段就需要构建依赖项存在才能解析项目的依赖项。

在这种情况下，可以在运行任何 `uv lock` 或 `uv sync` 命令之前，使用更底层的 `uv pip` API 安装构建依赖项。例如，给定：

```toml title="pyproject.toml"
[project]
name = "project"
version = "0.1.0"
description = "..."
readme = "README.md"
requires-python = ">=3.12"
dependencies = ["flash-attn"]

[tool.uv]
no-build-isolation-package = ["flash-attn"]
```

您可以运行以下命令序列来同步 `flash-attn`：

```console
$ uv venv
$ uv pip install torch setuptools
$ uv sync
```

或者，用户可以通过 [`dependency-metadata`](../../reference/settings.md#dependency-metadata) 设置预先提供 `flash-attn` 元数据，从而避免在依赖项解析阶段构建包。例如，要预先提供 `flash-attn` 元数据：

```toml title="pyproject.toml"
[[tool.uv.dependency-metadata]]
name = "flash-attn"
version = "2.6.3"
requires-dist = ["torch", "einops"]
```

## 可编辑模式 {#editable-mode}

默认情况下，项目将以可编辑模式安装，这样对源代码的更改会立即反映在环境中。`uv sync` 和 `uv run` 都接受 `--no-editable` 标志，指示 uv 以非可编辑模式安装项目。`--no-editable` 适用于部署场景，例如构建 Docker 容器，在这种场景中，项目应包含在部署环境中，而不依赖于原始源代码。

## 冲突依赖项 {#conflicting-dependencies}

uv 会一起解析所有项目依赖项，包括可选依赖项（"extras"）和依赖项组。如果在一个部分中声明的依赖项与另一个部分中的不兼容，uv 将无法解析项目的要求并报错。

uv 支持显式声明冲突的依赖项组。例如，要声明 `optional-dependency` 组 `extra1` 和 `extra2` 不兼容：

```toml title="pyproject.toml"
[tool.uv]
conflicts = [
    [
      { extra = "extra1" },
      { extra = "extra2" },
    ],
]
```

或者，要声明开发依赖项组 `group1` 和 `group2` 不兼容：

```toml title="pyproject.toml"
[tool.uv]
conflicts = [
    [
      { group = "group1" },
      { group = "group2" },
    ],
]
```

更多信息请参阅[解析文档](../resolution.md#conflicting-dependencies)。

## 受限解析环境 {#limited-resolution-environments}

如果您的项目支持更有限的平台或 Python 版本集合，您可以通过 `environments` 设置来约束已解析的平台集合，该设置接受 PEP 508 环境标记列表。例如，要将锁定文件约束到 macOS 和 Linux，并排除 Windows：

```toml title="pyproject.toml"
[tool.uv]
environments = [
    "sys_platform == 'darwin'",
    "sys_platform == 'linux'",
]
```

更多信息请参阅[解析文档](../resolution.md#limited-resolution-environments)。

## 必需环境 {#required-environments}

如果您的项目*必须*支持特定平台或 Python 版本，您可以通过 `required-environments` 设置将该平台标记为必需。例如，要求项目支持 Intel macOS：

```toml title="pyproject.toml"
[tool.uv]
required-environments = [
    "sys_platform == 'darwin' and platform_machine == 'x86_64'",
]
```

`required-environments` 设置仅适用于不发布源代码分发版的包（如 PyTorch），因为此类包*只能*在该包发布的预构建二进制分发版（wheel）集合所覆盖的环境中安装。

更多信息请参阅[解析文档](../resolution.md#required-environments)。
