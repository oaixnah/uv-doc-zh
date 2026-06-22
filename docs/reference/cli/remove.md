---
title: uv remove
description: uv remove 命令参考文档，从 Python 项目中移除依赖项，更新锁文件和环境，支持多种选项配置依赖移除行为。本文档详细介绍了 uv remove 的使用方法、参数说明和所有可用选项。
---

# uv remove

从项目中移除依赖项。

依赖项将从项目的 `pyproject.toml` 文件中移除。

如果给定的依赖项存在多个条目（即每个条目带有不同的标记（marker）），则所有条目都将被移除。

锁文件（lockfile）和项目环境将被更新以反映已移除的依赖项。要跳过锁文件的更新，请使用 `--frozen`。要跳过环境的更新，请使用 `--no-sync`。

如果请求的任何依赖项不存在于项目中，uv 将退出并报错。

如果某个包是通过 `uv pip install` 手动安装到环境中的，`uv remove` 不会将其移除。

uv 将在当前目录或任何父目录中搜索项目。如果找不到项目，uv 将退出并报错。

<h3 class="cli-reference">Usage</h3>

```
uv remove [OPTIONS] <PACKAGES>...
```

<h3 class="cli-reference">Arguments</h3>

<dl class="cli-reference"><dt id="uv-remove--packages"><a href="#uv-remove--packages"><code>PACKAGES</code></a></dt><dd><p>要移除的依赖项名称（例如 <code>ruff</code>）</p>
</dd></dl>

<h3 class="cli-reference">Options</h3>

<dl class="cli-reference"><dt id="uv-remove--active"><a href="#uv-remove--active"><code>--active</code></a></dt><dd><p>优先使用活动虚拟环境（active virtual environment），而非项目的虚拟环境。</p>
<p>如果项目的虚拟环境已处于活动状态，或者没有活动的虚拟环境，则此选项不起作用。</p>
</dd><dt id="uv-remove--allow-insecure-host"><a href="#uv-remove--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统的证书存储进行验证。仅在安全的网络中使用 <code>--allow-insecure-host</code> 并确保来源可信，因为它会绕过 SSL 验证，可能使您暴露于中间人攻击（MITM）的风险中。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-remove--cache-dir"><a href="#uv-remove--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认值为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-remove--color"><a href="#uv-remove--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测对颜色的支持。</p>
<p>可能的值：</p>
<ul>
<li><code>auto</code>：仅当输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，均启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-remove--compile-bytecode"><a href="#uv-remove--compile-bytecode"><code>--compile-bytecode</code></a>, <code>--compile</code></dt><dd><p>安装后将 Python 文件编译为字节码。</p>
<p>默认情况下，uv 不会将 Python（<code>.py</code>）文件编译为字节码（<code>__pycache__/*.pyc</code>）；相反，编译会在模块首次导入时延迟执行。对于启动时间至关重要的用例，例如 CLI 应用程序和 Docker 容器，可以启用此选项，以较长的安装时间换取更快的启动时间。</p>
<p>启用后，uv 将处理整个 site-packages 目录（包括当前操作未修改的包）以保持一致性。与 pip 类似，它也会忽略错误。</p>
<p>也可以通过 <code>UV_COMPILE_BYTECODE</code> 环境变量设置。</p></dd><dt id="uv-remove--config-file"><a href="#uv-remove--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件的路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许这样做。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-remove--config-setting"><a href="#uv-remove--config-setting"><code>--config-setting</code></a>, <code>--config-settings</code>, <code>-C</code> <i>config-setting</i></dt><dd><p>传递给 PEP 517 构建后端（build backend）的设置，以 <code>KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-remove--config-settings-package"><a href="#uv-remove--config-settings-package"><code>--config-settings-package</code></a>, <code>--config-settings-package</code> <i>config-settings-package</i></dt><dd><p>为特定包传递给 PEP 517 构建后端的设置，以 <code>PACKAGE:KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-remove--default-index"><a href="#uv-remove--default-index"><code>--default-index</code></a> <i>default-index</i></dt><dd><p>默认包索引的 URL（默认值为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或以相同格式组织的本地目录。</p>
<p>通过此标志指定的索引优先级低于通过 <code>--index</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_DEFAULT_INDEX</code> 环境变量设置。</p></dd><dt id="uv-remove--dev"><a href="#uv-remove--dev"><code>--dev</code></a></dt><dd><p>从开发依赖组（development dependency group）中移除包 [env: UV_DEV=]</p>
<p>此选项是 <code>--group dev</code> 的别名。</p>
</dd><dt id="uv-remove--directory"><a href="#uv-remove--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径将基于给定目录进行解析。</p>
<p>参见 <code>--project</code> 以仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-remove--exclude-newer"><a href="#uv-remove--exclude-newer"><code>--exclude-newer</code></a> <i>exclude-newer</i></dt><dd><p>将候选包限制为在给定日期之前上传的包。</p>
<p>日期与每个单独分发构件（distribution artifact）的上传时间（即每个文件上传到包索引的时间）进行比较，而非包版本的发布日期。</p>
<p>接受 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、基于系统配置时区解析的相同格式的本地日期（例如 <code>2006-12-02</code>）、友好格式的持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不考虑本地时区的语义，始终按固定秒数解析，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月份和年份等日历单位。</p>
<p>也可以通过 <code>UV_EXCLUDE_NEWER</code> 环境变量设置。</p></dd><dt id="uv-remove--exclude-newer-package"><a href="#uv-remove--exclude-newer-package"><code>--exclude-newer-package</code></a> <i>exclude-newer-package</i></dt><dd><p>将特定包的候选包限制为在给定日期之前上传的包。</p>
<p>接受 <code>PACKAGE=DATE</code> 格式的包-日期对，其中 <code>DATE</code> 是 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、基于系统配置时区解析的相同格式的本地日期（例如 <code>2006-12-02</code>）、友好格式的持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不考虑本地时区的语义，始终按固定秒数解析，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月份和年份等日历单位。</p>
<p>可以为不同的包多次提供。</p>
</dd><dt id="uv-remove--extra-index-url"><a href="#uv-remove--extra-index-url"><code>--extra-index-url</code></a> <i>extra-index-url</i></dt><dd><p>（已弃用：请改用 <code>--index</code>）除 <code>--index-url</code> 之外要使用的额外包索引 URL。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或以相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--index-url</code>（默认为 PyPI）指定的索引。当提供多个 <code>--extra-index-url</code> 标志时，较早的值优先级更高。</p>
<p>也可以通过 <code>UV_EXTRA_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-remove--find-links"><a href="#uv-remove--find-links"><code>--find-links</code></a>, <code>-f</code> <i>find-links</i></dt><dd><p>除注册表索引中找到的候选分发之外，还要搜索候选分发的位置。</p>
<p>如果是一个路径，目标必须是一个目录，其中包含顶层目录中的 wheel 文件（<code>.whl</code>）或源代码分发（例如 <code>.tar.gz</code> 或 <code>.zip</code>）。</p>
<p>如果是一个 URL，页面必须包含指向符合上述格式的包文件的扁平链接列表。</p>
<p>也可以通过 <code>UV_FIND_LINKS</code> 环境变量设置。</p></dd><dt id="uv-remove--fork-strategy"><a href="#uv-remove--fork-strategy"><code>--fork-strategy</code></a> <i>fork-strategy</i></dt><dd><p>在跨 Python 版本和平台选择给定包的多个版本时使用的策略。</p>
<p>默认情况下，uv 会优化为每个受支持的 Python 版本（<code>requires-python</code>）选择每个包的最新版本，同时最小化跨平台选中的版本数量。</p>
<p>使用 <code>fewest</code> 策略时，uv 将最小化每个包选中的版本数量，优先选择与更广泛的受支持 Python 版本或平台兼容的旧版本。</p>
<p>也可以通过 <code>UV_FORK_STRATEGY</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>fewest</code>：优化以选择每个包的最少版本数量。如果旧版本与更广泛的受支持 Python 版本或平台兼容，则可能优先选择旧版本</li>
<li><code>requires-python</code>：优化以选择每个受支持 Python 版本的每个包的最新版本</li>
</ul></dd><dt id="uv-remove--frozen"><a href="#uv-remove--frozen"><code>--frozen</code></a></dt><dd><p>移除依赖项而不重新锁定项目 [env: UV_FROZEN=]</p>
<p>项目环境将不会被同步。</p>
</dd><dt id="uv-remove--group"><a href="#uv-remove--group"><code>--group</code></a> <i>group</i></dt><dd><p>从指定的依赖组中移除包</p>
</dd><dt id="uv-remove--help"><a href="#uv-remove--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助信息</p>
</dd><dt id="uv-remove--index"><a href="#uv-remove--index"><code>--index</code></a> <i>index</i></dt><dd><p>解析依赖项时使用的 URL，作为默认索引的补充。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或以相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--default-index</code>（默认为 PyPI）指定的索引。当提供多个 <code>--index</code> 标志时，较早的值优先级更高。</p>
<p>不支持将索引名称作为值。相对路径必须使用 <code>./</code> 或 <code>../</code>（在 Unix 上）或 <code>.\\</code>、<code>..\\</code>、<code>./</code> 或 <code>../</code>（在 Windows 上）与索引名称区分开来。</p>
<p>也可以通过 <code>UV_INDEX</code> 环境变量设置。</p></dd><dt id="uv-remove--index-strategy"><a href="#uv-remove--index-strategy"><code>--index-strategy</code></a> <i>index-strategy</i></dt><dd><p>在解析多个索引 URL 时使用的策略。</p>
<p>默认情况下，uv 会在找到给定包的第一个索引处停止，并将解析限制为该第一个索引上存在的包（<code>first-index</code>）。这可以防止依赖混淆（dependency confusion）攻击，即攻击者可以在备用索引上以相同名称上传恶意包。</p>
<p>也可以通过 <code>UV_INDEX_STRATEGY</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>first-index</code>：仅使用为给定包名称返回匹配结果的第一个索引</li>
<li><code>unsafe-first-match</code>：在所有索引中搜索每个包名称，在移至下一个索引之前耗尽第一个索引的版本</li>
<li><code>unsafe-best-match</code>：在所有索引中搜索每个包名称，优先选择找到的最佳版本。如果某个包版本存在于多个索引中，则仅查看第一个索引的条目</li>
</ul></dd><dt id="uv-remove--index-url"><a href="#uv-remove--index-url"><code>--index-url</code></a>, <code>-i</code> <i>index-url</i></dt><dd><p>（已弃用：请改用 <code>--default-index</code>）Python 包索引的 URL（默认值为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或以相同格式组织的本地目录。</p>
<p>通过此标志指定的索引优先级低于通过 <code>--extra-index-url</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-remove--keyring-provider"><a href="#uv-remove--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>尝试使用 <code>keyring</code> 进行索引 URL 的身份验证。</p>
<p>目前仅支持 <code>--keyring-provider subprocess</code>，它会将 uv 配置为使用 <code>keyring</code> CLI 来处理身份验证。</p>
<p>默认值为 <code>disabled</code>。</p>
<p>也可以通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>disabled</code>：不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>：使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-remove--link-mode"><a href="#uv-remove--link-mode"><code>--link-mode</code></a> <i>link-mode</i></dt><dd><p>从全局缓存安装包时使用的链接方法。</p>
<p>在 macOS 和 Linux 上默认值为 <code>clone</code>（也称为写时复制 Copy-on-Write），在 Windows 上为 <code>hardlink</code>。</p>
<p>警告：不建议使用 symlink 链接模式，因为它会在缓存和目标环境之间创建紧密耦合。例如，清除缓存（<code>uv cache clean</code>）将会通过移除底层源文件来破坏所有已安装的包。请谨慎使用 symlink。</p>
<p>也可以通过 <code>UV_LINK_MODE</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>clone</code>：将包从源克隆（即写时复制）到目标</li>
<li><code>copy</code>：将包从源复制到目标</li>
<li><code>hardlink</code>：将包从源硬链接到目标</li>
<li><code>symlink</code>：将包从源符号链接到目标</li>
</ul></dd><dt id="uv-remove--locked"><a href="#uv-remove--locked"><code>--locked</code></a></dt><dd><p>断言 <code>uv.lock</code> 将保持不变 [env: UV_LOCKED=]</p>
<p>要求锁文件是最新的。如果锁文件缺失或需要更新，uv 将退出并报错。</p>
</dd><dt id="uv-remove--managed-python"><a href="#uv-remove--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用其管理的 Python 版本。但是，如果没有安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-remove--no-binary"><a href="#uv-remove--no-binary"><code>--no-binary</code></a></dt><dd><p>不安装预构建的 wheel。</p>
<p>给定的包将从源代码构建并安装。解析器仍将使用预构建的 wheel 来提取包元数据（如果可用）。</p>
<p>也可以通过 <code>UV_NO_BINARY</code> 环境变量设置。</p></dd><dt id="uv-remove--no-binary-package"><a href="#uv-remove--no-binary-package"><code>--no-binary-package</code></a> <i>no-binary-package</i></dt><dd><p>不为特定包安装预构建的 wheel [env: <code>UV_NO_BINARY_PACKAGE</code>=]</p>
</dd><dt id="uv-remove--no-build"><a href="#uv-remove--no-build"><code>--no-build</code></a></dt><dd><p>不构建源代码分发（source distribution）。</p>
<p>启用后，解析将不会运行任意的 Python 代码。已构建的源代码分发的缓存 wheel 将被重用，但需要构建分发的操作将退出并报错。</p>
<p>也可以通过 <code>UV_NO_BUILD</code> 环境变量设置。</p></dd><dt id="uv-remove--no-build-isolation"><a href="#uv-remove--no-build-isolation"><code>--no-build-isolation</code></a></dt><dd><p>构建源代码分发时禁用隔离。</p>
<p>假设 PEP 518 指定的构建依赖项已经安装。</p>
<p>也可以通过 <code>UV_NO_BUILD_ISOLATION</code> 环境变量设置。</p></dd><dt id="uv-remove--no-build-isolation-package"><a href="#uv-remove--no-build-isolation-package"><code>--no-build-isolation-package</code></a> <i>no-build-isolation-package</i></dt><dd><p>为特定包构建源代码分发时禁用隔离。</p>
<p>假设该包的 PEP 518 指定的构建依赖项已经安装。</p>
</dd><dt id="uv-remove--no-build-package"><a href="#uv-remove--no-build-package"><code>--no-build-package</code></a> <i>no-build-package</i></dt><dd><p>不为特定包构建源代码分发 [env: <code>UV_NO_BUILD_PACKAGE</code>=]</p>
</dd><dt id="uv-remove--no-cache"><a href="#uv-remove--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，在操作期间改用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-remove--no-config"><a href="#uv-remove--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-remove--no-index"><a href="#uv-remove--no-index"><code>--no-index</code></a></dt><dd><p>忽略注册表索引（例如 PyPI），转而依赖直接 URL 依赖项和通过 <code>--find-links</code> 提供的依赖项</p>
</dd><dt id="uv-remove--no-managed-python"><a href="#uv-remove--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用 uv 管理的 Python 版本的使用 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-remove--no-progress"><a href="#uv-remove--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转动画（spinner）或进度条。</p>
</dd><dt id="uv-remove--no-python-downloads"><a href="#uv-remove--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-remove--no-sources"><a href="#uv-remove--no-sources"><code>--no-sources</code></a></dt><dd><p>解析依赖项时忽略 <code>tool.uv.sources</code> 表。用于根据符合标准、可发布的包元数据进行锁定，而不是使用任何工作区（workspace）、Git、URL 或本地路径源</p>
<p>也可以通过 <code>UV_NO_SOURCES</code> 环境变量设置。</p></dd><dt id="uv-remove--no-sources-package"><a href="#uv-remove--no-sources-package"><code>--no-sources-package</code></a> <i>no-sources-package</i></dt><dd><p>不为指定包使用 <code>tool.uv.sources</code> 表中的源 [env: <code>UV_NO_SOURCES_PACKAGE</code>=]</p>
</dd><dt id="uv-remove--no-sync"><a href="#uv-remove--no-sync"><code>--no-sync</code></a></dt><dd><p>重新锁定项目后避免同步虚拟环境 [env: UV_NO_SYNC=]</p>
</dd><dt id="uv-remove--offline"><a href="#uv-remove--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用的文件。</p>
</dd><dt id="uv-remove--optional"><a href="#uv-remove--optional"><code>--optional</code></a> <i>optional</i></dt><dd><p>从项目指定 extra 的可选依赖项中移除包</p>
</dd><dt id="uv-remove--package"><a href="#uv-remove--package"><code>--package</code></a> <i>package</i></dt><dd><p>从工作区中的特定包中移除依赖项</p>
</dd><dt id="uv-remove--prerelease"><a href="#uv-remove--prerelease"><code>--prerelease</code></a> <i>prerelease</i></dt><dd><p>考虑预发布（pre-release）版本时使用的策略。</p>
<p>默认情况下，uv 将接受<em>仅</em>发布预发布版本的包的预发布版本，以及在其声明的版本说明符中包含显式预发布标记的第一方依赖项（<code>if-necessary-or-explicit</code>）。</p>
<p>也可以通过 <code>UV_PRERELEASE</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>disallow</code>：禁止所有预发布版本</li>
<li><code>allow</code>：允许所有预发布版本</li>
<li><code>if-necessary</code>：如果包的所有版本都是预发布版本，则允许预发布版本</li>
<li><code>explicit</code>：允许其版本要求中包含显式预发布标记的第一方包的预发布版本</li>
<li><code>if-necessary-or-explicit</code>：如果包的所有版本都是预发布版本，或者包在其版本要求中包含显式预发布标记，则允许预发布版本</li>
</ul></dd><dt id="uv-remove--project"><a href="#uv-remove--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-remove--python"><a href="#uv-remove--python"><code>--python</code></a>, <code>-p</code> <i>python</i></dt><dd><p>用于解析和同步的 Python 解释器。</p>
<p>有关 Python 发现和支持的请求格式的详细信息，请参见 <a href="#uv-python">uv python</a>。</p>
<p>也可以通过 <code>UV_PYTHON</code> 环境变量设置。</p></dd><dt id="uv-remove--quiet"><a href="#uv-remove--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用安静输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，在该模式下 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-remove--refresh"><a href="#uv-remove--refresh"><code>--refresh</code></a></dt><dd><p>刷新所有缓存数据</p>
</dd><dt id="uv-remove--refresh-package"><a href="#uv-remove--refresh-package"><code>--refresh-package</code></a> <i>refresh-package</i></dt><dd><p>刷新特定包的缓存数据</p>
</dd><dt id="uv-remove--reinstall"><a href="#uv-remove--reinstall"><code>--reinstall</code></a>, <code>--force-reinstall</code></dt><dd><p>重新安装所有包，无论它们是否已安装。隐含 <code>--refresh</code></p>
</dd><dt id="uv-remove--reinstall-package"><a href="#uv-remove--reinstall-package"><code>--reinstall-package</code></a> <i>reinstall-package</i></dt><dd><p>重新安装特定包，无论它是否已安装。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-remove--resolution"><a href="#uv-remove--resolution"><code>--resolution</code></a> <i>resolution</i></dt><dd><p>在给定包需求的不同兼容版本之间进行选择时使用的策略。</p>
<p>默认情况下，uv 将使用每个包的最新兼容版本（<code>highest</code>）。</p>
<p>也可以通过 <code>UV_RESOLUTION</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>highest</code>：解析每个包的最高兼容版本</li>
<li><code>lowest</code>：解析每个包的最低兼容版本</li>
<li><code>lowest-direct</code>：解析任何直接依赖项的最低兼容版本，以及任何传递依赖项的最高兼容版本</li>
</ul></dd><dt id="uv-remove--script"><a href="#uv-remove--script"><code>--script</code></a> <i>script</i></dt><dd><p>从指定的 Python 脚本中移除依赖项，而不是从项目中移除。</p>
<p>如果提供，uv 将根据 PEP 723 从脚本的内联元数据表（inline metadata table）中移除依赖项。</p>
</dd><dt id="uv-remove--system-certs"><a href="#uv-remove--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（特别是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能希望使用平台的原生证书存储，特别是当您依赖系统证书存储中包含的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-remove--upgrade"><a href="#uv-remove--upgrade"><code>--upgrade</code></a>, <code>-U</code></dt><dd><p>允许包升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh</code></p>
</dd><dt id="uv-remove--upgrade-group"><a href="#uv-remove--upgrade-group"><code>--upgrade-group</code></a> <i>upgrade-group</i></dt><dd><p>允许依赖组中所有包的升级，忽略任何现有输出文件中的固定版本</p>
</dd><dt id="uv-remove--upgrade-package"><a href="#uv-remove--upgrade-package"><code>--upgrade-package</code></a>, <code>-P</code> <i>upgrade-package</i></dt><dd><p>允许特定包的升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-remove--verbose"><a href="#uv-remove--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度的日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>
