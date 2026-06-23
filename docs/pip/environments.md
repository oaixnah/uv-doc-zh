---
subtitle: Using environments
description: 本文档详细介绍了 uv 中 Python 环境的使用指南，涵盖虚拟环境的创建、激活与退出、任意 Python 环境的使用方式，以及 uv 如何自动发现 Python 环境（包括 VIRTUAL_ENV、CONDA_PREFIX 和 .venv 的搜索优先级），帮助开发者高效管理 Python 项目依赖。
---

# 使用 Python 环境 {#using-python-environments}

每个 Python 安装都有一个在使用 Python 时处于活动状态的环境。可以将包安装到环境中，以便在你的 Python 脚本中使用它们的模块。通常，最佳实践是不要修改 Python 安装的环境。这对于操作系统自带的 Python 安装尤为重要，因为它们通常由系统自行管理包。虚拟环境是一种轻量级的方式，可将包与 Python 安装的环境隔离开来。与 `pip` 不同，uv 默认要求使用虚拟环境。

## 创建虚拟环境 {#creating-a-virtual-environment}

uv 支持创建虚拟环境，例如，在 `.venv` 处创建虚拟环境：

```console
$ uv venv
```

可以指定具体的名称或路径，例如，在 `my-name` 处创建虚拟环境：

```console
$ uv venv my-name
```

可以指定 Python 版本，例如，使用 Python 3.11 创建虚拟环境：

```console
$ uv venv --python 3.11
```

请注意，这要求系统上已安装所请求的 Python 版本。不过，如果该版本不可用，uv 会为你下载 Python。有关更多详细信息，请参阅 [Python 版本](../concepts/python-versions.md) 文档。

## 使用虚拟环境 {#using-a-virtual-environment}

当使用默认的虚拟环境名称时，uv 会在后续调用中自动找到并使用该虚拟环境。

```console
$ uv venv

$ # 在新的虚拟环境中安装一个包
$ uv pip install ruff
```

可以通过"激活"虚拟环境来使其中的包可用：

=== "macOS 和 Linux"

    ```console
    $ source .venv/bin/activate
    ```

=== "Windows"

    ```pwsh-session
    PS> .venv\Scripts\activate
    ```

!!! note

    Unix 上的默认激活脚本适用于符合 POSIX 标准的 shell，如 `sh`、`bash` 或 `zsh`。对于常见的替代 shell，还有额外的激活脚本。

    === "fish"

        ```console
        $ source .venv/bin/activate.fish
        ```

    === "csh / tcsh"


        ```console
        $ source .venv/bin/activate.csh
        ```

    === "Nushell"

        ```console
        $ use .venv\Scripts\activate.nu
        ```

## 退出环境 {#deactivating-an-environment}

要退出虚拟环境，请使用 `deactivate` 命令：

```console
$ deactivate
```

## 使用任意 Python 环境 {#using-arbitrary-python-environments}

由于 uv 不依赖 Python，它可以安装到除自身所在环境之外的其他虚拟环境中。例如，设置 `VIRTUAL_ENV=/path/to/venv` 将使 uv 安装到 `/path/to/venv`，无论 uv 安装在何处。请注意，如果 `VIRTUAL_ENV` 被设置为一个**不**符合 [PEP 405 规范](https://peps.python.org/pep-0405/#specification)的虚拟环境目录，则该设置将被忽略。

uv 还可以通过 `--python` 选项安装到任意环境，甚至是非虚拟环境。例如，`uv pip install --python /path/to/python` 将安装到 `/path/to/python` 解释器关联的环境中，无论该环境是否为虚拟环境。`--python` 选项也接受虚拟环境根目录的路径。

为了方便起见，`uv pip install --system` 将安装到系统 Python 环境中。使用 `--system` 大致等同于 `uv pip install --python $(which python)`，但请注意，链接到虚拟环境的可执行文件将被跳过。尽管我们通常建议使用虚拟环境进行依赖管理，但在持续集成和容器化环境中，`--system` 是合适的。

`--system` 标志也用于主动选择修改系统环境。例如，可以使用 `--python` 参数请求一个 Python 版本（例如 `--python 3.12`），uv 将搜索满足该请求的解释器。如果 uv 找到了一个系统解释器（例如 `/usr/lib/python3.12`），则需要 `--system` 标志来允许修改此非虚拟的 Python 环境。如果没有 `--system` 标志，uv 将忽略任何不在虚拟环境中的解释器。反之，当提供了 `--system` 标志时，uv 将忽略任何位于虚拟环境中的解释器。

跨平台和发行版安装到系统 Python 中是出了名的困难。uv 支持常见情况，但并非在所有情况下都能正常工作。例如，由于[发行版对 `distutils`（而非 `sysconfig`）的补丁](https://ffy00.github.io/blog/02-python-debian-and-the-install-locations/)，在 Python 3.10 之前的 Debian 上不支持安装到系统 Python。虽然我们始终建议使用虚拟环境，但在这些非标准环境中，uv 认为虚拟环境是必需的。

如果 uv 安装在某个 Python 环境中（例如通过 `pip` 安装），它仍然可以用来修改其他环境。然而，当通过 `python -m uv` 调用时，uv 将默认使用父解释器的环境。通过 Python 调用 uv 会增加启动开销，不推荐在常规使用中这样做。

uv 本身不依赖 Python，但它确实需要定位一个 Python 环境来（1）将依赖安装到该环境中，以及（2）构建源码分发包（source distributions）。

## Python 环境的发现 {#discovery-of-python-environments}

当运行会修改环境的命令时（如 `uv pip sync` 或 `uv pip install`），uv 将按以下顺序搜索虚拟环境：

- 基于 `VIRTUAL_ENV` 环境变量的已激活虚拟环境。
- 基于 `CONDA_PREFIX` 环境变量的已激活 Conda 环境。
- 当前目录或最近父目录中的 `.venv` 虚拟环境。

如果未找到虚拟环境，uv 将提示用户通过 `uv venv` 在当前目录中创建一个。

如果包含了 `--system` 标志，uv 将跳过虚拟环境搜索，转而查找已安装的 Python 版本。类似地，当运行不会修改环境的命令时（如 `uv pip compile`），uv 并不_要求_虚拟环境——但 Python 解释器仍然是必需的。有关已安装 Python 版本发现的详细信息，请参阅 [Python 发现](../concepts/python-versions.md#discovery-of-python-versions) 文档。
