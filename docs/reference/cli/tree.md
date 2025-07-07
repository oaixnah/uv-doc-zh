---
title: uv tree
---

# uv tree

显示项目的依赖树。

## Usage

```
uv tree [OPTIONS]
```

## Options

### [`--universal`](#-universal)

显示平台无关的依赖树

### [`-d, --depth`](#-d-depth)

依赖树的最大显示深度 [默认值：255]

### [`--prune`](#-prune)

从依赖树显示中修剪给定的包

### [`--package`](#-package)

仅显示指定的包

### [`--no-dedupe`](#-no-dedupe)

不去重复的依赖项。通常，当一个包已经显示了它的依赖项时，进一步的出现将不会重新显示其依赖项，并将包含一个 (*) 来表示它已经被显示过。此标志将导致这些重复项被重复显示

### [`--invert`](#-invert)

显示给定包的反向依赖关系。此标志将反转树并显示依赖于给定包的包

### [`--outdated`](#-outdated)

显示树中每个包的最新可用版本

### [`--only-dev`](#-only-dev)

仅包含开发依赖组

### [`--no-dev`](#-no-dev)

禁用开发依赖组

### [`--group`](#-group)

包含来自指定依赖组的依赖项

### [`--no-group`](#-no-group)

禁用指定的依赖组

### [`--no-default-groups`](#-no-default-groups)

忽略默认依赖组

### [`--only-group`](#-only-group)

仅包含来自指定依赖组的依赖项

### [`--all-groups`](#-all-groups)

包含来自所有依赖组的依赖项

### [`--locked`](#-locked)

断言 `uv.lock` 将保持不变 [env: UV_LOCKED=]

### [`--frozen`](#-frozen)

显示需求而不锁定项目 [env: UV_FROZEN=]

### [`--script`](#-script)

显示指定 PEP 723 Python 脚本的依赖树，而不是当前项目

### [`--python-version`](#-python-version)

过滤树时使用的 Python 版本

### [`--python-platform`](#-python-platform)

过滤树时使用的平台 [可能的值：windows, linux, macos, x86_64-pc-windows-msvc, i686-pc-windows-msvc, x86_64-unknown-linux-gnu, aarch64-apple-darwin, x86_64-apple-darwin, aarch64-unknown-linux-gnu, aarch64-unknown-linux-musl, x86_64-unknown-linux-musl, x86_64-manylinux2014, x86_64-manylinux_2_17, x86_64-manylinux_2_28, x86_64-manylinux_2_31, x86_64-manylinux_2_32, x86_64-manylinux_2_33, x86_64-manylinux_2_34, x86_64-manylinux_2_35, x86_64-manylinux_2_36, x86_64-manylinux_2_37, x86_64-manylinux_2_38, x86_64-manylinux_2_39, x86_64-manylinux_2_40, aarch64-manylinux2014, aarch64-manylinux_2_17, aarch64-manylinux_2_28, aarch64-manylinux_2_31, aarch64-manylinux_2_32, aarch64-manylinux_2_33, aarch64-manylinux_2_34, aarch64-manylinux_2_35, aarch64-manylinux_2_36, aarch64-manylinux_2_37, aarch64-manylinux_2_38, aarch64-manylinux_2_39, aarch64-manylinux_2_40, wasm32-pyodide2024]

## Build options

### [`--no-build`](#-no-build)

不构建源码分发包 [env: UV_NO_BUILD=]

### [`--no-build-package`](#-no-build-package)

不为特定包构建源码分发包 [env: UV_NO_BUILD_PACKAGE=]

### [`--no-binary`](#-no-binary)

不安装预构建的 wheel 包 [env: UV_NO_BINARY=]

### [`--no-binary-package`](#-no-binary-package)

不为特定包安装预构建的 wheel 包 [env: UV_NO_BINARY_PACKAGE=]

### [`-C, --config-setting`](#-c-config-setting)

传递给 PEP 517 构建后端的设置，指定为 `KEY=VALUE` 对

### [`--no-build-isolation`](#-no-build-isolation)

构建源码分发包时禁用隔离 [env: UV_NO_BUILD_ISOLATION=]

### [`--no-build-isolation-package`](#-no-build-isolation-package)

为特定包构建源码分发包时禁用隔离

## Index options

### [`--index`](#-index)

解析依赖项时使用的 URL，除了默认索引之外 [env: UV_INDEX=]

### [`--default-index`](#-default-index)

默认包索引的 URL（默认：<https://pypi.org/simple>）[env: UV_DEFAULT_INDEX=]

### [`-i, --index-url`](#-i-index-url)

（已弃用：请使用 `--default-index`）Python 包索引的 URL（默认：<https://pypi.org/simple>）[env: UV_INDEX_URL=]

### [`--extra-index-url`](#-extra-index-url)

（已弃用：请使用 `--index`）除了 `--index-url` 之外要使用的包索引的额外 URL [env: UV_EXTRA_INDEX_URL=]

### [`-f, --find-links`](#-f-find-links)

搜索候选分发包的位置，除了在注册表索引中找到的那些 [env: UV_FIND_LINKS=]

### [`--no-index`](#-no-index)

忽略注册表索引（例如 PyPI），而是依赖直接 URL 依赖项和通过 `--find-links` 提供的依赖项

### [`--index-strategy`](#-index-strategy)

针对多个索引 URL 进行解析时使用的策略 [env: UV_INDEX_STRATEGY=] [可能的值：first-index, unsafe-first-match, unsafe-best-match]

### [`--keyring-provider`](#-keyring-provider)

尝试使用 `keyring` 对索引 URL 进行身份验证 [env: UV_KEYRING_PROVIDER=] [可能的值：disabled, subprocess]

## Resolver options

### [`-U, --upgrade`](#-u-upgrade)

允许包升级，忽略任何现有输出文件中的固定版本。隐含 `--refresh`

### [`-P, --upgrade-package`](#-p-upgrade-package)

允许特定包的升级，忽略任何现有输出文件中的固定版本。隐含 `--refresh-package`

### [`--resolution`](#-resolution)

为给定包需求选择不同兼容版本时使用的策略 [env: UV_RESOLUTION=] [可能的值：highest, lowest, lowest-direct]

### [`--prerelease`](#-prerelease)

考虑预发布版本时使用的策略 [env: UV_PRERELEASE=] [可能的值：disallow, allow, if-necessary, explicit, if-necessary-or-explicit]

### [`--fork-strategy`](#-fork-strategy)

跨 Python 版本和平台选择给定包的多个版本时使用的策略 [env: UV_FORK_STRATEGY=] [可能的值：fewest, requires-python]

### [`--exclude-newer`](#-exclude-newer)

将候选包限制为在给定日期之前上传的包 [env: UV_EXCLUDE_NEWER=]

### [`--no-sources`](#-no-sources)

解析依赖项时忽略 `tool.uv.sources` 表。用于锁定符合标准的、可发布的包元数据，而不是使用任何工作区、Git、URL 或本地路径源

## Installer options

### [`--link-mode`](#-link-mode)

从全局缓存安装包时使用的方法 [env: UV_LINK_MODE=] [可能的值：clone, copy, hardlink, symlink]

## Python options

### [`-p, --python`](#-p-python)

用于锁定和过滤的 Python 解释器。[env: UV_PYTHON=]

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
