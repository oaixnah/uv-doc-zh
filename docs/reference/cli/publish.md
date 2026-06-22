---
title: uv publish
description: uv publish 命令用于将 Python 分发包（wheel 和源码分发包）上传到 PyPI 或其他索引。支持通过 --publish-url 指定上传端点、--check-url 跳过重复上传、--token 和 --username/--password 进行身份验证，以及 --trusted-publishing 配置 GitHub Actions / GitLab CI/CD 的可信发布。
---

# uv publish

将分发包上传到索引

<h3 class="cli-reference">用法</h3>

```
uv publish [OPTIONS] [FILES]...
```

<h3 class="cli-reference">参数</h3>

<dl class="cli-reference"><dt id="uv-publish--files"><a href="#uv-publish--files"><code>FILES</code></a></dt><dd><p>要上传的文件路径。支持 glob 表达式。</p>
<p>默认为 <code>dist</code> 目录。仅选择 wheel 包、源码分发包及其 attestation 文件，忽略其他文件。</p>
</dd></dl>

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-publish--allow-insecure-host"><a href="#uv-publish--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可以多次指定。</p>
<p>期望接收主机名（如 <code>localhost</code>）、主机-端口对（如 <code>localhost:8080</code>）或 URL（如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统证书存储进行验证。仅在安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您面临中间人攻击（MITM）的风险。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-publish--cache-dir"><a href="#uv-publish--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上默认为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-publish--check-url"><a href="#uv-publish--check-url"><code>--check-url</code></a> <i>check-url</i></dt><dd><p>检查索引 URL 中已存在的文件，以跳过重复上传。</p>
<p>此选项允许在部分文件上传失败后重试发布，并处理由于并行上传相同文件导致的错误。</p>
<p>上传前会检查索引。如果索引中已存在完全相同的文件，则不会上传该文件。如果上传过程中发生错误，会再次检查索引，以处理相同文件被并行上传两次的情况。</p>
<p>具体行为因索引而异。上传到 PyPI 时，即使不使用 <code>--check-url</code>，上传相同文件也会成功，而大多数其他索引会报错。上传到 pyx 时，索引 URL 可以从发布 URL 自动推断。</p>
<p>索引必须提供支持的哈希算法之一（SHA-256、SHA-384 或 SHA-512）。</p>
<p>也可以通过 <code>UV_PUBLISH_CHECK_URL</code> 环境变量设置。</p></dd><dt id="uv-publish--color"><a href="#uv-publish--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>：仅当输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-publish--config-file"><a href="#uv-publish--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许这样做。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-publish--directory"><a href="#uv-publish--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径将以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-publish--dry-run"><a href="#uv-publish--dry-run"><code>--dry-run</code></a></dt><dd><p>执行试运行而不上传文件。</p>
<p>启用后，如果提供了 <code>--check-url</code>，命令将检查已存在的文件，并在支持的情况下对索引执行验证，但不会上传任何文件。</p>
</dd><dt id="uv-publish--help"><a href="#uv-publish--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简要帮助</p>
</dd><dt id="uv-publish--index"><a href="#uv-publish--index"><code>--index</code></a> <i>index</i></dt><dd><p>配置中用于发布的索引名称。</p>
<p>索引必须具有 <code>publish-url</code> 设置，例如：</p>
<pre><code class="language-toml">[[tool.uv.index]]
name = &quot;pypi&quot;
url = &quot;https://pypi.org/simple&quot;
publish-url = &quot;https://upload.pypi.org/legacy/&quot;
</code></pre>
<p>索引 <code>url</code> 将用于检查已存在的文件以跳过重复上传。</p>
<p>使用这些设置，以下两种调用是等效的：</p>
<pre><code class="language-shell">uv publish --index pypi
uv publish --publish-url https://upload.pypi.org/legacy/ --check-url https://pypi.org/simple
</code></pre>
<p>也可以通过 <code>UV_PUBLISH_INDEX</code> 环境变量设置。</p></dd><dt id="uv-publish--keyring-provider"><a href="#uv-publish--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>尝试使用 <code>keyring</code> 进行远程需求文件的身份验证。</p>
<p>目前仅支持 <code>--keyring-provider subprocess</code>，它将 uv 配置为使用 <code>keyring</code> CLI 处理身份验证。</p>
<p>默认为 <code>disabled</code>。</p>
<p>也可以通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disabled</code>：不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>：使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-publish--managed-python"><a href="#uv-publish--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但如果未安装 uv 管理的 Python，则会使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-publish--no-attestations"><a href="#uv-publish--no-attestations"><code>--no-attestations</code></a></dt><dd><p>不上传已发布文件的 attestation 文件。</p>
<p>默认情况下，uv 会尝试为每个发布的分发包上传匹配的 PEP 740 attestation 文件。</p>
<p>也可以通过 <code>UV_PUBLISH_NO_ATTESTATIONS</code> 环境变量设置。</p></dd><dt id="uv-publish--no-cache"><a href="#uv-publish--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-publish--no-config"><a href="#uv-publish--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-publish--no-managed-python"><a href="#uv-publish--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-publish--no-progress"><a href="#uv-publish--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转图标或进度条。</p>
</dd><dt id="uv-publish--no-python-downloads"><a href="#uv-publish--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-publish--offline"><a href="#uv-publish--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存的数据和本地可用的文件。</p>
</dd><dt id="uv-publish--password"><a href="#uv-publish--password"><code>--password</code></a>, <code>-p</code> <i>password</i></dt><dd><p>上传密码</p>
<p>也可以通过 <code>UV_PUBLISH_PASSWORD</code> 环境变量设置。</p></dd><dt id="uv-publish--project"><a href="#uv-publish--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>参见 <code>--directory</code> 完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-publish--publish-url"><a href="#uv-publish--publish-url"><code>--publish-url</code></a> <i>publish-url</i></dt><dd><p>上传端点的 URL（不是索引 URL）。</p>
<p>请注意，索引访问（如 <code>https:://.../simple</code>）和索引上传通常使用不同的 URL。</p>
<p>默认为 PyPI 的发布 URL（<a href="https://upload.pypi.org/legacy/">https://upload.pypi.org/legacy/</a>）。</p>
<p>也可以通过 <code>UV_PUBLISH_URL</code> 环境变量设置。</p></dd><dt id="uv-publish--quiet"><a href="#uv-publish--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，如 <code>-qq</code>，将启用静默模式，uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-publish--system-certs"><a href="#uv-publish--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能希望使用平台的原生证书存储，特别是当您依赖系统证书存储中包含的企业信任根（例如用于强制代理）时。</p>
</dd><dt id="uv-publish--token"><a href="#uv-publish--token"><code>--token</code></a>, <code>-t</code> <i>token</i></dt><dd><p>上传令牌。</p>
<p>使用令牌等效于将 <code>__token__</code> 作为 <code>--username</code> 并将令牌作为 <code>--password</code> 密码传递。</p>
<p>也可以通过 <code>UV_PUBLISH_TOKEN</code> 环境变量设置。</p></dd><dt id="uv-publish--trusted-publishing"><a href="#uv-publish--trusted-publishing"><code>--trusted-publishing</code></a> <i>trusted-publishing</i></dt><dd><p>配置可信发布（trusted publishing）。</p>
<p>默认情况下，uv 在受支持的环境中运行时会检查可信发布，但如果未配置则忽略它。</p>
<p>uv 支持的可信发布环境包括 GitHub Actions 和 GitLab CI/CD。</p>
<p>可选值：</p>
<ul>
<li><code>automatic</code>：在受支持的环境中尝试可信发布，如果失败则继续</li>
<li><code>always</code></li>
<li><code>never</code></li>
</ul></dd><dt id="uv-publish--username"><a href="#uv-publish--username"><code>--username</code></a>, <code>-u</code> <i>username</i></dt><dd><p>上传用户名</p>
<p>也可以通过 <code>UV_PUBLISH_USERNAME</code> 环境变量设置。</p></dd><dt id="uv-publish--verbose"><a href="#uv-publish--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>