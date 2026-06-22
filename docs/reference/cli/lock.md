---
title: uv lock
description: uv lock 命令的完整中文参考文档，涵盖所有 CLI 选项的详细说明。包括锁文件更新、依赖解析策略、包索引配置、缓存管理、Python 版本选择、预发布版本策略、网络与安全选项等。适用于 uv 项目依赖锁定的各类场景。
---

# uv lock

更新项目的锁文件。

如果项目锁文件（`uv.lock`）不存在，将会创建它。如果锁文件已存在，其内容将作为依赖解析的偏好设置。

如果项目的依赖项没有变化，除非提供了 `--upgrade` 标志，否则锁定操作不会产生任何效果。

<h3 class="cli-reference">Usage</h3>

```
uv lock [OPTIONS]
```

<h3 class="cli-reference">Options</h3>

<dl class="cli-reference"><dt id="uv-lock--allow-insecure-host"><a href="#uv-lock--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统的证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您遭受中间人攻击。</p>
<p>也可通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-lock--cache-dir"><a href="#uv-lock--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上默认为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-lock--check"><a href="#uv-lock--check"><code>--check</code></a></dt><dd><p>检查锁文件是否是最新的。</p>
<p>断言 <code>uv.lock</code> 在解析后保持不变。如果锁文件缺失或需要更新，uv 将退出并返回错误。</p>
<p>等同于 <code>--locked</code>。</p>
</dd><dt id="uv-lock--check-exists"><a href="#uv-lock--check-exists"><code>--check-exists</code></a>, <code>--frozen</code></dt><dd><p>断言 <code>uv.lock</code> 存在，但不检查其是否是最新的 [env: UV_FROZEN=]</p>
<p>等同于 <code>--frozen</code>。</p>
</dd><dt id="uv-lock--color"><a href="#uv-lock--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测颜色支持。</p>
<p>可能的值：</p>
<ul>
<li><code>auto</code>：仅当输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，都启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-lock--config-file"><a href="#uv-lock--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许这样做。</p>
<p>也可通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-lock--config-setting"><a href="#uv-lock--config-setting"><code>--config-setting</code></a>, <code>--config-settings</code>, <code>-C</code> <i>config-setting</i></dt><dd><p>传递给 PEP 517 构建后端的设置，以 <code>KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-lock--config-settings-package"><a href="#uv-lock--config-settings-package"><code>--config-settings-package</code></a>, <code>--config-settings-package</code> <i>config-settings-package</i></dt><dd><p>为特定包传递给 PEP 517 构建后端的设置，以 <code>PACKAGE:KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-lock--default-index"><a href="#uv-lock--default-index"><code>--default-index</code></a> <i>default-index</i></dt><dd><p>默认包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式布局的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--index</code> 标志指定的所有其他索引。</p>
<p>也可通过 <code>UV_DEFAULT_INDEX</code> 环境变量设置。</p></dd><dt id="uv-lock--directory"><a href="#uv-lock--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 以仅更改项目根目录。</p>
<p>也可通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-lock--dry-run"><a href="#uv-lock--dry-run"><code>--dry-run</code></a></dt><dd><p>执行试运行，不写入锁文件。</p>
<p>在试运行模式下，uv 将解析项目的依赖项并报告结果变更，但不会将锁文件写入磁盘。</p>
</dd><dt id="uv-lock--exclude-newer"><a href="#uv-lock--exclude-newer"><code>--exclude-newer</code></a> <i>exclude-newer</i></dt><dd><p>将候选包限制为在给定日期之前上传的版本。</p>
<p>日期是与每个单独分发构件（即每个文件上传到包索引的时间）的上传时间进行比较，而非包版本的发布日期。</p>
<p>接受 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、基于系统配置时区解析的相同格式的本地日期（例如 <code>2006-12-02</code>）、"友好"的时长（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 时长（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>时长不遵循本地时区语义，始终解析为固定秒数，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月和年等日历单位。</p>
<p>也可通过 <code>UV_EXCLUDE_NEWER</code> 环境变量设置。</p></dd><dt id="uv-lock--exclude-newer-package"><a href="#uv-lock--exclude-newer-package"><code>--exclude-newer-package</code></a> <i>exclude-newer-package</i></dt><dd><p>将特定包的候选版本限制为在给定日期之前上传的版本。</p>
<p>接受 <code>PACKAGE=DATE</code> 格式的包-日期对，其中 <code>DATE</code> 可以是 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、基于系统配置时区解析的相同格式的本地日期（例如 <code>2006-12-02</code>）、"友好"的时长（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 时长（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>时长不遵循本地时区语义，始终解析为固定秒数，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月和年等日历单位。</p>
<p>可以为不同的包多次提供。</p>
</dd><dt id="uv-lock--extra-index-url"><a href="#uv-lock--extra-index-url"><code>--extra-index-url</code></a> <i>extra-index-url</i></dt><dd><p>（已弃用：请改用 <code>--index</code>）除 <code>--index-url</code> 之外要使用的额外包索引 URL。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式布局的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--index-url</code>（默认为 PyPI）指定的索引。当提供多个 <code>--extra-index-url</code> 标志时，较早的值优先级更高。</p>
<p>也可通过 <code>UV_EXTRA_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-lock--find-links"><a href="#uv-lock--find-links"><code>--find-links</code></a>, <code>-f</code> <i>find-links</i></dt><dd><p>除注册表索引中找到的之外，用于搜索候选分发包的额外位置。</p>
<p>如果是路径，目标必须是一个目录，其顶层包含 wheel 文件（<code>.whl</code>）或源码分发包（例如 <code>.tar.gz</code> 或 <code>.zip</code>）。</p>
<p>如果是 URL，页面必须包含一个扁平列表，其中包含符合上述格式的包文件链接。</p>
<p>也可通过 <code>UV_FIND_LINKS</code> 环境变量设置。</p></dd><dt id="uv-lock--fork-strategy"><a href="#uv-lock--fork-strategy"><code>--fork-strategy</code></a> <i>fork-strategy</i></dt><dd><p>在跨 Python 版本和平台选择给定包的多个版本时使用的策略。</p>
<p>默认情况下，uv 会优化为每个受支持的 Python 版本（<code>requires-python</code>）选择每个包的最新版本，同时最小化跨平台选择的版本数量。</p>
<p>在 <code>fewest</code> 模式下，uv 将最小化每个包选择的版本数量，优先选择与更广泛的受支持 Python 版本或平台兼容的旧版本。</p>
<p>也可通过 <code>UV_FORK_STRATEGY</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>fewest</code>：优化为每个包选择最少数量的版本。如果旧版本与更广泛的受支持 Python 版本或平台兼容，则可能优先选择旧版本</li>
<li><code>requires-python</code>：优化为每个受支持的 Python 版本选择每个包的最新支持版本</li>
</ul></dd><dt id="uv-lock--help"><a href="#uv-lock--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助</p>
</dd><dt id="uv-lock--index"><a href="#uv-lock--index"><code>--index</code></a> <i>index</i></dt><dd><p>解析依赖项时使用的 URL，除默认索引之外。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式布局的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--default-index</code>（默认为 PyPI）指定的索引。当提供多个 <code>--index</code> 标志时，较早的值优先级更高。</p>
<p>不支持将索引名称作为值。相对路径必须通过 <code>./</code> 或 <code>../</code>（Unix）或 <code>.\\</code>、<code>..\\</code>、<code>./</code> 或 <code>../</code>（Windows）与索引名称进行区分。</p>
<p>也可通过 <code>UV_INDEX</code> 环境变量设置。</p></dd><dt id="uv-lock--index-strategy"><a href="#uv-lock--index-strategy"><code>--index-strategy</code></a> <i>index-strategy</i></dt><dd><p>在多个索引 URL 上解析时使用的策略。</p>
<p>默认情况下，uv 会在第一个找到给定包的索引处停止，并将解析限制为该第一个索引（<code>first-index</code>）上存在的版本。这样可以防止"依赖混淆"攻击，即攻击者可以在替代索引上以相同名称上传恶意包。</p>
<p>也可通过 <code>UV_INDEX_STRATEGY</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>first-index</code>：仅使用第一个返回给定包名称匹配结果的索引</li>
<li><code>unsafe-first-match</code>：在所有索引中搜索每个包名称，在移动到下一个索引之前穷尽第一个索引的版本</li>
<li><code>unsafe-best-match</code>：在所有索引中搜索每个包名称，优先选择找到的"最佳"版本。如果包版本存在于多个索引中，则仅查看第一个索引的条目</li>
</ul></dd><dt id="uv-lock--index-url"><a href="#uv-lock--index-url"><code>--index-url</code></a>, <code>-i</code> <i>index-url</i></dt><dd><p>（已弃用：请改用 <code>--default-index</code>）Python 包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式布局的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--extra-index-url</code> 标志指定的所有其他索引。</p>
<p>也可通过 <code>UV_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-lock--keyring-provider"><a href="#uv-lock--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>尝试使用 <code>keyring</code> 对索引 URL 进行身份验证。</p>
<p>目前仅支持 <code>--keyring-provider subprocess</code>，它配置 uv 使用 <code>keyring</code> CLI 处理身份验证。</p>
<p>默认为 <code>disabled</code>。</p>
<p>也可通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>disabled</code>：不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>：使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-lock--link-mode"><a href="#uv-lock--link-mode"><code>--link-mode</code></a> <i>link-mode</i></dt><dd><p>从全局缓存安装包时使用的方法。</p>
<p>此选项仅在构建源码分发包时使用。</p>
<p>在 macOS 和 Linux 上默认为 <code>clone</code>（也称为写时复制），在 Windows 上默认为 <code>hardlink</code>。</p>
<p>警告：不鼓励使用符号链接（symlink）模式，因为它会在缓存和目标环境之间创建紧密耦合。例如，清除缓存（<code>uv cache clean</code>）将通过删除底层源文件来破坏所有已安装的包。请谨慎使用符号链接。</p>
<p>也可通过 <code>UV_LINK_MODE</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>clone</code>：从源克隆（即写时复制）包到目标</li>
<li><code>copy</code>：从源复制包到目标</li>
<li><code>hardlink</code>：从源硬链接包到目标</li>
<li><code>symlink</code>：从源符号链接包到目标</li>
</ul></dd><dt id="uv-lock--managed-python"><a href="#uv-lock--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用它管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-lock--no-binary"><a href="#uv-lock--no-binary"><code>--no-binary</code></a></dt><dd><p>不安装预构建 wheel。</p>
<p>给定的包将从源码构建并安装。解析器仍会使用预构建 wheel 提取包元数据（如果可用）。</p>
<p>也可通过 <code>UV_NO_BINARY</code> 环境变量设置。</p></dd><dt id="uv-lock--no-binary-package"><a href="#uv-lock--no-binary-package"><code>--no-binary-package</code></a> <i>no-binary-package</i></dt><dd><p>不对特定包安装预构建 wheel [env: <code>UV_NO_BINARY_PACKAGE</code>=]</p>
</dd><dt id="uv-lock--no-build"><a href="#uv-lock--no-build"><code>--no-build</code></a></dt><dd><p>不构建源码分发包。</p>
<p>启用后，解析不会运行任意 Python 代码。将重用已构建源码分发包的缓存 wheel，但需要构建分发的操作将退出并返回错误。</p>
<p>也可通过 <code>UV_NO_BUILD</code> 环境变量设置。</p></dd><dt id="uv-lock--no-build-isolation"><a href="#uv-lock--no-build-isolation"><code>--no-build-isolation</code></a></dt><dd><p>构建源码分发包时禁用隔离。</p>
<p>假设 PEP 518 指定的构建依赖已经安装。</p>
<p>也可通过 <code>UV_NO_BUILD_ISOLATION</code> 环境变量设置。</p></dd><dt id="uv-lock--no-build-isolation-package"><a href="#uv-lock--no-build-isolation-package"><code>--no-build-isolation-package</code></a> <i>no-build-isolation-package</i></dt><dd><p>为特定包构建源码分发包时禁用隔离。</p>
<p>假设包的 PEP 518 指定的构建依赖已经安装。</p>
</dd><dt id="uv-lock--no-build-package"><a href="#uv-lock--no-build-package"><code>--no-build-package</code></a> <i>no-build-package</i></dt><dd><p>不对特定包构建源码分发包 [env: <code>UV_NO_BUILD_PACKAGE</code>=]</p>
</dd><dt id="uv-lock--no-cache"><a href="#uv-lock--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免从缓存读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-lock--no-config"><a href="#uv-lock--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-lock--no-index"><a href="#uv-lock--no-index"><code>--no-index</code></a></dt><dd><p>忽略注册表索引（例如 PyPI），而是依赖直接 URL 依赖和通过 <code>--find-links</code> 提供的依赖</p>
</dd><dt id="uv-lock--no-managed-python"><a href="#uv-lock--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用使用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-lock--no-progress"><a href="#uv-lock--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转器或进度条。</p>
</dd><dt id="uv-lock--no-python-downloads"><a href="#uv-lock--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用自动下载 Python。</p>
</dd><dt id="uv-lock--no-sources"><a href="#uv-lock--no-sources"><code>--no-sources</code></a></dt><dd><p>解析依赖时忽略 <code>tool.uv.sources</code> 表。用于根据标准兼容、可发布的包元数据进行锁定，而不是使用任何工作区、Git、URL 或本地路径源</p>
<p>也可通过 <code>UV_NO_SOURCES</code> 环境变量设置。</p></dd><dt id="uv-lock--no-sources-package"><a href="#uv-lock--no-sources-package"><code>--no-sources-package</code></a> <i>no-sources-package</i></dt><dd><p>不对指定包使用 <code>tool.uv.sources</code> 表中的源 [env: <code>UV_NO_SOURCES_PACKAGE</code>=]</p>
</dd><dt id="uv-lock--offline"><a href="#uv-lock--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-lock--prerelease"><a href="#uv-lock--prerelease"><code>--prerelease</code></a> <i>prerelease</i></dt><dd><p>考虑预发布版本时使用的策略。</p>
<p>默认情况下，uv 会接受仅发布预发布版本的包的预发布版本，以及在声明的说明符中包含明确预发布标记的第一方依赖（<code>if-necessary-or-explicit</code>）。</p>
<p>也可通过 <code>UV_PRERELEASE</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>disallow</code>：不允许所有预发布版本</li>
<li><code>allow</code>：允许所有预发布版本</li>
<li><code>if-necessary</code>：如果包的所有版本都是预发布版本，则允许预发布版本</li>
<li><code>explicit</code>：允许在版本要求中带有明确预发布标记的第一方包的预发布版本</li>
<li><code>if-necessary-or-explicit</code>：如果包的所有版本都是预发布版本，或者包在其版本要求中带有明确的预发布标记，则允许预发布版本</li>
</ul></dd><dt id="uv-lock--project"><a href="#uv-lock--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时没有效果。</p>
<p>也可通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-lock--python"><a href="#uv-lock--python"><code>--python</code></a>, <code>-p</code> <i>python</i></dt><dd><p>解析期间使用的 Python 解释器。</p>
<p>当没有 wheel 可用时，需要 Python 解释器来构建源码分发版以确定包元数据。</p>
<p>如果未设置 <code>requires-python</code>，该解释器还用作最小 Python 版本的回退值。</p>
<p>有关 Python 发现和支持的请求格式的详细信息，请参见 <a href="#uv-python">uv python</a>。</p>
<p>也可通过 <code>UV_PYTHON</code> 环境变量设置。</p></dd><dt id="uv-lock--quiet"><a href="#uv-lock--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用安静输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，在此模式下 uv 不会向标准输出写入任何内容。</p>
</dd><dt id="uv-lock--refresh"><a href="#uv-lock--refresh"><code>--refresh</code></a></dt><dd><p>刷新所有缓存数据</p>
</dd><dt id="uv-lock--refresh-package"><a href="#uv-lock--refresh-package"><code>--refresh-package</code></a> <i>refresh-package</i></dt><dd><p>刷新特定包的缓存数据</p>
</dd><dt id="uv-lock--resolution"><a href="#uv-lock--resolution"><code>--resolution</code></a> <i>resolution</i></dt><dd><p>在给定包需求的不同兼容版本之间选择时使用的策略。</p>
<p>默认情况下，uv 会使用每个包的最新兼容版本（<code>highest</code>）。</p>
<p>也可通过 <code>UV_RESOLUTION</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>highest</code>：解析每个包的最高兼容版本</li>
<li><code>lowest</code>：解析每个包的最低兼容版本</li>
<li><code>lowest-direct</code>：解析任何直接依赖的最低兼容版本，以及任何传递依赖的最高兼容版本</li>
</ul></dd><dt id="uv-lock--script"><a href="#uv-lock--script"><code>--script</code></a> <i>script</i></dt><dd><p>锁定指定的 Python 脚本，而不是当前项目。</p>
<p>如果提供此选项，uv 会将脚本（基于其内联元数据表，符合 PEP 723）锁定到脚本本身旁边的 <code>.lock</code> 文件中。</p>
</dd><dt id="uv-lock--system-certs"><a href="#uv-lock--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（特别是在 macOS 上）。</p>
<p>但是，在某些情况下，你可能希望使用平台原生证书存储，特别是当你依赖包含在系统证书存储中的企业信任根（例如，对于强制代理）时。</p>
</dd><dt id="uv-lock--upgrade"><a href="#uv-lock--upgrade"><code>--upgrade</code></a>, <code>-U</code></dt><dd><p>允许包升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh</code></p>
</dd><dt id="uv-lock--upgrade-group"><a href="#uv-lock--upgrade-group"><code>--upgrade-group</code></a> <i>upgrade-group</i></dt><dd><p>允许升级依赖组中的所有包，忽略任何现有输出文件中的固定版本</p>
</dd><dt id="uv-lock--upgrade-package"><a href="#uv-lock--upgrade-package"><code>--upgrade-package</code></a>, <code>-P</code> <i>upgrade-package</i></dt><dd><p>允许升级特定包，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-lock--verbose"><a href="#uv-lock--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>你可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>
