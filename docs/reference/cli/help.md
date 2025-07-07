---
title: uv help
---

# uv help

显示命令的文档。

## Usage

```
uv [OPTIONS] <COMMAND>
```

## Commands

### [`run`](#run)

运行命令或脚本

### [`init`](#init)

创建一个新项目

### [`add`](#add)

向项目添加依赖项

### [`remove`](#remove)

从项目中移除依赖项

### [`version`](#version)

读取或更新项目的版本

### [`sync`](#sync)

更新项目的环境

### [`lock`](#lock)

更新项目的锁文件

### [`export`](#export)

将项目的锁文件导出为其他格式

### [`tree`](#tree)

显示项目的依赖树

### [`tool`](#tool)

运行和安装由 Python 包提供的命令

### [`python`](#python)

管理 Python 版本和安装

### [`pip`](#pip)

使用与 pip 兼容的接口管理 Python 包

### [`venv`](#venv)

创建虚拟环境

### [`build`](#build)

将 Python 包构建为源分发和轮子

### [`publish`](#publish)

将分发包上传到索引

### [`cache`](#cache)

管理 uv 的缓存

### [`self`](#self)

管理 uv 可执行文件

### [`generate-shell-completion`](#generate-shell-completion)

生成 shell 补全

### [`help`](#help)

显示命令的文档

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

### [`-V, --version`](#-v-version)

显示 uv 版本
