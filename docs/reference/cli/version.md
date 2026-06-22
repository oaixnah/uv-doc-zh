---
title: uv version
description: uv version 是 astral-sh/uv 包管理器中用于读取和更新项目版本的 CLI 命令。支持直接设置版本号，或通过 --bump 选项按语义化版本规范递增 major、minor、patch、alpha、beta、rc 等版本组件，支持干运行预览和 JSON 输出格式。本文档提供 uv version 命令的完整参数和选项说明。
---

# uv version

读取或更新项目的版本。

<h3 class="cli-reference">Usage</h3>

```
uv version [OPTIONS] [VALUE]
```

<h3 class="cli-reference">Arguments</h3>

<dl class="cli-reference"><dt id="uv-version--value"><a href="#uv-version--value"><code>VALUE</code></a></dt><dd><p>将项目版本设置为此值</p>
<p>要通过语义化版本组件来更新项目，请改用 <code>--bump</code>。</p>
</dd></dl>

<h3 class="cli-reference">Options</h3>

<dl class="cli-reference"><dt id="uv-version--active"><a href="#uv-version--active"><code>--active</code></a></dt><dd><p>优先使用激活的虚拟环境，而非项目的虚拟环境。</p>
<p>如果项目的虚拟环境已激活或没有虚拟环境处于激活状态，则此选项无效。</p>
</dd><dt id="uv-version--allow-insecure-host"><a href="#uv-version--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您遭受中间人攻击（MITM）。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-version--bump"><a href="#uv-version--bump"><code>--bump</code></a> <i>bump[=value]</i></dt><dd><p>使用给定的语义更新项目版本</p>
<p>此标志可以多次传递。</p>
<p>可选值：</p>
<ul>
<li><code>major</code>:  增加主版本号（例如 1.2.3 =&gt; 2.0.0）</li>
<li><code>minor</code>:  增加次版本号（例如 1.2.3 =&gt; 1.3.0）</li>
<li><code>patch</code>:  增加修订版本号（例如 1.2.3 =&gt; 1.2.4）</li>
<li><code>stable</code>:  从预发布版本移至稳定版本（例如 1.2.3b4.post5.dev6 =&gt; 1.2.3）</li>
<li><code>alpha</code>:  增加 alpha 版本号（例如 1.2.3a4 =&gt; 1.2.3a5）</li>
<li><code>beta</code>:  增加 beta 版本号（例如 1.2.3b4 =&gt; 1.2.3b5）</li>
<li><code>rc</code>:  增加 rc 版本号（例如 1.2.3rc4 =&gt; 1.2.3rc5）</li>
<li><code>post</code>:  增加 post 版本号（例如 1.2.3.post5 =&gt; 1.2.3.post6）</li>
<li><code>dev</code>:  增加 dev 版本号（例如 1.2.3a4.dev6 =&gt; 1.2.3.dev7）</li>
</ul></dd><dt id="uv-version--cache-dir"><a href="#uv-version--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录路径。</p>
<p>默认情况下，在 macOS 和 Linux 上为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-version--color"><a href="#uv-version--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 在写入终端时会自动检测颜色支持。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>:  仅当输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>:  无论检测到的环境如何，都启用彩色输出</li>
<li><code>never</code>:  禁用彩色输出</li>
</ul></dd><dt id="uv-version--compile-bytecode"><a href="#uv-version--compile-bytecode"><code>--compile-bytecode</code></a>, <code>--compile</code></dt><dd><p>安装后将 Python 文件编译为字节码。</p>
<p>默认情况下，uv 不会将 Python（<code>.py</code>）文件编译为字节码（<code>__pycache__/*.pyc</code>）；而是在第一次导入模块时延迟编译。对于启动时间至关重要的使用场景，例如 CLI 应用程序和 Docker 容器，启用此选项可以用更长的安装时间换取更快的启动速度。</p>
<p>启用后，uv 会为了一致性处理整个 site-packages 目录（包括当前操作未修改的包）。与 pip 一样，它也会忽略错误。</p>
<p>也可以通过 <code>UV_COMPILE_BYTECODE</code> 环境变量设置。</p></dd><dt id="uv-version--config-file"><a href="#uv-version--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用作配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许使用。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-version--config-setting"><a href="#uv-version--config-setting"><code>--config-setting</code></a>, <code>--config-settings</code>, <code>-C</code> <i>config-setting</i></dt><dd><p>传递给 PEP 517 构建后端的设置，格式为 <code>KEY=VALUE</code> 对</p>
</dd><dt id="uv-version--config-settings-package"><a href="#uv-version--config-settings-package"><code>--config-settings-package</code></a>, <code>--config-settings-package</code> <i>config-settings-package</i></dt><dd><p>传递给特定包的 PEP 517 构建后端的设置，格式为 <code>PACKAGE:KEY=VALUE</code> 对</p>
</dd><dt id="uv-version--default-index"><a href="#uv-version--default-index"><code>--default-index</code></a> <i>default-index</i></dt><dd><p>默认包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--index</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_DEFAULT_INDEX</code> 环境变量设置。</p></dd><dt id="uv-version--directory"><a href="#uv-version--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到给定的目录。</p>
<p>相对路径以给定的目录为基准进行解析。</p>
<p>参见 <code>--project</code> 以仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-version--dry-run"><a href="#uv-version--dry-run"><code>--dry-run</code></a></dt><dd><p>不将新版本写入 <code>pyproject.toml</code></p>
<p>相反，版本将仅被显示出来。</p>
</dd><dt id="uv-version--exclude-newer"><a href="#uv-version--exclude-newer"><code>--exclude-newer</code></a> <i>exclude-newer</i></dt><dd><p>将候选包限制为在给定日期之前上传的版本。</p>
<p>日期是与每个分发作品的<em>上传时间</em>（即每个文件上传到包索引的时间）进行比较，而不是与包版本的发布日期进行比较。</p>
<p>接受 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、相同格式的本地日期（例如 <code>2006-12-02</code>，基于系统配置的时区解析）、&quot;友好&quot;持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不遵循本地时区的语义，始终以固定秒数解析，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月和年等日历单位。</p>
<p>也可以通过 <code>UV_EXCLUDE_NEWER</code> 环境变量设置。</p></dd><dt id="uv-version--exclude-newer-package"><a href="#uv-version--exclude-newer-package"><code>--exclude-newer-package</code></a> <i>exclude-newer-package</i></dt><dd><p>将特定包的候选版本限制为在给定日期之前上传的版本。</p>
<p>接受格式为 <code>PACKAGE=DATE</code> 的包-日期对，其中 <code>DATE</code> 是 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、相同格式的本地日期（例如 <code>2006-12-02</code>，基于系统配置的时区解析）、&quot;友好&quot;持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不遵循本地时区的语义，始终以固定秒数解析，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月和年等日历单位。</p>
<p>可以为不同的包多次提供。</p>
</dd><dt id="uv-version--extra-index-url"><a href="#uv-version--extra-index-url"><code>--extra-index-url</code></a> <i>extra-index-url</i></dt><dd><p>（已弃用：请改用 <code>--index</code>）除 <code>--index-url</code> 之外要使用的额外包索引 URL。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--index-url</code>（默认为 PyPI）指定的索引。当提供多个 <code>--extra-index-url</code> 标志时，较早的值优先级更高。</p>
<p>也可以通过 <code>UV_EXTRA_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-version--find-links"><a href="#uv-version--find-links"><code>--find-links</code></a>, <code>-f</code> <i>find-links</i></dt><dd><p>搜索候选分发作品的位置，作为注册表索引之外的补充来源。</p>
<p>如果是路径，目标必须是一个目录，顶层包含作为 wheel 文件（<code>.whl</code>）或源代码分发（例如 <code>.tar.gz</code> 或 <code>.zip</code>）的包。</p>
<p>如果是 URL，页面必须包含一个扁平列表，列出符合上述格式的包文件链接。</p>
<p>也可以通过 <code>UV_FIND_LINKS</code> 环境变量设置。</p></dd><dt id="uv-version--fork-strategy"><a href="#uv-version--fork-strategy"><code>--fork-strategy</code></a> <i>fork-strategy</i></dt><dd><p>在跨 Python 版本和平台选择给定包的多个版本时使用的策略。</p>
<p>默认情况下，uv 会优化为每个受支持的 Python 版本（<code>requires-python</code>）选择每个包的最新版本，同时最小化跨平台的选定版本数量。</p>
<p>在 <code>fewest</code> 策略下，uv 会最小化每个包的选定版本数量，倾向于选择与更广泛的受支持 Python 版本或平台兼容的较旧版本。</p>
<p>也可以通过 <code>UV_FORK_STRATEGY</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>fewest</code>:  优化为每个包选择最少的版本数量。如果较旧版本与更广泛的受支持 Python 版本或平台兼容，则可能优先选择较旧版本</li>
<li><code>requires-python</code>:  优化为每个受支持的 Python 版本选择每个包的最新支持版本</li>
</ul></dd><dt id="uv-version--frozen"><a href="#uv-version--frozen"><code>--frozen</code></a></dt><dd><p>更新版本而不重新锁定项目 [env: UV_FROZEN=]</p>
<p>项目环境将不会同步。</p>
</dd><dt id="uv-version--help"><a href="#uv-version--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简洁帮助信息</p>
</dd><dt id="uv-version--index"><a href="#uv-version--index"><code>--index</code></a> <i>index</i></dt><dd><p>解析依赖项时使用的 URL，作为默认索引之外的补充。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--default-index</code>（默认为 PyPI）指定的索引。当提供多个 <code>--index</code> 标志时，较早的值优先级更高。</p>
<p>不支持索引名称作为值。相对路径必须通过以下方式与索引名称区分：在 Unix 上使用 <code>./</code> 或 <code>../</code>，在 Windows 上使用 <code>.\\</code>、<code>..\\</code>、<code>./</code> 或 <code>../</code>。</p>
<p>也可以通过 <code>UV_INDEX</code> 环境变量设置。</p></dd><dt id="uv-version--index-strategy"><a href="#uv-version--index-strategy"><code>--index-strategy</code></a> <i>index-strategy</i></dt><dd><p>在多个索引 URL 之间解析时使用的策略。</p>
<p>默认情况下，uv 会在第一个包含给定包的索引处停止，并将解析限制在该第一个索引上存在的版本（<code>first-index</code>）。这可以防止&quot;依赖混淆&quot;攻击，即攻击者可以在备用索引上上传同名的恶意包。</p>
<p>也可以通过 <code>UV_INDEX_STRATEGY</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>first-index</code>:  仅使用第一个为给定包名返回匹配的索引的结果</li>
<li><code>unsafe-first-match</code>:  在所有索引中搜索每个包名，在转到下一个索引之前耗尽第一个索引的版本</li>
<li><code>unsafe-best-match</code>:  在所有索引中搜索每个包名，优先选择&quot;最佳&quot;版本。如果某个包版本存在于多个索引中，则仅查看第一个索引中的条目</li>
</ul></dd><dt id="uv-version--index-url"><a href="#uv-version--index-url"><code>--index-url</code></a>, <code>-i</code> <i>index-url</i></dt><dd><p>（已弃用：请改用 <code>--default-index</code>）Python 包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--extra-index-url</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-version--keyring-provider"><a href="#uv-version--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>尝试使用 <code>keyring</code> 进行索引 URL 的身份验证。</p>
<p>目前仅支持 <code>--keyring-provider subprocess</code>，它配置 uv 使用 <code>keyring</code> CLI 来处理身份验证。</p>
<p>默认为 <code>disabled</code>。</p>
<p>也可以通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disabled</code>:  不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>:  使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-version--link-mode"><a href="#uv-version--link-mode"><code>--link-mode</code></a> <i>link-mode</i></dt><dd><p>从全局缓存安装包时使用的方法。</p>
<p>默认情况下，在 macOS 和 Linux 上为 <code>clone</code>（也称为写时复制），在 Windows 上为 <code>hardlink</code>。</p>
<p>警告：不鼓励使用 symlink 链接模式，因为它会在缓存和目标环境之间创建紧密耦合。例如，清除缓存（<code>uv cache clean</code>）将通过删除底层源文件来破坏所有已安装的包。请谨慎使用符号链接。</p>
<p>也可以通过 <code>UV_LINK_MODE</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>clone</code>:  从源克隆（即写时复制）包到目标位置</li>
<li><code>copy</code>:  从源复制包到目标位置</li>
<li><code>hardlink</code>:  从源硬链接包到目标位置</li>
<li><code>symlink</code>:  从源符号链接包到目标位置</li>
</ul></dd><dt id="uv-version--locked"><a href="#uv-version--locked"><code>--locked</code></a></dt><dd><p>断言 <code>uv.lock</code> 将保持不变 [env: UV_LOCKED=]</p>
<p>需要锁文件是最新的。如果锁文件缺失或需要更新，uv 将退出并报错。</p>
</dd><dt id="uv-version--managed-python"><a href="#uv-version--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 倾向于使用它管理的 Python 版本。但是，如果没有安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-version--no-binary"><a href="#uv-version--no-binary"><code>--no-binary</code></a></dt><dd><p>不安装预构建的 wheel。</p>
<p>给定的包将从源代码构建和安装。解析器仍将使用预构建的 wheel 来提取包元数据（如果可用）。</p>
<p>也可以通过 <code>UV_NO_BINARY</code> 环境变量设置。</p></dd><dt id="uv-version--no-binary-package"><a href="#uv-version--no-binary-package"><code>--no-binary-package</code></a> <i>no-binary-package</i></dt><dd><p>不为特定包安装预构建的 wheel [env: <code>UV_NO_BINARY_PACKAGE</code>=]</p>
</dd><dt id="uv-version--no-build"><a href="#uv-version--no-build"><code>--no-build</code></a></dt><dd><p>不构建源代码分发。</p>
<p>启用后，解析过程不会运行任意 Python 代码。将重用已构建源代码分发的缓存 wheel，但需要构建分发的操作将退出并报错。</p>
<p>也可以通过 <code>UV_NO_BUILD</code> 环境变量设置。</p></dd><dt id="uv-version--no-build-isolation"><a href="#uv-version--no-build-isolation"><code>--no-build-isolation</code></a></dt><dd><p>构建源代码分发时禁用隔离。</p>
<p>假设 PEP 518 指定的构建依赖已安装。</p>
<p>也可以通过 <code>UV_NO_BUILD_ISOLATION</code> 环境变量设置。</p></dd><dt id="uv-version--no-build-isolation-package"><a href="#uv-version--no-build-isolation-package"><code>--no-build-isolation-package</code></a> <i>no-build-isolation-package</i></dt><dd><p>为特定包构建源代码分发时禁用隔离。</p>
<p>假设 PEP 518 指定的该包的构建依赖已安装。</p>
</dd><dt id="uv-version--no-build-package"><a href="#uv-version--no-build-package"><code>--no-build-package</code></a> <i>no-build-package</i></dt><dd><p>不为特定包构建源代码分发 [env: <code>UV_NO_BUILD_PACKAGE</code>=]</p>
</dd><dt id="uv-version--no-cache"><a href="#uv-version--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-version--no-config"><a href="#uv-version--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-version--no-index"><a href="#uv-version--no-index"><code>--no-index</code></a></dt><dd><p>忽略注册表索引（例如 PyPI），转而依赖直接 URL 依赖项和通过 <code>--find-links</code> 提供的依赖项</p>
</dd><dt id="uv-version--no-managed-python"><a href="#uv-version--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>取而代之，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-version--no-progress"><a href="#uv-version--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转指示器或进度条。</p>
</dd><dt id="uv-version--no-python-downloads"><a href="#uv-version--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-version--no-sources"><a href="#uv-version--no-sources"><code>--no-sources</code></a></dt><dd><p>解析依赖项时忽略 <code>tool.uv.sources</code> 表。用于针对符合标准、可发布的包元数据进行锁定，而不使用任何工作区、Git、URL 或本地路径源</p>
<p>也可以通过 <code>UV_NO_SOURCES</code> 环境变量设置。</p></dd><dt id="uv-version--no-sources-package"><a href="#uv-version--no-sources-package"><code>--no-sources-package</code></a> <i>no-sources-package</i></dt><dd><p>不为指定包使用 <code>tool.uv.sources</code> 表中的源 [env: <code>UV_NO_SOURCES_PACKAGE</code>=]</p>
</dd><dt id="uv-version--no-sync"><a href="#uv-version--no-sync"><code>--no-sync</code></a></dt><dd><p>重新锁定项目后避免同步虚拟环境 [env: UV_NO_SYNC=]</p>
</dd><dt id="uv-version--offline"><a href="#uv-version--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存的数据和本地可用的文件。</p>
</dd><dt id="uv-version--output-format"><a href="#uv-version--output-format"><code>--output-format</code></a> <i>output-format</i></dt><dd><p>输出格式</p>
<p>[default: text]</p><p>可选值：</p>
<ul>
<li><code>text</code>:  以纯文本形式显示版本</li>
<li><code>json</code>:  以 JSON 形式显示版本</li>
</ul></dd><dt id="uv-version--package"><a href="#uv-version--package"><code>--package</code></a> <i>package</i></dt><dd><p>更新工作区中特定包的版本</p>
</dd><dt id="uv-version--prerelease"><a href="#uv-version--prerelease"><code>--prerelease</code></a> <i>prerelease</i></dt><dd><p>考虑预发布版本时使用的策略。</p>
<p>默认情况下，uv 会接受<em>仅</em>发布预发布版本的包的预发布版本，以及声明说明符中包含显式预发布标记的第一方需求（<code>if-necessary-or-explicit</code>）。</p>
<p>也可以通过 <code>UV_PRERELEASE</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disallow</code>:  禁止所有预发布版本</li>
<li><code>allow</code>:  允许所有预发布版本</li>
<li><code>if-necessary</code>:  如果包的所有版本都是预发布版本，则允许预发布版本</li>
<li><code>explicit</code>:  允许版本要求中带有显式预发布标记的第一方包使用预发布版本</li>
<li><code>if-necessary-or-explicit</code>:  如果包的所有版本都是预发布版本，或者包的版本要求中带有显式预发布标记，则允许预发布版本</li>
</ul></dd><dt id="uv-version--project"><a href="#uv-version--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也将如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-version--python"><a href="#uv-version--python"><code>--python</code></a>, <code>-p</code> <i>python</i></dt><dd><p>用于解析和同步的 Python 解释器。</p>
<p>有关 Python 发现和支持的请求格式的详细信息，请参见 <a href="#uv-python">uv python</a>。</p>
<p>也可以通过 <code>UV_PYTHON</code> 环境变量设置。</p></dd><dt id="uv-version--quiet"><a href="#uv-version--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-version--refresh"><a href="#uv-version--refresh"><code>--refresh</code></a></dt><dd><p>刷新所有缓存数据</p>
</dd><dt id="uv-version--refresh-package"><a href="#uv-version--refresh-package"><code>--refresh-package</code></a> <i>refresh-package</i></dt><dd><p>刷新特定包的缓存数据</p>
</dd><dt id="uv-version--reinstall"><a href="#uv-version--reinstall"><code>--reinstall</code></a>, <code>--force-reinstall</code></dt><dd><p>重新安装所有包，无论它们是否已安装。隐含 <code>--refresh</code></p>
</dd><dt id="uv-version--reinstall-package"><a href="#uv-version--reinstall-package"><code>--reinstall-package</code></a> <i>reinstall-package</i></dt><dd><p>重新安装特定包，无论它是否已安装。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-version--resolution"><a href="#uv-version--resolution"><code>--resolution</code></a> <i>resolution</i></dt><dd><p>在给定包需求的不同兼容版本之间进行选择时使用的策略。</p>
<p>默认情况下，uv 将使用每个包的最新兼容版本（<code>highest</code>）。</p>
<p>也可以通过 <code>UV_RESOLUTION</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>highest</code>:  解析每个包的最高兼容版本</li>
<li><code>lowest</code>:  解析每个包的最低兼容版本</li>
<li><code>lowest-direct</code>:  解析任何直接依赖项的最低兼容版本，以及任何传递依赖项的最高兼容版本</li>
</ul></dd><dt id="uv-version--short"><a href="#uv-version--short"><code>--short</code></a></dt><dd><p>仅显示版本号</p>
<p>默认情况下，uv 会在版本号前显示项目名称。</p>
</dd><dt id="uv-version--system-certs"><a href="#uv-version--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，你可能希望使用平台的原生证书存储，特别是当你依赖系统证书存储中包含的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-version--upgrade"><a href="#uv-version--upgrade"><code>--upgrade</code></a>, <code>-U</code></dt><dd><p>允许包升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh</code></p>
</dd><dt id="uv-version--upgrade-group"><a href="#uv-version--upgrade-group"><code>--upgrade-group</code></a> <i>upgrade-group</i></dt><dd><p>允许依赖组中所有包的升级，忽略任何现有输出文件中的固定版本</p>
</dd><dt id="uv-version--upgrade-package"><a href="#uv-version--upgrade-package"><code>--upgrade-package</code></a>, <code>-P</code> <i>upgrade-package</i></dt><dd><p>允许特定包的升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-version--verbose"><a href="#uv-version--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>你可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>
