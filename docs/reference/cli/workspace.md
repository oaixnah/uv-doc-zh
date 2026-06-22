---
title: uv workspace
description: uv workspace 命令参考文档，涵盖工作空间元数据查看（uv workspace metadata）、成员路径显示（uv workspace dir）和成员列表（uv workspace list）三个子命令的完整中文说明，包括所有选项的详细参数解释和使用示例。
---

# uv workspace

查看 uv 工作空间

<h3 class="cli-reference">Usage</h3>

```
uv workspace [OPTIONS] <COMMAND>
```

<h3 class="cli-reference">Commands</h3>

<dl class="cli-reference"><dt><a href="#uv-workspace-metadata"><code>uv workspace metadata</code></a></dt><dd><p>查看当前工作空间的元数据</p></dd>
<dt><a href="#uv-workspace-dir"><code>uv workspace dir</code></a></dt><dd><p>显示工作空间成员的路径</p></dd>
<dt><a href="#uv-workspace-list"><code>uv workspace list</code></a></dt><dd><p>列出工作空间的成员</p></dd>
</dl>

### uv workspace metadata

查看当前工作空间的元数据。

此命令的输出尚未稳定。

<h3 class="cli-reference">Usage</h3>

```
uv workspace metadata [OPTIONS]
```

<h3 class="cli-reference">Options</h3>

<dl class="cli-reference"><dt id="uv-workspace-metadata--allow-insecure-host"><a href="#uv-workspace-metadata--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您面临中间人攻击。</p>
<p>May also be set with the <code>UV_INSECURE_HOST</code> environment variable.</p></dd><dt id="uv-workspace-metadata--cache-dir"><a href="#uv-workspace-metadata--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上默认为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>May also be set with the <code>UV_CACHE_DIR</code> environment variable.</p></dd><dt id="uv-workspace-metadata--color"><a href="#uv-workspace-metadata--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 在写入终端时会自动检测颜色支持。</p>
<p>可能的值：</p>
<ul>
<li><code>auto</code>:  仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>:  无论检测到的环境如何，都启用彩色输出</li>
<li><code>never</code>:  禁用彩色输出</li>
</ul></dd><dt id="uv-workspace-metadata--config-file"><a href="#uv-workspace-metadata--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许。</p>
<p>May also be set with the <code>UV_CONFIG_FILE</code> environment variable.</p></dd><dt id="uv-workspace-metadata--config-setting"><a href="#uv-workspace-metadata--config-setting"><code>--config-setting</code></a>, <code>--config-settings</code>, <code>-C</code> <i>config-setting</i></dt><dd><p>传递给 PEP 517 构建后端的设置，以 <code>KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-workspace-metadata--config-settings-package"><a href="#uv-workspace-metadata--config-settings-package"><code>--config-settings-package</code></a>, <code>--config-settings-package</code> <i>config-settings-package</i></dt><dd><p>传递给特定包 PEP 517 构建后端的设置，以 <code>PACKAGE:KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-workspace-metadata--default-index"><a href="#uv-workspace-metadata--default-index"><code>--default-index</code></a> <i>default-index</i></dt><dd><p>默认包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或以相同格式组织的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--index</code> 标志指定的所有其他索引。</p>
<p>May also be set with the <code>UV_DEFAULT_INDEX</code> environment variable.</p></dd><dt id="uv-workspace-metadata--directory"><a href="#uv-workspace-metadata--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到给定目录。</p>
<p>相对路径以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 仅更改项目根目录。</p>
<p>May also be set with the <code>UV_WORKING_DIR</code> environment variable.</p></dd><dt id="uv-workspace-metadata--dry-run"><a href="#uv-workspace-metadata--dry-run"><code>--dry-run</code></a></dt><dd><p>执行试运行，不写入锁文件。</p>
<p>在试运行模式下，uv 将解析项目的依赖关系并报告结果更改，但不会将锁文件写入磁盘。</p>
</dd><dt id="uv-workspace-metadata--exclude-newer"><a href="#uv-workspace-metadata--exclude-newer"><code>--exclude-newer</code></a> <i>exclude-newer</i></dt><dd><p>将候选包限制为在给定日期之前上传的包。</p>
<p>日期与每个单独分发制品（即每个文件上传到包索引的时间）的上传时间进行比较，而不是与包版本的发布日期进行比较。</p>
<p>接受 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、基于系统配置时区解析的相同格式本地日期（例如 <code>2006-12-02</code>）、"友好"持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不遵循本地时区的语义，始终解析为固定秒数，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月份和年份等日历单位。</p>
<p>May also be set with the <code>UV_EXCLUDE_NEWER</code> environment variable.</p></dd><dt id="uv-workspace-metadata--exclude-newer-package"><a href="#uv-workspace-metadata--exclude-newer-package"><code>--exclude-newer-package</code></a> <i>exclude-newer-package</i></dt><dd><p>将特定包的候选包限制为在给定日期之前上传的包。</p>
<p>接受 <code>PACKAGE=DATE</code> 格式的包-日期对，其中 <code>DATE</code> 是 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、基于系统配置时区解析的相同格式本地日期（例如 <code>2006-12-02</code>）、"友好"持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不遵循本地时区的语义，始终解析为固定秒数，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月份和年份等日历单位。</p>
<p>可以为不同的包多次提供。</p>
</dd><dt id="uv-workspace-metadata--extra-index-url"><a href="#uv-workspace-metadata--extra-index-url"><code>--extra-index-url</code></a> <i>extra-index-url</i></dt><dd><p>（已弃用：请改用 <code>--index</code>）除 <code>--index-url</code> 之外要使用的额外包索引 URL。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或以相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--index-url</code> 指定的索引（默认为 PyPI）。当提供多个 <code>--extra-index-url</code> 标志时，较早的值优先。</p>
<p>May also be set with the <code>UV_EXTRA_INDEX_URL</code> environment variable.</p></dd><dt id="uv-workspace-metadata--find-links"><a href="#uv-workspace-metadata--find-links"><code>--find-links</code></a>, <code>-f</code> <i>find-links</i></dt><dd><p>除了在注册表索引中找到的之外，还要搜索候选分发的位置。</p>
<p>如果是路径，目标必须是一个目录，顶层包含 wheel 文件（<code>.whl</code>）或源分发（例如 <code>.tar.gz</code> 或 <code>.zip</code>）形式的包。</p>
<p>如果是 URL，页面必须包含一个符合上述格式的包文件链接的扁平列表。</p>
<p>May also be set with the <code>UV_FIND_LINKS</code> environment variable.</p></dd><dt id="uv-workspace-metadata--fork-strategy"><a href="#uv-workspace-metadata--fork-strategy"><code>--fork-strategy</code></a> <i>fork-strategy</i></dt><dd><p>在跨 Python 版本和平台选择给定包的多个版本时使用的策略。</p>
<p>默认情况下，uv 会优化为每个受支持的 Python 版本（<code>requires-python</code>）选择每个包的最新版本，同时尽量减少跨平台选择的版本数量。</p>
<p>在 <code>fewest</code> 策略下，uv 会尽量减少每个包选择的版本数量，优先选择与更广泛受支持的 Python 版本或平台兼容的旧版本。</p>
<p>May also be set with the <code>UV_FORK_STRATEGY</code> environment variable.</p><p>可能的值：</p>
<ul>
<li><code>fewest</code>:  优化为选择每个包的最少版本数量。如果旧版本与更广泛的受支持 Python 版本或平台兼容，则可能优先选择旧版本</li>
<li><code>requires-python</code>:  优化为每个受支持的 Python 版本选择每个包的最新支持版本</li>
</ul></dd><dt id="uv-workspace-metadata--frozen"><a href="#uv-workspace-metadata--frozen"><code>--frozen</code></a></dt><dd><p>断言 <code>uv.lock</code> 存在，但不检查它是否是最新的 [env: UV_FROZEN=]</p>
</dd><dt id="uv-workspace-metadata--help"><a href="#uv-workspace-metadata--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助</p>
</dd><dt id="uv-workspace-metadata--index"><a href="#uv-workspace-metadata--index"><code>--index</code></a> <i>index</i></dt><dd><p>解析依赖关系时使用的 URL，作为默认索引的补充。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或以相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--default-index</code> 指定的索引（默认为 PyPI）。当提供多个 <code>--index</code> 标志时，较早的值优先。</p>
<p>不支持将索引名称作为值。在 Unix 上，相对路径必须使用 <code>./</code> 或 <code>../</code> 与索引名称区分，在 Windows 上使用 <code>.\\</code>、<code>..\\</code>、<code>./</code> 或 <code>../</code>。</p>
<p>May also be set with the <code>UV_INDEX</code> environment variable.</p></dd><dt id="uv-workspace-metadata--index-strategy"><a href="#uv-workspace-metadata--index-strategy"><code>--index-strategy</code></a> <i>index-strategy</i></dt><dd><p>针对多个索引 URL 进行解析时使用的策略。</p>
<p>默认情况下，uv 会在第一个找到给定包的索引处停止，并将解析限制为该第一个索引上存在的包（<code>first-index</code>）。这可以防止"依赖混淆"攻击，即攻击者可以在备用索引上以相同名称上传恶意包。</p>
<p>May also be set with the <code>UV_INDEX_STRATEGY</code> environment variable.</p><p>可能的值：</p>
<ul>
<li><code>first-index</code>:  仅使用第一个为给定包名返回匹配结果的索引</li>
<li><code>unsafe-first-match</code>:  在所有索引中搜索每个包名，在移动到下一个索引之前穷尽第一个索引的版本</li>
<li><code>unsafe-best-match</code>:  在所有索引中搜索每个包名，优先选择找到的"最佳"版本。如果一个包版本存在于多个索引中，则只查看第一个索引的条目</li>
</ul></dd><dt id="uv-workspace-metadata--index-url"><a href="#uv-workspace-metadata--index-url"><code>--index-url</code></a>, <code>-i</code> <i>index-url</i></dt><dd><p>（已弃用：请改用 <code>--default-index</code>）Python 包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或以相同格式组织的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--extra-index-url</code> 标志指定的所有其他索引。</p>
<p>May also be set with the <code>UV_INDEX_URL</code> environment variable.</p></dd><dt id="uv-workspace-metadata--keyring-provider"><a href="#uv-workspace-metadata--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>尝试使用 <code>keyring</code> 对索引 URL 进行身份验证。</p>
<p>目前，仅支持 <code>--keyring-provider subprocess</code>，它配置 uv 使用 <code>keyring</code> CLI 来处理身份验证。</p>
<p>默认为 <code>disabled</code>。</p>
<p>May also be set with the <code>UV_KEYRING_PROVIDER</code> environment variable.</p><p>可能的值：</p>
<ul>
<li><code>disabled</code>:  不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>:  使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-workspace-metadata--link-mode"><a href="#uv-workspace-metadata--link-mode"><code>--link-mode</code></a> <i>link-mode</i></dt><dd><p>从全局缓存安装包时使用的方法。</p>
<p>此选项仅在构建源代码分发时使用。</p>
<p>在 macOS 和 Linux 上默认为 <code>clone</code>（也称为写时复制），在 Windows 上默认为 <code>hardlink</code>。</p>
<p>警告：不鼓励使用 symlink 链接模式，因为它会在缓存和目标环境之间创建紧密耦合。例如，清除缓存（<code>uv cache clean</code>）将通过删除底层源文件来破坏所有已安装的包。请谨慎使用 symlink。</p>
<p>May also be set with the <code>UV_LINK_MODE</code> environment variable.</p><p>可能的值：</p>
<ul>
<li><code>clone</code>:  将包从源克隆（即写时复制）到目标</li>
<li><code>copy</code>:  将包从源复制到目标</li>
<li><code>hardlink</code>:  将包从源硬链接到目标</li>
<li><code>symlink</code>:  将包从源符号链接到目标</li>
</ul></dd><dt id="uv-workspace-metadata--locked"><a href="#uv-workspace-metadata--locked"><code>--locked</code></a></dt><dd><p>检查锁文件是否是最新的 [env: UV_LOCKED=]</p>
<p>断言 <code>uv.lock</code> 在解析后保持不变。如果锁文件缺失或需要更新，uv 将退出并报错。</p>
</dd><dt id="uv-workspace-metadata--managed-python"><a href="#uv-workspace-metadata--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用它管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-workspace-metadata--no-binary"><a href="#uv-workspace-metadata--no-binary"><code>--no-binary</code></a></dt><dd><p>不安装预构建的 wheel。</p>
<p>给定的包将从源代码构建并安装。解析器仍将使用预构建的 wheel 来提取包元数据（如果可用）。</p>
<p>May also be set with the <code>UV_NO_BINARY</code> environment variable.</p></dd><dt id="uv-workspace-metadata--no-binary-package"><a href="#uv-workspace-metadata--no-binary-package"><code>--no-binary-package</code></a> <i>no-binary-package</i></dt><dd><p>不为特定包安装预构建的 wheel [env: <code>UV_NO_BINARY_PACKAGE</code>=]</p>
</dd><dt id="uv-workspace-metadata--no-build"><a href="#uv-workspace-metadata--no-build"><code>--no-build</code></a></dt><dd><p>不构建源代码分发。</p>
<p>启用后，解析将不会运行任意 Python 代码。已构建的源代码分发的缓存 wheel 将被重用，但需要构建分发的操作将退出并报错。</p>
<p>May also be set with the <code>UV_NO_BUILD</code> environment variable.</p></dd><dt id="uv-workspace-metadata--no-build-isolation"><a href="#uv-workspace-metadata--no-build-isolation"><code>--no-build-isolation</code></a></dt><dd><p>在构建源代码分发时禁用隔离。</p>
<p>假定 PEP 518 指定的构建依赖项已安装。</p>
<p>May also be set with the <code>UV_NO_BUILD_ISOLATION</code> environment variable.</p></dd><dt id="uv-workspace-metadata--no-build-isolation-package"><a href="#uv-workspace-metadata--no-build-isolation-package"><code>--no-build-isolation-package</code></a> <i>no-build-isolation-package</i></dt><dd><p>在构建特定包的源代码分发时禁用隔离。</p>
<p>假定该包由 PEP 518 指定的构建依赖项已安装。</p>
</dd><dt id="uv-workspace-metadata--no-build-package"><a href="#uv-workspace-metadata--no-build-package"><code>--no-build-package</code></a> <i>no-build-package</i></dt><dd><p>不为特定包构建源代码分发 [env: <code>UV_NO_BUILD_PACKAGE</code>=]</p>
</dd><dt id="uv-workspace-metadata--no-cache"><a href="#uv-workspace-metadata--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>May also be set with the <code>UV_NO_CACHE</code> environment variable.</p></dd><dt id="uv-workspace-metadata--no-config"><a href="#uv-workspace-metadata--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>May also be set with the <code>UV_NO_CONFIG</code> environment variable.</p></dd><dt id="uv-workspace-metadata--no-index"><a href="#uv-workspace-metadata--no-index"><code>--no-index</code></a></dt><dd><p>忽略注册表索引（例如 PyPI），转而依赖直接 URL 依赖项和通过 <code>--find-links</code> 提供的依赖项</p>
</dd><dt id="uv-workspace-metadata--no-managed-python"><a href="#uv-workspace-metadata--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-workspace-metadata--no-progress"><a href="#uv-workspace-metadata--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转指示器或进度条。</p>
</dd><dt id="uv-workspace-metadata--no-python-downloads"><a href="#uv-workspace-metadata--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用自动下载 Python。</p>
</dd><dt id="uv-workspace-metadata--no-sources"><a href="#uv-workspace-metadata--no-sources"><code>--no-sources</code></a></dt><dd><p>在解析依赖关系时忽略 <code>tool.uv.sources</code> 表。用于根据符合标准、可发布的包元数据进行锁定，而不是使用任何工作空间、Git、URL 或本地路径源</p>
<p>May also be set with the <code>UV_NO_SOURCES</code> environment variable.</p></dd><dt id="uv-workspace-metadata--no-sources-package"><a href="#uv-workspace-metadata--no-sources-package"><code>--no-sources-package</code></a> <i>no-sources-package</i></dt><dd><p>不对指定的包使用 <code>tool.uv.sources</code> 表中的源 [env: <code>UV_NO_SOURCES_PACKAGE</code>=]</p>
</dd><dt id="uv-workspace-metadata--offline"><a href="#uv-workspace-metadata--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存的数据和本地可用的文件。</p>
</dd><dt id="uv-workspace-metadata--prerelease"><a href="#uv-workspace-metadata--prerelease"><code>--prerelease</code></a> <i>prerelease</i></dt><dd><p>考虑预发布版本时使用的策略。</p>
<p>默认情况下，uv 将接受<em>仅</em>发布预发布版本的包，以及在其声明的版本说明符中包含显式预发布标记的第一方需求（<code>if-necessary-or-explicit</code>）。</p>
<p>May also be set with the <code>UV_PRERELEASE</code> environment variable.</p><p>可能的值：</p>
<ul>
<li><code>disallow</code>:  不允许所有预发布版本</li>
<li><code>allow</code>:  允许所有预发布版本</li>
<li><code>if-necessary</code>:  如果包的所有版本都是预发布版本，则允许预发布版本</li>
<li><code>explicit</code>:  允许在其版本需求中包含显式预发布标记的第一方包的预发布版本</li>
<li><code>if-necessary-or-explicit</code>:  如果包的所有版本都是预发布版本，或包在其版本需求中包含显式预发布标记，则允许预发布版本</li>
</ul></dd><dt id="uv-workspace-metadata--project"><a href="#uv-workspace-metadata--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>参见 <code>--directory</code> 完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>May also be set with the <code>UV_PROJECT</code> environment variable.</p></dd><dt id="uv-workspace-metadata--python"><a href="#uv-workspace-metadata--python"><code>--python</code></a>, <code>-p</code> <i>python</i></dt><dd><p>解析期间使用的 Python 解释器。</p>
<p>当没有 wheel 时，构建源代码分发需要 Python 解释器来确定包元数据。</p>
<p>如果未设置 <code>requires-python</code>，该解释器也用作最低 Python 版本的回退值。</p>
<p>有关 Python 发现和支持的请求格式的详细信息，请参阅 <a href="#uv-python">uv python</a>。</p>
<p>May also be set with the <code>UV_PYTHON</code> environment variable.</p></dd><dt id="uv-workspace-metadata--quiet"><a href="#uv-workspace-metadata--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，其中 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-workspace-metadata--refresh"><a href="#uv-workspace-metadata--refresh"><code>--refresh</code></a></dt><dd><p>刷新所有缓存数据</p>
</dd><dt id="uv-workspace-metadata--refresh-package"><a href="#uv-workspace-metadata--refresh-package"><code>--refresh-package</code></a> <i>refresh-package</i></dt><dd><p>刷新特定包的缓存数据</p>
</dd><dt id="uv-workspace-metadata--resolution"><a href="#uv-workspace-metadata--resolution"><code>--resolution</code></a> <i>resolution</i></dt><dd><p>在给定包需求的不同兼容版本之间进行选择时使用的策略。</p>
<p>默认情况下，uv 将使用每个包的最新兼容版本（<code>highest</code>）。</p>
<p>May also be set with the <code>UV_RESOLUTION</code> environment variable.</p><p>可能的值：</p>
<ul>
<li><code>highest</code>:  解析每个包的最高兼容版本</li>
<li><code>lowest</code>:  解析每个包的最低兼容版本</li>
<li><code>lowest-direct</code>:  解析所有直接依赖项的最低兼容版本，以及任何传递依赖项的最高兼容版本</li>
</ul></dd><dt id="uv-workspace-metadata--script"><a href="#uv-workspace-metadata--script"><code>--script</code></a> <i>script</i></dt><dd><p>查看指定 PEP 723 Python 脚本的元数据，而不是当前工作空间。</p>
<p>如果提供，uv 将根据脚本的内联元数据表解析依赖关系，遵循 PEP 723。</p>
</dd><dt id="uv-workspace-metadata--sync"><a href="#uv-workspace-metadata--sync"><code>--sync</code></a></dt><dd><p>同步环境以在输出中包含模块所有权元数据。</p>
<p>这将添加一个从可导入模块名称到提供它们的包节点引用的映射。为此，venv 将以非精确模式同步。</p>
</dd><dt id="uv-workspace-metadata--system-certs"><a href="#uv-workspace-metadata--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其在 macOS 上）。</p>
<p>但是，在某些情况下，您可能需要使用平台的原生证书存储，特别是如果您依赖系统证书存储中包含的企业信任根（例如，用于强制代理）。</p>
</dd><dt id="uv-workspace-metadata--upgrade"><a href="#uv-workspace-metadata--upgrade"><code>--upgrade</code></a>, <code>-U</code></dt><dd><p>允许包升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh</code></p>
</dd><dt id="uv-workspace-metadata--upgrade-group"><a href="#uv-workspace-metadata--upgrade-group"><code>--upgrade-group</code></a> <i>upgrade-group</i></dt><dd><p>允许依赖组中所有包的升级，忽略任何现有输出文件中的固定版本</p>
</dd><dt id="uv-workspace-metadata--upgrade-package"><a href="#uv-workspace-metadata--upgrade-package"><code>--upgrade-package</code></a>, <code>-P</code> <i>upgrade-package</i></dt><dd><p>允许特定包的升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-workspace-metadata--verbose"><a href="#uv-workspace-metadata--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。 (<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>)</p>
</dd></dl>

### uv workspace dir

显示工作空间成员的路径。

默认情况下，显示工作空间根目录的路径。可以使用 `--package` 选项来显示工作空间成员的路径。

如果在工作空间之外使用，即找不到 `pyproject.toml`，uv 将退出并报错。

<h3 class="cli-reference">Usage</h3>

```
uv workspace dir [OPTIONS]
```

<h3 class="cli-reference">Options</h3>

<dl class="cli-reference"><dt id="uv-workspace-dir--allow-insecure-host"><a href="#uv-workspace-dir--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您面临中间人攻击。</p>
<p>May also be set with the <code>UV_INSECURE_HOST</code> environment variable.</p></dd><dt id="uv-workspace-dir--cache-dir"><a href="#uv-workspace-dir--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上默认为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>May also be set with the <code>UV_CACHE_DIR</code> environment variable.</p></dd><dt id="uv-workspace-dir--color"><a href="#uv-workspace-dir--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 在写入终端时会自动检测颜色支持。</p>
<p>可能的值：</p>
<ul>
<li><code>auto</code>:  仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>:  无论检测到的环境如何，都启用彩色输出</li>
<li><code>never</code>:  禁用彩色输出</li>
</ul></dd><dt id="uv-workspace-dir--config-file"><a href="#uv-workspace-dir--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许。</p>
<p>May also be set with the <code>UV_CONFIG_FILE</code> environment variable.</p></dd><dt id="uv-workspace-dir--directory"><a href="#uv-workspace-dir--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到给定目录。</p>
<p>相对路径以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 仅更改项目根目录。</p>
<p>May also be set with the <code>UV_WORKING_DIR</code> environment variable.</p></dd><dt id="uv-workspace-dir--help"><a href="#uv-workspace-dir--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助</p>
</dd><dt id="uv-workspace-dir--managed-python"><a href="#uv-workspace-dir--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用它管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-workspace-dir--no-cache"><a href="#uv-workspace-dir--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>May also be set with the <code>UV_NO_CACHE</code> environment variable.</p></dd><dt id="uv-workspace-dir--no-config"><a href="#uv-workspace-dir--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>May also be set with the <code>UV_NO_CONFIG</code> environment variable.</p></dd><dt id="uv-workspace-dir--no-managed-python"><a href="#uv-workspace-dir--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-workspace-dir--no-progress"><a href="#uv-workspace-dir--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转指示器或进度条。</p>
</dd><dt id="uv-workspace-dir--no-python-downloads"><a href="#uv-workspace-dir--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用自动下载 Python。</p>
</dd><dt id="uv-workspace-dir--offline"><a href="#uv-workspace-dir--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存的数据和本地可用的文件。</p>
</dd><dt id="uv-workspace-dir--package"><a href="#uv-workspace-dir--package"><code>--package</code></a> <i>package</i></dt><dd><p>显示工作空间中特定包的路径</p>
</dd><dt id="uv-workspace-dir--project"><a href="#uv-workspace-dir--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>参见 <code>--directory</code> 完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>May also be set with the <code>UV_PROJECT</code> environment variable.</p></dd><dt id="uv-workspace-dir--quiet"><a href="#uv-workspace-dir--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，其中 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-workspace-dir--system-certs"><a href="#uv-workspace-dir--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其在 macOS 上）。</p>
<p>但是，在某些情况下，您可能需要使用平台的原生证书存储，特别是如果您依赖系统证书存储中包含的企业信任根（例如，用于强制代理）。</p>
</dd><dt id="uv-workspace-dir--verbose"><a href="#uv-workspace-dir--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。 (<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>)</p>
</dd></dl>

### uv workspace list

列出工作空间的成员。

显示以换行符分隔的工作空间成员名称。

<h3 class="cli-reference">Usage</h3>

```
uv workspace list [OPTIONS]
```

<h3 class="cli-reference">Options</h3>

<dl class="cli-reference"><dt id="uv-workspace-list--allow-insecure-host"><a href="#uv-workspace-list--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您面临中间人攻击。</p>
<p>May also be set with the <code>UV_INSECURE_HOST</code> environment variable.</p></dd><dt id="uv-workspace-list--cache-dir"><a href="#uv-workspace-list--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上默认为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>May also be set with the <code>UV_CACHE_DIR</code> environment variable.</p></dd><dt id="uv-workspace-list--color"><a href="#uv-workspace-list--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 在写入终端时会自动检测颜色支持。</p>
<p>可能的值：</p>
<ul>
<li><code>auto</code>:  仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>:  无论检测到的环境如何，都启用彩色输出</li>
<li><code>never</code>:  禁用彩色输出</li>
</ul></dd><dt id="uv-workspace-list--config-file"><a href="#uv-workspace-list--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许。</p>
<p>May also be set with the <code>UV_CONFIG_FILE</code> environment variable.</p></dd><dt id="uv-workspace-list--directory"><a href="#uv-workspace-list--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到给定目录。</p>
<p>相对路径以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 仅更改项目根目录。</p>
<p>May also be set with the <code>UV_WORKING_DIR</code> environment variable.</p></dd><dt id="uv-workspace-list--help"><a href="#uv-workspace-list--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助</p>
</dd><dt id="uv-workspace-list--managed-python"><a href="#uv-workspace-list--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用它管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-workspace-list--no-cache"><a href="#uv-workspace-list--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>May also be set with the <code>UV_NO_CACHE</code> environment variable.</p></dd><dt id="uv-workspace-list--no-config"><a href="#uv-workspace-list--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>May also be set with the <code>UV_NO_CONFIG</code> environment variable.</p></dd><dt id="uv-workspace-list--no-managed-python"><a href="#uv-workspace-list--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-workspace-list--no-progress"><a href="#uv-workspace-list--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转指示器或进度条。</p>
</dd><dt id="uv-workspace-list--no-python-downloads"><a href="#uv-workspace-list--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用自动下载 Python。</p>
</dd><dt id="uv-workspace-list--offline"><a href="#uv-workspace-list--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存的数据和本地可用的文件。</p>
</dd><dt id="uv-workspace-list--paths"><a href="#uv-workspace-list--paths"><code>--paths</code></a></dt><dd><p>显示路径而不是名称</p>
</dd><dt id="uv-workspace-list--project"><a href="#uv-workspace-list--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>参见 <code>--directory</code> 完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>May also be set with the <code>UV_PROJECT</code> environment variable.</p></dd><dt id="uv-workspace-list--quiet"><a href="#uv-workspace-list--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，其中 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-workspace-list--system-certs"><a href="#uv-workspace-list--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其在 macOS 上）。</p>
<p>但是，在某些情况下，您可能需要使用平台的原生证书存储，特别是如果您依赖系统证书存储中包含的企业信任根（例如，用于强制代理）。</p>
</dd><dt id="uv-workspace-list--verbose"><a href="#uv-workspace-list--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。 (<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>)</p>
</dd></dl>