---
title: uv publish
---

# uv publish

将分发包上传到索引。

## Usage

```
uv publish [OPTIONS] [FILES]...
```

## Arguments

### [`[FILES]...`](#files)

要上传的文件路径。接受 glob 表达式 [默认: dist/*]

## Options

### [`--index`](#-index)

配置中用于发布的索引名称 [env: UV_PUBLISH_INDEX=]

### [`-u, --username`](#-u-username)

上传的用户名 [env: UV_PUBLISH_USERNAME=]

### [`-p, --password`](#-p-password)

上传的密码 [env: UV_PUBLISH_PASSWORD=]

### [`-t, --token`](#-t-token)

上传的令牌 [env: UV_PUBLISH_TOKEN=]

### [`--trusted-publishing`](#-trusted-publishing)

通过 GitHub Actions 配置使用可信发布 [可能的值：automatic, always, never]

### [`--keyring-provider`](#-keyring-provider)

尝试使用 `keyring` 进行远程需求文件的身份验证 [env: UV_KEYRING_PROVIDER=] [可能的值：disabled, subprocess]

### [`--publish-url`](#-publish-url)

上传端点的 URL（不是索引 URL）[env: UV_PUBLISH_URL=]

### [`--check-url`](#-check-url)

检查索引 URL 中的现有文件以跳过重复上传 [env: UV_PUBLISH_CHECK_URL=]

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
