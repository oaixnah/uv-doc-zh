---
subtitle: Python versions
description: 学习uv支持的Python版本，包括uv管理的Python和系统Python。了解如何请求特定的Python版本，以及uv如何处理不同的Python实现。完整指南帮助您了解uv的Python版本支持。
---

# Python 版本

一个 Python 版本由一个 Python 解释器（即 `python` 可执行文件）、标准库和其他支持文件组成。

## uv 管理的 Python 和系统 Python

由于系统上通常已存在 Python 安装，uv 支持[发现](./python-versions.md#python_8) Python 版本。但是，uv 也支持自行[安装 Python 版本](./python-versions.md#python_2)。为了区分这两种类型的 Python 安装，uv 将其安装的 Python 版本称为 _uv 管理的_ Python 安装，而将所有其他 Python 安装称为 _系统_ Python 安装。

!!! note

    uv 不区分由操作系统安装的 Python 版本与由其他工具安装和管理的 Python 版本。例如，如果一个 Python 安装由 `pyenv` 管理，在 uv 中它仍被视为_系统_ Python 版本。

## 请求一个版本

在大多数 uv 命令中，可以使用 `--python` 标志请求特定的 Python 版本。例如，在创建虚拟环境时：

```console
$ uv venv --python 3.11.6
```

uv 将确保 Python 3.11.6 可用——必要时会下载并安装它——然后用它创建虚拟环境。

支持以下 Python 版本请求格式：

- `<version>` (例如, `3`, `3.12`, `3.12.3`)
- `<version-specifier>` (例如, `>=3.12,<3.13`)
- `<implementation>` (例如, `cpython` 或 `cp`)
- `<implementation>@<version>` (例如, `cpython@3.12`)
- `<implementation><version>` (例如, `cpython3.12` 或 `cp312`)
- `<implementation><version-specifier>` (例如, `cpython>=3.12,<3.13`)
- `<implementation>-<version>-<os>-<arch>-<libc>` (例如, `cpython-3.12.3-macos-aarch64-none`)

此外，可以使用以下方式请求特定的系统 Python 解释器：

- `<executable-path>` (例如, `/opt/homebrew/bin/python3`)
- `<executable-name>` (例如, `mypython3`)
- `<install-dir>` (例如, `/some/environment/`)

默认情况下，如果在系统上找不到 Python 版本，uv 将自动下载。此行为可以通过 [禁用 `python-downloads` 选项](./python-versions.md#python_10)禁用。

### Python 版本文件

`.python-version` 文件可用于创建默认的 Python 版本请求。uv 在工作目录及其每个父目录中搜索 `.python-version` 文件。如果未找到，uv 将检查用户级配置目录。可以使用上述任何请求格式，但建议使用版本号以便与其他工具互操作。

可以使用 [`uv python pin`](../reference/cli/python.md#pin) 命令在当前目录中创建 `.python-version` 文件。

可以使用 [`uv python pin --global`](../reference/cli/python.md#pin) 命令在用户配置目录中创建全局 `.python-version` 文件。

可以使用 `--no-config` 禁用对 `.python-version` 文件的发现。

uv 不会超出项目或工作区边界搜索 `.python-version` 文件（用户配置目录除外）。

## 安装 Python 版本

uv 捆绑了适用于 macOS、Linux 和 Windows 的可下载 CPython 和 PyPy 发行版列表。

!!! tip

    默认情况下，Python 版本会根据需要自动下载，而无需使用 `uv python install`。

要安装特定版本的 Python：

```console
$ uv python install 3.12.3
```

要安装最新的补丁版本：

```console
$ uv python install 3.12
```

要安装满足约束的版本：

```console
$ uv python install '>=3.8,<3.10'
```

要安装多个版本：

```console
$ uv python install 3.9 3.10 3.11
```

要安装特定的实现：

```console
$ uv python install pypy
```

除了用于请求本地解释器（如文件路径）的格式外，所有[Python 版本请求](./python-versions.md#_1)格式都受支持。

默认情况下，`uv python install` 将验证是否已安装 uv 管理的 Python 版本，或安装最新版本。如果存在 `.python-version` 文件，uv 将安装文件中列出的 Python 版本。需要多个 Python 版本的项目可以定义一个 `.python-versions` 文件。如果存在，uv 将安装文件中列出的所有 Python 版本。

!!! important

    每个 uv 版本可用的 Python 版本是固定的。要安装新的 Python 版本，您可能需要升级 uv。

### 安装 Python 可执行文件

!!! important

    对安装 Python 可执行文件的支持处于_预览_阶段。这意味着其行为是实验性的，可能会发生变化。

要将 Python 可执行文件安装到您的 `PATH` 中，请提供 `--preview` 选项：

```console
$ uv python install 3.12 --preview
```

这会将所请求版本的 Python 可执行文件安装到 `~/.local/bin` 中，例如 `python3.12`。

!!! tip

    如果 `~/.local/bin` 不在您的 `PATH` 中，您可以使用 `uv tool update-shell` 添加它。

要安装 `python` 和 `python3` 可执行文件，请包含 `--default` 选项：

```console
$ uv python install 3.12 --default --preview
```

安装 Python 可执行文件时，uv 仅在现有可执行文件由 uv 管理时才会覆盖它——例如，如果 `~/.local/bin/python3.12` 已存在，uv 不会在没有 `--force` 标志的情况下覆盖它。

uv 会更新它管理的可执行文件。但是，默认情况下，它会偏好每个 Python 次要版本的最新补丁版本。例如：

```console
$ uv python install 3.12.7 --preview  # 将 `python3.12` 添加到 `~/.local/bin`
$ uv python install 3.12.6 --preview  # 不更新 `python3.12`
$ uv python install 3.12.8 --preview  # 将 `python3.12` 更新为指向 3.12.8
```

## 升级 Python 版本

!!! important

    对升级 Python 版本的支持处于_预览_阶段。这意味着其行为是实验性的，可能会发生变化。

    仅支持对 uv 管理的 Python 版本进行升级。

    目前不支持对 PyPy 和 GraalPy 进行升级。

uv 允许将 Python 版本透明地升级到最新的补丁版本，例如从 3.13.4 升级到 3.13.5。uv 不允许跨 Python 次要版本进行透明升级，例如从 3.12 升级到 3.13，因为更改次要版本会影响依赖项解析。

可以使用 `python upgrade` 命令将 uv 管理的 Python 版本升级到最新的受支持补丁版本：

要将 Python 版本升级到最新的受支持补丁版本：

```console
$ uv python upgrade 3.12
```

要升级所有已安装的 Python 版本：

```console
$ uv python upgrade
```

升级后，uv 会偏好新版本，但会保留现有版本，因为它可能仍被虚拟环境使用。

如果 Python 版本是使用预览模式安装的，例如 `uv python install 3.12 --preview`，使用该 Python 版本的虚拟环境将自动升级到新的补丁版本。

!!! note

    如果在选择加入预览模式_之前_创建了虚拟环境，它将不会被包含在自动升级中。

如果虚拟环境是使用明确请求的补丁版本创建的，例如 `uv venv -p 3.10.8`，它将不会被透明地升级到新版本。

### 次要版本目录

虚拟环境的自动升级是通过使用带有 Python 次要版本的目录来实现的，例如：

```
~/.local/share/uv/python/cpython-3.12-macos-aarch64-none
```

它是一个指向特定补丁版本的符号链接（在 Unix 上）或连接点（在 Windows 上）：

```console
$ readlink ~/.local/share/uv/python/cpython-3.12-macos-aarch64-none
~/.local/share/uv/python/cpython-3.12.11-macos-aarch64-none
```

如果此链接被其他工具解析，例如通过规范化 Python 解释器路径，并用于创建虚拟环境，它将不会被自动升级。

## 项目 Python 版本

在项目命令调用期间，uv 将遵守 `pyproject.toml` 文件中 `requires-python` 定义的 Python 要求。将使用与要求兼容的第一个 Python 版本，除非另有请求，例如通过 `.python-version` 文件或 `--python` 标志。

## 查看可用的 Python 版本

要列出已安装和可用的 Python 版本：

```console
$ uv python list
```

要筛选 Python 版本，请提供一个请求，例如显示所有 Python 3.13 解释器：

```console
$ uv python list 3.13
```

或者，显示所有 PyPy 解释器：

```console
$ uv python list pypy
```

默认情况下，其他平台的下载和旧的补丁版本是隐藏的。

要查看所有版本：

```console
$ uv python list --all-versions
```

要查看其他平台的 Python 版本：

```console
$ uv python list --all-platforms
```

要排除下载并仅显示已安装的 Python 版本：

```console
$ uv python list --only-installed
```

有关更多详细信息，请参阅 [`uv python list`](../reference/cli/python.md#list) 参考。

## 查找 Python 可执行文件

要查找 Python 可执行文件，请使用 `uv python find` 命令：

```console
$ uv python find
```

默认情况下，这将显示第一个可用 Python 可执行文件的路径。有关如何发现可执行文件的详细信息，请参阅[发现规则](./python-versions.md#python_6)。

此接口还支持许多[请求格式](./python-versions.md#_1)，例如查找版本为 3.11 或更新的 Python 可执行文件：

```console
$ uv python find '>=3.11'
```

默认情况下，`uv python find` 将包含来自虚拟环境的 Python 版本。如果在工作目录或任何父目录中找到 `.venv` 目录，或者设置了 `VIRTUAL_ENV` 环境变量，它将优先于 `PATH` 上的任何 Python 可执行文件。

要忽略虚拟环境，请使用 `--system` 标志：

```console
$ uv python find --system
```

## 发现 Python 版本

搜索 Python 版本时，会检查以下位置：

- `UV_PYTHON_INSTALL_DIR` 中的 uv 管理的 Python 安装。
- `PATH` 上的 Python 解释器，在 macOS 和 Linux 上为 `python`、`python3` 或 `python3.x`，在 Windows 上为 `python.exe`。
- 在 Windows 上，Windows 注册表中的 Python 解释器和 Microsoft Store Python 解释器（请参阅 `py --list-paths`）与请求的版本匹配。

在某些情况下，uv 允许使用来自虚拟环境的 Python 版本。在这种情况下，将在搜索上述安装之前检查虚拟环境的解释器是否与请求兼容。有关详细信息，请参阅 [pip 兼容的虚拟环境发现](../pip/environments.md#python_2)文档。

执行发现时，将忽略非可执行文件。查询每个发现的可执行文件的元数据，以确保其满足[请求的 Python 版本](./python-versions.md#_1)。如果查询失败，将跳过该可执行文件。如果可执行文件满足请求，则使用它而不检查其他可执行文件。

搜索 uv 管理的 Python 版本时，uv 会优先选择较新的版本。搜索系统 Python 版本时，uv 将使用第一个兼容的版本，而不是最新的版本。

如果在系统上找不到 Python 版本，uv 将检查是否有兼容的 uv 管理的 Python 版本可供下载。

### Python 预发布版本

默认情况下不会选择 Python 预发布版本。如果没有其他可用的安装匹配请求，则将使用 Python 预发布版本。例如，如果只有预发布版本可用，则将使用它，否则将使用稳定版本。同样，如果提供了预发布 Python 可执行文件的路径，则没有其他 Python 版本匹配请求，将使用预发布版本。

如果可用的预发布 Python 版本与请求匹配，uv 不会下载稳定的 Python 版本。

## 禁用自动 Python 下载

默认情况下，uv 会在需要时自动下载 Python 版本。

可以使用 [`python-downloads`](../reference/settings/configuration.md#python-downloads) 选项禁用此行为。默认情况下，它设置为 `automatic`；设置为 `manual` 以仅在 `uv python install` 期间允许 Python 下载。

!!! tip "提示"

    可以在[持久配置文件](./configuration-files.md)中设置 `python-downloads` 设置以更改默认行为，或者可以将 `--no-python-downloads` 标志传递给任何 uv 命令。

## 要求或禁用 uv 管理的 Python 版本

默认情况下，uv 会尝试使用系统上找到的 Python 版本，仅在必要时下载 uv 管理的 Python 版本。要忽略系统 Python 版本，仅使用 uv 管理的 Python 版本，请使用 `--managed-python` 标志：

```console
$ uv python list --managed-python
```

同样，要忽略 uv 管理的 Python 版本，仅使用系统 Python 版本，请使用 `--no-managed-python` 标志：

```console
$ uv python list --no-managed-python
```

要在配置文件中更改 uv 的默认行为，请使用 [`python-preference` 设置](./python-versions.md#python_11)。

## 调整 Python 版本偏好

[`python-preference`](../reference/settings/configuration.md#python-preference) 设置决定是偏好使用系统上已有的 Python 安装，还是由 uv 下载和安装的 Python 安装。

默认情况下，`python-preference` 设置为 `managed`，它偏好 uv 管理的 Python 安装而不是系统 Python 安装。但是，系统 Python 安装仍然优先于下载 uv 管理的 Python 版本。

提供以下备用选项：

- `only-managed`：仅使用 uv 管理的 Python 安装；从不使用系统 Python 安装。等效于 `--managed-python`。
- `system`：偏好系统 Python 安装而不是 uv 管理的 Python 安装。
- `only-system`：仅使用系统 Python 安装；从不使用 uv 管理的 Python 安装。等效于 `--no-managed-python`。

!!! note

    可以在不更改偏好的情况下[禁用](./python-versions.md#python_10)自动 Python 版本下载。

## Python 实现支持

uv 支持 CPython、PyPy 和 GraalPy Python 实现。如果不支持某个 Python 实现，uv 将无法发现其解释器。

可以使用长名称或短名称请求实现：

- CPython: `cpython`, `cp`
- PyPy: `pypy`, `pp`
- GraalPy: `graalpy`, `gp`

实现名称请求不区分大小写。

有关支持格式的更多详细信息，请参阅[Python 版本请求](./python-versions.md#_1)文档。

## uv 管理的 Python 发行版

uv 支持下载和安装 CPython 和 PyPy 发行版。

### CPython 发行版

由于 Python 不发布官方的可分发 CPython 二进制文件，uv 转而使用来自 Astral [`python-build-standalone`](https://github.com/astral-sh/python-build-standalone) 项目的预构建发行版。`python-build-standalone` 也被许多其他 Python 项目使用，如 [Rye](https://github.com/astral-sh/rye)、[Mise](https://mise.jdx.dev/lang/python.html) 和 [bazelbuild/rules_python](https://github.com/bazelbuild/rules_python)。

uv Python 发行版是自包含、高度可移植且性能卓越的。虽然可以像 `pyenv` 等工具那样从源代码构建 Python，但这需要预安装的系统依赖项，并且创建优化的、高性能的构建（例如，启用 PGO 和 LTO）非常缓慢。

这些发行版存在一些行为怪癖，通常是可移植性的结果；有关详细信息，请参阅 [`python-build-standalone` 怪癖](https://gregoryszorc.com/docs/python-build-standalone/main/quirks.html)文档。此外，某些平台可能不受支持（例如，尚无适用于 ARM 上的 musl Linux 的发行版）。

### PyPy 发行版

PyPy 发行版由 PyPy 项目提供。
