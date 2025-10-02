---
title: 在项目中运行命令
subtitle: Running commands
description: 学习如何在Python项目中运行命令，包括使用`uv run`在项目环境中执行脚本和命令。了解如何请求额外的依赖项，以及如何在项目环境中运行脚本。完整指南帮助您高效地在项目中运行命令。
---

# 在项目中运行命令

在处理项目时，它会安装到位于 `.venv` 的虚拟环境中。默认情况下，此环境与当前 shell 隔离，因此需要该项目的调用（例如 `python -c "import example"`）将会失败。请改用 `uv run` 在项目环境中运行命令：

```console
$ uv run python -c "import example"
```

使用 `run` 时，uv 会在运行给定命令之前确保项目环境是最新的。

给定的命令可以由项目环境提供，也可以存在于项目环境之外，例如：

```console
$ # 假设项目提供了 `example-cli`
$ uv run example-cli foo

$ # 运行一个需要项目可用的 `bash` 脚本
$ uv run bash scripts/foo.sh
```

## 请求额外的依赖项

可以为每次调用请求额外的依赖项或不同版本的依赖项。

`--with` 选项用于为调用包含一个依赖项，例如，请求一个不同版本的 `httpx`：

```console
$ uv run --with httpx==0.26.0 python -c "import httpx; print(httpx.__version__)"
0.26.0
$ uv run --with httpx==0.25.0 python -c "import httpx; print(httpx.__version__)"
0.25.0
```

无论项目的要求如何，请求的版本都将得到遵守。例如，即使项目需要 `httpx==0.24.0`，上面的输出也会是相同的。

## 运行脚本

声明了内联元数据的脚本会自动在与项目隔离的环境中执行。有关更多详细信息，请参阅[脚本指南](../../guides/scripts.md#_4)。

例如，给定一个脚本：

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

调用 `uv run example.py` 将在与项目 _隔离_ 的环境中运行，只使用列出的给定依赖项。

## 旧版 Windows 脚本

支持[旧版 setuptools 脚本](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#scripts)。这些类型的脚本是 setuptools 安装在 `.venv\Scripts` 中的附加文件。

目前仅支持带有 `.ps1`、`.cmd` 和 `.bat` 扩展名的旧版脚本。

例如，下面是运行命令提示符脚本的示例。

```console
$ uv run --with nuitka==2.6.7 -- nuitka.cmd --version
```

此外，您无需指定扩展名。`uv` 会自动按执行顺序为您查找以 `.ps1`、`.cmd` 和 `.bat` 结尾的文件。

```console
$ uv run --with nuitka==2.6.7 -- nuitka --version
```

## 信号处理

uv 不会将进程的控制权交给派生的命令，以便在失败时提供更好的错误消息。因此，uv 负责将某些信号转发到所请求命令运行的子进程中。

在 Unix 系统上，uv 会将 SIGINT 和 SIGTERM 转发给子进程。由于终端在按下 Ctrl-C 时会向​​前台进程组发送 SIGINT，因此只有在多次发送 SIGINT 或子进程组与 uv 的进程组不同时，uv 才会将 SIGINT 转发给子进程。

在 Windows 上，这些概念不适用，uv 会忽略 Ctrl-C 事件，将处理推迟到子进程，以便它可以干净地退出。
