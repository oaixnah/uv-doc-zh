---
title: uv run
description: 本文档是 uv run 命令的完整 CLI 参考，详细介绍了如何在 Python 环境中运行命令或脚本，包括所有可用选项的中文说明，涵盖项目环境管理、依赖解析、包索引配置、虚拟环境隔离、跨平台目标支持及高级功能。
---

# uv run

运行命令或脚本。

确保命令在 Python 环境中运行。

当与 `.py` 结尾的文件或 HTTP(S) URL 一起使用时，该文件将被视为脚本并使用 Python 解释器运行，即 `uv run file.py` 等价于 `uv run python file.py`。对于 URL，脚本会在执行前临时下载。如果脚本包含内联依赖元数据，这些依赖将被安装到一个隔离的临时环境中。当与 `-` 一起使用时，将从 stdin 读取输入并将其视为 Python 脚本。

在项目中使用时，项目环境将在调用命令之前创建并更新。

在项目外部使用时，如果在当前目录或父目录中找到虚拟环境，命令将在该环境中运行。否则，命令将在所发现解释器的环境中运行。

默认情况下，项目或工作区从当前工作目录中发现。但是，当使用 `--preview-features target-workspace-discovery` 时，项目或工作区将从目标脚本的目录中发现。

命令（或脚本）之后的参数不会被解释为 uv 的参数。所有 uv 选项必须在命令之前提供，例如 `uv run --verbose foo`。可以使用 `--` 将命令与 uv 选项分开以增加清晰度，例如 `uv run --python 3.12 -- python`。

<h3 class="cli-reference">Usage</h3>

```
uv run [OPTIONS] [COMMAND]
```

<h3 class="cli-reference">Options</h3>

<dl class="cli-reference"><dt id="uv-run--active"><a href="#uv-run--active"><code>--active</code></a></dt><dd><p>优先使用活动虚拟环境，而非项目的虚拟环境。</p>
<p>如果项目虚拟环境已处于活动状态或没有活动虚拟环境，此选项无效。</p>
</dd><dt id="uv-run--all-extras"><a href="#uv-run--all-extras"><code>--all-extras</code></a></dt><dd><p>包含所有可选依赖。</p>
<p>此选项仅在项目中运行时可用。</p>
</dd><dt id="uv-run--all-groups"><a href="#uv-run--all-groups"><code>--all-groups</code></a></dt><dd><p>包含所有依赖组中的依赖。</p>
<p>可使用 <code>--no-group</code> 排除特定组。</p>
</dd><dt id="uv-run--all-packages"><a href="#uv-run--all-packages"><code>--all-packages</code></a></dt><dd><p>在安装所有工作区成员的情况下运行命令。</p>
<p>工作区环境（<code>.venv</code>）将更新以包含所有工作区成员。</p>
<p>通过 <code>--extra</code>、<code>--group</code> 或相关选项指定的任何 extras 或组将应用于所有工作区成员。</p>
</dd><dt id="uv-run--allow-insecure-host"><a href="#uv-run--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机的非安全连接。</p>
<p>可多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机不会根据系统证书存储进行验证。仅在安全的网络中使用 <code>--allow-insecure-host</code> 并确保来源可验证，因为它绕过 SSL 验证，可能使您遭受中间人攻击。</p>
<p>也可通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-run--cache-dir"><a href="#uv-run--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-run--color"><a href="#uv-run--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测颜色支持。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>：仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-run--compile-bytecode"><a href="#uv-run--compile-bytecode"><code>--compile-bytecode</code></a>, <code>--compile</code></dt><dd><p>安装后将 Python 文件编译为字节码。</p>
<p>默认情况下，uv 不会将 Python（<code>.py</code>）文件编译为字节码（<code>__pycache__/*.pyc</code>）；相反，编译会在模块首次导入时延迟执行。对于启动时间至关重要的用例，例如 CLI 应用程序和 Docker 容器，可以启用此选项，以较长的安装时间换取更快的启动速度。</p>
<p>启用后，uv 将处理整个 site-packages 目录（包括当前操作未修改的包）以保持一致性。与 pip 类似，它也会忽略错误。</p>
<p>也可通过 <code>UV_COMPILE_BYTECODE</code> 环境变量设置。</p></dd><dt id="uv-run--config-file"><a href="#uv-run--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许。</p>
<p>也可通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-run--config-setting"><a href="#uv-run--config-setting"><code>--config-setting</code></a>, <code>--config-settings</code>, <code>-C</code> <i>config-setting</i></dt><dd><p>传递给 PEP 517 构建后端的设置，指定为 <code>KEY=VALUE</code> 对</p>
</dd><dt id="uv-run--config-settings-package"><a href="#uv-run--config-settings-package"><code>--config-settings-package</code></a>, <code>--config-settings-package</code> <i>config-settings-package</i></dt><dd><p>传递给特定包的 PEP 517 构建后端的设置，指定为 <code>PACKAGE:KEY=VALUE</code> 对</p>
</dd><dt id="uv-run--default-index"><a href="#uv-run--default-index"><code>--default-index</code></a> <i>default-index</i></dt><dd><p>默认包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--index</code> 标志指定的所有其他索引。</p>
<p>也可通过 <code>UV_DEFAULT_INDEX</code> 环境变量设置。</p></dd><dt id="uv-run--directory"><a href="#uv-run--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到给定目录。</p>
<p>相对路径以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 以仅更改项目根目录。</p>
<p>也可通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-run--env-file"><a href="#uv-run--env-file"><code>--env-file</code></a> <i>env-file</i></dt><dd><p>从 <code>.env</code> 文件加载环境变量。</p>
<p>可多次提供，后续文件中的值将覆盖先前文件中定义的值。</p>
<p>也可通过 <code>UV_ENV_FILE</code> 环境变量设置。</p></dd><dt id="uv-run--exact"><a href="#uv-run--exact"><code>--exact</code></a></dt><dd><p>执行精确同步，移除多余的包。</p>
<p>启用后，uv 将从环境中移除任何多余的包。默认情况下，<code>uv run</code> 仅进行满足需求所需的最小更改。</p>
</dd><dt id="uv-run--exclude-newer"><a href="#uv-run--exclude-newer"><code>--exclude-newer</code></a> <i>exclude-newer</i></dt><dd><p>将候选包限制为在给定日期之前上传的版本。</p>
<p>日期与每个分发包构件的上传时间（即每个文件上传到包索引的时间）进行比较，而非包版本的发布日期。</p>
<p>接受 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、相同格式的本地日期（例如 <code>2006-12-02</code>，基于系统配置的时区解析）、"友好"持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不遵循本地时区的语义，始终解析为固定的秒数，假设一天为 24 小时（例如，忽略 DST 转换）。不允许使用日历单位（如月和年）。</p>
<p>也可通过 <code>UV_EXCLUDE_NEWER</code> 环境变量设置。</p></dd><dt id="uv-run--exclude-newer-package"><a href="#uv-run--exclude-newer-package"><code>--exclude-newer-package</code></a> <i>exclude-newer-package</i></dt><dd><p>将特定包的候选包限制为在给定日期之前上传的版本。</p>
<p>接受 <code>PACKAGE=DATE</code> 格式的包-日期对，其中 <code>DATE</code> 是 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、相同格式的本地日期（例如 <code>2006-12-02</code>，基于系统配置的时区解析）、"友好"持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不遵循本地时区的语义，始终解析为固定的秒数，假设一天为 24 小时（例如，忽略 DST 转换）。不允许使用日历单位（如月和年）。</p>
<p>可为不同包多次提供。</p>
</dd><dt id="uv-run--extra"><a href="#uv-run--extra"><code>--extra</code></a> <i>extra</i></dt><dd><p>包含来自指定 extra 名称的可选依赖。</p>
<p>可多次提供。</p>
<p>此选项仅在项目中运行时可用。</p>
</dd><dt id="uv-run--extra-index-url"><a href="#uv-run--extra-index-url"><code>--extra-index-url</code></a> <i>extra-index-url</i></dt><dd><p>（已弃用：请改用 <code>--index</code>）除 <code>--index-url</code> 之外要使用的额外包索引 URL。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--index-url</code> 指定的索引（默认为 PyPI）。当提供多个 <code>--extra-index-url</code> 标志时，较早的值优先级更高。</p>
<p>也可通过 <code>UV_EXTRA_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-run--find-links"><a href="#uv-run--find-links"><code>--find-links</code></a>, <code>-f</code> <i>find-links</i></dt><dd><p>搜索候选分发包的位置，作为注册表索引中已找到项的补充。</p>
<p>如果是路径，目标必须是一个目录，其中包含 wheel 文件（<code>.whl</code>）或源码分发包（例如 <code>.tar.gz</code> 或 <code>.zip</code>）作为顶层内容。</p>
<p>如果是 URL，页面必须包含一个扁平列表，链接到符合上述格式的包文件。</p>
<p>也可通过 <code>UV_FIND_LINKS</code> 环境变量设置。</p></dd><dt id="uv-run--fork-strategy"><a href="#uv-run--fork-strategy"><code>--fork-strategy</code></a> <i>fork-strategy</i></dt><dd><p>在跨 Python 版本和平台选择给定包的多个版本时使用的策略。</p>
<p>默认情况下，uv 会优化以为每个受支持的 Python 版本（<code>requires-python</code>）选择每个包的最新版本，同时最小化跨平台选择的版本数。</p>
<p>在 <code>fewest</code> 模式下，uv 将最小化每个包的选择版本数，优先选择与更广泛的受支持 Python 版本或平台兼容的旧版本。</p>
<p>也可通过 <code>UV_FORK_STRATEGY</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>fewest</code>：优化以选择每个包的最少版本数。如果旧版本与更广泛的受支持 Python 版本或平台兼容，可能会优先选择旧版本</li>
<li><code>requires-python</code>：优化以为每个受支持的 Python 版本选择每个包的最新支持版本</li>
</ul></dd><dt id="uv-run--frozen"><a href="#uv-run--frozen"><code>--frozen</code></a></dt><dd><p>在不更新 <code>uv.lock</code> 文件的情况下运行 [env: UV_FROZEN=]</p>
<p>不检查锁文件是否为最新版本，而是将锁文件中的版本作为唯一真实来源。如果锁文件缺失，uv 将退出并报错。如果 <code>pyproject.toml</code> 包含尚未纳入锁文件的依赖更改，这些更改将不会体现在环境中。</p>
</dd><dt id="uv-run--group"><a href="#uv-run--group"><code>--group</code></a> <i>group</i></dt><dd><p>包含来自指定依赖组的依赖。</p>
<p>可多次提供。</p>
</dd><dt id="uv-run--gui-script"><a href="#uv-run--gui-script"><code>--gui-script</code></a></dt><dd><p>将给定路径作为 Python GUI 脚本运行。</p>
<p>使用 <code>--gui-script</code> 将尝试将路径解析为 PEP 723 脚本，并使用 <code>pythonw.exe</code> 运行，无论其扩展名如何。仅适用于 Windows。</p>
</dd><dt id="uv-run--help"><a href="#uv-run--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助</p>
</dd><dt id="uv-run--index"><a href="#uv-run--index"><code>--index</code></a> <i>index</i></dt><dd><p>解析依赖时使用的 URL，作为默认索引的补充。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--default-index</code> 指定的索引（默认为 PyPI）。当提供多个 <code>--index</code> 标志时，较早的值优先级更高。</p>
<p>索引名称不支持作为值。相对路径必须通过 <code>./</code> 或 <code>../</code>（Unix 上）或 <code>.\\</code>、<code>..\\</code>、<code>./</code> 或 <code>../</code>（Windows 上）与索引名称区分。</p>
<p>也可通过 <code>UV_INDEX</code> 环境变量设置。</p></dd><dt id="uv-run--index-strategy"><a href="#uv-run--index-strategy"><code>--index-strategy</code></a> <i>index-strategy</i></dt><dd><p>针对多个索引 URL 进行解析时使用的策略。</p>
<p>默认情况下，uv 会在第一个找到给定包的索引处停止，并将解析限制为该第一个索引上存在的版本（<code>first-index</code>）。这可以防止"依赖混淆"攻击，即攻击者可以在备用索引上以相同名称上传恶意包。</p>
<p>也可通过 <code>UV_INDEX_STRATEGY</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>first-index</code>：仅使用第一个返回给定包名称匹配结果的索引</li>
<li><code>unsafe-first-match</code>：在所有索引中搜索每个包名称，先穷尽第一个索引的版本，然后再转到下一个</li>
<li><code>unsafe-best-match</code>：在所有索引中搜索每个包名称，优先选择找到的"最佳"版本。如果某个包版本存在于多个索引中，仅查看第一个索引中的条目</li>
</ul></dd><dt id="uv-run--index-url"><a href="#uv-run--index-url"><code>--index-url</code></a>, <code>-i</code> <i>index-url</i></dt><dd><p>（已弃用：请改用 <code>--default-index</code>）Python 包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--extra-index-url</code> 标志指定的所有其他索引。</p>
<p>也可通过 <code>UV_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-run--isolated"><a href="#uv-run--isolated"><code>--isolated</code></a></dt><dd><p>在隔离的虚拟环境中运行命令 [env: UV_ISOLATED=]</p>
<p>通常，项目环境会为性能而复用。此选项强制为项目使用全新的环境，强制依赖项与需求声明之间严格隔离。</p>
<p>项目仍会使用可编辑安装。</p>
<p>当与 <code>--with</code> 或 <code>--with-requirements</code> 一起使用时，额外的依赖仍将在第二个环境中分层叠加。</p>
</dd><dt id="uv-run--keyring-provider"><a href="#uv-run--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>尝试使用 <code>keyring</code> 对索引 URL 进行身份验证。</p>
<p>目前仅支持 <code>--keyring-provider subprocess</code>，它配置 uv 使用 <code>keyring</code> CLI 来处理身份验证。</p>
<p>默认为 <code>disabled</code>。</p>
<p>也可通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disabled</code>：不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>：使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-run--link-mode"><a href="#uv-run--link-mode"><code>--link-mode</code></a> <i>link-mode</i></dt><dd><p>从全局缓存安装包时使用的方法。</p>
<p>在 macOS 和 Linux 上默认为 <code>clone</code>（也称为写时复制），在 Windows 上默认为 <code>hardlink</code>。</p>
<p>警告：不鼓励使用 symlink 链接模式，因为它会在缓存和目标环境之间创建紧密耦合。例如，清除缓存（<code>uv cache clean</code>）将通过移除底层源文件来破坏所有已安装的包。请谨慎使用 symlink。</p>
<p>也可通过 <code>UV_LINK_MODE</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>clone</code>：将包从源克隆（即写时复制）到目标</li>
<li><code>copy</code>：将包从源复制到目标</li>
<li><code>hardlink</code>：将包从源硬链接到目标</li>
<li><code>symlink</code>：将包从源符号链接到目标</li>
</ul></dd><dt id="uv-run--locked"><a href="#uv-run--locked"><code>--locked</code></a></dt><dd><p>断言 <code>uv.lock</code> 将保持不变 [env: UV_LOCKED=]</p>
<p>要求锁文件是最新的。如果锁文件缺失或需要更新，uv 将退出并报错。</p>
</dd><dt id="uv-run--managed-python"><a href="#uv-run--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用它管理的 Python 版本。但是，如果没有安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-run--module"><a href="#uv-run--module"><code>--module</code></a>, <code>-m</code></dt><dd><p>运行 Python 模块。</p>
<p>等价于 <code>python -m &lt;module&gt;</code>。</p>
</dd><dt id="uv-run--no-binary"><a href="#uv-run--no-binary"><code>--no-binary</code></a></dt><dd><p>不安装预构建的 wheel。</p>
<p>给定的包将从源码构建并安装。解析器仍将使用预构建的 wheel 来提取包元数据（如果可用）。</p>
<p>也可通过 <code>UV_NO_BINARY</code> 环境变量设置。</p></dd><dt id="uv-run--no-binary-package"><a href="#uv-run--no-binary-package"><code>--no-binary-package</code></a> <i>no-binary-package</i></dt><dd><p>不为特定包安装预构建的 wheel [env: <code>UV_NO_BINARY_PACKAGE</code>=]</p>
</dd><dt id="uv-run--no-build"><a href="#uv-run--no-build"><code>--no-build</code></a></dt><dd><p>不构建源码分发包。</p>
<p>启用后，解析将不会运行任意 Python 代码。已构建的源码分发包的缓存 wheel 将被复用，但需要构建分发包的操作将退出并报错。</p>
<p>也可通过 <code>UV_NO_BUILD</code> 环境变量设置。</p></dd><dt id="uv-run--no-build-isolation"><a href="#uv-run--no-build-isolation"><code>--no-build-isolation</code></a></dt><dd><p>构建源码分发包时禁用隔离。</p>
<p>假设 PEP 518 指定的构建依赖已经安装。</p>
<p>也可通过 <code>UV_NO_BUILD_ISOLATION</code> 环境变量设置。</p></dd><dt id="uv-run--no-build-isolation-package"><a href="#uv-run--no-build-isolation-package"><code>--no-build-isolation-package</code></a> <i>no-build-isolation-package</i></dt><dd><p>为特定包构建源码分发包时禁用隔离。</p>
<p>假设该包的 PEP 518 指定的构建依赖已经安装。</p>
</dd><dt id="uv-run--no-build-package"><a href="#uv-run--no-build-package"><code>--no-build-package</code></a> <i>no-build-package</i></dt><dd><p>不为特定包构建源码分发包 [env: <code>UV_NO_BUILD_PACKAGE</code>=]</p>
</dd><dt id="uv-run--no-cache"><a href="#uv-run--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-run--no-config"><a href="#uv-run--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中发现。</p>
<p>也可通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-run--no-default-groups"><a href="#uv-run--no-default-groups"><code>--no-default-groups</code></a></dt><dd><p>忽略默认依赖组。</p>
<p>uv 默认包含 <code>tool.uv.default-groups</code> 中定义的组。此选项禁用该行为，但仍可通过 <code>--group</code> 包含特定组。</p>
<p>也可通过 <code>UV_NO_DEFAULT_GROUPS</code> 环境变量设置。</p></dd><dt id="uv-run--no-dev"><a href="#uv-run--no-dev"><code>--no-dev</code></a></dt><dd><p>禁用开发依赖组 [env: UV_NO_DEV=]</p>
<p>此选项是 <code>--no-group dev</code> 的别名。参见 <code>--no-default-groups</code> 以禁用所有默认组。</p>
<p>此选项仅在项目中运行时可用。</p>
</dd><dt id="uv-run--no-editable"><a href="#uv-run--no-editable"><code>--no-editable</code></a></dt><dd><p>将所有可编辑依赖（包括项目和工作区成员）以非可编辑方式安装 [env: UV_NO_EDITABLE=]</p>
</dd><dt id="uv-run--no-editable-package"><a href="#uv-run--no-editable-package"><code>--no-editable-package</code></a> <i>no-editable-package</i></dt><dd><p>将指定的可编辑包以非可编辑方式安装</p>
</dd><dt id="uv-run--no-env-file"><a href="#uv-run--no-env-file"><code>--no-env-file</code></a></dt><dd><p>避免从 <code>.env</code> 文件读取环境变量 [env: UV_NO_ENV_FILE=]</p>
</dd><dt id="uv-run--no-extra"><a href="#uv-run--no-extra"><code>--no-extra</code></a> <i>no-extra</i></dt><dd><p>如果提供了 <code>--all-extras</code>，则排除指定的可选依赖。</p>
<p>可多次提供。</p>
</dd><dt id="uv-run--no-group"><a href="#uv-run--no-group"><code>--no-group</code></a> <i>no-group</i></dt><dd><p>禁用指定的依赖组 [env: <code>UV_NO_GROUP</code>=]</p>
<p>此选项始终优先于默认组、<code>--all-groups</code> 和 <code>--group</code>。</p>
<p>可多次提供。</p>
</dd><dt id="uv-run--no-index"><a href="#uv-run--no-index"><code>--no-index</code></a></dt><dd><p>忽略注册表索引（例如 PyPI），转而依赖直接 URL 依赖和通过 <code>--find-links</code> 提供的依赖</p>
</dd><dt id="uv-run--no-managed-python"><a href="#uv-run--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-run--no-progress"><a href="#uv-run--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转指示器或进度条。</p>
</dd><dt id="uv-run--no-project"><a href="#uv-run--no-project"><code>--no-project</code></a>, <code>--no_workspace</code></dt><dd><p>避免发现项目或工作区。</p>
<p>不在当前目录和父目录中搜索项目，而是在由 <code>--with</code> 需求填充的隔离临时环境中运行。</p>
<p>如果虚拟环境处于活动状态或在当前或父目录中找到，它将像没有项目或工作区一样被使用。</p>
<p>也可通过 <code>UV_NO_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-run--no-python-downloads"><a href="#uv-run--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-run--no-sources"><a href="#uv-run--no-sources"><code>--no-sources</code></a></dt><dd><p>解析依赖时忽略 <code>tool.uv.sources</code> 表。用于基于符合标准的、可发布的包元数据进行锁定，而不是使用任何工作区、Git、URL 或本地路径源</p>
<p>也可通过 <code>UV_NO_SOURCES</code> 环境变量设置。</p></dd><dt id="uv-run--no-sources-package"><a href="#uv-run--no-sources-package"><code>--no-sources-package</code></a> <i>no-sources-package</i></dt><dd><p>不为指定包使用 <code>tool.uv.sources</code> 表中的源 [env: <code>UV_NO_SOURCES_PACKAGE</code>=]</p>
</dd><dt id="uv-run--no-sync"><a href="#uv-run--no-sync"><code>--no-sync</code></a></dt><dd><p>避免同步虚拟环境 [env: UV_NO_SYNC=]</p>
<p>隐含 <code>--frozen</code>，因为项目依赖将被忽略（即锁文件不会更新，因为环境无论如何都不会同步）。</p>
</dd><dt id="uv-run--offline"><a href="#uv-run--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-run--only-dev"><a href="#uv-run--only-dev"><code>--only-dev</code></a></dt><dd><p>仅包含开发依赖组。</p>
<p>项目及其依赖将被省略。</p>
<p>此选项是 <code>--only-group dev</code> 的别名。隐含 <code>--no-default-groups</code>。</p>
</dd><dt id="uv-run--only-group"><a href="#uv-run--only-group"><code>--only-group</code></a> <i>only-group</i></dt><dd><p>仅包含来自指定依赖组的依赖。</p>
<p>项目及其依赖将被省略。</p>
<p>可多次提供。隐含 <code>--no-default-groups</code>。</p>
</dd><dt id="uv-run--package"><a href="#uv-run--package"><code>--package</code></a> <i>package</i></dt><dd><p>在工作区中的特定包中运行命令。</p>
<p>如果工作区成员不存在，uv 将退出并报错。</p>
</dd><dt id="uv-run--prerelease"><a href="#uv-run--prerelease"><code>--prerelease</code></a> <i>prerelease</i></dt><dd><p>考虑预发布版本时使用的策略。</p>
<p>默认情况下，uv 将接受<em>仅</em>发布预发布版本的包的预发布版本，以及声明的版本说明符中包含显式预发布标记的第一方需求（<code>if-necessary-or-explicit</code>）。</p>
<p>也可通过 <code>UV_PRERELEASE</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disallow</code>：禁止所有预发布版本</li>
<li><code>allow</code>：允许所有预发布版本</li>
<li><code>if-necessary</code>：如果包的所有版本都是预发布版本，则允许预发布版本</li>
<li><code>explicit</code>：允许版本需求中带有显式预发布标记的第一方包的预发布版本</li>
<li><code>if-necessary-or-explicit</code>：如果包的所有版本都是预发布版本，或包的版本需求中带有显式预发布标记，则允许预发布版本</li>
</ul></dd><dt id="uv-run--project"><a href="#uv-run--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-run--python"><a href="#uv-run--python"><code>--python</code></a>, <code>-p</code> <i>python</i></dt><dd><p>用于运行环境的 Python 解释器。</p>
<p>如果解释器请求由已发现的环境满足，则将使用该环境。</p>
<p>参见 <a href="#uv-python">uv python</a> 查看支持的请求格式。</p>
<p>也可通过 <code>UV_PYTHON</code> 环境变量设置。</p></dd><dt id="uv-run--python-platform"><a href="#uv-run--python-platform"><code>--python-platform</code></a> <i>python-platform</i></dt><dd><p>应为其安装需求的目标平台。</p>
<p>表示为"目标三元组"，一个描述目标平台的字符串，包含其 CPU、供应商和操作系统名称，如 <code>x86_64-unknown-linux-gnu</code> 或 <code>aarch64-apple-darwin</code>。</p>
<p>当目标为 macOS（Darwin）时，默认最低版本为 <code>13.0</code>。使用 <code>MACOSX_DEPLOYMENT_TARGET</code> 指定不同的最低版本，例如 <code>14.0</code>。</p>
<p>当目标为 iOS 时，默认最低版本为 <code>13.0</code>。使用 <code>IPHONEOS_DEPLOYMENT_TARGET</code> 指定不同的最低版本，例如 <code>14.0</code>。</p>
<p>当目标为 Android 时，默认最低 Android API 级别为 <code>24</code>。使用 <code>ANDROID_API_LEVEL</code> 指定不同的最低版本，例如 <code>26</code>。</p>
<p>警告：指定后，uv 将选择与<em>目标</em>平台兼容的 wheel；因此，安装的分发包可能与<em>当前</em>平台不兼容。反之，任何从源码构建的分发包可能与<em>目标</em>平台不兼容，因为它们将为<em>当前</em>平台构建。<code>--python-platform</code> 选项适用于高级用例。</p>
<p>可选值：</p>
<ul>
<li><code>windows</code>：<code>x86_64-pc-windows-msvc</code> 的别名，Windows 的默认目标</li>
<li><code>linux</code>：<code>x86_64-unknown-linux-gnu</code> 的别名，Linux 的默认目标</li>
<li><code>macos</code>：<code>aarch64-apple-darwin</code> 的别名，macOS 的默认目标</li>
<li><code>x86_64-pc-windows-msvc</code>：64 位 x86 Windows 目标</li>
<li><code>aarch64-pc-windows-msvc</code>：ARM64 Windows 目标</li>
<li><code>i686-pc-windows-msvc</code>：32 位 x86 Windows 目标</li>
<li><code>x86_64-unknown-linux-gnu</code>：x86 Linux 目标。等价于 <code>x86_64-manylinux_2_28</code></li>
<li><code>aarch64-apple-darwin</code>：基于 ARM 的 macOS 目标，用于 Apple Silicon 设备</li>
<li><code>x86_64-apple-darwin</code>：x86 macOS 目标</li>
<li><code>aarch64-unknown-linux-gnu</code>：ARM64 Linux 目标。等价于 <code>aarch64-manylinux_2_28</code></li>
<li><code>aarch64-unknown-linux-musl</code>：ARM64 Linux 目标</li>
<li><code>x86_64-unknown-linux-musl</code>：<code>x86_64</code> Linux 目标</li>
<li><code>riscv64-unknown-linux</code>：RISCV64 Linux 目标</li>
<li><code>x86_64-manylinux2014</code>：<code>manylinux2014</code> 平台的 <code>x86_64</code> 目标。等价于 <code>x86_64-manylinux_2_17</code></li>
<li><code>x86_64-manylinux_2_17</code>：<code>manylinux_2_17</code> 平台的 <code>x86_64</code> 目标</li>
<li><code>x86_64-manylinux_2_28</code>：<code>manylinux_2_28</code> 平台的 <code>x86_64</code> 目标</li>
<li><code>x86_64-manylinux_2_31</code>：<code>manylinux_2_31</code> 平台的 <code>x86_64</code> 目标</li>
<li><code>x86_64-manylinux_2_32</code>：<code>manylinux_2_32</code> 平台的 <code>x86_64</code> 目标</li>
<li><code>x86_64-manylinux_2_33</code>：<code>manylinux_2_33</code> 平台的 <code>x86_64</code> 目标</li>
<li><code>x86_64-manylinux_2_34</code>：<code>manylinux_2_34</code> 平台的 <code>x86_64</code> 目标</li>
<li><code>x86_64-manylinux_2_35</code>：<code>manylinux_2_35</code> 平台的 <code>x86_64</code> 目标</li>
<li><code>x86_64-manylinux_2_36</code>：<code>manylinux_2_36</code> 平台的 <code>x86_64</code> 目标</li>
<li><code>x86_64-manylinux_2_37</code>：<code>manylinux_2_37</code> 平台的 <code>x86_64</code> 目标</li>
<li><code>x86_64-manylinux_2_38</code>：<code>manylinux_2_38</code> 平台的 <code>x86_64</code> 目标</li>
<li><code>x86_64-manylinux_2_39</code>：<code>manylinux_2_39</code> 平台的 <code>x86_64</code> 目标</li>
<li><code>x86_64-manylinux_2_40</code>：<code>manylinux_2_40</code> 平台的 <code>x86_64</code> 目标</li>
<li><code>aarch64-manylinux2014</code>：<code>manylinux2014</code> 平台的 ARM64 目标。等价于 <code>aarch64-manylinux_2_17</code></li>
<li><code>aarch64-manylinux_2_17</code>：<code>manylinux_2_17</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_28</code>：<code>manylinux_2_28</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_31</code>：<code>manylinux_2_31</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_32</code>：<code>manylinux_2_32</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_33</code>：<code>manylinux_2_33</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_34</code>：<code>manylinux_2_34</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_35</code>：<code>manylinux_2_35</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_36</code>：<code>manylinux_2_36</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_37</code>：<code>manylinux_2_37</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_38</code>：<code>manylinux_2_38</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_39</code>：<code>manylinux_2_39</code> 平台的 ARM64 目标</li>
<li><code>aarch64-manylinux_2_40</code>：<code>manylinux_2_40</code> 平台的 ARM64 目标</li>
<li><code>aarch64-linux-android</code>：ARM64 Android 目标</li>
<li><code>x86_64-linux-android</code>：<code>x86_64</code> Android 目标</li>
<li><code>wasm32-pyodide2024</code>：使用 Pyodide 2024 平台的 wasm32 目标。适用于 Python 3.12。参见 <a href="https://pyodide.org/en/stable/development/abi/312.html">https://pyodide.org/en/stable/development/abi/312.html</a></li>
<li><code>wasm32-pyodide2025</code>：使用 Pyodide 2025 平台的 wasm32 目标。适用于 Python 3.13。参见 <a href="https://pyodide.org/en/stable/development/abi/313.html">https://pyodide.org/en/stable/development/abi/313.html</a></li>
<li><code>arm64-apple-ios</code>：iOS 设备的 ARM64 目标</li>
<li><code>arm64-apple-ios-simulator</code>：iOS 模拟器的 ARM64 目标</li>
<li><code>x86_64-apple-ios-simulator</code>：iOS 模拟器的 <code>x86_64</code> 目标</li>
</ul></dd><dt id="uv-run--quiet"><a href="#uv-run--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用安静输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，在此模式下 uv 不会向标准输出（stdout）写入任何输出。</p>
</dd><dt id="uv-run--refresh"><a href="#uv-run--refresh"><code>--refresh</code></a></dt><dd><p>刷新所有缓存数据</p>
</dd><dt id="uv-run--refresh-package"><a href="#uv-run--refresh-package"><code>--refresh-package</code></a> <i>refresh-package</i></dt><dd><p>刷新特定包的缓存数据</p>
</dd><dt id="uv-run--reinstall"><a href="#uv-run--reinstall"><code>--reinstall</code></a>, <code>--force-reinstall</code></dt><dd><p>重新安装所有包，无论它们是否已经安装。隐含 <code>--refresh</code></p>
</dd><dt id="uv-run--reinstall-package"><a href="#uv-run--reinstall-package"><code>--reinstall-package</code></a> <i>reinstall-package</i></dt><dd><p>重新安装特定包，无论它是否已经安装。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-run--resolution"><a href="#uv-run--resolution"><code>--resolution</code></a> <i>resolution</i></dt><dd><p>在给定包需求的不同兼容版本之间选择时使用的策略。</p>
<p>默认情况下，uv 将使用每个包的最新兼容版本（<code>highest</code>）。</p>
<p>也可通过 <code>UV_RESOLUTION</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>highest</code>：解析每个包的最高兼容版本</li>
<li><code>lowest</code>：解析每个包的最低兼容版本</li>
<li><code>lowest-direct</code>：解析任何直接依赖的最低兼容版本，以及任何传递依赖的最高兼容版本</li>
</ul></dd><dt id="uv-run--script"><a href="#uv-run--script"><code>--script</code></a>, <code>-s</code></dt><dd><p>将给定路径作为 Python 脚本运行。</p>
<p>使用 <code>--script</code> 将尝试将路径解析为 PEP 723 脚本，无论其扩展名是什么。</p>
</dd><dt id="uv-run--system-certs"><a href="#uv-run--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能希望使用平台的原生证书存储，特别是当您依赖包含在系统证书存储中的企业信任根（例如，对于强制代理）时。</p>
</dd><dt id="uv-run--upgrade"><a href="#uv-run--upgrade"><code>--upgrade</code></a>, <code>-U</code></dt><dd><p>允许包升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh</code></p>
</dd><dt id="uv-run--upgrade-group"><a href="#uv-run--upgrade-group"><code>--upgrade-group</code></a> <i>upgrade-group</i></dt><dd><p>允许依赖组中所有包升级，忽略任何现有输出文件中的固定版本</p>
</dd><dt id="uv-run--upgrade-package"><a href="#uv-run--upgrade-package"><code>--upgrade-package</code></a>, <code>-P</code> <i>upgrade-package</i></dt><dd><p>允许特定包升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-run--verbose"><a href="#uv-run--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd><dt id="uv-run--with"><a href="#uv-run--with"><code>--with</code></a>, <code>-w</code> <i>with</i></dt><dd><p>在安装了给定包的情况下运行。</p>
<p>在项目中使用时，这些依赖将分层叠加在项目环境之上的独立临时环境中。这些依赖允许与项目指定的依赖冲突。</p>
</dd><dt id="uv-run--with-editable"><a href="#uv-run--with-editable"><code>--with-editable</code></a> <i>with-editable</i></dt><dd><p>在以可编辑模式安装给定包的情况下运行。</p>
<p>在项目中使用时，这些依赖将分层叠加在项目环境之上的独立临时环境中。这些依赖允许与项目指定的依赖冲突。</p>
</dd><dt id="uv-run--with-requirements"><a href="#uv-run--with-requirements"><code>--with-requirements</code></a> <i>with-requirements</i></dt><dd><p>在安装了给定文件中列出的包的情况下运行。</p>
<p>支持以下格式：<code>requirements.txt</code>、带有内联元数据的 <code>.py</code> 文件和 <code>pylock.toml</code>。</p>
<p>适用与 <code>--with</code> 相同的环境语义。</p>
<p>不允许使用 <code>pyproject.toml</code>、<code>setup.py</code> 或 <code>setup.cfg</code> 文件。</p>
</dd></dl>
