---
title: uv cache
description: uv cache 命令的完整中文参考文档，涵盖 uv cache clean（清除缓存）、uv cache prune（修剪不可达对象）、uv cache dir（显示缓存目录）和 uv cache size（显示缓存大小）四个子命令的全部选项及用法说明。
---

# uv cache

管理 uv 的缓存

<h3 class="cli-reference">用法</h3>

```
uv cache [OPTIONS] <COMMAND>
```

<h3 class="cli-reference">命令</h3>

<dl class="cli-reference"><dt><a href="#uv-cache-clean"><code>uv cache clean</code></a></dt><dd><p>清除缓存，移除所有条目或仅移除与特定包关联的条目</p></dd>
<dt><a href="#uv-cache-prune"><code>uv cache prune</code></a></dt><dd><p>修剪缓存中所有不可达的对象</p></dd>
<dt><a href="#uv-cache-dir"><code>uv cache dir</code></a></dt><dd><p>显示缓存目录</p></dd>
<dt><a href="#uv-cache-size"><code>uv cache size</code></a></dt><dd><p>显示缓存大小</p></dd>
</dl>

### uv cache clean

清除缓存，移除所有条目或仅移除与特定包关联的条目

<h3 class="cli-reference">用法</h3>

```
uv cache clean [OPTIONS] [PACKAGE]...
```

<h3 class="cli-reference">参数</h3>

<dl class="cli-reference"><dt id="uv-cache-clean--package"><a href="#uv-cache-clean--package"><code>PACKAGE</code></a></dt><dd><p>要从缓存中移除的包</p>
</dd></dl>

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-cache-clean--allow-insecure-host"><a href="#uv-cache-clean--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机的非安全连接。</p>
<p>可多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会通过系统证书存储进行验证。仅在安全的网络环境中使用 <code>--allow-insecure-host</code>，并确保来源可信，因为此选项会绕过 SSL 验证，可能使你暴露于中间人攻击（MITM）的风险中。</p>
<p>也可通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-cache-clean--cache-dir"><a href="#uv-cache-clean--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>默认在 macOS 和 Linux 上为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-cache-clean--color"><a href="#uv-cache-clean--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>：仅当输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，均启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-cache-clean--config-file"><a href="#uv-cache-clean--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许这样做。</p>
<p>也可通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-cache-clean--directory"><a href="#uv-cache-clean--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径以该目录为基准进行解析。</p>
<p>如果只想更改项目根目录，请参阅 <code>--project</code>。</p>
<p>也可通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-cache-clean--force"><a href="#uv-cache-clean--force"><code>--force</code></a></dt><dd><p>强制移除缓存，忽略使用中检查。</p>
<p>默认情况下，<code>uv cache clean</code> 会阻塞直到没有进程正在读取缓存。使用 <code>--force</code> 时，<code>uv cache clean</code> 将在不获取锁的情况下继续执行。</p>
</dd><dt id="uv-cache-clean--help"><a href="#uv-cache-clean--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助信息</p>
</dd><dt id="uv-cache-clean--managed-python"><a href="#uv-cache-clean--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-cache-clean--no-cache"><a href="#uv-cache-clean--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免从缓存读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-cache-clean--no-config"><a href="#uv-cache-clean--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-cache-clean--no-managed-python"><a href="#uv-cache-clean--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用使用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-cache-clean--no-progress"><a href="#uv-cache-clean--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转动画或进度条。</p>
</dd><dt id="uv-cache-clean--no-python-downloads"><a href="#uv-cache-clean--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-cache-clean--offline"><a href="#uv-cache-clean--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-cache-clean--project"><a href="#uv-cache-clean--project"><code>--project</code></a> <i>project</i></dt><dd><p>在指定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>如果要完全更改工作目录，请参阅 <code>--directory</code>。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-cache-clean--quiet"><a href="#uv-cache-clean--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，在此模式下 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-cache-clean--system-certs"><a href="#uv-cache-clean--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，你可能希望使用平台的原生证书存储，特别是当你依赖系统证书存储中包含的企业信任根（例如用于强制代理）时。</p>
</dd><dt id="uv-cache-clean--verbose"><a href="#uv-cache-clean--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>你可以使用 <code>RUST_LOG</code> 环境变量配置细粒度的日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>

### uv cache prune

修剪缓存中所有不可达的对象

<h3 class="cli-reference">用法</h3>

```
uv cache prune [OPTIONS]
```

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-cache-prune--allow-insecure-host"><a href="#uv-cache-prune--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机的非安全连接。</p>
<p>可多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会通过系统证书存储进行验证。仅在安全的网络环境中使用 <code>--allow-insecure-host</code>，并确保来源可信，因为此选项会绕过 SSL 验证，可能使你暴露于中间人攻击（MITM）的风险中。</p>
<p>也可通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-cache-prune--cache-dir"><a href="#uv-cache-prune--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>默认在 macOS 和 Linux 上为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-cache-prune--ci"><a href="#uv-cache-prune--ci"><code>--ci</code></a></dt><dd><p>优化缓存以在持续集成环境（如 GitHub Actions）中持久化。</p>
<p>默认情况下，uv 会同时缓存从源码构建的 wheel 和直接下载的预构建 wheel，以实现高性能的包安装。但在某些场景下，持久化预构建 wheel 可能并不理想。例如，在 GitHub Actions 中，从缓存中省略预构建 wheel 并在每次运行时重新下载它们会更快。然而，缓存从源码构建的 wheel 通常会更快，因为 wheel 构建过程可能很昂贵，尤其是对于扩展模块。</p>
<p>在 <code>--ci</code> 模式下，uv 将从缓存中修剪所有预构建的 wheel，但保留所有从源码构建的 wheel。</p>
</dd><dt id="uv-cache-prune--color"><a href="#uv-cache-prune--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>：仅当输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，均启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-cache-prune--config-file"><a href="#uv-cache-prune--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许这样做。</p>
<p>也可通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-cache-prune--directory"><a href="#uv-cache-prune--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径以该目录为基准进行解析。</p>
<p>如果只想更改项目根目录，请参阅 <code>--project</code>。</p>
<p>也可通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-cache-prune--force"><a href="#uv-cache-prune--force"><code>--force</code></a></dt><dd><p>强制移除缓存，忽略使用中检查。</p>
<p>默认情况下，<code>uv cache prune</code> 会阻塞直到没有进程正在读取缓存。使用 <code>--force</code> 时，<code>uv cache prune</code> 将在不获取锁的情况下继续执行。</p>
</dd><dt id="uv-cache-prune--help"><a href="#uv-cache-prune--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助信息</p>
</dd><dt id="uv-cache-prune--managed-python"><a href="#uv-cache-prune--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-cache-prune--no-cache"><a href="#uv-cache-prune--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免从缓存读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-cache-prune--no-config"><a href="#uv-cache-prune--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-cache-prune--no-managed-python"><a href="#uv-cache-prune--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用使用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-cache-prune--no-progress"><a href="#uv-cache-prune--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转动画或进度条。</p>
</dd><dt id="uv-cache-prune--no-python-downloads"><a href="#uv-cache-prune--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-cache-prune--offline"><a href="#uv-cache-prune--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-cache-prune--project"><a href="#uv-cache-prune--project"><code>--project</code></a> <i>project</i></dt><dd><p>在指定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>如果要完全更改工作目录，请参阅 <code>--directory</code>。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-cache-prune--quiet"><a href="#uv-cache-prune--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，在此模式下 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-cache-prune--system-certs"><a href="#uv-cache-prune--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，你可能希望使用平台的原生证书存储，特别是当你依赖系统证书存储中包含的企业信任根（例如用于强制代理）时。</p>
</dd><dt id="uv-cache-prune--verbose"><a href="#uv-cache-prune--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>你可以使用 <code>RUST_LOG</code> 环境变量配置细粒度的日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>

### uv cache dir

显示缓存目录。

默认情况下，缓存在 Unix 上存储在 `$XDG_CACHE_HOME/uv` 或 `$HOME/.cache/uv` 中，在 Windows 上存储在 `%LOCALAPPDATA%\uv\cache` 中。

当使用 `--no-cache` 时，缓存存储在临时目录中，并在进程退出时丢弃。

可以通过 `cache-dir` 设置、`--cache-dir` 选项或 `$UV_CACHE_DIR` 环境变量指定替代的缓存目录。

请注意，为了获得最佳性能，缓存目录应与 uv 正在操作的 Python 环境位于同一文件系统上。

<h3 class="cli-reference">用法</h3>

```
uv cache dir [OPTIONS]
```

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-cache-dir--allow-insecure-host"><a href="#uv-cache-dir--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机的非安全连接。</p>
<p>可多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会通过系统证书存储进行验证。仅在安全的网络环境中使用 <code>--allow-insecure-host</code>，并确保来源可信，因为此选项会绕过 SSL 验证，可能使你暴露于中间人攻击（MITM）的风险中。</p>
<p>也可通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-cache-dir--cache-dir"><a href="#uv-cache-dir--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>默认在 macOS 和 Linux 上为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-cache-dir--color"><a href="#uv-cache-dir--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>：仅当输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，均启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-cache-dir--config-file"><a href="#uv-cache-dir--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许这样做。</p>
<p>也可通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-cache-dir--directory"><a href="#uv-cache-dir--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径以该目录为基准进行解析。</p>
<p>如果只想更改项目根目录，请参阅 <code>--project</code>。</p>
<p>也可通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-cache-dir--help"><a href="#uv-cache-dir--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助信息</p>
</dd><dt id="uv-cache-dir--managed-python"><a href="#uv-cache-dir--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-cache-dir--no-cache"><a href="#uv-cache-dir--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免从缓存读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-cache-dir--no-config"><a href="#uv-cache-dir--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-cache-dir--no-managed-python"><a href="#uv-cache-dir--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用使用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-cache-dir--no-progress"><a href="#uv-cache-dir--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转动画或进度条。</p>
</dd><dt id="uv-cache-dir--no-python-downloads"><a href="#uv-cache-dir--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-cache-dir--offline"><a href="#uv-cache-dir--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-cache-dir--project"><a href="#uv-cache-dir--project"><code>--project</code></a> <i>project</i></dt><dd><p>在指定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>如果要完全更改工作目录，请参阅 <code>--directory</code>。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-cache-dir--quiet"><a href="#uv-cache-dir--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，在此模式下 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-cache-dir--system-certs"><a href="#uv-cache-dir--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，你可能希望使用平台的原生证书存储，特别是当你依赖系统证书存储中包含的企业信任根（例如用于强制代理）时。</p>
</dd><dt id="uv-cache-dir--verbose"><a href="#uv-cache-dir--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>你可以使用 <code>RUST_LOG</code> 环境变量配置细粒度的日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>

### uv cache size

显示缓存大小。

显示缓存目录的总大小。这包括所有已下载和已构建的 wheel、源码分发包（source distributions）以及其他缓存数据。默认情况下，以原始字节数输出大小；使用 `--human` 可获得人类可读的输出。

<h3 class="cli-reference">用法</h3>

```
uv cache size [OPTIONS]
```

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-cache-size--allow-insecure-host"><a href="#uv-cache-size--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机的非安全连接。</p>
<p>可多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会通过系统证书存储进行验证。仅在安全的网络环境中使用 <code>--allow-insecure-host</code>，并确保来源可信，因为此选项会绕过 SSL 验证，可能使你暴露于中间人攻击（MITM）的风险中。</p>
<p>也可通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-cache-size--cache-dir"><a href="#uv-cache-size--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>默认在 macOS 和 Linux 上为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-cache-size--color"><a href="#uv-cache-size--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>：仅当输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，均启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-cache-size--config-file"><a href="#uv-cache-size--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许这样做。</p>
<p>也可通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-cache-size--directory"><a href="#uv-cache-size--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径以该目录为基准进行解析。</p>
<p>如果只想更改项目根目录，请参阅 <code>--project</code>。</p>
<p>也可通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-cache-size--help"><a href="#uv-cache-size--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助信息</p>
</dd><dt id="uv-cache-size--human"><a href="#uv-cache-size--human"><code>--human</code></a>, <code>--human-readable</code>, <code>-H</code></dt><dd><p>以人类可读的格式显示缓存大小（例如 <code>1.2 GiB</code> 而非原始字节数）</p>
</dd><dt id="uv-cache-size--managed-python"><a href="#uv-cache-size--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-cache-size--no-cache"><a href="#uv-cache-size--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免从缓存读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-cache-size--no-config"><a href="#uv-cache-size--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-cache-size--no-managed-python"><a href="#uv-cache-size--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用使用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-cache-size--no-progress"><a href="#uv-cache-size--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转动画或进度条。</p>
</dd><dt id="uv-cache-size--no-python-downloads"><a href="#uv-cache-size--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-cache-size--offline"><a href="#uv-cache-size--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-cache-size--project"><a href="#uv-cache-size--project"><code>--project</code></a> <i>project</i></dt><dd><p>在指定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>如果要完全更改工作目录，请参阅 <code>--directory</code>。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-cache-size--quiet"><a href="#uv-cache-size--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，在此模式下 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-cache-size--system-certs"><a href="#uv-cache-size--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，你可能希望使用平台的原生证书存储，特别是当你依赖系统证书存储中包含的企业信任根（例如用于强制代理）时。</p>
</dd><dt id="uv-cache-size--verbose"><a href="#uv-cache-size--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>你可以使用 <code>RUST_LOG</code> 环境变量配置细粒度的日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>