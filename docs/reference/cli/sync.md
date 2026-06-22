---
title: uv sync
description: uv sync 是 uv 项目中用于同步项目环境的核心命令。它根据锁文件确保所有项目依赖项都已正确安装和更新，支持虚拟环境管理、依赖组、可选依赖、平台交叉编译等多种配置选项，帮助开发者快速搭建和维护一致的 Python 开发环境。
---

# uv sync

更新项目的环境。

同步操作确保所有项目依赖项已安装并与锁文件（lockfile）保持一致。

默认情况下，uv 会执行精确同步：移除那些未被声明为项目依赖项的包。使用 `--inexact` 标志可以保留多余的包。请注意，如果多余的包与项目依赖项冲突，它仍会被移除。此外，如果使用了 `--no-build-isolation`，uv 将不会移除多余的包，以避免移除可能的构建依赖项。

如果项目虚拟环境（`.venv`）不存在，它将被创建。

除非提供了 `--locked` 或 `--frozen` 标志，否则项目在同步之前会重新锁定。

uv 将在当前目录或任何父目录中搜索项目。如果找不到项目，uv 将退出并报错。

请注意，从锁文件安装时，uv 不会对已撤回（yanked）的包版本发出警告。

<h3 class="cli-reference">Usage</h3>

```
uv sync [OPTIONS]
```

<h3 class="cli-reference">Options</h3>

<dl class="cli-reference"><dt id="uv-sync--active"><a href="#uv-sync--active"><code>--active</code></a></dt><dd><p>将依赖项同步到激活的虚拟环境。</p>
<p>如果设置了 <code>VIRTUAL_ENV</code> 环境变量，uv 将优先使用激活的虚拟环境，而不是创建或更新项目或脚本的虚拟环境。</p>
</dd><dt id="uv-sync--all-extras"><a href="#uv-sync--all-extras"><code>--all-extras</code></a></dt><dd><p>包含所有可选依赖项。</p>
<p>当 <code>tool.uv.conflicts</code> 中声明了两个或多个冲突的 extras 时，使用此标志将始终导致错误。</p>
<p>请注意，所有可选依赖项始终包含在解析中；此选项仅影响要安装的包的选择。</p>
</dd><dt id="uv-sync--all-groups"><a href="#uv-sync--all-groups"><code>--all-groups</code></a></dt><dd><p>包含所有依赖组中的依赖项。</p>
<p>可以使用 <code>--no-group</code> 排除特定组。</p>
</dd><dt id="uv-sync--all-packages"><a href="#uv-sync--all-packages"><code>--all-packages</code></a></dt><dd><p>同步工作区中的所有包。</p>
<p>工作区环境（<code>.venv</code>）将更新以包含所有工作区成员。</p>
<p>通过 <code>--extra</code>、<code>--group</code> 或相关选项指定的任何 extras 或组将应用于所有工作区成员。</p>
</dd><dt id="uv-sync--allow-insecure-host"><a href="#uv-sync--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您遭受中间人攻击（MITM）。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-sync--cache-dir"><a href="#uv-sync--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录路径。</p>
<p>默认情况下，在 macOS 和 Linux 上为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-sync--check"><a href="#uv-sync--check"><code>--check</code></a></dt><dd><p>检查 Python 环境是否与项目同步。</p>
<p>如果环境不是最新的，uv 将退出并报错。</p>
</dd><dt id="uv-sync--color"><a href="#uv-sync--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 在写入终端时会自动检测颜色支持。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>:  仅当输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>:  无论检测到的环境如何，都启用彩色输出</li>
<li><code>never</code>:  禁用彩色输出</li>
</ul></dd><dt id="uv-sync--compile-bytecode"><a href="#uv-sync--compile-bytecode"><code>--compile-bytecode</code></a>, <code>--compile</code></dt><dd><p>安装后将 Python 文件编译为字节码。</p>
<p>默认情况下，uv 不会将 Python（<code>.py</code>）文件编译为字节码（<code>__pycache__/*.pyc</code>）；而是在第一次导入模块时延迟编译。对于启动时间至关重要的使用场景，例如 CLI 应用程序和 Docker 容器，启用此选项可以用更长的安装时间换取更快的启动速度。</p>
<p>启用后，uv 会为了一致性处理整个 site-packages 目录（包括当前操作未修改的包）。与 pip 一样，它也会忽略错误。</p>
<p>也可以通过 <code>UV_COMPILE_BYTECODE</code> 环境变量设置。</p></dd><dt id="uv-sync--config-file"><a href="#uv-sync--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用作配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许使用。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-sync--config-setting"><a href="#uv-sync--config-setting"><code>--config-setting</code></a>, <code>--config-settings</code>, <code>-C</code> <i>config-setting</i></dt><dd><p>传递给 PEP 517 构建后端的设置，格式为 <code>键=值</code> 对</p>
</dd><dt id="uv-sync--config-settings-package"><a href="#uv-sync--config-settings-package"><code>--config-settings-package</code></a>, <code>--config-settings-package</code> <i>config-settings-package</i></dt><dd><p>传递给特定包的 PEP 517 构建后端的设置，格式为 <code>包名:键=值</code> 对</p>
</dd><dt id="uv-sync--default-index"><a href="#uv-sync--default-index"><code>--default-index</code></a> <i>default-index</i></dt><dd><p>默认包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--index</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_DEFAULT_INDEX</code> 环境变量设置。</p></dd><dt id="uv-sync--directory"><a href="#uv-sync--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到给定的目录。</p>
<p>相对路径以给定的目录为基准进行解析。</p>
<p>参见 <code>--project</code> 以仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-sync--dry-run"><a href="#uv-sync--dry-run"><code>--dry-run</code></a></dt><dd><p>执行预演（dry run），不写入锁文件或修改项目环境。</p>
<p>在预演模式下，uv 将解析项目的依赖项并报告锁文件和项目环境的预期变更，但不会修改任何一方。</p>
</dd><dt id="uv-sync--exclude-newer"><a href="#uv-sync--exclude-newer"><code>--exclude-newer</code></a> <i>exclude-newer</i></dt><dd><p>将候选包限制为在给定日期之前上传的版本。</p>
<p>日期是与每个分发作品的<em>上传时间</em>（即每个文件上传到包索引的时间）进行比较，而不是与包版本的发布日期进行比较。</p>
<p>接受 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、相同格式的本地日期（例如 <code>2006-12-02</code>，基于系统配置的时区解析）、&quot;友好&quot;持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不遵循本地时区的语义，始终以固定秒数解析，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月和年等日历单位。</p>
<p>也可以通过 <code>UV_EXCLUDE_NEWER</code> 环境变量设置。</p></dd><dt id="uv-sync--exclude-newer-package"><a href="#uv-sync--exclude-newer-package"><code>--exclude-newer-package</code></a> <i>exclude-newer-package</i></dt><dd><p>将特定包的候选版本限制为在给定日期之前上传的版本。</p>
<p>接受格式为 <code>包名=日期</code> 的包-日期对，其中 <code>日期</code> 是 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、相同格式的本地日期（例如 <code>2006-12-02</code>，基于系统配置的时区解析）、&quot;友好&quot;持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不遵循本地时区的语义，始终以固定秒数解析，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月和年等日历单位。</p>
<p>可以为不同的包多次提供。</p>
</dd><dt id="uv-sync--extra"><a href="#uv-sync--extra"><code>--extra</code></a> <i>extra</i></dt><dd><p>包含指定 extra 名称的可选依赖项。</p>
<p>可以多次提供。</p>
<p>当指定了多个 extras 或组且它们出现在 <code>tool.uv.conflicts</code> 中时，uv 将报告错误。</p>
<p>请注意，所有可选依赖项始终包含在解析中；此选项仅影响要安装的包的选择。</p>
</dd><dt id="uv-sync--extra-index-url"><a href="#uv-sync--extra-index-url"><code>--extra-index-url</code></a> <i>extra-index-url</i></dt><dd><p>（已弃用：请改用 <code>--index</code>）除 <code>--index-url</code> 之外要使用的额外包索引 URL。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--index-url</code>（默认为 PyPI）指定的索引。当提供多个 <code>--extra-index-url</code> 标志时，较早的值优先级更高。</p>
<p>也可以通过 <code>UV_EXTRA_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-sync--find-links"><a href="#uv-sync--find-links"><code>--find-links</code></a>, <code>-f</code> <i>find-links</i></dt><dd><p>搜索候选分发作品的位置，作为注册表索引之外的补充来源。</p>
<p>如果是路径，目标必须是一个目录，顶层包含作为 wheel 文件（<code>.whl</code>）或源代码分发（例如 <code>.tar.gz</code> 或 <code>.zip</code>）的包。</p>
<p>如果是 URL，页面必须包含一个扁平列表，列出符合上述格式的包文件链接。</p>
<p>也可以通过 <code>UV_FIND_LINKS</code> 环境变量设置。</p></dd><dt id="uv-sync--fork-strategy"><a href="#uv-sync--fork-strategy"><code>--fork-strategy</code></a> <i>fork-strategy</i></dt><dd><p>在跨 Python 版本和平台选择给定包的多个版本时使用的策略。</p>
<p>默认情况下，uv 会优化为每个受支持的 Python 版本（<code>requires-python</code>）选择每个包的最新版本，同时最小化跨平台的选定版本数量。</p>
<p>在 <code>fewest</code> 策略下，uv 会最小化每个包的选定版本数量，倾向于选择与更广泛的受支持 Python 版本或平台兼容的较旧版本。</p>
<p>也可以通过 <code>UV_FORK_STRATEGY</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>fewest</code>:  优化为每个包选择最少数量的版本。如果较旧版本与更广泛的受支持 Python 版本或平台兼容，则可能优先选择它们</li>
<li><code>requires-python</code>:  优化为每个受支持的 Python 版本选择每个包的最新支持版本</li>
</ul></dd><dt id="uv-sync--frozen"><a href="#uv-sync--frozen"><code>--frozen</code></a></dt><dd><p>同步而不更新 <code>uv.lock</code> 文件 [env: UV_FROZEN=]</p>
<p>不检查锁文件是否为最新，而是将锁文件中的版本作为唯一真实来源。如果锁文件缺失，uv 将退出并报错。如果 <code>pyproject.toml</code> 中包含尚未纳入锁文件的依赖项变更，这些变更将不会反映在环境中。</p>
</dd><dt id="uv-sync--group"><a href="#uv-sync--group"><code>--group</code></a> <i>group</i></dt><dd><p>包含指定依赖组中的依赖项。</p>
<p>当指定了多个 extras 或组且它们出现在 <code>tool.uv.conflicts</code> 中时，uv 将报告错误。</p>
<p>可以多次提供。</p>
</dd><dt id="uv-sync--help"><a href="#uv-sync--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助信息</p>
</dd><dt id="uv-sync--index"><a href="#uv-sync--index"><code>--index</code></a> <i>index</i></dt><dd><p>解析依赖项时使用的 URL，作为默认索引的补充。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--default-index</code>（默认为 PyPI）指定的索引。当提供多个 <code>--index</code> 标志时，较早的值优先级更高。</p>
<p>不支持索引名称作为值。相对路径必须通过 <code>./</code> 或 <code>../</code>（Unix）或 <code>.\\</code>、<code>..\\</code>、<code>./</code> 或 <code>../</code>（Windows）与索引名称区分开来。</p>
<p>也可以通过 <code>UV_INDEX</code> 环境变量设置。</p></dd><dt id="uv-sync--index-strategy"><a href="#uv-sync--index-strategy"><code>--index-strategy</code></a> <i>index-strategy</i></dt><dd><p>在多个索引 URL 之间进行解析时使用的策略。</p>
<p>默认情况下，uv 会在第一个找到给定包的索引处停止，并将解析限制为该第一个索引上存在的包（<code>first-index</code>）。这可以防止&quot;依赖混淆&quot;攻击，即攻击者可以在备用索引上以相同名称上传恶意包。</p>
<p>也可以通过 <code>UV_INDEX_STRATEGY</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>first-index</code>:  仅使用第一个返回给定包名匹配结果的索引</li>
<li><code>unsafe-first-match</code>:  在所有索引中搜索每个包名，在移动到下一个索引之前穷尽第一个索引的版本</li>
<li><code>unsafe-best-match</code>:  在所有索引中搜索每个包名，优先选择找到的&quot;最佳&quot;版本。如果一个包版本存在于多个索引中，则仅查看第一个索引的条目</li>
</ul></dd><dt id="uv-sync--index-url"><a href="#uv-sync--index-url"><code>--index-url</code></a>, <code>-i</code> <i>index-url</i></dt><dd><p>（已弃用：请改用 <code>--default-index</code>）Python 包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--extra-index-url</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-sync--inexact"><a href="#uv-sync--inexact"><code>--inexact</code></a>, <code>--no-exact</code></dt><dd><p>不移除环境中存在的多余包。</p>
<p>启用后，uv 只会进行满足需求所需的最小变更。默认情况下，同步会从环境中移除任何多余的包</p>
</dd><dt id="uv-sync--keyring-provider"><a href="#uv-sync--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>尝试使用 <code>keyring</code> 进行索引 URL 的身份验证。</p>
<p>目前仅支持 <code>--keyring-provider subprocess</code>，它将 uv 配置为使用 <code>keyring</code> CLI 处理身份验证。</p>
<p>默认值为 <code>disabled</code>。</p>
<p>也可以通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disabled</code>:  不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>:  使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-sync--link-mode"><a href="#uv-sync--link-mode"><code>--link-mode</code></a> <i>link-mode</i></dt><dd><p>从全局缓存安装包时使用的方法。</p>
<p>在 macOS 和 Linux 上默认为 <code>clone</code>（也称为写时复制，Copy-on-Write），在 Windows 上默认为 <code>hardlink</code>。</p>
<p>警告：不建议使用 symlink 链接模式，因为它会在缓存和目标环境之间产生紧密耦合。例如，清除缓存（<code>uv cache clean</code>）将因移除底层源文件而破坏所有已安装的包。请谨慎使用符号链接。</p>
<p>也可以通过 <code>UV_LINK_MODE</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>clone</code>:  从源克隆（即写时复制）包到目标位置</li>
<li><code>copy</code>:  从源复制包到目标位置</li>
<li><code>hardlink</code>:  从源硬链接包到目标位置</li>
<li><code>symlink</code>:  从源符号链接包到目标位置</li>
</ul></dd><dt id="uv-sync--locked"><a href="#uv-sync--locked"><code>--locked</code></a></dt><dd><p>断言 <code>uv.lock</code> 将保持不变 [env: UV_LOCKED=]</p>
<p>要求锁文件是最新的。如果锁文件缺失或需要更新，uv 将退出并报错。</p>
</dd><dt id="uv-sync--managed-python"><a href="#uv-sync--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 倾向于使用它管理的 Python 版本。然而，如果没有安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-sync--no-binary"><a href="#uv-sync--no-binary"><code>--no-binary</code></a></dt><dd><p>不安装预构建的 wheel。</p>
<p>给定的包将从源代码构建并安装。解析器仍会使用预构建的 wheel 提取包元数据（如果可用）。</p>
<p>也可以通过 <code>UV_NO_BINARY</code> 环境变量设置。</p></dd><dt id="uv-sync--no-binary-package"><a href="#uv-sync--no-binary-package"><code>--no-binary-package</code></a> <i>no-binary-package</i></dt><dd><p>不安装特定包的预构建 wheel [env: <code>UV_NO_BINARY_PACKAGE</code>=]</p>
</dd><dt id="uv-sync--no-build"><a href="#uv-sync--no-build"><code>--no-build</code></a></dt><dd><p>不构建源代码分发（source distributions）。</p>
<p>启用后，解析将不会运行任意 Python 代码。已构建的源代码分发的缓存 wheel 将被重用，但需要构建分发的操作将退出并报错。</p>
<p>也可以通过 <code>UV_NO_BUILD</code> 环境变量设置。</p></dd><dt id="uv-sync--no-build-isolation"><a href="#uv-sync--no-build-isolation"><code>--no-build-isolation</code></a></dt><dd><p>构建源代码分发时禁用隔离。</p>
<p>假设 PEP 518 指定的构建依赖项已安装。</p>
<p>也可以通过 <code>UV_NO_BUILD_ISOLATION</code> 环境变量设置。</p></dd><dt id="uv-sync--no-build-isolation-package"><a href="#uv-sync--no-build-isolation-package"><code>--no-build-isolation-package</code></a> <i>no-build-isolation-package</i></dt><dd><p>构建特定包的源代码分发时禁用隔离。</p>
<p>假设该包的 PEP 518 指定的构建依赖项已安装。</p>
</dd><dt id="uv-sync--no-build-package"><a href="#uv-sync--no-build-package"><code>--no-build-package</code></a> <i>no-build-package</i></dt><dd><p>不构建特定包的源代码分发 [env: <code>UV_NO_BUILD_PACKAGE</code>=]</p>
</dd><dt id="uv-sync--no-cache"><a href="#uv-sync--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-sync--no-config"><a href="#uv-sync--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-sync--no-default-groups"><a href="#uv-sync--no-default-groups"><code>--no-default-groups</code></a></dt><dd><p>忽略默认依赖组。</p>
<p>默认情况下，uv 包含 <code>tool.uv.default-groups</code> 中定义的组。此选项禁用该行为，但仍可通过 <code>--group</code> 包含特定组。</p>
<p>也可以通过 <code>UV_NO_DEFAULT_GROUPS</code> 环境变量设置。</p></dd><dt id="uv-sync--no-dev"><a href="#uv-sync--no-dev"><code>--no-dev</code></a></dt><dd><p>禁用开发依赖组 [env: UV_NO_DEV=]</p>
<p>此选项是 <code>--no-group dev</code> 的别名。参见 <code>--no-default-groups</code> 以禁用所有默认组。</p>
</dd><dt id="uv-sync--no-editable"><a href="#uv-sync--no-editable"><code>--no-editable</code></a></dt><dd><p>将所有可编辑依赖项（包括项目和任何工作区成员）以非可编辑模式安装 [env: UV_NO_EDITABLE=]</p>
</dd><dt id="uv-sync--no-editable-package"><a href="#uv-sync--no-editable-package"><code>--no-editable-package</code></a> <i>no-editable-package</i></dt><dd><p>将指定的可编辑包以非可编辑模式安装</p>
</dd><dt id="uv-sync--no-extra"><a href="#uv-sync--no-extra"><code>--no-extra</code></a> <i>no-extra</i></dt><dd><p>在提供了 <code>--all-extras</code> 时，排除指定的可选依赖项。</p>
<p>可以多次提供。</p>
</dd><dt id="uv-sync--no-group"><a href="#uv-sync--no-group"><code>--no-group</code></a> <i>no-group</i></dt><dd><p>禁用指定的依赖组 [env: <code>UV_NO_GROUP</code>=]</p>
<p>此选项始终优先于默认组、<code>--all-groups</code> 和 <code>--group</code>。</p>
<p>可以多次提供。</p>
</dd><dt id="uv-sync--no-index"><a href="#uv-sync--no-index"><code>--no-index</code></a></dt><dd><p>忽略注册表索引（例如 PyPI），仅依赖直接 URL 依赖项和通过 <code>--find-links</code> 提供的依赖项</p>
</dd><dt id="uv-sync--no-install-local"><a href="#uv-sync--no-install-local"><code>--no-install-local</code></a></dt><dd><p>不安装本地路径依赖项 [env: UV_NO_INSTALL_LOCAL=]</p>
<p>跳过当前项目、工作区成员和任何其他本地（路径或可编辑）包。仅安装远程/索引的依赖项。在 Docker 构建中很有用，可以先缓存大型第三方依赖项，然后单独分层安装本地包。</p>
<p>反向选项 <code>--only-install-local</code> 可用于<em>仅</em>安装本地包，排除所有远程依赖项。</p>
</dd><dt id="uv-sync--no-install-package"><a href="#uv-sync--no-install-package"><code>--no-install-package</code></a> <i>no-install-package</i></dt><dd><p>不安装指定的包。</p>
<p>默认情况下，项目的所有依赖项都会安装到环境中。<code>--no-install-package</code> 选项允许排除特定包。请注意，这可能导致环境损坏，应谨慎使用。</p>
<p>反向选项 <code>--only-install-package</code> 可用于<em>仅</em>安装指定的包，排除所有其他包。</p>
</dd><dt id="uv-sync--no-install-project"><a href="#uv-sync--no-install-project"><code>--no-install-project</code></a></dt><dd><p>不安装当前项目 [env: UV_NO_INSTALL_PROJECT=]</p>
<p>默认情况下，当前项目及其所有依赖项都会安装到环境中。<code>--no-install-project</code> 选项允许排除项目本身，但其所有依赖项仍会被安装。这在构建 Docker 镜像等场景中特别有用，将项目与其依赖项分开安装可以实现最佳的层缓存。</p>
<p>反向选项 <code>--only-install-project</code> 可用于<em>仅</em>安装项目本身，排除所有依赖项。</p>
</dd><dt id="uv-sync--no-install-workspace"><a href="#uv-sync--no-install-workspace"><code>--no-install-workspace</code></a></dt><dd><p>不安装任何工作区成员，包括根项目 [env: UV_NO_INSTALL_WORKSPACE=]</p>
<p>默认情况下，所有工作区成员及其依赖项都会安装到环境中。<code>--no-install-workspace</code> 选项允许排除所有工作区成员，同时保留其依赖项。这在构建 Docker 镜像等场景中特别有用，将工作区与其依赖项分开安装可以实现最佳的层缓存。</p>
<p>反向选项 <code>--only-install-workspace</code> 可用于<em>仅</em>安装工作区成员，排除所有其他依赖项。</p>
</dd><dt id="uv-sync--no-managed-python"><a href="#uv-sync--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用 uv 管理的 Python 版本的使用 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-sync--no-progress"><a href="#uv-sync--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转动画或进度条。</p>
</dd><dt id="uv-sync--no-python-downloads"><a href="#uv-sync--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-sync--no-sources"><a href="#uv-sync--no-sources"><code>--no-sources</code></a></dt><dd><p>解析依赖项时忽略 <code>tool.uv.sources</code> 表。用于基于符合标准的、可发布的包元数据进行锁定，而不使用任何工作区、Git、URL 或本地路径源</p>
<p>也可以通过 <code>UV_NO_SOURCES</code> 环境变量设置。</p></dd><dt id="uv-sync--no-sources-package"><a href="#uv-sync--no-sources-package"><code>--no-sources-package</code></a> <i>no-sources-package</i></dt><dd><p>不为指定包使用 <code>tool.uv.sources</code> 表中的源 [env: <code>UV_NO_SOURCES_PACKAGE</code>=]</p>
</dd><dt id="uv-sync--offline"><a href="#uv-sync--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-sync--only-dev"><a href="#uv-sync--only-dev"><code>--only-dev</code></a></dt><dd><p>仅包含开发依赖组。</p>
<p>项目及其依赖项将被省略。</p>
<p>此选项是 <code>--only-group dev</code> 的别名。隐含 <code>--no-default-groups</code>。</p>
</dd><dt id="uv-sync--only-group"><a href="#uv-sync--only-group"><code>--only-group</code></a> <i>only-group</i></dt><dd><p>仅包含指定依赖组中的依赖项。</p>
<p>项目及其依赖项将被省略。</p>
<p>可以多次提供。隐含 <code>--no-default-groups</code>。</p>
</dd><dt id="uv-sync--output-format"><a href="#uv-sync--output-format"><code>--output-format</code></a> <i>output-format</i></dt><dd><p>选择输出格式</p>
<p>[默认值: text]</p><p>可选值：</p>
<ul>
<li><code>text</code>:  以人类可读格式显示结果</li>
<li><code>json</code>:  以 JSON 格式显示结果</li>
</ul></dd><dt id="uv-sync--package"><a href="#uv-sync--package"><code>--package</code></a> <i>package</i></dt><dd><p>为工作区中的特定包进行同步。</p>
<p>工作区环境（<code>.venv</code>）将更新以反映指定工作区成员包所声明的依赖项子集。</p>
<p>如果任何工作区成员不存在，uv 将退出并报错。</p>
</dd><dt id="uv-sync--prerelease"><a href="#uv-sync--prerelease"><code>--prerelease</code></a> <i>prerelease</i></dt><dd><p>考虑预发布版本时使用的策略。</p>
<p>默认情况下，uv 会接受那些<em>仅</em>发布预发布版本的包，以及在其声明的版本说明符中包含显式预发布标记的第一方需求（<code>if-necessary-or-explicit</code>）。</p>
<p>也可以通过 <code>UV_PRERELEASE</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disallow</code>:  禁止所有预发布版本</li>
<li><code>allow</code>:  允许所有预发布版本</li>
<li><code>if-necessary</code>:  如果某个包的所有版本都是预发布版本，则允许预发布版本</li>
<li><code>explicit</code>:  对于在其版本需求中带有显式预发布标记的第一方包，允许预发布版本</li>
<li><code>if-necessary-or-explicit</code>:  如果某个包的所有版本都是预发布版本，或者该包在其版本需求中带有显式预发布标记，则允许预发布版本</li>
</ul></dd><dt id="uv-sync--project"><a href="#uv-sync--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>在 <code>uv pip</code> 接口中使用时，此设置无效。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-sync--python"><a href="#uv-sync--python"><code>--python</code></a>, <code>-p</code> <i>python</i></dt><dd><p>用于项目环境的 Python 解释器。</p>
<p>默认情况下，使用满足项目 <code>requires-python</code> 约束的第一个解释器。</p>
<p>如果提供了虚拟环境中的 Python 解释器，则不会将包同步到给定环境。该解释器将用于在项目中创建虚拟环境。</p>
<p>有关 Python 发现和支持的请求格式的详细信息，请参见 <a href="#uv-python">uv python</a>。</p>
<p>也可以通过 <code>UV_PYTHON</code> 环境变量设置。</p></dd><dt id="uv-sync--python-platform"><a href="#uv-sync--python-platform"><code>--python-platform</code></a> <i>python-platform</i></dt><dd><p>应安装需求的目标平台。</p>
<p>表示为&quot;目标三元组&quot;，一个描述目标平台的 CPU、供应商和操作系统名称的字符串，例如 <code>x86_64-unknown-linux-gnu</code> 或 <code>aarch64-apple-darwin</code>。</p>
<p>当目标为 macOS（Darwin）时，默认最低版本为 <code>13.0</code>。使用 <code>MACOSX_DEPLOYMENT_TARGET</code> 指定不同的最低版本，例如 <code>14.0</code>。</p>
<p>当目标为 iOS 时，默认最低版本为 <code>13.0</code>。使用 <code>IPHONEOS_DEPLOYMENT_TARGET</code> 指定不同的最低版本，例如 <code>14.0</code>。</p>
<p>当目标为 Android 时，默认最低 Android API 级别为 <code>24</code>。使用 <code>ANDROID_API_LEVEL</code> 指定不同的最低版本，例如 <code>26</code>。</p>
<p>警告：指定后，uv 将选择与<em>目标</em>平台兼容的 wheel；因此，安装的分发作品可能与<em>当前</em>平台不兼容。反之，从源代码构建的任何分发作品可能与<em>目标</em>平台不兼容，因为它们是为<em>当前</em>平台构建的。<code>--python-platform</code> 选项适用于高级使用场景。</p>
<p>可选值：</p>
<ul>
<li><code>windows</code>:  <code>x86_64-pc-windows-msvc</code> 的别名，Windows 的默认目标</li>
<li><code>linux</code>:  <code>x86_64-unknown-linux-gnu</code> 的别名，Linux 的默认目标</li>
<li><code>macos</code>:  <code>aarch64-apple-darwin</code> 的别名，macOS 的默认目标</li>
<li><code>x86_64-pc-windows-msvc</code>:  64 位 x86 Windows 目标</li>
<li><code>aarch64-pc-windows-msvc</code>:  ARM64 Windows 目标</li>
<li><code>i686-pc-windows-msvc</code>:  32 位 x86 Windows 目标</li>
<li><code>x86_64-unknown-linux-gnu</code>:  x86 Linux 目标。相当于 <code>x86_64-manylinux_2_28</code></li>
<li><code>aarch64-apple-darwin</code>:  基于 ARM 的 macOS 目标，见于 Apple Silicon 设备</li>
<li><code>x86_64-apple-darwin</code>:  x86 macOS 目标</li>
<li><code>aarch64-unknown-linux-gnu</code>:  ARM64 Linux 目标。相当于 <code>aarch64-manylinux_2_28</code></li>
<li><code>aarch64-unknown-linux-musl</code>:  ARM64 Linux 目标（musl）</li>
<li><code>x86_64-unknown-linux-musl</code>:  <code>x86_64</code> Linux 目标（musl）</li>
<li><code>riscv64-unknown-linux</code>:  RISCV64 Linux 目标</li>
<li><code>x86_64-manylinux2014</code>:  <code>manylinux2014</code> 平台的 <code>x86_64</code> 目标。相当于 <code>x86_64-manylinux_2_17</code></li>
<li><code>x86_64-manylinux_2_17</code>:  <code>manylinux_2_17</code> 平台的 <code>x86_64</code> 目标</li>
<li><code>x86_64-manylinux_2_28</code>:  <code>manylinux_2_28</code> 平台的 <code>x86_64</code> 目标</li>
<li><code>x86_64-manylinux_2_31</code>:  <code>manylinux_2_31</code> 平台的 <code>x86_64</code> 目标</li>
<li><code>x86_64-manylinux_2_32</code>:  <code>manylinux_2_32</code> 平台的 <code>x86_64</code> 目标</li>
<li><code>x86_64-manylinux_2_33</code>:  <code>manylinux_2_33</code> 平台的 <code>x86_64</code> 目标</li>
<li><code>x86_64-manylinux_2_34</code>:  <code>manylinux_2_34</code> 平台的 <code>x86_64</code> 目标</li>
<li><code>x86_64-manylinux_2_35</code>:  <code>manylinux_2_35</code> 平台的 <code>x86_64</code> 目标</li>
<li><code>x86_64-manylinux_2_36</code>:  <code>manylinux_2_36</code> 平台的 <code>x86_64</code> 目标</li>
<li><code>x86_64-manylinux_2_37</code>:  <code>manylinux_2_37</code> 平台的 <code>x86_64</code> 目标</li>
<li><code>x86_64-manylinux_2_38</code>:  <code>manylinux_2_38</code> 平台的 <code>x86_64</code> 目标</li>
<li><code>x86_64-manylinux_2_39</code>:  <code>manylinux_2_39</code> 平台的 <code>x86_64</code> 目标</li>
<li><code>x86_64-manylinux_2_40</code>:  <code>manylinux_2_40</code> 平台的 <code>x86_64</code> 目标</li>
<li><code>aarch64-manylinux2014</code>:  <code>manylinux2014</code> 平台的 ARM64 目标。相当于 <code>aarch64-manylinux_2_17</code></li>
<li><code>aarch64-manylinux_2_17</code>:  <code>manylinux_2_17</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_28</code>:  <code>manylinux_2_28</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_31</code>:  <code>manylinux_2_31</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_32</code>:  <code>manylinux_2_32</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_33</code>:  <code>manylinux_2_33</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_34</code>:  <code>manylinux_2_34</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_35</code>:  <code>manylinux_2_35</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_36</code>:  <code>manylinux_2_36</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_37</code>:  <code>manylinux_2_37</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_38</code>:  <code>manylinux_2_38</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_39</code>:  <code>manylinux_2_39</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_40</code>:  <code>manylinux_2_40</code> 平台的 ARM64 目标</li>
<li><code>aarch64-linux-android</code>:  ARM64 Android 目标</li>
<li><code>x86_64-linux-android</code>:  <code>x86_64</code> Android 目标</li>
<li><code>wasm32-pyodide2024</code>:  使用 Pyodide 2024 平台的 wasm32 目标。适用于 Python 3.12。参见 <a href="https://pyodide.org/en/stable/development/abi/312.html">https://pyodide.org/en/stable/development/abi/312.html</a></li>
<li><code>wasm32-pyodide2025</code>:  使用 Pyodide 2025 平台的 wasm32 目标。适用于 Python 3.13。参见 <a href="https://pyodide.org/en/stable/development/abi/313.html">https://pyodide.org/en/stable/development/abi/313.html</a></li>
<li><code>arm64-apple-ios</code>:  iOS 设备的 ARM64 目标</li>
<li><code>arm64-apple-ios-simulator</code>:  iOS 模拟器的 ARM64 目标</li>
<li><code>x86_64-apple-ios-simulator</code>:  iOS 模拟器的 <code>x86_64</code> 目标</li>
</ul></dd><dt id="uv-sync--quiet"><a href="#uv-sync--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用安静输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，在此模式下 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-sync--refresh"><a href="#uv-sync--refresh"><code>--refresh</code></a></dt><dd><p>刷新所有缓存数据</p>
</dd><dt id="uv-sync--refresh-package"><a href="#uv-sync--refresh-package"><code>--refresh-package</code></a> <i>refresh-package</i></dt><dd><p>刷新特定包的缓存数据</p>
</dd><dt id="uv-sync--reinstall"><a href="#uv-sync--reinstall"><code>--reinstall</code></a>, <code>--force-reinstall</code></dt><dd><p>重新安装所有包，无论它们是否已安装。隐含 <code>--refresh</code></p>
</dd><dt id="uv-sync--reinstall-package"><a href="#uv-sync--reinstall-package"><code>--reinstall-package</code></a> <i>reinstall-package</i></dt><dd><p>重新安装特定包，无论它是否已安装。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-sync--resolution"><a href="#uv-sync--resolution"><code>--resolution</code></a> <i>resolution</i></dt><dd><p>在为给定包需求选择不同兼容版本时使用的策略。</p>
<p>默认情况下，uv 将使用每个包的最新兼容版本（<code>highest</code>）。</p>
<p>也可以通过 <code>UV_RESOLUTION</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>highest</code>:  解析每个包的最高兼容版本</li>
<li><code>lowest</code>:  解析每个包的最低兼容版本</li>
<li><code>lowest-direct</code>:  解析所有直接依赖项的最低兼容版本，以及所有传递依赖项的最高兼容版本</li>
</ul></dd><dt id="uv-sync--script"><a href="#uv-sync--script"><code>--script</code></a> <i>script</i></dt><dd><p>为 Python 脚本同步环境，而非当前项目。</p>
<p>如果提供，uv 将根据脚本的内联元数据表同步依赖项，遵循 PEP 723。</p>
</dd><dt id="uv-sync--system-certs"><a href="#uv-sync--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能希望使用平台的原生证书存储，尤其是在您依赖系统的证书存储中包含的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-sync--upgrade"><a href="#uv-sync--upgrade"><code>--upgrade</code></a>, <code>-U</code></dt><dd><p>允许包升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh</code></p>
</dd><dt id="uv-sync--upgrade-group"><a href="#uv-sync--upgrade-group"><code>--upgrade-group</code></a> <i>upgrade-group</i></dt><dd><p>允许依赖组中所有包的升级，忽略任何现有输出文件中的固定版本</p>
</dd><dt id="uv-sync--upgrade-package"><a href="#uv-sync--upgrade-package"><code>--upgrade-package</code></a>, <code>-P</code> <i>upgrade-package</i></dt><dd><p>允许特定包的升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-sync--verbose"><a href="#uv-sync--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度的日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>
