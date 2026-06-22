---
title: uv format
description: uv format 命令使用 Ruff 格式化器格式化项目中的 Python 代码，支持 --check 检查模式、--diff 差异查看以及丰富的配置选项（如缓存目录、Python 版本管理、网络离线模式等）。
---

# uv format

格式化项目中的 Python 代码。

使用 Ruff 格式化器格式化 Python 代码。默认情况下，项目中的所有 Python 文件都会被格式化。此命令的行为与在项目根目录中运行 `ruff format` 相同。

要检查文件是否已格式化而不修改它们，请使用 `--check`。要查看格式化更改的差异，请使用 `--diff`。

可以在 `--` 之后向 Ruff 传递额外的参数。

<h3 class="cli-reference">用法</h3>

```
uv format [OPTIONS] [-- <EXTRA_ARGS>...]
```

<h3 class="cli-reference">参数</h3>

<dl class="cli-reference"><dt id="uv-format--extra_args"><a href="#uv-format--extra_args"><code>EXTRA_ARGS</code></a></dt><dd><p>传递给 Ruff 的额外参数。</p>
<p>例如，使用 <code>uv format -- --line-length 100</code> 设置行长度，或使用 <code>uv format -- src/module/foo.py</code> 格式化特定文件。</p>
</dd></dl>

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-format--allow-insecure-host"><a href="#uv-format--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可以多次提供。</p>
<p>预期接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统的证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您遭受中间人攻击（MITM）。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-format--cache-dir"><a href="#uv-format--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-format--check"><a href="#uv-format--check"><code>--check</code></a></dt><dd><p>检查文件是否已格式化，而不应用更改</p>
</dd><dt id="uv-format--color"><a href="#uv-format--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 在写入终端时会自动检测是否支持颜色。</p>
<p>可能的值：</p>
<ul>
<li><code>auto</code>：仅当输出发送到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-format--config-file"><a href="#uv-format--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件的路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-format--diff"><a href="#uv-format--diff"><code>--diff</code></a></dt><dd><p>显示格式化更改的差异，而不应用它们。</p>
<p>隐含 <code>--check</code>。</p>
</dd><dt id="uv-format--directory"><a href="#uv-format--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到给定目录。</p>
<p>相对路径以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-format--exclude-newer"><a href="#uv-format--exclude-newer"><code>--exclude-newer</code></a> <i>exclude-newer</i></dt><dd><p>将候选 Ruff 版本限制为在给定日期之前发布的版本。</p>
<p>接受 <a href="https://www.rfc-editor.org/rfc/rfc3339.html">RFC 3339</a> 的超集（例如 <code>2006-12-02T02:07:43Z</code>）或相同格式的本地日期（例如 <code>2006-12-02</code>），以及相对于"现在"的持续时间（例如 <code>-1 week</code>）。</p>
<p>也可以通过 <code>UV_EXCLUDE_NEWER</code> 环境变量设置。</p></dd><dt id="uv-format--help"><a href="#uv-format--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简洁帮助信息</p>
</dd><dt id="uv-format--managed-python"><a href="#uv-format--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用它管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-format--no-cache"><a href="#uv-format--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-format--no-config"><a href="#uv-format--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-format--no-managed-python"><a href="#uv-format--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-format--no-progress"><a href="#uv-format--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转动画或进度条。</p>
</dd><dt id="uv-format--no-project"><a href="#uv-format--no-project"><code>--no-project</code></a></dt><dd><p>避免发现项目或工作区。</p>
<p>不在当前项目的上下文中运行格式化器，而是在当前目录的上下文中运行。当当前目录不是项目时，这很有用。</p>
<p>也可以通过 <code>UV_NO_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-format--no-python-downloads"><a href="#uv-format--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用自动下载 Python。</p>
</dd><dt id="uv-format--offline"><a href="#uv-format--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存的数据和本地可用的文件。</p>
</dd><dt id="uv-format--project"><a href="#uv-format--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（例如相对路径）将相对于当前工作目录进行解析。</p>
<p>参见 <code>--directory</code> 完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-format--quiet"><a href="#uv-format--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，在此模式下 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-format--system-certs"><a href="#uv-format--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的本地证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用内置的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能希望使用平台的本地证书存储，特别是当您依赖系统证书存储中包含的企业信任根（例如用于强制代理）时。</p>
</dd><dt id="uv-format--verbose"><a href="#uv-format--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度的日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd><dt id="uv-format--version"><a href="#uv-format--version"><code>--version</code></a> <i>version</i></dt><dd><p>用于格式化的 Ruff 版本。</p>
<p>接受版本号（例如 <code>0.8.2</code>，将被视为精确锁定）、版本说明符（例如 <code>&gt;=0.8.0</code>）或 <code>latest</code> 以使用最新可用版本。</p>
<p>默认情况下，将使用受约束的 Ruff 版本范围（例如 <code>&gt;=0.15,&lt;0.16</code>）。</p>
</dd></dl>
