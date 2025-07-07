---
title: uv pip
---

# uv pip

使用与 pip 兼容的接口管理 Python 包

## Usage

```
uv pip [OPTIONS] <COMMAND>
```

## Commands

### [`compile`](#compile)

将 `requirements.in` 文件编译为 `requirements.txt` 或 `pylock.toml` 文件

### [`sync`](#sync)

将环境与 `requirements.txt` 或 `pylock.toml` 文件同步

### [`install`](#install)

将包安装到环境中

### [`uninstall`](#uninstall)

从环境中卸载包

### [`freeze`](#freeze)

以 requirements 格式列出环境中已安装的包

### [`list`](#list)

以表格格式列出环境中已安装的包

### [`show`](#show)

显示一个或多个已安装包的信息

### [`tree`](#tree)

显示环境的依赖树

### [`check`](#check)

验证已安装的包是否具有兼容的依赖关系

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
