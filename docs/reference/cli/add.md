---
title: uv add
description: 向项目添加依赖项。
---

# uv add

向项目添加依赖项。

依赖项会被添加到项目的 `pyproject.toml` 文件中。

如果给定的依赖项已经存在，它将被更新为新的版本说明符，除非它包含与现有说明符不同的标记，在这种情况下，将为该依赖项添加另一个条目。

锁文件和项目环境将被更新以反映添加的依赖项。要跳过更新锁文件，请使用 `--frozen`。要跳过更新环境，请使用 `--no-sync`。

如果找不到任何请求的依赖项，uv 将退出并报错，除非提供了 `--frozen` 标志，在这种情况下，uv 将逐字添加依赖项而不检查它们是否存在或与项目兼容。

uv 将在当前目录或任何父目录中搜索项目。如果找不到项目，uv 将退出并报错。

## Usage

```
uv add [OPTIONS] <PACKAGES|--requirements <REQUIREMENTS>>
```

## Arguments

### [`[PACKAGES]...`](#packages)

要添加的包，作为 PEP 508 要求（例如，`ruff==0.5.0`）

## Options

### [`-r, --requirements`](#-r-requirements)

添加给定 `requirements.txt` 文件中列出的所有包

### [`-c, --constraints`](#-c-constraints)

使用给定的要求文件约束版本 [env: UV_CONSTRAINT=]

### [`-m, --marker`](#-m-marker)

将此标记应用于所有添加的包

### [`--dev`](#-dev)

将要求添加到开发依赖组

### [`--optional`](#-optional)

将要求添加到指定额外功能的包的可选依赖项

### [`--group`](#-group)

将要求添加到指定的依赖组

### [`--editable`](#-editable)

将要求添加为可编辑的

### [`--raw`](#-raw)

按提供的方式添加依赖项

### [`--bounds`](#-bounds)

添加依赖项时使用的版本说明符类型 [可能的值：lower, major, minor, exact]

### [`--rev`](#-rev)

从 Git 添加依赖项时使用的提交

### [`--tag`](#-tag)

从 Git 添加依赖项时使用的标签

### [`--branch`](#-branch)

从 Git 添加依赖项时使用的分支

### [`--extra`](#-extra)

为依赖项启用的额外功能

### [`--no-sync`](#-no-sync)

避免同步虚拟环境 [env: UV_NO_SYNC=]

### [`--locked`](#-locked)

断言 `uv.lock` 将保持不变 [env: UV_LOCKED=]

### [`--frozen`](#-frozen)

添加依赖项而不重新锁定项目 [env: UV_FROZEN=]

### [`--active`](#-active)

优先使用活动虚拟环境而不是项目的虚拟环境

### [`--package`](#-package)

将依赖项添加到工作区中的特定包

### [`--script`](#-script)

将依赖项添加到指定的 Python 脚本，而不是项目

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

除了在注册表索引中找到的候选发行版之外，还要搜索的位置 [env: UV_FIND_LINKS=]

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

在为给定包要求选择不同兼容版本时使用的策略 [env: UV_RESOLUTION=] [可能的值：highest, lowest, lowest-direct]

### [`--prerelease`](#-prerelease)

考虑预发布版本时使用的策略 [env: UV_PRERELEASE=] [可能的值：disallow, allow, if-necessary, explicit, if-necessary-or-explicit]

### [`--fork-strategy`](#-fork-strategy)

在跨 Python 版本和平台选择给定包的多个版本时使用的策略 [env: UV_FORK_STRATEGY=] [可能的值：fewest, requires-python]

### [`--exclude-newer`](#-exclude-newer)

将候选包限制为在给定日期之前上传的包 [env: UV_EXCLUDE_NEWER=]

### [`--no-sources`](#-no-sources)

解析依赖项时忽略 `tool.uv.sources` 表。用于锁定符合标准的、可发布的包元数据，而不是使用任何工作区、Git、URL 或本地路径源

## Installer options

### [`--reinstall`](#-reinstall)

重新安装所有包，无论它们是否已经安装。隐含 `--refresh`

### [`--reinstall-package`](#-reinstall-package)

重新安装特定包，无论它是否已经安装。隐含 `--refresh-package`

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

用于解析和同步的 Python 解释器。[env: UV_PYTHON=]

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
