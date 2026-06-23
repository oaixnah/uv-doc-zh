---
subtitle: Environment variables
description: 本文档是 uv 项目的环境变量配置参考，详细列出了 uv 定义和遵循的所有环境变量，包括 UV_ASTRAL_MIRROR_URL、UV_CACHE_DIR、UV_PYTHON 等 uv 特有变量，以及 ALL_PROXY、AWS_ACCESS_KEY_ID、SSL_CERT_FILE 等外部定义变量，涵盖镜像配置、缓存管理、Python 安装、网络代理、TLS 证书、认证凭证等各个方面。
---

# 环境变量

uv 定义并遵循以下环境变量：

### `UV_ASTRAL_MIRROR_URL`
<small class="added-in">added in `0.11.14`</small>

用于替换所有 Astral 镜像元数据和制品下载的 `https://releases.astral.sh` 基础 URL。

设置后，uv 仅使用配置的镜像 URL，不会回退到 GitHub 或 raw GitHub。URL 中的路径组件将被保留：仅在追加正常路径后缀（例如 `/github/versions/main/v1/uv.ndjson`）之前修剪尾部斜杠。

这对于代理仓库（例如 Artifactory、Nexus）镜像 `releases.astral.sh` 非常有用。

更具体的源具有更高优先级：
[`UV_PYTHON_INSTALL_MIRROR`](Self::UV_PYTHON_INSTALL_MIRROR) 和 `python-install-mirror` 会覆盖此变量用于 CPython 下载，而
[`UV_INSTALLER_GITHUB_BASE_URL`](Self::UV_INSTALLER_GITHUB_BASE_URL) 和
[`UV_INSTALLER_GHE_BASE_URL`](Self::UV_INSTALLER_GHE_BASE_URL) 会覆盖此变量用于 `uv self update`。

### `UV_AZURE_ENDPOINT_URL`
<small class="added-in">added in `0.11.14`</small>

要视为 Azure Blob Storage 端点的 URL。对此端点的请求将使用 Azure 凭据进行签名，凭据来自默认凭据链，包括 Azure CLI 凭据和工作负载身份。

### `UV_BREAK_SYSTEM_PACKAGES`
<small class="added-in">added in `0.1.32`</small>

等同于 `--break-system-packages` 命令行参数。如果设置为 `true`，uv 将允许安装与系统安装的包冲突的包。

警告：`UV_BREAK_SYSTEM_PACKAGES=true` 适用于持续集成（CI）或容器化环境，应谨慎使用，因为修改系统 Python 可能导致意外行为。

### `UV_BUILD_CONSTRAINT`
<small class="added-in">added in `0.2.34`</small>

等同于 `--build-constraints` 命令行参数。如果设置，uv 将使用此文件作为任何源码分发构建的约束。使用空格分隔的文件列表。

### `UV_CACHE_DIR`
<small class="added-in">added in `0.0.5`</small>

等同于 `--cache-dir` 命令行参数。如果设置，uv 将使用此目录进行缓存，而不是默认缓存目录。

### `UV_COMPILE_BYTECODE`
<small class="added-in">added in `0.3.3`</small>

等同于 `--compile-bytecode` 命令行参数。如果设置，uv 将在安装后将 Python 源文件编译为字节码。

### `UV_COMPILE_BYTECODE_TIMEOUT`
<small class="added-in">added in `0.7.22`</small>

字节码编译的超时时间（秒）。

### `UV_CONCURRENT_BUILDS`
<small class="added-in">added in `0.1.43`</small>

设置 uv 在任何给定时间同时构建的源码分发的最大数量。

### `UV_CONCURRENT_DOWNLOADS`
<small class="added-in">added in `0.1.43`</small>

设置 uv 在任何给定时间同时进行中的并发下载的最大数量。

### `UV_CONCURRENT_INSTALLS`
<small class="added-in">added in `0.1.45`</small>

控制安装和解压包时使用的线程数。

### `UV_CONFIG_FILE`
<small class="added-in">added in `0.1.34`</small>

等同于 `--config-file` 命令行参数。期望一个本地 `uv.toml` 文件的路径作为配置文件使用。

### `UV_CONSTRAINT`
<small class="added-in">added in `0.1.36`</small>

等同于 `--constraints` 命令行参数。如果设置，uv 将使用此文件作为约束文件。使用空格分隔的文件列表。

### `UV_CREDENTIALS_DIR`
<small class="added-in">added in `0.8.15`</small>

使用纯文本后端时存储凭据的目录。

### `UV_CUSTOM_COMPILE_COMMAND`
<small class="added-in">added in `0.1.23`</small>

等同于 `--custom-compile-command` 命令行参数。

用于覆盖 `uv pip compile` 生成的 `requirements.txt` 文件输出头中的 uv。适用于在包装脚本中调用 `uv pip compile` 的场景，以便在输出文件中包含包装脚本的名称。

### `UV_DEFAULT_INDEX`
<small class="added-in">added in `0.4.23`</small>

等同于 `--default-index` 命令行参数。如果设置，uv 将使用此 URL 作为搜索包时的默认索引。

### `UV_DEV`
<small class="added-in">added in `0.8.7`</small>

等同于 `--dev` 命令行参数。如果设置，uv 将包含开发依赖项。

### `UV_DOWNLOAD_URL`
<small class="added-in">added in `0.8.4`</small>

使用独立安装器下载 uv 的 URL。默认从 uv 的 GitHub Releases 安装。`INSTALLER_DOWNLOAD_URL` 也作为别名受支持，用于向后兼容。

### `UV_ENV_FILE`
<small class="added-in">added in `0.4.30`</small>

执行 `uv run` 命令时从中加载环境变量的 `.env` 文件。

### `UV_EXCLUDE`
<small class="added-in">added in `0.9.8`</small>

等同于 `--excludes` 命令行参数。如果设置，uv 将使用此文件作为排除文件。使用空格分隔的文件列表。

### `UV_EXCLUDE_NEWER`
<small class="added-in">added in `0.2.12`</small>

等同于 `--exclude-newer` 命令行参数。如果设置，uv 将排除在指定日期之后发布的分发。

### `UV_EXTRA_INDEX_URL`
<small class="added-in">added in `0.1.3`</small>

等同于 `--extra-index-url` 命令行参数。如果设置，uv 将使用此空格分隔的 URL 列表作为搜索包时的额外索引。
（已弃用：请改用 `UV_INDEX`。）

### `UV_FIND_LINKS`
<small class="added-in">added in `0.4.19`</small>

等同于 `--find-links` 命令行参数。如果设置，uv 将使用此逗号分隔的额外位置列表来搜索包。

### `UV_FORK_STRATEGY`
<small class="added-in">added in `0.5.9`</small>

等同于 `--fork-strategy` 参数。在通用解析过程中控制版本选择。

### `UV_FROZEN`
<small class="added-in">added in `0.4.25`</small>

等同于 `--frozen` 命令行参数。如果设置，uv 将在不更新 `uv.lock` 文件的情况下运行。

### `UV_GCS_ENDPOINT_URL`
<small class="added-in">added in `0.9.26`</small>

要视为 GCS 兼容存储端点的 URL。对此端点的请求将使用 Google Cloud 身份验证进行签名，基于 `GOOGLE_APPLICATION_CREDENTIALS` 环境变量或应用默认凭据。

### `UV_GITHUB_TOKEN`
<small class="added-in">added in `0.4.10`</small>

等同于 self update 的 `--token` 参数。用于身份验证的 GitHub 令牌。

### `UV_GIT_LFS`
<small class="added-in">added in `0.5.19`</small>

启用从 Git 仓库安装包时获取存储在 Git LFS 中的文件。

### `UV_HIDE_BUILD_OUTPUT`
<small class="added-in">added in `0.9.15`</small>

在构建源码分发时抑制构建后端的输出，即使在构建失败时也如此。

### `UV_HTTP_CONNECT_TIMEOUT`
<small class="added-in">added in `0.10.0`</small>

连接服务器的超时时间（秒）。（默认值：10 秒）

如果 `UV_HTTP_TIMEOUT` 低于此值，则将使用 `UV_HTTP_TIMEOUT`。

### `UV_HTTP_RETRIES`
<small class="added-in">added in `0.7.21`</small>

HTTP 请求的重试次数。（默认值：3）

### `UV_HTTP_TIMEOUT`
<small class="added-in">added in `0.1.7`</small>

HTTP 读取的超时时间（秒）。（默认值：30 秒）

### `UV_INDEX`
<small class="added-in">added in `0.4.23`</small>

等同于 `--index` 命令行参数。如果设置，uv 将使用此空格分隔的 URL 列表作为搜索包时的额外索引。

### `UV_INDEX_STRATEGY`
<small class="added-in">added in `0.1.29`</small>

等同于 `--index-strategy` 命令行参数。

例如，如果设置为 `unsafe-best-match`，uv 将考虑给定包在所有索引 URL 中可用的版本，而不是将搜索限制在包含该包的第一个索引 URL。

### `UV_INDEX_URL`
<small class="added-in">added in `0.0.5`</small>

等同于 `--index-url` 命令行参数。如果设置，uv 将使用此 URL 作为搜索包时的默认索引。
（已弃用：请改用 `UV_DEFAULT_INDEX`。）

### `UV_INDEX_{name}_PASSWORD`
<small class="added-in">added in `0.4.23`</small>

为命名索引提供 HTTP Basic 身份验证密码。

`name` 参数是索引的名称。例如，对于名为 `foo` 的索引，环境变量键将是 `UV_INDEX_FOO_PASSWORD`。

### `UV_INDEX_{name}_USERNAME`
<small class="added-in">added in `0.4.23`</small>

为命名索引提供 HTTP Basic 身份验证用户名。

`name` 参数是索引的名称。例如，对于名为 `foo` 的索引，环境变量键将是 `UV_INDEX_FOO_USERNAME`。

### `UV_INIT_BARE`
<small class="added-in">added in `0.10.7`</small>

等同于 `uv init` 的 `--bare` 参数。如果设置，uv 将仅创建 `pyproject.toml`。

### `UV_INIT_BUILD_BACKEND`
<small class="added-in">added in `0.8.2`</small>

等同于 `uv init` 的 `--build-backend` 参数。确定创建新项目时使用的默认后端。

### `UV_INSECURE_HOST`
<small class="added-in">added in `0.3.5`</small>

等同于 `--allow-insecure-host` 参数。

### `UV_INSECURE_NO_ZIP_VALIDATION`
<small class="added-in">added in `0.8.6`</small>

禁用流式 wheel 和基于 ZIP 的源码分发的 ZIP 验证。

警告：禁用 ZIP 验证可能通过绕过完整性检查并使 uv 安装潜在恶意 ZIP 文件，使您的系统面临安全风险。如果 uv 因验证失败而拒绝某个 ZIP 文件，则该文件很可能格式错误；请考虑向包维护者提交问题。

### `UV_INSTALLER_GHE_BASE_URL`
<small class="added-in">added in `0.5.0`</small>

使用独立安装器和 `self update` 功能下载 uv 的 URL，替代默认的 GitHub Enterprise URL。

此更具体的安装器源优先于 `uv self update` 的 [`UV_ASTRAL_MIRROR_URL`](Self::UV_ASTRAL_MIRROR_URL)。

### `UV_INSTALLER_GITHUB_BASE_URL`
<small class="added-in">added in `0.5.0`</small>

使用独立安装器和 `self update` 功能下载 uv 的 URL，替代默认的 GitHub URL。

此更具体的安装器源优先于 `uv self update` 的 [`UV_ASTRAL_MIRROR_URL`](Self::UV_ASTRAL_MIRROR_URL)。

### `UV_INSTALL_DIR`
<small class="added-in">added in `0.5.0`</small>

使用独立安装器和 `self update` 功能安装 uv 的目录。默认为 `~/.local/bin`。

### `UV_ISOLATED`
<small class="added-in">added in `0.8.14`</small>

等同于 `--isolated` 命令行参数。如果设置，uv 将避免发现 `pyproject.toml` 或 `uv.toml` 文件。

### `UV_KEYRING_PROVIDER`
<small class="added-in">added in `0.1.19`</small>

等同于 `--keyring-provider` 命令行参数。如果设置，uv 将使用此值作为 keyring 提供程序。

### `UV_LIBC`
<small class="added-in">added in `0.7.22`</small>

在 Linux 系统上填充 Python 版本请求中的当前平台时，覆盖环境确定的 libc。选项包括：`gnu`、`gnueabi`、`gnueabihf`、`musl`、`musleabi`、`musleabihf` 和 `none`。

### `UV_LINK_MODE`
<small class="added-in">added in `0.1.40`</small>

等同于 `--link-mode` 命令行参数。如果设置，uv 将使用此值作为链接模式。

### `UV_LOCKED`
<small class="added-in">added in `0.4.25`</small>

等同于 `--locked` 命令行参数。如果设置，uv 将断言 `uv.lock` 保持不变。

### `UV_LOCK_TIMEOUT`
<small class="added-in">added in `0.9.4`</small>

uv 等待文件锁可用的时间（秒）。

默认为 300 秒（5 分钟）。

### `UV_LOG_CONTEXT`
<small class="added-in">added in `0.6.4`</small>

为日志消息添加额外的上下文和结构。

如果未启用日志记录（例如通过 `RUST_LOG` 或 `-v`），此设置无效。

### `UV_MALWARE_CHECK`
<small class="added-in">added in `0.11.16`</small>

设置为 `1` 以启用在 `uv sync` 后运行的自动恶意软件检查。

启用后，uv 会在每次锁文件同步后对 OSV 数据库执行轻量级检查，以查找已知恶意软件公告。将此变量设置为 `0` 可退出。

### `UV_MALWARE_CHECK_URL`
<small class="added-in">added in `0.11.16`</small>

覆盖自动恶意软件检查的漏洞服务 URL。

默认为 OSV API 端点（`https://api.osv.dev/`）。

### `UV_MANAGED_PYTHON`
<small class="added-in">added in `0.6.8`</small>

要求使用 uv 管理的 Python 版本。

### `UV_NATIVE_TLS`
<small class="added-in">added in `0.1.19`</small>

等同于 `--native-tls` 命令行参数。如果设置为 `true`，uv 将从平台的原生证书存储加载 TLS 证书，而不是捆绑的 Mozilla 根证书。
（已弃用：请改用 `UV_SYSTEM_CERTS`。）

### `UV_NO_BINARY`
<small class="added-in">added in `0.5.30`</small>

等同于 `--no-binary` 命令行参数。如果设置，uv 将安装所有包的源码版本。解析器仍将使用预构建的 wheel 来提取包元数据（如果可用）。

### `UV_NO_BINARY_PACKAGE`
<small class="added-in">added in `0.5.30`</small>

等同于 `--no-binary-package` 命令行参数。如果设置，uv 将不会为给定的空格分隔包列表使用预构建的 wheel。

### `UV_NO_BUILD`
<small class="added-in">added in `0.1.40`</small>

等同于 `--no-build` 命令行参数。如果设置，uv 将不会构建源码分发。

### `UV_NO_BUILD_ISOLATION`
<small class="added-in">added in `0.1.40`</small>

等同于 `--no-build-isolation` 命令行参数。如果设置，uv 将在构建源码分发时跳过隔离。

### `UV_NO_BUILD_PACKAGE`
<small class="added-in">added in `0.6.5`</small>

等同于 `--no-build-package` 命令行参数。如果设置，uv 将不会为给定的空格分隔包列表构建源码分发。

### `UV_NO_CACHE`
<small class="added-in">added in `0.1.2`</small>

等同于 `--no-cache` 命令行参数。如果设置，uv 将不会在任何操作中使用缓存。

### `UV_NO_CONFIG`
<small class="added-in">added in `0.2.30`</small>

等同于 `--no-config` 命令行参数。如果设置，uv 将不会从当前目录、父目录或用户配置目录中读取任何配置文件。

### `UV_NO_DEFAULT_GROUPS`
<small class="added-in">added in `0.9.9`</small>

等同于 `--no-default-groups` 命令行参数。如果设置，uv 将不会选择 `tool.uv.default-groups` 中定义的默认依赖组。

### `UV_NO_DEV`
<small class="added-in">added in `0.8.7`</small>

等同于 `--no-dev` 命令行参数。如果设置，uv 将排除开发依赖项。

### `UV_NO_EDITABLE`
<small class="added-in">added in `0.6.15`</small>

等同于 `--no-editable` 命令行参数。如果设置，uv 将以非可编辑模式安装或导出任何可编辑依赖项，包括项目和任何工作区成员。

### `UV_NO_ENV_FILE`
<small class="added-in">added in `0.4.30`</small>

执行 `uv run` 命令时忽略 `.env` 文件。

### `UV_NO_GITHUB_FAST_PATH`
<small class="added-in">added in `0.7.13`</small>

禁用 GitHub 特定请求，这些请求允许 uv 在某些情况下跳过 `git fetch`。

### `UV_NO_GROUP`
<small class="added-in">added in `0.9.8`</small>

等同于 `--no-group` 命令行参数。如果设置，uv 将为给定的空格分隔包列表禁用指定的依赖组。

### `UV_NO_HF_TOKEN`
<small class="added-in">added in `0.8.1`</small>

禁用 Hugging Face 身份验证，即使已设置 `HF_TOKEN`。

### `UV_NO_INSTALLER_METADATA`
<small class="added-in">added in `0.5.7`</small>

跳过将 `uv` 安装器元数据文件（例如 `INSTALLER`、`REQUESTED` 和 `direct_url.json`）写入 site-packages `.dist-info` 目录。

### `UV_NO_INSTALL_LOCAL`
<small class="added-in">added in `0.11.20`</small>

等同于 `--no-install-local` 命令行参数。如果设置，uv 将跳过当前项目、工作区成员以及任何其他本地（路径或可编辑）包，仅安装远程依赖项。

### `UV_NO_INSTALL_PROJECT`
<small class="added-in">added in `0.11.20`</small>

等同于 `--no-install-project` 命令行参数。如果设置，uv 将安装项目的依赖项，但不安装项目本身。

### `UV_NO_INSTALL_WORKSPACE`
<small class="added-in">added in `0.11.20`</small>

等同于 `--no-install-workspace` 命令行参数。如果设置，uv 将安装工作区依赖项，但不安装工作区成员（包括当前项目）。

### `UV_NO_MANAGED_PYTHON`
<small class="added-in">added in `0.6.8`</small>

禁用使用 uv 管理的 Python 版本。

### `UV_NO_MODIFY_PATH`
<small class="added-in">added in `0.8.4`</small>

使用独立安装器和 `self update` 功能安装 uv 时，避免修改 `PATH` 环境变量。`INSTALLER_NO_MODIFY_PATH` 也作为别名受支持，用于向后兼容。

### `UV_NO_PROGRESS`
<small class="added-in">added in `0.2.28`</small>

等同于 `--no-progress` 命令行参数。禁用所有进度输出。例如，旋转器和进度条。

### `UV_NO_PROJECT`
<small class="added-in">added in `0.11.8`</small>

等同于 `--no-project` 命令行参数。

### `UV_NO_SOURCES`
<small class="added-in">added in `0.9.8`</small>

等同于 `--no-sources` 命令行参数。如果设置，uv 将在解析依赖项时忽略 `[tool.uv.sources]` 注释。

### `UV_NO_SOURCES_PACKAGE`
<small class="added-in">added in `0.9.26`</small>

等同于 `--no-sources-package` 命令行参数。如果设置，uv 将为给定的空格分隔包列表忽略 `tool.uv.sources` 表。

### `UV_NO_SYNC`
<small class="added-in">added in `0.4.18`</small>

等同于 `--no-sync` 命令行参数。如果设置，uv 将跳过更新环境。

### `UV_NO_SYSTEM_CONFIG`
<small class="added-in">added in `0.11.16`</small>

如果设置，uv 将不会读取系统级配置文件。

### `UV_NO_VERIFY_HASHES`
<small class="added-in">added in `0.5.3`</small>

等同于 `--no-verify-hashes` 参数。禁用 `requirements.txt` 文件的哈希验证。

### `UV_NO_WRAP`
<small class="added-in">added in `0.0.5`</small>

用于禁用诊断信息的行换行。

### `UV_OFFLINE`
<small class="added-in">added in `0.5.9`</small>

等同于 `--offline` 命令行参数。如果设置，uv 将禁用网络访问。

### `UV_OVERRIDE`
<small class="added-in">added in `0.2.22`</small>

等同于 `--overrides` 命令行参数。如果设置，uv 将使用此文件作为覆盖文件。使用空格分隔的文件列表。

### `UV_PRERELEASE`
<small class="added-in">added in `0.1.16`</small>

等同于 `--prerelease` 命令行参数。例如，如果设置为 `allow`，uv 将允许所有依赖项的预发布版本。

### `UV_PREVIEW`
<small class="added-in">added in `0.1.37`</small>

等同于 `--preview` 参数。启用预览模式。

### `UV_PREVIEW_FEATURES`
<small class="added-in">added in `0.8.4`</small>

等同于 `--preview-features` 参数。启用特定的预览功能。

### `UV_PROJECT`
<small class="added-in">added in `0.4.4`</small>

等同于 `--project` 命令行参数。

### `UV_PROJECT_ENVIRONMENT`
<small class="added-in">added in `0.4.4`</small>

指定用于项目虚拟环境的目录路径。

请参阅[项目文档](../concepts/projects/config.md#project-environment-path)了解更多详情。

### `UV_PUBLISH_CHECK_URL`
<small class="added-in">added in `0.4.30`</small>

等同于 `uv publish` 中的 `--check-url` 命令行参数。如果文件已存在于索引上，则不上传。该值是索引的 URL。

### `UV_PUBLISH_INDEX`
<small class="added-in">added in `0.5.8`</small>

等同于 `uv publish` 中的 `--index` 命令行参数。如果设置，uv 将在发布时使用配置中具有此名称的索引。

### `UV_PUBLISH_NO_ATTESTATIONS`
<small class="added-in">added in `0.9.12`</small>

等同于 `uv publish` 中的 `--no-attestations` 命令行参数。如果设置，uv 将跳过上传任何已收集的发布分发的证明。

### `UV_PUBLISH_PASSWORD`
<small class="added-in">added in `0.4.16`</small>

等同于 `uv publish` 中的 `--password` 命令行参数。如果设置，uv 将使用此密码进行发布。

### `UV_PUBLISH_TOKEN`
<small class="added-in">added in `0.4.16`</small>

等同于 `uv publish` 中的 `--token` 命令行参数。如果设置，uv 将使用此令牌（用户名为 `__token__`）进行发布。

### `UV_PUBLISH_URL`
<small class="added-in">added in `0.4.16`</small>

等同于 `--publish-url` 命令行参数。与 `uv publish` 一起使用的索引上传端点的 URL。

### `UV_PUBLISH_USERNAME`
<small class="added-in">added in `0.4.16`</small>

等同于 `uv publish` 中的 `--username` 命令行参数。如果设置，uv 将使用此用户名进行发布。

### `UV_PYPY_INSTALL_MIRROR`
<small class="added-in">added in `0.2.35`</small>

托管的 PyPy 安装从 [python.org](https://downloads.python.org/) 下载。

此变量可以设置为镜像 URL，以使用不同的源进行 PyPy 安装。提供的 URL 将替换
`https://downloads.python.org/pypy`，例如在
`https://downloads.python.org/pypy/pypy3.8-v7.3.7-osx64.tar.bz2` 中。
可以使用 `file://` URL 方案从本地目录读取分发文件。

### `UV_PYTHON`
<small class="added-in">added in `0.1.40`</small>

等同于 `--python` 命令行参数。如果设置为路径，uv 将在所有操作中使用此 Python 解释器。

### `UV_PYTHON_BIN_DIR`
<small class="added-in">added in `0.4.29`</small>

指定放置已安装的托管 Python 可执行文件链接的目录。

### `UV_PYTHON_CACHE_DIR`
<small class="added-in">added in `0.7.0`</small>

指定用于在安装前缓存托管 Python 安装归档文件的目录。

### `UV_PYTHON_CPYTHON_BUILD`
<small class="added-in">added in `0.8.14`</small>

将托管 CPython 版本固定到特定的构建版本。

对于 CPython，这应该是构建日期（例如 `"20250814"`）。

### `UV_PYTHON_DOWNLOADS`
<small class="added-in">added in `0.3.2`</small>

等同于 [`python-downloads`](../reference/settings/configuration.md#python-downloads) 设置，以及在禁用时等同于 `--no-python-downloads` 选项。控制 uv 是否应允许 Python 下载。

### `UV_PYTHON_DOWNLOADS_JSON_URL`
<small class="added-in">added in `0.6.13`</small>

托管的 Python 安装信息硬编码在 `uv` 二进制文件中。

此变量可以设置为指向 Python 安装的 JSON 列表的本地路径或 URL，以覆盖硬编码列表。

这允许自定义下载的 URL 或使用比此 `uv` 构建中硬编码的版本稍旧或稍新的 Python 版本。

### `UV_PYTHON_GRAALPY_BUILD`
<small class="added-in">added in `0.8.14`</small>

将托管 GraalPy 版本固定到特定的构建版本。

对于 GraalPy，这应该是 GraalPy 版本（例如 `"24.2.2"`）。

### `UV_PYTHON_INSTALL_BIN`
<small class="added-in">added in `0.8.0`</small>

是否将 Python 可执行文件安装到 `UV_PYTHON_BIN_DIR` 目录中。

### `UV_PYTHON_INSTALL_DIR`
<small class="added-in">added in `0.2.22`</small>

指定用于存储托管 Python 安装的目录。

### `UV_PYTHON_INSTALL_MIRROR`
<small class="added-in">added in `0.2.35`</small>

托管的 Python 安装从 Astral 的 [`python-build-standalone`](https://github.com/astral-sh/python-build-standalone) 项目下载。

此变量可以设置为镜像 URL，以使用不同的源进行 Python 安装。提供的 URL 将替换
`https://github.com/astral-sh/python-build-standalone/releases/download`，例如在
`https://github.com/astral-sh/python-build-standalone/releases/download/20240713/cpython-3.12.4%2B20240713-aarch64-apple-darwin-install_only.tar.gz` 中。
可以使用 `file://` URL 方案从本地目录读取分发文件。

此更具体的镜像优先于 CPython 下载的 [`UV_ASTRAL_MIRROR_URL`](Self::UV_ASTRAL_MIRROR_URL)。

### `UV_PYTHON_INSTALL_REGISTRY`
<small class="added-in">added in `0.8.0`</small>

是否将 Python 可执行文件安装到 Windows 注册表中。

### `UV_PYTHON_NO_REGISTRY`
<small class="added-in">added in `0.11.8`</small>

禁用使用 Windows 注册表进行 Python 发现和注册。

设置后，uv 将不会从 Windows 注册表或 Microsoft Store 位置发现 Python 解释器，并且托管 Python 安装将不会注册到 Windows 注册表中。

### `UV_PYTHON_PREFERENCE`
<small class="added-in">added in `0.3.2`</small>

uv 是否应优先选择系统 Python 版本还是托管 Python 版本。

### `UV_PYTHON_PYODIDE_BUILD`
<small class="added-in">added in `0.8.14`</small>

将托管 Pyodide 版本固定到特定的构建版本。

对于 Pyodide，这应该是 Pyodide 版本（例如 `"0.28.1"`）。

### `UV_PYTHON_PYPY_BUILD`
<small class="added-in">added in `0.8.14`</small>

将托管 PyPy 版本固定到特定的构建版本。

对于 PyPy，这应该是 PyPy 版本（例如 `"7.3.20"`）。

### `UV_PYTHON_SEARCH_PATH`
<small class="added-in">added in `0.11.8`</small>

用于覆盖 `PATH` 以进行 Python 可执行文件发现。

设置后，uv 将在由此变量指定的目录中搜索 Python 解释器，而不是 `PATH`。

### `UV_REQUEST_TIMEOUT`
<small class="added-in">added in `0.1.6`</small>

HTTP 请求的超时时间（秒）。等同于 `UV_HTTP_TIMEOUT`。

### `UV_REQUIRE_HASHES`
<small class="added-in">added in `0.1.34`</small>

等同于 `--require-hashes` 命令行参数。如果设置为 `true`，uv 将要求所有依赖项在 requirements 文件中指定哈希值。

### `UV_RESOLUTION`
<small class="added-in">added in `0.1.27`</small>

等同于 `--resolution` 命令行参数。例如，如果设置为 `lowest-direct`，uv 将安装所有直接依赖项的最低兼容版本。

### `UV_S3_ENDPOINT_URL`
<small class="added-in">added in `0.8.21`</small>

要视为 S3 兼容存储端点的 URL。对此端点的请求将使用 AWS Signature Version 4 进行签名，基于 `AWS_ACCESS_KEY_ID`、`AWS_SECRET_ACCESS_KEY`、`AWS_PROFILE` 和 `AWS_CONFIG_FILE` 环境变量。

### `UV_SKIP_WHEEL_FILENAME_CHECK`
<small class="added-in">added in `0.8.23`</small>

在安装 wheel 时避免验证 wheel 文件名是否与其内容匹配。不建议使用此选项，因为文件名不一致的 wheel 应被视为无效，并应由相关包维护者修正；但是，此选项可在少数情况下用于绕过无效的制品。

### `UV_STACK_SIZE`
<small class="added-in">added in `0.0.5`</small>

用于设置 uv 使用的栈大小。

该值以字节为单位，如果 `UV_STACK_SIZE` 和 `RUST_MIN_STACK` 均未设置，uv 使用 4MB（4194304）栈。`UV_STACK_SIZE` 优先于 `RUST_MIN_STACK`。

与正常的 `RUST_MIN_STACK` 语义不同，这可以影响主线程栈大小，因为我们实际上会生成自己的 main2 线程来解决 Windows 真实主线程仅 1MB 的问题。该线程的大小为 `max(UV_STACK_SIZE, 1MB)`。

### `UV_SYSTEM_CERTS`
<small class="added-in">added in `0.11.0`</small>

等同于 `--system-certs` 命令行参数。如果设置为 `true`，uv 将从平台的原生证书存储加载 TLS 证书，而不是捆绑的 Mozilla 根证书。

### `UV_SYSTEM_PYTHON`
<small class="added-in">added in `0.1.18`</small>

等同于 `--system` 命令行参数。如果设置为 `true`，uv 将使用在系统 `PATH` 中找到的第一个 Python 解释器。

警告：`UV_SYSTEM_PYTHON=true` 适用于持续集成（CI）或容器化环境，应谨慎使用，因为修改系统 Python 可能导致意外行为。

### `UV_TEST_NO_HTTP_RETRY_DELAY`
<small class="added-in">added in `0.7.21`</small>

用于在测试中禁用 HTTP 重试延迟。

### `UV_TOOL_BIN_DIR`
<small class="added-in">added in `0.3.0`</small>

指定用于安装工具可执行文件的 "bin" 目录。

### `UV_TOOL_DIR`
<small class="added-in">added in `0.2.16`</small>

指定 uv 存储托管工具的目录。

### `UV_TORCH_BACKEND`
<small class="added-in">added in `0.6.9`</small>

等同于 `--torch-backend` 命令行参数（例如 `cpu`、`cu126` 或 `auto`）。

### `UV_UNMANAGED_INSTALL`
<small class="added-in">added in `0.5.0`</small>

用于 CI 等临时环境，将 uv 安装到特定路径，同时防止安装器修改 shell 配置文件或环境变量。

### `UV_UPLOAD_HTTP_TIMEOUT`
<small class="added-in">added in `0.9.1`</small>

仅用于上传 HTTP 请求的超时时间（秒）。（默认值：900 秒）

### `UV_VENV_CLEAR`
<small class="added-in">added in `0.8.0`</small>

等同于 `--clear` 命令行参数。如果设置，uv 将删除目标路径上任何现有的文件或目录。

### `UV_VENV_RELOCATABLE`
<small class="added-in">added in `0.10.8`</small>

等同于 `--relocatable` 命令行参数。如果设置，虚拟环境将是可重定位的。

### `UV_VENV_SEED`
<small class="added-in">added in `0.5.21`</small>

将种子包（以下一项或多项：`pip`、`setuptools` 和 `wheel`）安装到 `uv venv` 创建的虚拟环境中。

请注意，`setuptools` 和 `wheel` 不包含在 Python 3.12+ 环境中。

### `UV_WORKING_DIR`
<small class="added-in">added in `0.9.14`</small>

等同于 `--directory` 命令行参数。`UV_WORKING_DIRECTORY`（在 v0.9.1 中添加）也受支持用于向后兼容。



## 外部定义变量

uv 还会读取以下外部定义的环境变量：

### `ALL_PROXY`
<small class="added-in">added in `0.1.38`</small>

所有网络请求的通用代理。

### `ANDROID_API_LEVEL`
<small class="added-in">added in `0.8.16`</small>

与 `--python-platform aarch64-linux-android` 及相关变体一起使用，以设置 Android API 级别（即最低支持的 Android API 级别）。

默认为 `24`。

### `APPDATA`
<small class="added-in">added in `0.1.42`</small>

Windows 系统上用户级配置目录的路径。

### `AWS_ACCESS_KEY_ID`
<small class="added-in">added in `0.8.21`</small>

签名 S3 请求时使用的 AWS 访问密钥 ID。

### `AWS_CONFIG_FILE`
<small class="added-in">added in `0.8.21`</small>

签名 S3 请求时使用的 AWS 配置文件。

### `AWS_DEFAULT_REGION`
<small class="added-in">added in `0.8.21`</small>

签名 S3 请求时使用的默认 AWS 区域（如果未设置 `AWS_REGION`）。

### `AWS_PROFILE`
<small class="added-in">added in `0.8.21`</small>

签名 S3 请求时使用的 AWS 配置文件。

### `AWS_REGION`
<small class="added-in">added in `0.8.21`</small>

签名 S3 请求时使用的 AWS 区域。

### `AWS_SECRET_ACCESS_KEY`
<small class="added-in">added in `0.8.21`</small>

签名 S3 请求时使用的 AWS 秘密访问密钥。

### `AWS_SESSION_TOKEN`
<small class="added-in">added in `0.8.21`</small>

签名 S3 请求时使用的 AWS 会话令牌。

### `AWS_SHARED_CREDENTIALS_FILE`
<small class="added-in">added in `0.8.21`</small>

签名 S3 请求时使用的 AWS 共享凭据文件。

### `BASH_VERSION`
<small class="added-in">added in `0.1.28`</small>

用于检测 Bash shell 的使用。

### `CLICOLOR_FORCE`
<small class="added-in">added in `0.1.32`</small>

通过 `anstyle` 控制颜色。

### `COLUMNS`
<small class="added-in">added in `0.6.2`</small>

覆盖用于换行的终端宽度。uv 不直接读取此变量。

这是一个准标准变量，在 `ncurses(3x)` 等中有描述。

### `CONDA_DEFAULT_ENV`
<small class="added-in">added in `0.5.0`</small>

用于确定活动 Conda 环境的名称。

### `CONDA_PREFIX`
<small class="added-in">added in `0.0.5`</small>

用于检测活动 Conda 环境的路径。

### `DEPENDABOT`
<small class="added-in">added in `0.9.11`</small>

用于确定是否在 Dependabot 中运行。

### `FISH_VERSION`
<small class="added-in">added in `0.1.28`</small>

用于检测 Fish shell 的使用。

### `FORCE_COLOR`
<small class="added-in">added in `0.2.7`</small>

无论终端是否支持，强制彩色输出。

参见 [force-color.org](https://force-color.org)。

### `GITHUB_ACTIONS`
<small class="added-in">added in `0.4.16`</small>

表示当前进程正在 GitHub Actions 中运行。

设置为 `true` 时，`uv publish` 可能会尝试可信发布流程。

### `GITLAB_CI`
<small class="added-in">added in `0.8.18`</small>

表示当前进程正在 GitLab CI 中运行。

设置为 `true` 时，`uv publish` 可能会尝试可信发布流程。

### `HF_TOKEN`
<small class="added-in">added in `0.8.1`</small>

Hugging Face 请求的身份验证令牌。设置后，uv 在对 `https://huggingface.co/` 及其任何子域发出请求时将使用此令牌。

### `HOME`
<small class="added-in">added in `0.0.5`</small>

标准的 `HOME` 环境变量。

### `HTTPS_PROXY`
<small class="added-in">added in `0.1.38`</small>

HTTPS 请求的代理。

### `HTTP_PROXY`
<small class="added-in">added in `0.1.38`</small>

HTTP 请求的代理。

### `HTTP_TIMEOUT`
<small class="added-in">added in `0.1.7`</small>

HTTP 请求的超时时间（秒）。等同于 `UV_HTTP_TIMEOUT`。

### `IPHONEOS_DEPLOYMENT_TARGET`
<small class="added-in">added in `0.8.16`</small>

与 `--python-platform arm64-apple-ios` 及相关变体一起使用，以设置部署目标（即最低支持的 iOS 版本）。

默认为 `13.0`。

### `JPY_SESSION_NAME`
<small class="added-in">added in `0.2.6`</small>

用于检测在 Jupyter notebook 中运行。

### `KSH_VERSION`
<small class="added-in">added in `0.2.33`</small>

用于检测 Ksh shell 的使用。

### `LOCALAPPDATA`
<small class="added-in">added in `0.3.3`</small>

用于查找 Microsoft Store Python 安装。

### `MACOSX_DEPLOYMENT_TARGET`
<small class="added-in">added in `0.1.42`</small>

与 `--python-platform macos` 及相关变体一起使用，以设置部署目标（即最低支持的 macOS 版本）。

默认为 `13.0`，即撰写本文时最早的非 EOL macOS 版本。

### `NETRC`
<small class="added-in">added in `0.1.16`</small>

用于设置 .netrc 文件位置。

### `NO_COLOR`
<small class="added-in">added in `0.2.7`</small>

禁用彩色输出（优先于 `FORCE_COLOR`）。

参见 [no-color.org](https://no-color.org)。

### `NO_PROXY`
<small class="added-in">added in `0.1.38`</small>

逗号分隔的主机名（例如 `example.com`）和/或模式（例如 `192.168.1.0/24`）列表，这些应绕过代理。

### `NU_VERSION`
<small class="added-in">added in `0.1.16`</small>

用于检测 `NuShell` 的使用。

### `PAGER`
<small class="added-in">added in `0.4.18`</small>

标准的 `PAGER` posix 环境变量。`uv` 用于配置适当的 pager。

### `PATH`
<small class="added-in">added in `0.0.5`</small>

标准的 `PATH` 环境变量。

### `PROMPT`
<small class="added-in">added in `0.1.16`</small>

用于检测 Windows 命令提示符（与 PowerShell 相对）的使用。

### `PSModulePath`
<small class="added-in">added in `0.10.0`</small>

用于检测 PowerShell 的使用（由 PowerShell 在所有平台上设置）。

### `PWD`
<small class="added-in">added in `0.0.5`</small>

标准的 `PWD` posix 环境变量。

### `PYC_INVALIDATION_MODE`
<small class="added-in">added in `0.1.7`</small>

使用 `--compile` 运行时的验证模式。

参见 [`PycInvalidationMode`](https://docs.python.org/3/library/py_compile.html#py_compile.PycInvalidationMode)。

### `PYTHONPATH`
<small class="added-in">added in `0.1.22`</small>

将目录添加到 Python 模块搜索路径（例如 `PYTHONPATH=/path/to/modules`）。

### `PYX_API_KEY`
<small class="added-in">added in `0.8.15`</small>

pyx API 密钥（例如 `sk-pyx-...`）。

### `PYX_API_URL`
<small class="added-in">added in `0.8.15`</small>

pyx Simple API 服务器的 URL。

### `PYX_AUTH_TOKEN`
<small class="added-in">added in `0.8.15`</small>

pyx 身份验证令牌（例如 `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...`），由 `uv auth token` 输出。

### `PYX_CDN_DOMAIN`
<small class="added-in">added in `0.8.15`</small>

pyx CDN 的域名。

### `PYX_CREDENTIALS_DIR`
<small class="added-in">added in `0.8.15`</small>

指定 uv 存储 pyx 凭据的目录。

### `RUFF`
<small class="added-in">added in `0.11.22`</small>

`uv format` 使用的 Ruff 二进制文件路径。

### `RUST_BACKTRACE`
<small class="added-in">added in `0.7.22`</small>

如果设置，可用于在发生 panic 时显示更多栈跟踪详细信息。这在 Windows 上特别被 uv 用于在平台异常期间显示更多详细信息。

例如：

* `RUST_BACKTRACE=1` 将打印简短的回溯。
* `RUST_BACKTRACE=full` 将打印完整的回溯。

请参阅 [Rust backtrace 文档](https://doc.rust-lang.org/std/backtrace/index.html)了解更多信息。

### `RUST_LOG`
<small class="added-in">added in `0.0.5`</small>

如果设置，uv 将使用此值作为其 `--verbose` 输出的日志级别。接受任何与 `tracing_subscriber` crate 兼容的过滤器。

例如：

* `RUST_LOG=uv=debug` 等同于在命令行上添加 `--verbose`
* `RUST_LOG=trace` 将启用 trace 级别的日志记录。

请参阅 [tracing 文档](https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#example-syntax)了解更多信息。

### `RUST_MIN_STACK`
<small class="added-in">added in `0.5.19`</small>

用于设置 uv 使用的栈大小。

该值以字节为单位，如果 `UV_STACK_SIZE` 和 `RUST_MIN_STACK` 均未设置，uv 使用 4MB（4194304）栈。`UV_STACK_SIZE` 优先于 `RUST_MIN_STACK`。

建议设置 `UV_STACK_SIZE`，因为 `RUST_MIN_STACK` 也会影响子进程，例如使用 Rust 代码的构建后端。

与正常的 `RUST_MIN_STACK` 语义不同，这可以影响主线程栈大小，因为我们实际上会生成自己的 main2 线程来解决 Windows 真实主线程仅 1MB 的问题。该线程的大小为 `max(RUST_MIN_STACK, 1MB)`。

### `SHELL`
<small class="added-in">added in `0.1.16`</small>

标准的 `SHELL` posix 环境变量。

### `SSL_CERT_DIR`
<small class="added-in">added in `0.9.10`</small>

指向包含用于 TLS 连接的 PEM 编码 CA 证书文件的目录路径。

支持多个条目，使用平台特定的分隔符分隔（Unix 上为 `:`，Windows 上为 `;`）。

证书通常以 `.pem`、`.crt` 或 `.cer` 扩展名存储，但 uv 将尝试从提供的 `SSL_CERT_DIR` 中的任何常规文件读取证书。

无法解析为 PEM 证书的文件将被忽略。uv 会解析符号链接并忽略悬空符号链接。

仅支持 PEM 编码的文件，即不支持 DER 编码的文件。

设置后，这将覆盖默认证书源（捆绑的 Mozilla 根证书或系统证书）。仅信任此目录中的证书。

### `SSL_CERT_FILE`
<small class="added-in">added in `0.1.14`</small>

TLS 连接的 CA 证书捆绑文件路径。

需要 PEM 编码的证书文件（例如 `certs.pem`、`ca-bundle.crt`）。不支持 DER 编码的文件。

设置后，这将覆盖默认证书源（捆绑的 Mozilla 根证书或系统证书）。仅信任此文件中的证书。

### `SSL_CLIENT_CERT`
<small class="added-in">added in `0.2.11`</small>

如果设置，uv 将使用此文件进行 mTLS 身份验证。
这应该是一个包含证书和私钥的 PEM 格式单一文件。

### `SYSTEMDRIVE`
<small class="added-in">added in `0.4.26`</small>

Windows 系统上系统级配置目录的路径。

### `TRACING_DURATIONS_FILE`
<small class="added-in">added in `0.0.5`</small>

用于通过 `tracing-durations-export` 功能创建追踪持续时间文件。

### `TY`
<small class="added-in">added in `0.11.22`</small>

`uv check` 使用的 ty 二进制文件路径。

### `USERPROFILE`
<small class="added-in">added in `0.0.5`</small>

Windows 系统上用户配置文件根目录的路径。

### `UV`
<small class="added-in">added in `0.6.0`</small>

用于调用 uv 的二进制文件路径。

这将传播到 uv 生成的所有子进程。

如果可执行文件是通过符号链接调用的，某些平台将返回符号链接的路径，而其他平台将返回符号链接目标的路径。

有关安全注意事项，请参阅 <https://doc.rust-lang.org/std/env/fn.current_exe.html#security>。

### `VIRTUAL_ENV`
<small class="added-in">added in `0.0.5`</small>

用于检测已激活的虚拟环境。

### `VIRTUAL_ENV_DISABLE_PROMPT`
<small class="added-in">added in `0.0.5`</small>

如果在激活虚拟环境之前设置为 `1`，则虚拟环境名称将不会添加到终端提示符之前。

### `XDG_BIN_HOME`
<small class="added-in">added in `0.2.16`</small>

安装可执行文件的目录路径。

### `XDG_CACHE_HOME`
<small class="added-in">added in `0.1.17`</small>

Unix 系统上缓存目录的路径。

### `XDG_CONFIG_DIRS`
<small class="added-in">added in `0.4.26`</small>

Unix 系统上系统级配置目录的路径。

### `XDG_CONFIG_HOME`
<small class="added-in">added in `0.1.34`</small>

Unix 系统上用户级配置目录的路径。

### `XDG_DATA_HOME`
<small class="added-in">added in `0.2.16`</small>

用于存储托管 Python 安装和工具的目录路径。

### `ZDOTDIR`
<small class="added-in">added in `0.2.25`</small>

用于在使用 Zsh 时确定使用哪个 `.zshenv`。

### `ZSH_VERSION`
<small class="added-in">added in `0.1.28`</small>

用于检测 Zsh shell 的使用。

### `_CONDA_ROOT`
<small class="added-in">added in `0.8.18`</small>

用于确定 Conda 的根安装路径。
