---
title: uv check
description: uv check 命令用于对项目运行检查，默认使用 ty 对项目中的所有 Python 文件进行类型检查（type check）。本页面详细列出了该命令的全部命令行选项，包括依赖管理、缓存控制、索引策略、Python 解释器选择、构建隔离、链接模式等配置项，每个选项均附有中文说明和可用枚举值。
---

# uv check

对项目运行检查。

目前，此命令使用 ty 对 Python 代码进行类型检查（type check）。默认情况下，将检查项目中的所有 Python 文件。

<h3 class="cli-reference">用法</h3>

```
uv check [OPTIONS]
```

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-check--all-extras"><a href="#uv-check--all-extras"><code>--all-extras</code></a></dt><dd><p>包含所有可选依赖项。</p>
<p>当在 <code>tool.uv.conflicts</code> 中声明了两个或多个冲突的 extras 时，使用此标志将始终导致错误。</p>
<p>请注意，所有可选依赖项始终包含在解析过程中；此选项仅影响要安装的包的选择。</p>
</dd><dt id="uv-check--all-groups"><a href="#uv-check--all-groups"><code>--all-groups</code></a></dt><dd><p>包含所有依赖组中的依赖项。</p>
<p>可以使用 <code>--no-group</code> 排除特定组。</p>
</dd><dt id="uv-check--allow-insecure-host"><a href="#uv-check--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许到主机的非安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统的证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您面临中间人攻击（MITM）的风险。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-check--cache-dir"><a href="#uv-check--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>默认情况下，在 macOS 和 Linux 上为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-check--color"><a href="#uv-check--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测颜色支持。</p>
<p>可能的值：</p>
<ul>
<li><code>auto</code>：仅当输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-check--compile-bytecode"><a href="#uv-check--compile-bytecode"><code>--compile-bytecode</code></a>, <code>--compile</code></dt><dd><p>安装后将 Python 文件编译为字节码。</p>
<p>默认情况下，uv 不会将 Python（<code>.py</code>）文件编译为字节码（<code>__pycache__/*.pyc</code>）；而是延迟到首次导入模块时进行编译。对于启动时间至关重要的用例（如 CLI 应用程序和 Docker 容器），可以启用此选项，以较长的安装时间换取更快的启动时间。</p>
<p>启用后，uv 将处理整个 site-packages 目录（包括当前操作未修改的包）以保持一致性。与 pip 类似，它也会忽略错误。</p>
<p>也可以通过 <code>UV_COMPILE_BYTECODE</code> 环境变量设置。</p></dd><dt id="uv-check--config-file"><a href="#uv-check--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-check--config-setting"><a href="#uv-check--config-setting"><code>--config-setting</code></a>, <code>--config-settings</code>, <code>-C</code> <i>config-setting</i></dt><dd><p>传递给 PEP 517 构建后端的设置，指定为 <code>KEY=VALUE</code> 对</p>
</dd><dt id="uv-check--config-settings-package"><a href="#uv-check--config-settings-package"><code>--config-settings-package</code></a>, <code>--config-settings-package</code> <i>config-settings-package</i></dt><dd><p>传递给特定包的 PEP 517 构建后端的设置，指定为 <code>PACKAGE:KEY=VALUE</code> 对</p>
</dd><dt id="uv-check--default-index"><a href="#uv-check--default-index"><code>--default-index</code></a> <i>default-index</i></dt><dd><p>默认包索引的 URL（默认值：<a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--index</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_DEFAULT_INDEX</code> 环境变量设置。</p></dd><dt id="uv-check--directory"><a href="#uv-check--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径以给定目录为基础进行解析。</p>
<p>请参阅 <code>--project</code> 仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-check--exclude-newer"><a href="#uv-check--exclude-newer"><code>--exclude-newer</code></a> <i>exclude-newer</i></dt><dd><p>将候选包限制为在指定日期之前上传的包。</p>
<p>日期与每个单独分发包构件的上传时间进行比较（即每个文件上传到包索引的时间），而不是包版本的发布日期。</p>
<p>接受 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、基于系统配置时区解析的相同格式的本地日期（例如 <code>2006-12-02</code>）、"友好"时长（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 时长（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>时长不考虑本地时区的语义，始终解析为固定秒数，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用日历单位（如月和年）。</p>
<p>也可以通过 <code>UV_EXCLUDE_NEWER</code> 环境变量设置。</p></dd><dt id="uv-check--exclude-newer-package"><a href="#uv-check--exclude-newer-package"><code>--exclude-newer-package</code></a> <i>exclude-newer-package</i></dt><dd><p>将特定包的候选包限制为在指定日期之前上传的包。</p>
<p>接受格式为 <code>PACKAGE=DATE</code> 的包-日期对，其中 <code>DATE</code> 为 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、基于系统配置时区解析的相同格式的本地日期（例如 <code>2006-12-02</code>）、"友好"时长（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 时长（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>时长不考虑本地时区的语义，始终解析为固定秒数，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用日历单位（如月和年）。</p>
<p>可以为不同的包多次提供。</p>
</dd><dt id="uv-check--extra"><a href="#uv-check--extra"><code>--extra</code></a> <i>extra</i></dt><dd><p>包含来自指定 extra 名称的可选依赖项。</p>
<p>可以多次提供。</p>
<p>当指定的多个 extras 或组出现在 <code>tool.uv.conflicts</code> 中时，uv 将报告错误。</p>
<p>请注意，所有可选依赖项始终包含在解析过程中；此选项仅影响要安装的包的选择。</p>
</dd><dt id="uv-check--extra-index-url"><a href="#uv-check--extra-index-url"><code>--extra-index-url</code></a> <i>extra-index-url</i></dt><dd><p>（已弃用：请改用 <code>--index</code>）除 <code>--index-url</code> 之外要使用的额外包索引 URL。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--index-url</code> 指定的索引（默认值为 PyPI）。当提供多个 <code>--extra-index-url</code> 标志时，较早的值优先级更高。</p>
<p>也可以通过 <code>UV_EXTRA_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-check--find-links"><a href="#uv-check--find-links"><code>--find-links</code></a>, <code>-f</code> <i>find-links</i></dt><dd><p>除注册表索引中找到的分发包外，还要搜索候选分发包的位置。</p>
<p>如果是路径，目标必须是一个目录，其中包含顶层 wheel 文件（<code>.whl</code>）或源码分发包（例如 <code>.tar.gz</code> 或 <code>.zip</code>）。</p>
<p>如果是 URL，页面必须包含指向符合上述格式的包文件的扁平链接列表。</p>
<p>也可以通过 <code>UV_FIND_LINKS</code> 环境变量设置。</p></dd><dt id="uv-check--fork-strategy"><a href="#uv-check--fork-strategy"><code>--fork-strategy</code></a> <i>fork-strategy</i></dt><dd><p>在跨 Python 版本和平台选择给定包的多个版本时使用的策略。</p>
<p>默认情况下，uv 会优化为对每个受支持的 Python 版本（<code>requires-python</code>）选择每个包的最新版本，同时最小化跨平台选择的版本数量。</p>
<p>在 <code>fewest</code> 模式下，uv 将最小化每个包选择的版本数量，偏好与更广泛的受支持 Python 版本或平台兼容的旧版本。</p>
<p>也可以通过 <code>UV_FORK_STRATEGY</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>fewest</code>：优化为对每个包选择最少的版本数量。如果旧版本与更广泛的受支持 Python 版本或平台兼容，可能会优先选择旧版本</li>
<li><code>requires-python</code>：优化为对每个受支持的 Python 版本选择每个包的最新支持版本</li>
</ul></dd><dt id="uv-check--frozen"><a href="#uv-check--frozen"><code>--frozen</code></a></dt><dd><p>同步而不更新 <code>uv.lock</code> 文件 [env: UV_FROZEN=]</p>
<p>不检查锁文件是否是最新的，而是使用锁文件中的版本作为真实来源。如果锁文件缺失，uv 将退出并报错。如果 <code>pyproject.toml</code> 包含尚未包含在锁文件中的依赖项更改，这些更改将不会出现在环境中。</p>
</dd><dt id="uv-check--group"><a href="#uv-check--group"><code>--group</code></a> <i>group</i></dt><dd><p>包含来自指定依赖组的依赖项。</p>
<p>当指定的多个 extras 或组出现在 <code>tool.uv.conflicts</code> 中时，uv 将报告错误。</p>
<p>可以多次提供。</p>
</dd><dt id="uv-check--help"><a href="#uv-check--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助</p>
</dd><dt id="uv-check--index"><a href="#uv-check--index"><code>--index</code></a> <i>index</i></dt><dd><p>在解析依赖项时除默认索引外还要使用的 URL。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--default-index</code> 指定的索引（默认值为 PyPI）。当提供多个 <code>--index</code> 标志时，较早的值优先级更高。</p>
<p>不支持索引名称作为值。相对路径必须通过 <code>./</code> 或 <code>../</code>（在 Unix 上）或 <code>.\\</code>、<code>..\\</code>、<code>./</code> 或 <code>../</code>（在 Windows 上）来消除与索引名称的歧义。</p>
<p>也可以通过 <code>UV_INDEX</code> 环境变量设置。</p></dd><dt id="uv-check--index-strategy"><a href="#uv-check--index-strategy"><code>--index-strategy</code></a> <i>index-strategy</i></dt><dd><p>在针对多个索引 URL 解析时使用的策略。</p>
<p>默认情况下，uv 会在找到给定包的第一个索引处停止，并将解析限制为该第一个索引上存在的版本（<code>first-index</code>）。这可以防止"依赖混淆"（dependency confusion）攻击，即攻击者可以将同名的恶意包上传到备用索引。</p>
<p>也可以通过 <code>UV_INDEX_STRATEGY</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>first-index</code>：仅使用第一个返回给定包名称匹配项的索引的结果</li>
<li><code>unsafe-first-match</code>：在所有索引中搜索每个包名称，先用完第一个索引的版本，再转到下一个索引</li>
<li><code>unsafe-best-match</code>：在所有索引中搜索每个包名称，优先选择找到的"最佳"版本。如果某个包版本存在于多个索引中，仅查看第一个索引的条目</li>
</ul></dd><dt id="uv-check--index-url"><a href="#uv-check--index-url"><code>--index-url</code></a>, <code>-i</code> <i>index-url</i></dt><dd><p>（已弃用：请改用 <code>--default-index</code>）Python 包索引的 URL（默认值：<a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--extra-index-url</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-check--isolated"><a href="#uv-check--isolated"><code>--isolated</code></a></dt><dd><p>运行检查而不更改项目状态 [env: UV_ISOLATED=]</p>
<p>使用临时虚拟环境，保持现有环境和项目锁文件不变。声明的项目需求将被解析并安装到临时环境中。</p>
</dd><dt id="uv-check--keyring-provider"><a href="#uv-check--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>尝试使用 <code>keyring</code> 进行索引 URL 的身份验证。</p>
<p>目前仅支持 <code>--keyring-provider subprocess</code>，它将 uv 配置为使用 <code>keyring</code> CLI 处理身份验证。</p>
<p>默认值为 <code>disabled</code>。</p>
<p>也可以通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>disabled</code>：不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>：使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-check--link-mode"><a href="#uv-check--link-mode"><code>--link-mode</code></a> <i>link-mode</i></dt><dd><p>从全局缓存安装包时使用的方法。</p>
<p>默认情况下，在 macOS 和 Linux 上为 <code>clone</code>（也称为写时复制，Copy-on-Write），在 Windows 上为 <code>hardlink</code>（硬链接）。</p>
<p>警告：不鼓励使用 symlink（符号链接）链接模式，因为它会在缓存和目标环境之间创建紧密耦合。例如，清除缓存（<code>uv cache clean</code>）将通过移除底层源文件来破坏所有已安装的包。请谨慎使用符号链接。</p>
<p>也可以通过 <code>UV_LINK_MODE</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>clone</code>：将包从源克隆（即写时复制）到目标</li>
<li><code>copy</code>：将包从源复制到目标</li>
<li><code>hardlink</code>：将包从源硬链接到目标</li>
<li><code>symlink</code>：将包从源符号链接到目标</li>
</ul></dd><dt id="uv-check--locked"><a href="#uv-check--locked"><code>--locked</code></a></dt><dd><p>断言 <code>uv.lock</code> 将保持不变 [env: UV_LOCKED=]</p>
<p>要求锁文件是最新的。如果锁文件缺失或需要更新，uv 将退出并报错。</p>
</dd><dt id="uv-check--managed-python"><a href="#uv-check--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 偏好使用它管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-check--no-binary"><a href="#uv-check--no-binary"><code>--no-binary</code></a></dt><dd><p>不安装预构建的 wheel。</p>
<p>给定的包将从源码构建并安装。解析器仍将使用预构建的 wheel 来提取包元数据（如果可用）。</p>
<p>也可以通过 <code>UV_NO_BINARY</code> 环境变量设置。</p></dd><dt id="uv-check--no-binary-package"><a href="#uv-check--no-binary-package"><code>--no-binary-package</code></a> <i>no-binary-package</i></dt><dd><p>不为特定包安装预构建的 wheel [env: <code>UV_NO_BINARY_PACKAGE</code>=]</p>
</dd><dt id="uv-check--no-build"><a href="#uv-check--no-build"><code>--no-build</code></a></dt><dd><p>不构建源码分发包。</p>
<p>启用后，解析将不会运行任意 Python 代码。已构建的源码分发包的缓存 wheel 将被重用，但需要构建分发包的操作将退出并报错。</p>
<p>也可以通过 <code>UV_NO_BUILD</code> 环境变量设置。</p></dd><dt id="uv-check--no-build-isolation"><a href="#uv-check--no-build-isolation"><code>--no-build-isolation</code></a></dt><dd><p>在构建源码分发包时禁用隔离。</p>
<p>假设 PEP 518 指定的构建依赖项已经安装。</p>
<p>也可以通过 <code>UV_NO_BUILD_ISOLATION</code> 环境变量设置。</p></dd><dt id="uv-check--no-build-isolation-package"><a href="#uv-check--no-build-isolation-package"><code>--no-build-isolation-package</code></a> <i>no-build-isolation-package</i></dt><dd><p>在构建特定包的源码分发包时禁用隔离。</p>
<p>假设该包由 PEP 518 指定的构建依赖项已经安装。</p>
</dd><dt id="uv-check--no-build-package"><a href="#uv-check--no-build-package"><code>--no-build-package</code></a> <i>no-build-package</i></dt><dd><p>不为特定包构建源码分发包 [env: <code>UV_NO_BUILD_PACKAGE</code>=]</p>
</dd><dt id="uv-check--no-cache"><a href="#uv-check--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-check--no-config"><a href="#uv-check--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-check--no-default-groups"><a href="#uv-check--no-default-groups"><code>--no-default-groups</code></a></dt><dd><p>忽略默认依赖组。</p>
</dd><dt id="uv-check--no-dev"><a href="#uv-check--no-dev"><code>--no-dev</code></a></dt><dd><p>忽略开发依赖组。</p>
<p>项目及其依赖项将被省略。</p>
<p>此选项是 <code>--only-group dev</code> 的别名。隐含 <code>--no-default-groups</code>。</p>
</dd><dt id="uv-check--only-group"><a href="#uv-check--only-group"><code>--only-group</code></a> <i>only-group</i></dt><dd><p>仅包含来自指定依赖组的依赖项。</p>
<p>项目及其依赖项将被省略。</p>
<p>可以多次提供。隐含 <code>--no-default-groups</code>。</p>
</dd><dt id="uv-check--prerelease"><a href="#uv-check--prerelease"><code>--prerelease</code></a> <i>prerelease</i></dt><dd><p>考虑预发布版本时使用的策略。</p>
<p>默认情况下，uv 将接受<em>仅</em>发布预发布版本的包的预发布版本，以及声明版本说明符中包含显式预发布标记的第一方依赖项（<code>if-necessary-or-explicit</code>）。</p>
<p>也可以通过 <code>UV_PRERELEASE</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>disallow</code>：禁止所有预发布版本</li>
<li><code>allow</code>：允许所有预发布版本</li>
<li><code>if-necessary</code>：如果包的所有版本都是预发布版本，则允许预发布版本</li>
<li><code>explicit</code>：允许版本要求中带有显式预发布标记的第一方包的预发布版本</li>
<li><code>if-necessary-or-explicit</code>：如果包的所有版本都是预发布版本，或者包的版本要求中带有显式预发布标记，则允许预发布版本</li>
</ul></dd><dt id="uv-check--project"><a href="#uv-check--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>请参阅 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-check--python"><a href="#uv-check--python"><code>--python</code></a>, <code>-p</code> <i>python</i></dt><dd><p>用于项目环境的 Python 解释器。</p>
<p>默认情况下，使用满足项目 <code>requires-python</code> 约束的第一个解释器。</p>
<p>有关 Python 发现和请求的更多详细信息，请参见 <code>uv python</code>。</p>
<p>也可以通过 <code>UV_PYTHON</code> 环境变量设置。</p></dd><dt id="uv-check--quiet"><a href="#uv-check--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，在此模式下 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-check--refresh"><a href="#uv-check--refresh"><code>--refresh</code></a></dt><dd><p>刷新所有缓存数据</p>
</dd><dt id="uv-check--refresh-package"><a href="#uv-check--refresh-package"><code>--refresh-package</code></a> <i>refresh-package</i></dt><dd><p>刷新特定包的缓存数据</p>
</dd><dt id="uv-check--reinstall"><a href="#uv-check--reinstall"><code>--reinstall</code></a>, <code>--force-reinstall</code></dt><dd><p>重新安装所有包，无论它们是否已安装。隐含 <code>--refresh</code></p>
</dd><dt id="uv-check--reinstall-package"><a href="#uv-check--reinstall-package"><code>--reinstall-package</code></a> <i>reinstall-package</i></dt><dd><p>重新安装特定包，无论它是否已安装。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-check--resolution"><a href="#uv-check--resolution"><code>--resolution</code></a> <i>resolution</i></dt><dd><p>在给定包需求的不同兼容版本之间进行选择时使用的策略。</p>
<p>默认情况下，uv 将使用每个包的最新兼容版本（<code>highest</code>）。</p>
<p>也可以通过 <code>UV_RESOLUTION</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>highest</code>：解析每个包的最高兼容版本</li>
<li><code>lowest</code>：解析每个包的最低兼容版本</li>
<li><code>lowest-direct</code>：解析所有直接依赖项的最低兼容版本，以及所有传递依赖项的最高兼容版本</li>
</ul></dd><dt id="uv-check--script"><a href="#uv-check--script"><code>--script</code></a> <i>script</i></dt><dd><p>对指定的 PEP 723 Python 脚本运行检查，而不是对当前项目运行检查。</p>
<p>如果提供，uv 将根据脚本的内联元数据表使用依赖项，遵循 PEP 723。</p>
</dd><dt id="uv-check--system-certs"><a href="#uv-check--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能希望使用平台的原生证书存储，特别是当您依赖包含在系统证书存储中的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-check--ty-version"><a href="#uv-check--ty-version"><code>--ty-version</code></a> <i>ty-version</i></dt><dd><p>用于类型检查的 ty 版本。</p>
<p>接受版本号（例如 <code>0.0.1</code>），将被视为精确固定版本；版本说明符（例如 <code>&gt;=0.0.1</code>）；或 <code>latest</code> 以使用最新可用版本。</p>
<p>默认情况下，将使用 ty 的约束版本范围（例如 <code>&gt;=0.0,&lt;0.1</code>）。</p>
</dd><dt id="uv-check--upgrade"><a href="#uv-check--upgrade"><code>--upgrade</code></a>, <code>-U</code></dt><dd><p>允许包升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh</code></p>
</dd><dt id="uv-check--upgrade-group"><a href="#uv-check--upgrade-group"><code>--upgrade-group</code></a> <i>upgrade-group</i></dt><dd><p>允许依赖组中所有包的升级，忽略任何现有输出文件中的固定版本</p>
</dd><dt id="uv-check--upgrade-package"><a href="#uv-check--upgrade-package"><code>--upgrade-package</code></a>, <code>-P</code> <i>upgrade-package</i></dt><dd><p>允许特定包的升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-check--verbose"><a href="#uv-check--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>