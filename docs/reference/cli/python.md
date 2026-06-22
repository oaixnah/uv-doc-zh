---
title: uv python
description: uv python 命令行参考文档，涵盖安装、列出、查找、升级、卸载、锁定 Python 版本，以及管理 Python 安装目录和 PATH 配置的完整中文命令参考。
---

# uv python

管理 Python 版本和安装。

通常，uv 首先会在虚拟环境中搜索 Python，无论是当前激活的虚拟环境，还是当前工作目录或任意父目录中的 `.venv` 目录。如果不需要虚拟环境，uv 则会搜索 Python 解释器。Python 解释器通过搜索 `PATH` 环境变量中的 Python 可执行文件来查找。

在 Windows 上，还会搜索注册表中的 Python 可执行文件。

默认情况下，如果找不到所需版本，uv 会下载 Python。可以通过 `--no-python-downloads` 标志或 `python-downloads` 设置来禁用此行为。

`--python` 选项用于请求不同的解释器。

支持以下 Python 版本请求格式：

- `<version>`，例如 `3`、`3.12`、`3.12.3`
- `<version-specifier>`（版本指定符），例如 `>=3.12,<3.13`
- `<version><short-variant>`（短变体），例如 `3.13t`、`3.12.0d`
- `<version>+<variant>`（变体），例如 `3.13+freethreaded`、`3.12.0+debug`
- `<implementation>`（实现），例如 `cpython` 或 `cp`
- `<implementation>@<version>`（实现@版本），例如 `cpython@3.12`
- `<implementation><version>`（实现版本），例如 `cpython3.12` 或 `cp312`
- `<implementation><version-specifier>`（实现版本指定符），例如 `cpython>=3.12,<3.13`
- `<implementation>-<version>-<os>-<arch>-<libc>`，例如 `cpython-3.12.3-macos-aarch64-none`

此外，通常可以通过以下方式请求特定的系统 Python 解释器：

- `<executable-path>`（可执行文件路径），例如 `/opt/homebrew/bin/python3`
- `<executable-name>`（可执行文件名称），例如 `mypython3`
- `<install-dir>`（安装目录），例如 `/some/environment/`

当使用 `--python` 选项时，正常的发现规则仍然适用，但发现的解释器会与请求进行兼容性检查，例如，如果请求 `pypy`，uv 会首先检查虚拟环境中是否包含 PyPy 解释器，然后检查路径中的每个可执行文件是否为 PyPy 解释器。

uv 支持发现 CPython、PyPy 和 GraalPy 解释器。不受支持的解释器将在发现过程中被跳过。如果请求了不受支持的解释器实现，uv 将退出并报错。

<h3 class="cli-reference">用法</h3>

```
uv python [OPTIONS] <COMMAND>
```

<h3 class="cli-reference">命令</h3>

<dl class="cli-reference"><dt><a href="#uv-python-list"><code>uv python list</code></a></dt><dd><p>列出可用的 Python 安装</p></dd>
<dt><a href="#uv-python-install"><code>uv python install</code></a></dt><dd><p>下载并安装 Python 版本</p></dd>
<dt><a href="#uv-python-upgrade"><code>uv python upgrade</code></a></dt><dd><p>升级已安装的 Python 版本</p></dd>
<dt><a href="#uv-python-find"><code>uv python find</code></a></dt><dd><p>搜索 Python 安装</p></dd>
<dt><a href="#uv-python-pin"><code>uv python pin</code></a></dt><dd><p>锁定到特定的 Python 版本</p></dd>
<dt><a href="#uv-python-dir"><code>uv python dir</code></a></dt><dd><p>显示 uv Python 安装目录</p></dd>
<dt><a href="#uv-python-uninstall"><code>uv python uninstall</code></a></dt><dd><p>卸载 Python 版本</p></dd>
<dt><a href="#uv-python-update-shell"><code>uv python update-shell</code></a></dt><dd><p>确保 Python 可执行文件目录在 <code>PATH</code> 中</p></dd>
</dl>

### uv python list

列出可用的 Python 安装。

默认情况下，会显示已安装的 Python 版本以及每个受支持的 Python 主版本的最新可用补丁版本的下载信息。

使用 `--managed-python` 仅查看由 uv 管理的 Python 版本。

使用 `--no-managed-python` 忽略由 uv 管理的 Python 版本。

使用 `--all-versions` 查看所有可用的补丁版本。

使用 `--only-installed` 忽略可用的下载信息。

<h3 class="cli-reference">用法</h3>

```
uv python list [OPTIONS] [REQUEST]
```

<h3 class="cli-reference">参数</h3>

<dl class="cli-reference"><dt id="uv-python-list--request"><a href="#uv-python-list--request"><code>REQUEST</code></a></dt><dd><p>用于过滤的 Python 请求。</p>
<p>请参阅 <a href="#uv-python">uv python</a> 了解支持的请求格式。</p>
</dd></dl>

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-python-list--all-arches"><a href="#uv-python-list--all-arches"><code>--all-arches</code></a>, <code>--all_architectures</code></dt><dd><p>列出所有架构的 Python 下载。</p>
<p>默认情况下，仅显示当前架构的下载。</p>
</dd><dt id="uv-python-list--all-platforms"><a href="#uv-python-list--all-platforms"><code>--all-platforms</code></a></dt><dd><p>列出所有平台的 Python 下载。</p>
<p>默认情况下，仅显示当前平台的下载。</p>
</dd><dt id="uv-python-list--all-versions"><a href="#uv-python-list--all-versions"><code>--all-versions</code></a></dt><dd><p>列出所有 Python 版本，包括旧的补丁版本。</p>
<p>默认情况下，每个次要版本仅显示最新的补丁版本。</p>
</dd><dt id="uv-python-list--allow-insecure-host"><a href="#uv-python-list--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会通过系统的证书存储进行验证。仅在安全的网络中使用 <code>--allow-insecure-host</code>，并确保来源可信，因为它会绕过 SSL 验证，可能使您面临中间人攻击（MITM）的风险。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-python-list--cache-dir"><a href="#uv-python-list--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-python-list--color"><a href="#uv-python-list--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>：仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-python-list--config-file"><a href="#uv-python-list--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许这样做。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-python-list--directory"><a href="#uv-python-list--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径以指定目录为基准进行解析。</p>
<p>请参阅 <code>--project</code> 仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-python-list--help"><a href="#uv-python-list--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助</p>
</dd><dt id="uv-python-list--managed-python"><a href="#uv-python-list--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁止使用系统 Python 版本。</p>
</dd><dt id="uv-python-list--no-cache"><a href="#uv-python-list--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-python-list--no-config"><a href="#uv-python-list--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常情况下，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-python-list--no-managed-python"><a href="#uv-python-list--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用使用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-python-list--no-progress"><a href="#uv-python-list--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转器或进度条。</p>
</dd><dt id="uv-python-list--no-python-downloads"><a href="#uv-python-list--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-python-list--offline"><a href="#uv-python-list--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-python-list--only-downloads"><a href="#uv-python-list--only-downloads"><code>--only-downloads</code></a></dt><dd><p>仅显示可用的 Python 下载。</p>
<p>默认情况下，会显示已安装的发行版和当前平台可用的下载。</p>
</dd><dt id="uv-python-list--only-installed"><a href="#uv-python-list--only-installed"><code>--only-installed</code></a></dt><dd><p>仅显示已安装的 Python 版本。</p>
<p>默认情况下，会显示已安装的发行版和当前平台可用的下载。</p>
</dd><dt id="uv-python-list--output-format"><a href="#uv-python-list--output-format"><code>--output-format</code></a> <i>output-format</i></dt><dd><p>选择输出格式</p>
<p>[默认值: text]</p><p>可选值：</p>
<ul>
<li><code>text</code>：纯文本（供人类阅读）</li>
<li><code>json</code>：JSON（供计算机处理）</li>
</ul></dd><dt id="uv-python-list--project"><a href="#uv-python-list--project"><code>--project</code></a> <i>project</i></dt><dd><p>在指定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>请参阅 <code>--directory</code> 完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-python-list--python-downloads-json-url"><a href="#uv-python-list--python-downloads-json-url"><code>--python-downloads-json-url</code></a> <i>python-downloads-json-url</i></dt><dd><p>指向自定义 Python 安装 JSON 的 URL</p>
</dd><dt id="uv-python-list--quiet"><a href="#uv-python-list--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项（例如 <code>-qq</code>）将启用静默模式，此时 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-python-list--show-urls"><a href="#uv-python-list--show-urls"><code>--show-urls</code></a></dt><dd><p>显示可用 Python 下载的 URL。</p>
<p>默认情况下，这些显示为 <code>&lt;download available&gt;</code>。</p>
</dd><dt id="uv-python-list--system-certs"><a href="#uv-python-list--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能希望使用平台的原生证书存储，特别是当您依赖包含在系统证书存储中的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-python-list--verbose"><a href="#uv-python-list--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>

### uv python install

下载并安装 Python 版本。

支持 CPython 和 PyPy。CPython 发行版从 Astral 的 `python-build-standalone` 项目下载。PyPy 发行版从 `python.org` 下载。可用的 Python 版本随每个 uv 发行版捆绑发布。要安装新的 Python 版本，您可能需要升级 uv。

Python 版本安装到 uv Python 目录中，可以通过 `uv python dir` 获取该目录。

默认情况下，Python 可执行文件会添加到路径中的目录中，并带有次要版本后缀，例如 `python3.13`。要安装 `python3` 和 `python`，请使用 `--default` 标志。使用 `uv python dir --bin` 查看目标目录。

可以请求多个 Python 版本。

请参阅 `uv help python` 了解支持的请求格式。

<h3 class="cli-reference">用法</h3>

```
uv python install [OPTIONS] [TARGETS]...
```

<h3 class="cli-reference">参数</h3>

<dl class="cli-reference"><dt id="uv-python-install--targets"><a href="#uv-python-install--targets"><code>TARGETS</code></a></dt><dd><p>要安装的 Python 版本。</p>
<p>如果未提供，请求的 Python 版本将从 <code>UV_PYTHON</code> 环境变量中读取，然后从 <code>.python-versions</code> 或 <code>.python-version</code> 文件中读取。如果以上都没有，uv 将检查是否已安装任何 Python 版本。如果没有，它将安装最新的稳定 Python 版本。</p>
<p>请参阅 <a href="#uv-python">uv python</a> 了解支持的请求格式。</p>
</dd></dl>

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-python-install--allow-insecure-host"><a href="#uv-python-install--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会通过系统的证书存储进行验证。仅在安全的网络中使用 <code>--allow-insecure-host</code>，并确保来源可信，因为它会绕过 SSL 验证，可能使您面临中间人攻击（MITM）的风险。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-python-install--cache-dir"><a href="#uv-python-install--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-python-install--color"><a href="#uv-python-install--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>：仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-python-install--compile-bytecode"><a href="#uv-python-install--compile-bytecode"><code>--compile-bytecode</code></a>, <code>--compile</code></dt><dd><p>安装后将 Python 标准库编译为字节码。</p>
<p>默认情况下，uv 不会将 Python（<code>.py</code>）文件编译为字节码（<code>__pycache__/*.pyc</code>）；相反，编译会在首次导入模块时延迟执行。对于启动时间很重要的用例（如 CLI 应用程序和 Docker 容器），可以启用此选项，以更长的安装时间和额外的磁盘空间换取更快的启动时间。</p>
<p>启用后，uv 将处理 Python 版本的 <code>stdlib</code> 目录。它将忽略任何编译错误。</p>
<p>也可以通过 <code>UV_COMPILE_BYTECODE</code> 环境变量设置。</p></dd><dt id="uv-python-install--config-file"><a href="#uv-python-install--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许这样做。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-python-install--default"><a href="#uv-python-install--default"><code>--default</code></a></dt><dd><p>用作默认 Python 版本。</p>
<p>默认情况下，仅安装 <code>python{major}.{minor}</code> 可执行文件，例如 <code>python3.10</code>。当使用 <code>--default</code> 标志时，还会安装 <code>python{major}</code>（例如 <code>python3</code>）和 <code>python</code> 可执行文件。</p>
<p>替代的 Python 变体仍会包含其标签。例如，使用 <code>--default</code> 安装 3.13+freethreaded 将包含 <code>python3t</code> 和 <code>pythont</code>，而不是 <code>python3</code> 和 <code>python</code>。</p>
<p>如果请求了多个 Python 版本，uv 将退出并报错。</p>
</dd><dt id="uv-python-install--directory"><a href="#uv-python-install--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径以指定目录为基准进行解析。</p>
<p>请参阅 <code>--project</code> 仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-python-install--force"><a href="#uv-python-install--force"><code>--force</code></a>, <code>-f</code></dt><dd><p>在安装过程中替换现有的 Python 可执行文件。</p>
<p>默认情况下，uv 会拒绝替换非其管理的可执行文件。</p>
<p>隐含 <code>--reinstall</code>。</p>
</dd><dt id="uv-python-install--help"><a href="#uv-python-install--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助</p>
</dd><dt id="uv-python-install--install-dir"><a href="#uv-python-install--install-dir"><code>--install-dir</code></a>, <code>-i</code> <i>install-dir</i></dt><dd><p>存储 Python 安装的目录。</p>
<p>如果提供，后续操作需要设置 <code>UV_PYTHON_INSTALL_DIR</code> 以便 uv 发现 Python 安装。</p>
<p>请参阅 <code>uv python dir</code> 查看当前的 Python 安装目录。默认为 <code>~/.local/share/uv/python</code>。</p>
<p>也可以通过 <code>UV_PYTHON_INSTALL_DIR</code> 环境变量设置。</p></dd><dt id="uv-python-install--managed-python"><a href="#uv-python-install--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁止使用系统 Python 版本。</p>
</dd><dt id="uv-python-install--mirror"><a href="#uv-python-install--mirror"><code>--mirror</code></a> <i>mirror</i></dt><dd><p>设置用作下载 Python 安装源的 URL。</p>
<p>提供的 URL 将替换 <code>https://github.com/astral-sh/python-build-standalone/releases/download</code>，例如在 <code>https://github.com/astral-sh/python-build-standalone/releases/download/20240713/cpython-3.12.4%2B20240713-aarch64-apple-darwin-install_only.tar.gz</code> 中。</p>
<p>可以通过使用 <code>file://</code> URL 方案从本地目录读取发行版。</p>
</dd><dt id="uv-python-install--no-cache"><a href="#uv-python-install--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-python-install--no-config"><a href="#uv-python-install--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常情况下，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-python-install--no-managed-python"><a href="#uv-python-install--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用使用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-python-install--no-progress"><a href="#uv-python-install--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转器或进度条。</p>
</dd><dt id="uv-python-install--no-python-downloads"><a href="#uv-python-install--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-python-install--offline"><a href="#uv-python-install--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-python-install--project"><a href="#uv-python-install--project"><code>--project</code></a> <i>project</i></dt><dd><p>在指定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>请参阅 <code>--directory</code> 完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-python-install--pypy-mirror"><a href="#uv-python-install--pypy-mirror"><code>--pypy-mirror</code></a> <i>pypy-mirror</i></dt><dd><p>设置用作下载 PyPy 安装源的 URL。</p>
<p>提供的 URL 将替换 <code>https://downloads.python.org/pypy</code>，例如在 <code>https://downloads.python.org/pypy/pypy3.8-v7.3.7-osx64.tar.bz2</code> 中。</p>
<p>可以通过使用 <code>file://</code> URL 方案从本地目录读取发行版。</p>
</dd><dt id="uv-python-install--python-downloads-json-url"><a href="#uv-python-install--python-downloads-json-url"><code>--python-downloads-json-url</code></a> <i>python-downloads-json-url</i></dt><dd><p>指向自定义 Python 安装 JSON 的 URL</p>
</dd><dt id="uv-python-install--quiet"><a href="#uv-python-install--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项（例如 <code>-qq</code>）将启用静默模式，此时 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-python-install--reinstall"><a href="#uv-python-install--reinstall"><code>--reinstall</code></a>, <code>-r</code></dt><dd><p>重新安装最新的 Python 补丁版本（如果已安装）。</p>
<p>默认情况下，如果最新补丁已安装，uv 将成功退出。</p>
</dd><dt id="uv-python-install--system-certs"><a href="#uv-python-install--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能希望使用平台的原生证书存储，特别是当您依赖包含在系统证书存储中的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-python-install--verbose"><a href="#uv-python-install--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>

### uv python upgrade

升级已安装的 Python 版本。

请参阅 `uv python install` 以查看 Python 版本安装的详细信息。

<h3 class="cli-reference">用法</h3>

```
uv python upgrade [OPTIONS] [TARGETS]...
```

<h3 class="cli-reference">参数</h3>

<dl class="cli-reference"><dt id="uv-python-upgrade--targets"><a href="#uv-python-upgrade--targets"><code>TARGETS</code></a></dt><dd><p>要升级的 Python 版本。</p>
<p>如果未提供，请求的 Python 版本将从 <code>UV_PYTHON</code> 环境变量中读取，然后从 <code>.python-versions</code> 或 <code>.python-version</code> 文件中读取。如果以上都没有，uv 将升级所有已安装的版本。</p>
<p>请参阅 <a href="#uv-python">uv python</a> 了解支持的请求格式。</p>
</dd></dl>

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-python-upgrade--allow-insecure-host"><a href="#uv-python-upgrade--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会通过系统的证书存储进行验证。仅在安全的网络中使用 <code>--allow-insecure-host</code>，并确保来源可信，因为它会绕过 SSL 验证，可能使您面临中间人攻击（MITM）的风险。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-python-upgrade--cache-dir"><a href="#uv-python-upgrade--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-python-upgrade--color"><a href="#uv-python-upgrade--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>：仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-python-upgrade--compile-bytecode"><a href="#uv-python-upgrade--compile-bytecode"><code>--compile-bytecode</code></a>, <code>--compile</code></dt><dd><p>安装后将 Python 标准库编译为字节码。</p>
<p>默认情况下，uv 不会将 Python（<code>.py</code>）文件编译为字节码（<code>__pycache__/*.pyc</code>）；相反，编译会在首次导入模块时延迟执行。对于启动时间很重要的用例（如 CLI 应用程序和 Docker 容器），可以启用此选项，以更长的安装时间和额外的磁盘空间换取更快的启动时间。</p>
<p>启用后，uv 将处理 Python 版本的 <code>stdlib</code> 目录。它将忽略任何编译错误。</p>
<p>也可以通过 <code>UV_COMPILE_BYTECODE</code> 环境变量设置。</p></dd><dt id="uv-python-upgrade--config-file"><a href="#uv-python-upgrade--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许这样做。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-python-upgrade--directory"><a href="#uv-python-upgrade--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径以指定目录为基准进行解析。</p>
<p>请参阅 <code>--project</code> 仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-python-upgrade--help"><a href="#uv-python-upgrade--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助</p>
</dd><dt id="uv-python-upgrade--install-dir"><a href="#uv-python-upgrade--install-dir"><code>--install-dir</code></a>, <code>-i</code> <i>install-dir</i></dt><dd><p>Python 安装的存储目录。</p>
<p>如果提供，后续操作需要设置 <code>UV_PYTHON_INSTALL_DIR</code> 以便 uv 发现 Python 安装。</p>
<p>请参阅 <code>uv python dir</code> 查看当前的 Python 安装目录。默认为 <code>~/.local/share/uv/python</code>。</p>
<p>也可以通过 <code>UV_PYTHON_INSTALL_DIR</code> 环境变量设置。</p></dd><dt id="uv-python-upgrade--managed-python"><a href="#uv-python-upgrade--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁止使用系统 Python 版本。</p>
</dd><dt id="uv-python-upgrade--mirror"><a href="#uv-python-upgrade--mirror"><code>--mirror</code></a> <i>mirror</i></dt><dd><p>设置用作下载 Python 安装源的 URL。</p>
<p>提供的 URL 将替换 <code>https://github.com/astral-sh/python-build-standalone/releases/download</code>，例如在 <code>https://github.com/astral-sh/python-build-standalone/releases/download/20240713/cpython-3.12.4%2B20240713-aarch64-apple-darwin-install_only.tar.gz</code> 中。</p>
<p>可以通过使用 <code>file://</code> URL 方案从本地目录读取发行版。</p>
</dd><dt id="uv-python-upgrade--no-cache"><a href="#uv-python-upgrade--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-python-upgrade--no-config"><a href="#uv-python-upgrade--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常情况下，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-python-upgrade--no-managed-python"><a href="#uv-python-upgrade--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用使用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-python-upgrade--no-progress"><a href="#uv-python-upgrade--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转器或进度条。</p>
</dd><dt id="uv-python-upgrade--no-python-downloads"><a href="#uv-python-upgrade--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-python-upgrade--offline"><a href="#uv-python-upgrade--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-python-upgrade--project"><a href="#uv-python-upgrade--project"><code>--project</code></a> <i>project</i></dt><dd><p>在指定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>请参阅 <code>--directory</code> 完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-python-upgrade--pypy-mirror"><a href="#uv-python-upgrade--pypy-mirror"><code>--pypy-mirror</code></a> <i>pypy-mirror</i></dt><dd><p>设置用作下载 PyPy 安装源的 URL。</p>
<p>提供的 URL 将替换 <code>https://downloads.python.org/pypy</code>，例如在 <code>https://downloads.python.org/pypy/pypy3.8-v7.3.7-osx64.tar.bz2</code> 中。</p>
<p>可以通过使用 <code>file://</code> URL 方案从本地目录读取发行版。</p>
</dd><dt id="uv-python-upgrade--python-downloads-json-url"><a href="#uv-python-upgrade--python-downloads-json-url"><code>--python-downloads-json-url</code></a> <i>python-downloads-json-url</i></dt><dd><p>指向自定义 Python 安装 JSON 的 URL</p>
</dd><dt id="uv-python-upgrade--quiet"><a href="#uv-python-upgrade--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项（例如 <code>-qq</code>）将启用静默模式，此时 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-python-upgrade--reinstall"><a href="#uv-python-upgrade--reinstall"><code>--reinstall</code></a>, <code>-r</code></dt><dd><p>重新安装最新的 Python 补丁版本（如果已安装）。</p>
<p>默认情况下，如果最新补丁已安装，uv 将成功退出。</p>
</dd><dt id="uv-python-upgrade--system-certs"><a href="#uv-python-upgrade--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能希望使用平台的原生证书存储，特别是当您依赖包含在系统证书存储中的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-python-upgrade--verbose"><a href="#uv-python-upgrade--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>

### uv python find

搜索 Python 安装。

显示 Python 可执行文件的路径。

请参阅 `uv help python` 了解支持的请求格式和发现行为的详细信息。

<h3 class="cli-reference">用法</h3>

```
uv python find [OPTIONS] [REQUEST]
```

<h3 class="cli-reference">参数</h3>

<dl class="cli-reference"><dt id="uv-python-find--request"><a href="#uv-python-find--request"><code>REQUEST</code></a></dt><dd><p>Python 请求。</p>
<p>请参阅 <a href="#uv-python">uv python</a> 了解支持的请求格式。</p>
</dd></dl>

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-python-find--allow-insecure-host"><a href="#uv-python-find--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会通过系统的证书存储进行验证。仅在安全的网络中使用 <code>--allow-insecure-host</code>，并确保来源可信，因为它会绕过 SSL 验证，可能使您面临中间人攻击（MITM）的风险。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-python-find--cache-dir"><a href="#uv-python-find--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-python-find--color"><a href="#uv-python-find--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>：仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-python-find--config-file"><a href="#uv-python-find--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许这样做。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-python-find--directory"><a href="#uv-python-find--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径以指定目录为基准进行解析。</p>
<p>请参阅 <code>--project</code> 仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-python-find--help"><a href="#uv-python-find--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助</p>
</dd><dt id="uv-python-find--managed-python"><a href="#uv-python-find--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁止使用系统 Python 版本。</p>
</dd><dt id="uv-python-find--no-cache"><a href="#uv-python-find--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-python-find--no-config"><a href="#uv-python-find--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常情况下，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-python-find--no-managed-python"><a href="#uv-python-find--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用使用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-python-find--no-progress"><a href="#uv-python-find--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转器或进度条。</p>
</dd><dt id="uv-python-find--no-project"><a href="#uv-python-find--no-project"><code>--no-project</code></a>, <code>--no_workspace</code></dt><dd><p>避免发现项目或工作区。</p>
<p>否则，当未提供请求时，将使用当前目录或父目录中项目的 Python 需求。</p>
<p>也可以通过 <code>UV_NO_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-python-find--no-python-downloads"><a href="#uv-python-find--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-python-find--offline"><a href="#uv-python-find--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-python-find--project"><a href="#uv-python-find--project"><code>--project</code></a> <i>project</i></dt><dd><p>在指定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>请参阅 <code>--directory</code> 完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-python-find--python-downloads-json-url"><a href="#uv-python-find--python-downloads-json-url"><code>--python-downloads-json-url</code></a> <i>python-downloads-json-url</i></dt><dd><p>指向自定义 Python 安装 JSON 的 URL</p>
</dd><dt id="uv-python-find--quiet"><a href="#uv-python-find--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项（例如 <code>-qq</code>）将启用静默模式，此时 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-python-find--resolve-links"><a href="#uv-python-find--resolve-links"><code>--resolve-links</code></a></dt><dd><p>解析输出路径中的符号链接。</p>
<p>启用后，输出路径将被规范化，解析所有符号链接。</p>
</dd><dt id="uv-python-find--script"><a href="#uv-python-find--script"><code>--script</code></a> <i>script</i></dt><dd><p>查找 Python 脚本的环境，而非当前项目</p>
</dd><dt id="uv-python-find--show-version"><a href="#uv-python-find--show-version"><code>--show-version</code></a></dt><dd><p>显示将要使用的 Python 版本，而非解释器路径</p>
</dd><dt id="uv-python-find--system"><a href="#uv-python-find--system"><code>--system</code></a></dt><dd><p>仅查找系统 Python 解释器。</p>
<p>默认情况下，uv 会报告它将使用的第一个 Python 解释器，包括活动虚拟环境中的解释器，或当前工作目录或任意父目录中虚拟环境中的解释器。</p>
<p><code>--system</code> 选项指示 uv 跳过虚拟环境 Python 解释器，并将其搜索限制在系统路径中。</p>
<p>也可以通过 <code>UV_SYSTEM_PYTHON</code> 环境变量设置。</p></dd><dt id="uv-python-find--system-certs"><a href="#uv-python-find--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能希望使用平台的原生证书存储，特别是当您依赖包含在系统证书存储中的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-python-find--verbose"><a href="#uv-python-find--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>

### uv python pin

锁定到特定的 Python 版本。

将锁定的 Python 版本写入 `.python-version` 文件，其他 uv 命令使用该文件来确定所需的 Python 版本。

如果未提供版本，uv 将查找现有的 `.python-version` 文件并显示当前锁定的版本。如果未找到 `.python-version` 文件，uv 将退出并报错。

请参阅 `uv help python` 了解支持的请求格式。

<h3 class="cli-reference">用法</h3>

```
uv python pin [OPTIONS] [REQUEST]
```

<h3 class="cli-reference">参数</h3>

<dl class="cli-reference"><dt id="uv-python-pin--request"><a href="#uv-python-pin--request"><code>REQUEST</code></a></dt><dd><p>Python 版本请求。</p>
<p>uv 支持的格式比其他读取 <code>.python-version</code> 文件的工具（如 <code>pyenv</code>）更多。如果需要与这些工具兼容，请仅使用版本号，而不是复杂的请求（如 <code>cpython@3.10</code>）。</p>
<p>如果未提供请求，将显示当前锁定的版本。</p>
<p>请参阅 <a href="#uv-python">uv python</a> 了解支持的请求格式。</p>
</dd></dl>

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-python-pin--allow-insecure-host"><a href="#uv-python-pin--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会通过系统的证书存储进行验证。仅在安全的网络中使用 <code>--allow-insecure-host</code>，并确保来源可信，因为它会绕过 SSL 验证，可能使您面临中间人攻击（MITM）的风险。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-python-pin--cache-dir"><a href="#uv-python-pin--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-python-pin--color"><a href="#uv-python-pin--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>：仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-python-pin--config-file"><a href="#uv-python-pin--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许这样做。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-python-pin--directory"><a href="#uv-python-pin--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径以指定目录为基准进行解析。</p>
<p>请参阅 <code>--project</code> 仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-python-pin--help"><a href="#uv-python-pin--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助</p>
</dd><dt id="uv-python-pin--managed-python"><a href="#uv-python-pin--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁止使用系统 Python 版本。</p>
</dd><dt id="uv-python-pin--no-cache"><a href="#uv-python-pin--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-python-pin--no-config"><a href="#uv-python-pin--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常情况下，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-python-pin--no-managed-python"><a href="#uv-python-pin--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用使用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-python-pin--no-progress"><a href="#uv-python-pin--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转器或进度条。</p>
</dd><dt id="uv-python-pin--no-python-downloads"><a href="#uv-python-pin--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-python-pin--offline"><a href="#uv-python-pin--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-python-pin--project"><a href="#uv-python-pin--project"><code>--project</code></a> <i>project</i></dt><dd><p>在指定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>请参阅 <code>--directory</code> 完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-python-pin--python-downloads-json-url"><a href="#uv-python-pin--python-downloads-json-url"><code>--python-downloads-json-url</code></a> <i>python-downloads-json-url</i></dt><dd><p>指向自定义 Python 安装 JSON 的 URL</p>
</dd><dt id="uv-python-pin--quiet"><a href="#uv-python-pin--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项（例如 <code>-qq</code>）将启用静默模式，此时 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-python-pin--resolved"><a href="#uv-python-pin--resolved"><code>--resolved</code></a></dt><dd><p>写入已解析的 Python 解释器路径，而非请求。</p>
<p>确保使用完全相同的解释器。</p>
<p>当将 <code>.python-version</code> 文件提交到版本控制时，通常不建议使用此选项。</p>
</dd><dt id="uv-python-pin--rm"><a href="#uv-python-pin--rm"><code>--rm</code></a></dt><dd><p>移除 Python 版本锁定</p>
</dd><dt id="uv-python-pin--system-certs"><a href="#uv-python-pin--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能希望使用平台的原生证书存储，特别是当您依赖包含在系统证书存储中的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-python-pin--verbose"><a href="#uv-python-pin--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>

### uv python dir

显示 uv Python 安装目录。

默认情况下，Python 安装存储在 uv 数据目录中，在 Unix 上为 `$XDG_DATA_HOME/uv/python` 或 `$HOME/.local/share/uv/python`，在 Windows 上为 `%APPDATA%\uv\data\python`。

Python 安装目录可以通过 `$UV_PYTHON_INSTALL_DIR` 覆盖。

要查看 uv 安装 Python 可执行文件的目录，请使用 `--bin` 标志。Python 可执行文件目录可以通过 `$UV_PYTHON_BIN_DIR` 覆盖。请注意，Python 可执行文件仅在启用预览模式时才会安装。

<h3 class="cli-reference">用法</h3>

```
uv python dir [OPTIONS]
```

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-python-dir--allow-insecure-host"><a href="#uv-python-dir--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会通过系统的证书存储进行验证。仅在安全的网络中使用 <code>--allow-insecure-host</code>，并确保来源可信，因为它会绕过 SSL 验证，可能使您面临中间人攻击（MITM）的风险。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-python-dir--bin"><a href="#uv-python-dir--bin"><code>--bin</code></a></dt><dd><p>显示 <code>uv python</code> 将安装 Python 可执行文件的目录。</p>
<p>请注意，此目录仅在启用预览模式安装 Python 时使用。</p>
<p>Python 可执行文件目录根据 XDG 标准确定，并派生自以下环境变量，按优先级顺序排列：</p>
<ul>
<li><code>$UV_PYTHON_BIN_DIR</code></li>
<li><code>$XDG_BIN_HOME</code></li>
<li><code>$XDG_DATA_HOME/../bin</code></li>
<li><code>$HOME/.local/bin</code></li>
</ul>
</dd><dt id="uv-python-dir--cache-dir"><a href="#uv-python-dir--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-python-dir--color"><a href="#uv-python-dir--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>：仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-python-dir--config-file"><a href="#uv-python-dir--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许这样做。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-python-dir--directory"><a href="#uv-python-dir--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径以指定目录为基准进行解析。</p>
<p>请参阅 <code>--project</code> 仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-python-dir--help"><a href="#uv-python-dir--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助</p>
</dd><dt id="uv-python-dir--managed-python"><a href="#uv-python-dir--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁止使用系统 Python 版本。</p>
</dd><dt id="uv-python-dir--no-cache"><a href="#uv-python-dir--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-python-dir--no-config"><a href="#uv-python-dir--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常情况下，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-python-dir--no-managed-python"><a href="#uv-python-dir--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用使用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-python-dir--no-progress"><a href="#uv-python-dir--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转器或进度条。</p>
</dd><dt id="uv-python-dir--no-python-downloads"><a href="#uv-python-dir--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-python-dir--offline"><a href="#uv-python-dir--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-python-dir--project"><a href="#uv-python-dir--project"><code>--project</code></a> <i>project</i></dt><dd><p>在指定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>请参阅 <code>--directory</code> 完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-python-dir--quiet"><a href="#uv-python-dir--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项（例如 <code>-qq</code>）将启用静默模式，此时 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-python-dir--system-certs"><a href="#uv-python-dir--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能希望使用平台的原生证书存储，特别是当您依赖包含在系统证书存储中的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-python-dir--verbose"><a href="#uv-python-dir--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>

### uv python uninstall

卸载 Python 版本

<h3 class="cli-reference">用法</h3>

```
uv python uninstall [OPTIONS] <TARGETS>...
```

<h3 class="cli-reference">参数</h3>

<dl class="cli-reference"><dt id="uv-python-uninstall--targets"><a href="#uv-python-uninstall--targets"><code>TARGETS</code></a></dt><dd><p>要卸载的 Python 版本。</p>
<p>请参阅 <a href="#uv-python">uv python</a> 了解支持的请求格式。</p>
</dd></dl>

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-python-uninstall--all"><a href="#uv-python-uninstall--all"><code>--all</code></a></dt><dd><p>卸载所有由 uv 管理的 Python 版本</p>
</dd><dt id="uv-python-uninstall--allow-insecure-host"><a href="#uv-python-uninstall--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会通过系统的证书存储进行验证。仅在安全的网络中使用 <code>--allow-insecure-host</code>，并确保来源可信，因为它会绕过 SSL 验证，可能使您面临中间人攻击（MITM）的风险。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-python-uninstall--cache-dir"><a href="#uv-python-uninstall--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-python-uninstall--color"><a href="#uv-python-uninstall--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>：仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-python-uninstall--config-file"><a href="#uv-python-uninstall--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许这样做。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-python-uninstall--directory"><a href="#uv-python-uninstall--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径以指定目录为基准进行解析。</p>
<p>请参阅 <code>--project</code> 仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-python-uninstall--help"><a href="#uv-python-uninstall--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助</p>
</dd><dt id="uv-python-uninstall--install-dir"><a href="#uv-python-uninstall--install-dir"><code>--install-dir</code></a>, <code>-i</code> <i>install-dir</i></dt><dd><p>Python 的安装目录</p>
<p>也可以通过 <code>UV_PYTHON_INSTALL_DIR</code> 环境变量设置。</p></dd><dt id="uv-python-uninstall--managed-python"><a href="#uv-python-uninstall--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁止使用系统 Python 版本。</p>
</dd><dt id="uv-python-uninstall--no-cache"><a href="#uv-python-uninstall--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-python-uninstall--no-config"><a href="#uv-python-uninstall--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常情况下，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-python-uninstall--no-managed-python"><a href="#uv-python-uninstall--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用使用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-python-uninstall--no-progress"><a href="#uv-python-uninstall--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转器或进度条。</p>
</dd><dt id="uv-python-uninstall--no-python-downloads"><a href="#uv-python-uninstall--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-python-uninstall--offline"><a href="#uv-python-uninstall--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-python-uninstall--project"><a href="#uv-python-uninstall--project"><code>--project</code></a> <i>project</i></dt><dd><p>在指定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>请参阅 <code>--directory</code> 完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-python-uninstall--quiet"><a href="#uv-python-uninstall--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项（例如 <code>-qq</code>）将启用静默模式，此时 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-python-uninstall--system-certs"><a href="#uv-python-uninstall--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能希望使用平台的原生证书存储，特别是当您依赖包含在系统证书存储中的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-python-uninstall--verbose"><a href="#uv-python-uninstall--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>

### uv python update-shell

确保 Python 可执行文件目录位于 `PATH` 中。

如果 Python 可执行文件目录不在 `PATH` 中，uv 将尝试将其添加到相关的 shell 配置文件中。

如果 shell 配置文件已包含将可执行文件目录添加到路径的片段，但该目录不在 `PATH` 中，uv 将退出并报错。

Python 可执行文件目录根据 XDG 标准确定，可以通过 `uv python dir --bin` 获取。

<h3 class="cli-reference">用法</h3>

```
uv python update-shell [OPTIONS]
```

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-python-update-shell--allow-insecure-host"><a href="#uv-python-update-shell--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会通过系统的证书存储进行验证。仅在安全的网络中使用 <code>--allow-insecure-host</code>，并确保来源可信，因为它会绕过 SSL 验证，可能使您面临中间人攻击（MITM）的风险。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-python-update-shell--cache-dir"><a href="#uv-python-update-shell--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-python-update-shell--color"><a href="#uv-python-update-shell--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>：仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-python-update-shell--config-file"><a href="#uv-python-update-shell--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许这样做。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-python-update-shell--directory"><a href="#uv-python-update-shell--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径以指定目录为基准进行解析。</p>
<p>请参阅 <code>--project</code> 仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-python-update-shell--help"><a href="#uv-python-update-shell--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助</p>
</dd><dt id="uv-python-update-shell--no-cache"><a href="#uv-python-update-shell--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-python-update-shell--no-config"><a href="#uv-python-update-shell--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常情况下，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-python-update-shell--no-progress"><a href="#uv-python-update-shell--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转器或进度条。</p>
</dd><dt id="uv-python-update-shell--project"><a href="#uv-python-update-shell--project"><code>--project</code></a> <i>project</i></dt><dd><p>在指定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>请参阅 <code>--directory</code> 完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-python-update-shell--quiet"><a href="#uv-python-update-shell--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项（例如 <code>-qq</code>）将启用静默模式，此时 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-python-update-shell--system-certs"><a href="#uv-python-update-shell--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能希望使用平台的原生证书存储，特别是当您依赖包含在系统证书存储中的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-python-update-shell--verbose"><a href="#uv-python-update-shell--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>