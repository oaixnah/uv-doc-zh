---
title: uv build
description: uv build 命令用于将 Python 包构建为源码分发包（sdist）和轮子包（wheel）。本页面详细介绍了 uv build 的所有参数和选项，包括工作空间构建、包索引配置、构建隔离、缓存管理、链接模式等功能，是 uv 构建命令的完整 CLI 参考文档。
---

# uv build

将 Python 包构建为源码分发包（source distribution）和轮子包（wheel）。

`uv build` 接受一个目录或源码分发包的路径，默认为当前工作目录。

默认情况下，如果传入目录，`uv build` 将从源码目录构建源码分发包（"sdist"），并从源码分发包构建二进制分发包（"wheel"）。

`uv build --sdist` 可用于仅构建源码分发包，`uv build --wheel` 可用于仅构建二进制分发包，`uv build --sdist --wheel` 可用于从源码同时构建两种分发包。

如果传入源码分发包，`uv build --wheel` 将从该源码分发包构建 wheel。

<h3 class="cli-reference">用法（Usage）</h3>

```
uv build [OPTIONS] [SRC]
```

<h3 class="cli-reference">参数（Arguments）</h3>

<dl class="cli-reference"><dt id="uv-build--src"><a href="#uv-build--src"><code>SRC</code></a></dt><dd><p>用于构建分发包的目录，或者要构建为 wheel 的源码分发包归档文件。</p>
<p>默认为当前工作目录。</p>
</dd></dl>

<h3 class="cli-reference">选项（Options）</h3>

<dl class="cli-reference"><dt id="uv-build--all-packages"><a href="#uv-build--all-packages"><code>--all-packages</code></a>, <code>--all</code></dt><dd><p>构建工作空间（workspace）中的所有包。</p>
<p>工作空间将从提供的源码目录中发现，如果未提供源码目录，则从当前目录中发现。</p>
<p>如果工作空间成员不存在，uv 将退出并报错。</p>
</dd><dt id="uv-build--allow-insecure-host"><a href="#uv-build--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机的非安全连接。</p>
<p>可多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统的证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您遭受中间人（MITM）攻击。</p>
<p>也可通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-build--build-constraints"><a href="#uv-build--build-constraints"><code>--build-constraints</code></a>, <code>--build-constraint</code>, <code>-b</code> <i>build-constraints</i></dt><dd><p>构建分发包时，使用给定的依赖要求文件（requirements files）来约束构建依赖。</p>
<p>约束文件（constraints files）是类似 <code>requirements.txt</code> 的文件，仅控制所安装的构建依赖的<em>版本</em>。但是，在约束文件中包含某个包并不会自动触发该包的安装。</p>
<p>也可通过 <code>UV_BUILD_CONSTRAINT</code> 环境变量设置。</p></dd><dt id="uv-build--cache-dir"><a href="#uv-build--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上默认为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-build--clear"><a href="#uv-build--clear"><code>--clear</code></a></dt><dd><p>构建前清空输出目录，移除过时的构建产物</p>
</dd><dt id="uv-build--color"><a href="#uv-build--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>：仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-build--config-file"><a href="#uv-build--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在当前上下文中不允许这样做。</p>
<p>也可通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-build--config-setting"><a href="#uv-build--config-setting"><code>--config-setting</code></a>, <code>--config-settings</code>, <code>-C</code> <i>config-setting</i></dt><dd><p>传递给 PEP 517 构建后端的设置，以 <code>KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-build--config-settings-package"><a href="#uv-build--config-settings-package"><code>--config-settings-package</code></a>, <code>--config-settings-package</code> <i>config-settings-package</i></dt><dd><p>为特定包传递给 PEP 517 构建后端的设置，以 <code>PACKAGE:KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-build--default-index"><a href="#uv-build--default-index"><code>--default-index</code></a> <i>default-index</i></dt><dd><p>默认包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志指定的索引的优先级低于通过 <code>--index</code> 标志指定的所有其他索引。</p>
<p>也可通过 <code>UV_DEFAULT_INDEX</code> 环境变量设置。</p></dd><dt id="uv-build--directory"><a href="#uv-build--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 以仅更改项目根目录。</p>
<p>也可通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-build--exclude-newer"><a href="#uv-build--exclude-newer"><code>--exclude-newer</code></a> <i>exclude-newer</i></dt><dd><p>将候选包限制为在给定日期之前上传的包。</p>
<p>日期比较的是每个单独分发包工件的上传时间（即每个文件上传到包索引的时间），而不是包版本的发布日期。</p>
<p>接受 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、基于系统配置时区解析的相同格式的本地日期（例如 <code>2006-12-02</code>）、"友好"时长（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 时长（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>时长不遵循本地时区的语义，始终解析为固定秒数，假设一天为 24 小时（例如忽略夏令时转换）。不允许使用月和年等日历单位。</p>
<p>也可通过 <code>UV_EXCLUDE_NEWER</code> 环境变量设置。</p></dd><dt id="uv-build--exclude-newer-package"><a href="#uv-build--exclude-newer-package"><code>--exclude-newer-package</code></a> <i>exclude-newer-package</i></dt><dd><p>将特定包的候选包限制为在给定日期之前上传的包。</p>
<p>接受 <code>PACKAGE=DATE</code> 格式的包-日期对，其中 <code>DATE</code> 为 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、基于系统配置时区解析的相同格式的本地日期（例如 <code>2006-12-02</code>）、"友好"时长（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 时长（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>时长不遵循本地时区的语义，始终解析为固定秒数，假设一天为 24 小时（例如忽略夏令时转换）。不允许使用月和年等日历单位。</p>
<p>可为不同包多次提供。</p>
</dd><dt id="uv-build--extra-index-url"><a href="#uv-build--extra-index-url"><code>--extra-index-url</code></a> <i>extra-index-url</i></dt><dd><p>（已弃用：请改用 <code>--index</code>）除 <code>--index-url</code> 之外要使用的额外包索引 URL。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--index-url</code>（默认为 PyPI）指定的索引。当提供多个 <code>--extra-index-url</code> 标志时，较早的值优先级更高。</p>
<p>也可通过 <code>UV_EXTRA_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-build--find-links"><a href="#uv-build--find-links"><code>--find-links</code></a>, <code>-f</code> <i>find-links</i></dt><dd><p>除注册表索引中找到的分发包之外，用于搜索候选分发包的位置。</p>
<p>如果是路径，目标必须是一个目录，其中在顶层包含 wheel 文件（<code>.whl</code>）或源码分发包（例如 <code>.tar.gz</code> 或 <code>.zip</code>）形式的包。</p>
<p>如果是 URL，页面必须包含一个扁平列表，其中包含指向符合上述格式的包文件的链接。</p>
<p>也可通过 <code>UV_FIND_LINKS</code> 环境变量设置。</p></dd><dt id="uv-build--force-pep517"><a href="#uv-build--force-pep517"><code>--force-pep517</code></a></dt><dd><p>始终通过 PEP 517 构建，不使用 uv 构建后端的快速路径。</p>
<p>默认情况下，uv 不会为使用 uv 构建后端的包创建 PEP 517 构建环境，而是使用直接调用构建后端的快速路径。此选项强制始终使用 PEP 517。</p>
</dd><dt id="uv-build--fork-strategy"><a href="#uv-build--fork-strategy"><code>--fork-strategy</code></a> <i>fork-strategy</i></dt><dd><p>跨 Python 版本和平台选择给定包的多个版本时使用的策略。</p>
<p>默认情况下，uv 会优化为每个受支持的 Python 版本（<code>requires-python</code>）选择每个包的最新版本，同时最小化跨平台选择的版本数量。</p>
<p>在 <code>fewest</code> 策略下，uv 将最小化每个包选择的版本数量，优先选择与更广泛的受支持 Python 版本或平台兼容的旧版本。</p>
<p>也可通过 <code>UV_FORK_STRATEGY</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>fewest</code>：优化为每个包选择最少数量的版本。如果旧版本与更广泛的受支持 Python 版本或平台兼容，可能会优先选择旧版本</li>
<li><code>requires-python</code>：优化为每个受支持的 Python 版本选择每个包的最新支持版本</li>
</ul></dd><dt id="uv-build--help"><a href="#uv-build--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助信息</p>
</dd><dt id="uv-build--index"><a href="#uv-build--index"><code>--index</code></a> <i>index</i></dt><dd><p>解析依赖时使用的 URL，作为默认索引的补充。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--default-index</code>（默认为 PyPI）指定的索引。当提供多个 <code>--index</code> 标志时，较早的值优先级更高。</p>
<p>不支持将索引名称作为值。相对路径必须通过 <code>./</code> 或 <code>../</code>（Unix）或 <code>.\\</code>、<code>..\\</code>、<code>./</code> 或 <code>../</code>（Windows）与索引名称区分开来。</p>
<p>也可通过 <code>UV_INDEX</code> 环境变量设置。</p></dd><dt id="uv-build--index-strategy"><a href="#uv-build--index-strategy"><code>--index-strategy</code></a> <i>index-strategy</i></dt><dd><p>针对多个索引 URL 进行解析时使用的策略。</p>
<p>默认情况下，uv 会在第一个包含给定包的索引处停止，并将解析限制为该第一个索引上存在的包（<code>first-index</code>）。这可以防止"依赖混淆"（dependency confusion）攻击，即攻击者可以在备用索引上以相同名称上传恶意包。</p>
<p>也可通过 <code>UV_INDEX_STRATEGY</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>first-index</code>：仅使用第一个为给定包名返回匹配结果的索引的结果</li>
<li><code>unsafe-first-match</code>：在所有索引中搜索每个包名，在转到下一个索引之前穷尽第一个索引的版本</li>
<li><code>unsafe-best-match</code>：在所有索引中搜索每个包名，优先选择找到的"最佳"版本。如果某个包版本在多个索引中，仅查看第一个索引中的条目</li>
</ul></dd><dt id="uv-build--index-url"><a href="#uv-build--index-url"><code>--index-url</code></a>, <code>-i</code> <i>index-url</i></dt><dd><p>（已弃用：请改用 <code>--default-index</code>）Python 包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志指定的索引的优先级低于通过 <code>--extra-index-url</code> 标志指定的所有其他索引。</p>
<p>也可通过 <code>UV_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-build--keyring-provider"><a href="#uv-build--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>尝试使用 <code>keyring</code> 进行索引 URL 的身份验证。</p>
<p>目前仅支持 <code>--keyring-provider subprocess</code>，它配置 uv 使用 <code>keyring</code> CLI 来处理身份验证。</p>
<p>默认为 <code>disabled</code>。</p>
<p>也可通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disabled</code>：不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>：使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-build--link-mode"><a href="#uv-build--link-mode"><code>--link-mode</code></a> <i>link-mode</i></dt><dd><p>从全局缓存安装包时使用的方法。</p>
<p>此选项仅在构建源码分发包时使用。</p>
<p>在 macOS 和 Linux 上默认为 <code>clone</code>（也称为写时复制 Copy-on-Write），在 Windows 上默认为 <code>hardlink</code>。</p>
<p>警告：不鼓励使用符号链接（symlink）链接模式，因为它们会在缓存和目标环境之间创建紧密耦合。例如，清除缓存（<code>uv cache clean</code>）将通过移除底层源文件来破坏所有已安装的包。请谨慎使用符号链接。</p>
<p>也可通过 <code>UV_LINK_MODE</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>clone</code>：将包从源克隆（即写时复制）到目标</li>
<li><code>copy</code>：将包从源复制到目标</li>
<li><code>hardlink</code>：将包从源硬链接到目标</li>
<li><code>symlink</code>：将包从源符号链接到目标</li>
</ul></dd><dt id="uv-build--managed-python"><a href="#uv-build--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用它管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-build--no-binary"><a href="#uv-build--no-binary"><code>--no-binary</code></a></dt><dd><p>不安装预构建的 wheel。</p>
<p>给定的包将从源码构建并安装。解析器仍将使用预构建的 wheel 来提取包元数据（如果可用）。</p>
<p>也可通过 <code>UV_NO_BINARY</code> 环境变量设置。</p></dd><dt id="uv-build--no-binary-package"><a href="#uv-build--no-binary-package"><code>--no-binary-package</code></a> <i>no-binary-package</i></dt><dd><p>不为特定包安装预构建的 wheel [env: <code>UV_NO_BINARY_PACKAGE</code>=]</p>
</dd><dt id="uv-build--no-build"><a href="#uv-build--no-build"><code>--no-build</code></a></dt><dd><p>不构建源码分发包。</p>
<p>启用后，解析将不会运行任意 Python 代码。已构建的源码分发包的缓存 wheel 将被重用，但需要构建分发包的操作将退出并报错。</p>
<p>也可通过 <code>UV_NO_BUILD</code> 环境变量设置。</p></dd><dt id="uv-build--no-build-isolation"><a href="#uv-build--no-build-isolation"><code>--no-build-isolation</code></a></dt><dd><p>构建源码分发包时禁用隔离。</p>
<p>假定 PEP 518 指定的构建依赖已经安装。</p>
<p>也可通过 <code>UV_NO_BUILD_ISOLATION</code> 环境变量设置。</p></dd><dt id="uv-build--no-build-isolation-package"><a href="#uv-build--no-build-isolation-package"><code>--no-build-isolation-package</code></a> <i>no-build-isolation-package</i></dt><dd><p>为特定包构建源码分发包时禁用隔离。</p>
<p>假定该包的 PEP 518 指定的构建依赖已经安装。</p>
</dd><dt id="uv-build--no-build-logs"><a href="#uv-build--no-build-logs"><code>--no-build-logs</code></a></dt><dd><p>隐藏构建后端的日志</p>
</dd><dt id="uv-build--no-build-package"><a href="#uv-build--no-build-package"><code>--no-build-package</code></a> <i>no-build-package</i></dt><dd><p>不为特定包构建源码分发包 [env: <code>UV_NO_BUILD_PACKAGE</code>=]</p>
</dd><dt id="uv-build--no-cache"><a href="#uv-build--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，在操作期间改用临时目录</p>
<p>也可通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-build--no-config"><a href="#uv-build--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-build--no-create-gitignore"><a href="#uv-build--no-create-gitignore"><code>--no-create-gitignore</code></a></dt><dd><p>不在输出目录中创建 <code>.gitignore</code> 文件。</p>
<p>默认情况下，uv 会在输出目录中创建一个 <code>.gitignore</code> 文件，以将构建产物排除在版本控制之外。使用此标志时，将省略该文件。</p>
</dd><dt id="uv-build--no-index"><a href="#uv-build--no-index"><code>--no-index</code></a></dt><dd><p>忽略注册表索引（例如 PyPI），改为依赖直接 URL 依赖和通过 <code>--find-links</code> 提供的依赖</p>
</dd><dt id="uv-build--no-managed-python"><a href="#uv-build--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd></dl>
