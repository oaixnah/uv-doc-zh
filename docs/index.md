---
hide:
  - navigation
---

# uv

一个用 Rust 编写的极速 Python 包和项目管理器。

![显示基准测试结果的条形图](assets/316150503-03aa9163-1c79-4a87-a31d-7a9311ed9310.svg#only-dark)
![显示基准测试结果的条形图](assets/316150505-629e59c0-9c6e-4013-9ad4-adb2bcf5080d.svg#only-light)
/// caption
_使用热缓存安装 [Trio](https://trio.readthedocs.io/) 的依赖项。_
///

## 亮点

- 🚀 一个工具即可取代 `pip`、`pip-tools`、`pipx`、`poetry`、`pyenv`、`twine`、`virtualenv` 等。
- ⚡️ 比 `pip` [快 10-100 倍](reference/benchmarks.md)。
- 🗂️ 提供[全面的项目管理](#_3)，并带有[通用锁文件](./concepts/projects/layout.md#_3)。
- ❇️ [运行脚本](#_4)，支持[内联依赖元数据](./guides/scripts.md#_4)。
- 🐍 [安装和管理](#python) Python 版本。
- 🛠️ [运行和安装](#_5) 作为 Python 包发布的工具。
- 🔩 包含一个 [pip 兼容接口](#pip)，以熟悉的 CLI 提供性能提升。
- 🏢 支持 Cargo 风格的[工作区](./concepts/projects/workspaces.md)，适用于可扩展项目。
- 💾 磁盘空间高效，具有用于依赖项去重的[全局缓存](./concepts/cache.md)。
- ⏬ 无需 Rust 或 Python，即可通过 `curl` 或 `pip` 安装。
- 🖥️ 支持 macOS、Linux 和 Windows。

uv 由 [Ruff](https://github.com/astral-sh/ruff) 的创建者 [Astral](https://astral.sh) 提供支持。

## 安装

使用我们的官方独立安装程序安装 uv：

=== "macOS 和 Linux"

    ```console
    $ curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

=== "Windows"

    ```pwsh-session
    PS> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

然后，查看[第一步](./getting-started/first-steps.md)或继续阅读简要概述。

!!! tip

    uv 也可以通过 pip、Homebrew 等方式安装。在[安装页面](./getting-started/installation.md)上查看所有方法。

## 项目

uv 管理项目依赖项和环境，支持锁文件、工作区等，类似于 `rye` 或 `poetry`：

```console
$ uv init example
Initialized project `example` at `/home/user/example`

$ cd example

$ uv add ruff
Creating virtual environment at: .venv
Resolved 2 packages in 170ms
   Built example @ file:///home/user/example
Prepared 2 packages in 627ms
Installed 2 packages in 1ms
 + example==0.1.0 (from file:///home/user/example)
 + ruff==0.5.4

$ uv run ruff check
All checks passed!

$ uv lock
Resolved 2 packages in 0.33ms

$ uv sync
Resolved 2 packages in 0.70ms
Audited 1 package in 0.02ms
```

请参阅[项目指南](./guides/projects.md)以开始使用。

uv 还支持构建和发布项目，即使它们不是用 uv 管理的。请参阅[打包指南](./guides/package.md)以了解更多信息。

## 脚本

uv 管理单文件脚本的依赖项和环境。

创建一个新脚本并添加内联元数据以声明其依赖项：

```console
$ echo 'import requests; print(requests.get("https://astral.sh"))' > example.py

$ uv add --script example.py requests
Updated `example.py`
```

然后，在隔离的虚拟环境中运行脚本：

```console
$ uv run example.py
Reading inline script metadata from: example.py
Installed 5 packages in 12ms
<Response [200]>
```

请参阅[脚本指南](./guides/scripts.md)以开始使用。

## 工具

uv 执行和安装由 Python 包提供的命令行工具，类似于 `pipx`。

使用 `uvx`（`uv tool run` 的别名）在临时环境中运行工具：

```console
$ uvx pycowsay 'hello world!'
Resolved 1 package in 167ms
Installed 1 package in 9ms
 + pycowsay==0.0.0.2
  """

  ------------
< hello world! >
  ------------
   \   ^__^
    \  (oo)\_______
       (__)\       )\/\
           ||----w |
           ||     ||
```

使用 `uv tool install` 安装工具：

```console
$ uv tool install ruff
Resolved 1 package in 6ms
Installed 1 package in 2ms
 + ruff==0.5.4
Installed 1 executable: ruff

$ ruff --version
ruff 0.5.4
```

请参阅[工具指南](./guides/tools.md)以开始使用。

## Python 版本

uv 安装 Python 并允许在版本之间快速切换。

安装多个 Python 版本：

```console
$ uv python install 3.10 3.11 3.12
Searching for Python versions matching: Python 3.10
Searching for Python versions matching: Python 3.11
Searching for Python versions matching: Python 3.12
Installed 3 versions in 3.42s
 + cpython-3.10.14-macos-aarch64-none
 + cpython-3.11.9-macos-aarch64-none
 + cpython-3.12.4-macos-aarch64-none
```

根据需要下载 Python 版本：

```console
$ uv venv --python 3.12.0
Using CPython 3.12.0
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate

$ uv run --python pypy@3.8 -- python
Python 3.8.16 (a9dbdca6fc3286b0addd2240f11d97d8e8de187a, Dec 29 2022, 11:45:30)
[PyPy 7.3.11 with GCC Apple LLVM 13.1.6 (clang-1316.0.21.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>>
```

在当前目录中使用特定的 Python 版本：

```console
$ uv python pin 3.11
Pinned `.python-version` to `3.11`
```

请参阅[安装 Python 指南](./guides/install-python.md)以开始使用。

## pip 接口

uv 为常见的 `pip`、`pip-tools` 和 `virtualenv` 命令提供了直接替代品。

uv 通过高级功能扩展了它们的接口，例如依赖版本覆盖、平台无关的解析、可复现的解析、替代解析策略等。

使用 `uv pip` 接口，无需更改现有工作流程即可迁移到 uv，并体验 10-100 倍的速度提升。

将需求编译为平台无关的需求文件：

```console
$ uv pip compile docs/requirements.in \
   --universal \
   --output-file docs/requirements.txt
Resolved 43 packages in 12ms
```

创建一个虚拟环境：

```console
$ uv venv
Using CPython 3.12.3
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
```

安装锁定的需求：

```console
$ uv pip sync docs/requirements.txt
Resolved 43 packages in 11ms
Installed 43 packages in 208ms
 + babel==2.15.0
 + black==24.4.2
 + certifi==2024.7.4
 ...
```

请参阅 [pip 接口文档](./pip/index.md)以开始使用。

## 了解更多

请参阅[第一步](./getting-started/first-steps.md)或直接跳转到[使用指南](./guides/index.md)以开始使用 uv。
