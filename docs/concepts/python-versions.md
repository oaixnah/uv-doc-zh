---
subtitle: Python 版本
description: 学习uv支持的Python版本，包括uv管理的Python和系统Python。了解如何请求特定的Python版本，以及uv如何处理不同的Python实现。完整指南帮助您了解uv的Python版本支持。
---

# Python 版本 {#python-versions}

Python 版本由 Python 解释器（即 `python` 可执行文件）、标准库和其他支持文件组成。

## 托管安装和系统安装的 Python {#managed-and-system-python-installations}

由于系统通常已经存在 Python 安装，uv 支持[发现](#discovery-of-python-versions)Python 版本。然而，uv 也支持自行[安装 Python 版本](#installing-a-python-version)。为了区分这两种类型的 Python 安装，uv 将自身安装的 Python 版本称为**托管**（managed）Python 安装，而将所有其他 Python 安装称为**系统**（system）Python 安装。

!!! note

    uv 并不区分由操作系统安装的 Python 版本与由其他工具安装和管理的 Python 版本。例如，如果一个 Python 安装由 `pyenv` 管理，在 uv 中仍会被视为**系统** Python 版本。

## 请求版本 {#requesting-a-version}

在大多数 uv 命令中，可以通过 `--python` 标志来请求特定的 Python 版本。例如，在创建虚拟环境时：

```console
$ uv venv --python 3.11.6
```

uv 将确保 Python 3.11.6 可用——必要时会下载并安装——然后使用它创建虚拟环境。

支持以下 Python 版本请求格式：

- `<version>`（例如 `3`、`3.12`、`3.12.3`）
- `<version-specifier>`（例如 `>=3.12,<3.13`）
- `<version><short-variant>`（例如 `3.13t`、`3.12.0d`）
- `<version>+<variant>`（例如 `3.13+freethreaded`、`3.12.0+debug`、`3.14+gil`）
- `<implementation>`（例如 `cpython` 或 `cp`）
- `<implementation>@<version>`（例如 `cpython@3.12`）
- `<implementation><version>`（例如 `cpython3.12` 或 `cp312`）
- `<implementation><version-specifier>`（例如 `cpython>=3.12,<3.13`）
- `<implementation>-<version>-<os>-<arch>-<libc>`（例如 `cpython-3.12.3-macos-aarch64-none`）

此外，还可以通过以下方式请求特定的系统 Python 解释器：

- `<executable-path>`（例如 `/opt/homebrew/bin/python3`）
- `<executable-name>`（例如 `mypython3`）
- `<install-dir>`（例如 `/some/environment/`）

默认情况下，如果在系统上找不到 Python 版本，uv 将自动下载。可以通过
[`python-downloads` 选项禁用此行为](#disabling-automatic-python-downloads)。

### Python 版本文件 {#python-version-files}

`.python-version` 文件可用于创建默认的 Python 版本请求。uv 会在工作目录及其每个父目录中搜索 `.python-version` 文件。如果找不到，uv 将检查用户级配置目录。可以使用上述任何请求格式，但建议使用版本号以保持与其他工具的互操作性。

可以使用 [`uv python pin`](../reference/cli.md/#uv-python-pin) 命令在当前目录中创建 `.python-version` 文件。

可以使用 [`uv python pin --global`](../reference/cli.md/#uv-python-pin) 命令在用户配置目录中创建全局 `.python-version` 文件。

可以通过 `--no-config` 禁用 `.python-version` 文件的发现。

uv 不会在项目或工作区边界之外搜索 `.python-version` 文件（用户配置目录除外）。

## 安装 Python 版本 {#installing-a-python-version}

uv 内置了适用于 macOS、Linux 和 Windows 的可下载 CPython 和 PyPy 发行版列表。

!!! tip

    默认情况下，Python 版本会根据需要自动下载，无需使用 `uv python install`。

安装特定版本：

```console
$ uv python install 3.12.3
```

安装最新的补丁版本：

```console
$ uv python install 3.12
```

安装满足约束条件的版本：

```console
$ uv python install '>=3.8,<3.10'
```

安装多个版本：

```console
$ uv python install 3.9 3.10 3.11
```

安装特定实现：

```console
$ uv python install pypy
```

支持所有 [Python 版本请求](#requesting-a-version)格式，但用于请求本地解释器的格式（如文件路径）除外。

默认情况下，`uv python install` 会验证托管 Python 版本是否已安装，或安装最新版本。如果存在 `.python-version` 文件，uv 将安装该文件中列出的 Python 版本。需要多个 Python 版本的项目可以定义 `.python-versions` 文件。如果该文件存在，uv 将安装文件中列出的所有 Python 版本。

!!! important

    每个 uv 发行版中可用的 Python 版本是固定的。要安装新的 Python 版本，可能需要升级 uv。

有关已安装 Python 版本存储位置的详细信息，请参阅[存储文档](../reference/storage.md#python-versions)。

### 安装 Python 可执行文件 {#installing-python-executables}

uv 默认将 Python 可执行文件安装到你的 `PATH` 中，例如，在 Unix 上 `uv python install 3.12` 会将 Python 可执行文件安装到 `~/.local/bin`，文件名为 `python3.12`。有关目标目录的更多详细信息，请参阅[存储文档](../reference/storage.md#python-executables)。

!!! tip

    如果 `~/.local/bin` 不在你的 `PATH` 中，你可以使用 `uv python update-shell` 将其添加。

要安装 `python` 和 `python3` 可执行文件，请使用实验性的 `--default` 选项：

```console
$ uv python install 3.12 --default
```

安装 Python 可执行文件时，uv 仅会覆盖由 uv 管理的已有可执行文件——例如，如果 `~/.local/bin/python3.12` 已存在，uv 不会在没有 `--force` 标志的情况下覆盖它。

uv 会更新其管理下的可执行文件。但是，默认情况下它会优先选择每个 Python 次版本的最新补丁版本。例如：

```console
$ uv python install 3.12.7  # 将 `python3.12` 添加到 `~/.local/bin`
$ uv python install 3.12.6  # 不会更新 `python3.12`
$ uv python install 3.12.8  # 更新 `python3.12` 以指向 3.12.8
```

## 升级 Python 版本 {#upgrading-python-versions}

!!! important

    升级仅支持 uv 管理的 Python 版本。

    目前不支持 PyPy、GraalPy 和 Pyodide 的升级。

uv 允许将 Python 版本透明升级到最新的补丁版本，例如从 3.13.4 升级到 3.13.5。uv 不允许跨次版本透明升级，例如从 3.12 升级到 3.13，因为更改次版本可能会影响依赖解析。

可以使用 `python upgrade` 命令将 uv 管理的 Python 版本升级到最新的受支持补丁版本：

升级某个 Python 版本到最新的受支持补丁版本：

```console
$ uv python upgrade 3.12
```

升级所有已安装的 Python 版本：

```console
$ uv python upgrade
```

升级后，uv 会优先使用新版本，但会保留旧版本，因为虚拟环境可能仍在使用它。

使用该 Python 版本的虚拟环境将自动升级到新的补丁版本。

如果虚拟环境是使用显式指定的补丁版本创建的（例如 `uv venv -p 3.10.8`），则不会透明升级到新版本。

### 次版本目录 {#minor-version-directories}

虚拟环境的自动升级是通过使用 Python 次版本目录实现的，例如：

```
~/.local/share/uv/python/cpython-3.12-macos-aarch64-none
```

这是一个符号链接（Unix）或交接点（junction，Windows），指向特定的补丁版本：

```console
$ readlink ~/.local/share/uv/python/cpython-3.12-macos-aarch64-none
~/.local/share/uv/python/cpython-3.12.11-macos-aarch64-none
```

如果此链接被其他工具解析（例如通过规范化 Python 解释器路径）并用于创建虚拟环境，则不会自动升级。

## 项目 Python 版本 {#project-python-versions}

在执行项目命令时，uv 会遵循 `pyproject.toml` 文件中 `requires-python` 定义的 Python 要求。将使用与要求兼容的第一个 Python 版本，除非通过其他方式指定了版本，例如通过 `.python-version` 文件或 `--python` 标志。

## 查看可用的 Python 版本 {#viewing-available-python-versions}

列出已安装和可用的 Python 版本：

```console
$ uv python list
```

要筛选 Python 版本，请提供一个请求，例如显示所有 Python 3.13 解释器：

```console
$ uv python list 3.13
```

或者显示所有 PyPy 解释器：

```console
$ uv python list pypy
```

默认情况下，其他平台和旧补丁版本的下载项会被隐藏。

查看所有版本：

```console
$ uv python list --all-versions
```

查看其他平台的 Python 版本：

```console
$ uv python list --all-platforms
```

排除下载项，仅显示已安装的 Python 版本：

```console
$ uv python list --only-installed
```

更多详细信息，请参阅 [`uv python list`](../reference/cli.md#uv-python-list) 参考文档。

## 查找 Python 可执行文件 {#finding-a-python-executable}

要查找 Python 可执行文件，请使用 `uv python find` 命令：

```console
$ uv python find
```

默认情况下，这将显示第一个可用 Python 可执行文件的路径。有关可执行文件发现方式的详细信息，请参阅[发现规则](#discovery-of-python-versions)。

此接口也支持多种[请求格式](#requesting-a-version)，例如，查找版本为 3.11 或更新的 Python 可执行文件：

```console
$ uv python find '>=3.11'
```

默认情况下，`uv python find` 会包括来自虚拟环境的 Python 版本。如果在工作目录或其任何父目录中找到 `.venv` 目录，或者设置了 `VIRTUAL_ENV` 环境变量，它将优先于 `PATH` 上的任何 Python 可执行文件。

要忽略虚拟环境，请使用 `--system` 标志：

```console
$ uv python find --system
```

## Python 版本发现 {#discovery-of-python-versions}

搜索 Python 版本时，会检查以下位置：

- `UV_PYTHON_INSTALL_DIR` 中的托管 Python 安装。
- 在 macOS 和 Linux 的 `PATH` 中作为 `python`、`python3` 或 `python3.x`，或在 Windows 上作为 `python.exe` 的 Python 解释器。
- 在 Windows 上，Windows 注册表和 Microsoft Store 中与请求版本匹配的 Python 解释器（请参阅 `py --list-paths`）。

在某些情况下，uv 允许使用虚拟环境中的 Python 版本。在这种情况下，在按上述方式搜索安装之前，会先检查虚拟环境的解释器是否与请求兼容。详细信息请参阅[兼容 pip 的虚拟环境发现](../pip/environments.md#discovery-of-python-environments)文档。

执行发现时，非可执行文件会被忽略。每个发现的可执行文件都会被查询元数据，以确保其满足[请求的 Python 版本](#requesting-a-version)。如果查询失败，该可执行文件会被跳过。如果可执行文件满足请求要求，则直接使用而不再检查其他可执行文件。

搜索托管 Python 版本时，uv 会优先选择更新的版本。搜索系统 Python 版本时，uv 会使用第一个兼容版本——而不是最新版本。

如果在系统上找不到 Python 版本，uv 会检查是否可以下载兼容的托管 Python 版本。

## Python 预发布版本 {#python-pre-releases}

默认情况下不会选择 Python 预发布版本。只有当没有其他可用的安装匹配请求时，才会使用 Python 预发布版本。例如，如果只有预发布版本可用，则会使用它，否则会使用稳定发布版本。同理，如果提供了预发布 Python 可执行文件的路径，且没有其他 Python 版本匹配请求，则会使用该预发布版本。

如果已有可用的预发布 Python 版本匹配请求，uv 不会转而下载稳定版本。

## 无 GIL（Free-threaded）Python {#free-threaded-python}

uv 支持在 CPython 3.13+ 中发现和安装[无 GIL](https://docs.python.org/3.14/glossary.html#term-free-threading)（free-threaded）Python 变体。

对于 Python 3.13，默认不会选择无 GIL Python 版本。只有在显式请求时才会选择无 GIL Python 版本，例如使用 `3.13t` 或 `3.13+freethreaded`。

对于 Python 3.14+，uv 允许在无需显式指定的情况下使用无 GIL 的 Python 3.14+ 解释器。GIL 启用的 Python 构建版本仍会被优先选择，例如在执行 `uv python install 3.14` 安装时。但是，如果无 GIL 解释器在 `PATH` 上的位置先于 GIL 启用的构建版本，则会被使用。

如果系统上同时有无 GIL 和 GIL 启用的 Python 版本可用，并且希望在项目中要求使用 GIL 启用的变体，可以使用 `+gil` 变体说明符。

## Debug 调试 Python 变体 {#debug-python-variants}

uv 支持发现和安装 Python 的[调试构建](https://docs.python.org/3.14/using/configure.html#debug-build)（debug builds），即启用了调试断言的版本。

!!! important

    Python 的调试构建速度较慢，不适合一般用途。

当没有其他可用的安装匹配请求时，会使用调试构建。例如，如果只有调试版本可用，则会使用它，否则会使用稳定发布版本。同理，如果提供了调试 Python 可执行文件的路径，且没有其他 Python 版本匹配请求，则会使用该调试版本。

可以通过例如 `3.13d` 或 `3.13+debug` 显式请求 Python 的调试构建。

!!! note

    uv 安装的 CPython 版本通常会剥离调试符号以减小发行版大小。这些调试构建不会剥离调试符号，这在使用 C 级调试器调试 Python 进程时非常有用。

## 禁用自动 Python 下载 {#disabling-automatic-python-downloads}

默认情况下，uv 会在需要时自动下载 Python 版本。

[`python-downloads`](../reference/settings.md#python-downloads) 选项可用于禁用此行为。默认值为 `automatic`；设置为 `manual` 则只允许在 `uv python install` 期间下载 Python。

!!! tip

    `python-downloads` 设置可以在[持久化配置文件](./configuration-files.md)中设置以更改默认行为，或者可以将 `--no-python-downloads` 标志传递给任何 uv 命令。

## 要求或禁用托管 Python 版本 {#requiring-or-disabling-managed-python-versions}

默认情况下，uv 会尝试使用系统上找到的 Python 版本，仅在必要时下载托管 Python 版本。要忽略系统 Python 版本，仅使用托管 Python 版本，请使用 `--managed-python` 标志：

```console
$ uv python list --managed-python
```

类似地，要忽略托管 Python 版本，仅使用系统 Python 版本，请使用 `--no-managed-python` 标志：

```console
$ uv python list --no-managed-python
```

要在配置文件中更改 uv 的默认行为，请使用
[`python-preference` 设置](#adjusting-python-version-preferences)。

## 调整 Python 版本偏好 {#adjusting-python-version-preferences}

[`python-preference`](../reference/settings.md#python-preference) 设置决定是优先使用系统上已有的 Python 安装，还是 uv 下载和安装的版本。

默认情况下，`python-preference` 设置为 `managed`，即优先使用托管 Python 安装而非系统 Python 安装。但是，系统 Python 安装仍优先于下载新的托管 Python 版本。

以下替代选项可用：

- `only-managed`：仅使用托管 Python 安装，绝不使用系统 Python 安装。等同于 `--managed-python`。
- `system`：优先使用系统 Python 安装而非托管 Python 安装。
- `only-system`：仅使用系统 Python 安装，绝不使用托管 Python 安装。等同于 `--no-managed-python`。

!!! note

    可以在不更改偏好的情况下[禁用自动 Python 版本下载](#disabling-automatic-python-downloads)。

## Python 实现支持 {#python-implementation-support}

uv 支持 CPython、PyPy、Pyodide 和 GraalPy 等 Python 实现。如果 Python 实现不受支持，uv 将无法发现其解释器。

可以使用长名称或短名称请求这些实现：

- CPython: `cpython`、`cp`
- PyPy: `pypy`、`pp`
- GraalPy: `graalpy`、`gp`
- Pyodide: `pyodide`

实现名称的请求不区分大小写。

有关支持格式的更多详细信息，请参阅 [Python 版本请求](#requesting-a-version)文档。

## 托管 Python 发行版 {#managed-python-distributions}

uv 支持下载并安装 CPython、PyPy 和 Pyodide 发行版。

### CPython 发行版 {#cpython-distributions}

由于 Python 官方不发布可分发 CPython 二进制文件，uv 转而使用来自 Astral
[`python-build-standalone`](https://github.com/astral-sh/python-build-standalone) 项目的预构建发行版。
`python-build-standalone` 也被许多其他 Python 项目使用，如
[Mise](https://mise.jdx.dev/lang/python.html) 和
[bazelbuild/rules_python](https://github.com/bazelbuild/rules_python)。

uv 的 Python 发行版是自包含、高度可移植且高性能的。虽然可以像 `pyenv` 等工具那样从源码构建 Python，但这需要预装系统依赖，并且创建优化、高性能的构建（例如启用 PGO 和 LTO）非常缓慢。

这些发行版存在一些行为上的特殊之处，通常是由于可移植性导致的；详细信息请参阅
[`python-build-standalone` 特殊行为](https://gregoryszorc.com/docs/python-build-standalone/main/quirks.html)文档。

### PyPy 发行版 {#pypy-distributions}

!!! note

    PyPy 版本落后于 CPython，目前仅支持最高 3.11 的 Python 版本。

PyPy 发行版由 [PyPy 项目](https://pypy.org)提供。

### Pyodide 发行版 {#pyodide-distributions}

Pyodide 发行版由 [Pyodide 项目](https://github.com/pyodide/pyodide)提供。

Pyodide 是 CPython 面向 WebAssembly / Emscripten 平台的移植版本。

## aarch64 上的透明 x86_64 模拟 {#transparent-x86_64-emulation-on-aarch64}

macOS 和 Windows 都支持通过透明模拟在 aarch64 上运行 x86_64 二进制文件。这被称为 [Rosetta 2](https://support.apple.com/en-gb/102527) 或
[Windows on ARM (WoA) 模拟](https://learn.microsoft.com/en-us/windows/arm/apps-on-arm-x86-emulation)。
可以在 aarch64 上使用 x86_64 版本的 uv，也可以在 aarch64 上使用 x86_64 的 Python 解释器。两种架构的 uv 二进制文件都可以使用任一种架构的 Python 解释器，但 Python 解释器需要其架构对应的包，即全部为 x86_64 或全部为 aarch64。

## Windows 注册表注册 {#registration-in-the-windows-registry}

在 Windows 上，安装托管 Python 版本时会按照 [PEP 514](https://peps.python.org/pep-0514/) 的定义将其注册到 Windows 注册表中。

安装后，可以使用 `py` 启动器选择这些 Python 版本，例如：

```console
$ uv python install 3.13.1
$ py -V:Astral/CPython3.13.1
```

卸载时，uv 将移除目标版本的注册表项以及任何损坏的注册表项。
