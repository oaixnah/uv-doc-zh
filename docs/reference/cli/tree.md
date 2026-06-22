---
title: uv tree
description: uv tree 命令的完整 CLI 参考文档，涵盖依赖树显示的所有选项，包括依赖组过滤、索引策略、Python 版本/平台过滤、反向依赖查看、预发布版本策略、链接模式等高级配置。
---

# uv tree

显示项目的依赖树。

<h3 class="cli-reference">用法</h3>

```
uv tree [OPTIONS]
```

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-tree--all-groups"><a href="#uv-tree--all-groups"><code>--all-groups</code></a></dt><dd><p>包含所有依赖组（dependency group）中的依赖。</p>
<p>可以使用 <code>--no-group</code> 来排除特定组。</p>
</dd><dt id="uv-tree--allow-insecure-host"><a href="#uv-tree--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可以多次提供。</p>
<p>接受主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统的证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您遭受中间人攻击（MITM）。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-tree--cache-dir"><a href="#uv-tree--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>默认值：macOS 和 Linux 上为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-tree--color"><a href="#uv-tree--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>：仅在输出目标是支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-tree--config-file"><a href="#uv-tree--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-tree--config-setting"><a href="#uv-tree--config-setting"><code>--config-setting</code></a>, <code>--config-settings</code>, <code>-C</code> <i>config-setting</i></dt><dd><p>传递给 PEP 517 构建后端的设置，以 <code>KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-tree--config-settings-package"><a href="#uv-tree--config-settings-package"><code>--config-settings-package</code></a>, <code>--config-settings-package</code> <i>config-settings-package</i></dt><dd><p>为特定包传递给 PEP 517 构建后端的设置，以 <code>PACKAGE:KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-tree--default-index"><a href="#uv-tree--default-index"><code>--default-index</code></a> <i>default-index</i></dt><dd><p>默认包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--index</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_DEFAULT_INDEX</code> 环境变量设置。</p></dd><dt id="uv-tree--depth"><a href="#uv-tree--depth"><code>--depth</code></a>, <code>-d</code> <i>depth</i></dt><dd><p>依赖树的最大显示深度</p>
<p>[默认值: 255]</p></dd><dt id="uv-tree--directory"><a href="#uv-tree--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 以仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-tree--exclude-newer"><a href="#uv-tree--exclude-newer"><code>--exclude-newer</code></a> <i>exclude-newer</i></dt><dd><p>将候选包限制为在给定日期之前上传的版本。</p>
<p>日期是与每个单独分发构件（即每个文件上传到包索引的时间）的上传时间进行比较，而非包版本的发布日期。</p>
<p>接受 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、基于系统配置时区解析的相同格式的本地日期（例如 <code>2006-12-02</code>）、"友好"时长（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 时长（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>时长不遵循本地时区的语义，始终以固定秒数解析，假设一天为 24 小时（例如忽略夏令时转换）。不允许使用日历单位，如月和年。</p>
<p>也可以通过 <code>UV_EXCLUDE_NEWER</code> 环境变量设置。</p></dd><dt id="uv-tree--exclude-newer-package"><a href="#uv-tree--exclude-newer-package"><code>--exclude-newer-package</code></a> <i>exclude-newer-package</i></dt><dd><p>将特定包的候选包限制为在给定日期之前上传的版本。</p>
<p>接受 <code>PACKAGE=DATE</code> 格式的包-日期对，其中 <code>DATE</code> 是 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、基于系统配置时区解析的相同格式的本地日期（例如 <code>2006-12-02</code>）、"友好"时长（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 时长（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>时长不遵循本地时区的语义，始终以固定秒数解析，假设一天为 24 小时（例如忽略夏令时转换）。不允许使用日历单位，如月和年。</p>
<p>可以多次提供以指定不同的包。</p>
</dd><dt id="uv-tree--extra-index-url"><a href="#uv-tree--extra-index-url"><code>--extra-index-url</code></a> <i>extra-index-url</i></dt><dd><p>（已弃用：改用 <code>--index</code>）除 <code>--index-url</code> 之外要使用的额外包索引 URL。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--index-url</code> 指定的索引（默认为 PyPI）。当提供多个 <code>--extra-index-url</code> 标志时，先出现的值优先级更高。</p>
<p>也可以通过 <code>UV_EXTRA_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-tree--find-links"><a href="#uv-tree--find-links"><code>--find-links</code></a>, <code>-f</code> <i>find-links</i></dt><dd><p>除注册表索引中已有的之外，搜索候选分发包的位置。</p>
<p>如果是路径，目标必须是一个目录，该目录在顶层包含作为 wheel 文件（<code>.whl</code>）或源码分发包（例如 <code>.tar.gz</code> 或 <code>.zip</code>）的包。</p>
<p>如果是 URL，页面必须包含一个符合上述格式的包文件链接的扁平列表。</p>
<p>也可以通过 <code>UV_FIND_LINKS</code> 环境变量设置。</p></dd><dt id="uv-tree--fork-strategy"><a href="#uv-tree--fork-strategy"><code>--fork-strategy</code></a> <i>fork-strategy</i></dt><dd><p>在跨 Python 版本和平台选择给定包的多个版本时使用的策略。</p>
<p>默认情况下，uv 会优化为每个支持的 Python 版本（<code>requires-python</code>）选择每个包的最新版本，同时尽量减少跨平台所选版本的数量。</p>
<p>在 <code>fewest</code> 策略下，uv 将尽量减少每个包所选版本的数量，优先选择与更广泛支持的 Python 版本或平台兼容的旧版本。</p>
<p>也可以通过 <code>UV_FORK_STRATEGY</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>fewest</code>：优化为每个包选择最少数量的版本。如果旧版本与更广泛支持的 Python 版本或平台兼容，则可能优先选择旧版本</li>
<li><code>requires-python</code>：优化为每个支持的 Python 版本选择每个包的最新支持版本</li>
</ul></dd><dt id="uv-tree--frozen"><a href="#uv-tree--frozen"><code>--frozen</code></a></dt><dd><p>在不锁定项目的情况下显示依赖要求 [env: UV_FROZEN=]</p>
<p>如果锁文件缺失，uv 将退出并报错。</p>
</dd><dt id="uv-tree--group"><a href="#uv-tree--group"><code>--group</code></a> <i>group</i></dt><dd><p>包含指定依赖组中的依赖。</p>
<p>可以多次提供。</p>
</dd><dt id="uv-tree--help"><a href="#uv-tree--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助信息</p>
</dd><dt id="uv-tree--index"><a href="#uv-tree--index"><code>--index</code></a> <i>index</i></dt><dd><p>解析依赖时使用的 URL，作为默认索引的补充。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--default-index</code> 指定的索引（默认为 PyPI）。当提供多个 <code>--index</code> 标志时，先出现的值优先级更高。</p>
<p>不支持索引名称作为值。相对路径必须使用 <code>./</code> 或 <code>../</code>（Unix）或 <code>.\\</code>、<code>..\\</code>、<code>./</code> 或 <code>../</code>（Windows）来与索引名称区分。</p>
<p>也可以通过 <code>UV_INDEX</code> 环境变量设置。</p></dd><dt id="uv-tree--index-strategy"><a href="#uv-tree--index-strategy"><code>--index-strategy</code></a> <i>index-strategy</i></dt><dd><p>针对多个索引 URL 解析时使用的策略。</p>
<p>默认情况下，uv 会在找到给定包的第一个索引处停止，并将解析限制为该第一个索引（<code>first-index</code>）上存在的版本。这可以防止"依赖混淆"（dependency confusion）攻击，即攻击者可以在替代索引上以相同名称上传恶意包。</p>
<p>也可以通过 <code>UV_INDEX_STRATEGY</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>first-index</code>：仅使用第一个返回给定包名匹配结果的索引</li>
<li><code>unsafe-first-match</code>：在所有索引中搜索每个包名，在切换到下一个索引之前耗尽第一个索引的版本</li>
<li><code>unsafe-best-match</code>：在所有索引中搜索每个包名，优先选择找到的"最佳"版本。如果一个包版本存在于多个索引中，只查看第一个索引的条目</li>
</ul></dd><dt id="uv-tree--index-url"><a href="#uv-tree--index-url"><code>--index-url</code></a>, <code>-i</code> <i>index-url</i></dt><dd><p>（已弃用：改用 <code>--default-index</code>）Python 包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--extra-index-url</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-tree--invert"><a href="#uv-tree--invert"><code>--invert</code></a>, <code>--reverse</code></dt><dd><p>显示给定包的反向依赖。此标志将反转树并显示依赖给定包的包</p>
</dd><dt id="uv-tree--keyring-provider"><a href="#uv-tree--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>尝试使用 <code>keyring</code> 进行索引 URL 的身份验证。</p>
<p>目前仅支持 <code>--keyring-provider subprocess</code>，它配置 uv 使用 <code>keyring</code> CLI 来处理身份验证。</p>
<p>默认为 <code>disabled</code>。</p>
<p>也可以通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disabled</code>：不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>：使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-tree--link-mode"><a href="#uv-tree--link-mode"><code>--link-mode</code></a> <i>link-mode</i></dt><dd><p>从全局缓存安装包时使用的方法。</p>
<p>此选项仅在构建源码分发包时使用。</p>
<p>默认值：macOS 和 Linux 上为 <code>clone</code>（也称为写时复制，Copy-on-Write），Windows 上为 <code>hardlink</code>。</p>
<p>警告：不鼓励使用 symlink 链接模式，因为它会在缓存和目标环境之间创建紧密耦合。例如，清除缓存（<code>uv cache clean</code>）将因移除底层源文件而破坏所有已安装的包。请谨慎使用符号链接。</p>
<p>也可以通过 <code>UV_LINK_MODE</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>clone</code>：从源克隆（即写时复制）包到目标位置</li>
<li><code>copy</code>：从源复制包到目标位置</li>
<li><code>hardlink</code>：从源硬链接包到目标位置</li>
<li><code>symlink</code>：从源符号链接包到目标位置</li>
</ul></dd><dt id="uv-tree--locked"><a href="#uv-tree--locked"><code>--locked</code></a></dt><dd><p>断言 <code>uv.lock</code> 将保持不变 [env: UV_LOCKED=]</p>
<p>要求锁文件是最新的。如果锁文件缺失或需要更新，uv 将退出并报错。</p>
</dd><dt id="uv-tree--managed-python"><a href="#uv-tree--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用它管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-tree--no-binary"><a href="#uv-tree--no-binary"><code>--no-binary</code></a></dt><dd><p>不安装预构建的 wheel。</p>
<p>指定的包将从源码构建并安装。解析器仍将使用预构建的 wheel 来提取包元数据（如果可用）。</p>
<p>也可以通过 <code>UV_NO_BINARY</code> 环境变量设置。</p></dd><dt id="uv-tree--no-binary-package"><a href="#uv-tree--no-binary-package"><code>--no-binary-package</code></a> <i>no-binary-package</i></dt><dd><p>不对特定包安装预构建的 wheel [env: <code>UV_NO_BINARY_PACKAGE</code>=]</p>
</dd><dt id="uv-tree--no-build"><a href="#uv-tree--no-build"><code>--no-build</code></a></dt><dd><p>不构建源码分发版。</p>
<p>启用后，解析过程不会运行任意 Python 代码。会重用已构建源码分发版的缓存 wheel，但需要构建分发版的操作将退出并报错。</p>
<p>也可以通过 <code>UV_NO_BUILD</code> 环境变量设置。</p></dd><dt id="uv-tree--no-build-isolation"><a href="#uv-tree--no-build-isolation"><code>--no-build-isolation</code></a></dt><dd><p>禁用构建源码分发版时的隔离。</p>
<p>假设 PEP 518 指定的构建依赖已安装。</p>
<p>也可以通过 <code>UV_NO_BUILD_ISOLATION</code> 环境变量设置。</p></dd><dt id="uv-tree--no-build-isolation-package"><a href="#uv-tree--no-build-isolation-package"><code>--no-build-isolation-package</code></a> <i>no-build-isolation-package</i></dt><dd><p>禁用构建特定包源码分发版时的隔离。</p>
<p>假设 PEP 518 指定的该包构建依赖已安装。</p>
</dd><dt id="uv-tree--no-build-package"><a href="#uv-tree--no-build-package"><code>--no-build-package</code></a> <i>no-build-package</i></dt><dd><p>不构建特定包的源码分发版 [env: <code>UV_NO_BUILD_PACKAGE</code>=]</p>
</dd><dt id="uv-tree--no-cache"><a href="#uv-tree--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-tree--no-config"><a href="#uv-tree--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，会在当前目录、父目录或用户配置目录中发现配置文件。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-tree--no-dedupe"><a href="#uv-tree--no-dedupe"><code>--no-dedupe</code></a></dt><dd><p>不对重复的依赖进行去重。通常，当一个包已经显示过其依赖后，再次出现不会重新显示其依赖，并会用 (*) 表示已经显示过。此标志会导致这些重复项重复显示</p>
</dd><dt id="uv-tree--no-default-groups"><a href="#uv-tree--no-default-groups"><code>--no-default-groups</code></a></dt><dd><p>忽略默认依赖组。</p>
<p>uv 默认包含 <code>tool.uv.default-groups</code> 中定义的组。此选项禁用该功能，但仍可以使用 <code>--group</code> 包含特定组。</p>
<p>也可以通过 <code>UV_NO_DEFAULT_GROUPS</code> 环境变量设置。</p></dd><dt id="uv-tree--no-dev"><a href="#uv-tree--no-dev"><code>--no-dev</code></a></dt><dd><p>禁用开发依赖组 [env: UV_NO_DEV=]</p>
<p>此选项是 <code>--no-group dev</code> 的别名。参见 <code>--no-default-groups</code> 以禁用所有默认组。</p>
</dd><dt id="uv-tree--no-group"><a href="#uv-tree--no-group"><code>--no-group</code></a> <i>no-group</i></dt><dd><p>禁用指定依赖组 [env: <code>UV_NO_GROUP</code>=]</p>
<p>此选项始终优先于默认组、<code>--all-groups</code> 和 <code>--group</code>。</p>
<p>可以多次提供。</p>
</dd><dt id="uv-tree--no-index"><a href="#uv-tree--no-index"><code>--no-index</code></a></dt><dd><p>忽略注册表索引（例如 PyPI），改为依赖直接 URL 依赖和通过 <code>--find-links</code> 提供的依赖</p>
</dd><dt id="uv-tree--no-managed-python"><a href="#uv-tree--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用使用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-tree--no-progress"><a href="#uv-tree--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如旋转加载指示器或进度条。</p>
</dd><dt id="uv-tree--no-python-downloads"><a href="#uv-tree--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-tree--no-sources"><a href="#uv-tree--no-sources"><code>--no-sources</code></a></dt><dd><p>在解析依赖时忽略 <code>tool.uv.sources</code> 表。用于根据符合标准的、可发布的包元数据进行锁定，而不是使用任何工作区、Git、URL 或本地路径源</p>
<p>也可以通过 <code>UV_NO_SOURCES</code> 环境变量设置。</p></dd><dt id="uv-tree--no-sources-package"><a href="#uv-tree--no-sources-package"><code>--no-sources-package</code></a> <i>no-sources-package</i></dt><dd><p>不对指定包使用 <code>tool.uv.sources</code> 表中的源 [env: <code>UV_NO_SOURCES_PACKAGE</code>=]</p>
</dd><dt id="uv-tree--offline"><a href="#uv-tree--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-tree--only-dev"><a href="#uv-tree--only-dev"><code>--only-dev</code></a></dt><dd><p>仅包含开发依赖组。</p>
<p>项目及其依赖将被省略。</p>
<p>此选项是 <code>--only-group dev</code> 的别名。隐含 <code>--no-default-groups</code>。</p>
</dd><dt id="uv-tree--only-group"><a href="#uv-tree--only-group"><code>--only-group</code></a> <i>only-group</i></dt><dd><p>仅包含指定依赖组中的依赖。</p>
<p>项目及其依赖将被省略。</p>
<p>可以多次提供。隐含 <code>--no-default-groups</code>。</p>
</dd><dt id="uv-tree--outdated"><a href="#uv-tree--outdated"><code>--outdated</code></a></dt><dd><p>显示树中每个包的最新可用版本</p>
</dd><dt id="uv-tree--package"><a href="#uv-tree--package"><code>--package</code></a> <i>package</i></dt><dd><p>仅显示指定的包</p>
</dd><dt id="uv-tree--prerelease"><a href="#uv-tree--prerelease"><code>--prerelease</code></a> <i>prerelease</i></dt><dd><p>考虑预发布（pre-release）版本时使用的策略。</p>
<p>默认情况下，uv 将接受<em>仅</em>发布预发布版本的包的预发布版本，以及在声明式版本说明符（specifier）中包含显式预发布标记的第一方依赖（<code>if-necessary-or-explicit</code>）。</p>
<p>也可以通过 <code>UV_PRERELEASE</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disallow</code>：禁止所有预发布版本</li>
<li><code>allow</code>：允许所有预发布版本</li>
<li><code>if-necessary</code>：如果包的所有版本都是预发布版本，则允许</li>
<li><code>explicit</code>：允许版本要求中带有显式预发布标记的第一方包的预发布版本</li>
<li><code>if-necessary-or-explicit</code>：如果包的所有版本都是预发布版本，或者包的版本要求中带有显式预发布标记，则允许</li>
</ul></dd><dt id="uv-tree--project"><a href="#uv-tree--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>通过从项目根目录向上遍历目录树，会发现所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件，以及项目的虚拟环境（<code>.venv</code>）。</p>
<p>其他命令行参数（例如相对路径）将相对于当前工作目录解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-tree--prune"><a href="#uv-tree--prune"><code>--prune</code></a> <i>prune</i></dt><dd><p>从依赖树显示中剪去给定包</p>
</dd><dt id="uv-tree--python"><a href="#uv-tree--python"><code>--python</code></a>, <code>-p</code> <i>python</i></dt><dd><p>用于锁定和过滤的 Python 解释器。</p>
<p>默认情况下，树会被过滤以匹配 Python 解释器报告的平台。使用 <code>--universal</code> 显示所有平台的树，或使用 <code>--python-version</code> 或 <code>--python-platform</code> 覆盖部分标记（marker）。</p>
<p>有关 Python 发现和支持的请求格式的详细信息，请参见 <a href="#uv-python">uv python</a>。</p>
<p>也可以通过 <code>UV_PYTHON</code> 环境变量设置。</p></dd><dt id="uv-tree--python-platform"><a href="#uv-tree--python-platform"><code>--python-platform</code></a> <i>python-platform</i></dt><dd><p>过滤树时使用的平台。</p>
<p>例如，传入 <code>--platform windows</code> 以显示在 Windows 上安装时会包含的依赖。</p>
<p>表示为"目标三元组"（target triple），即根据 CPU、厂商和操作系统名称描述目标平台的字符串，例如 <code>x86_64-unknown-linux-gnu</code> 或 <code>aarch64-apple-darwin</code>。</p>
<p>可选值：</p>
<ul>
<li><code>windows</code>：<code>x86_64-pc-windows-msvc</code> 的别名，Windows 的默认目标</li>
<li><code>linux</code>：<code>x86_64-unknown-linux-gnu</code> 的别名，Linux 的默认目标</li>
<li><code>macos</code>：<code>aarch64-apple-darwin</code> 的别名，macOS 的默认目标</li>
<li><code>x86_64-pc-windows-msvc</code>：64 位 x86 Windows 目标</li>
<li><code>aarch64-pc-windows-msvc</code>：ARM64 Windows 目标</li>
<li><code>i686-pc-windows-msvc</code>：32 位 x86 Windows 目标</li>
<li><code>x86_64-unknown-linux-gnu</code>：x86 Linux 目标。等同于 <code>x86_64-manylinux_2_28</code></li>
<li><code>aarch64-apple-darwin</code>：基于 ARM 的 macOS 目标，适用于 Apple Silicon 设备</li>
<li><code>x86_64-apple-darwin</code>：x86 macOS 目标</li>
<li><code>aarch64-unknown-linux-gnu</code>：ARM64 Linux 目标。等同于 <code>aarch64-manylinux_2_28</code></li>
<li><code>aarch64-unknown-linux-musl</code>：ARM64 Linux 目标</li>
<li><code>x86_64-unknown-linux-musl</code>：<code>x86_64</code> Linux 目标</li>
<li><code>riscv64-unknown-linux</code>：RISCV64 Linux 目标</li>
<li><code>x86_64-manylinux2014</code>：<code>x86_64</code> 目标，适用于 <code>manylinux2014</code> 平台。等同于 <code>x86_64-manylinux_2_17</code></li>
<li><code>x86_64-manylinux_2_17</code>：<code>x86_64</code> 目标，适用于 <code>manylinux_2_17</code> 平台</li>
<li><code>x86_64-manylinux_2_28</code>：<code>x86_64</code> 目标，适用于 <code>manylinux_2_28</code> 平台</li>
<li><code>x86_64-manylinux_2_31</code>：<code>x86_64</code> 目标，适用于 <code>manylinux_2_31</code> 平台</li>
<li><code>x86_64-manylinux_2_32</code>：<code>x86_64</code> 目标，适用于 <code>manylinux_2_32</code> 平台</li>
<li><code>x86_64-manylinux_2_33</code>：<code>x86_64</code> 目标，适用于 <code>manylinux_2_33</code> 平台</li>
<li><code>x86_64-manylinux_2_34</code>：<code>x86_64</code> 目标，适用于 <code>manylinux_2_34</code> 平台</li>
<li><code>x86_64-manylinux_2_35</code>：<code>x86_64</code> 目标，适用于 <code>manylinux_2_35</code> 平台</li>
<li><code>x86_64-manylinux_2_36</code>：<code>x86_64</code> 目标，适用于 <code>manylinux_2_36</code> 平台</li>
<li><code>x86_64-manylinux_2_37</code>：<code>x86_64</code> 目标，适用于 <code>manylinux_2_37</code> 平台</li>
<li><code>x86_64-manylinux_2_38</code>：<code>x86_64</code> 目标，适用于 <code>manylinux_2_38</code> 平台</li>
<li><code>x86_64-manylinux_2_39</code>：<code>x86_64</code> 目标，适用于 <code>manylinux_2_39</code> 平台</li>
<li><code>x86_64-manylinux_2_40</code>：<code>x86_64</code> 目标，适用于 <code>manylinux_2_40</code> 平台</li>
<li><code>aarch64-manylinux2014</code>：ARM64 目标，适用于 <code>manylinux2014</code> 平台。等同于 <code>aarch64-manylinux_2_17</code></li>
<li><code>aarch64-manylinux_2_17</code>：ARM64 目标，适用于 <code>manylinux_2_17</code> 平台</li>
<li><code>aarch64-manylinux_2_28</code>：ARM64 目标，适用于 <code>manylinux_2_28</code> 平台</li>
<li><code>aarch64-manylinux_2_31</code>：ARM64 目标，适用于 <code>manylinux_2_31</code> 平台</li>
<li><code>aarch64-manylinux_2_32</code>：ARM64 目标，适用于 <code>manylinux_2_32</code> 平台</li>
<li><code>aarch64-manylinux_2_33</code>：ARM64 目标，适用于 <code>manylinux_2_33</code> 平台</li>
<li><code>aarch64-manylinux_2_34</code>：ARM64 目标，适用于 <code>manylinux_2_34</code> 平台</li>
<li><code>aarch64-manylinux_2_35</code>：ARM64 目标，适用于 <code>manylinux_2_35</code> 平台</li>
<li><code>aarch64-manylinux_2_36</code>：ARM64 目标，适用于 <code>manylinux_2_36</code> 平台</li>
<li><code>aarch64-manylinux_2_37</code>：ARM64 目标，适用于 <code>manylinux_2_37</code> 平台</li>
<li><code>aarch64-manylinux_2_38</code>：ARM64 目标，适用于 <code>manylinux_2_38</code> 平台</li>
<li><code>aarch64-manylinux_2_39</code>：ARM64 目标，适用于 <code>manylinux_2_39</code> 平台</li>
<li><code>aarch64-manylinux_2_40</code>：ARM64 目标，适用于 <code>manylinux_2_40</code> 平台</li>
<li><code>aarch64-linux-android</code>：ARM64 Android 目标</li>
<li><code>x86_64-linux-android</code>：<code>x86_64</code> Android 目标</li>
<li><code>wasm32-pyodide2024</code>：使用 Pyodide 2024 平台的 wasm32 目标。适用于 Python 3.12。参见 <a href="https://pyodide.org/en/stable/development/abi/312.html">https://pyodide.org/en/stable/development/abi/312.html</a></li>
<li><code>wasm32-pyodide2025</code>：使用 Pyodide 2025 平台的 wasm32 目标。适用于 Python 3.13。参见 <a href="https://pyodide.org/en/stable/development/abi/313.html">https://pyodide.org/en/stable/development/abi/313.html</a></li>
<li><code>arm64-apple-ios</code>：ARM64 目标，适用于 iOS 设备</li>
<li><code>arm64-apple-ios-simulator</code>：ARM64 目标，适用于 iOS 模拟器</li>
<li><code>x86_64-apple-ios-simulator</code>：<code>x86_64</code> 目标，适用于 iOS 模拟器</li>
</ul></dd><dt id="uv-tree--python-version"><a href="#uv-tree--python-version"><code>--python-version</code></a> <i>python-version</i></dt><dd><p>过滤树时使用的 Python 版本。</p>
<p>例如，传入 <code>--python-version 3.10</code> 以显示在 Python 3.10 上安装时会包含的依赖。</p>
<p>默认为发现的 Python 解释器的版本。</p>
</dd><dt id="uv-tree--quiet"><a href="#uv-tree--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，在此模式下 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-tree--resolution"><a href="#uv-tree--resolution"><code>--resolution</code></a> <i>resolution</i></dt><dd><p>在给定包依赖的不同兼容版本之间进行选择时使用的策略。</p>
<p>默认情况下，uv 将使用每个包的最新兼容版本（<code>highest</code>）。</p>
<p>也可以通过 <code>UV_RESOLUTION</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>highest</code>：解析每个包的最高兼容版本</li>
<li><code>lowest</code>：解析每个包的最低兼容版本</li>
<li><code>lowest-direct</code>：解析所有直接依赖的最低兼容版本，以及所有传递依赖的最高兼容版本</li>
</ul></dd><dt id="uv-tree--script"><a href="#uv-tree--script"><code>--script</code></a> <i>script</i></dt><dd><p>显示指定 PEP 723 Python 脚本的依赖树，而不是当前项目。</p>
<p>如果提供，uv 将根据其内联元数据表解析依赖，遵循 PEP 723 规范。</p>
</dd><dt id="uv-tree--show-sizes"><a href="#uv-tree--show-sizes"><code>--show-sizes</code></a></dt><dd><p>显示树中包的压缩 wheel 大小</p>
</dd><dt id="uv-tree--system-certs"><a href="#uv-tree--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能希望使用平台的原生证书存储，特别是当您依赖系统证书存储中包含的企业信任根（例如用于强制代理）时。</p>
</dd><dt id="uv-tree--universal"><a href="#uv-tree--universal"><code>--universal</code></a></dt><dd><p>显示平台无关的依赖树。</p>
<p>显示所有 Python 版本和平台的已解析包版本，而不是过滤为与当前环境相关的版本。</p>
<p>每个包可能显示多个版本。</p>
</dd><dt id="uv-tree--upgrade"><a href="#uv-tree--upgrade"><code>--upgrade</code></a>, <code>-U</code></dt><dd><p>允许包升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh</code></p>
</dd><dt id="uv-tree--upgrade-group"><a href="#uv-tree--upgrade-group"><code>--upgrade-group</code></a> <i>upgrade-group</i></dt><dd><p>允许依赖组中所有包的升级，忽略任何现有输出文件中的固定版本</p>
</dd><dt id="uv-tree--upgrade-package"><a href="#uv-tree--upgrade-package"><code>--upgrade-package</code></a>, <code>-P</code> <i>upgrade-package</i></dt><dd><p>允许特定包的升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-tree--verbose"><a href="#uv-tree--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>
