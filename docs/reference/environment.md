---
subtitle: Environment variables
---

# 环境变量

## uv 环境变量

### [`UV_BREAK_SYSTEM_PACKAGES`](#uv_break_system_packages)

等同于 `--break-system-packages` 命令行参数。如果设置为 `true`，uv 将允许安装与系统安装的软件包冲突的软件包。

警告：`UV_BREAK_SYSTEM_PACKAGES=true` 旨在用于持续集成 (CI) 或容器化环境，应谨慎使用，因为修改系统 Python 可能导致意外行为。

### [`UV_BUILD_CONSTRAINT`](#uv_build_constraint)

等同于 `--build-constraint` 命令行参数。如果设置，uv 将使用此文件作为任何源发行版构建的约束。使用以空格分隔的文件列表。

### [`UV_CACHE_DIR`](#uv_cache_dir)

等同于 `--cache-dir` 命令行参数。如果设置，uv 将使用此目录进行缓存，而不是默认的缓存目录。

### [`UV_COMPILE_BYTECODE`](#uv_compile_bytecode)

等同于 `--compile-bytecode` 命令行参数。如果设置，uv 将在安装后将 Python 源文件编译为字节码。

### [`UV_CONCURRENT_BUILDS`](#uv_concurrent_builds)

设置 uv 在任何给定时间将同时构建的源发行版的最大数量。

### [`UV_CONCURRENT_DOWNLOADS`](#uv_concurrent_downloads)

设置 uv 在任何给定时间将执行的正在进行的并发下载的最大数量。

### [`UV_CONCURRENT_INSTALLS`](#uv_concurrent_installs)

控制安装和解压缩软件包时使用的线程数。

### [`UV_CONFIG_FILE`](#uv_config_file)

等同于 `--config-file` 命令行参数。需要一个本地 `uv.toml` 文件的路径作为配置文件。

### [`UV_CONSTRAINT`](#uv_constraint)

等同于 `--constraint` 命令行参数。如果设置，uv 将使用此文件作为约束文件。使用以空格分隔的文件列表。

### [`UV_CUSTOM_COMPILE_COMMAND`](#uv_custom_compile_command)

等同于 `--custom-compile-command` 命令行参数。

用于在 `uv pip compile` 生成的 `requirements.txt` 文件的输出头中覆盖 uv。旨在用于从包装器脚本中调用 `uv pip compile`
的用例，以在输出文件中包含包装器脚本的名称。

### [`UV_DEFAULT_INDEX`](#uv_default_index)

等同于 `--default-index` 命令行参数。如果设置，uv 将在搜索软件包时使用此 URL 作为默认索引。

### [`UV_ENV_FILE`](#uv_env_file)

在执行 `uv run` 命令时从中加载环境变量的 `.env` 文件。

### [`UV_EXCLUDE_NEWER`](#uv_exclude_newer)

等同于 `--exclude-newer` 命令行参数。如果设置，uv 将排除在指定日期之后发布的发行版。

### [`UV_EXTRA_INDEX_URL`](#uv_extra_index_url)

等同于 `--extra-index-url` 命令行参数。如果设置，uv 将在搜索软件包时使用此以空格分隔的 URL 列表作为附加索引。
（已弃用：请改用 `UV_INDEX`。）

### [`UV_FIND_LINKS`](#uv_find_links)

等同于 `--find-links` 命令行参数。如果设置，uv 将使用此以逗号分隔的附加位置列表来搜索软件包。

### [`UV_FORK_STRATEGY`](#uv_fork_strategy)

等同于 `--fork-strategy` 参数。在通用解析期间控制版本选择。

### [`UV_FROZEN`](#uv_frozen)

等同于 `--frozen` 命令行参数。如果设置，uv 将在不更新 `uv.lock` 文件的情况下运行。

### [`UV_GITHUB_TOKEN`](#uv_github_token)

等同于 `self update` 的 `--token` 参数。用于身份验证的 GitHub 令牌。

### [`UV_GIT_LFS`](#uv_git_lfs)

在从 Git 存储库安装软件包时启用获取存储在 Git LFS 中的文件。

### [`UV_HTTP_TIMEOUT`](#uv_http_timeout)

HTTP 请求的超时时间（以秒为单位）。（默认值：30 秒）

### [`UV_INDEX`](#uv_index)

等同于 `--index` 命令行参数。如果设置，uv 将在搜索软件包时使用此以空格分隔的 URL 列表作为附加索引。

### [`UV_INDEX_STRATEGY`](#uv_index_strategy)

等同于 `--index-strategy` 命令行参数。

例如，如果设置为 `unsafe-best-match`，uv 将考虑在所有索引 URL 中可用的给定软件包的版本，而不是将其搜索限制在包含该软件包的第一个索引
URL。

### [`UV_INDEX_URL`](#uv_index_url)

等同于 `--index-url` 命令行参数。如果设置，uv 将在搜索软件包时使用此 URL 作为默认索引。
（已弃用：请改用 `UV_DEFAULT_INDEX`。）

### [`UV_INDEX_{name}_PASSWORD`](#uv_index_name_password)

提供命名索引的 HTTP 基本身份验证密码。

`name` 参数是索引的名称。例如，对于名为 `foo` 的索引，环境变量键将是 `UV_INDEX_FOO_PASSWORD`。

### [`UV_INDEX_{name}_USERNAME`](#uv_index_name_username)

提供命名索引的 HTTP 基本身份验证用户名。

`name` 参数是索引的名称。例如，对于名为 `foo` 的索引，环境变量键将是 `UV_INDEX_FOO_USERNAME`。

### [`UV_INSECURE_HOST`](#uv_insecure_host)

等同于 `--allow-insecure-host` 参数。

### [`UV_INSTALLER_GHE_BASE_URL`](#uv_installer_ghe_base_url)

使用独立安装程序和 `self update` 功能下载 uv 的 URL，以代替默认的 GitHub Enterprise URL。

### [`UV_INSTALLER_GITHUB_BASE_URL`](#uv_installer_github_base_url)

使用独立安装程序和 `self update` 功能下载 uv 的 URL，以代替默认的 GitHub URL。

### [`UV_INSTALL_DIR`](#uv_install_dir)

使用独立安装程序和 `self update` 功能安装 uv 的目录。
默认为 `~/.local/bin`。

### [`UV_KEYRING_PROVIDER`](#uv_keyring_provider)

等同于 `--keyring-provider` 命令行参数。如果设置，uv 将使用此值作为密钥环提供程序。

### [`UV_LINK_MODE`](#uv_link_mode)

等同于 `--link-mode` 命令行参数。如果设置，uv 将使用此作为链接模式。

### [`UV_LOCKED`](#uv_locked)

等同于 `--locked` 命令行参数。如果设置，uv 将断言 `uv.lock` 保持不变。

### [`UV_LOG_CONTEXT`](#uv_log_context)

向日志消息添加额外的上下文和结构。

如果未启用日志记录（例如，使用 `RUST_LOG` 或 `-v`），则此项无效。

### [`UV_MANAGED_PYTHON`](#uv_managed_python)

需要使用 uv 管理的 Python 版本。

### [`UV_NATIVE_TLS`](#uv_native_tls)

等同于 `--native-tls` 命令行参数。如果设置为 `true`，uv 将使用系统的信任存储区，而不是捆绑的 `webpki-roots` crate。

### [`UV_NO_BINARY`](#uv_no_binary)

等同于 `--no-binary` 命令行参数。如果设置，uv 将从源代码安装所有软件包。解析器仍将使用预构建的 wheel 来提取软件包元数据（如果可用）。

### [`UV_NO_BINARY_PACKAGE`](#uv_no_binary_package)

等同于 `--no-binary-package` 命令行参数。如果设置，uv 将不会对给定的以空格分隔的软件包列表使用预构建的 wheel。

### [`UV_NO_BUILD`](#uv_no_build)

等同于 `--no-build` 命令行参数。如果设置，uv 将不会构建源发行版。

### [`UV_NO_BUILD_ISOLATION`](#uv_no_build_isolation)

等同于 `--no-build-isolation` 命令行参数。如果设置，uv 将在构建源发行版时跳过隔离。

### [`UV_NO_BUILD_PACKAGE`](#uv_no_build_package)

等同于 `--no-build-package` 命令行参数。如果设置，uv 将不会为给定的以空格分隔的软件包列表构建源发行版。

### [`UV_NO_CACHE`](#uv_no_cache)

等同于 `--no-cache` 命令行参数。如果设置，uv 将不会对任何操作使用缓存。

### [`UV_NO_CONFIG`](#uv_no_config)

等同于 `--no-config` 命令行参数。如果设置，uv 将不会从当前目录、父目录或用户配置目录中读取任何配置文件。

### [`UV_NO_EDITABLE`](#uv_no_editable)

等同于 `--no-editable` 命令行参数。如果设置，uv 将安装任何可编辑的依赖项，包括项目和任何工作区成员，作为不可编辑的。

### [`UV_NO_ENV_FILE`](#uv_no_env_file)

在执行 `uv run` 命令时忽略 `.env` 文件。

### [`UV_NO_GITHUB_FAST_PATH`](#uv_no_github_fast_path)

禁用允许 uv 在某些情况下跳过 `git fetch` 的 GitHub 特定请求。

### [`UV_NO_INSTALLER_METADATA`](#uv_no_installer_metadata)

跳过将 `uv` 安装程序元数据文件（例如 `INSTALLER`、`REQUESTED` 和 `direct_url.json`）写入 site-packages `.dist-info` 目录。

### [`UV_NO_MANAGED_PYTHON`](#uv_no_managed_python)

禁用 uv 管理的 Python 版本。

### [`UV_NO_PROGRESS`](#uv_no_progress)

等同于 `--no-progress` 命令行参数。禁用所有进度输出。例如，旋转器和进度条。

### [`UV_NO_SYNC`](#uv_no_sync)

等同于 `--no-sync` 命令行参数。如果设置，uv 将跳过更新环境。

### [`UV_NO_VERIFY_HASHES`](#uv_no_verify_hashes)

等同于 `--no-verify-hashes` 参数。禁用 `requirements.txt` 文件的哈希验证。

### [`UV_NO_WRAP`](#uv_no_wrap)

用于禁用诊断的换行。

### [`UV_OFFLINE`](#uv_offline)

等同于 `--offline` 命令行参数。如果设置，uv 将禁用网络访问。

### [`UV_OVERRIDE`](#uv_override)

等同于 `--override` 命令行参数。如果设置，uv 将使用此文件作为覆盖文件。使用以空格分隔的文件列表。

### [`UV_PRERELEASE`](#uv_prerelease)

等同于 `--prerelease` 命令行参数。例如，如果设置为 `allow`，uv 将允许所有依赖项的预发布版本。

### [`UV_PREVIEW`](#uv_preview)

等同于 `--preview` 参数。启用预览模式。

### [`UV_PROJECT`](#uv_project)

等同于 `--project` 命令行参数。

### [`UV_PROJECT_ENVIRONMENT`](#uv_project_environment)

指定用于项目虚拟环境的目录路径。

有关更多详细信息，请参阅[项目文档](../concepts/projects/config.md#_9)。

### [`UV_PUBLISH_CHECK_URL`](#uv_publish_check_url)

如果文件已存在于索引中，则不要上传。该值是索引的 URL。

### [`UV_PUBLISH_INDEX`](#uv_publish_index)

等同于 `uv publish` 中的 `--index` 命令行参数。如果设置，uv 将在配置中使用此名称的索引进行发布。

### [`UV_PUBLISH_PASSWORD`](#uv_publish_password)

等同于 `uv publish` 中的 `--password` 命令行参数。如果设置，uv 将使用此密码进行发布。

### [`UV_PUBLISH_TOKEN`](#uv_publish_token)

等同于 `uv publish` 中的 `--token` 命令行参数。如果设置，uv 将使用此令牌（用户名为 `__token__`）进行发布。

### [`UV_PUBLISH_URL`](#uv_publish_url)

等同于 `--publish-url` 命令行参数。与 `uv publish` 一起使用的索引上传端点的 URL。

### [`UV_PUBLISH_USERNAME`](#uv_publish_username)

等同于 `uv publish` 中的 `--username` 命令行参数。如果设置，uv 将使用此用户名进行发布。

### [`UV_PYPY_INSTALL_MIRROR`](#uv_pypy_install_mirror)

托管的 PyPy 安装从 [python.org](https://downloads.python.org/) 下载。

此变量可以设置为镜像 URL，以使用不同的 PyPy 安装源。提供的 URL 将替换
`https://downloads.python.org/pypy`，例如，在 `https://downloads.python.org/pypy/pypy3.8-v7.3.7-osx64.tar.bz2` 中。
可以使用 `file://` URL 方案从本地目录读取发行版。

### [`UV_PYTHON`](#uv_python)

等同于 `--python` 命令行参数。如果设置为路径，uv 将对所有操作使用此 Python 解释器。

### [`UV_PYTHON_BIN_DIR`](#uv_python_bin_dir)

指定放置已安装的、托管的 Python 可执行文件链接的目录。

### [`UV_PYTHON_CACHE_DIR`](#uv_python_cache_dir)

指定在安装前缓存托管 Python 安装存档的目录。

### [`UV_PYTHON_DOWNLOADS`](#uv_python_downloads)

等同于 [`python-downloads`](../reference/settings/configuration.md#python-downloads) 设置，以及在禁用时，`--no-python-downloads` 选项。uv
是否应允许 Python 下载。

### [`UV_PYTHON_DOWNLOADS_JSON_URL`](#uv_python_downloads_json_url)

托管的 Python 安装信息硬编码在 `uv` 二进制文件中。

此变量可以设置为指向 JSON 的 URL，以用作 Python 安装列表。这将允许设置 Python 安装的每个属性，主要是用于离线镜像的 url 部分。

请注意，目前仅支持本地路径。

### [`UV_PYTHON_INSTALL_DIR`](#uv_python_install_dir)

指定存储托管 Python 安装的目录。

### [`UV_PYTHON_INSTALL_MIRROR`](#uv_python_install_mirror)

托管的 Python 安装从 Astral [`python-build-standalone`](https://github.com/astral-sh/python-build-standalone) 项目下载。

此变量可以设置为镜像 URL，以使用不同的 Python 安装源。提供的 URL 将替换
`https://github.com/astral-sh/python-build-standalone/releases/download`，例如，在 `https://github.com/astral-sh/python-build-standalone/releases/download/20240713/cpython-3.12.4%2B20240713-aarch64-apple-darwin-install_only.tar.gz` 中。
可以使用 `file://` URL 方案从本地目录读取发行版。

### [`UV_PYTHON_PREFERENCE`](#uv_python_preference)

uv 是否应首选系统或托管的 Python 版本。

### [`UV_REQUEST_TIMEOUT`](#uv_request_timeout)

HTTP 请求的超时时间（以秒为单位）。等同于 `UV_HTTP_TIMEOUT`。

### [`UV_REQUIRE_HASHES`](#uv_require_hashes)

等同于 `--require-hashes` 命令行参数。如果设置为 `true`，uv 将要求所有依赖项在需求文件中都指定了哈希值。

### [`UV_RESOLUTION`](#uv_resolution)

等同于 `--resolution` 命令行参数。例如，如果设置为 `lowest-direct`，uv 将安装所有直接依赖项的最低兼容版本。

### [`UV_STACK_SIZE`](#uv_stack_size)

用于设置 uv 使用的堆栈大小。

该值以字节为单位，如果 `UV_STACK_SIZE` 和 `RUST_MIN_STACK` 都未设置，uv 将使用 4MB (4194304) 的堆栈。`UV_STACK_SIZE` 优先于
`RUST_MIN_STACK`。

与正常的 `RUST_MIN_STACK` 语义不同，这可能会影响主线程堆栈大小，因为我们实际上生成了自己的 main2 线程来解决 Windows
真正的主线程只有 1MB 的问题。该线程的大小为 `max(UV_STACK_SIZE, 1MB)`。

### [`UV_SYSTEM_PYTHON`](#uv_system_python)

等同于 `--system` 命令行参数。如果设置为 `true`，uv 将使用在系统 `PATH` 中找到的第一个 Python 解释器。

警告：`UV_SYSTEM_PYTHON=true` 旨在用于持续集成 (CI) 或容器化环境，应谨慎使用，因为修改系统 Python 可能导致意外行为。

### [`UV_TOOL_BIN_DIR`](#uv_tool_bin_dir)

指定用于安装工具可执行文件的“bin”目录。

### [`UV_TOOL_DIR`](#uv_tool_dir)

指定 uv 存储托管工具的目录。

### [`UV_TORCH_BACKEND`](#uv_torch_backend)

等同于 `--torch-backend` 命令行参数（例如，`cpu`、`cu126` 或 `auto`）。

### [`UV_UNMANAGED_INSTALL`](#uv_unmanaged_install)

用于 CI 等临时环境，将 uv 安装到特定路径，同时防止安装程序修改 shell 配置文件或环境变量。

### [`UV_VENV_SEED`](#uv_venv_seed)

将种子包（`pip`、`setuptools` 和 `wheel` 中的一个或多个）安装到 `uv venv` 创建的虚拟环境中。

请注意，`setuptools` 和 `wheel` 不包含在 Python 3.12+ 环境中。

## 外部定义变量

uv 还读取以下外部定义的环境变量：

### [`ACTIONS_ID_TOKEN_REQUEST_TOKEN`](#actions_id_token_request_token)

用于通过 `uv publish` 进行可信发布。包含 oidc 请求令牌。

### [`ACTIONS_ID_TOKEN_REQUEST_URL`](#actions_id_token_request_url)

用于通过 `uv publish` 进行可信发布。包含 oidc 令牌 url。

### [`ALL_PROXY`](#all_proxy)

所有网络请求的通用代理。

### [`APPDATA`](#appdata)

Windows 系统上用户级配置目录的路径。

### [`BASH_VERSION`](#bash_version)

用于检测 Bash shell 的使用情况。

### [`CLICOLOR_FORCE`](#clicolor_force)

用于通过 `anstyle` 控制颜色。

### [`COLUMNS`](#columns)

覆盖用于换行的终端宽度。此变量不由 uv 直接读取。

这是一个准标准变量，例如在 `ncurses(3x)` 中有描述。

### [`CONDA_DEFAULT_ENV`](#conda_default_env)

用于确定活动的 Conda 环境是否为基础环境。

### [`CONDA_PREFIX`](#conda_prefix)

用于检测已激活的 Conda 环境。

### [`FISH_VERSION`](#fish_version)

用于检测 Fish shell 的使用情况。

### [`FORCE_COLOR`](#force_color)

无论终端支持如何，都强制使用彩色输出。

请参阅 [force-color.org](https://force-color.org)。

### [`GITHUB_ACTIONS`](#github_actions)

用于通过 `uv publish` 进行可信发布。

### [`HOME`](#home)

标准的 `HOME` 环境变量。

### [`HTTPS_PROXY`](#https_proxy)

HTTPS 请求的代理。

### [`HTTP_PROXY`](#http_proxy)

HTTP 请求的代理。

### [`HTTP_TIMEOUT`](#http_timeout)

HTTP 请求的超时时间（以秒为单位）。等同于 `UV_HTTP_TIMEOUT`。

### [`INSTALLER_NO_MODIFY_PATH`](#installer_no_modify_path)

在使用独立安装程序和 `self update` 功能安装 uv 时，避免修改 `PATH` 环境变量。

### [`JPY_SESSION_NAME`](#jpy_session_name)

用于检测在 Jupyter notebook 中运行的情况。

### [`KSH_VERSION`](#ksh_version)

用于检测 Ksh shell 的使用情况。

### [`LOCALAPPDATA`](#localappdata)

用于查找 Microsoft Store Pythons 安装。

### [`MACOSX_DEPLOYMENT_TARGET`](#macosx_deployment_target)

与 `--python-platform macos` 及相关变体一起使用，以设置部署目标（即支持的最低 macOS 版本）。

默认为 `13.0`，即撰写本文时最新的非 EOL macOS 版本。

### [`NETRC`](#netrc)

用于设置 .netrc 文件的位置。

### [`NO_COLOR`](#no_color)

禁用彩色输出（优先于 `FORCE_COLOR`）。

请参阅 [no-color.org](https://no-color.org)。

### [`NU_VERSION`](#nu_version)

用于检测 `NuShell` 的使用情况。

### [`PAGER`](#pager)

标准的 `PAGER` posix 环境变量。`uv` 使用它来配置适当的分页器。

### [`PATH`](#path)

标准的 `PATH` 环境变量。

### [`PROMPT`](#prompt)

用于检测 Windows 命令提示符（而不是 PowerShell）的使用情况。

### [`PWD`](#pwd)

标准的 `PWD` posix 环境变量。

### [`PYC_INVALIDATION_MODE`](#pyc_invalidation_mode)

与 `--compile` 一起运行时使用的验证模式。

请参阅 [`PycInvalidationMode`](https://docs.python.org/3/library/py_compile.html#py_compile.PycInvalidationMode)。

### [`PYTHONPATH`](#pythonpath)

将目录添加到 Python 模块搜索路径（例如，`PYTHONPATH=/path/to/modules`）。

### [`RUST_LOG`](#rust_log)

如果设置，uv 将使用此值作为其 `--verbose` 输出的日志级别。接受与 `tracing_subscriber` crate 兼容的任何过滤器。

例如：

* `RUST_LOG=uv=debug` 等同于在命令行中添加 `--verbose`
* `RUST_LOG=trace` 将启用跟踪级日志记录。

有关更多信息，请参阅 [tracing 文档](https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#example-syntax)。

### [`RUST_MIN_STACK`](#rust_min_stack)

用于设置 uv 使用的堆栈大小。

该值以字节为单位，如果 `UV_STACK_SIZE` 和 `RUST_MIN_STACK` 都未设置，uv 将使用 4MB (4194304) 的堆栈。`UV_STACK_SIZE` 优先于
`RUST_MIN_STACK`。

建议设置 `UV_STACK_SIZE`，因为 `RUST_MIN_STACK` 也会影响子进程，例如使用 Rust 代码的构建后端。

与正常的 `RUST_MIN_STACK` 语义不同，这可能会影响主线程堆栈大小，因为我们实际上生成了自己的 main2 线程来解决 Windows
真正的主线程只有 1MB 的问题。该线程的大小为 `max(RUST_MIN_STACK, 1MB)`。

### [`SHELL`](#shell)

标准的 `SHELL` posix 环境变量。

### [`SSL_CERT_FILE`](#ssl_cert_file)

用于 SSL 连接的自定义证书捆绑文件路径。

### [`SSL_CLIENT_CERT`](#ssl_client_cert)

如果设置，uv 将使用此文件进行 mTLS 身份验证。
这应该是一个包含证书和私钥的 PEM 格式的单个文件。

### [`SYSTEMDRIVE`](#systemdrive)

Windows 系统上系统级配置目录的路径。

### [`TRACING_DURATIONS_FILE`](#tracing_durations_file)

用于通过 `tracing-durations-export` 功能创建跟踪持续时间文件。

### [`USERPROFILE`](#userprofile)

Windows 系统上用户配置文件根目录的路径。

### [`UV`](#uv)

用于调用 uv 的二进制文件的路径。

这将传播到 uv 生成的所有子进程。

如果可执行文件是通过符号链接调用的，某些平台将返回符号链接的路径，而其他平台将返回符号链接目标的路径。

有关安全注意事项，请参阅 <https://doc.rust-lang.org/std/env/fn.current_exe.html#security>。

### [`VIRTUAL_ENV`](#virtual_env)

用于检测已激活的虚拟环境。

### [`VIRTUAL_ENV_DISABLE_PROMPT`](#virtual_env_disable_prompt)

如果在激活虚拟环境之前设置为 `1`，则虚拟环境名称不会前置到终端提示符。

### [`XDG_BIN_HOME`](#xdg_bin_home)

安装可执行文件的目录路径。

### [`XDG_CACHE_HOME`](#xdg_cache_home)

Unix 系统上缓存目录的路径。

### [`XDG_CONFIG_DIRS`](#xdg_config_dirs)

Unix 系统上系统级配置目录的路径。

### [`XDG_CONFIG_HOME`](#xdg_config_home)

Unix 系统上用户级配置目录的路径。

### [`XDG_DATA_HOME`](#xdg_data_home)

用于存储托管的 Python 安装和工具的目录路径。

### [`ZDOTDIR`](#zdotdir)

用于确定在使用 Zsh 时使用哪个 `.zshenv`。

### [`ZSH_VERSION`](#zsh_version)

用于检测 Zsh shell 的使用情况。
