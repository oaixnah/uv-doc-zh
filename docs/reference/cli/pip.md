---
title: uv pip
description: 使用与 pip 兼容的接口管理 Python 包
---

# uv pip

使用与 pip 兼容的接口管理 Python 包

<h3 class="cli-reference">Usage</h3>

```
uv pip [OPTIONS] <COMMAND>
```

<h3 class="cli-reference">Commands</h3>

<dl class="cli-reference"><dt><a href="#uv-pip-compile"><code>uv pip compile</code></a></dt><dd><p>将 <code>requirements.in</code> 文件编译为 <code>requirements.txt</code> 或 <code>pylock.toml</code> 文件</p></dd>
<dt><a href="#uv-pip-sync"><code>uv pip sync</code></a></dt><dd><p>使用 <code>requirements.txt</code> 或 <code>pylock.toml</code> 文件同步环境</p></dd>
<dt><a href="#uv-pip-install"><code>uv pip install</code></a></dt><dd><p>将包安装到环境中</p></dd>
<dt><a href="#uv-pip-uninstall"><code>uv pip uninstall</code></a></dt><dd><p>从环境中卸载包</p></dd>
<dt><a href="#uv-pip-freeze"><code>uv pip freeze</code></a></dt><dd><p>以 requirements 格式列出环境中已安装的包</p></dd>
<dt><a href="#uv-pip-list"><code>uv pip list</code></a></dt><dd><p>以表格格式列出环境中已安装的包</p></dd>
<dt><a href="#uv-pip-show"><code>uv pip show</code></a></dt><dd><p>显示一个或多个已安装包的信息</p></dd>
<dt><a href="#uv-pip-tree"><code>uv pip tree</code></a></dt><dd><p>显示环境的依赖树</p></dd>
<dt><a href="#uv-pip-check"><code>uv pip check</code></a></dt><dd><p>验证已安装的包是否具有兼容的依赖</p></dd>
</dl>

## uv pip compile

将 `requirements.in` 文件编译为 `requirements.txt` 或 `pylock.toml` 文件

<h3 class="cli-reference">Usage</h3>

```
uv pip compile [OPTIONS] <SRC_FILE|--group <GROUP>>
```

<h3 class="cli-reference">Arguments</h3>

<dl class="cli-reference"><dt id="uv-pip-compile--src_file"><a href="#uv-pip-compile--src_file"><code>SRC_FILE</code></a></dt><dd><p>包含指定文件中列出的包。</p>
<p>支持以下格式：<code>requirements.txt</code>、带有内联元数据的 <code>.py</code> 文件、<code>pylock.toml</code>、<code>pyproject.toml</code>、<code>setup.py</code> 和 <code>setup.cfg</code>。</p>
<p>如果提供的是 <code>pyproject.toml</code>、<code>setup.py</code> 或 <code>setup.cfg</code> 文件，uv 将提取相关项目的依赖要求。</p>
<p>如果提供 <code>-</code>，则从标准输入读取依赖要求。</p>
<p>requirements 文件及其中的依赖要求顺序用于确定解析过程中的优先级。</p>
</dd></dl>

<h3 class="cli-reference">Options</h3>

<dl class="cli-reference"><dt id="uv-pip-compile--all-extras"><a href="#uv-pip-compile--all-extras"><code>--all-extras</code></a></dt><dd><p>包含所有可选依赖。</p>
<p>仅适用于 <code>pyproject.toml</code>、<code>setup.py</code> 和 <code>setup.cfg</code> 源。</p>
</dd><dt id="uv-pip-compile--allow-insecure-host"><a href="#uv-pip-compile--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机的非安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（如 <code>localhost</code>）、主机-端口对（如 <code>localhost:8080</code>）或 URL（如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您面临中间人攻击（MITM）的风险。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-pip-compile--annotation-style"><a href="#uv-pip-compile--annotation-style"><code>--annotation-style</code></a> <i>annotation-style</i></dt><dd><p>输出文件中包含的注解注释的样式，用于指示每个包的来源。</p>
<p>默认为 <code>split</code>。</p>
<p>可选值：</p>
<ul>
<li><code>line</code>:  在单行中以逗号分隔渲染注解</li>
<li><code>split</code>:  每个注解独占一行渲染</li>
</ul></dd><dt id="uv-pip-compile--build-constraints"><a href="#uv-pip-compile--build-constraints"><code>--build-constraints</code></a>, <code>--build-constraint</code>, <code>-b</code> <i>build-constraints</i></dt><dd><p>构建源代码分发包时，使用给定的 requirements 文件来约束构建依赖。</p>
<p>约束文件（constraints files）是类似 <code>requirements.txt</code> 的文件，仅控制所安装依赖的<em>版本</em>。但是，在约束文件中包含某个包<em>不会</em>触发该包的安装。</p>
<p>也可以通过 <code>UV_BUILD_CONSTRAINT</code> 环境变量设置。</p></dd><dt id="uv-pip-compile--cache-dir"><a href="#uv-pip-compile--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>默认值为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>（macOS 和 Linux），以及 <code>%LOCALAPPDATA%\uv\cache</code>（Windows）。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-pip-compile--color"><a href="#uv-pip-compile--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 在写入终端时会自动检测颜色支持。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>:  仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>:  无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>:  禁用彩色输出</li>
</ul></dd><dt id="uv-pip-compile--config-file"><a href="#uv-pip-compile--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-pip-compile--config-setting"><a href="#uv-pip-compile--config-setting"><code>--config-setting</code></a>, <code>--config-settings</code>, <code>-C</code> <i>config-setting</i></dt><dd><p>传递给 PEP 517 构建后端（build backend）的设置，以 <code>KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-pip-compile--config-settings-package"><a href="#uv-pip-compile--config-settings-package"><code>--config-settings-package</code></a>, <code>--config-settings-package</code> <i>config-settings-package</i></dt><dd><p>为特定包传递给 PEP 517 构建后端（build backend）的设置，以 <code>PACKAGE:KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-pip-compile--constraints"><a href="#uv-pip-compile--constraints"><code>--constraints</code></a>, <code>--constraint</code>, <code>-c</code> <i>constraints</i></dt><dd><p>使用给定的 requirements 文件来约束版本。</p>
<p>约束文件（constraints files）是类似 <code>requirements.txt</code> 的文件，仅控制所安装依赖的<em>版本</em>。但是，在约束文件中包含某个包<em>不会</em>触发该包的安装。</p>
<p>这相当于 pip 的 <code>--constraint</code> 选项。</p>
<p>也可以通过 <code>UV_CONSTRAINT</code> 环境变量设置。</p></dd><dt id="uv-pip-compile--custom-compile-command"><a href="#uv-pip-compile--custom-compile-command"><code>--custom-compile-command</code></a> <i>custom-compile-command</i></dt><dd><p>要包含在 <code>uv pip compile</code> 生成的输出文件顶部的头部注释。</p>
<p>用于反映包装了 <code>uv pip compile</code> 的自定义构建脚本和命令。</p>
<p>也可以通过 <code>UV_CUSTOM_COMPILE_COMMAND</code> 环境变量设置。</p></dd><dt id="uv-pip-compile--default-index"><a href="#uv-pip-compile--default-index"><code>--default-index</code></a> <i>default-index</i></dt><dd><p>默认包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志指定的索引优先级低于通过 <code>--index</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_DEFAULT_INDEX</code> 环境变量设置。</p></dd><dt id="uv-pip-compile--directory"><a href="#uv-pip-compile--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径将以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-pip-compile--emit-build-options"><a href="#uv-pip-compile--emit-build-options"><code>--emit-build-options</code></a></dt><dd><p>在生成的输出文件中包含 <code>--no-binary</code> 和 <code>--only-binary</code> 条目</p>
</dd><dt id="uv-pip-compile--emit-find-links"><a href="#uv-pip-compile--emit-find-links"><code>--emit-find-links</code></a></dt><dd><p>在生成的输出文件中包含 <code>--find-links</code> 条目</p>
</dd><dt id="uv-pip-compile--emit-index-annotation"><a href="#uv-pip-compile--emit-index-annotation"><code>--emit-index-annotation</code></a></dt><dd><p>在输出文件中包含指示用于解析每个包的索引的注释注解（例如 <code># from https://pypi.org/simple</code>）</p>
</dd><dt id="uv-pip-compile--emit-index-url"><a href="#uv-pip-compile--emit-index-url"><code>--emit-index-url</code></a></dt><dd><p>在生成的输出文件中包含 <code>--index-url</code> 和 <code>--extra-index-url</code> 条目</p>
</dd><dt id="uv-pip-compile--exclude-newer"><a href="#uv-pip-compile--exclude-newer"><code>--exclude-newer</code></a> <i>exclude-newer</i></dt><dd><p>将候选包限制为在给定日期之前上传的版本。</p>
<p>日期与每个单独分发制品（distribution artifact）的上传时间（即每个文件上传到包索引的时间）进行比较，而非包版本的发布日期。</p>
<p>接受 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、相同格式的本地日期（例如 <code>2006-12-02</code>，基于系统配置的时区解析）、"友好"持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不遵循本地时区语义，始终按固定秒数计算，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月和年等日历单位。</p>
<p>也可通过 <code>UV_EXCLUDE_NEWER</code> 环境变量设置。</p></dd><dt id="uv-pip-compile--exclude-newer-package"><a href="#uv-pip-compile--exclude-newer-package"><code>--exclude-newer-package</code></a> <i>exclude-newer-package</i></dt><dd><p>将特定包的候选版本限制为在给定日期之前上传的版本。</p>
<p>接受 <code>PACKAGE=DATE</code> 格式的包-日期对，其中 <code>DATE</code> 为 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、相同格式的本地日期（例如 <code>2006-12-02</code>，基于系统配置的时区解析）、"友好"持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不遵循本地时区语义，始终按固定秒数计算，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月和年等日历单位。</p>
<p>可为不同包多次提供。</p>
</dd><dt id="uv-pip-compile--excludes"><a href="#uv-pip-compile--excludes"><code>--excludes</code></a>, <code>--exclude</code> <i>excludes</i></dt><dd><p>使用给定的 requirements 文件从解析中排除包。</p>
<p>排除文件是类似 <code>requirements.txt</code> 的文件，指定要从解析中排除的包。当包被排除时，它将完全从依赖列表中省略，并且其自身的依赖关系将在解析阶段被忽略。排除是无条件的，即忽略 requirement 版本说明符和标记（markers）；提供的文件中列出的任何包都将从所有已解析环境中省略。</p>
<p>也可通过 <code>UV_EXCLUDE</code> 环境变量设置。</p></dd><dt id="uv-pip-compile--extra"><a href="#uv-pip-compile--extra"><code>--extra</code></a> <i>extra</i></dt><dd><p>包含来自指定 extra 名称的可选依赖；可多次提供。</p>
<p>仅适用于 <code>pyproject.toml</code>、<code>setup.py</code> 和 <code>setup.cfg</code> 源。</p>
</dd><dt id="uv-pip-compile--extra-index-url"><a href="#uv-pip-compile--extra-index-url"><code>--extra-index-url</code></a> <i>extra-index-url</i></dt><dd><p>（已弃用：请改用 <code>--index</code>）除 <code>--index-url</code> 之外要使用的额外包索引 URL。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于由 <code>--index-url</code> 指定的索引（默认为 PyPI）。当提供多个 <code>--extra-index-url</code> 标志时，优先级按先后顺序递减。</p>
<p>也可通过 <code>UV_EXTRA_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-pip-compile--find-links"><a href="#uv-pip-compile--find-links"><code>--find-links</code></a>, <code>-f</code> <i>find-links</i></dt><dd><p>在注册表索引之外，搜索候选分发包的额外位置。</p>
<p>如果提供的是路径，目标必须是一个目录，其顶层包含作为 wheel 文件（<code>.whl</code>）或源代码分发包（例如 <code>.tar.gz</code> 或 <code>.zip</code>）的包。</p>
<p>如果提供的是 URL，页面必须包含一个扁平列表，其中包含符合上述格式的包文件链接。</p>
<p>也可通过 <code>UV_FIND_LINKS</code> 环境变量设置。</p></dd><dt id="uv-pip-compile--fork-strategy"><a href="#uv-pip-compile--fork-strategy"><code>--fork-strategy</code></a> <i>fork-strategy</i></dt><dd><p>在跨 Python 版本和平台选择给定包的多个版本时使用的策略。</p>
<p>默认情况下，uv 会为每个受支持的 Python 版本（<code>requires-python</code>）优化选择每个包的最新版本，同时最小化跨平台选择的版本数量。</p>
<p>在 <code>fewest</code> 策略下，uv 将最小化每个包选择的版本数量，优先选择与更广泛受支持的 Python 版本或平台兼容的旧版本。</p>
<p>也可通过 <code>UV_FORK_STRATEGY</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>fewest</code>:  优化选择每个包的最少版本数。如果旧版本与更广泛的受支持 Python 版本或平台兼容，则可能会优先选择旧版本</li>
<li><code>requires-python</code>:  优化选择每个受支持 Python 版本的每个包的最新支持版本</li>
</ul></dd><dt id="uv-pip-compile--format"><a href="#uv-pip-compile--format"><code>--format</code></a> <i>format</i></dt><dd><p>解析结果应输出的格式。</p>
<p>支持 <code>requirements.txt</code> 和 <code>pylock.toml</code>（PEP 751）两种输出格式。</p>
<p>uv 将根据输出文件的扩展名推断输出格式（如果提供了输出文件）。否则，默认为 <code>requirements.txt</code>。</p>
<p>可选值：</p>
<ul>
<li><code>requirements.txt</code>:  以 <code>requirements.txt</code> 格式导出</li>
<li><code>pylock.toml</code>:  以 <code>pylock.toml</code> 格式导出</li>
</ul></dd><dt id="uv-pip-compile--generate-hashes"><a href="#uv-pip-compile--generate-hashes"><code>--generate-hashes</code></a></dt><dd><p>在输出文件中包含分发哈希值</p>
</dd><dt id="uv-pip-compile--group"><a href="#uv-pip-compile--group"><code>--group</code></a> <i>group</i></dt><dd><p>从给定的 <code>pyproject.toml</code> 安装指定的依赖组。</p>
<p>如果未提供路径，则使用工作目录中的 <code>pyproject.toml</code>。</p>
<p>可多次提供。</p>
</dd><dt id="uv-pip-compile--help"><a href="#uv-pip-compile--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简洁帮助信息</p>
</dd><dt id="uv-pip-compile--index"><a href="#uv-pip-compile--index"><code>--index</code></a> <i>index</i></dt><dd><p>解析依赖时使用的 URL，作为默认索引的补充。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于由 <code>--default-index</code> 指定的索引（默认为 PyPI）。当提供多个 <code>--index</code> 标志时，优先级按先后顺序递减。</p>
<p>不支持将索引名称作为值。相对路径必须通过 <code>./</code> 或 <code>../</code>（Unix 上）或 <code>.\\</code>、<code>..\\</code>、<code>./</code> 或 <code>../</code>（Windows 上）与索引名称进行区分。</p>
<p>也可通过 <code>UV_INDEX</code> 环境变量设置。</p></dd><dt id="uv-pip-compile--index-strategy"><a href="#uv-pip-compile--index-strategy"><code>--index-strategy</code></a> <i>index-strategy</i></dt><dd><p>针对多个索引 URL 进行解析时使用的策略。</p>
<p>默认情况下，uv 会在第一个包含给定包的索引处停止，并将解析范围限制为在该第一个索引（<code>first-index</code>）中存在的包。这可以防止"依赖混淆"攻击，即攻击者可以在备用索引上以相同名称上传恶意包。</p>
<p>也可通过 <code>UV_INDEX_STRATEGY</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>first-index</code>:  仅使用第一个返回给定包名匹配的索引的结果</li>
<li><code>unsafe-first-match</code>:  搜索所有索引中的每个包名，在切换到下一个索引之前耗尽第一个索引的版本</li>
<li><code>unsafe-best-match</code>:  搜索所有索引中的每个包名，优先选择找到的"最佳"版本。如果一个包版本存在于多个索引中，则仅查看第一个索引的条目</li>
</ul></dd><dt id="uv-pip-compile--index-url"><a href="#uv-pip-compile--index-url"><code>--index-url</code></a>, <code>-i</code> <i>index-url</i></dt><dd><p>（已弃用：请改用 <code>--default-index</code>）Python 包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志指定的索引优先级低于通过 <code>--extra-index-url</code> 标志指定的所有其他索引。</p>
<p>也可通过 <code>UV_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-pip-compile--keyring-provider"><a href="#uv-pip-compile--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>尝试使用 <code>keyring</code> 对索引 URL 进行身份验证。</p>
<p>目前仅支持 <code>--keyring-provider subprocess</code>，该选项配置 uv 使用 <code>keyring</code> CLI 来处理身份验证。</p>
<p>默认为 <code>disabled</code>。</p>
<p>也可通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disabled</code>:  不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>:  使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-pip-compile--link-mode"><a href="#uv-pip-compile--link-mode"><code>--link-mode</code></a> <i>link-mode</i></dt><dd><p>从全局缓存安装包时使用的方法。</p>
<p>此选项仅在构建源代码分发包时使用。</p>
<p>默认在 macOS 和 Linux 上为 <code>clone</code>（也称为写时复制，Copy-on-Write），在 Windows 上为 <code>hardlink</code>。</p>
<p>警告：不建议使用 symlink 链接模式，因为它会在缓存和目标环境之间创建紧密耦合。例如，清除缓存（<code>uv cache clean</code>）将通过移除底层源文件来破坏所有已安装的包。请谨慎使用 symlink。</p>
<p>也可通过 <code>UV_LINK_MODE</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>clone</code>:  从源克隆（即写时复制）包到目标</li>
<li><code>copy</code>:  从源复制包到目标</li>
<li><code>hardlink</code>:  从源硬链接包到目标</li>
<li><code>symlink</code>:  从源符号链接包到目标</li>
</ul></dd><dt id="uv-pip-compile--managed-python"><a href="#uv-pip-compile--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果没有安装 uv 管理的 Python 版本，则会使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-pip-compile--no-annotate"><a href="#uv-pip-compile--no-annotate"><code>--no-annotate</code></a></dt><dd><p>排除指示每个包来源的注释注解</p>
</dd><dt id="uv-pip-compile--no-binary"><a href="#uv-pip-compile--no-binary"><code>--no-binary</code></a> <i>no-binary</i></dt><dd><p>不安装预构建的 wheel。</p>
<p>给定的包将从源代码构建并安装。解析器仍将使用预构建的 wheel 来提取包元数据（如果可用）。</p>
<p>可以指定多个包。使用 <code>:all:</code> 禁用所有包的二进制文件。使用 <code>:none:</code> 清除之前指定的包。</p>
</dd><dt id="uv-pip-compile--no-build"><a href="#uv-pip-compile--no-build"><code>--no-build</code></a></dt><dd><p>不构建源代码分发包。</p>
<p>启用后，解析过程将不会运行任意 Python 代码。已构建的源代码分发包的缓存 wheel 将被重用，但需要构建分发包的操作将报错退出。</p>
<p><code>--only-binary :all:</code> 的别名。</p>
</dd><dt id="uv-pip-compile--no-build-isolation"><a href="#uv-pip-compile--no-build-isolation"><code>--no-build-isolation</code></a></dt><dd><p>构建源代码分发包时禁用隔离环境。</p>
<p>假定 PEP 518 指定的构建依赖已安装。</p>
<p>也可通过 <code>UV_NO_BUILD_ISOLATION</code> 环境变量设置。</p></dd><dt id="uv-pip-compile--no-build-isolation-package"><a href="#uv-pip-compile--no-build-isolation-package"><code>--no-build-isolation-package</code></a> <i>no-build-isolation-package</i></dt><dd><p>为特定包构建源代码分发包时禁用隔离。</p>
<p>假定这些包的 PEP 518 指定的构建依赖已安装。</p>
</dd><dt id="uv-pip-compile--no-cache"><a href="#uv-pip-compile--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-pip-compile--no-deps"><a href="#uv-pip-compile--no-deps"><code>--no-deps</code></a></dt><dd><p>忽略包依赖，仅将命令行中显式列出的包添加到生成的 requirements 文件中</p>
</dd><dt id="uv-pip-compile--no-emit-package"><a href="#uv-pip-compile--no-emit-package"><code>--no-emit-package</code></a>, <code>--unsafe-package</code> <i>no-emit-package</i></dt><dd><p>指定要从输出解析结果中省略的包。其依赖仍会包含在解析结果中。等效于 pip-compile 的 <code>--unsafe-package</code> 选项</p>
</dd><dt id="uv-pip-compile--no-header"><a href="#uv-pip-compile--no-header"><code>--no-header</code></a></dt><dd><p>排除生成的输出文件顶部的注释头部</p>
</dd><dt id="uv-pip-compile--no-index"><a href="#uv-pip-compile--no-index"><code>--no-index</code></a></dt><dd><p>忽略注册表索引（例如 PyPI），转而依赖直接 URL 依赖和通过 <code>--find-links</code> 提供的依赖</p>
</dd><dt id="uv-pip-compile--no-managed-python"><a href="#uv-pip-compile--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用使用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>uv 将改为在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-pip-compile--no-progress"><a href="#uv-pip-compile--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，spinner 或进度条。</p>
</dd><dt id="uv-pip-compile--no-python-downloads"><a href="#uv-pip-compile--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用自动下载 Python。</p>
</dd><dt id="uv-pip-compile--no-sources"><a href="#uv-pip-compile--no-sources"><code>--no-sources</code></a></dt><dd><p>解析依赖时忽略 <code>tool.uv.sources</code> 表。用于基于符合标准的、可发布的包元数据进行锁定，而不是使用任何工作空间、Git、URL 或本地路径源</p>
<p>也可通过 <code>UV_NO_SOURCES</code> 环境变量设置。</p></dd><dt id="uv-pip-compile--no-sources-package"><a href="#uv-pip-compile--no-sources-package"><code>--no-sources-package</code></a> <i>no-sources-package</i></dt><dd><p>不要为指定的包使用 <code>tool.uv.sources</code> 表中的源 [env: <code>UV_NO_SOURCES_PACKAGE</code>=]</p>
</dd><dt id="uv-pip-compile--no-strip-extras"><a href="#uv-pip-compile--no-strip-extras"><code>--no-strip-extras</code></a></dt><dd><p>在输出文件中包含 extras。</p>
<p>默认情况下，uv 会去除 extras，因为由 extras 引入的任何包已经作为依赖直接包含在输出文件中。此外，使用 <code>--no-strip-extras</code> 生成的输出文件不能用作 <code>install</code> 和 <code>sync</code> 调用中的约束文件。</p>
</dd><dt id="uv-pip-compile--no-strip-markers"><a href="#uv-pip-compile--no-strip-markers"><code>--no-strip-markers</code></a></dt><dd><p>在输出文件中包含环境标记（environment markers）。</p>
<p>默认情况下，uv 会去除环境标记（environment markers），因为 <code>compile</code> 生成的解析结果仅保证对目标环境正确。</p>
</dd><dt id="uv-pip-compile--offline"><a href="#uv-pip-compile--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-pip-compile--only-binary"><a href="#uv-pip-compile--only-binary"><code>--only-binary</code></a> <i>only-binary</i></dt><dd><p>仅使用预构建的 wheel；不构建源代码分发包。</p>
<p>启用后，解析过程将不会运行来自给定包的代码。已构建的源代码分发包的缓存 wheel 将被重用，但需要构建分发包的操作将报错退出。</p>
<p>可以指定多个包。使用 <code>:all:</code> 禁用所有包的二进制文件。使用 <code>:none:</code> 清除之前指定的包。</p>
</dd><dt id="uv-pip-compile--output-file"><a href="#uv-pip-compile--output-file"><code>--output-file</code></a>, <code>-o</code> <i>output-file</i></dt><dd><p>将编译后的 requirements 写入给定的 <code>requirements.txt</code> 或 <code>pylock.toml</code> 文件。</p>
<p>如果文件已存在，则解析依赖时会优先使用现有版本，除非同时指定了 <code>--upgrade</code>。</p>
</dd><dt id="uv-pip-compile--overrides"><a href="#uv-pip-compile--overrides"><code>--overrides</code></a>, <code>--override</code> <i>overrides</i></dt><dd><p>使用给定的 requirements 文件覆盖版本。</p>
<p>覆盖文件是类似 <code>requirements.txt</code> 的文件，强制安装特定版本的 requirement，无论任何组成包声明的依赖如何，也无论这是否会被视为无效的解析结果。</p>
<p>约束是<em>附加性</em>的，即它们与组成包的 requirements 合并，而覆盖是<em>绝对性</em>的，即它们完全替换组成包的 requirements。</p>
<p>也可通过 <code>UV_OVERRIDE</code> 环境变量设置。</p></dd><dt id="uv-pip-compile--prerelease"><a href="#uv-pip-compile--prerelease"><code>--prerelease</code></a> <i>prerelease</i></dt><dd><p>考虑预发布版本时使用的策略。</p>
<p>默认情况下，uv 将接受<em>仅</em>发布预发布版本的包的预发布版本，以及声明的版本说明符中包含显式预发布标记的第一方 requirement（<code>if-necessary-or-explicit</code>）。</p>
<p>也可通过 <code>UV_PRERELEASE</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disallow</code>:  禁止所有预发布版本</li>
<li><code>allow</code>:  允许所有预发布版本</li>
<li><code>if-necessary</code>:  Allow pre-release versions if all versions of a package are pre-release</li>
<li><code>explicit</code>:  允许版本要求中带有显式预发布标记的第一方包的预发布版本</li>
<li><code>if-necessary-or-explicit</code>:  如果一个包的所有版本都是预发布版本，或者该包的版本要求中带有显式预发布标记，则允许预发布版本</li>
</ul></dd><dt id="uv-pip-compile--project"><a href="#uv-pip-compile--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-pip-compile--python"><a href="#uv-pip-compile--python"><code>--python</code></a>, <code>-p</code> <i>python</i></dt><dd><p>解析过程中使用的 Python 解释器。</p>
<p>需要 Python 解释器来构建源代码分发包，以在没有 wheel 时确定包元数据。</p>
<p>解释器还用于确定默认的最低 Python 版本，除非提供了 <code>--python-version</code>。</p>
<p>此选项遵循 <code>UV_PYTHON</code>，但当通过环境变量设置时，会被 <code>--python-version</code> 覆盖。</p>
<p>参见 <a href="#uv-python">uv python</a> 了解 Python 发现机制和支持的请求格式的详细信息。</p>
</dd><dt id="uv-pip-compile--python-platform"><a href="#uv-pip-compile--python-platform"><code>--python-platform</code></a> <i>python-platform</i></dt><dd><p>要为其解析 requirements 的平台。</p>
<p>表示为"目标三元组"（target triple），一个描述目标平台的字符串，包含 CPU、供应商和操作系统名称，如 <code>x86_64-unknown-linux-gnu</code> 或 <code>aarch64-apple-darwin</code>。</p>
<p>当目标为 macOS（Darwin）时，默认最低版本为 <code>13.0</code>。使用 <code>MACOSX_DEPLOYMENT_TARGET</code> 指定不同的最低版本，例如 <code>14.0</code>。</p>
<p>当目标为 iOS 时，默认最低版本为 <code>13.0</code>。使用 <code>IPHONEOS_DEPLOYMENT_TARGET</code> 指定不同的最低版本，例如 <code>14.0</code>。</p>
<p>当目标为 Android 时，默认最低 Android API 级别为 <code>24</code>。使用 <code>ANDROID_API_LEVEL</code> 指定不同的最低版本，例如 <code>26</code>。</p>
<p>可选值：</p>
<ul>
<li><code>windows</code>:  <code>x86_64-pc-windows-msvc</code> 的别名，Windows 的默认目标</li>
<li><code>linux</code>:  <code>x86_64-unknown-linux-gnu</code> 的别名，Linux 的默认目标</li>
<li><code>macos</code>:  <code>aarch64-apple-darwin</code> 的别名，macOS 的默认目标</li>
<li><code>x86_64-pc-windows-msvc</code>:  64 位 x86 Windows 目标</li>
<li><code>aarch64-pc-windows-msvc</code>:  ARM64 Windows 目标</li>
<li><code>i686-pc-windows-msvc</code>:  32 位 x86 Windows 目标</li>
<li><code>x86_64-unknown-linux-gnu</code>:  x86 Linux 目标。等效于 <code>x86_64-manylinux_2_28</code></li>
<li><code>aarch64-apple-darwin</code>:  基于 ARM 的 macOS 目标，如 Apple Silicon 设备上所见</li>
<li><code>x86_64-apple-darwin</code>:  x86 macOS 目标</li>
<li><code>aarch64-unknown-linux-gnu</code>:  ARM64 Linux 目标。等效于 <code>aarch64-manylinux_2_28</code></li>
<li><code>aarch64-unknown-linux-musl</code>:  ARM64 Linux 目标</li>
<li><code>x86_64-unknown-linux-musl</code>:  <code>x86_64</code> Linux 目标</li>
<li><code>riscv64-unknown-linux</code>:  RISCV64 Linux 目标</li>
<li><code>x86_64-manylinux2014</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux2014</code> 平台。等效于 <code>x86_64-manylinux_2_17</code></li>
<li><code>x86_64-manylinux_2_17</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_17</code> 平台</li>
<li><code>x86_64-manylinux_2_28</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_28</code> 平台</li>
<li><code>x86_64-manylinux_2_31</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_31</code> 平台</li>
<li><code>x86_64-manylinux_2_32</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_32</code> 平台</li>
<li><code>x86_64-manylinux_2_33</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_33</code> 平台</li>
<li><code>x86_64-manylinux_2_34</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_34</code> 平台</li>
<li><code>x86_64-manylinux_2_35</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_35</code> 平台</li>
<li><code>x86_64-manylinux_2_36</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_36</code> 平台</li>
<li><code>x86_64-manylinux_2_37</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_37</code> 平台</li>
<li><code>x86_64-manylinux_2_38</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_38</code> 平台</li>
<li><code>x86_64-manylinux_2_39</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_39</code> 平台</li>
<li><code>x86_64-manylinux_2_40</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_40</code> 平台</li>
<li><code>aarch64-manylinux2014</code>:  ARM64 目标，适用于 <code>manylinux2014</code> 平台。等效于 <code>aarch64-manylinux_2_17</code></li>
<li><code>aarch64-manylinux_2_17</code>:  ARM64 目标，适用于 <code>manylinux_2_17</code> 平台</li>
<li><code>aarch64-manylinux_2_28</code>:  ARM64 目标，适用于 <code>manylinux_2_28</code> 平台</li>
<li><code>aarch64-manylinux_2_31</code>:  ARM64 目标，适用于 <code>manylinux_2_31</code> 平台</li>
<li><code>aarch64-manylinux_2_32</code>:  ARM64 目标，适用于 <code>manylinux_2_32</code> 平台</li>
<li><code>aarch64-manylinux_2_33</code>:  ARM64 目标，适用于 <code>manylinux_2_33</code> 平台</li>
<li><code>aarch64-manylinux_2_34</code>:  ARM64 目标，适用于 <code>manylinux_2_34</code> 平台</li>
<li><code>aarch64-manylinux_2_35</code>:  ARM64 目标，适用于 <code>manylinux_2_35</code> 平台</li>
<li><code>aarch64-manylinux_2_36</code>:  ARM64 目标，适用于 <code>manylinux_2_36</code> 平台</li>
<li><code>aarch64-manylinux_2_37</code>:  ARM64 目标，适用于 <code>manylinux_2_37</code> 平台</li>
<li><code>aarch64-manylinux_2_38</code>:  ARM64 目标，适用于 <code>manylinux_2_38</code> 平台</li>
<li><code>aarch64-manylinux_2_39</code>:  ARM64 目标，适用于 <code>manylinux_2_39</code> 平台</li>
<li><code>aarch64-manylinux_2_40</code>:  ARM64 目标，适用于 <code>manylinux_2_40</code> 平台</li>
<li><code>aarch64-linux-android</code>:  ARM64 Android 目标</li>
<li><code>x86_64-linux-android</code>:  <code>x86_64</code> Android 目标</li>
<li><code>wasm32-pyodide2024</code>:  wasm32 目标，使用 Pyodide 2024 平台。适用于 Python 3.12。参见 <a href="https://pyodide.org/en/stable/development/abi/312.html">https://pyodide.org/en/stable/development/abi/312.html</a></li>
<li><code>wasm32-pyodide2025</code>:  wasm32 目标，使用 Pyodide 2025 平台。适用于 Python 3.13。参见 <a href="https://pyodide.org/en/stable/development/abi/313.html">https://pyodide.org/en/stable/development/abi/313.html</a></li>
<li><code>arm64-apple-ios</code>:  iOS 设备的 ARM64 目标</li>
<li><code>arm64-apple-ios-simulator</code>:  iOS 模拟器的 ARM64 目标</li>
<li><code>x86_64-apple-ios-simulator</code>:  iOS 模拟器的 <code>x86_64</code> 目标</li>
</ul></dd><dt id="uv-pip-compile--python-version"><a href="#uv-pip-compile--python-version"><code>--python-version</code></a> <i>python-version</i></dt><dd><p>用于解析的 Python 版本。</p>
<p>例如，<code>3.8</code> 或 <code>3.8.17</code>。</p>
<p>默认为用于解析的 Python 解释器版本。</p>
<p>定义已解析的 requirements 必须支持的最低 Python 版本。</p>
<p>如果省略了补丁版本，则假定最低补丁版本。例如，<code>3.8</code> 映射为 <code>3.8.0</code>。</p>
</dd><dt id="uv-pip-compile--quiet"><a href="#uv-pip-compile--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项（如 <code>-qq</code>）将启用静默模式，uv 将不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-pip-compile--refresh"><a href="#uv-pip-compile--refresh"><code>--refresh</code></a></dt><dd><p>刷新所有缓存数据</p>
</dd><dt id="uv-pip-compile--refresh-package"><a href="#uv-pip-compile--refresh-package"><code>--refresh-package</code></a> <i>refresh-package</i></dt><dd><p>刷新特定包的缓存数据</p>
</dd><dt id="uv-pip-compile--resolution"><a href="#uv-pip-compile--resolution"><code>--resolution</code></a> <i>resolution</i></dt><dd><p>在给定包需求的不同兼容版本之间进行选择时使用的策略。</p>
<p>默认情况下，uv 会使用每个包的最新兼容版本（<code>highest</code>）。</p>
<p>也可通过 <code>UV_RESOLUTION</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>highest</code>:  解析每个包的最高兼容版本</li>
<li><code>lowest</code>:  解析每个包的最低兼容版本</li>
<li><code>lowest-direct</code>:  解析所有直接依赖的最低兼容版本，以及所有传递依赖的最高兼容版本</li>
</ul></dd><dt id="uv-pip-compile--system"><a href="#uv-pip-compile--system"><code>--system</code></a></dt><dd><p>将包安装到系统 Python 环境中。</p>
<p>默认情况下，uv 使用当前工作目录或任何父目录中的虚拟环境，回退到在 <code>PATH</code> 中搜索 Python 可执行文件。<code>--system</code> 选项指示 uv 避免使用虚拟环境中的 Python，并将搜索范围限制为系统路径。</p>
<p>也可通过 <code>UV_SYSTEM_PYTHON</code> 环境变量设置。</p></dd><dt id="uv-pip-compile--system-certs"><a href="#uv-pip-compile--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能需要使用平台的原生证书存储，特别是当您依赖系统证书存储中包含的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-pip-compile--torch-backend"><a href="#uv-pip-compile--torch-backend"><code>--torch-backend</code></a> <i>torch-backend</i></dt><dd><p>获取 PyTorch 生态系统中软件包时使用的后端（例如，<code>cpu</code>、<code>cu126</code> 或 <code>auto</code>）。</p>
<p>设置后，uv 将忽略为 PyTorch 生态系统中的包配置的索引 URL，而改用定义的后端。</p>
<p>For example, when set to <code>cpu</code>, uv will use the CPU-only PyTorch index; when set to <code>cu126</code>, uv will use the PyTorch index for CUDA 12.6.</p>
<p><code>auto</code> 模式将尝试根据当前安装的 CUDA 驱动程序检测适当的 PyTorch 索引。</p>
<p>此选项为预览功能，可能在未来的任何版本中发生变化。</p>
<p>May also be set with the <code>UV_TORCH_BACKEND</code> environment variable.</p><p>可选值：</p>
<ul>
<li><code>auto</code>:  Select the appropriate PyTorch index based on the operating system and CUDA driver version</li>
<li><code>cpu</code>:  Use the CPU-only PyTorch index</li>
<li><code>cu130</code>:  Use the PyTorch index for CUDA 13.0</li>
<li><code>cu129</code>:  Use the PyTorch index for CUDA 12.9</li>
<li><code>cu128</code>:  Use the PyTorch index for CUDA 12.8</li>
<li><code>cu126</code>:  Use the PyTorch index for CUDA 12.6</li>
<li><code>cu125</code>:  Use the PyTorch index for CUDA 12.5</li>
<li><code>cu124</code>:  Use the PyTorch index for CUDA 12.4</li>
<li><code>cu123</code>:  Use the PyTorch index for CUDA 12.3</li>
<li><code>cu122</code>:  Use the PyTorch index for CUDA 12.2</li>
<li><code>cu121</code>:  Use the PyTorch index for CUDA 12.1</li>
<li><code>cu120</code>:  Use the PyTorch index for CUDA 12.0</li>
<li><code>cu118</code>:  Use the PyTorch index for CUDA 11.8</li>
<li><code>cu117</code>:  Use the PyTorch index for CUDA 11.7</li>
<li><code>cu116</code>:  Use the PyTorch index for CUDA 11.6</li>
<li><code>cu115</code>:  Use the PyTorch index for CUDA 11.5</li>
<li><code>cu114</code>:  Use the PyTorch index for CUDA 11.4</li>
<li><code>cu113</code>:  Use the PyTorch index for CUDA 11.3</li>
<li><code>cu112</code>:  Use the PyTorch index for CUDA 11.2</li>
<li><code>cu111</code>:  Use the PyTorch index for CUDA 11.1</li>
<li><code>cu110</code>:  Use the PyTorch index for CUDA 11.0</li>
<li><code>cu102</code>:  Use the PyTorch index for CUDA 10.2</li>
<li><code>cu101</code>:  Use the PyTorch index for CUDA 10.1</li>
<li><code>cu100</code>:  Use the PyTorch index for CUDA 10.0</li>
<li><code>cu92</code>:  Use the PyTorch index for CUDA 9.2</li>
<li><code>cu91</code>:  Use the PyTorch index for CUDA 9.1</li>
<li><code>cu90</code>:  Use the PyTorch index for CUDA 9.0</li>
<li><code>cu80</code>:  Use the PyTorch index for CUDA 8.0</li>
<li><code>rocm7.2</code>:  Use the PyTorch index for ROCm 7.2</li>
<li><code>rocm7.1</code>:  Use the PyTorch index for ROCm 7.1</li>
<li><code>rocm7.0</code>:  Use the PyTorch index for ROCm 7.0</li>
<li><code>rocm6.4</code>:  Use the PyTorch index for ROCm 6.4</li>
<li><code>rocm6.3</code>:  Use the PyTorch index for ROCm 6.3</li>
<li><code>rocm6.2.4</code>:  Use the PyTorch index for ROCm 6.2.4</li>
<li><code>rocm6.2</code>:  Use the PyTorch index for ROCm 6.2</li>
<li><code>rocm6.1</code>:  Use the PyTorch index for ROCm 6.1</li>
<li><code>rocm6.0</code>:  Use the PyTorch index for ROCm 6.0</li>
<li><code>rocm5.7</code>:  Use the PyTorch index for ROCm 5.7</li>
<li><code>rocm5.6</code>:  Use the PyTorch index for ROCm 5.6</li>
<li><code>rocm5.5</code>:  Use the PyTorch index for ROCm 5.5</li>
<li><code>rocm5.4.2</code>:  Use the PyTorch index for ROCm 5.4.2</li>
<li><code>rocm5.4</code>:  Use the PyTorch index for ROCm 5.4</li>
<li><code>rocm5.3</code>:  Use the PyTorch index for ROCm 5.3</li>
<li><code>rocm5.2</code>:  Use the PyTorch index for ROCm 5.2</li>
<li><code>rocm5.1.1</code>:  Use the PyTorch index for ROCm 5.1.1</li>
<li><code>rocm4.2</code>:  Use the PyTorch index for ROCm 4.2</li>
<li><code>rocm4.1</code>:  Use the PyTorch index for ROCm 4.1</li>
<li><code>rocm4.0.1</code>:  Use the PyTorch index for ROCm 4.0.1</li>
<li><code>xpu</code>:  Use the PyTorch index for Intel XPU</li>
</ul></dd><dt id="uv-pip-compile--universal"><a href="#uv-pip-compile--universal"><code>--universal</code></a></dt><dd><p>Perform a universal resolution, attempting to generate a single <code>requirements.txt</code> output file that is compatible with all operating systems, architectures, and Python implementations.</p>
<p>在通用模式下，当前 Python 版本（或用户提供的 <code>--python-version</code>）将被视为下限。例如，<code>--universal --python-version 3.7</code> 将为 Python 3.7 及更高版本生成通用解析结果。</p>
<p>隐含 <code>--no-strip-markers</code>。</p>
</dd><dt id="uv-pip-compile--upgrade"><a href="#uv-pip-compile--upgrade"><code>--upgrade</code></a>, <code>-U</code></dt><dd><p>允许包升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh</code></p>
</dd><dt id="uv-pip-compile--upgrade-group"><a href="#uv-pip-compile--upgrade-group"><code>--upgrade-group</code></a> <i>upgrade-group</i></dt><dd><p>Allow upgrades for all packages in a dependency group, ignoring pinned versions in any existing output file</p>
</dd><dt id="uv-pip-compile--upgrade-package"><a href="#uv-pip-compile--upgrade-package"><code>--upgrade-package</code></a>, <code>-P</code> <i>upgrade-package</i></dt><dd><p>允许特定包的升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-pip-compile--verbose"><a href="#uv-pip-compile--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>

## uv pip sync

使用 `requirements.txt` 或 `pylock.toml` 文件同步环境。

同步环境时，任何未在 `requirements.txt` 或 `pylock.toml` 文件中列出的包都将被移除。要保留额外包，请改用 `uv pip install`。

输入文件假定为 `pip compile` 或 `uv export` 操作的输出，其中包含所有传递依赖。如果文件中不存在传递依赖，则不会安装它们。使用 `--strict` 可在任何传递依赖缺失时发出警告。

<h3 class="cli-reference">Usage</h3>

```
uv pip sync [OPTIONS] <SRC_FILE>...
```

<h3 class="cli-reference">Arguments</h3>

<dl class="cli-reference"><dt id="uv-pip-sync--src_file"><a href="#uv-pip-sync--src_file"><code>SRC_FILE</code></a></dt><dd><p>Include the packages listed in the given files.</p>
<p>支持以下格式：<code>requirements.txt</code>、包含内联元数据的 <code>.py</code> 文件、<code>pylock.toml</code>、<code>pyproject.toml</code>、<code>setup.py</code> 和 <code>setup.cfg</code>。</p>
<p>如果提供了 <code>pyproject.toml</code>、<code>setup.py</code> 或 <code>setup.cfg</code> 文件，uv 将提取相关项目的 requirements。</p>
<p>If <code>-</code> is provided, then requirements will be read from stdin.</p>
</dd></dl>

<h3 class="cli-reference">Options</h3>

<dl class="cli-reference"><dt id="uv-pip-sync--all-extras"><a href="#uv-pip-sync--all-extras"><code>--all-extras</code></a></dt><dd><p>包含所有可选依赖。</p>
<p>仅适用于 <code>pylock.toml</code>、<code>pyproject.toml</code>、<code>setup.py</code> 和 <code>setup.cfg</code> 源。</p>
</dd><dt id="uv-pip-sync--allow-empty-requirements"><a href="#uv-pip-sync--allow-empty-requirements"><code>--allow-empty-requirements</code></a></dt><dd><p>Allow sync of empty requirements, which will clear the environment of all packages</p>
</dd><dt id="uv-pip-sync--allow-insecure-host"><a href="#uv-pip-sync--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机的非安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（如 <code>localhost</code>）、主机-端口对（如 <code>localhost:8080</code>）或 URL（如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您面临中间人攻击（MITM）的风险。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-pip-sync--break-system-packages"><a href="#uv-pip-sync--break-system-packages"><code>--break-system-packages</code></a></dt><dd><p>允许 uv 修改 <code>EXTERNALLY-MANAGED</code> 的 Python 安装。</p>
<p>警告：<code>--break-system-packages</code> 旨在用于持续集成（CI）环境中，当安装到由外部包管理器（如 <code>apt</code>）管理的 Python 安装中时。应谨慎使用，因为此类 Python 安装明确建议不要由其他包管理器（如 uv 或 <code>pip</code>）进行修改。</p>
<p>也可通过 <code>UV_BREAK_SYSTEM_PACKAGES</code> 环境变量设置。</p></dd><dt id="uv-pip-sync--build-constraints"><a href="#uv-pip-sync--build-constraints"><code>--build-constraints</code></a>, <code>--build-constraint</code>, <code>-b</code> <i>build-constraints</i></dt><dd><p>构建源代码分发包时，使用给定的 requirements 文件来约束构建依赖。</p>
<p>约束文件（constraints files）是类似 <code>requirements.txt</code> 的文件，仅控制所安装依赖的<em>版本</em>。但是，在约束文件中包含某个包<em>不会</em>触发该包的安装。</p>
<p>也可以通过 <code>UV_BUILD_CONSTRAINT</code> 环境变量设置。</p></dd><dt id="uv-pip-sync--cache-dir"><a href="#uv-pip-sync--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>默认值为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>（macOS 和 Linux），以及 <code>%LOCALAPPDATA%\uv\cache</code>（Windows）。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-pip-sync--color"><a href="#uv-pip-sync--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 在写入终端时会自动检测颜色支持。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>:  仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>:  无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>:  禁用彩色输出</li>
</ul></dd><dt id="uv-pip-sync--compile-bytecode"><a href="#uv-pip-sync--compile-bytecode"><code>--compile-bytecode</code></a>, <code>--compile</code></dt><dd><p>安装后编译 Python 文件为字节码。</p>
<p>默认情况下，uv 不会将 Python（<code>.py</code>）文件编译为字节码（<code>__pycache__/*.pyc</code>）；而是在首次导入模块时延迟编译。对于启动时间至关重要的用例，例如 CLI 应用程序和 Docker 容器，可以启用此选项，以较长的安装时间换取更快的启动时间。</p>
<p>启用后，uv 将处理整个 site-packages 目录（包括当前操作未修改的包）以保持一致性。与 pip 一样，它也会忽略错误。</p>
<p>也可通过 <code>UV_COMPILE_BYTECODE</code> 环境变量设置。</p></dd><dt id="uv-pip-sync--config-file"><a href="#uv-pip-sync--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-pip-sync--config-setting"><a href="#uv-pip-sync--config-setting"><code>--config-setting</code></a>, <code>--config-settings</code>, <code>-C</code> <i>config-setting</i></dt><dd><p>传递给 PEP 517 构建后端（build backend）的设置，以 <code>KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-pip-sync--config-settings-package"><a href="#uv-pip-sync--config-settings-package"><code>--config-settings-package</code></a>, <code>--config-settings-package</code> <i>config-settings-package</i></dt><dd><p>为特定包传递给 PEP 517 构建后端（build backend）的设置，以 <code>PACKAGE:KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-pip-sync--constraints"><a href="#uv-pip-sync--constraints"><code>--constraints</code></a>, <code>--constraint</code>, <code>-c</code> <i>constraints</i></dt><dd><p>使用给定的 requirements 文件来约束版本。</p>
<p>约束文件（constraints files）是类似 <code>requirements.txt</code> 的文件，仅控制所安装依赖的<em>版本</em>。但是，在约束文件中包含某个包<em>不会</em>触发该包的安装。</p>
<p>这相当于 pip 的 <code>--constraint</code> 选项。</p>
<p>也可以通过 <code>UV_CONSTRAINT</code> 环境变量设置。</p></dd><dt id="uv-pip-sync--default-index"><a href="#uv-pip-sync--default-index"><code>--default-index</code></a> <i>default-index</i></dt><dd><p>默认包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志指定的索引优先级低于通过 <code>--index</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_DEFAULT_INDEX</code> 环境变量设置。</p></dd><dt id="uv-pip-sync--directory"><a href="#uv-pip-sync--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径将以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-pip-sync--dry-run"><a href="#uv-pip-sync--dry-run"><code>--dry-run</code></a></dt><dd><p>执行预演（dry run），即不实际安装任何内容，仅解析依赖并打印结果计划</p>
</dd><dt id="uv-pip-sync--exclude-newer"><a href="#uv-pip-sync--exclude-newer"><code>--exclude-newer</code></a> <i>exclude-newer</i></dt><dd><p>将候选包限制为在给定日期之前上传的版本。</p>
<p>日期与每个单独分发制品（distribution artifact）的上传时间（即每个文件上传到包索引的时间）进行比较，而非包版本的发布日期。</p>
<p>接受 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、相同格式的本地日期（例如 <code>2006-12-02</code>，基于系统配置的时区解析）、"友好"持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不遵循本地时区语义，始终按固定秒数计算，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月和年等日历单位。</p>
<p>也可通过 <code>UV_EXCLUDE_NEWER</code> 环境变量设置。</p></dd><dt id="uv-pip-sync--exclude-newer-package"><a href="#uv-pip-sync--exclude-newer-package"><code>--exclude-newer-package</code></a> <i>exclude-newer-package</i></dt><dd><p>将特定包的候选版本限制为在给定日期之前上传的版本。</p>
<p>接受 <code>PACKAGE=DATE</code> 格式的包-日期对，其中 <code>DATE</code> 为 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、相同格式的本地日期（例如 <code>2006-12-02</code>，基于系统配置的时区解析）、"友好"持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不遵循本地时区语义，始终按固定秒数计算，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月和年等日历单位。</p>
<p>可为不同包多次提供。</p>
</dd><dt id="uv-pip-sync--extra"><a href="#uv-pip-sync--extra"><code>--extra</code></a> <i>extra</i></dt><dd><p>包含来自指定 extra 名称的可选依赖；可多次提供。</p>
<p>仅适用于 <code>pylock.toml</code>、<code>pyproject.toml</code>、<code>setup.py</code> 和 <code>setup.cfg</code> 源。</p>
</dd><dt id="uv-pip-sync--extra-index-url"><a href="#uv-pip-sync--extra-index-url"><code>--extra-index-url</code></a> <i>extra-index-url</i></dt><dd><p>（已弃用：请改用 <code>--index</code>）除 <code>--index-url</code> 之外要使用的额外包索引 URL。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于由 <code>--index-url</code> 指定的索引（默认为 PyPI）。当提供多个 <code>--extra-index-url</code> 标志时，优先级按先后顺序递减。</p>
<p>也可通过 <code>UV_EXTRA_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-pip-sync--find-links"><a href="#uv-pip-sync--find-links"><code>--find-links</code></a>, <code>-f</code> <i>find-links</i></dt><dd><p>在注册表索引之外，搜索候选分发包的额外位置。</p>
<p>如果提供的是路径，目标必须是一个目录，其顶层包含作为 wheel 文件（<code>.whl</code>）或源代码分发包（例如 <code>.tar.gz</code> 或 <code>.zip</code>）的包。</p>
<p>如果提供的是 URL，页面必须包含一个扁平列表，其中包含符合上述格式的包文件链接。</p>
<p>也可通过 <code>UV_FIND_LINKS</code> 环境变量设置。</p></dd><dt id="uv-pip-sync--group"><a href="#uv-pip-sync--group"><code>--group</code></a> <i>group</i></dt><dd><p>从给定的 <code>pylock.toml</code> 或 <code>pyproject.toml</code> 安装指定的依赖组。</p>
<p>如果未提供路径，则使用工作目录中的 <code>pylock.toml</code> 或 <code>pyproject.toml</code>。</p>
<p>可多次提供。</p>
</dd><dt id="uv-pip-sync--help"><a href="#uv-pip-sync--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简洁帮助信息</p>
</dd><dt id="uv-pip-sync--index"><a href="#uv-pip-sync--index"><code>--index</code></a> <i>index</i></dt><dd><p>解析依赖时使用的 URL，作为默认索引的补充。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于由 <code>--default-index</code> 指定的索引（默认为 PyPI）。当提供多个 <code>--index</code> 标志时，优先级按先后顺序递减。</p>
<p>不支持将索引名称作为值。相对路径必须通过 <code>./</code> 或 <code>../</code>（Unix 上）或 <code>.\\</code>、<code>..\\</code>、<code>./</code> 或 <code>../</code>（Windows 上）与索引名称进行区分。</p>
<p>也可通过 <code>UV_INDEX</code> 环境变量设置。</p></dd><dt id="uv-pip-sync--index-strategy"><a href="#uv-pip-sync--index-strategy"><code>--index-strategy</code></a> <i>index-strategy</i></dt><dd><p>针对多个索引 URL 进行解析时使用的策略。</p>
<p>默认情况下，uv 会在第一个包含给定包的索引处停止，并将解析范围限制为在该第一个索引（<code>first-index</code>）中存在的包。这可以防止"依赖混淆"攻击，即攻击者可以在备用索引上以相同名称上传恶意包。</p>
<p>也可通过 <code>UV_INDEX_STRATEGY</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>first-index</code>:  仅使用第一个返回给定包名匹配的索引的结果</li>
<li><code>unsafe-first-match</code>:  搜索所有索引中的每个包名，在切换到下一个索引之前耗尽第一个索引的版本</li>
<li><code>unsafe-best-match</code>:  搜索所有索引中的每个包名，优先选择找到的"最佳"版本。如果一个包版本存在于多个索引中，则仅查看第一个索引的条目</li>
</ul></dd><dt id="uv-pip-sync--index-url"><a href="#uv-pip-sync--index-url"><code>--index-url</code></a>, <code>-i</code> <i>index-url</i></dt><dd><p>（已弃用：请改用 <code>--default-index</code>）Python 包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志指定的索引优先级低于通过 <code>--extra-index-url</code> 标志指定的所有其他索引。</p>
<p>也可通过 <code>UV_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-pip-sync--keyring-provider"><a href="#uv-pip-sync--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>尝试使用 <code>keyring</code> 对索引 URL 进行身份验证。</p>
<p>目前仅支持 <code>--keyring-provider subprocess</code>，该选项配置 uv 使用 <code>keyring</code> CLI 来处理身份验证。</p>
<p>默认为 <code>disabled</code>。</p>
<p>也可通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disabled</code>:  不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>:  使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-pip-sync--link-mode"><a href="#uv-pip-sync--link-mode"><code>--link-mode</code></a> <i>link-mode</i></dt><dd><p>从全局缓存安装包时使用的方法。</p>
<p>默认在 macOS 和 Linux 上为 <code>clone</code>（也称为写时复制，Copy-on-Write），在 Windows 上为 <code>hardlink</code>。</p>
<p>警告：不建议使用 symlink 链接模式，因为它会在缓存和目标环境之间创建紧密耦合。例如，清除缓存（<code>uv cache clean</code>）将通过移除底层源文件来破坏所有已安装的包。请谨慎使用 symlink。</p>
<p>也可通过 <code>UV_LINK_MODE</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>clone</code>:  从源克隆（即写时复制）包到目标</li>
<li><code>copy</code>:  从源复制包到目标</li>
<li><code>hardlink</code>:  从源硬链接包到目标</li>
<li><code>symlink</code>:  从源符号链接包到目标</li>
</ul></dd><dt id="uv-pip-sync--managed-python"><a href="#uv-pip-sync--managed-python"><code>--managed-python</code></a></dt><dd><p>Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果没有安装 uv 管理的 Python 版本，则会使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-pip-sync--no-allow-empty-requirements"><a href="#uv-pip-sync--no-allow-empty-requirements"><code>--no-allow-empty-requirements</code></a></dt><dt id="uv-pip-sync--no-binary"><a href="#uv-pip-sync--no-binary"><code>--no-binary</code></a> <i>no-binary</i></dt><dd><p>不安装预构建的 wheel。</p>
<p>给定的包将从源代码构建并安装。解析器仍将使用预构建的 wheel 来提取包元数据（如果可用）。</p>
<p>可以指定多个包。使用 <code>:all:</code> 禁用所有包的二进制文件。使用 <code>:none:</code> 清除之前指定的包。</p>
</dd><dt id="uv-pip-sync--no-break-system-packages"><a href="#uv-pip-sync--no-break-system-packages"><code>--no-break-system-packages</code></a></dt><dt id="uv-pip-sync--no-build"><a href="#uv-pip-sync--no-build"><code>--no-build</code></a></dt><dd><p>不构建源代码分发包。</p>
<p>启用后，解析过程将不会运行任意 Python 代码。已构建的源代码分发包的缓存 wheel 将被重用，但需要构建分发包的操作将报错退出。</p>
<p><code>--only-binary :all:</code> 的别名。</p>
</dd><dt id="uv-pip-sync--no-build-isolation"><a href="#uv-pip-sync--no-build-isolation"><code>--no-build-isolation</code></a></dt><dd><p>构建源代码分发包时禁用隔离环境。</p>
<p>假定 PEP 518 指定的构建依赖已安装。</p>
<p>也可通过 <code>UV_NO_BUILD_ISOLATION</code> 环境变量设置。</p></dd><dt id="uv-pip-sync--no-cache"><a href="#uv-pip-sync--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-pip-sync--no-index"><a href="#uv-pip-sync--no-index"><code>--no-index</code></a></dt><dd><p>忽略注册表索引（例如 PyPI），转而依赖直接 URL 依赖和通过 <code>--find-links</code> 提供的依赖</p>
</dd><dt id="uv-pip-sync--no-managed-python"><a href="#uv-pip-sync--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用使用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>uv 将改为在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-pip-sync--no-progress"><a href="#uv-pip-sync--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，spinner 或进度条。</p>
</dd><dt id="uv-pip-sync--no-python-downloads"><a href="#uv-pip-sync--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用自动下载 Python。</p>
</dd><dt id="uv-pip-sync--no-sources"><a href="#uv-pip-sync--no-sources"><code>--no-sources</code></a></dt><dd><p>解析依赖时忽略 <code>tool.uv.sources</code> 表。用于基于符合标准的、可发布的包元数据进行锁定，而不是使用任何工作空间、Git、URL 或本地路径源</p>
<p>也可通过 <code>UV_NO_SOURCES</code> 环境变量设置。</p></dd><dt id="uv-pip-sync--no-sources-package"><a href="#uv-pip-sync--no-sources-package"><code>--no-sources-package</code></a> <i>no-sources-package</i></dt><dd><p>不要为指定的包使用 <code>tool.uv.sources</code> 表中的源 [env: <code>UV_NO_SOURCES_PACKAGE</code>=]</p>
</dd><dt id="uv-pip-sync--no-verify-hashes"><a href="#uv-pip-sync--no-verify-hashes"><code>--no-verify-hashes</code></a></dt><dd><p>Disable validation of hashes in the requirements file.</p>
<p>默认情况下，uv 将验证 requirements 文件中任何可用的哈希值，但不会要求所有 requirement 都有关联的哈希值。要强制哈希验证，请使用 <code>--require-hashes</code>。</p>
<p>May also be set with the <code>UV_NO_VERIFY_HASHES</code> environment variable.</p></dd><dt id="uv-pip-sync--offline"><a href="#uv-pip-sync--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-pip-sync--only-binary"><a href="#uv-pip-sync--only-binary"><code>--only-binary</code></a> <i>only-binary</i></dt><dd><p>仅使用预构建的 wheel；不构建源代码分发包。</p>
<p>启用后，解析过程将不会运行来自给定包的代码。已构建的源代码分发包的缓存 wheel 将被重用，但需要构建分发包的操作将报错退出。</p>
<p>可以指定多个包。使用 <code>:all:</code> 禁用所有包的二进制文件。使用 <code>:none:</code> 清除之前指定的包。</p>
</dd><dt id="uv-pip-sync--prefix"><a href="#uv-pip-sync--prefix"><code>--prefix</code></a> <i>prefix</i></dt><dd><p>将包安装到指定目录下的 <code>lib</code>、<code>bin</code> 和其他顶层文件夹中，如同在该位置存在虚拟环境一样。</p>
<p>In general, prefer the use of <code>--python</code> to install into an alternate environment, as scripts and other artifacts installed via <code>--prefix</code> will reference the installing interpreter, rather than any interpreter added to the <code>--prefix</code> directory, rendering them non-portable.</p>
<p>与其他安装操作不同，此命令不需要发现现有 Python 环境，仅搜索用于包解析的 Python 解释器。如果找不到合适的 Python 解释器，uv 将安装一个。要禁用此行为，请添加 <code>--no-python-downloads</code>。</p>
</dd><dt id="uv-pip-sync--project"><a href="#uv-pip-sync--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-pip-sync--python"><a href="#uv-pip-sync--python"><code>--python</code></a>, <code>-p</code> <i>python</i></dt><dd><p>The Python interpreter into which packages should be installed.</p>
<p>By default, syncing requires a virtual environment. A path to an alternative Python can be
provided, but it is only recommended in continuous integration (CI) environments and should
be used with caution, as it can modify the system Python installation.</p>
<p>参见 <a href="#uv-python">uv python</a> 了解 Python 发现机制和支持的请求格式的详细信息。</p>
<p>May also be set with the <code>UV_PYTHON</code> environment variable.</p></dd><dt id="uv-pip-sync--python-platform"><a href="#uv-pip-sync--python-platform"><code>--python-platform</code></a> <i>python-platform</i></dt><dd><p>The platform for which requirements should be installed.</p>
<p>表示为"目标三元组"（target triple），一个描述目标平台的字符串，包含 CPU、供应商和操作系统名称，如 <code>x86_64-unknown-linux-gnu</code> 或 <code>aarch64-apple-darwin</code>。</p>
<p>当目标为 macOS（Darwin）时，默认最低版本为 <code>13.0</code>。使用 <code>MACOSX_DEPLOYMENT_TARGET</code> 指定不同的最低版本，例如 <code>14.0</code>。</p>
<p>当目标为 iOS 时，默认最低版本为 <code>13.0</code>。使用 <code>IPHONEOS_DEPLOYMENT_TARGET</code> 指定不同的最低版本，例如 <code>14.0</code>。</p>
<p>当目标为 Android 时，默认最低 Android API 级别为 <code>24</code>。使用 <code>ANDROID_API_LEVEL</code> 指定不同的最低版本，例如 <code>26</code>。</p>
<p>WARNING: When specified, uv will select wheels that are compatible with the <em>target</em> platform; as a result, the installed distributions may not be compatible with the <em>current</em> platform. Conversely, any distributions that are built from source may be incompatible with the <em>target</em> platform, as they will be built for the <em>current</em> platform. The <code>--python-platform</code> option is intended for advanced use cases.</p>
<p>可选值：</p>
<ul>
<li><code>windows</code>:  <code>x86_64-pc-windows-msvc</code> 的别名，Windows 的默认目标</li>
<li><code>linux</code>:  <code>x86_64-unknown-linux-gnu</code> 的别名，Linux 的默认目标</li>
<li><code>macos</code>:  <code>aarch64-apple-darwin</code> 的别名，macOS 的默认目标</li>
<li><code>x86_64-pc-windows-msvc</code>:  64 位 x86 Windows 目标</li>
<li><code>aarch64-pc-windows-msvc</code>:  ARM64 Windows 目标</li>
<li><code>i686-pc-windows-msvc</code>:  32 位 x86 Windows 目标</li>
<li><code>x86_64-unknown-linux-gnu</code>:  x86 Linux 目标。等效于 <code>x86_64-manylinux_2_28</code></li>
<li><code>aarch64-apple-darwin</code>:  基于 ARM 的 macOS 目标，如 Apple Silicon 设备上所见</li>
<li><code>x86_64-apple-darwin</code>:  x86 macOS 目标</li>
<li><code>aarch64-unknown-linux-gnu</code>:  ARM64 Linux 目标。等效于 <code>aarch64-manylinux_2_28</code></li>
<li><code>aarch64-unknown-linux-musl</code>:  ARM64 Linux 目标</li>
<li><code>x86_64-unknown-linux-musl</code>:  <code>x86_64</code> Linux 目标</li>
<li><code>riscv64-unknown-linux</code>:  RISCV64 Linux 目标</li>
<li><code>x86_64-manylinux2014</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux2014</code> 平台。等效于 <code>x86_64-manylinux_2_17</code></li>
<li><code>x86_64-manylinux_2_17</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_17</code> 平台</li>
<li><code>x86_64-manylinux_2_28</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_28</code> 平台</li>
<li><code>x86_64-manylinux_2_31</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_31</code> 平台</li>
<li><code>x86_64-manylinux_2_32</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_32</code> 平台</li>
<li><code>x86_64-manylinux_2_33</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_33</code> 平台</li>
<li><code>x86_64-manylinux_2_34</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_34</code> 平台</li>
<li><code>x86_64-manylinux_2_35</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_35</code> 平台</li>
<li><code>x86_64-manylinux_2_36</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_36</code> 平台</li>
<li><code>x86_64-manylinux_2_37</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_37</code> 平台</li>
<li><code>x86_64-manylinux_2_38</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_38</code> 平台</li>
<li><code>x86_64-manylinux_2_39</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_39</code> 平台</li>
<li><code>x86_64-manylinux_2_40</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_40</code> 平台</li>
<li><code>aarch64-manylinux2014</code>:  ARM64 目标，适用于 <code>manylinux2014</code> 平台。等效于 <code>aarch64-manylinux_2_17</code></li>
<li><code>aarch64-manylinux_2_17</code>:  ARM64 目标，适用于 <code>manylinux_2_17</code> 平台</li>
<li><code>aarch64-manylinux_2_28</code>:  ARM64 目标，适用于 <code>manylinux_2_28</code> 平台</li>
<li><code>aarch64-manylinux_2_31</code>:  ARM64 目标，适用于 <code>manylinux_2_31</code> 平台</li>
<li><code>aarch64-manylinux_2_32</code>:  ARM64 目标，适用于 <code>manylinux_2_32</code> 平台</li>
<li><code>aarch64-manylinux_2_33</code>:  ARM64 目标，适用于 <code>manylinux_2_33</code> 平台</li>
<li><code>aarch64-manylinux_2_34</code>:  ARM64 目标，适用于 <code>manylinux_2_34</code> 平台</li>
<li><code>aarch64-manylinux_2_35</code>:  ARM64 目标，适用于 <code>manylinux_2_35</code> 平台</li>
<li><code>aarch64-manylinux_2_36</code>:  ARM64 目标，适用于 <code>manylinux_2_36</code> 平台</li>
<li><code>aarch64-manylinux_2_37</code>:  ARM64 目标，适用于 <code>manylinux_2_37</code> 平台</li>
<li><code>aarch64-manylinux_2_38</code>:  ARM64 目标，适用于 <code>manylinux_2_38</code> 平台</li>
<li><code>aarch64-manylinux_2_39</code>:  ARM64 目标，适用于 <code>manylinux_2_39</code> 平台</li>
<li><code>aarch64-manylinux_2_40</code>:  ARM64 目标，适用于 <code>manylinux_2_40</code> 平台</li>
<li><code>aarch64-linux-android</code>:  ARM64 Android 目标</li>
<li><code>x86_64-linux-android</code>:  <code>x86_64</code> Android 目标</li>
<li><code>wasm32-pyodide2024</code>:  wasm32 目标，使用 Pyodide 2024 平台。适用于 Python 3.12。参见 <a href="https://pyodide.org/en/stable/development/abi/312.html">https://pyodide.org/en/stable/development/abi/312.html</a></li>
<li><code>wasm32-pyodide2025</code>:  wasm32 目标，使用 Pyodide 2025 平台。适用于 Python 3.13。参见 <a href="https://pyodide.org/en/stable/development/abi/313.html">https://pyodide.org/en/stable/development/abi/313.html</a></li>
<li><code>arm64-apple-ios</code>:  iOS 设备的 ARM64 目标</li>
<li><code>arm64-apple-ios-simulator</code>:  iOS 模拟器的 ARM64 目标</li>
<li><code>x86_64-apple-ios-simulator</code>:  iOS 模拟器的 <code>x86_64</code> 目标</li>
</ul></dd><dt id="uv-pip-sync--python-version"><a href="#uv-pip-sync--python-version"><code>--python-version</code></a> <i>python-version</i></dt><dd><p>The minimum Python version that should be supported by the requirements (e.g., <code>3.7</code> or <code>3.7.9</code>).</p>
<p>If a patch version is omitted, the minimum patch version is assumed. For example, <code>3.7</code> is mapped to <code>3.7.0</code>.</p>
</dd><dt id="uv-pip-sync--quiet"><a href="#uv-pip-sync--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项（如 <code>-qq</code>）将启用静默模式，uv 将不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-pip-sync--refresh"><a href="#uv-pip-sync--refresh"><code>--refresh</code></a></dt><dd><p>刷新所有缓存数据</p>
</dd><dt id="uv-pip-sync--refresh-package"><a href="#uv-pip-sync--refresh-package"><code>--refresh-package</code></a> <i>refresh-package</i></dt><dd><p>刷新特定包的缓存数据</p>
</dd><dt id="uv-pip-sync--reinstall"><a href="#uv-pip-sync--reinstall"><code>--reinstall</code></a>, <code>--force-reinstall</code></dt><dd><p>Reinstall all packages, regardless of whether they're already installed. Implies <code>--refresh</code></p>
</dd><dt id="uv-pip-sync--reinstall-package"><a href="#uv-pip-sync--reinstall-package"><code>--reinstall-package</code></a> <i>reinstall-package</i></dt><dd><p>Reinstall a specific package, regardless of whether it's already installed. Implies <code>--refresh-package</code></p>
</dd><dt id="uv-pip-sync--require-hashes"><a href="#uv-pip-sync--require-hashes"><code>--require-hashes</code></a></dt><dd><p>Require a matching hash for each requirement.</p>
<p>默认情况下，uv 将验证 requirements 文件中任何可用的哈希值，但不会要求所有 requirement 都有关联的哈希值。</p>
<p>When <code>--require-hashes</code> is enabled, <em>all</em> requirements must include a hash or set of hashes, and <em>all</em> requirements must either be pinned to exact versions (e.g., <code>==1.0.0</code>), or be specified via direct URL.</p>
<p>哈希检查模式引入了许多额外的约束：</p>
<ul>
<li>Git dependencies are not supported. - Editable installations are not supported. - Local dependencies are not supported, unless they point to a specific wheel (<code>.whl</code>) or source archive (<code>.zip</code>, <code>.tar.gz</code>), as opposed to a directory.</li>
</ul>
<p>May also be set with the <code>UV_REQUIRE_HASHES</code> environment variable.</p></dd><dt id="uv-pip-sync--strict"><a href="#uv-pip-sync--strict"><code>--strict</code></a></dt><dd><p>安装完成后验证 Python 环境，检测包含缺失依赖或其他问题的包</p>
</dd><dt id="uv-pip-sync--system"><a href="#uv-pip-sync--system"><code>--system</code></a></dt><dd><p>Install packages into the system Python environment.</p>
<p>默认情况下，uv 安装到当前工作目录或任何父目录中的虚拟环境。<code>--system</code> 选项指示 uv 改为使用系统 <code>PATH</code> 中找到的第一个 Python。</p>
<p>警告：<code>--system</code> 旨在用于持续集成（CI）环境中，应谨慎使用，因为它可能会修改系统 Python 安装。</p>
<p>May also be set with the <code>UV_SYSTEM_PYTHON</code> environment variable.</p></dd><dt id="uv-pip-sync--system-certs"><a href="#uv-pip-sync--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能需要使用平台的原生证书存储，特别是当您依赖系统证书存储中包含的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-pip-sync--target"><a href="#uv-pip-sync--target"><code>--target</code></a>, <code>-t</code> <i>target</i></dt><dd><p>Install packages into the specified directory, rather than into the virtual or system Python environment. The packages will be installed at the top-level of the directory.</p>
<p>与其他安装操作不同，此命令不需要发现现有 Python 环境，仅搜索用于包解析的 Python 解释器。如果找不到合适的 Python 解释器，uv 将安装一个。要禁用此行为，请添加 <code>--no-python-downloads</code>。</p>
</dd><dt id="uv-pip-sync--torch-backend"><a href="#uv-pip-sync--torch-backend"><code>--torch-backend</code></a> <i>torch-backend</i></dt><dd><p>获取 PyTorch 生态系统中软件包时使用的后端（例如，<code>cpu</code>、<code>cu126</code> 或 <code>auto</code>）。</p>
<p>设置后，uv 将忽略为 PyTorch 生态系统中的包配置的索引 URL，而改用定义的后端。</p>
<p>For example, when set to <code>cpu</code>, uv will use the CPU-only PyTorch index; when set to <code>cu126</code>, uv will use the PyTorch index for CUDA 12.6.</p>
<p><code>auto</code> 模式将尝试根据当前安装的 CUDA 驱动程序检测适当的 PyTorch 索引。</p>
<p>此选项为预览功能，可能在未来的任何版本中发生变化。</p>
<p>May also be set with the <code>UV_TORCH_BACKEND</code> environment variable.</p><p>可选值：</p>
<ul>
<li><code>auto</code>:  Select the appropriate PyTorch index based on the operating system and CUDA driver version</li>
<li><code>cpu</code>:  Use the CPU-only PyTorch index</li>
<li><code>cu130</code>:  Use the PyTorch index for CUDA 13.0</li>
<li><code>cu129</code>:  Use the PyTorch index for CUDA 12.9</li>
<li><code>cu128</code>:  Use the PyTorch index for CUDA 12.8</li>
<li><code>cu126</code>:  Use the PyTorch index for CUDA 12.6</li>
<li><code>cu125</code>:  Use the PyTorch index for CUDA 12.5</li>
<li><code>cu124</code>:  Use the PyTorch index for CUDA 12.4</li>
<li><code>cu123</code>:  Use the PyTorch index for CUDA 12.3</li>
<li><code>cu122</code>:  Use the PyTorch index for CUDA 12.2</li>
<li><code>cu121</code>:  Use the PyTorch index for CUDA 12.1</li>
<li><code>cu120</code>:  Use the PyTorch index for CUDA 12.0</li>
<li><code>cu118</code>:  Use the PyTorch index for CUDA 11.8</li>
<li><code>cu117</code>:  Use the PyTorch index for CUDA 11.7</li>
<li><code>cu116</code>:  Use the PyTorch index for CUDA 11.6</li>
<li><code>cu115</code>:  Use the PyTorch index for CUDA 11.5</li>
<li><code>cu114</code>:  Use the PyTorch index for CUDA 11.4</li>
<li><code>cu113</code>:  Use the PyTorch index for CUDA 11.3</li>
<li><code>cu112</code>:  Use the PyTorch index for CUDA 11.2</li>
<li><code>cu111</code>:  Use the PyTorch index for CUDA 11.1</li>
<li><code>cu110</code>:  Use the PyTorch index for CUDA 11.0</li>
<li><code>cu102</code>:  Use the PyTorch index for CUDA 10.2</li>
<li><code>cu101</code>:  Use the PyTorch index for CUDA 10.1</li>
<li><code>cu100</code>:  Use the PyTorch index for CUDA 10.0</li>
<li><code>cu92</code>:  Use the PyTorch index for CUDA 9.2</li>
<li><code>cu91</code>:  Use the PyTorch index for CUDA 9.1</li>
<li><code>cu90</code>:  Use the PyTorch index for CUDA 9.0</li>
<li><code>cu80</code>:  Use the PyTorch index for CUDA 8.0</li>
<li><code>rocm7.2</code>:  Use the PyTorch index for ROCm 7.2</li>
<li><code>rocm7.1</code>:  Use the PyTorch index for ROCm 7.1</li>
<li><code>rocm7.0</code>:  Use the PyTorch index for ROCm 7.0</li>
<li><code>rocm6.4</code>:  Use the PyTorch index for ROCm 6.4</li>
<li><code>rocm6.3</code>:  Use the PyTorch index for ROCm 6.3</li>
<li><code>rocm6.2.4</code>:  Use the PyTorch index for ROCm 6.2.4</li>
<li><code>rocm6.2</code>:  Use the PyTorch index for ROCm 6.2</li>
<li><code>rocm6.1</code>:  Use the PyTorch index for ROCm 6.1</li>
<li><code>rocm6.0</code>:  Use the PyTorch index for ROCm 6.0</li>
<li><code>rocm5.7</code>:  Use the PyTorch index for ROCm 5.7</li>
<li><code>rocm5.6</code>:  Use the PyTorch index for ROCm 5.6</li>
<li><code>rocm5.5</code>:  Use the PyTorch index for ROCm 5.5</li>
<li><code>rocm5.4.2</code>:  Use the PyTorch index for ROCm 5.4.2</li>
<li><code>rocm5.4</code>:  Use the PyTorch index for ROCm 5.4</li>
<li><code>rocm5.3</code>:  Use the PyTorch index for ROCm 5.3</li>
<li><code>rocm5.2</code>:  Use the PyTorch index for ROCm 5.2</li>
<li><code>rocm5.1.1</code>:  Use the PyTorch index for ROCm 5.1.1</li>
<li><code>rocm4.2</code>:  Use the PyTorch index for ROCm 4.2</li>
<li><code>rocm4.1</code>:  Use the PyTorch index for ROCm 4.1</li>
<li><code>rocm4.0.1</code>:  Use the PyTorch index for ROCm 4.0.1</li>
<li><code>xpu</code>:  Use the PyTorch index for Intel XPU</li>
</ul></dd><dt id="uv-pip-sync--verbose"><a href="#uv-pip-sync--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>

## uv pip install

将包安装到环境中

<h3 class="cli-reference">Usage</h3>

```
uv pip install [OPTIONS] <PACKAGE|--requirements <REQUIREMENTS>|--editable <EDITABLE>|--group <GROUP>>
```

<h3 class="cli-reference">Arguments</h3>

<dl class="cli-reference"><dt id="uv-pip-install--package"><a href="#uv-pip-install--package"><code>PACKAGE</code></a></dt><dd><p>Install all listed packages.</p>
<p>包的顺序用于确定解析过程中的优先级。</p>
</dd></dl>

<h3 class="cli-reference">Options</h3>

<dl class="cli-reference"><dt id="uv-pip-install--all-extras"><a href="#uv-pip-install--all-extras"><code>--all-extras</code></a></dt><dd><p>包含所有可选依赖。</p>
<p>仅适用于 <code>pylock.toml</code>、<code>pyproject.toml</code>、<code>setup.py</code> 和 <code>setup.cfg</code> 源。</p>
</dd><dt id="uv-pip-install--allow-insecure-host"><a href="#uv-pip-install--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机的非安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（如 <code>localhost</code>）、主机-端口对（如 <code>localhost:8080</code>）或 URL（如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您面临中间人攻击（MITM）的风险。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-pip-install--break-system-packages"><a href="#uv-pip-install--break-system-packages"><code>--break-system-packages</code></a></dt><dd><p>允许 uv 修改 <code>EXTERNALLY-MANAGED</code> 的 Python 安装。</p>
<p>警告：<code>--break-system-packages</code> 旨在用于持续集成（CI）环境中，当安装到由外部包管理器（如 <code>apt</code>）管理的 Python 安装中时。应谨慎使用，因为此类 Python 安装明确建议不要由其他包管理器（如 uv 或 <code>pip</code>）进行修改。</p>
<p>也可通过 <code>UV_BREAK_SYSTEM_PACKAGES</code> 环境变量设置。</p></dd><dt id="uv-pip-install--build-constraints"><a href="#uv-pip-install--build-constraints"><code>--build-constraints</code></a>, <code>--build-constraint</code>, <code>-b</code> <i>build-constraints</i></dt><dd><p>构建源代码分发包时，使用给定的 requirements 文件来约束构建依赖。</p>
<p>约束文件（constraints files）是类似 <code>requirements.txt</code> 的文件，仅控制所安装依赖的<em>版本</em>。但是，在约束文件中包含某个包<em>不会</em>触发该包的安装。</p>
<p>也可以通过 <code>UV_BUILD_CONSTRAINT</code> 环境变量设置。</p></dd><dt id="uv-pip-install--cache-dir"><a href="#uv-pip-install--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>默认值为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>（macOS 和 Linux），以及 <code>%LOCALAPPDATA%\uv\cache</code>（Windows）。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-pip-install--color"><a href="#uv-pip-install--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 在写入终端时会自动检测颜色支持。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>:  仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>:  无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>:  禁用彩色输出</li>
</ul></dd><dt id="uv-pip-install--compile-bytecode"><a href="#uv-pip-install--compile-bytecode"><code>--compile-bytecode</code></a>, <code>--compile</code></dt><dd><p>安装后编译 Python 文件为字节码。</p>
<p>默认情况下，uv 不会将 Python（<code>.py</code>）文件编译为字节码（<code>__pycache__/*.pyc</code>）；而是在首次导入模块时延迟编译。对于启动时间至关重要的用例，例如 CLI 应用程序和 Docker 容器，可以启用此选项，以较长的安装时间换取更快的启动时间。</p>
<p>启用后，uv 将处理整个 site-packages 目录（包括当前操作未修改的包）以保持一致性。与 pip 一样，它也会忽略错误。</p>
<p>也可通过 <code>UV_COMPILE_BYTECODE</code> 环境变量设置。</p></dd><dt id="uv-pip-install--config-file"><a href="#uv-pip-install--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-pip-install--config-setting"><a href="#uv-pip-install--config-setting"><code>--config-setting</code></a>, <code>--config-settings</code>, <code>-C</code> <i>config-setting</i></dt><dd><p>传递给 PEP 517 构建后端（build backend）的设置，以 <code>KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-pip-install--config-settings-package"><a href="#uv-pip-install--config-settings-package"><code>--config-settings-package</code></a>, <code>--config-settings-package</code> <i>config-settings-package</i></dt><dd><p>为特定包传递给 PEP 517 构建后端（build backend）的设置，以 <code>PACKAGE:KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-pip-install--constraints"><a href="#uv-pip-install--constraints"><code>--constraints</code></a>, <code>--constraint</code>, <code>-c</code> <i>constraints</i></dt><dd><p>使用给定的 requirements 文件来约束版本。</p>
<p>约束文件（constraints files）是类似 <code>requirements.txt</code> 的文件，仅控制所安装依赖的<em>版本</em>。但是，在约束文件中包含某个包<em>不会</em>触发该包的安装。</p>
<p>这相当于 pip 的 <code>--constraint</code> 选项。</p>
<p>也可以通过 <code>UV_CONSTRAINT</code> 环境变量设置。</p></dd><dt id="uv-pip-install--default-index"><a href="#uv-pip-install--default-index"><code>--default-index</code></a> <i>default-index</i></dt><dd><p>默认包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志指定的索引优先级低于通过 <code>--index</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_DEFAULT_INDEX</code> 环境变量设置。</p></dd><dt id="uv-pip-install--directory"><a href="#uv-pip-install--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径将以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-pip-install--dry-run"><a href="#uv-pip-install--dry-run"><code>--dry-run</code></a></dt><dd><p>执行预演（dry run），即不实际安装任何内容，仅解析依赖并打印结果计划</p>
</dd><dt id="uv-pip-install--editable"><a href="#uv-pip-install--editable"><code>--editable</code></a>, <code>-e</code> <i>editable</i></dt><dd><p>Install the editable package based on the provided local file path</p>
</dd><dt id="uv-pip-install--exact"><a href="#uv-pip-install--exact"><code>--exact</code></a></dt><dd><p>Perform an exact sync, removing extraneous packages.</p>
<p>默认情况下，安装将进行最小必要更改以满足 requirements。启用后，uv 将更新环境以精确匹配 requirements，移除不在 requirements 中的包。</p>
</dd><dt id="uv-pip-install--exclude-newer"><a href="#uv-pip-install--exclude-newer"><code>--exclude-newer</code></a> <i>exclude-newer</i></dt><dd><p>将候选包限制为在给定日期之前上传的版本。</p>
<p>日期与每个单独分发制品（distribution artifact）的上传时间（即每个文件上传到包索引的时间）进行比较，而非包版本的发布日期。</p>
<p>接受 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、相同格式的本地日期（例如 <code>2006-12-02</code>，基于系统配置的时区解析）、"友好"持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不遵循本地时区语义，始终按固定秒数计算，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月和年等日历单位。</p>
<p>也可通过 <code>UV_EXCLUDE_NEWER</code> 环境变量设置。</p></dd><dt id="uv-pip-install--exclude-newer-package"><a href="#uv-pip-install--exclude-newer-package"><code>--exclude-newer-package</code></a> <i>exclude-newer-package</i></dt><dd><p>将特定包的候选版本限制为在给定日期之前上传的版本。</p>
<p>接受 <code>PACKAGE=DATE</code> 格式的包-日期对，其中 <code>DATE</code> 为 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、相同格式的本地日期（例如 <code>2006-12-02</code>，基于系统配置的时区解析）、"友好"持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不遵循本地时区语义，始终按固定秒数计算，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月和年等日历单位。</p>
<p>可为不同包多次提供。</p>
</dd><dt id="uv-pip-install--excludes"><a href="#uv-pip-install--excludes"><code>--excludes</code></a>, <code>--exclude</code> <i>excludes</i></dt><dd><p>使用给定的 requirements 文件从解析中排除包。</p>
<p>排除文件是类似 <code>requirements.txt</code> 的文件，指定要从解析中排除的包。当包被排除时，它将完全从依赖列表中省略，并且其自身的依赖关系将在解析阶段被忽略。排除是无条件的，即忽略 requirement 版本说明符和标记（markers）；提供的文件中列出的任何包都将从所有已解析环境中省略。</p>
<p>也可通过 <code>UV_EXCLUDE</code> 环境变量设置。</p></dd><dt id="uv-pip-install--extra"><a href="#uv-pip-install--extra"><code>--extra</code></a> <i>extra</i></dt><dd><p>包含来自指定 extra 名称的可选依赖；可多次提供。</p>
<p>仅适用于 <code>pylock.toml</code>、<code>pyproject.toml</code>、<code>setup.py</code> 和 <code>setup.cfg</code> 源。</p>
</dd><dt id="uv-pip-install--extra-index-url"><a href="#uv-pip-install--extra-index-url"><code>--extra-index-url</code></a> <i>extra-index-url</i></dt><dd><p>（已弃用：请改用 <code>--index</code>）除 <code>--index-url</code> 之外要使用的额外包索引 URL。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于由 <code>--index-url</code> 指定的索引（默认为 PyPI）。当提供多个 <code>--extra-index-url</code> 标志时，优先级按先后顺序递减。</p>
<p>也可通过 <code>UV_EXTRA_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-pip-install--find-links"><a href="#uv-pip-install--find-links"><code>--find-links</code></a>, <code>-f</code> <i>find-links</i></dt><dd><p>在注册表索引之外，搜索候选分发包的额外位置。</p>
<p>如果提供的是路径，目标必须是一个目录，其顶层包含作为 wheel 文件（<code>.whl</code>）或源代码分发包（例如 <code>.tar.gz</code> 或 <code>.zip</code>）的包。</p>
<p>如果提供的是 URL，页面必须包含一个扁平列表，其中包含符合上述格式的包文件链接。</p>
<p>也可通过 <code>UV_FIND_LINKS</code> 环境变量设置。</p></dd><dt id="uv-pip-install--fork-strategy"><a href="#uv-pip-install--fork-strategy"><code>--fork-strategy</code></a> <i>fork-strategy</i></dt><dd><p>在跨 Python 版本和平台选择给定包的多个版本时使用的策略。</p>
<p>默认情况下，uv 会为每个受支持的 Python 版本（<code>requires-python</code>）优化选择每个包的最新版本，同时最小化跨平台选择的版本数量。</p>
<p>在 <code>fewest</code> 策略下，uv 将最小化每个包选择的版本数量，优先选择与更广泛受支持的 Python 版本或平台兼容的旧版本。</p>
<p>也可通过 <code>UV_FORK_STRATEGY</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>fewest</code>:  优化选择每个包的最少版本数。如果旧版本与更广泛的受支持 Python 版本或平台兼容，则可能会优先选择旧版本</li>
<li><code>requires-python</code>:  优化选择每个受支持 Python 版本的每个包的最新支持版本</li>
</ul></dd><dt id="uv-pip-install--group"><a href="#uv-pip-install--group"><code>--group</code></a> <i>group</i></dt><dd><p>从给定的 <code>pylock.toml</code> 或 <code>pyproject.toml</code> 安装指定的依赖组。</p>
<p>如果未提供路径，则使用工作目录中的 <code>pylock.toml</code> 或 <code>pyproject.toml</code>。</p>
<p>可多次提供。</p>
</dd><dt id="uv-pip-install--help"><a href="#uv-pip-install--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简洁帮助信息</p>
</dd><dt id="uv-pip-install--index"><a href="#uv-pip-install--index"><code>--index</code></a> <i>index</i></dt><dd><p>解析依赖时使用的 URL，作为默认索引的补充。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于由 <code>--default-index</code> 指定的索引（默认为 PyPI）。当提供多个 <code>--index</code> 标志时，优先级按先后顺序递减。</p>
<p>不支持将索引名称作为值。相对路径必须通过 <code>./</code> 或 <code>../</code>（Unix 上）或 <code>.\\</code>、<code>..\\</code>、<code>./</code> 或 <code>../</code>（Windows 上）与索引名称进行区分。</p>
<p>也可通过 <code>UV_INDEX</code> 环境变量设置。</p></dd><dt id="uv-pip-install--index-strategy"><a href="#uv-pip-install--index-strategy"><code>--index-strategy</code></a> <i>index-strategy</i></dt><dd><p>针对多个索引 URL 进行解析时使用的策略。</p>
<p>默认情况下，uv 会在第一个包含给定包的索引处停止，并将解析范围限制为在该第一个索引（<code>first-index</code>）中存在的包。这可以防止"依赖混淆"攻击，即攻击者可以在备用索引上以相同名称上传恶意包。</p>
<p>也可通过 <code>UV_INDEX_STRATEGY</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>first-index</code>:  仅使用第一个返回给定包名匹配的索引的结果</li>
<li><code>unsafe-first-match</code>:  搜索所有索引中的每个包名，在切换到下一个索引之前耗尽第一个索引的版本</li>
<li><code>unsafe-best-match</code>:  搜索所有索引中的每个包名，优先选择找到的"最佳"版本。如果一个包版本存在于多个索引中，则仅查看第一个索引的条目</li>
</ul></dd><dt id="uv-pip-install--index-url"><a href="#uv-pip-install--index-url"><code>--index-url</code></a>, <code>-i</code> <i>index-url</i></dt><dd><p>（已弃用：请改用 <code>--default-index</code>）Python 包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志指定的索引优先级低于通过 <code>--extra-index-url</code> 标志指定的所有其他索引。</p>
<p>也可通过 <code>UV_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-pip-install--keyring-provider"><a href="#uv-pip-install--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>尝试使用 <code>keyring</code> 对索引 URL 进行身份验证。</p>
<p>目前仅支持 <code>--keyring-provider subprocess</code>，该选项配置 uv 使用 <code>keyring</code> CLI 来处理身份验证。</p>
<p>默认为 <code>disabled</code>。</p>
<p>也可通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disabled</code>:  不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>:  使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-pip-install--link-mode"><a href="#uv-pip-install--link-mode"><code>--link-mode</code></a> <i>link-mode</i></dt><dd><p>从全局缓存安装包时使用的方法。</p>
<p>默认在 macOS 和 Linux 上为 <code>clone</code>（也称为写时复制，Copy-on-Write），在 Windows 上为 <code>hardlink</code>。</p>
<p>警告：不建议使用 symlink 链接模式，因为它会在缓存和目标环境之间创建紧密耦合。例如，清除缓存（<code>uv cache clean</code>）将通过移除底层源文件来破坏所有已安装的包。请谨慎使用 symlink。</p>
<p>也可通过 <code>UV_LINK_MODE</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>clone</code>:  从源克隆（即写时复制）包到目标</li>
<li><code>copy</code>:  从源复制包到目标</li>
<li><code>hardlink</code>:  从源硬链接包到目标</li>
<li><code>symlink</code>:  从源符号链接包到目标</li>
</ul></dd><dt id="uv-pip-install--managed-python"><a href="#uv-pip-install--managed-python"><code>--managed-python</code></a></dt><dd><p>Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果没有安装 uv 管理的 Python 版本，则会使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-pip-install--no-binary"><a href="#uv-pip-install--no-binary"><code>--no-binary</code></a> <i>no-binary</i></dt><dd><p>不安装预构建的 wheel。</p>
<p>给定的包将从源代码构建并安装。解析器仍将使用预构建的 wheel 来提取包元数据（如果可用）。</p>
<p>可以指定多个包。使用 <code>:all:</code> 禁用所有包的二进制文件。使用 <code>:none:</code> 清除之前指定的包。</p>
</dd><dt id="uv-pip-install--no-break-system-packages"><a href="#uv-pip-install--no-break-system-packages"><code>--no-break-system-packages</code></a></dt><dt id="uv-pip-install--no-build"><a href="#uv-pip-install--no-build"><code>--no-build</code></a></dt><dd><p>不构建源代码分发包。</p>
<p>启用后，解析过程将不会运行任意 Python 代码。已构建的源代码分发包的缓存 wheel 将被重用，但需要构建分发包的操作将报错退出。</p>
<p><code>--only-binary :all:</code> 的别名。</p>
</dd><dt id="uv-pip-install--no-build-isolation"><a href="#uv-pip-install--no-build-isolation"><code>--no-build-isolation</code></a></dt><dd><p>构建源代码分发包时禁用隔离环境。</p>
<p>假定 PEP 518 指定的构建依赖已安装。</p>
<p>也可通过 <code>UV_NO_BUILD_ISOLATION</code> 环境变量设置。</p></dd><dt id="uv-pip-install--no-build-isolation-package"><a href="#uv-pip-install--no-build-isolation-package"><code>--no-build-isolation-package</code></a> <i>no-build-isolation-package</i></dt><dd><p>为特定包构建源代码分发包时禁用隔离。</p>
<p>假定这些包的 PEP 518 指定的构建依赖已安装。</p>
</dd><dt id="uv-pip-install--no-cache"><a href="#uv-pip-install--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-pip-install--no-config"><a href="#uv-pip-install--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常情况下，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-pip-install--no-deps"><a href="#uv-pip-install--no-deps"><code>--no-deps</code></a></dt><dd><p>Ignore package dependencies, instead only installing those packages explicitly listed on the command line or in the requirements files</p>
</dd><dt id="uv-pip-install--no-editable"><a href="#uv-pip-install--no-editable"><code>--no-editable</code></a></dt><dd><p>Install any editable dependencies as non-editable [env: UV_NO_EDITABLE=]</p>
</dd><dt id="uv-pip-install--no-editable-package"><a href="#uv-pip-install--no-editable-package"><code>--no-editable-package</code></a> <i>no-editable-package</i></dt><dd><p>Install the specified editable packages as non-editable</p>
</dd><dt id="uv-pip-install--no-index"><a href="#uv-pip-install--no-index"><code>--no-index</code></a></dt><dd><p>忽略注册表索引（例如 PyPI），转而依赖直接 URL 依赖和通过 <code>--find-links</code> 提供的依赖</p>
</dd><dt id="uv-pip-install--no-managed-python"><a href="#uv-pip-install--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用使用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>uv 将改为在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-pip-install--no-progress"><a href="#uv-pip-install--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，spinner 或进度条。</p>
</dd><dt id="uv-pip-install--no-python-downloads"><a href="#uv-pip-install--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用自动下载 Python。</p>
</dd><dt id="uv-pip-install--no-sources"><a href="#uv-pip-install--no-sources"><code>--no-sources</code></a></dt><dd><p>解析依赖时忽略 <code>tool.uv.sources</code> 表。用于基于符合标准的、可发布的包元数据进行锁定，而不是使用任何工作空间、Git、URL 或本地路径源</p>
<p>也可通过 <code>UV_NO_SOURCES</code> 环境变量设置。</p></dd><dt id="uv-pip-install--no-sources-package"><a href="#uv-pip-install--no-sources-package"><code>--no-sources-package</code></a> <i>no-sources-package</i></dt><dd><p>不要为指定的包使用 <code>tool.uv.sources</code> 表中的源 [env: <code>UV_NO_SOURCES_PACKAGE</code>=]</p>
</dd><dt id="uv-pip-install--no-verify-hashes"><a href="#uv-pip-install--no-verify-hashes"><code>--no-verify-hashes</code></a></dt><dd><p>Disable validation of hashes in the requirements file.</p>
<p>默认情况下，uv 将验证 requirements 文件中任何可用的哈希值，但不会要求所有 requirement 都有关联的哈希值。要强制哈希验证，请使用 <code>--require-hashes</code>。</p>
<p>May also be set with the <code>UV_NO_VERIFY_HASHES</code> environment variable.</p></dd><dt id="uv-pip-install--offline"><a href="#uv-pip-install--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-pip-install--only-binary"><a href="#uv-pip-install--only-binary"><code>--only-binary</code></a> <i>only-binary</i></dt><dd><p>仅使用预构建的 wheel；不构建源代码分发包。</p>
<p>启用后，解析过程将不会运行来自给定包的代码。已构建的源代码分发包的缓存 wheel 将被重用，但需要构建分发包的操作将报错退出。</p>
<p>可以指定多个包。使用 <code>:all:</code> 禁用所有包的二进制文件。使用 <code>:none:</code> 清除之前指定的包。</p>
</dd><dt id="uv-pip-install--overrides"><a href="#uv-pip-install--overrides"><code>--overrides</code></a>, <code>--override</code> <i>overrides</i></dt><dd><p>使用给定的 requirements 文件覆盖版本。</p>
<p>覆盖文件是类似 <code>requirements.txt</code> 的文件，强制安装特定版本的 requirement，无论任何组成包声明的依赖如何，也无论这是否会被视为无效的解析结果。</p>
<p>约束是<em>附加性</em>的，即它们与组成包的 requirements 合并，而覆盖是<em>绝对性</em>的，即它们完全替换组成包的 requirements。</p>
<p>也可通过 <code>UV_OVERRIDE</code> 环境变量设置。</p></dd><dt id="uv-pip-install--prefix"><a href="#uv-pip-install--prefix"><code>--prefix</code></a> <i>prefix</i></dt><dd><p>将包安装到指定目录下的 <code>lib</code>、<code>bin</code> 和其他顶层文件夹中，如同在该位置存在虚拟环境一样。</p>
<p>In general, prefer the use of <code>--python</code> to install into an alternate environment, as scripts and other artifacts installed via <code>--prefix</code> will reference the installing interpreter, rather than any interpreter added to the <code>--prefix</code> directory, rendering them non-portable.</p>
<p>与其他安装操作不同，此命令不需要发现现有 Python 环境，仅搜索用于包解析的 Python 解释器。如果找不到合适的 Python 解释器，uv 将安装一个。要禁用此行为，请添加 <code>--no-python-downloads</code>。</p>
</dd><dt id="uv-pip-install--prerelease"><a href="#uv-pip-install--prerelease"><code>--prerelease</code></a> <i>prerelease</i></dt><dd><p>考虑预发布版本时使用的策略。</p>
<p>默认情况下，uv 将接受<em>仅</em>发布预发布版本的包的预发布版本，以及声明的版本说明符中包含显式预发布标记的第一方 requirement（<code>if-necessary-or-explicit</code>）。</p>
<p>也可通过 <code>UV_PRERELEASE</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disallow</code>:  禁止所有预发布版本</li>
<li><code>allow</code>:  允许所有预发布版本</li>
<li><code>if-necessary</code>:  Allow pre-release versions if all versions of a package are pre-release</li>
<li><code>explicit</code>:  允许版本要求中带有显式预发布标记的第一方包的预发布版本</li>
<li><code>if-necessary-or-explicit</code>:  如果一个包的所有版本都是预发布版本，或者该包的版本要求中带有显式预发布标记，则允许预发布版本</li>
</ul></dd><dt id="uv-pip-install--project"><a href="#uv-pip-install--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-pip-install--python"><a href="#uv-pip-install--python"><code>--python</code></a>, <code>-p</code> <i>python</i></dt><dd><p>The Python interpreter into which packages should be installed.</p>
<p>By default, installation requires a virtual environment. A path to an alternative Python can
be provided, but it is only recommended in continuous integration (CI) environments and
should be used with caution, as it can modify the system Python installation.</p>
<p>参见 <a href="#uv-python">uv python</a> 了解 Python 发现机制和支持的请求格式的详细信息。</p>
<p>May also be set with the <code>UV_PYTHON</code> environment variable.</p></dd><dt id="uv-pip-install--python-platform"><a href="#uv-pip-install--python-platform"><code>--python-platform</code></a> <i>python-platform</i></dt><dd><p>The platform for which requirements should be installed.</p>
<p>表示为"目标三元组"（target triple），一个描述目标平台的字符串，包含 CPU、供应商和操作系统名称，如 <code>x86_64-unknown-linux-gnu</code> 或 <code>aarch64-apple-darwin</code>。</p>
<p>当目标为 macOS（Darwin）时，默认最低版本为 <code>13.0</code>。使用 <code>MACOSX_DEPLOYMENT_TARGET</code> 指定不同的最低版本，例如 <code>14.0</code>。</p>
<p>当目标为 iOS 时，默认最低版本为 <code>13.0</code>。使用 <code>IPHONEOS_DEPLOYMENT_TARGET</code> 指定不同的最低版本，例如 <code>14.0</code>。</p>
<p>当目标为 Android 时，默认最低 Android API 级别为 <code>24</code>。使用 <code>ANDROID_API_LEVEL</code> 指定不同的最低版本，例如 <code>26</code>。</p>
<p>WARNING: When specified, uv will select wheels that are compatible with the <em>target</em> platform; as a result, the installed distributions may not be compatible with the <em>current</em> platform. Conversely, any distributions that are built from source may be incompatible with the <em>target</em> platform, as they will be built for the <em>current</em> platform. The <code>--python-platform</code> option is intended for advanced use cases.</p>
<p>可选值：</p>
<ul>
<li><code>windows</code>:  <code>x86_64-pc-windows-msvc</code> 的别名，Windows 的默认目标</li>
<li><code>linux</code>:  <code>x86_64-unknown-linux-gnu</code> 的别名，Linux 的默认目标</li>
<li><code>macos</code>:  <code>aarch64-apple-darwin</code> 的别名，macOS 的默认目标</li>
<li><code>x86_64-pc-windows-msvc</code>:  64 位 x86 Windows 目标</li>
<li><code>aarch64-pc-windows-msvc</code>:  ARM64 Windows 目标</li>
<li><code>i686-pc-windows-msvc</code>:  32 位 x86 Windows 目标</li>
<li><code>x86_64-unknown-linux-gnu</code>:  x86 Linux 目标。等效于 <code>x86_64-manylinux_2_28</code></li>
<li><code>aarch64-apple-darwin</code>:  基于 ARM 的 macOS 目标，如 Apple Silicon 设备上所见</li>
<li><code>x86_64-apple-darwin</code>:  x86 macOS 目标</li>
<li><code>aarch64-unknown-linux-gnu</code>:  ARM64 Linux 目标。等效于 <code>aarch64-manylinux_2_28</code></li>
<li><code>aarch64-unknown-linux-musl</code>:  ARM64 Linux 目标</li>
<li><code>x86_64-unknown-linux-musl</code>:  <code>x86_64</code> Linux 目标</li>
<li><code>riscv64-unknown-linux</code>:  RISCV64 Linux 目标</li>
<li><code>x86_64-manylinux2014</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux2014</code> 平台。等效于 <code>x86_64-manylinux_2_17</code></li>
<li><code>x86_64-manylinux_2_17</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_17</code> 平台</li>
<li><code>x86_64-manylinux_2_28</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_28</code> 平台</li>
<li><code>x86_64-manylinux_2_31</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_31</code> 平台</li>
<li><code>x86_64-manylinux_2_32</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_32</code> 平台</li>
<li><code>x86_64-manylinux_2_33</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_33</code> 平台</li>
<li><code>x86_64-manylinux_2_34</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_34</code> 平台</li>
<li><code>x86_64-manylinux_2_35</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_35</code> 平台</li>
<li><code>x86_64-manylinux_2_36</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_36</code> 平台</li>
<li><code>x86_64-manylinux_2_37</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_37</code> 平台</li>
<li><code>x86_64-manylinux_2_38</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_38</code> 平台</li>
<li><code>x86_64-manylinux_2_39</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_39</code> 平台</li>
<li><code>x86_64-manylinux_2_40</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_40</code> 平台</li>
<li><code>aarch64-manylinux2014</code>:  ARM64 目标，适用于 <code>manylinux2014</code> 平台。等效于 <code>aarch64-manylinux_2_17</code></li>
<li><code>aarch64-manylinux_2_17</code>:  ARM64 目标，适用于 <code>manylinux_2_17</code> 平台</li>
<li><code>aarch64-manylinux_2_28</code>:  ARM64 目标，适用于 <code>manylinux_2_28</code> 平台</li>
<li><code>aarch64-manylinux_2_31</code>:  ARM64 目标，适用于 <code>manylinux_2_31</code> 平台</li>
<li><code>aarch64-manylinux_2_32</code>:  ARM64 目标，适用于 <code>manylinux_2_32</code> 平台</li>
<li><code>aarch64-manylinux_2_33</code>:  ARM64 目标，适用于 <code>manylinux_2_33</code> 平台</li>
<li><code>aarch64-manylinux_2_34</code>:  ARM64 目标，适用于 <code>manylinux_2_34</code> 平台</li>
<li><code>aarch64-manylinux_2_35</code>:  ARM64 目标，适用于 <code>manylinux_2_35</code> 平台</li>
<li><code>aarch64-manylinux_2_36</code>:  ARM64 目标，适用于 <code>manylinux_2_36</code> 平台</li>
<li><code>aarch64-manylinux_2_37</code>:  ARM64 目标，适用于 <code>manylinux_2_37</code> 平台</li>
<li><code>aarch64-manylinux_2_38</code>:  ARM64 目标，适用于 <code>manylinux_2_38</code> 平台</li>
<li><code>aarch64-manylinux_2_39</code>:  ARM64 目标，适用于 <code>manylinux_2_39</code> 平台</li>
<li><code>aarch64-manylinux_2_40</code>:  ARM64 目标，适用于 <code>manylinux_2_40</code> 平台</li>
<li><code>aarch64-linux-android</code>:  ARM64 Android 目标</li>
<li><code>x86_64-linux-android</code>:  <code>x86_64</code> Android 目标</li>
<li><code>wasm32-pyodide2024</code>:  wasm32 目标，使用 Pyodide 2024 平台。适用于 Python 3.12。参见 <a href="https://pyodide.org/en/stable/development/abi/312.html">https://pyodide.org/en/stable/development/abi/312.html</a></li>
<li><code>wasm32-pyodide2025</code>:  wasm32 目标，使用 Pyodide 2025 平台。适用于 Python 3.13。参见 <a href="https://pyodide.org/en/stable/development/abi/313.html">https://pyodide.org/en/stable/development/abi/313.html</a></li>
<li><code>arm64-apple-ios</code>:  iOS 设备的 ARM64 目标</li>
<li><code>arm64-apple-ios-simulator</code>:  iOS 模拟器的 ARM64 目标</li>
<li><code>x86_64-apple-ios-simulator</code>:  iOS 模拟器的 <code>x86_64</code> 目标</li>
</ul></dd><dt id="uv-pip-install--python-version"><a href="#uv-pip-install--python-version"><code>--python-version</code></a> <i>python-version</i></dt><dd><p>The minimum Python version that should be supported by the requirements (e.g., <code>3.7</code> or <code>3.7.9</code>).</p>
<p>If a patch version is omitted, the minimum patch version is assumed. For example, <code>3.7</code> is mapped to <code>3.7.0</code>.</p>
</dd><dt id="uv-pip-install--quiet"><a href="#uv-pip-install--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项（如 <code>-qq</code>）将启用静默模式，uv 将不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-pip-install--refresh"><a href="#uv-pip-install--refresh"><code>--refresh</code></a></dt><dd><p>刷新所有缓存数据</p>
</dd><dt id="uv-pip-install--refresh-package"><a href="#uv-pip-install--refresh-package"><code>--refresh-package</code></a> <i>refresh-package</i></dt><dd><p>刷新特定包的缓存数据</p>
</dd><dt id="uv-pip-install--reinstall"><a href="#uv-pip-install--reinstall"><code>--reinstall</code></a>, <code>--force-reinstall</code></dt><dd><p>Reinstall all packages, regardless of whether they're already installed. Implies <code>--refresh</code></p>
</dd><dt id="uv-pip-install--reinstall-package"><a href="#uv-pip-install--reinstall-package"><code>--reinstall-package</code></a> <i>reinstall-package</i></dt><dd><p>Reinstall a specific package, regardless of whether it's already installed. Implies <code>--refresh-package</code></p>
</dd><dt id="uv-pip-install--require-hashes"><a href="#uv-pip-install--require-hashes"><code>--require-hashes</code></a></dt><dd><p>Require a matching hash for each requirement.</p>
<p>默认情况下，uv 将验证 requirements 文件中任何可用的哈希值，但不会要求所有 requirement 都有关联的哈希值。</p>
<p>When <code>--require-hashes</code> is enabled, <em>all</em> requirements must include a hash or set of hashes, and <em>all</em> requirements must either be pinned to exact versions (e.g., <code>==1.0.0</code>), or be specified via direct URL.</p>
<p>哈希检查模式引入了许多额外的约束：</p>
<ul>
<li>Git dependencies are not supported. - Editable installations are not supported. - Local dependencies are not supported, unless they point to a specific wheel (<code>.whl</code>) or source archive (<code>.zip</code>, <code>.tar.gz</code>), as opposed to a directory.</li>
</ul>
<p>May also be set with the <code>UV_REQUIRE_HASHES</code> environment variable.</p></dd><dt id="uv-pip-install--requirements"><a href="#uv-pip-install--requirements"><code>--requirements</code></a>, <code>--requirement</code>, <code>-r</code> <i>requirements</i></dt><dd><p>安装 requirements 文件中列出的包。</p>
<p>支持以下格式：<code>requirements.txt</code>、包含内联元数据的 <code>.py</code> 文件、<code>pylock.toml</code>、<code>pyproject.toml</code>、<code>setup.py</code> 和 <code>setup.cfg</code>。</p>
<p>如果提供了 <code>pyproject.toml</code>、<code>setup.py</code> 或 <code>setup.cfg</code> 文件，uv 将提取相关项目的 requirements。</p>
<p>If <code>-</code> is provided, then requirements will be read from stdin.</p>
</dd><dt id="uv-pip-install--resolution"><a href="#uv-pip-install--resolution"><code>--resolution</code></a> <i>resolution</i></dt><dd><p>在给定包需求的不同兼容版本之间进行选择时使用的策略。</p>
<p>默认情况下，uv 会使用每个包的最新兼容版本（<code>highest</code>）。</p>
<p>May also be set with the <code>UV_RESOLUTION</code> environment variable.</p><p>可选值：</p>
<ul>
<li><code>highest</code>:  Resolve the highest compatible version of each package</li>
<li><code>lowest</code>:  Resolve the lowest compatible version of each package</li>
<li><code>lowest-direct</code>:  Resolve the lowest compatible version of any direct dependencies, and the highest compatible version of any transitive dependencies</li>
</ul></dd><dt id="uv-pip-install--strict"><a href="#uv-pip-install--strict"><code>--strict</code></a></dt><dd><p>安装完成后验证 Python 环境，检测包含缺失依赖或其他问题的包</p>
</dd><dt id="uv-pip-install--system"><a href="#uv-pip-install--system"><code>--system</code></a></dt><dd><p>Install packages into the system Python environment.</p>
<p>默认情况下，uv 安装到当前工作目录或任何父目录中的虚拟环境。<code>--system</code> 选项指示 uv 改为使用系统 <code>PATH</code> 中找到的第一个 Python。</p>
<p>警告：<code>--system</code> 旨在用于持续集成（CI）环境中，应谨慎使用，因为它可能会修改系统 Python 安装。</p>
<p>May also be set with the <code>UV_SYSTEM_PYTHON</code> environment variable.</p></dd><dt id="uv-pip-install--system-certs"><a href="#uv-pip-install--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能需要使用平台的原生证书存储，特别是当您依赖系统证书存储中包含的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-pip-install--target"><a href="#uv-pip-install--target"><code>--target</code></a>, <code>-t</code> <i>target</i></dt><dd><p>Install packages into the specified directory, rather than into the virtual or system Python environment. The packages will be installed at the top-level of the directory.</p>
<p>与其他安装操作不同，此命令不需要发现现有 Python 环境，仅搜索用于包解析的 Python 解释器。如果找不到合适的 Python 解释器，uv 将安装一个。要禁用此行为，请添加 <code>--no-python-downloads</code>。</p>
</dd><dt id="uv-pip-install--torch-backend"><a href="#uv-pip-install--torch-backend"><code>--torch-backend</code></a> <i>torch-backend</i></dt><dd><p>获取 PyTorch 生态系统中软件包时使用的后端（例如，<code>cpu</code>、<code>cu126</code> 或 <code>auto</code>）</p>
<p>设置后，uv 将忽略为 PyTorch 生态系统中的包配置的索引 URL，而改用定义的后端。</p>
<p>For example, when set to <code>cpu</code>, uv will use the CPU-only PyTorch index; when set to <code>cu126</code>, uv will use the PyTorch index for CUDA 12.6.</p>
<p><code>auto</code> 模式将尝试根据当前安装的 CUDA 驱动程序检测适当的 PyTorch 索引。</p>
<p>此选项为预览功能，可能在未来的任何版本中发生变化。</p>
<p>May also be set with the <code>UV_TORCH_BACKEND</code> environment variable.</p><p>可选值：</p>
<ul>
<li><code>auto</code>:  Select the appropriate PyTorch index based on the operating system and CUDA driver version</li>
<li><code>cpu</code>:  Use the CPU-only PyTorch index</li>
<li><code>cu130</code>:  Use the PyTorch index for CUDA 13.0</li>
<li><code>cu129</code>:  Use the PyTorch index for CUDA 12.9</li>
<li><code>cu128</code>:  Use the PyTorch index for CUDA 12.8</li>
<li><code>cu126</code>:  Use the PyTorch index for CUDA 12.6</li>
<li><code>cu125</code>:  Use the PyTorch index for CUDA 12.5</li>
<li><code>cu124</code>:  Use the PyTorch index for CUDA 12.4</li>
<li><code>cu123</code>:  Use the PyTorch index for CUDA 12.3</li>
<li><code>cu122</code>:  Use the PyTorch index for CUDA 12.2</li>
<li><code>cu121</code>:  Use the PyTorch index for CUDA 12.1</li>
<li><code>cu120</code>:  Use the PyTorch index for CUDA 12.0</li>
<li><code>cu118</code>:  Use the PyTorch index for CUDA 11.8</li>
<li><code>cu117</code>:  Use the PyTorch index for CUDA 11.7</li>
<li><code>cu116</code>:  Use the PyTorch index for CUDA 11.6</li>
<li><code>cu115</code>:  Use the PyTorch index for CUDA 11.5</li>
<li><code>cu114</code>:  Use the PyTorch index for CUDA 11.4</li>
<li><code>cu113</code>:  Use the PyTorch index for CUDA 11.3</li>
<li><code>cu112</code>:  Use the PyTorch index for CUDA 11.2</li>
<li><code>cu111</code>:  Use the PyTorch index for CUDA 11.1</li>
<li><code>cu110</code>:  Use the PyTorch index for CUDA 11.0</li>
<li><code>cu102</code>:  Use the PyTorch index for CUDA 10.2</li>
<li><code>cu101</code>:  Use the PyTorch index for CUDA 10.1</li>
<li><code>cu100</code>:  Use the PyTorch index for CUDA 10.0</li>
<li><code>cu92</code>:  Use the PyTorch index for CUDA 9.2</li>
<li><code>cu91</code>:  Use the PyTorch index for CUDA 9.1</li>
<li><code>cu90</code>:  Use the PyTorch index for CUDA 9.0</li>
<li><code>cu80</code>:  Use the PyTorch index for CUDA 8.0</li>
<li><code>rocm7.2</code>:  Use the PyTorch index for ROCm 7.2</li>
<li><code>rocm7.1</code>:  Use the PyTorch index for ROCm 7.1</li>
<li><code>rocm7.0</code>:  Use the PyTorch index for ROCm 7.0</li>
<li><code>rocm6.4</code>:  Use the PyTorch index for ROCm 6.4</li>
<li><code>rocm6.3</code>:  Use the PyTorch index for ROCm 6.3</li>
<li><code>rocm6.2.4</code>:  Use the PyTorch index for ROCm 6.2.4</li>
<li><code>rocm6.2</code>:  Use the PyTorch index for ROCm 6.2</li>
<li><code>rocm6.1</code>:  Use the PyTorch index for ROCm 6.1</li>
<li><code>rocm6.0</code>:  Use the PyTorch index for ROCm 6.0</li>
<li><code>rocm5.7</code>:  Use the PyTorch index for ROCm 5.7</li>
<li><code>rocm5.6</code>:  Use the PyTorch index for ROCm 5.6</li>
<li><code>rocm5.5</code>:  Use the PyTorch index for ROCm 5.5</li>
<li><code>rocm5.4.2</code>:  Use the PyTorch index for ROCm 5.4.2</li>
<li><code>rocm5.4</code>:  Use the PyTorch index for ROCm 5.4</li>
<li><code>rocm5.3</code>:  Use the PyTorch index for ROCm 5.3</li>
<li><code>rocm5.2</code>:  Use the PyTorch index for ROCm 5.2</li>
<li><code>rocm5.1.1</code>:  Use the PyTorch index for ROCm 5.1.1</li>
<li><code>rocm4.2</code>:  Use the PyTorch index for ROCm 4.2</li>
<li><code>rocm4.1</code>:  Use the PyTorch index for ROCm 4.1</li>
<li><code>rocm4.0.1</code>:  Use the PyTorch index for ROCm 4.0.1</li>
<li><code>xpu</code>:  Use the PyTorch index for Intel XPU</li>
</ul></dd><dt id="uv-pip-install--upgrade"><a href="#uv-pip-install--upgrade"><code>--upgrade</code></a>, <code>-U</code></dt><dd><p>允许包升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh</code></p>
</dd><dt id="uv-pip-install--upgrade-group"><a href="#uv-pip-install--upgrade-group"><code>--upgrade-group</code></a> <i>upgrade-group</i></dt><dd><p>Allow upgrades for all packages in a dependency group, ignoring pinned versions in any existing output file</p>
</dd><dt id="uv-pip-install--upgrade-package"><a href="#uv-pip-install--upgrade-package"><code>--upgrade-package</code></a>, <code>-P</code> <i>upgrade-package</i></dt><dd><p>允许特定包的升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-pip-install--user"><a href="#uv-pip-install--user"><code>--user</code></a></dt><dt id="uv-pip-install--verbose"><a href="#uv-pip-install--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>

## uv pip uninstall

从环境中卸载包

<h3 class="cli-reference">Usage</h3>

```
uv pip uninstall [OPTIONS] <PACKAGE|--requirements <REQUIREMENTS>>
```

<h3 class="cli-reference">Arguments</h3>

<dl class="cli-reference"><dt id="uv-pip-uninstall--package"><a href="#uv-pip-uninstall--package"><code>PACKAGE</code></a></dt><dd><p>Uninstall all listed packages</p>
</dd></dl>

<h3 class="cli-reference">Options</h3>

<dl class="cli-reference"><dt id="uv-pip-uninstall--allow-insecure-host"><a href="#uv-pip-uninstall--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机的非安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（如 <code>localhost</code>）、主机-端口对（如 <code>localhost:8080</code>）或 URL（如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您面临中间人攻击（MITM）的风险。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-pip-uninstall--break-system-packages"><a href="#uv-pip-uninstall--break-system-packages"><code>--break-system-packages</code></a></dt><dd><p>允许 uv 修改 <code>EXTERNALLY-MANAGED</code> 的 Python 安装。</p>
<p>警告：<code>--break-system-packages</code> 旨在用于持续集成（CI）环境中，当安装到由外部包管理器（如 <code>apt</code>）管理的 Python 安装中时。应谨慎使用，因为此类 Python 安装明确建议不要由其他包管理器（如 uv 或 <code>pip</code>）进行修改。</p>
<p>也可通过 <code>UV_BREAK_SYSTEM_PACKAGES</code> 环境变量设置。</p></dd><dt id="uv-pip-uninstall--cache-dir"><a href="#uv-pip-uninstall--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>默认值为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>（macOS 和 Linux），以及 <code>%LOCALAPPDATA%\uv\cache</code>（Windows）。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-pip-uninstall--color"><a href="#uv-pip-uninstall--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 在写入终端时会自动检测颜色支持。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>:  仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>:  无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>:  禁用彩色输出</li>
</ul></dd><dt id="uv-pip-uninstall--config-file"><a href="#uv-pip-uninstall--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-pip-uninstall--directory"><a href="#uv-pip-uninstall--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径将以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-pip-uninstall--dry-run"><a href="#uv-pip-uninstall--dry-run"><code>--dry-run</code></a></dt><dd><p>Perform a dry run, i.e., don't actually uninstall anything but print the resulting plan</p>
</dd><dt id="uv-pip-uninstall--help"><a href="#uv-pip-uninstall--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简洁帮助信息</p>
</dd><dt id="uv-pip-uninstall--keyring-provider"><a href="#uv-pip-uninstall--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>Attempt to use <code>keyring</code> for authentication for remote requirements files.</p>
<p>目前仅支持 <code>--keyring-provider subprocess</code>，该选项配置 uv 使用 <code>keyring</code> CLI 来处理身份验证。</p>
<p>默认为 <code>disabled</code>。</p>
<p>也可通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disabled</code>:  不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>:  使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-pip-uninstall--managed-python"><a href="#uv-pip-uninstall--managed-python"><code>--managed-python</code></a></dt><dd><p>Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果没有安装 uv 管理的 Python 版本，则会使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-pip-uninstall--no-break-system-packages"><a href="#uv-pip-uninstall--no-break-system-packages"><code>--no-break-system-packages</code></a></dt><dt id="uv-pip-uninstall--no-cache"><a href="#uv-pip-uninstall--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-pip-uninstall--no-config"><a href="#uv-pip-uninstall--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常情况下，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-pip-uninstall--no-managed-python"><a href="#uv-pip-uninstall--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用使用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>uv 将改为在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-pip-uninstall--no-progress"><a href="#uv-pip-uninstall--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，spinner 或进度条。</p>
</dd><dt id="uv-pip-uninstall--no-python-downloads"><a href="#uv-pip-uninstall--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用自动下载 Python。</p>
</dd><dt id="uv-pip-uninstall--offline"><a href="#uv-pip-uninstall--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-pip-uninstall--prefix"><a href="#uv-pip-uninstall--prefix"><code>--prefix</code></a> <i>prefix</i></dt><dd><p>Uninstall packages from the specified <code>--prefix</code> directory</p>
</dd><dt id="uv-pip-uninstall--project"><a href="#uv-pip-uninstall--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-pip-uninstall--python"><a href="#uv-pip-uninstall--python"><code>--python</code></a>, <code>-p</code> <i>python</i></dt><dd><p>The Python interpreter from which packages should be uninstalled.</p>
<p>By default, uninstallation requires a virtual environment. A path to an alternative Python
can be provided, but it is only recommended in continuous integration (CI) environments and
should be used with caution, as it can modify the system Python installation.</p>
<p>参见 <a href="#uv-python">uv python</a> 了解 Python 发现机制和支持的请求格式的详细信息。</p>
<p>May also be set with the <code>UV_PYTHON</code> environment variable.</p></dd><dt id="uv-pip-uninstall--quiet"><a href="#uv-pip-uninstall--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项（如 <code>-qq</code>）将启用静默模式，uv 将不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-pip-uninstall--requirements"><a href="#uv-pip-uninstall--requirements"><code>--requirements</code></a>, <code>--requirement</code>, <code>-r</code> <i>requirements</i></dt><dd><p>Uninstall the packages listed in the given files.</p>
<p>支持以下格式：<code>requirements.txt</code>、包含内联元数据的 <code>.py</code> 文件、<code>pylock.toml</code>、<code>pyproject.toml</code>、<code>setup.py</code> 和 <code>setup.cfg</code>。</p>
</dd><dt id="uv-pip-uninstall--system"><a href="#uv-pip-uninstall--system"><code>--system</code></a></dt><dd><p>使用系统 Python 来卸载包。</p>
<p>默认情况下，uv 从当前工作目录或任何父目录中的虚拟环境卸载包。<code>--system</code> 选项指示 uv 改为使用系统 <code>PATH</code> 中找到的第一个 Python。</p>
<p>警告：<code>--system</code> 旨在用于持续集成（CI）环境中，应谨慎使用，因为它可能会修改系统 Python 安装。</p>
<p>May also be set with the <code>UV_SYSTEM_PYTHON</code> environment variable.</p></dd><dt id="uv-pip-uninstall--system-certs"><a href="#uv-pip-uninstall--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能需要使用平台的原生证书存储，特别是当您依赖系统证书存储中包含的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-pip-uninstall--target"><a href="#uv-pip-uninstall--target"><code>--target</code></a>, <code>-t</code> <i>target</i></dt><dd><p>Uninstall packages from the specified <code>--target</code> directory</p>
</dd><dt id="uv-pip-uninstall--verbose"><a href="#uv-pip-uninstall--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>

## uv pip freeze

以 requirements 格式列出环境中已安装的包

<h3 class="cli-reference">Usage</h3>

```
uv pip freeze [OPTIONS]
```

<h3 class="cli-reference">Options</h3>

<dl class="cli-reference"><dt id="uv-pip-freeze--allow-insecure-host"><a href="#uv-pip-freeze--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机的非安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（如 <code>localhost</code>）、主机-端口对（如 <code>localhost:8080</code>）或 URL（如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您面临中间人攻击（MITM）的风险。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-pip-freeze--cache-dir"><a href="#uv-pip-freeze--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>默认值为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>（macOS 和 Linux），以及 <code>%LOCALAPPDATA%\uv\cache</code>（Windows）。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-pip-freeze--color"><a href="#uv-pip-freeze--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 在写入终端时会自动检测颜色支持。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>:  仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>:  无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>:  禁用彩色输出</li>
</ul></dd><dt id="uv-pip-freeze--config-file"><a href="#uv-pip-freeze--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-pip-freeze--directory"><a href="#uv-pip-freeze--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径将以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-pip-freeze--exclude"><a href="#uv-pip-freeze--exclude"><code>--exclude</code></a> <i>exclude</i></dt><dd><p>Exclude the specified package(s) from the output</p>
</dd><dt id="uv-pip-freeze--exclude-editable"><a href="#uv-pip-freeze--exclude-editable"><code>--exclude-editable</code></a></dt><dd><p>Exclude any editable packages from output</p>
</dd><dt id="uv-pip-freeze--help"><a href="#uv-pip-freeze--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简洁帮助信息</p>
</dd><dt id="uv-pip-freeze--managed-python"><a href="#uv-pip-freeze--managed-python"><code>--managed-python</code></a></dt><dd><p>Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果没有安装 uv 管理的 Python 版本，则会使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-pip-freeze--no-cache"><a href="#uv-pip-freeze--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-pip-freeze--no-config"><a href="#uv-pip-freeze--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常情况下，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-pip-freeze--no-managed-python"><a href="#uv-pip-freeze--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用使用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>uv 将改为在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-pip-freeze--no-progress"><a href="#uv-pip-freeze--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，spinner 或进度条。</p>
</dd><dt id="uv-pip-freeze--no-python-downloads"><a href="#uv-pip-freeze--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用自动下载 Python。</p>
</dd><dt id="uv-pip-freeze--offline"><a href="#uv-pip-freeze--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-pip-freeze--path"><a href="#uv-pip-freeze--path"><code>--path</code></a> <i>paths</i></dt><dd><p>Restrict to the specified installation path for listing packages (can be used multiple times)</p>
</dd><dt id="uv-pip-freeze--prefix"><a href="#uv-pip-freeze--prefix"><code>--prefix</code></a> <i>prefix</i></dt><dd><p>List packages from the specified <code>--prefix</code> directory</p>
</dd><dt id="uv-pip-freeze--project"><a href="#uv-pip-freeze--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-pip-freeze--python"><a href="#uv-pip-freeze--python"><code>--python</code></a>, <code>-p</code> <i>python</i></dt><dd><p>The Python interpreter for which packages should be listed.</p>
<p>By default, uv lists packages in a virtual environment but will show packages in a system
Python environment if no virtual environment is found.</p>
<p>参见 <a href="#uv-python">uv python</a> 了解 Python 发现机制和支持的请求格式的详细信息。</p>
<p>May also be set with the <code>UV_PYTHON</code> environment variable.</p></dd><dt id="uv-pip-freeze--quiet"><a href="#uv-pip-freeze--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项（如 <code>-qq</code>）将启用静默模式，uv 将不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-pip-freeze--strict"><a href="#uv-pip-freeze--strict"><code>--strict</code></a></dt><dd><p>Validate the Python environment, to detect packages with missing dependencies and other issues</p>
</dd><dt id="uv-pip-freeze--system"><a href="#uv-pip-freeze--system"><code>--system</code></a></dt><dd><p>List packages in the system Python environment.</p>
<p>禁用虚拟环境的发现。</p>
<p>参见 <a href="#uv-python">uv python</a> 了解 Python 发现机制的详细信息。</p>
<p>May also be set with the <code>UV_SYSTEM_PYTHON</code> environment variable.</p></dd><dt id="uv-pip-freeze--system-certs"><a href="#uv-pip-freeze--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能需要使用平台的原生证书存储，特别是当您依赖系统证书存储中包含的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-pip-freeze--target"><a href="#uv-pip-freeze--target"><code>--target</code></a>, <code>-t</code> <i>target</i></dt><dd><p>List packages from the specified <code>--target</code> directory</p>
</dd><dt id="uv-pip-freeze--verbose"><a href="#uv-pip-freeze--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>

## uv pip list

以表格格式列出环境中已安装的包

<h3 class="cli-reference">Usage</h3>

```
uv pip list [OPTIONS]
```

<h3 class="cli-reference">Options</h3>

<dl class="cli-reference"><dt id="uv-pip-list--allow-insecure-host"><a href="#uv-pip-list--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机的非安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（如 <code>localhost</code>）、主机-端口对（如 <code>localhost:8080</code>）或 URL（如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您面临中间人攻击（MITM）的风险。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-pip-list--cache-dir"><a href="#uv-pip-list--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>默认值为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>（macOS 和 Linux），以及 <code>%LOCALAPPDATA%\uv\cache</code>（Windows）。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-pip-list--color"><a href="#uv-pip-list--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 在写入终端时会自动检测颜色支持。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>:  仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>:  无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>:  禁用彩色输出</li>
</ul></dd><dt id="uv-pip-list--config-file"><a href="#uv-pip-list--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-pip-list--default-index"><a href="#uv-pip-list--default-index"><code>--default-index</code></a> <i>default-index</i></dt><dd><p>默认包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志指定的索引优先级低于通过 <code>--index</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_DEFAULT_INDEX</code> 环境变量设置。</p></dd><dt id="uv-pip-list--directory"><a href="#uv-pip-list--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径将以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-pip-list--editable"><a href="#uv-pip-list--editable"><code>--editable</code></a>, <code>-e</code></dt><dd><p>Only include editable projects</p>
</dd><dt id="uv-pip-list--exclude"><a href="#uv-pip-list--exclude"><code>--exclude</code></a> <i>exclude</i></dt><dd><p>Exclude the specified package(s) from the output</p>
</dd><dt id="uv-pip-list--exclude-editable"><a href="#uv-pip-list--exclude-editable"><code>--exclude-editable</code></a></dt><dd><p>Exclude any editable packages from output</p>
</dd><dt id="uv-pip-list--exclude-newer"><a href="#uv-pip-list--exclude-newer"><code>--exclude-newer</code></a> <i>exclude-newer</i></dt><dd><p>将候选包限制为在给定日期之前上传的版本。</p>
<p>日期与每个单独分发制品（distribution artifact）的上传时间（即每个文件上传到包索引的时间）进行比较，而非包版本的发布日期。</p>
<p>接受 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、相同格式的本地日期（例如 <code>2006-12-02</code>，基于系统配置的时区解析）、"友好"持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不遵循本地时区语义，始终按固定秒数计算，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月和年等日历单位。</p>
<p>也可通过 <code>UV_EXCLUDE_NEWER</code> 环境变量设置。</p></dd><dt id="uv-pip-list--extra-index-url"><a href="#uv-pip-list--extra-index-url"><code>--extra-index-url</code></a> <i>extra-index-url</i></dt><dd><p>（已弃用：请改用 <code>--index</code>）除 <code>--index-url</code> 之外要使用的额外包索引 URL。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于由 <code>--index-url</code> 指定的索引（默认为 PyPI）。当提供多个 <code>--extra-index-url</code> 标志时，优先级按先后顺序递减。</p>
<p>也可通过 <code>UV_EXTRA_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-pip-list--find-links"><a href="#uv-pip-list--find-links"><code>--find-links</code></a>, <code>-f</code> <i>find-links</i></dt><dd><p>在注册表索引之外，搜索候选分发包的额外位置。</p>
<p>如果提供的是路径，目标必须是一个目录，其顶层包含作为 wheel 文件（<code>.whl</code>）或源代码分发包（例如 <code>.tar.gz</code> 或 <code>.zip</code>）的包。</p>
<p>如果提供的是 URL，页面必须包含一个扁平列表，其中包含符合上述格式的包文件链接。</p>
<p>也可通过 <code>UV_FIND_LINKS</code> 环境变量设置。</p></dd><dt id="uv-pip-list--format"><a href="#uv-pip-list--format"><code>--format</code></a> <i>format</i></dt><dd><p>Select the output format</p>
<p>[default: columns]</p><p>可选值：</p>
<ul>
<li><code>columns</code>:  Display the list of packages in a human-readable table</li>
<li><code>freeze</code>:  Display the list of packages in a <code>pip freeze</code>-like format, with one package per line alongside its version</li>
<li><code>json</code>:  Display the list of packages in a machine-readable JSON format</li>
</ul></dd><dt id="uv-pip-list--help"><a href="#uv-pip-list--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简洁帮助信息</p>
</dd><dt id="uv-pip-list--index"><a href="#uv-pip-list--index"><code>--index</code></a> <i>index</i></dt><dd><p>解析依赖时使用的 URL，作为默认索引的补充。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于由 <code>--default-index</code> 指定的索引（默认为 PyPI）。当提供多个 <code>--index</code> 标志时，优先级按先后顺序递减。</p>
<p>不支持将索引名称作为值。相对路径必须通过 <code>./</code> 或 <code>../</code>（Unix 上）或 <code>.\\</code>、<code>..\\</code>、<code>./</code> 或 <code>../</code>（Windows 上）与索引名称进行区分。</p>
<p>也可通过 <code>UV_INDEX</code> 环境变量设置。</p></dd><dt id="uv-pip-list--index-strategy"><a href="#uv-pip-list--index-strategy"><code>--index-strategy</code></a> <i>index-strategy</i></dt><dd><p>针对多个索引 URL 进行解析时使用的策略。</p>
<p>默认情况下，uv 会在第一个包含给定包的索引处停止，并将解析范围限制为在该第一个索引（<code>first-index</code>）中存在的包。这可以防止"依赖混淆"攻击，即攻击者可以在备用索引上以相同名称上传恶意包。</p>
<p>也可通过 <code>UV_INDEX_STRATEGY</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>first-index</code>:  仅使用第一个返回给定包名匹配的索引的结果</li>
<li><code>unsafe-first-match</code>:  搜索所有索引中的每个包名，在切换到下一个索引之前耗尽第一个索引的版本</li>
<li><code>unsafe-best-match</code>:  搜索所有索引中的每个包名，优先选择找到的"最佳"版本。如果一个包版本存在于多个索引中，则仅查看第一个索引的条目</li>
</ul></dd><dt id="uv-pip-list--index-url"><a href="#uv-pip-list--index-url"><code>--index-url</code></a>, <code>-i</code> <i>index-url</i></dt><dd><p>（已弃用：请改用 <code>--default-index</code>）Python 包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志指定的索引优先级低于通过 <code>--extra-index-url</code> 标志指定的所有其他索引。</p>
<p>也可通过 <code>UV_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-pip-list--keyring-provider"><a href="#uv-pip-list--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>尝试使用 <code>keyring</code> 对索引 URL 进行身份验证。</p>
<p>目前仅支持 <code>--keyring-provider subprocess</code>，该选项配置 uv 使用 <code>keyring</code> CLI 来处理身份验证。</p>
<p>默认为 <code>disabled</code>。</p>
<p>也可通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disabled</code>:  不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>:  使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-pip-list--managed-python"><a href="#uv-pip-list--managed-python"><code>--managed-python</code></a></dt><dd><p>Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果没有安装 uv 管理的 Python 版本，则会使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-pip-list--no-cache"><a href="#uv-pip-list--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-pip-list--no-config"><a href="#uv-pip-list--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常情况下，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-pip-list--no-index"><a href="#uv-pip-list--no-index"><code>--no-index</code></a></dt><dd><p>忽略注册表索引（例如 PyPI），转而依赖直接 URL 依赖和通过 <code>--find-links</code> 提供的依赖</p>
</dd><dt id="uv-pip-list--no-managed-python"><a href="#uv-pip-list--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用使用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>uv 将改为在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-pip-list--no-progress"><a href="#uv-pip-list--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，spinner 或进度条。</p>
</dd><dt id="uv-pip-list--no-python-downloads"><a href="#uv-pip-list--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用自动下载 Python。</p>
</dd><dt id="uv-pip-list--offline"><a href="#uv-pip-list--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-pip-list--outdated"><a href="#uv-pip-list--outdated"><code>--outdated</code></a></dt><dd><p>List outdated packages.</p>
<p>每个包的最新版本将与已安装版本并排显示。已是最新版本的包将从输出中省略。</p>
</dd><dt id="uv-pip-list--prefix"><a href="#uv-pip-list--prefix"><code>--prefix</code></a> <i>prefix</i></dt><dd><p>List packages from the specified <code>--prefix</code> directory</p>
</dd><dt id="uv-pip-list--project"><a href="#uv-pip-list--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-pip-list--python"><a href="#uv-pip-list--python"><code>--python</code></a>, <code>-p</code> <i>python</i></dt><dd><p>The Python interpreter for which packages should be listed.</p>
<p>By default, uv lists packages in a virtual environment but will show packages in a system
Python environment if no virtual environment is found.</p>
<p>参见 <a href="#uv-python">uv python</a> 了解 Python 发现机制和支持的请求格式的详细信息。</p>
<p>May also be set with the <code>UV_PYTHON</code> environment variable.</p></dd><dt id="uv-pip-list--quiet"><a href="#uv-pip-list--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项（如 <code>-qq</code>）将启用静默模式，uv 将不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-pip-list--strict"><a href="#uv-pip-list--strict"><code>--strict</code></a></dt><dd><p>Validate the Python environment, to detect packages with missing dependencies and other issues</p>
</dd><dt id="uv-pip-list--system"><a href="#uv-pip-list--system"><code>--system</code></a></dt><dd><p>List packages in the system Python environment.</p>
<p>禁用虚拟环境的发现。</p>
<p>参见 <a href="#uv-python">uv python</a> 了解 Python 发现机制的详细信息。</p>
<p>May also be set with the <code>UV_SYSTEM_PYTHON</code> environment variable.</p></dd><dt id="uv-pip-list--system-certs"><a href="#uv-pip-list--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能需要使用平台的原生证书存储，特别是当您依赖系统证书存储中包含的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-pip-list--target"><a href="#uv-pip-list--target"><code>--target</code></a>, <code>-t</code> <i>target</i></dt><dd><p>List packages from the specified <code>--target</code> directory</p>
</dd><dt id="uv-pip-list--verbose"><a href="#uv-pip-list--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>

## uv pip show

显示一个或多个已安装包的信息

<h3 class="cli-reference">Usage</h3>

```
uv pip show [OPTIONS] [PACKAGE]...
```

<h3 class="cli-reference">Arguments</h3>

<dl class="cli-reference"><dt id="uv-pip-show--package"><a href="#uv-pip-show--package"><code>PACKAGE</code></a></dt><dd><p>The package(s) to display</p>
</dd></dl>

<h3 class="cli-reference">Options</h3>

<dl class="cli-reference"><dt id="uv-pip-show--allow-insecure-host"><a href="#uv-pip-show--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机的非安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（如 <code>localhost</code>）、主机-端口对（如 <code>localhost:8080</code>）或 URL（如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您面临中间人攻击（MITM）的风险。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-pip-show--cache-dir"><a href="#uv-pip-show--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>默认值为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>（macOS 和 Linux），以及 <code>%LOCALAPPDATA%\uv\cache</code>（Windows）。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-pip-show--color"><a href="#uv-pip-show--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 在写入终端时会自动检测颜色支持。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>:  仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>:  无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>:  禁用彩色输出</li>
</ul></dd><dt id="uv-pip-show--config-file"><a href="#uv-pip-show--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-pip-show--directory"><a href="#uv-pip-show--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径将以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-pip-show--files"><a href="#uv-pip-show--files"><code>--files</code></a>, <code>-f</code></dt><dd><p>Show the full list of installed files for each package</p>
</dd><dt id="uv-pip-show--help"><a href="#uv-pip-show--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简洁帮助信息</p>
</dd><dt id="uv-pip-show--managed-python"><a href="#uv-pip-show--managed-python"><code>--managed-python</code></a></dt><dd><p>Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果没有安装 uv 管理的 Python 版本，则会使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-pip-show--no-cache"><a href="#uv-pip-show--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-pip-show--no-config"><a href="#uv-pip-show--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常情况下，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-pip-show--no-managed-python"><a href="#uv-pip-show--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用使用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>uv 将改为在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-pip-show--no-progress"><a href="#uv-pip-show--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，spinner 或进度条。</p>
</dd><dt id="uv-pip-show--no-python-downloads"><a href="#uv-pip-show--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用自动下载 Python。</p>
</dd><dt id="uv-pip-show--offline"><a href="#uv-pip-show--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-pip-show--prefix"><a href="#uv-pip-show--prefix"><code>--prefix</code></a> <i>prefix</i></dt><dd><p>Show a package from the specified <code>--prefix</code> directory</p>
</dd><dt id="uv-pip-show--project"><a href="#uv-pip-show--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-pip-show--python"><a href="#uv-pip-show--python"><code>--python</code></a>, <code>-p</code> <i>python</i></dt><dd><p>The Python interpreter to find the package in.</p>
<p>By default, uv looks for packages in a virtual environment but will look for packages in a
system Python environment if no virtual environment is found.</p>
<p>参见 <a href="#uv-python">uv python</a> 了解 Python 发现机制和支持的请求格式的详细信息。</p>
<p>May also be set with the <code>UV_PYTHON</code> environment variable.</p></dd><dt id="uv-pip-show--quiet"><a href="#uv-pip-show--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项（如 <code>-qq</code>）将启用静默模式，uv 将不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-pip-show--strict"><a href="#uv-pip-show--strict"><code>--strict</code></a></dt><dd><p>Validate the Python environment, to detect packages with missing dependencies and other issues</p>
</dd><dt id="uv-pip-show--system"><a href="#uv-pip-show--system"><code>--system</code></a></dt><dd><p>Show a package in the system Python environment.</p>
<p>禁用虚拟环境的发现。</p>
<p>参见 <a href="#uv-python">uv python</a> 了解 Python 发现机制的详细信息。</p>
<p>May also be set with the <code>UV_SYSTEM_PYTHON</code> environment variable.</p></dd><dt id="uv-pip-show--system-certs"><a href="#uv-pip-show--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能需要使用平台的原生证书存储，特别是当您依赖系统证书存储中包含的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-pip-show--target"><a href="#uv-pip-show--target"><code>--target</code></a>, <code>-t</code> <i>target</i></dt><dd><p>Show a package from the specified <code>--target</code> directory</p>
</dd><dt id="uv-pip-show--verbose"><a href="#uv-pip-show--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>

## uv pip tree

显示环境的依赖树

<h3 class="cli-reference">Usage</h3>

```
uv pip tree [OPTIONS]
```

<h3 class="cli-reference">Options</h3>

<dl class="cli-reference"><dt id="uv-pip-tree--allow-insecure-host"><a href="#uv-pip-tree--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机的非安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（如 <code>localhost</code>）、主机-端口对（如 <code>localhost:8080</code>）或 URL（如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您面临中间人攻击（MITM）的风险。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-pip-tree--cache-dir"><a href="#uv-pip-tree--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>默认值为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>（macOS 和 Linux），以及 <code>%LOCALAPPDATA%\uv\cache</code>（Windows）。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-pip-tree--color"><a href="#uv-pip-tree--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 在写入终端时会自动检测颜色支持。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>:  仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>:  无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>:  禁用彩色输出</li>
</ul></dd><dt id="uv-pip-tree--config-file"><a href="#uv-pip-tree--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-pip-tree--default-index"><a href="#uv-pip-tree--default-index"><code>--default-index</code></a> <i>default-index</i></dt><dd><p>默认包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志指定的索引优先级低于通过 <code>--index</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_DEFAULT_INDEX</code> 环境变量设置。</p></dd><dt id="uv-pip-tree--depth"><a href="#uv-pip-tree--depth"><code>--depth</code></a>, <code>-d</code> <i>depth</i></dt><dd><p>Maximum display depth of the dependency tree</p>
<p>[default: 255]</p></dd><dt id="uv-pip-tree--directory"><a href="#uv-pip-tree--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径将以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-pip-tree--exclude-newer"><a href="#uv-pip-tree--exclude-newer"><code>--exclude-newer</code></a> <i>exclude-newer</i></dt><dd><p>将候选包限制为在给定日期之前上传的版本。</p>
<p>日期与每个单独分发制品（distribution artifact）的上传时间（即每个文件上传到包索引的时间）进行比较，而非包版本的发布日期。</p>
<p>接受 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、相同格式的本地日期（例如 <code>2006-12-02</code>，基于系统配置的时区解析）、"友好"持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不遵循本地时区语义，始终按固定秒数计算，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月和年等日历单位。</p>
<p>也可通过 <code>UV_EXCLUDE_NEWER</code> 环境变量设置。</p></dd><dt id="uv-pip-tree--extra-index-url"><a href="#uv-pip-tree--extra-index-url"><code>--extra-index-url</code></a> <i>extra-index-url</i></dt><dd><p>（已弃用：请改用 <code>--index</code>）除 <code>--index-url</code> 之外要使用的额外包索引 URL。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于由 <code>--index-url</code> 指定的索引（默认为 PyPI）。当提供多个 <code>--extra-index-url</code> 标志时，优先级按先后顺序递减。</p>
<p>也可通过 <code>UV_EXTRA_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-pip-tree--find-links"><a href="#uv-pip-tree--find-links"><code>--find-links</code></a>, <code>-f</code> <i>find-links</i></dt><dd><p>在注册表索引之外，搜索候选分发包的额外位置。</p>
<p>如果提供的是路径，目标必须是一个目录，其顶层包含作为 wheel 文件（<code>.whl</code>）或源代码分发包（例如 <code>.tar.gz</code> 或 <code>.zip</code>）的包。</p>
<p>如果提供的是 URL，页面必须包含一个扁平列表，其中包含符合上述格式的包文件链接。</p>
<p>也可通过 <code>UV_FIND_LINKS</code> 环境变量设置。</p></dd><dt id="uv-pip-tree--help"><a href="#uv-pip-tree--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简洁帮助信息</p>
</dd><dt id="uv-pip-tree--index"><a href="#uv-pip-tree--index"><code>--index</code></a> <i>index</i></dt><dd><p>解析依赖时使用的 URL，作为默认索引的补充。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于由 <code>--default-index</code> 指定的索引（默认为 PyPI）。当提供多个 <code>--index</code> 标志时，优先级按先后顺序递减。</p>
<p>不支持将索引名称作为值。相对路径必须通过 <code>./</code> 或 <code>../</code>（Unix 上）或 <code>.\\</code>、<code>..\\</code>、<code>./</code> 或 <code>../</code>（Windows 上）与索引名称进行区分。</p>
<p>也可通过 <code>UV_INDEX</code> 环境变量设置。</p></dd><dt id="uv-pip-tree--index-strategy"><a href="#uv-pip-tree--index-strategy"><code>--index-strategy</code></a> <i>index-strategy</i></dt><dd><p>针对多个索引 URL 进行解析时使用的策略。</p>
<p>默认情况下，uv 会在第一个包含给定包的索引处停止，并将解析范围限制为在该第一个索引（<code>first-index</code>）中存在的包。这可以防止"依赖混淆"攻击，即攻击者可以在备用索引上以相同名称上传恶意包。</p>
<p>也可通过 <code>UV_INDEX_STRATEGY</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>first-index</code>:  仅使用第一个返回给定包名匹配的索引的结果</li>
<li><code>unsafe-first-match</code>:  搜索所有索引中的每个包名，在切换到下一个索引之前耗尽第一个索引的版本</li>
<li><code>unsafe-best-match</code>:  搜索所有索引中的每个包名，优先选择找到的"最佳"版本。如果一个包版本存在于多个索引中，则仅查看第一个索引的条目</li>
</ul></dd><dt id="uv-pip-tree--index-url"><a href="#uv-pip-tree--index-url"><code>--index-url</code></a>, <code>-i</code> <i>index-url</i></dt><dd><p>（已弃用：请改用 <code>--default-index</code>）Python 包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志指定的索引优先级低于通过 <code>--extra-index-url</code> 标志指定的所有其他索引。</p>
<p>也可通过 <code>UV_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-pip-tree--invert"><a href="#uv-pip-tree--invert"><code>--invert</code></a>, <code>--reverse</code></dt><dd><p>Show the reverse dependencies for the given package. This flag will invert the tree and display the packages that depend on the given package</p>
</dd><dt id="uv-pip-tree--keyring-provider"><a href="#uv-pip-tree--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>尝试使用 <code>keyring</code> 对索引 URL 进行身份验证。</p>
<p>目前仅支持 <code>--keyring-provider subprocess</code>，该选项配置 uv 使用 <code>keyring</code> CLI 来处理身份验证。</p>
<p>默认为 <code>disabled</code>。</p>
<p>也可通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disabled</code>:  不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>:  使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-pip-tree--managed-python"><a href="#uv-pip-tree--managed-python"><code>--managed-python</code></a></dt><dd><p>Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果没有安装 uv 管理的 Python 版本，则会使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-pip-tree--no-cache"><a href="#uv-pip-tree--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-pip-tree--no-config"><a href="#uv-pip-tree--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常情况下，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-pip-tree--no-dedupe"><a href="#uv-pip-tree--no-dedupe"><code>--no-dedupe</code></a></dt><dd><p>Do not de-duplicate repeated dependencies. Usually, when a package has already displayed its dependencies, further occurrences will not re-display its dependencies, and will include a (*) to indicate it has already been shown. This flag will cause those duplicates to be repeated</p>
</dd><dt id="uv-pip-tree--no-index"><a href="#uv-pip-tree--no-index"><code>--no-index</code></a></dt><dd><p>忽略注册表索引（例如 PyPI），转而依赖直接 URL 依赖和通过 <code>--find-links</code> 提供的依赖</p>
</dd><dt id="uv-pip-tree--no-managed-python"><a href="#uv-pip-tree--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用使用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>uv 将改为在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-pip-tree--no-progress"><a href="#uv-pip-tree--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，spinner 或进度条。</p>
</dd><dt id="uv-pip-tree--no-python-downloads"><a href="#uv-pip-tree--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用自动下载 Python。</p>
</dd><dt id="uv-pip-tree--offline"><a href="#uv-pip-tree--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-pip-tree--outdated"><a href="#uv-pip-tree--outdated"><code>--outdated</code></a></dt><dd><p>Show the latest available version of each package in the tree</p>
</dd><dt id="uv-pip-tree--package"><a href="#uv-pip-tree--package"><code>--package</code></a> <i>package</i></dt><dd><p>Display only the specified packages</p>
</dd><dt id="uv-pip-tree--project"><a href="#uv-pip-tree--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-pip-tree--prune"><a href="#uv-pip-tree--prune"><code>--prune</code></a> <i>prune</i></dt><dd><p>Prune the given package from the display of the dependency tree</p>
</dd><dt id="uv-pip-tree--python"><a href="#uv-pip-tree--python"><code>--python</code></a>, <code>-p</code> <i>python</i></dt><dd><p>The Python interpreter for which packages should be listed.</p>
<p>By default, uv lists packages in a virtual environment but will show packages in a system
Python environment if no virtual environment is found.</p>
<p>参见 <a href="#uv-python">uv python</a> 了解 Python 发现机制和支持的请求格式的详细信息。</p>
<p>May also be set with the <code>UV_PYTHON</code> environment variable.</p></dd><dt id="uv-pip-tree--quiet"><a href="#uv-pip-tree--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项（如 <code>-qq</code>）将启用静默模式，uv 将不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-pip-tree--show-sizes"><a href="#uv-pip-tree--show-sizes"><code>--show-sizes</code></a></dt><dd><p>Show compressed wheel sizes for packages in the tree</p>
</dd><dt id="uv-pip-tree--show-version-specifiers"><a href="#uv-pip-tree--show-version-specifiers"><code>--show-version-specifiers</code></a></dt><dd><p>Show the version constraint(s) imposed on each package</p>
</dd><dt id="uv-pip-tree--strict"><a href="#uv-pip-tree--strict"><code>--strict</code></a></dt><dd><p>Validate the Python environment, to detect packages with missing dependencies and other issues</p>
</dd><dt id="uv-pip-tree--system"><a href="#uv-pip-tree--system"><code>--system</code></a></dt><dd><p>List packages in the system Python environment.</p>
<p>禁用虚拟环境的发现。</p>
<p>参见 <a href="#uv-python">uv python</a> 了解 Python 发现机制的详细信息。</p>
<p>May also be set with the <code>UV_SYSTEM_PYTHON</code> environment variable.</p></dd><dt id="uv-pip-tree--system-certs"><a href="#uv-pip-tree--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能需要使用平台的原生证书存储，特别是当您依赖系统证书存储中包含的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-pip-tree--verbose"><a href="#uv-pip-tree--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>

## uv pip check

验证已安装的包是否具有兼容的依赖

<h3 class="cli-reference">Usage</h3>

```
uv pip check [OPTIONS]
```

<h3 class="cli-reference">Options</h3>

<dl class="cli-reference"><dt id="uv-pip-check--allow-insecure-host"><a href="#uv-pip-check--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机的非安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（如 <code>localhost</code>）、主机-端口对（如 <code>localhost:8080</code>）或 URL（如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您面临中间人攻击（MITM）的风险。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-pip-check--cache-dir"><a href="#uv-pip-check--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>默认值为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>（macOS 和 Linux），以及 <code>%LOCALAPPDATA%\uv\cache</code>（Windows）。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-pip-check--color"><a href="#uv-pip-check--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 在写入终端时会自动检测颜色支持。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>:  仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>:  无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>:  禁用彩色输出</li>
</ul></dd><dt id="uv-pip-check--config-file"><a href="#uv-pip-check--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-pip-check--directory"><a href="#uv-pip-check--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径将以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-pip-check--help"><a href="#uv-pip-check--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简洁帮助信息</p>
</dd><dt id="uv-pip-check--managed-python"><a href="#uv-pip-check--managed-python"><code>--managed-python</code></a></dt><dd><p>Require use of uv-managed Python versions [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果没有安装 uv 管理的 Python 版本，则会使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-pip-check--no-cache"><a href="#uv-pip-check--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-pip-check--no-config"><a href="#uv-pip-check--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常情况下，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-pip-check--no-managed-python"><a href="#uv-pip-check--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用使用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>uv 将改为在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-pip-check--no-progress"><a href="#uv-pip-check--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，spinner 或进度条。</p>
</dd><dt id="uv-pip-check--no-python-downloads"><a href="#uv-pip-check--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用自动下载 Python。</p>
</dd><dt id="uv-pip-check--offline"><a href="#uv-pip-check--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-pip-check--project"><a href="#uv-pip-check--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-pip-check--python"><a href="#uv-pip-check--python"><code>--python</code></a>, <code>-p</code> <i>python</i></dt><dd><p>The Python interpreter for which packages should be checked.</p>
<p>By default, uv checks packages in a virtual environment but will check packages in a system
Python environment if no virtual environment is found.</p>
<p>参见 <a href="#uv-python">uv python</a> 了解 Python 发现机制和支持的请求格式的详细信息。</p>
<p>May also be set with the <code>UV_PYTHON</code> environment variable.</p></dd><dt id="uv-pip-check--python-platform"><a href="#uv-pip-check--python-platform"><code>--python-platform</code></a> <i>python-platform</i></dt><dd><p>The platform for which packages should be checked.</p>
<p>By default, the installed packages are checked against the platform of the current interpreter.</p>
<p>表示为"目标三元组"（target triple），一个描述目标平台的字符串，包含 CPU、供应商和操作系统名称，如 <code>x86_64-unknown-linux-gnu</code> 或 <code>aarch64-apple-darwin</code>。</p>
<p>当目标为 macOS（Darwin）时，默认最低版本为 <code>13.0</code>。使用 <code>MACOSX_DEPLOYMENT_TARGET</code> 指定不同的最低版本，例如 <code>14.0</code>。</p>
<p>当目标为 iOS 时，默认最低版本为 <code>13.0</code>。使用 <code>IPHONEOS_DEPLOYMENT_TARGET</code> 指定不同的最低版本，例如 <code>14.0</code>。</p>
<p>当目标为 Android 时，默认最低 Android API 级别为 <code>24</code>。使用 <code>ANDROID_API_LEVEL</code> 指定不同的最低版本，例如 <code>26</code>。</p>
<p>可选值：</p>
<ul>
<li><code>windows</code>:  <code>x86_64-pc-windows-msvc</code> 的别名，Windows 的默认目标</li>
<li><code>linux</code>:  <code>x86_64-unknown-linux-gnu</code> 的别名，Linux 的默认目标</li>
<li><code>macos</code>:  <code>aarch64-apple-darwin</code> 的别名，macOS 的默认目标</li>
<li><code>x86_64-pc-windows-msvc</code>:  64 位 x86 Windows 目标</li>
<li><code>aarch64-pc-windows-msvc</code>:  ARM64 Windows 目标</li>
<li><code>i686-pc-windows-msvc</code>:  32 位 x86 Windows 目标</li>
<li><code>x86_64-unknown-linux-gnu</code>:  x86 Linux 目标。等效于 <code>x86_64-manylinux_2_28</code></li>
<li><code>aarch64-apple-darwin</code>:  基于 ARM 的 macOS 目标，如 Apple Silicon 设备上所见</li>
<li><code>x86_64-apple-darwin</code>:  x86 macOS 目标</li>
<li><code>aarch64-unknown-linux-gnu</code>:  ARM64 Linux 目标。等效于 <code>aarch64-manylinux_2_28</code></li>
<li><code>aarch64-unknown-linux-musl</code>:  ARM64 Linux 目标</li>
<li><code>x86_64-unknown-linux-musl</code>:  <code>x86_64</code> Linux 目标</li>
<li><code>riscv64-unknown-linux</code>:  RISCV64 Linux 目标</li>
<li><code>x86_64-manylinux2014</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux2014</code> 平台。等效于 <code>x86_64-manylinux_2_17</code></li>
<li><code>x86_64-manylinux_2_17</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_17</code> 平台</li>
<li><code>x86_64-manylinux_2_28</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_28</code> 平台</li>
<li><code>x86_64-manylinux_2_31</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_31</code> 平台</li>
<li><code>x86_64-manylinux_2_32</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_32</code> 平台</li>
<li><code>x86_64-manylinux_2_33</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_33</code> 平台</li>
<li><code>x86_64-manylinux_2_34</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_34</code> 平台</li>
<li><code>x86_64-manylinux_2_35</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_35</code> 平台</li>
<li><code>x86_64-manylinux_2_36</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_36</code> 平台</li>
<li><code>x86_64-manylinux_2_37</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_37</code> 平台</li>
<li><code>x86_64-manylinux_2_38</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_38</code> 平台</li>
<li><code>x86_64-manylinux_2_39</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_39</code> 平台</li>
<li><code>x86_64-manylinux_2_40</code>:  <code>x86_64</code> 目标，适用于 <code>manylinux_2_40</code> 平台</li>
<li><code>aarch64-manylinux2014</code>:  ARM64 目标，适用于 <code>manylinux2014</code> 平台。等效于 <code>aarch64-manylinux_2_17</code></li>
<li><code>aarch64-manylinux_2_17</code>:  ARM64 目标，适用于 <code>manylinux_2_17</code> 平台</li>
<li><code>aarch64-manylinux_2_28</code>:  ARM64 目标，适用于 <code>manylinux_2_28</code> 平台</li>
<li><code>aarch64-manylinux_2_31</code>:  ARM64 目标，适用于 <code>manylinux_2_31</code> 平台</li>
<li><code>aarch64-manylinux_2_32</code>:  ARM64 目标，适用于 <code>manylinux_2_32</code> 平台</li>
<li><code>aarch64-manylinux_2_33</code>:  ARM64 目标，适用于 <code>manylinux_2_33</code> 平台</li>
<li><code>aarch64-manylinux_2_34</code>:  ARM64 目标，适用于 <code>manylinux_2_34</code> 平台</li>
<li><code>aarch64-manylinux_2_35</code>:  ARM64 目标，适用于 <code>manylinux_2_35</code> 平台</li>
<li><code>aarch64-manylinux_2_36</code>:  ARM64 目标，适用于 <code>manylinux_2_36</code> 平台</li>
<li><code>aarch64-manylinux_2_37</code>:  ARM64 目标，适用于 <code>manylinux_2_37</code> 平台</li>
<li><code>aarch64-manylinux_2_38</code>:  ARM64 目标，适用于 <code>manylinux_2_38</code> 平台</li>
<li><code>aarch64-manylinux_2_39</code>:  ARM64 目标，适用于 <code>manylinux_2_39</code> 平台</li>
<li><code>aarch64-manylinux_2_40</code>:  ARM64 目标，适用于 <code>manylinux_2_40</code> 平台</li>
<li><code>aarch64-linux-android</code>:  ARM64 Android 目标</li>
<li><code>x86_64-linux-android</code>:  <code>x86_64</code> Android 目标</li>
<li><code>wasm32-pyodide2024</code>:  wasm32 目标，使用 Pyodide 2024 平台。适用于 Python 3.12。参见 <a href="https://pyodide.org/en/stable/development/abi/312.html">https://pyodide.org/en/stable/development/abi/312.html</a></li>
<li><code>wasm32-pyodide2025</code>:  wasm32 目标，使用 Pyodide 2025 平台。适用于 Python 3.13。参见 <a href="https://pyodide.org/en/stable/development/abi/313.html">https://pyodide.org/en/stable/development/abi/313.html</a></li>
<li><code>arm64-apple-ios</code>:  iOS 设备的 ARM64 目标</li>
<li><code>arm64-apple-ios-simulator</code>:  iOS 模拟器的 ARM64 目标</li>
<li><code>x86_64-apple-ios-simulator</code>:  iOS 模拟器的 <code>x86_64</code> 目标</li>
</ul></dd><dt id="uv-pip-check--python-version"><a href="#uv-pip-check--python-version"><code>--python-version</code></a> <i>python-version</i></dt><dd><p>The Python version against which packages should be checked.</p>
<p>By default, the installed packages are checked against the version of the current interpreter.</p>
</dd><dt id="uv-pip-check--quiet"><a href="#uv-pip-check--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项（如 <code>-qq</code>）将启用静默模式，uv 将不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-pip-check--system"><a href="#uv-pip-check--system"><code>--system</code></a></dt><dd><p>Check packages in the system Python environment.</p>
<p>禁用虚拟环境的发现。</p>
<p>参见 <a href="#uv-python">uv python</a> 了解 Python 发现机制的详细信息。</p>
<p>May also be set with the <code>UV_SYSTEM_PYTHON</code> environment variable.</p></dd><dt id="uv-pip-check--system-certs"><a href="#uv-pip-check--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能需要使用平台的原生证书存储，特别是当您依赖系统证书存储中包含的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-pip-check--verbose"><a href="#uv-pip-check--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>