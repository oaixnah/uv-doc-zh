---
title: uv export
description: uv export 命令将项目的锁文件导出为 requirements.txt、pylock.toml 或 CycloneDX JSON 等其他格式。本文档提供了 uv export 命令的完整选项说明，包括依赖导出、格式选择、缓存管理、索引配置等参数使用方法，帮助 Python 开发者将 uv 项目依赖导出为兼容格式以便与其他工具集成。
---

# uv export

将项目的锁文件（lockfile）导出为其他格式。

目前支持 `requirements.txt`、`pylock.toml`（PEP 751）和 CycloneDX v1.5 JSON 输出格式。

除非提供了 `--locked` 或 `--frozen` 标志，否则项目在导出前会重新锁定。

uv 会在当前目录或任意父目录中搜索项目。如果找不到项目，uv 将退出并报错。

如果在工作区（workspace）中操作，默认会导出根项目；但可以使用 `--package` 选项选择特定的成员。

<h3 class="cli-reference">用法（Usage）</h3>

```
uv export [OPTIONS]
```

<h3 class="cli-reference">选项（Options）</h3>

<dl class="cli-reference"><dt id="uv-export--all-extras"><a href="#uv-export--all-extras"><code>--all-extras</code></a></dt><dd><p>包含所有可选依赖</p>
</dd><dt id="uv-export--all-groups"><a href="#uv-export--all-groups"><code>--all-groups</code></a></dt><dd><p>包含所有依赖组中的依赖。</p>
<p>可以使用 <code>--no-group</code> 来排除特定组。</p>
</dd><dt id="uv-export--all-packages"><a href="#uv-export--all-packages"><code>--all-packages</code></a></dt><dd><p>导出整个工作区。</p>
<p>所有工作区成员的依赖都将包含在导出的 requirements 文件中。</p>
<p>通过 <code>--extra</code>、<code>--group</code> 或相关选项指定的任何 extras 或组将应用于所有工作区成员。</p>
</dd><dt id="uv-export--allow-insecure-host"><a href="#uv-export--allow-insecure-host"><code>--allow-insecure-host</code></a>、<code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统的证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您遭受中间人（MITM）攻击。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-export--cache-dir"><a href="#uv-export--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上默认为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-export--color"><a href="#uv-export--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>：仅当输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-export--config-file"><a href="#uv-export--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许这样做。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-export--config-setting"><a href="#uv-export--config-setting"><code>--config-setting</code></a>、<code>--config-settings</code>、<code>-C</code> <i>config-setting</i></dt><dd><p>传递给 PEP 517 构建后端（build backend）的设置，以 <code>KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-export--config-settings-package"><a href="#uv-export--config-settings-package"><code>--config-settings-package</code></a>、<code>--config-settings-package</code> <i>config-settings-package</i></dt><dd><p>为特定包传递给 PEP 517 构建后端的设置，以 <code>PACKAGE:KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-export--default-index"><a href="#uv-export--default-index"><code>--default-index</code></a> <i>default-index</i></dt><dd><p>默认包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或以相同格式组织的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--index</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_DEFAULT_INDEX</code> 环境变量设置。</p></dd><dt id="uv-export--directory"><a href="#uv-export--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到给定目录。</p>
<p>相对路径以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 以仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-export--emit-find-links"><a href="#uv-export--emit-find-links"><code>--emit-find-links</code></a></dt><dd><p>在生成的输出文件中包含 <code>--find-links</code> 条目</p>
</dd><dt id="uv-export--emit-index-url"><a href="#uv-export--emit-index-url"><code>--emit-index-url</code></a></dt><dd><p>在生成的输出文件中包含 <code>--index-url</code> 和 <code>--extra-index-url</code> 条目</p>
</dd><dt id="uv-export--exclude-newer"><a href="#uv-export--exclude-newer"><code>--exclude-newer</code></a> <i>exclude-newer</i></dt><dd><p>将候选包限制为在给定日期之前上传的版本。</p>
<p>日期是与每个单独分发构件（distribution artifact）的上传时间（即每个文件上传到包索引的时间）进行比较，而不是包版本的发布日期。</p>
<p>接受 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、相同格式的本地日期（例如 <code>2006-12-02</code>，基于系统配置的时区解析）、"友好"持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不考虑本地时区的语义，始终按固定秒数解析，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月份和年份等日历单位。</p>
<p>也可以通过 <code>UV_EXCLUDE_NEWER</code> 环境变量设置。</p></dd><dt id="uv-export--exclude-newer-package"><a href="#uv-export--exclude-newer-package"><code>--exclude-newer-package</code></a> <i>exclude-newer-package</i></dt><dd><p>将特定包的候选版本限制为在给定日期之前上传的版本。</p>
<p>接受 <code>PACKAGE=DATE</code> 格式的包-日期对，其中 <code>DATE</code> 是 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、相同格式的本地日期（例如 <code>2006-12-02</code>，基于系统配置的时区解析）、"友好"持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不考虑本地时区的语义，始终按固定秒数解析，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月份和年份等日历单位。</p>
<p>可以为不同的包多次提供。</p>
</dd><dt id="uv-export--extra"><a href="#uv-export--extra"><code>--extra</code></a> <i>extra</i></dt><dd><p>包含来自指定 extra 名称的可选依赖。</p>
<p>可以多次提供。</p>
</dd><dt id="uv-export--extra-index-url"><a href="#uv-export--extra-index-url"><code>--extra-index-url</code></a> <i>extra-index-url</i></dt><dd><p>（已弃用：请改用 <code>--index</code>）除 <code>--index-url</code> 之外使用的额外包索引 URL。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或以相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--index-url</code> 指定的索引（默认为 PyPI）。当提供多个 <code>--extra-index-url</code> 标志时，较早的值优先级更高。</p>
<p>也可以通过 <code>UV_EXTRA_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-export--find-links"><a href="#uv-export--find-links"><code>--find-links</code></a>、<code>-f</code> <i>find-links</i></dt><dd><p>除注册表索引中找到的之外，还要搜索候选分发包的位置。</p>
<p>如果是路径，目标必须是一个目录，顶层包含作为 wheel 文件（<code>.whl</code>）或源码分发包（例如 <code>.tar.gz</code> 或 <code>.zip</code>）的包。</p>
<p>如果是 URL，页面必须包含指向符合上述格式的包文件的扁平链接列表。</p>
<p>也可以通过 <code>UV_FIND_LINKS</code> 环境变量设置。</p></dd><dt id="uv-export--fork-strategy"><a href="#uv-export--fork-strategy"><code>--fork-strategy</code></a> <i>fork-strategy</i></dt><dd><p>在跨 Python 版本和平台选择给定包的多个版本时使用的策略。</p>
<p>默认情况下，uv 会优化为每个受支持的 Python 版本（<code>requires-python</code>）选择每个包的最新版本，同时最小化跨平台选择的版本数量。</p>
<p>在 <code>fewest</code> 模式下，uv 将最小化每个包选择的版本数量，优先选择与更广泛的受支持 Python 版本或平台兼容的旧版本。</p>
<p>也可以通过 <code>UV_FORK_STRATEGY</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>fewest</code>：优化为每个包选择最少数量的版本。如果旧版本与更广泛的受支持 Python 版本或平台兼容，可能会优先选择旧版本</li>
<li><code>requires-python</code>：优化为每个受支持的 Python 版本选择每个包的最新支持版本</li>
</ul></dd><dt id="uv-export--format"><a href="#uv-export--format"><code>--format</code></a> <i>format</i></dt><dd><p><code>uv.lock</code> 应导出到的格式。</p>
<p>支持 <code>requirements.txt</code>、<code>pylock.toml</code>（PEP 751）和 CycloneDX v1.5 JSON 输出格式。</p>
<p>如果提供了输出文件，uv 将从输出文件的扩展名推断输出格式。否则，默认为 <code>requirements.txt</code>。</p>
<p>可选值：</p>
<ul>
<li><code>requirements.txt</code>：以 <code>requirements.txt</code> 格式导出</li>
<li><code>pylock.toml</code>：以 <code>pylock.toml</code> 格式导出</li>
<li><code>cyclonedx1.5</code>：以 <code>CycloneDX</code> v1.5 JSON 格式导出</li>
</ul></dd><dt id="uv-export--frozen"><a href="#uv-export--frozen"><code>--frozen</code></a></dt><dd><p>导出前不更新 <code>uv.lock</code> [env: UV_FROZEN=]</p>
<p>如果 <code>uv.lock</code> 不存在，uv 将退出并报错。</p>
</dd><dt id="uv-export--group"><a href="#uv-export--group"><code>--group</code></a> <i>group</i></dt><dd><p>包含来自指定依赖组的依赖。</p>
<p>可以多次提供。</p>
</dd><dt id="uv-export--help"><a href="#uv-export--help"><code>--help</code></a>、<code>-h</code></dt><dd><p>显示此命令的简明帮助</p>
</dd><dt id="uv-export--index"><a href="#uv-export--index"><code>--index</code></a> <i>index</i></dt><dd><p>解析依赖时使用的 URL，作为默认索引的补充。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或以相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--default-index</code> 指定的索引（默认为 PyPI）。当提供多个 <code>--index</code> 标志时，较早的值优先级更高。</p>
<p>不支持将索引名称作为值。相对路径必须通过以下方式与索引名称区分：在 Unix 上使用 <code>./</code> 或 <code>../</code>，在 Windows 上使用 <code>.\\</code>、<code>..\\</code>、<code>./</code> 或 <code>../</code>。</p>
<p>也可以通过 <code>UV_INDEX</code> 环境变量设置。</p></dd><dt id="uv-export--index-strategy"><a href="#uv-export--index-strategy"><code>--index-strategy</code></a> <i>index-strategy</i></dt><dd><p>在多个索引 URL 之间解析时使用的策略。</p>
<p>默认情况下，uv 会在第一个找到给定包的索引处停止，并将解析限制在该第一个索引上存在的版本（<code>first-index</code>）。这可以防止"依赖混淆"（dependency confusion）攻击，即攻击者可以在替代索引上以相同名称上传恶意包。</p>
<p>也可以通过 <code>UV_INDEX_STRATEGY</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>first-index</code>：仅使用第一个返回给定包名匹配的索引的结果</li>
<li><code>unsafe-first-match</code>：在所有索引中搜索每个包名，先用尽第一个索引的版本，然后再转到下一个</li>
<li><code>unsafe-best-match</code>：在所有索引中搜索每个包名，优先选择找到的"最佳"版本。如果一个包版本存在于多个索引中，则仅查看第一个索引的条目</li>
</ul></dd><dt id="uv-export--index-url"><a href="#uv-export--index-url"><code>--index-url</code></a>、<code>-i</code> <i>index-url</i></dt><dd><p>（已弃用：请改用 <code>--default-index</code>）Python 包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或以相同格式组织的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--extra-index-url</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-export--keyring-provider"><a href="#uv-export--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>尝试使用 <code>keyring</code> 进行索引 URL 的身份验证。</p>
<p>目前仅支持 <code>--keyring-provider subprocess</code>，它配置 uv 使用 <code>keyring</code> CLI 来处理身份验证。</p>
<p>默认为 <code>disabled</code>。</p>
<p>也可以通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disabled</code>：不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>：使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-export--link-mode"><a href="#uv-export--link-mode"><code>--link-mode</code></a> <i>link-mode</i></dt><dd><p>从全局缓存安装包时使用的方法。</p>
<p>此选项仅在构建源码分发包（source distributions）时使用。</p>
<p>在 macOS 和 Linux 上默认为 <code>clone</code>（也称为写时复制 Copy-on-Write），在 Windows 上默认为 <code>hardlink</code>。</p>
<p>警告：不建议使用 symlink 链接模式，因为它会在缓存和目标环境之间创建紧密耦合。例如，清除缓存（<code>uv cache clean</code>）将通过移除底层源文件来破坏所有已安装的包。请谨慎使用 symlink。</p>
<p>也可以通过 <code>UV_LINK_MODE</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>clone</code>：将包从源克隆（即写时复制）到目标</li>
<li><code>copy</code>：将包从源复制到目标</li>
<li><code>hardlink</code>：将包从源硬链接到目标</li>
<li><code>symlink</code>：将包从源符号链接到目标</li>
</ul></dd><dt id="uv-export--locked"><a href="#uv-export--locked"><code>--locked</code></a></dt><dd><p>断言 <code>uv.lock</code> 将保持不变 [env: UV_LOCKED=]</p>
<p>要求锁文件是最新的。如果锁文件缺失或需要更新，uv 将退出并报错。</p>
</dd><dt id="uv-export--managed-python"><a href="#uv-export--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用它管理的 Python 版本。但是，如果没有安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-export--no-annotate"><a href="#uv-export--no-annotate"><code>--no-annotate</code></a></dt><dd><p>排除指示每个包来源的注释注解</p>
</dd><dt id="uv-export--no-binary"><a href="#uv-export--no-binary"><code>--no-binary</code></a></dt><dd><p>不安装预构建的 wheel。</p>
<p>给定的包将从源码构建并安装。解析器仍将使用预构建的 wheel 来提取包元数据（如果可用）。</p>
<p>也可以通过 <code>UV_NO_BINARY</code> 环境变量设置。</p></dd><dt id="uv-export--no-binary-package"><a href="#uv-export--no-binary-package"><code>--no-binary-package</code></a> <i>no-binary-package</i></dt><dd><p>不为特定包安装预构建的 wheel [env: <code>UV_NO_BINARY_PACKAGE</code>=]</p>
</dd><dt id="uv-export--no-build"><a href="#uv-export--no-build"><code>--no-build</code></a></dt><dd><p>不构建源码分发包。</p>
<p>启用后，解析将不会运行任意 Python 代码。已构建的源码分发包的缓存 wheel 将被重用，但需要构建分发包的操作将退出并报错。</p>
<p>也可以通过 <code>UV_NO_BUILD</code> 环境变量设置。</p></dd><dt id="uv-export--no-build-isolation"><a href="#uv-export--no-build-isolation"><code>--no-build-isolation</code></a></dt><dd><p>构建源码分发包时禁用隔离。</p>
<p>假设 PEP 518 指定的构建依赖已安装。</p>
<p>也可以通过 <code>UV_NO_BUILD_ISOLATION</code> 环境变量设置。</p></dd><dt id="uv-export--no-build-isolation-package"><a href="#uv-export--no-build-isolation-package"><code>--no-build-isolation-package</code></a> <i>no-build-isolation-package</i></dt><dd><p>为特定包构建源码分发包时禁用隔离。</p>
<p>假设 PEP 518 指定的该包的构建依赖已安装。</p>
</dd><dt id="uv-export--no-build-package"><a href="#uv-export--no-build-package"><code>--no-build-package</code></a> <i>no-build-package</i></dt><dd><p>不为特定包构建源码分发包 [env: <code>UV_NO_BUILD_PACKAGE</code>=]</p>
</dd><dt id="uv-export--no-cache"><a href="#uv-export--no-cache"><code>--no-cache</code></a>、<code>--no-cache-dir</code>、<code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-export--no-config"><a href="#uv-export--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
</dd><dt id="uv-export--no-default-groups"><a href="#uv-export--no-default-groups"><code>--no-default-groups</code></a></dt><dd><p>排除默认依赖组中指定的依赖。</p>
<p>默认情况下，如果存在 <code>dev</code> 依赖组，则将其包含在内。</p>
</dd><dt id="uv-export--no-dev"><a href="#uv-export--no-dev"><code>--no-dev</code></a></dt><dd><p>排除开发依赖组。</p>
<p>此选项是 <code>--no-group dev</code> 的别名。</p>
</dd><dt id="uv-export--no-editable"><a href="#uv-export--no-editable"><code>--no-editable</code></a></dt><dd><p>不安装任何包为可编辑模式（editable）。</p>
<p>当项目被导出到 <code>requirements.txt</code> 时，uv 默认会以可编辑模式包含当前项目（和其他工作区成员），以便在其他环境中安装时，这些包的更改能立即反映。</p>
<p>此选项强制所有包以非可编辑模式安装。</p>
</dd><dt id="uv-export--no-extra"><a href="#uv-export--no-extra"><code>--no-extra</code></a> <i>no-extra</i></dt><dd><p>排除指定的可选依赖（如果已包含）。</p>
<p>可以与 <code>--all-extras</code> 结合使用以排除特定的 extras。</p>
</dd><dt id="uv-export--no-group"><a href="#uv-export--no-group"><code>--no-group</code></a> <i>no-group</i></dt><dd><p>排除指定的依赖组中的依赖。</p>
<p>可以与 <code>--all-groups</code> 结合使用以排除特定的组。</p>
</dd><dt id="uv-export--no-hashes"><a href="#uv-export--no-hashes"><code>--no-hashes</code></a></dt><dd><p>在导出的输出中省略哈希值</p>
</dd><dt id="uv-export--no-header"><a href="#uv-export--no-header"><code>--no-header</code></a></dt><dd><p>排除导出的输出顶部的注释头。</p>
<p>默认情况下，uv 会在输出的开头包含一个注释头，指示导出命令和 uv 版本。</p>
</dd><dt id="uv-export--no-index"><a href="#uv-export--no-index"><code>--no-index</code></a></dt><dd><p>忽略所有注册表索引（例如 PyPI），而是仅依赖直接 URL 依赖和通过 <code>--find-links</code> 提供的源。</p>
</dd><dt id="uv-export--no-python-downloads"><a href="#uv-export--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p></dd><dt id="uv-export--no-progress"><a href="#uv-export--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转指示器或进度条。</p>
</dd><dt id="uv-export--no-python-downloads"><a href="#uv-export--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p></dd><dt id="uv-export--no-sources"><a href="#uv-export--no-sources"><code>--no-sources</code></a></dt><dd><p>解析依赖时忽略 <code>tool.uv.sources</code> 表。用于根据符合标准的、可发布的包元数据进行锁定，而不是使用任何工作区、Git、URL 或本地路径源</p>
<p>也可以通过 <code>UV_NO_SOURCES</code> 环境变量设置。</p></dd><dt id="uv-export--no-sources-package"><a href="#uv-export--no-sources-package"><code>--no-sources-package</code></a> <i>no-sources-package</i></dt><dd><p>不为指定包使用 <code>tool.uv.sources</code> 表中的源 [env: <code>UV_NO_SOURCES_PACKAGE</code>=]</p>
</dd><dt id="uv-export--offline"><a href="#uv-export--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-export--only-dev"><a href="#uv-export--only-dev"><code>--only-dev</code></a></dt><dd><p>仅包含开发依赖组。</p>
<p>项目及其依赖将被省略。</p>
<p>此选项是 <code>--only-group dev</code> 的别名。隐含 <code>--no-default-groups</code>。</p>
</dd><dt id="uv-export--only-group"><a href="#uv-export--only-group"><code>--only-group</code></a> <i>only-group</i></dt><dd><p>仅包含来自指定依赖组的依赖。</p>
<p>项目及其依赖将被省略。</p>
<p>可以多次提供。隐含 <code>--no-default-groups</code>。</p>
</dd><dt id="uv-export--output-file"><a href="#uv-export--output-file"><code>--output-file</code></a>、<code>-o</code> <i>output-file</i></dt><dd><p>将导出的 requirements 写入给定文件</p>
</dd><dt id="uv-export--package"><a href="#uv-export--package"><code>--package</code></a> <i>package</i></dt><dd><p>导出工作区中特定包的依赖。</p>
<p>如果任何工作区成员不存在，uv 将退出并报错。</p>
</dd><dt id="uv-export--prerelease"><a href="#uv-export--prerelease"><code>--prerelease</code></a> <i>prerelease</i></dt><dd><p>考虑预发布（pre-release）版本时使用的策略。</p>
<p>默认情况下，uv 将接受仅发布预发布版本的包，以及声明的版本说明符中包含显式预发布标记的第一方依赖（<code>if-necessary-or-explicit</code>）。</p>
<p>也可以通过 <code>UV_PRERELEASE</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disallow</code>：禁止所有预发布版本</li>
<li><code>allow</code>：允许所有预发布版本</li>
<li><code>if-necessary</code>：如果包的所有版本都是预发布版本，则允许预发布版本</li>
<li><code>explicit</code>：对于版本要求中包含显式预发布标记的第一方包，允许预发布版本</li>
<li><code>if-necessary-or-explicit</code>：如果包的所有版本都是预发布版本，或者包的版本要求中包含显式预发布标记，则允许预发布版本</li>
</ul></dd><dt id="uv-export--project"><a href="#uv-export--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-export--prune"><a href="#uv-export--prune"><code>--prune</code></a> <i>package</i></dt><dd><p>从依赖树中修剪（prune）给定的包。</p>
<p>被修剪的包将从导出的 requirements 文件中排除，移除被修剪包后不再需要的任何依赖也将被排除。</p>
</dd><dt id="uv-export--python"><a href="#uv-export--python"><code>--python</code></a>、<code>-p</code> <i>python</i></dt><dd><p>解析期间使用的 Python 解释器。</p>
<p>当没有 wheel 时，需要 Python 解释器来构建源码分发包以确定包元数据。</p>
<p>如果未设置 <code>requires-python</code>，解释器也用作最低 Python 版本的回退值。</p>
<p>有关 Python 发现和支持的请求格式的详细信息，请参见 <a href="#uv-python">uv python</a>。</p>
<p>也可以通过 <code>UV_PYTHON</code> 环境变量设置。</p></dd><dt id="uv-export--quiet"><a href="#uv-export--quiet"><code>--quiet</code></a>、<code>-q</code></dt><dd><p>使用安静输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，uv 将不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-export--refresh"><a href="#uv-export--refresh"><code>--refresh</code></a></dt><dd><p>刷新所有缓存数据</p>
</dd><dt id="uv-export--refresh-package"><a href="#uv-export--refresh-package"><code>--refresh-package</code></a> <i>refresh-package</i></dt><dd><p>刷新特定包的缓存数据</p>
</dd><dt id="uv-export--resolution"><a href="#uv-export--resolution"><code>--resolution</code></a> <i>resolution</i></dt><dd><p>在给定包要求的不同兼容版本之间进行选择时使用的策略。</p>
<p>默认情况下，uv 将使用每个包的最新兼容版本（<code>highest</code>）。</p>
<p>也可以通过 <code>UV_RESOLUTION</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>highest</code>：解析每个包的最高兼容版本</li>
<li><code>lowest</code>：解析每个包的最低兼容版本</li>
<li><code>lowest-direct</code>：解析任何直接依赖的最低兼容版本，以及任何传递依赖的最高兼容版本</li>
</ul></dd><dt id="uv-export--script"><a href="#uv-export--script"><code>--script</code></a> <i>script</i></dt><dd><p>导出指定 PEP 723 Python 脚本的依赖，而不是当前项目的依赖。</p>
<p>如果提供，uv 将根据其内联元数据表（inline metadata table）解析依赖，遵循 PEP 723。</p>
</dd><dt id="uv-export--system-certs"><a href="#uv-export--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（特别是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能希望使用平台的原生证书存储，特别是如果您依赖系统证书存储中包含的企业信任根（例如，用于强制代理）。</p>
</dd><dt id="uv-export--upgrade"><a href="#uv-export--upgrade"><code>--upgrade</code></a>、<code>-U</code></dt><dd><p>允许包升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh</code></p>
</dd><dt id="uv-export--upgrade-group"><a href="#uv-export--upgrade-group"><code>--upgrade-group</code></a> <i>upgrade-group</i></dt><dd><p>允许依赖组中所有包的升级，忽略任何现有输出文件中的固定版本</p>
</dd><dt id="uv-export--upgrade-package"><a href="#uv-export--upgrade-package"><code>--upgrade-package</code></a>、<code>-P</code> <i>upgrade-package</i></dt><dd><p>允许特定包的升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-export--verbose"><a href="#uv-export--verbose"><code>--verbose</code></a>、<code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>
