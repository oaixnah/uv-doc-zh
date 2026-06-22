---
title: uv audit
description: uv audit 命令用于审计项目依赖，检查已知漏洞以及弃用、隔离等不良状态。默认审计项目中的所有附加依赖和依赖组，支持通过 ID 忽略特定漏洞、仅在修复可用前忽略漏洞。支持 OSV 漏洞查询服务，提供多种配置选项用于索引策略、Python 版本、平台限制等。本文档提供 uv audit 命令的完整 CLI 参考，包括所有参数、选项及其详细说明。
---

# uv audit

审计项目的依赖项。

审计会检查依赖项中的已知漏洞，以及弃用和隔离等"不良"状态。

默认情况下，会审计项目中的所有附加依赖（extras）和依赖组。要从审计中排除附加依赖和/或依赖组，请使用 `--no-extra`、`--no-group` 及相关选项。

<h3 class="cli-reference">用法</h3>

```
uv audit [OPTIONS]
```

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-audit--allow-insecure-host"><a href="#uv-audit--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可以提供多次。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您遭受中间人（MITM）攻击。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-audit--cache-dir"><a href="#uv-audit--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上默认为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-audit--color"><a href="#uv-audit--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 在写入终端时会自动检测对颜色的支持。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>:  仅当输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>:  无论检测到何种环境，始终启用彩色输出</li>
<li><code>never</code>:  禁用彩色输出</li>
</ul></dd><dt id="uv-audit--config-file"><a href="#uv-audit--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-audit--config-setting"><a href="#uv-audit--config-setting"><code>--config-setting</code></a>, <code>--config-settings</code>, <code>-C</code> <i>config-setting</i></dt><dd><p>传递给 PEP 517 构建后端的设置，以 <code>KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-audit--config-settings-package"><a href="#uv-audit--config-settings-package"><code>--config-settings-package</code></a>, <code>--config-settings-package</code> <i>config-settings-package</i></dt><dd><p>传递给特定包的 PEP 517 构建后端的设置，以 <code>PACKAGE:KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-audit--default-index"><a href="#uv-audit--default-index"><code>--default-index</code></a> <i>default-index</i></dt><dd><p>默认包索引的 URL（默认为：<a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式布局的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--index</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_DEFAULT_INDEX</code> 环境变量设置。</p></dd><dt id="uv-audit--directory"><a href="#uv-audit--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>运行命令前切换到给定目录。</p>
<p>相对路径以给定目录为基准进行解析。</p>
<p>如需仅更改项目根目录，请参见 <code>--project</code>。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-audit--exclude-newer"><a href="#uv-audit--exclude-newer"><code>--exclude-newer</code></a> <i>exclude-newer</i></dt><dd><p>将候选包限制为在给定日期之前上传的包。</p>
<p>日期会与每个分发包构件的上传时间进行比较（即每个文件上传到包索引的时间），而非包版本的发布日期。</p>
<p>接受 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、相同格式的本地日期（例如 <code>2006-12-02</code>，根据系统配置的时区解析）、"友好"时长（例如 <code>24 小时</code>、<code>1 周</code>、<code>30 天</code>）或 ISO 8601 时长（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>时长不遵守本地时区的语义，始终解析为固定的秒数，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月和年等日历单位。</p>
<p>也可以通过 <code>UV_EXCLUDE_NEWER</code> 环境变量设置。</p></dd><dt id="uv-audit--exclude-newer-package"><a href="#uv-audit--exclude-newer-package"><code>--exclude-newer-package</code></a> <i>exclude-newer-package</i></dt><dd><p>将特定包的候选包限制为在给定日期之前上传的包。</p>
<p>接受格式为 <code>PACKAGE=DATE</code> 的包-日期对，其中 <code>DATE</code> 是 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、相同格式的本地日期（例如 <code>2006-12-02</code>，根据系统配置的时区解析）、"友好"时长（例如 <code>24 小时</code>、<code>1 周</code>、<code>30 天</code>）或 ISO 8601 时长（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>时长不遵守本地时区的语义，始终解析为固定的秒数，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月和年等日历单位。</p>
<p>可为不同的包提供多次。</p>
</dd><dt id="uv-audit--extra-index-url"><a href="#uv-audit--extra-index-url"><code>--extra-index-url</code></a> <i>extra-index-url</i></dt><dd><p>（已弃用：请改用 <code>--index</code>）除了 <code>--index-url</code> 之外，还要使用的额外包索引 URL。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式布局的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于通过 <code>--index-url</code> 指定的索引（默认为 PyPI）。当提供多个 <code>--extra-index-url</code> 标志时，先提供的值优先级更高。</p>
<p>也可以通过 <code>UV_EXTRA_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-audit--find-links"><a href="#uv-audit--find-links"><code>--find-links</code></a>, <code>-f</code> <i>find-links</i></dt><dd><p>除了注册表索引中找到的候选分发包之外，还要搜索的位置。</p>
<p>如果是路径，目标必须是一个顶级包含 wheel 文件（<code>.whl</code>）或源码分发版（例如 <code>.tar.gz</code> 或 <code>.zip</code>）的目录。</p>
<p>如果是 URL，该页面必须包含符合上述格式的包文件扁平链接列表。</p>
<p>也可以通过 <code>UV_FIND_LINKS</code> 环境变量设置。</p></dd><dt id="uv-audit--fork-strategy"><a href="#uv-audit--fork-strategy"><code>--fork-strategy</code></a> <i>fork-strategy</i></dt><dd><p>在跨 Python 版本和平台选择给定包的多个版本时使用的策略。</p>
<p>默认情况下，uv 会优化为每个支持的 Python 版本（<code>requires-python</code>）选择每个包的最新版本，同时最大限度地减少跨平台选择的版本数量。</p>
<p>在 <code>fewest</code> 模式下，uv 会最大限度地减少每个包选择的版本数量，如果你选择那些较旧版本，它们兼容更广泛的支持 Python 版本或平台。</p>
<p>也可以通过 <code>UV_FORK_STRATEGY</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>fewest</code>:  优化为每个包选择最少数量的版本。如果较旧版本兼容更广泛的支持 Python 版本或平台，则可能优先选择较旧版本</li>
<li><code>requires-python</code>:  优化为每个支持的 Python 版本选择最新支持版本</li>
</ul></dd><dt id="uv-audit--frozen"><a href="#uv-audit--frozen"><code>--frozen</code></a></dt><dd><p>不锁定项目即可审计依赖项 [环境变量：UV_FROZEN=]</p>
<p>如果锁定文件缺失，uv 将退出并报错。</p>
</dd><dt id="uv-audit--help"><a href="#uv-audit--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助</p>
</dd><dt id="uv-audit--ignore"><a href="#uv-audit--ignore"><code>--ignore</code></a> <i>ignore</i></dt><dd><p>按 ID 忽略漏洞。</p>
<p>匹配任何提供 ID（包括别名）的漏洞将从审计结果中排除。</p>
<p>可以提供多次。</p>
</dd><dt id="uv-audit--ignore-until-fixed"><a href="#uv-audit--ignore-until-fixed"><code>--ignore-until-fixed</code></a> <i>ignore-until-fixed</i></dt><dd><p>按 ID 忽略漏洞，但仅在没有可用修复时忽略。</p>
<p>匹配任何提供 ID（包括别名）的漏洞，只要它们没有已知的修复版本，就会从审计结果中排除。一旦有修复版本可用，该漏洞将再次被报告。</p>
<p>可以提供多次。</p>
</dd><dt id="uv-audit--index"><a href="#uv-audit--index"><code>--index</code></a> <i>index</i></dt><dd><p>除了默认索引之外，解析依赖时要使用的 URL。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式布局的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于通过 <code>--default-index</code> 指定的索引（默认为 PyPI）。当提供多个 <code>--index</code> 标志时，先提供的值优先级更高。</p>
<p>不支持将索引名称作为值。在 Unix 系统上，相对路径必须使用 <code>./</code> 或 <code>../</code> 与索引名称区分，在 Windows 上必须使用 <code>.\\</code>、<code>..\\</code>、<code>./</code> 或 <code>../</code> 区分。</p>
<p>也可以通过 <code>UV_INDEX</code> 环境变量设置。</p></dd><dt id="uv-audit--index-strategy"><a href="#uv-audit--index-strategy"><code>--index-strategy</code></a> <i>index-strategy</i></dt><dd><p>针对多个索引 URL 解析时使用的策略。</p>
<p>默认情况下，uv 会在第一个包含给定包可用的索引处停止，将解析限制在第一个索引上存在的包（<code>first-index</code>）。这样可以防止"依赖混淆"攻击，即攻击者可以在备用索引下上传同名的恶意包。</p>
<p>也可以通过 <code>UV_INDEX_STRATEGY</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>first-index</code>:  仅使用第一个返回给定包名匹配结果的索引</li>
<li><code>unsafe-first-match</code>:  在所有索引中搜索每个包名，在耗尽第一个索引的所有版本后再移动到下一个</li>
<li><code>unsafe-best-match</code>:  在所有索引中搜索每个包名，优先选择找到的"最佳"版本。如果包版本在多个索引中存在，则仅查看第一个索引的条目</li>
</ul></dd><dt id="uv-audit--index-url"><a href="#uv-audit--index-url"><code>--index-url</code></a>, <code>-i</code> <i>index-url</i></dt><dd><p>（已弃用：请改用 <code>--default-index</code>）Python 包索引的 URL（默认为：<a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式布局的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--extra-index-url</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-audit--keyring-provider"><a href="#uv-audit--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>尝试使用 <code>keyring</code> 进行索引 URL 的身份验证。</p>
<p>目前，仅支持 <code>--keyring-provider subprocess</code>，它配置 uv 使用 <code>keyring</code> CLI 处理身份验证。</p>
<p>默认为 <code>disabled</code>。</p>
<p>也可以通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disabled</code>:  不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>:  使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-audit--link-mode"><a href="#uv-audit--link-mode"><code>--link-mode</code></a> <i>link-mode</i></dt><dd><p>从全局缓存安装包时使用的方法。</p>
<p>此选项仅在构建源码分发版时使用。</p>
<p>在 macOS 和 Linux 上默认为 <code>clone</code>（也称为写时复制），在 Windows 上默认为 <code>hardlink</code>。</p>
<p>警告：不推荐使用符号链接模式，因为它们会在缓存和目标环境之间产生紧密耦合。例如，清除缓存（<code>uv cache clean</code>）会通过删除底层源文件破坏所有已安装的包。请谨慎使用符号链接。</p>
<p>也可以通过 <code>UV_LINK_MODE</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>clone</code>:  从源克隆（即写时复制）包到目标位置</li>
<li><code>copy</code>:  从源复制包到目标位置</li>
<li><code>hardlink</code>:  从源硬链接包到目标位置</li>
<li><code>symlink</code>:  从源符号链接包到目标位置</li>
</ul></dd><dt id="uv-audit--locked"><a href="#uv-audit--locked"><code>--locked</code></a></dt><dd><p>断言 <code>uv.lock</code> 将保持不变 [环境变量：UV_LOCKED=]</p>
<p>要求锁定文件是最新的。如果锁定文件缺失或需要更新，uv 将退出并报错。</p>
</dd><dt id="uv-audit--managed-python"><a href="#uv-audit--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [环境变量：UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用它管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它会使用系统 Python 版本。此选项禁用使用系统 Python 版本。</p>
</dd><dt id="uv-audit--no-binary"><a href="#uv-audit--no-binary"><code>--no-binary</code></a></dt><dd><p>不安装预构建 wheel。</p>
<p>给定的包将从源码构建和安装。如果可用，解析器仍会使用预构建 wheel 提取包元数据。</p>
<p>也可以通过 <code>UV_NO_BINARY</code> 环境变量设置。</p></dd><dt id="uv-audit--no-binary-package"><a href="#uv-audit--no-binary-package"><code>--no-binary-package</code></a> <i>no-binary-package</i></dt><dd><p>特定包不安装预构建 wheel [环境变量：<code>UV_NO_BINARY_PACKAGE</code>=]</p>
</dd><dt id="uv-audit--no-build"><a href="#uv-audit--no-build"><code>--no-build</code></a></dt><dd><p>不构建源码分发版。</p>
<p>启用后，解析将不会运行任意 Python 代码。将重用已构建源码分发版的缓存 wheel，但需要构建分发包的操作将退出并报错。</p>
<p>也可以通过 <code>UV_NO_BUILD</code> 环境变量设置。</p></dd><dt id="uv-audit--no-build-isolation"><a href="#uv-audit--no-build-isolation"><code>--no-build-isolation</code></a></dt><dd><p>构建源码分发版时禁用隔离。</p>
<p>假设 PEP 518 指定的构建依赖已安装。</p>
<p>也可以通过 <code>UV_NO_BUILD_ISOLATION</code> 环境变量设置。</p></dd><dt id="uv-audit--no-build-isolation-package"><a href="#uv-audit--no-build-isolation-package"><code>--no-build-isolation-package</code></a> <i>no-build-isolation-package</i></dt><dd><p>构建特定包的源码分发版时禁用隔离。</p>
<p>假设包的构建依赖（由 PEP 518 指定）已安装。</p>
</dd><dt id="uv-audit--no-build-package"><a href="#uv-audit--no-build-package"><code>--no-build-package</code></a> <i>no-build-package</i></dt><dd><p>不构建特定包的源码分发版 [环境变量：<code>UV_NO_BUILD_PACKAGE</code>=]</p>
</dd><dt id="uv-audit--no-cache"><a href="#uv-audit--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，改为在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-audit--no-config"><a href="#uv-audit--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，会在当前目录、父目录或用户配置目录中发现配置文件。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-audit--no-default-groups"><a href="#uv-audit--no-default-groups"><code>--no-default-groups</code></a></dt><dd><p>不审计默认依赖组</p>
<p>也可以通过 <code>UV_NO_DEFAULT_GROUPS</code> 环境变量设置。</p></dd><dt id="uv-audit--no-dev"><a href="#uv-audit--no-dev"><code>--no-dev</code></a></dt><dd><p>不审计开发依赖组 [环境变量：UV_NO_DEV=]</p>
<p>此选项是 <code>--no-group dev</code> 的别名。如需排除所有默认组，请参见 <code>--no-default-groups</code>。</p>
<p>此选项仅在项目中运行时可用。</p>
</dd><dt id="uv-audit--no-extra"><a href="#uv-audit--no-extra"><code>--no-extra</code></a> <i>no-extra</i></dt><dd><p>不审计指定的可选依赖。</p>
<p>可以提供多次。</p>
</dd><dt id="uv-audit--no-group"><a href="#uv-audit--no-group"><code>--no-group</code></a> <i>no-group</i></dt><dd><p>不审计指定的依赖组 [环境变量：<code>UV_NO_GROUP</code>=]</p>
<p>可以提供多次。</p>
</dd><dt id="uv-audit--no-index"><a href="#uv-audit--no-index"><code>--no-index</code></a></dt><dd><p>忽略注册表索引（例如 PyPI），转而依赖直接 URL 依赖和通过 <code>--find-links</code> 提供的依赖</p>
</dd><dt id="uv-audit--no-managed-python"><a href="#uv-audit--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用使用 uv 管理的 Python 版本 [环境变量：UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-audit--no-progress"><a href="#uv-audit--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [环境变量：UV_NO_PROGRESS=]</p>
<p>例如，旋转指示器或进度条。</p>
</dd><dt id="uv-audit--no-python-downloads"><a href="#uv-audit--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-audit--only-group"><a href="#uv-audit--only-group"><code>--only-group</code></a> <i>only-group</i></dt><dd><p>仅审计指定的依赖组</p>
<p>可以提供多次。</p>
</dd><dt id="uv-audit--os"><a href="#uv-audit--os"><code>--os</code></a> <i>os</i></dt><dd><p>解析依赖时要定位的操作系统。</p>
<p>默认为当前系统的操作系统。</p>
<p>也可以通过 <code>UV_OS</code> 环境变量设置。</p>
</dd><dt id="uv-audit--platform"><a href="#uv-audit--platform"><code>--platform</code></a> <i>platform</i></dt><dd><p>解析依赖时要定位的平台。</p>
<p>接受任何 <a href="https://doc.rust-lang.org/nightly/std/env/consts/struct.OS.html">rustc 平台三元组</a>，例如 <code>x86_64-apple-darwin</code> 或 <code>aarch64-unknown-linux-gnu</code>。</p>
<p>也可以通过 <code>UV_PLATFORM</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>aarch64-apple-darwin</code>:  Apple Silicon macOS 平台</li>
<li><code>aarch64-unknown-linux-gnu</code>:  GNU 工具链下的 ARM64 Linux 平台</li>
<li><code>aarch64-unknown-linux-musl</code>:  musl 工具链下的 ARM64 Linux 平台</li>
<li><code>arm-unknown-linux-gnueabihf</code>:  GNU 工具链下的 ARMv6 Linux 平台</li>
<li><code>armv7-unknown-linux-gnueabihf</code>:  GNU 工具链下的 ARMv7 Linux 平台</li>
<li><code>i686-apple-darwin</code>:  Intel 32 位 macOS 平台</li>
<li><code>i686-unknown-linux-gnu</code>:  GNU 工具链下的 32 位 x86 Linux 平台</li>
<li><code>powerpc64-unknown-linux-gnu</code>:  GNU 工具链下的 64 位 PowerPC Linux（大端序）平台</li>
<li><code>powerpc64le-unknown-linux-gnu</code>:  GNU 工具链下的 64 位 PowerPC Linux（小端序）平台</li>
<li><code>riscv64gc-unknown-linux-gnu</code>:  GNU 工具链下的 RISC-V 64 GC Linux 平台</li>
<li><code>x86_64-apple-darwin</code>:  Intel macOS 平台</li>
<li><code>x86_64-pc-windows-msvc</code>:  64 位 Windows MSVC 平台</li>
<li><code>x86_64-unknown-linux-gnu</code>:  GNU 工具链下的 64 位 x86 Linux 平台</li>
<li><code>x86_64-unknown-linux-musl</code>:  musl 工具链下的 64 位 x86 Linux 平台</li>
<li><code>aarch64-apple-ios</code>:  iOS ARM64 平台</li>
<li><code>aarch64-apple-ios-sim</code>:  iOS 模拟器 ARM64 平台</li>
<li><code>aarch64-linux-android</code>:  Android ARM64 平台</li>
<li><code>x86_64-linux-android</code>:  Android x86_64 平台</li>
<li><code>x86_64-unknown-none</code>:  裸机 x86_64 平台</li>
<li><code>aarch64-unknown-none</code>:  裸机 ARM64 平台</li>
<li><code>thumbv7em-none-eabi</code>:  ARMv7-M FPU 裸机平台</li>
<li><code>thumbv8m.main-none-eabi</code>:  ARMv8-M 主裸机平台</li>
<li><code>wasm32-unknown-emscripten</code>:  Emscripten WebAssembly 平台</li>
<li><code>wasm32-unknown-unknown</code>:  通用 WebAssembly 平台</li>
<li><code>aarch64-manylinux_2_24</code>:  用于 <code>manylinux_2_24</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_25</code>:  用于 <code>manylinux_2_25</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_26</code>:  用于 <code>manylinux_2_26</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_27</code>:  用于 <code>manylinux_2_27</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_28</code>:  用于 <code>manylinux_2_28</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_29</code>:  用于 <code>manylinux_2_29</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_30</code>:  用于 <code>manylinux_2_30</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_31</code>:  用于 <code>manylinux_2_31</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_32</code>:  用于 <code>manylinux_2_32</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_33</code>:  用于 <code>manylinux_2_33</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_34</code>:  用于 <code>manylinux_2_34</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_35</code>:  用于 <code>manylinux_2_35</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_36</code>:  用于 <code>manylinux_2_36</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_37</code>:  用于 <code>manylinux_2_37</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_38</code>:  用于 <code>manylinux_2_38</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_39</code>:  用于 <code>manylinux_2_39</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_40</code>:  用于 <code>manylinux_2_40</code> 平台的 ARM64 目标</li>
<li><code>aarch64-linux-android</code>:  ARM64 Android 目标</li>
<li><code>x86_64-linux-android</code>:  x86_64 Android 目标</li>
<li><code>wasm32-pyodide2024</code>:  使用 Pyodide 2024 平台的 wasm32 目标。适用于 Python 3.12。参见 <a href="https://pyodide.org/en/stable/development/abi/312.html">https://pyodide.org/en/stable/development/abi/312.html</a></li>
<li><code>wasm32-pyodide2025</code>:  使用 Pyodide 2025 平台的 wasm32 目标。适用于 Python 3.13。参见 <a href="https://pyodide.org/en/stable/development/abi/313.html">https://pyodide.org/en/stable/development/abi/313.html</a></li>
<li><code>arm64-apple-ios</code>:  iOS 设备的 ARM64 目标</li>
<li><code>arm64-apple-ios-simulator</code>:  iOS 模拟器的 ARM64 目标</li>
<li><code>x86_64-apple-ios-simulator</code>:  iOS 模拟器的 x86_64 目标</li>
</ul></dd><dt id="uv-audit--python-version"><a href="#uv-audit--python-version"><code>--python-version</code></a> <i>python-version</i></dt><dd><p>审计时使用的 Python 版本。</p>
<p>例如，传递 <code>--python-version 3.10</code> 以审计在 Python 3.10 上安装时会包含的依赖项。</p>
<p>默认为发现的 Python 解释器版本。</p>
</dd><dt id="uv-audit--quiet"><a href="#uv-audit--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用安静输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，在此模式下 uv 不会向标准输出写入任何内容。</p>
</dd><dt id="uv-audit--resolution"><a href="#uv-audit--resolution"><code>--resolution</code></a> <i>resolution</i></dt><dd><p>在给定包需求的不同兼容版本之间选择时使用的策略。</p>
<p>默认情况下，uv 会使用每个包的最新兼容版本（<code>highest</code>）。</p>
<p>也可以通过 <code>UV_RESOLUTION</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>highest</code>:  解析每个包的最高兼容版本</li>
<li><code>lowest</code>:  解析每个包的最低兼容版本</li>
<li><code>lowest-direct</code>:  解析所有直接依赖的最低兼容版本，以及所有传递依赖的最高兼容版本</li>
</ul></dd><dt id="uv-audit--script"><a href="#uv-audit--script"><code>--script</code></a> <i>script</i></dt><dd><p>审计指定的 PEP 723 Python 脚本，而非当前项目。</p>
<p>指定的脚本必须已锁定，即在审计之前需要使用 <code>uv lock --script &lt;script&gt;</code> 进行锁定。</p>
</dd><dt id="uv-audit--service-format"><a href="#uv-audit--service-format"><code>--service-format</code></a> <i>service-format</i></dt><dd><p>漏洞查询使用的服务格式。</p>
<p>每个服务格式都有默认 URL，可以通过 <code>--service-url</code> 更改。默认值为：</p>
<ul>
<li>OSV: <a href="https://api.osv.dev/">https://api.osv.dev/</a></li>
</ul>
<p>[默认：osv]</p><p>可选值：</p>
<ul>
<li><code>osv</code></li>
</ul></dd><dt id="uv-audit--service-url"><a href="#uv-audit--service-url"><code>--service-url</code></a> <i>service-url</i></dt><dd><p>漏洞服务 API 端点的 URL。</p>
<p>如果未提供，将使用所选服务的默认 URL。</p>
<p>服务需要使用 OSV 协议，除非 <code>--service-format</code> 请求了不同的格式。</p>
</dd><dt id="uv-audit--system-certs"><a href="#uv-audit--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台原生证书存储加载 TLS 证书 [环境变量：UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能需要使用平台原生证书存储，特别是当您依赖包含在系统证书存储中的企业信任根（例如，强制代理）时。</p>
</dd><dt id="uv-audit--upgrade"><a href="#uv-audit--upgrade"><code>--upgrade</code></a>, <code>-U</code></dt><dd><p>允许包升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh</code></p>
</dd><dt id="uv-audit--upgrade-group"><a href="#uv-audit--upgrade-group"><code>--upgrade-group</code></a> <i>upgrade-group</i></dt><dd><p>允许依赖组中所有包升级，忽略任何现有输出文件中的固定版本</p>
</dd><dt id="uv-audit--upgrade-package"><a href="#uv-audit--upgrade-package"><code>--upgrade-package</code></a>, <code>-P</code> <i>upgrade-package</i></dt><dd><p>允许特定包升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-audit--verbose"><a href="#uv-audit--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>你可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>
