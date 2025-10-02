---
title: uv venv
description: 创建虚拟环境。
---

# uv venv

创建虚拟环境。

默认情况下，在工作目录中创建名为 `.venv` 的虚拟环境。可以通过位置参数提供替代路径。

如果在项目中，可以使用 `UV_PROJECT_ENVIRONMENT` 环境变量更改默认环境名称；这仅在从项目根目录运行时适用。

如果目标路径存在虚拟环境，它将被删除并创建一个新的空虚拟环境。

使用 uv 时，虚拟环境不需要激活。uv 将在工作目录或任何父目录中查找虚拟环境（名为 `.venv`）。

## Usage

```
uv venv [OPTIONS] [PATH]
```

## Arguments

### [`[PATH]`](#path)

要创建的虚拟环境的路径

## Options

### [`--no-project`](#-no-project)

避免发现项目或工作区

### [`--seed`](#-seed)

将种子包（`pip`、`setuptools` 和 `wheel` 中的一个或多个）安装到虚拟环境中 [env: UV_VENV_SEED=]

### [`--allow-existing`](#-allow-existing)

保留目标路径上的任何现有文件或目录

### [`--prompt`](#-prompt)

为虚拟环境提供替代提示前缀

### [`--system-site-packages`](#-system-site-packages)

让虚拟环境访问系统站点包目录

### [`--relocatable`](#-relocatable)

使虚拟环境可重定位

### [`--index-strategy`](#-index-strategy)

解析多个索引 URL 时使用的策略 [env: UV_INDEX_STRATEGY=] [可能的值：first-index, unsafe-first-match, unsafe-best-match]

### [`--keyring-provider`](#-keyring-provider)

尝试使用 `keyring` 进行索引 URL 身份验证 [env: UV_KEYRING_PROVIDER=] [可能的值：disabled, subprocess]

### [`--exclude-newer`](#-exclude-newer)

将候选包限制为在给定日期之前上传的包 [env: UV_EXCLUDE_NEWER=]

### [`--link-mode`](#-link-mode)

从全局缓存安装包时使用的方法 [env: UV_LINK_MODE=] [可能的值：clone, copy, hardlink, symlink]

## Python options

### [`-p, --python`](#-p-python)

用于虚拟环境的 Python 解释器。[env: UV_PYTHON=]

### [`--managed-python`](#-managed-python)

要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]

### [`--no-managed-python`](#-no-managed-python)

禁用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]

### [`--no-python-downloads`](#-no-python-downloads)

禁用 Python 的自动下载。[env: "UV_PYTHON_DOWNLOADS=never"]

## Index options

### [`--index`](#-index)

解析依赖项时使用的 URL，除了默认索引之外 [env: UV_INDEX=]

### [`--default-index`](#-default-index)

默认包索引的 URL（默认：<https://pypi.org/simple>）[env: UV_DEFAULT_INDEX=]

### [`-i, --index-url`](#-i-index-url)

（已弃用：请使用 `--default-index`）Python 包索引的 URL（默认：<https://pypi.org/simple>）[env: UV_INDEX_URL=]

### [`--extra-index-url`](#-extra-index-url)

（已弃用：请使用 `--index`）除了 `--index-url` 之外使用的包索引的额外 URL [env: UV_EXTRA_INDEX_URL=]

### [`-f, --find-links`](#-f-find-links)

搜索候选分发的位置，除了在注册表索引中找到的那些 [env: UV_FIND_LINKS=]

### [`--no-index`](#-no-index)

忽略注册表索引（例如 PyPI），而是依赖直接 URL 依赖项和通过 `--find-links` 提供的依赖项

## Cache options

### [`--refresh`](#-refresh)

刷新所有缓存数据

### [`-n, --no-cache`](#-n-no-cache)

避免读取或写入缓存，而是在操作期间使用临时目录 [env: UV_NO_CACHE=]

### [`--refresh-package`](#-refresh-package)

刷新特定包的缓存数据

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
