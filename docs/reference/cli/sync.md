---
title: uv sync
description: 更新项目的环境。
---

# uv sync

更新项目的环境。

同步确保所有项目依赖项都已安装并与锁文件保持最新状态。

默认情况下，执行精确同步：uv 会移除未声明为项目依赖项的包。使用 `--inexact` 标志来保留无关包。请注意，如果无关包与项目依赖项冲突，它仍会被移除。此外，如果使用 `--no-build-isolation`，uv 将不会移除无关包，以避免移除可能的构建依赖项。

如果项目虚拟环境（`.venv`）不存在，将会创建它。

除非提供 `--locked` 或 `--frozen` 标志，否则项目会在同步前重新锁定。

uv 将在当前目录或任何父目录中搜索项目。如果找不到项目，uv 将退出并报错。

请注意，从锁文件安装时，uv 不会为已撤回的包版本提供警告。

## Usage

```
uv sync [OPTIONS]
```

## Options

### [`--extra`](#-extra)

包含指定额外名称的可选依赖项

### [`--all-extras`](#-all-extras)

包含所有可选依赖项

### [`--no-extra`](#-no-extra)

如果提供了 `--all-extras`，则排除指定的可选依赖项

### [`--no-dev`](#-no-dev)

禁用开发依赖组

### [`--only-dev`](#-only-dev)

仅包含开发依赖组

### [`--group`](#-group)

包含指定依赖组的依赖项

### [`--no-group`](#-no-group)

禁用指定的依赖组

### [`--no-default-groups`](#-no-default-groups)

忽略默认依赖组

### [`--only-group`](#-only-group)

仅包含指定依赖组的依赖项

### [`--all-groups`](#-all-groups)

包含所有依赖组的依赖项

### [`--no-editable`](#-no-editable)

将任何可编辑依赖项（包括项目和任何工作区成员）安装为非可编辑 [env: UV_NO_EDITABLE=]

### [`--inexact`](#-inexact)

不移除环境中存在的无关包

### [`--active`](#-active)

将依赖项同步到活动虚拟环境

### [`--no-install-project`](#-no-install-project)

不安装当前项目

### [`--no-install-workspace`](#-no-install-workspace)

不安装任何工作区成员，包括根项目

### [`--no-install-package`](#-no-install-package)

不安装给定的包

### [`--locked`](#-locked)

断言 `uv.lock` 将保持不变 [env: UV_LOCKED=]

### [`--frozen`](#-frozen)

同步时不更新 `uv.lock` 文件 [env: UV_FROZEN=]

### [`--dry-run`](#-dry-run)

执行试运行，不写入锁文件或修改项目环境

### [`--all-packages`](#-all-packages)

同步工作区中的所有包

### [`--package`](#-package)

同步工作区中的特定包

### [`--script`](#-script)

为 Python 脚本同步环境，而不是当前项目

### [`--check`](#-check)

检查 Python 环境是否与项目同步

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

### [`--index-strategy`](#-index-strategy)

解析多个索引 URL 时使用的策略 [env: UV_INDEX_STRATEGY=] [可能的值：first-index, unsafe-first-match, unsafe-best-match]

### [`--keyring-provider`](#-keyring-provider)

尝试使用 `keyring` 进行索引 URL 身份验证 [env: UV_KEYRING_PROVIDER=] [可能的值：disabled, subprocess]

## Resolver options

### [`-U, --upgrade`](#-u-upgrade)

允许包升级，忽略任何现有输出文件中的固定版本。暗示 `--refresh`

### [`-P, --upgrade-package`](#-p-upgrade-package)

允许特定包的升级，忽略任何现有输出文件中的固定版本。暗示 `--refresh-package`

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

### [`--reinstall`](#-reinstall)

重新安装所有包，无论它们是否已安装。暗示 `--refresh`

### [`--reinstall-package`](#-reinstall-package)

重新安装特定包，无论它是否已安装。暗示 `--refresh-package`

### [`--link-mode`](#-link-mode)

从全局缓存安装包时使用的方法 [env: UV_LINK_MODE=] [可能的值：clone, copy, hardlink, symlink]

### [`--compile-bytecode`](#-compile-bytecode)

安装后将 Python 文件编译为字节码 [env: UV_COMPILE_BYTECODE=]

## Build options

### [`-C, --config-setting`](#-c-config-setting)

传递给 PEP 517 构建后端的设置，指定为 `KEY=VALUE` 对

### [`--no-build-isolation`](#-no-build-isolation)

构建源分发时禁用隔离 [env: UV_NO_BUILD_ISOLATION=]

### [`--no-build-isolation-package`](#-no-build-isolation-package)

为特定包构建源分发时禁用隔离

### [`--no-build`](#-no-build)

不构建源分发 [env: UV_NO_BUILD=]

### [`--no-build-package`](#-no-build-package)

不为特定包构建源分发 [env: UV_NO_BUILD_PACKAGE=]

### [`--no-binary`](#-no-binary)

不安装预构建的 wheel [env: UV_NO_BINARY=]

### [`--no-binary-package`](#-no-binary-package)

不为特定包安装预构建的 wheel [env: UV_NO_BINARY_PACKAGE=]

## Cache options

### [`-n, --no-cache`](#-n-no-cache)

避免读取或写入缓存，而是在操作期间使用临时目录 [env: UV_NO_CACHE=]

### [`--cache-dir`](#-cache-dir)

缓存目录的路径 [env: UV_CACHE_DIR=]

### [`--refresh`](#-refresh)

刷新所有缓存数据

### [`--refresh-package`](#-refresh-package)

刷新特定包的缓存数据

## Python options

### [`-p, --python`](#-p-python)

用于项目环境的 Python 解释器。[env: UV_PYTHON=]

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
