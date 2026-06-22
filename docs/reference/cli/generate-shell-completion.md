---
subtitle: 生成 shell 补全脚本
description: uv generate-shell-completion 命令用于生成指定 shell 的自动补全脚本，支持 bash、zsh、fish 等常见 shell，帮助用户在命令行中高效使用 uv 工具。
---

# uv generate-shell-completion

生成 shell 补全脚本。

<h3 class="cli-reference">用法</h3>

```
uv generate-shell-completion [OPTIONS] <SHELL>
```

<h3 class="cli-reference">参数</h3>

<dl class="cli-reference"><dt id="uv-generate-shell-completion--shell"><a href="#uv-generate-shell-completion--shell"><code>SHELL</code></a></dt><dd><p>要为其生成补全脚本的 shell。</p>
</dd></dl>

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-generate-shell-completion--allow-insecure-host"><a href="#uv-generate-shell-completion--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会通过系统证书存储进行验证。仅在具有可验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您遭受中间人攻击（MITM attacks）。</p>
<p>也可通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-generate-shell-completion--directory"><a href="#uv-generate-shell-completion--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径以指定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 以仅更改项目根目录。</p>
<p>也可通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-generate-shell-completion--managed-python"><a href="#uv-generate-shell-completion--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本。[env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用它管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-generate-shell-completion--no-managed-python"><a href="#uv-generate-shell-completion--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用 uv 管理的 Python 版本。[env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-generate-shell-completion--project"><a href="#uv-generate-shell-completion--project"><code>--project</code></a> <i>project</i></dt><dd><p>在指定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也将一并发现。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-generate-shell-completion--system-certs"><a href="#uv-generate-shell-completion--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储中加载 TLS 证书。[env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能希望使用平台的原生证书存储，特别是当您依赖系统证书存储中包含的企业信任根（例如用于强制代理）时。</p>
</dd></dl>