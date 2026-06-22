---
title: uv self
description: uv self 命令的完整中文参考文档，涵盖 uv self update（更新 uv 可执行文件到指定版本或最新版本）和 uv self version（显示 uv 当前版本）两个子命令的全部选项及用法说明，包括缓存目录、网络代理、TLS 证书、GitHub 令牌等配置参数。
---

# uv self

管理 uv 可执行文件

<h3 class="cli-reference">用法</h3>

```
uv self [OPTIONS] <COMMAND>
```

<h3 class="cli-reference">命令</h3>

<dl class="cli-reference"><dt><a href="#uv-self-update"><code>uv self update</code></a></dt><dd><p>更新 uv</p></dd>
<dt><a href="#uv-self-version"><code>uv self version</code></a></dt><dd><p>显示 uv 的版本</p></dd>
</dl>

### uv self update

更新 uv

<h3 class="cli-reference">用法</h3>

```
uv self update [OPTIONS] [TARGET_VERSION]
```

<h3 class="cli-reference">参数</h3>

<dl class="cli-reference"><dt id="uv-self-update--target_version"><a href="#uv-self-update--target_version"><code>TARGET_VERSION</code></a></dt><dd><p>更新到指定版本。如果未提供，uv 将更新到最新版本</p>
</dd></dl>

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-self-update--allow-insecure-host"><a href="#uv-self-update--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您遭受中间人攻击（MITM）。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-self-update--cache-dir"><a href="#uv-self-update--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>默认在 macOS 和 Linux 上为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-self-update--color"><a href="#uv-self-update--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 在写入终端时会自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>：仅当输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，均启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-self-update--config-file"><a href="#uv-self-update--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许这样做。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-self-update--directory"><a href="#uv-self-update--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径以该目录为基准进行解析。</p>
<p>如果只想更改项目根目录，请参阅 <code>--project</code>。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-self-update--dry-run"><a href="#uv-self-update--dry-run"><code>--dry-run</code></a></dt><dd><p>不执行更新操作</p>
</dd><dt id="uv-self-update--help"><a href="#uv-self-update--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助信息</p>
</dd><dt id="uv-self-update--managed-python"><a href="#uv-self-update--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-self-update--no-cache"><a href="#uv-self-update--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免从缓存读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-self-update--no-config"><a href="#uv-self-update--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-self-update--no-managed-python"><a href="#uv-self-update--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-self-update--no-progress"><a href="#uv-self-update--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转动画或进度条。</p>
</dd><dt id="uv-self-update--no-python-downloads"><a href="#uv-self-update--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-self-update--offline"><a href="#uv-self-update--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-self-update--project"><a href="#uv-self-update--project"><code>--project</code></a> <i>project</i></dt><dd><p>在指定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>如果要完全更改工作目录，请参阅 <code>--directory</code>。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-self-update--quiet"><a href="#uv-self-update--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，在此模式下 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-self-update--system-certs"><a href="#uv-self-update--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能希望使用平台的原生证书存储，特别是当您依赖系统证书存储中包含的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-self-update--token"><a href="#uv-self-update--token"><code>--token</code></a> <i>token</i></dt><dd><p>用于身份验证的 GitHub 令牌。令牌不是必需的，但可以用来降低遇到速率限制的几率</p>
<p>也可以通过 <code>UV_GITHUB_TOKEN</code> 环境变量设置。</p></dd><dt id="uv-self-update--verbose"><a href="#uv-self-update--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度的日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>

### uv self version

显示 uv 的版本

<h3 class="cli-reference">用法</h3>

```
uv self version [OPTIONS]
```

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-self-version--allow-insecure-host"><a href="#uv-self-version--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您遭受中间人攻击（MITM）。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-self-version--cache-dir"><a href="#uv-self-version--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>默认在 macOS 和 Linux 上为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-self-version--color"><a href="#uv-self-version--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 在写入终端时会自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>：仅当输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，均启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-self-version--config-file"><a href="#uv-self-version--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许这样做。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-self-version--directory"><a href="#uv-self-version--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径以该目录为基准进行解析。</p>
<p>如果只想更改项目根目录，请参阅 <code>--project</code>。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-self-version--help"><a href="#uv-self-version--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助信息</p>
</dd><dt id="uv-self-version--managed-python"><a href="#uv-self-version--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-self-version--no-cache"><a href="#uv-self-version--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免从缓存读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-self-version--no-config"><a href="#uv-self-version--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-self-version--no-managed-python"><a href="#uv-self-version--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-self-version--no-progress"><a href="#uv-self-version--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转动画或进度条。</p>
</dd><dt id="uv-self-version--no-python-downloads"><a href="#uv-self-version--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-self-version--offline"><a href="#uv-self-version--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-self-version--output-format"><a href="#uv-self-version--output-format"><code>--output-format</code></a> <i>output-format</i></dt><dt id="uv-self-version--project"><a href="#uv-self-version--project"><code>--project</code></a> <i>project</i></dt><dd><p>在指定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>如果要完全更改工作目录，请参阅 <code>--directory</code>。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-self-version--quiet"><a href="#uv-self-version--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，在此模式下 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-self-version--short"><a href="#uv-self-version--short"><code>--short</code></a></dt><dd><p>仅输出版本</p>
</dd><dt id="uv-self-version--system-certs"><a href="#uv-self-version--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能希望使用平台的原生证书存储，特别是当您依赖系统证书存储中包含的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-self-version--verbose"><a href="#uv-self-version--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度的日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>