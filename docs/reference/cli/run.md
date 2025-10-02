---
title: uv run
description: 运行命令或脚本。
---

# uv run

运行命令或脚本。

确保命令在 Python 环境中运行。

当与以 `.py` 结尾的文件或 HTTP(S) URL 一起使用时，该文件将被视为脚本并使用 Python
解释器运行，即 `uv run file.py` 等同于 `uv run python file.py`。对于 URL，脚本会在执行前临时
下载。如果脚本包含内联依赖元数据，它将被安装到一个隔离的、临时的环境中。当与 `-` 一起使用时，输入将从 stdin 读取，并被视为
Python 脚本。

在项目中使用时，项目环境将在调用命令之前创建和更新。

在项目外使用时，如果在当前目录或父目录中可以找到虚拟环境，命令将在该环境中运行。否则，命令将在发现的解释器环境中运行。

命令（或脚本）后面的参数不会被解释为 uv 的参数。所有 uv 选项必须在命令之前提供，例如 `uv run --verbose foo`。可以使用 `--`
来分隔命令和 uv 选项以提高清晰度，例如 `uv run --python 3.12 -- python`。

## Usage

```
uv run [OPTIONS] [COMMAND]
```

## Options

### [`--extra`](#-extra)

包含指定额外名称的可选依赖

### [`--all-extras`](#-all-extras)

包含所有可选依赖

### [`--no-extra`](#-no-extra)

如果提供了 `--all-extras`，则排除指定的可选依赖

### [`--no-dev`](#-no-dev)

禁用开发依赖组

### [`--group`](#-group)

包含指定依赖组的依赖

### [`--no-group`](#-no-group)

禁用指定的依赖组

### [`--no-default-groups`](#-no-default-groups)

忽略默认依赖组

### [`--only-group`](#-only-group)

仅包含指定依赖组的依赖

### [`--all-groups`](#-all-groups)

包含所有依赖组的依赖

### [`-m, --module`](#-m-module)

运行 Python 模块

### [`--only-dev`](#-only-dev)

仅包含开发依赖组

### [`--no-editable`](#-no-editable)

将任何可编辑依赖（包括项目和任何工作区成员）安装为
非可编辑 [env: UV_NO_EDITABLE=]

### [`--exact`](#-exact)

执行精确同步，移除多余的包

### [`--env-file`](#-env-file)

从 `.env` 文件加载环境变量 [env: UV_ENV_FILE=]

### [`--no-env-file`](#-no-env-file)

避免从 `.env` 文件读取环境变量 [env: UV_NO_ENV_FILE=]

### [`--with`](#-with)

运行时安装给定的包

### [`--with-editable`](#-with-editable)

以可编辑模式安装给定的包并运行

### [`--with-requirements`](#-with-requirements)

运行时安装给定 `requirements.txt` 文件中列出的所有包

### [`--isolated`](#-isolated)

在隔离的虚拟环境中运行命令

### [`--active`](#-active)

优先使用活动虚拟环境而不是项目的虚拟环境

### [`--no-sync`](#-no-sync)

避免同步虚拟环境 [env: UV_NO_SYNC=]

### [`--locked`](#-locked)

断言 `uv.lock` 将保持不变 [env: UV_LOCKED=]

### [`--frozen`](#-frozen)

运行时不更新 `uv.lock` 文件 [env: UV_FROZEN=]

### [`-s, --script`](#-s-script)

将给定路径作为 Python 脚本运行

### [`--gui-script`](#-gui-script)

将给定路径作为 Python GUI 脚本运行

### [`--all-packages`](#-all-packages)

运行命令时安装所有工作区成员

### [`--package`](#-package)

在工作区的特定包中运行命令

### [`--no-project`](#-no-project)

避免发现项目或工作区

## Index options

### [`--index`](#-index)

解析依赖时使用的 URL，除了默认索引之外 [env: UV_INDEX=]

### [`--default-index`](#-default-index)

默认包索引的 URL（默认为：<https://pypi.org/simple>）[env: UV_DEFAULT_INDEX=]

### [`-i, --index-url`](#-i-index-url)

（已弃用：请使用 `--default-index`）Python 包索引的 URL（默认为：<https://pypi.org/simple>）[env: UV_INDEX_URL=]

### [`--extra-index-url`](#-extra-index-url)

（已弃用：请使用 `--index`）除了 `--index-url` 之外要使用的额外包索引 URL [env: UV_EXTRA_INDEX_URL=]

### [`-f, --find-links`](#-f-find-links)

除了在注册表索引中找到的候选发行版之外，还要搜索的位置 [env: UV_FIND_LINKS=]

### [`--no-index`](#-no-index)

忽略注册表索引（例如 PyPI），而是依赖直接 URL 依赖和通过 `--find-links` 提供的依赖

### [`--index-strategy`](#-index-strategy)

针对多个索引 URL
进行解析时使用的策略 [env: UV_INDEX_STRATEGY=] [可能的值：first-index, unsafe-first-match, unsafe-best-match]

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

在跨 Python 版本和平台选择给定包的多个版本时使用的策略 [env: UV_FORK_STRATEGY=] [可能的值：fewest, requires-python]

### [`--exclude-newer`](#-exclude-newer)

将候选包限制为在给定日期之前上传的包 [env: UV_EXCLUDE_NEWER=]

### [`--no-sources`](#-no-sources)

解析依赖时忽略 `tool.uv.sources` 表。用于锁定符合标准的、可发布的包元数据，而不是使用任何工作区、Git、URL 或本地路径源

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

构建源发行版时禁用隔离 [env: UV_NO_BUILD_ISOLATION=]

### [`--no-build-isolation-package`](#-no-build-isolation-package)

为特定包构建源发行版时禁用隔离

### [`--no-build`](#-no-build)

不构建源发行版 [env: UV_NO_BUILD=]

### [`--no-build-package`](#-no-build-package)

不为特定包构建源发行版 [env: UV_NO_BUILD_PACKAGE=]

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

用于运行环境的 Python 解释器。[env: UV_PYTHON=]

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
