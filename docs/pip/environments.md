---
subtitle: Using environments
description: 一份关于 uv 使用 Python 环境的指南，包括创建虚拟环境、使用虚拟环境等。
---

# 使用 Python 环境

每个 Python 安装都有一个在使用 Python 时处于活动状态的环境。可以将包安装到环境中，以便从您的 Python 脚本中访问其模块。通常，最佳实践是不修改 Python 安装的环境。这对于操作系统附带的 Python 安装尤其重要，因为它们通常自己管理包。虚拟环境是一种从 Python 安装环境中隔离包的轻量级方法。与 `pip` 不同，uv 默认要求使用虚拟环境。

## 创建虚拟环境

uv 支持创建虚拟环境，例如，在 `.venv` 创建一个虚拟环境：

```console
$ uv venv
```

可以指定特定的名称或路径，例如，在 `my-name` 创建一个虚拟环境：

```console
$ uv venv my-name
```

可以请求一个 Python 版本，例如，使用 Python 3.11 创建一个虚拟环境：

```console
$ uv venv --python 3.11
```

请注意，这要求所请求的 Python 版本在系统上可用。但是，如果不可用，uv 将为您下载 Python。有关更多详细信息，请参阅 [Python 版本](../concepts/python-versions.md)文档。

## 使用虚拟环境

使用默认虚拟环境名称时，uv 将在后续调用期间自动查找并使用该虚拟环境。

```console
$ uv venv

$ # 在新的虚拟环境中安装一个包
$ uv pip install ruff
```

可以“激活”虚拟环境以使其包可用：

=== "macOS 和 Linux"

    ```console
    $ source .venv/bin/activate
    ```

=== "Windows"

    ```pwsh-session
    PS> .venv\Scripts\activate
    ```

!!! note

    Unix 上的默认激活脚本适用于 POSIX 兼容的 shell，如 `sh`、`bash` 或 `zsh`。
    对于常见的替代 shell，还有其他激活脚本。

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

## 停用环境

要退出虚拟环境，请使用 `deactivate` 命令：

```console
$ deactivate
```

## 使用任意 Python 环境

由于 uv 对 Python 没有依赖，因此它可以安装到其自身之外的虚拟环境中。
例如，设置 `VIRTUAL_ENV=/path/to/venv` 将导致 uv 安装到 `/path/to/venv`，而不管 uv 安装在哪里。请注意，如果 `VIRTUAL_ENV` 设置为**不**是 [PEP 405 兼容](https://peps.python.org/pep-0405/#specification)的虚拟环境的目录，它将被忽略。

uv 还可以使用提供给 `uv pip sync` 或 `uv pip install` 的 `--python` 参数安装到任意的，甚至非虚拟的环境中。例如，`uv pip install --python /path/to/python` 将安装到链接到 `/path/to/python` 解释器的环境中。

为方便起见，`uv pip install --system` 将安装到系统 Python 环境中。使用 `--system` 大致相当于 `uv pip install --python $(which python)`，但请注意，链接到虚拟环境的可执行文件将被跳过。虽然我们通常建议使用虚拟环境进行依赖管理，但 `--system` 在持续集成和容器化环境中是合适的。

`--system` 标志还用于选择性地修改系统环境。例如，`--python` 参数可用于请求 Python 版本（例如 `--python 3.12`），uv 将搜索满足请求的解释器。如果 uv 找到系统解释器（例如 `/usr/lib/python3.12`），则需要 `--system` 标志以允许修改此非虚拟 Python 环境。如果没有 `--system` 标志，uv 将忽略任何不在虚拟环境中的解释器。相反，当提供 `--system` 标志时，uv 将忽略任何*在*虚拟环境中的解释器。

在不同平台和发行版上安装到系统 Python 是出了名的困难。uv 支持常见情况，但并非在所有情况下都有效。例如，由于[发行版对 `distutils`（而非 `sysconfig`）的修补](https://ffy00.github.io/blog/02-python-debian-and-the-install-locations/)，不支持在 Python 3.10 之前的 Debian 上安装到系统 Python。虽然我们始终建议使用虚拟环境，但 uv 认为在这些非标准环境中它们是必需的。

如果 uv 安装在 Python 环境中（例如，使用 `pip`），它仍然可以用于修改其他环境。但是，当使用 `python -m uv` 调用时，uv 将默认使用父解释器的环境。通过 Python 调用 uv 会增加启动开销，不建议常规使用。

uv 本身不依赖于 Python，但它确实需要定位一个 Python 环境来 (1) 将依赖项安装到环境中以及 (2) 构建源发行版。

## Python 环境的发现

当运行一个会改变环境的命令时，比如 `uv pip sync` 或 `uv pip install`，uv 会按照以下顺序搜索虚拟环境：

- 基于 `VIRTUAL_ENV` 环境变量的已激活虚拟环境。
- 基于 `CONDA_PREFIX` 环境变量的已激活 Conda 环境。
- 当前目录或最近的父目录中的 `.venv` 虚拟环境。

如果没有找到虚拟环境，uv 将提示用户通过 `uv venv` 在当前目录中创建一个。

如果包含 `--system` 标志，uv 将跳过虚拟环境搜索已安装的 Python 版本。同样，当运行一个不会改变环境的命令时，比如 `uv pip compile`，uv *不要求*虚拟环境——但是，仍然需要一个 Python 解释器。有关已安装 Python 版本发现的详细信息，请参阅 [Python 发现](../concepts/python-versions.md#python_8)的文档。
