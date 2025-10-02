---
title: uv python
description: 管理 Python 版本和安装。
---

# uv python

管理 Python 版本和安装。

通常，uv 首先在虚拟环境中搜索 Python，无论是活动的虚拟环境还是当前工作目录或任何父目录中的 `.venv` 目录。如果不需要虚拟环境，uv 将搜索 Python 解释器。通过在 `PATH` 环境变量中搜索 Python 可执行文件来找到 Python 解释器。

在 Windows 上，注册表也会被搜索以查找 Python 可执行文件。

默认情况下，如果找不到版本，uv 将下载 Python。可以使用 `--no-python-downloads` 标志或 `python-downloads` 设置来禁用此行为。

`--python` 选项允许请求不同的解释器。

支持以下 Python 版本请求格式：

- `<version>` 例如 `3`、`3.12`、`3.12.3`
- `<version-specifier>` 例如 `>=3.12,<3.13`
- `<implementation>` 例如 `cpython` 或 `cp`
- `<implementation>@<version>` 例如 `cpython@3.12`
- `<implementation><version>` 例如 `cpython3.12` 或 `cp312`
- `<implementation><version-specifier>` 例如 `cpython>=3.12,<3.13`
- `<implementation>-<version>-<os>-<arch>-<libc>` 例如 `cpython-3.12.3-macos-aarch64-none`

此外，通常可以使用以下方式请求特定的系统 Python 解释器：

- `<executable-path>` 例如 `/opt/homebrew/bin/python3`
- `<executable-name>` 例如 `mypython3`
- `<install-dir>` 例如 `/some/environment/`

当使用 `--python` 选项时，正常的发现规则适用，但会检查发现的解释器是否与请求兼容，例如，如果请求 `pypy`，uv 将首先检查虚拟环境是否包含 PyPy 解释器，然后检查路径中的每个可执行文件是否为 PyPy 解释器。

uv 支持发现 CPython、PyPy 和 GraalPy 解释器。不支持的解释器将在发现过程中被跳过。如果请求不支持的解释器实现，uv 将退出并报错。

## Usage

```
uv python [OPTIONS] <COMMAND>
```

## Commands

### [`list`](#list)

列出可用的 Python 安装

### [`install`](#install)

下载并安装 Python 版本

### [`upgrade`](#upgrade)

将已安装的 Python 版本升级到最新支持的补丁版本（需要 `--preview` 标志）

### [`find`](#find)

搜索 Python 安装

### [`pin`](#pin)

固定到特定的 Python 版本

### [`dir`](#dir)

显示 uv Python 安装目录

### [`uninstall`](#uninstall)

卸载 Python 版本

## Cache options

### [`-n, --no-cache`](#-n-no-cache)

避免读取或写入缓存，而是在操作期间使用临时目录 [env: UV_NO_CACHE=]

### [`--cache-dir`](#-cache-dir)

缓存目录的路径 [env: UV_CACHE_DIR=]

## Python options

### [`--managed-python`](#-managed-python)

要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]

### [`--no-managed-python`](#-no-managed-python)

禁用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]

### [`--no-python-downloads`](#-no-python-downloads)

禁用 Python 的自动下载。[env: "UV_PYTHON_DOWNLOADS=never"]

## Global options

### [`-q, --quiet...`](#-q-quiet)

使用静默输出

### [`-v, --verbose...`](#-v-verbose)

使用详细输出

### [`--color`](#-color)

控制输出中颜色的使用 [可能的值：auto, always, never]

### [`--native-tls`](#-native-tls)

是否从平台的本机证书存储加载 TLS 证书 [env: UV_NATIVE_TLS=]

### [`--offline`](#-offline)

禁用网络访问 [env: UV_OFFLINE=]

### [`--allow-insecure-host`](#-allow-insecure-host)

允许与主机的不安全连接 [env: UV_INSECURE_HOST=]

### [`--no-progress`](#-no-progress)

隐藏所有进度输出 [env: UV_NO_PROGRESS=]

### [`--directory`](#-directory)

在运行命令之前切换到给定目录

### [`--project`](#-project)

在给定项目目录中运行命令 [env: UV_PROJECT=]

### [`--config-file`](#-config-file)

用于配置的 `uv.toml` 文件路径 [env: UV_CONFIG_FILE=]

### [`--no-config`](#-no-config)

避免发现配置文件（`pyproject.toml`、`uv.toml`）[env: UV_NO_CONFIG=]

### [`-h, --help`](#-h-help)

显示此命令的简洁帮助
