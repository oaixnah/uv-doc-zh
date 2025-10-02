---
title: uv init
description: 创建一个新项目。
---

# uv init

创建一个新项目。

遵循 `pyproject.toml` 规范。

如果目标位置已存在 `pyproject.toml`，uv 将退出并报错。

如果在目标路径的任何父目录中找到 `pyproject.toml`，该项目将被添加为父项目的工作区成员。

某些项目状态在需要时才会创建，例如，项目虚拟环境（`.venv`）和锁文件（`uv.lock`）在首次同步时才会延迟创建。

## Usage

```
uv init [OPTIONS] [PATH]
```

## Arguments

### [`[PATH]`](#path)

用于项目/脚本的路径

## Options

### [`--name`](#-name)

项目的名称

### [`--bare`](#-bare)

仅创建 `pyproject.toml`

### [`--package`](#-package)

将项目设置为构建为 Python 包

### [`--no-package`](#-no-package)

不将项目设置为构建为 Python 包

### [`--app`](#-app)

为应用程序创建项目

### [`--lib`](#-lib)

为库创建项目

### [`--script`](#-script)

创建脚本

### [`--description`](#-description)

设置项目描述

### [`--no-description`](#-no-description)

禁用项目描述

### [`--vcs`](#-vcs)

为项目初始化版本控制系统 [可能的值：git, none]

### [`--build-backend`](#-build-backend)

为项目初始化选择的构建后端 [可能的值：hatch, flit, pdm, poetry, setuptools, maturin, scikit]

### [`--no-readme`](#-no-readme)

不创建 `README.md` 文件

### [`--author-from`](#-author-from)

填写 `pyproject.toml` 中的 `authors` 字段 [可能的值：auto, git, none]

### [`--no-pin-python`](#-no-pin-python)

不为项目创建 `.python-version` 文件

### [`--no-workspace`](#-no-workspace)

避免发现工作区并创建独立项目

## Python options

### [`-p, --python`](#-p-python)

用于确定最低支持 Python 版本的 Python 解释器。[env: UV_PYTHON=]

### [`--managed-python`](#-managed-python)

要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]

### [`--no-managed-python`](#-no-managed-python)

禁用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]

### [`--no-python-downloads`](#-no-python-downloads)

禁用 Python 的自动下载。[env: "UV_PYTHON_DOWNLOADS=never"]

## Cache options

### [`-n, --no-cache`](#-n-no-cache)

避免读取或写入缓存，而是在操作期间使用临时目录 [env: UV_NO_CACHE=]

### [`--cache-dir`](#-cache-dir)

缓存目录的路径 [env: UV_CACHE_DIR=]

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
