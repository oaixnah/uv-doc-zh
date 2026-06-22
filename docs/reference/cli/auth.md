---
description: 本文档是 uv auth 命令的中文参考手册，介绍了 uv 包管理器中用于管理包索引服务身份认证的命令。包括 uv auth login 登录服务、uv auth logout 登出服务、uv auth token 显示认证令牌、uv auth dir 查看凭据目录路径等子命令的详细用法、参数说明和选项配置。帮助中文开发者快速掌握 uv 的身份认证功能。
---

# uv auth

管理身份认证

<h3 class="cli-reference">用法</h3>

```
uv auth [OPTIONS] <COMMAND>
```

<h3 class="cli-reference">Commands</h3>

<dl class="cli-reference"><dt><a href="#uv-auth-login"><code>uv auth login</code></a></dt><dd><p>登录到服务</p></dd>
<dt><a href="#uv-auth-logout"><code>uv auth logout</code></a></dt><dd><p>从服务登出</p></dd>
<dt><a href="#uv-auth-token"><code>uv auth token</code></a></dt><dd><p>显示服务的身份认证令牌</p></dd>
<dt><a href="#uv-auth-dir"><code>uv auth dir</code></a></dt><dd><p>显示 uv 凭据目录的路径</p></dd>
</dl>

## uv auth login

登录到服务

<h3 class="cli-reference">用法</h3>

```
uv auth login [OPTIONS] <SERVICE>
```

<h3 class="cli-reference">Arguments</h3>

<dl class="cli-reference"><dt id="uv-auth-login--service"><a href="#uv-auth-login--service"><code>SERVICE</code></a></dt><dd><p>要登录的服务的域名或 URL</p>
</dd></dl>

<h3 class="cli-reference">Options</h3>

<dl class="cli-reference"><dt id="uv-auth-login--allow-insecure-host"><a href="#uv-auth-login--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许到主机的非安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统的证书存储进行验证。仅在安全的网络中使用 <code>--allow-insecure-host</code>，并确保来源已验证，因为它会绕过 SSL 验证，可能使你暴露于中间人攻击（MITM）的风险中。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-auth-login--cache-dir"><a href="#uv-auth-login--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上默认为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-auth-login--color"><a href="#uv-auth-login--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 在写入终端时会自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>:  仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>:  无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>:  禁用彩色输出</li>
</ul></dd><dt id="uv-auth-login--config-file"><a href="#uv-auth-login--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件的路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-auth-login--directory"><a href="#uv-auth-login--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径将以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 以仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-auth-login--help"><a href="#uv-auth-login--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助</p>
</dd><dt id="uv-auth-login--keyring-provider"><a href="#uv-auth-login--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>用于存储凭据的 keyring 提供程序。</p>
<p><code>login</code> 仅支持 <code>--keyring-provider native</code>，它通过 uv 内置的集成使用系统 keyring。</p>
<p>也可以通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disabled</code>:  不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>:  使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-auth-login--managed-python"><a href="#uv-auth-login--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-auth-login--no-cache"><a href="#uv-auth-login--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-auth-login--no-config"><a href="#uv-auth-login--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-auth-login--no-managed-python"><a href="#uv-auth-login--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-auth-login--no-progress"><a href="#uv-auth-login--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转指示器或进度条。</p>
</dd><dt id="uv-auth-login--no-python-downloads"><a href="#uv-auth-login--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-auth-login--offline"><a href="#uv-auth-login--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存的数据和本地可用的文件。</p>
</dd><dt id="uv-auth-login--password"><a href="#uv-auth-login--password"><code>--password</code></a> <i>password</i></dt><dd><p>用于服务的密码。</p>
<p>使用 <code>-</code> 从标准输入读取密码。</p>
</dd><dt id="uv-auth-login--project"><a href="#uv-auth-login--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时没有效果。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-auth-login--quiet"><a href="#uv-auth-login--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，在此模式下 uv 不会向标准输出写入任何内容。</p>
</dd><dt id="uv-auth-login--system-certs"><a href="#uv-auth-login--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储中加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用内置的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，你可能希望使用平台的原生证书存储，特别是当你依赖系统证书存储中包含的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-auth-login--token"><a href="#uv-auth-login--token"><code>--token</code></a>, <code>-t</code> <i>token</i></dt><dd><p>用于服务的令牌。</p>
<p>用户名将设置为 <code>__token__</code>。</p>
<p>使用 <code>-</code> 从标准输入读取令牌。</p>
</dd><dt id="uv-auth-login--username"><a href="#uv-auth-login--username"><code>--username</code></a>, <code>-u</code> <i>username</i></dt><dd><p>用于服务的用户名</p>
</dd><dt id="uv-auth-login--verbose"><a href="#uv-auth-login--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>你可以使用 <code>RUST_LOG</code> 环境变量配置细粒度的日志记录。 (<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>)</p>
</dd></dl>

## uv auth logout

从服务登出

<h3 class="cli-reference">用法</h3>

```
uv auth logout [OPTIONS] <SERVICE>
```

<h3 class="cli-reference">Arguments</h3>

<dl class="cli-reference"><dt id="uv-auth-logout--service"><a href="#uv-auth-logout--service"><code>SERVICE</code></a></dt><dd><p>要登出的服务的域名或 URL</p>
</dd></dl>

<h3 class="cli-reference">Options</h3>

<dl class="cli-reference"><dt id="uv-auth-logout--allow-insecure-host"><a href="#uv-auth-logout--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许到主机的非安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统的证书存储进行验证。仅在安全的网络中使用 <code>--allow-insecure-host</code>，并确保来源已验证，因为它会绕过 SSL 验证，可能使你暴露于中间人攻击（MITM）的风险中。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-auth-logout--cache-dir"><a href="#uv-auth-logout--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上默认为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-auth-logout--color"><a href="#uv-auth-logout--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 在写入终端时会自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>:  仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>:  无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>:  禁用彩色输出</li>
</ul></dd><dt id="uv-auth-logout--config-file"><a href="#uv-auth-logout--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件的路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-auth-logout--directory"><a href="#uv-auth-logout--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径将以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 以仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-auth-logout--help"><a href="#uv-auth-logout--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助</p>
</dd><dt id="uv-auth-logout--keyring-provider"><a href="#uv-auth-logout--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>用于存储凭据的 keyring 提供程序。</p>
<p><code>logout</code> 仅支持 <code>--keyring-provider native</code>，它通过 uv 内置的集成使用系统 keyring。</p>
<p>也可以通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disabled</code>:  不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>:  使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-auth-logout--managed-python"><a href="#uv-auth-logout--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-auth-logout--no-cache"><a href="#uv-auth-logout--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-auth-logout--no-config"><a href="#uv-auth-logout--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-auth-logout--no-managed-python"><a href="#uv-auth-logout--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-auth-logout--no-progress"><a href="#uv-auth-logout--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转指示器或进度条。</p>
</dd><dt id="uv-auth-logout--no-python-downloads"><a href="#uv-auth-logout--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-auth-logout--offline"><a href="#uv-auth-logout--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存的数据和本地可用的文件。</p>
</dd><dt id="uv-auth-logout--project"><a href="#uv-auth-logout--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时没有效果。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-auth-logout--quiet"><a href="#uv-auth-logout--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，在此模式下 uv 不会向标准输出写入任何内容。</p>
</dd><dt id="uv-auth-logout--system-certs"><a href="#uv-auth-logout--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储中加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用内置的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，你可能希望使用平台的原生证书存储，特别是当你依赖系统证书存储中包含的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-auth-logout--username"><a href="#uv-auth-logout--username"><code>--username</code></a>, <code>-u</code> <i>username</i></dt><dd><p>要登出的用户名</p>
</dd><dt id="uv-auth-logout--verbose"><a href="#uv-auth-logout--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>你可以使用 <code>RUST_LOG</code> 环境变量配置细粒度的日志记录。 (<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>)</p>
</dd></dl>

## uv auth token

显示服务的身份认证令牌

<h3 class="cli-reference">用法</h3>

```
uv auth token [OPTIONS] <SERVICE>
```

<h3 class="cli-reference">Arguments</h3>

<dl class="cli-reference"><dt id="uv-auth-token--service"><a href="#uv-auth-token--service"><code>SERVICE</code></a></dt><dd><p>要查询的服务的域名或 URL</p>
</dd></dl>

<h3 class="cli-reference">Options</h3>

<dl class="cli-reference"><dt id="uv-auth-token--allow-insecure-host"><a href="#uv-auth-token--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许到主机的非安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统的证书存储进行验证。仅在安全的网络中使用 <code>--allow-insecure-host</code>，并确保来源已验证，因为它会绕过 SSL 验证，可能使你暴露于中间人攻击（MITM）的风险中。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-auth-token--cache-dir"><a href="#uv-auth-token--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上默认为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-auth-token--color"><a href="#uv-auth-token--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 在写入终端时会自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>:  仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>:  无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>:  禁用彩色输出</li>
</ul></dd><dt id="uv-auth-token--config-file"><a href="#uv-auth-token--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件的路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-auth-token--directory"><a href="#uv-auth-token--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径将以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 以仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-auth-token--help"><a href="#uv-auth-token--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助</p>
</dd><dt id="uv-auth-token--keyring-provider"><a href="#uv-auth-token--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>用于读取凭据的 keyring 提供程序。</p>
<p>也可以通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disabled</code>:  不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>:  使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-auth-token--managed-python"><a href="#uv-auth-token--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-auth-token--no-cache"><a href="#uv-auth-token--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-auth-token--no-config"><a href="#uv-auth-token--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-auth-token--no-managed-python"><a href="#uv-auth-token--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-auth-token--no-progress"><a href="#uv-auth-token--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转指示器或进度条。</p>
</dd><dt id="uv-auth-token--no-python-downloads"><a href="#uv-auth-token--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-auth-token--offline"><a href="#uv-auth-token--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存的数据和本地可用的文件。</p>
</dd><dt id="uv-auth-token--project"><a href="#uv-auth-token--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时没有效果。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-auth-token--quiet"><a href="#uv-auth-token--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，在此模式下 uv 不会向标准输出写入任何内容。</p>
</dd><dt id="uv-auth-token--system-certs"><a href="#uv-auth-token--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储中加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用内置的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，你可能希望使用平台的原生证书存储，特别是当你依赖系统证书存储中包含的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-auth-token--username"><a href="#uv-auth-token--username"><code>--username</code></a>, <code>-u</code> <i>username</i></dt><dd><p>要查询的用户名</p>
</dd><dt id="uv-auth-token--verbose"><a href="#uv-auth-token--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>你可以使用 <code>RUST_LOG</code> 环境变量配置细粒度的日志记录。 (<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>)</p>
</dd></dl>

## uv auth dir

显示 uv 凭据目录的路径。

默认情况下，凭据存储在 uv 数据目录中，在 Unix 上为 `$XDG_DATA_HOME/uv/credentials` 或 `$HOME/.local/share/uv/credentials`，在 Windows 上为 `%APPDATA%\uv\data\credentials`。

凭据目录可以通过 `$UV_CREDENTIALS_DIR` 环境变量覆盖。

仅当使用明文（plaintext）后端时，凭据才会存储在此目录中；而原生（native）后端则使用系统 keyring。

<h3 class="cli-reference">用法</h3>

```
uv auth dir [OPTIONS] [SERVICE]
```

<h3 class="cli-reference">Arguments</h3>

<dl class="cli-reference"><dt id="uv-auth-dir--service"><a href="#uv-auth-dir--service"><code>SERVICE</code></a></dt><dd><p>要查询的服务的域名或 URL</p>
</dd></dl>

<h3 class="cli-reference">Options</h3>

<dl class="cli-reference"><dt id="uv-auth-dir--allow-insecure-host"><a href="#uv-auth-dir--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许到主机的非安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统的证书存储进行验证。仅在安全的网络中使用 <code>--allow-insecure-host</code>，并确保来源已验证，因为它会绕过 SSL 验证，可能使你暴露于中间人攻击（MITM）的风险中。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-auth-dir--cache-dir"><a href="#uv-auth-dir--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上默认为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-auth-dir--color"><a href="#uv-auth-dir--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 在写入终端时会自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>:  仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>:  无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>:  禁用彩色输出</li>
</ul></dd><dt id="uv-auth-dir--config-file"><a href="#uv-auth-dir--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件的路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-auth-dir--directory"><a href="#uv-auth-dir--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径将以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 以仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-auth-dir--help"><a href="#uv-auth-dir--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助</p>
</dd><dt id="uv-auth-dir--managed-python"><a href="#uv-auth-dir--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-auth-dir--no-cache"><a href="#uv-auth-dir--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-auth-dir--no-config"><a href="#uv-auth-dir--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-auth-dir--no-managed-python"><a href="#uv-auth-dir--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-auth-dir--no-progress"><a href="#uv-auth-dir--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转指示器或进度条。</p>
</dd><dt id="uv-auth-dir--no-python-downloads"><a href="#uv-auth-dir--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-auth-dir--offline"><a href="#uv-auth-dir--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存的数据和本地可用的文件。</p>
</dd><dt id="uv-auth-dir--project"><a href="#uv-auth-dir--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时没有效果。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-auth-dir--quiet"><a href="#uv-auth-dir--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，在此模式下 uv 不会向标准输出写入任何内容。</p>
</dd><dt id="uv-auth-dir--system-certs"><a href="#uv-auth-dir--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储中加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用内置的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，你可能希望使用平台的原生证书存储，特别是当你依赖系统证书存储中包含的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-auth-dir--verbose"><a href="#uv-auth-dir--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>你可以使用 <code>RUST_LOG</code> 环境变量配置细粒度的日志记录。 (<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>)</p>
</dd></dl>
