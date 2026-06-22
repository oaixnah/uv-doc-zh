---
title: uv help
description: 显示命令的文档。
---

# uv help

显示命令的文档

<h3 class="cli-reference">用法</h3>

```
uv help [OPTIONS] [COMMAND]...
```

<h3 class="cli-reference">参数</h3>

<dl class="cli-reference"><dt id="uv-help--command"><a href="#uv-help--command"><code>COMMAND</code></a></dt></dl>

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-help--allow-insecure-host"><a href="#uv-help--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机的非安全连接。</p>
<p>可以多次指定。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会通过系统证书存储进行验证。仅在安全网络中使用 <code>--allow-insecure-host</code> 并确保来源已验证，因为它绕过了 SSL 验证，可能使您面临中间人攻击（MITM）的风险。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-help--cache-dir"><a href="#uv-help--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上默认为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-help--color"><a href="#uv-help--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>：仅当输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-help--config-file"><a href="#uv-help--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许这样做。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-help--directory"><a href="#uv-help--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到给定目录。</p>
<p>相对路径以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 以仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-help--help"><a href="#uv-help--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助信息</p>
</dd><dt id="uv-help--managed-python"><a href="#uv-help--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-help--no-cache"><a href="#uv-help--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免从缓存读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-help--no-config"><a href="#uv-help--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-help--no-managed-python"><a href="#uv-help--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用使用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-help--no-pager"><a href="#uv-help--no-pager"><code>--no-pager</code></a></dt><dd><p>打印帮助时禁用分页器</p>
</dd><dt id="uv-help--no-progress"><a href="#uv-help--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转动画或进度条。</p>
</dd><dt id="uv-help--no-python-downloads"><a href="#uv-help--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-help--offline"><a href="#uv-help--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-help--project"><a href="#uv-help--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>如果要完全更改工作目录，请参见 <code>--directory</code>。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-help--quiet"><a href="#uv-help--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，在该模式下 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-help--system-certs"><a href="#uv-help--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>然而，在某些情况下，您可能希望使用平台的原生证书存储，特别是当您依赖企业信任根（例如，用于强制代理）且该根证书已包含在系统证书存储中时。</p>
</dd><dt id="uv-help--verbose"><a href="#uv-help--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度的日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>