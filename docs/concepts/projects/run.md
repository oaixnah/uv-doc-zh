---
title: 在项目中运行命令
subtitle: Running commands
description: 学习如何在Python项目中使用`uv run`运行命令，包括请求额外依赖项、运行脚本、Windows旧式脚本支持以及信号处理机制。完整指南帮助您高效地在uv项目环境中运行命令。
---

# 在项目中运行命令 {#running-commands-in-projects}

在项目开发过程中，项目会被安装到 `.venv` 虚拟环境中。该环境默认与当前 shell 隔离，因此需要项目依赖的调用操作（例如 `python -c "import example"`）将会失败。此时应使用 `uv run` 在项目环境中运行命令：

```console
$ uv run python -c "import example"
```

使用 `run` 时，uv 会在执行给定命令之前确保项目环境是最新的。

给定的命令可以由项目环境提供，也可以存在于项目环境之外，例如：

```console
$ # 假设项目提供了 `example-cli`
$ uv run example-cli foo

$ # 运行一个需要项目环境可用的 `bash` 脚本
$ uv run bash scripts/foo.sh
```

## 请求额外的依赖项 {#requesting-additional-dependencies}

每次调用时可以请求额外的依赖项或不同版本的依赖项。

`--with` 选项用于在调用时包含一个依赖项，例如请求不同版本的 `httpx`：

```console
$ uv run --with httpx==0.26.0 python -c "import httpx; print(httpx.__version__)"
0.26.0
$ uv run --with httpx==0.25.0 python -c "import httpx; print(httpx.__version__)"
0.25.0
```

无论项目的要求如何，请求的版本都会得到遵循。例如，即使项目要求 `httpx==0.24.0`，上述输出仍将保持不变。

## 运行脚本 {#running-scripts}

声明了内联元数据（inline metadata）的脚本会自动在与项目隔离的环境中执行。更多详情请参阅[脚本指南](../../guides/scripts.md#declaring-script-dependencies)。

例如，给定以下脚本：

```python title="example.py"
# /// script
# dependencies = [
#   "httpx",
# ]
# ///

import httpx

resp = httpx.get("https://peps.python.org/api/peps.json")
data = resp.json()
print([(k, v["title"]) for k, v in data.items()][:10])
```

调用 `uv run example.py` 将在与项目_隔离_的环境中运行，仅使用所列出的依赖项。

## Windows 上的旧式脚本 {#legacy-scripts-on-windows}

uv 支持[旧式 setuptools 脚本](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#scripts)。这类脚本是 setuptools 在 `.venv\Scripts` 中安装的额外文件。

目前仅支持扩展名为 `.ps1`、`.cmd` 和 `.bat` 的旧式脚本。

例如，以下是运行命令提示符（Command Prompt）脚本的示例：

```console
$ uv run --with nuitka==2.6.7 -- nuitka.cmd --version
```

此外，您无需指定扩展名。`uv` 会自动按 `.ps1`、`.cmd`、`.bat` 的执行顺序查找对应文件：

```console
$ uv run --with nuitka==2.6.7 -- nuitka --version
```

## 信号处理 {#signal-handling}

为了在命令失败时提供更好的错误信息，uv 不会将进程控制权完全交给生成的子命令。因此，uv 负责将某些信号转发给所请求命令运行的子进程。

在 Unix 系统上，uv 会将大多数信号（SIGKILL、SIGCHLD、SIGIO 和 SIGPOLL 除外）转发给子进程。由于终端在按下 Ctrl-C 时会向当前前台进程组发送 SIGINT，uv 只有在收到多次 SIGINT 或子进程组与 uv 的进程组不同时，才会将 SIGINT 转发给子进程。

在 Windows 上，这些概念不适用，uv 会忽略 Ctrl-C 事件，将处理权交给子进程以便其能够正常退出。
