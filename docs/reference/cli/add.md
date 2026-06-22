---
title: uv add
description: uv add 命令用于向项目添加依赖项，是 uv 包管理器的核心命令之一。依赖项将被添加到 pyproject.toml 文件中，锁文件和项目环境会同步更新。支持丰富的选项：版本约束符策略（--bounds）、开发依赖组（--dev/--group）、可编辑模式（--editable）、Git 依赖（--branch/--tag/--rev）、预发布版本策略（--prerelease）、索引策略（--index-strategy）、冻结模式（--frozen）以及 Docker 构建优化（--no-install-project）等。本文档提供 uv add 命令的完整 CLI 参考，包括所有参数、选项及其详细说明。
---

# uv add

向项目添加依赖项。

依赖项将被添加到项目的 `pyproject.toml` 文件中。

如果某个依赖项已存在，它将更新为新的版本约束符，除非其标记（marker）与现有约束符不同，在这种情况下将为该依赖项添加另一个条目。

锁文件和项目环境将更新以反映已添加的依赖项。要跳过更新锁文件，请使用 `--frozen`。要跳过更新环境，请使用 `--no-sync`。

如果找不到任何请求的依赖项，uv 将退出并报错，除非提供了 `--frozen` 标志，在这种情况下 uv 将原样添加依赖项，而不检查它们是否存在或是否与项目兼容。

uv 将在当前目录或任何父目录中搜索项目。如果找不到项目，uv 将退出并报错。

<h3 class="cli-reference">Usage</h3>

```
uv add [OPTIONS] <PACKAGES|--requirements <REQUIREMENTS>>
```

<h3 class="cli-reference">Arguments</h3>

<dl class="cli-reference"><dt id="uv-add--packages"><a href="#uv-add--packages"><code>PACKAGES</code></a></dt><dd><p>要添加的包，格式为 PEP 508 依赖项声明（例如 <code>ruff==0.5.0</code>）</p>
</dd></dl>

<h3 class="cli-reference">Options</h3>

<dl class="cli-reference"><dt id="uv-add--active"><a href="#uv-add--active"><code>--active</code></a></dt><dd><p>优先使用激活的虚拟环境，而非项目的虚拟环境。</p>
<p>如果项目的虚拟环境已激活或没有虚拟环境处于激活状态，则此选项无效。</p>
</dd><dt id="uv-add--allow-insecure-host"><a href="#uv-add--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可以提供多次。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您遭受中间人攻击（MITM）。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-add--bounds"><a href="#uv-add--bounds"><code>--bounds</code></a> <i>bounds</i></dt><dd><p>添加依赖项时使用的版本约束符类型。</p>
<p>当向项目添加依赖项时，如果未提供约束或 URL，则会根据该包的最新兼容版本添加约束。默认情况下，使用下限约束，例如 <code>&gt;=1.2.3</code>。</p>
<p>当提供 <code>--frozen</code> 时，不执行解析，依赖项始终不带约束地添加。</p>
<p>此选项处于预览阶段，可能在未来的任何版本中发生变化。</p>
<p>可选值：</p>
<ul>
<li><code>lower</code>:  仅下限约束，例如 <code>&gt;=1.2.3</code></li>
<li><code>major</code>:  允许相同的主版本，类似于 semver 的插入符（caret），例如 <code>&gt;=1.2.3, &lt;2.0.0</code></li>
<li><code>minor</code>:  允许相同的次版本，类似于 semver 的波浪号（tilde），例如 <code>&gt;=1.2.3, &lt;1.3.0</code></li>
<li><code>exact</code>:  锁定精确版本，例如 <code>==1.2.3</code></li>
</ul></dd><dt id="uv-add--branch"><a href="#uv-add--branch"><code>--branch</code></a> <i>branch</i></dt><dd><p>从 Git 添加依赖项时使用的分支</p>
</dd><dt id="uv-add--cache-dir"><a href="#uv-add--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录路径。</p>
<p>默认情况下，在 macOS 和 Linux 上为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-add--color"><a href="#uv-add--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 在写入终端时会自动检测颜色支持。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>:  仅当输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>:  无论检测到的环境如何，都启用彩色输出</li>
<li><code>never</code>:  禁用彩色输出</li>
</ul></dd><dt id="uv-add--compile-bytecode"><a href="#uv-add--compile-bytecode"><code>--compile-bytecode</code></a>, <code>--compile</code></dt><dd><p>安装后将 Python 文件编译为字节码。</p>
<p>默认情况下，uv 不会将 Python（<code>.py</code>）文件编译为字节码（<code>__pycache__/*.pyc</code>）；而是在第一次导入模块时延迟编译。对于启动时间至关重要的使用场景，例如 CLI 应用程序和 Docker 容器，启用此选项可以用更长的安装时间换取更快的启动速度。</p>
<p>启用后，uv 会为了一致性处理整个 site-packages 目录（包括当前操作未修改的包）。与 pip 一样，它也会忽略错误。</p>
<p>也可以通过 <code>UV_COMPILE_BYTECODE</code> 环境变量设置。</p></dd><dt id="uv-add--config-file"><a href="#uv-add--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用作配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许使用。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-add--config-setting"><a href="#uv-add--config-setting"><code>--config-setting</code></a>, <code>--config-settings</code>, <code>-C</code> <i>config-setting</i></dt><dd><p>传递给 PEP 517 构建后端的设置，格式为 <code>键=值</code> 对</p>
</dd><dt id="uv-add--config-settings-package"><a href="#uv-add--config-settings-package"><code>--config-settings-package</code></a>, <code>--config-settings-package</code> <i>config-settings-package</i></dt><dd><p>传递给特定包的 PEP 517 构建后端的设置，格式为 <code>包名:键=值</code> 对</p>
</dd><dt id="uv-add--constraints"><a href="#uv-add--constraints"><code>--constraints</code></a>, <code>--constraint</code>, <code>-c</code> <i>constraints</i></dt><dd><p>使用给定的需求文件约束版本。</p>
<p>约束文件是类似于 <code>requirements.txt</code> 的文件，仅控制已安装需求的<em>版本</em>。约束<em>不会</em>添加到项目的 <code>pyproject.toml</code> 文件中，但<em>会</em>在依赖解析期间被遵守。</p>
<p>这等价于 pip 的 <code>--constraint</code> 选项。</p>
<p>也可以通过 <code>UV_CONSTRAINT</code> 环境变量设置。</p></dd><dt id="uv-add--default-index"><a href="#uv-add--default-index"><code>--default-index</code></a> <i>default-index</i></dt><dd><p>默认包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--index</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_DEFAULT_INDEX</code> 环境变量设置。</p></dd><dt id="uv-add--dev"><a href="#uv-add--dev"><code>--dev</code></a></dt><dd><p>将需求添加到开发依赖组 [env: UV_DEV=]</p>
<p>此选项是 <code>--group dev</code> 的别名。</p>
</dd><dt id="uv-add--directory"><a href="#uv-add--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到给定的目录。</p>
<p>相对路径以给定的目录为基准进行解析。</p>
<p>参见 <code>--project</code> 以仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-add--editable"><a href="#uv-add--editable"><code>--editable</code></a></dt><dd><p>以可编辑模式添加需求</p>
</dd><dt id="uv-add--exclude-newer"><a href="#uv-add--exclude-newer"><code>--exclude-newer</code></a> <i>exclude-newer</i></dt><dd><p>将候选包限制为在给定日期之前上传的版本。</p>
<p>日期是与每个分发作品的<em>上传时间</em>（即每个文件上传到包索引的时间）进行比较，而不是与包版本的发布日期进行比较。</p>
<p>接受 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、相同格式的本地日期（例如 <code>2006-12-02</code>，基于系统配置的时区解析）、&quot;友好&quot;持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不遵循本地时区的语义，始终以固定秒数解析，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月和年等日历单位。</p>
<p>也可以通过 <code>UV_EXCLUDE_NEWER</code> 环境变量设置。</p></dd><dt id="uv-add--exclude-newer-package"><a href="#uv-add--exclude-newer-package"><code>--exclude-newer-package</code></a> <i>exclude-newer-package</i></dt><dd><p>将特定包的候选版本限制为在给定日期之前上传的版本。</p>
<p>接受格式为 <code>包名=日期</code> 的包-日期对，其中 <code>日期</code> 是 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、相同格式的本地日期（例如 <code>2006-12-02</code>，基于系统配置的时区解析）、&quot;友好&quot;持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不遵循本地时区的语义，始终以固定秒数解析，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月和年等日历单位。</p>
<p>可以为不同的包多次提供。</p>
</dd><dt id="uv-add--extra"><a href="#uv-add--extra"><code>--extra</code></a> <i>extra</i></dt><dd><p>为依赖项启用的额外功能（extras）。</p>
<p>可以多次提供。</p>
<p>要将此依赖项添加到可选 extra 而非主依赖中，请参见 <code>--optional</code>。</p>
</dd><dt id="uv-add--extra-index-url"><a href="#uv-add--extra-index-url"><code>--extra-index-url</code></a> <i>extra-index-url</i></dt><dd><p>（已弃用：请改用 <code>--index</code>）除 <code>--index-url</code> 之外要使用的额外包索引 URL。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--index-url</code>（默认为 PyPI）指定的索引。当提供多个 <code>--extra-index-url</code> 标志时，较早的值优先级更高。</p>
<p>也可以通过 <code>UV_EXTRA_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-add--find-links"><a href="#uv-add--find-links"><code>--find-links</code></a>, <code>-f</code> <i>find-links</i></dt><dd><p>搜索候选分发作品的位置，作为注册表索引之外的补充来源。</p>
<p>如果是路径，目标必须是一个目录，顶层包含作为 wheel 文件（<code>.whl</code>）或源代码分发（例如 <code>.tar.gz</code> 或 <code>.zip</code>）的包。</p>
<p>如果是 URL，页面必须包含一个扁平列表，列出符合上述格式的包文件链接。</p>
<p>也可以通过 <code>UV_FIND_LINKS</code> 环境变量设置。</p></dd><dt id="uv-add--fork-strategy"><a href="#uv-add--fork-strategy"><code>--fork-strategy</code></a> <i>fork-strategy</i></dt><dd><p>在跨 Python 版本和平台选择给定包的多个版本时使用的策略。</p>
<p>默认情况下，uv 会优化为每个受支持的 Python 版本（<code>requires-python</code>）选择每个包的最新版本，同时最小化跨平台的选定版本数量。</p>
<p>在 <code>fewest</code> 策略下，uv 会最小化每个包的选定版本数量，倾向于选择与更广泛的受支持 Python 版本或平台兼容的较旧版本。</p>
<p>也可以通过 <code>UV_FORK_STRATEGY</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>fewest</code>:  优化为每个包选择最少的版本数量。如果较旧版本与更广泛的受支持 Python 版本或平台兼容，则可能优先选择较旧版本</li>
<li><code>requires-python</code>:  优化为每个受支持的 Python 版本选择每个包的最新支持版本</li>
</ul></dd><dt id="uv-add--frozen"><a href="#uv-add--frozen"><code>--frozen</code></a></dt><dd><p>添加依赖项而不重新锁定项目 [env: UV_FROZEN=]</p>
<p>项目环境将不会同步。</p>
</dd><dt id="uv-add--group"><a href="#uv-add--group"><code>--group</code></a> <i>group</i></dt><dd><p>将需求添加到指定的依赖组。</p>
<p>这些需求不会包含在项目的已发布元数据中。</p>
</dd><dt id="uv-add--help"><a href="#uv-add--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简洁帮助信息</p>
</dd><dt id="uv-add--index"><a href="#uv-add--index"><code>--index</code></a> <i>index</i></dt><dd><p>解析依赖项时使用的 URL，作为默认索引之外的补充。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--default-index</code>（默认为 PyPI）指定的索引。当提供多个 <code>--index</code> 标志时，较早的值优先级更高。</p>
<p>不支持索引名称作为值。相对路径必须通过以下方式与索引名称区分：在 Unix 上使用 <code>./</code> 或 <code>../</code>，在 Windows 上使用 <code>.\\</code>、<code>..\\</code>、<code>./</code> 或 <code>../</code>。</p>
<p>也可以通过 <code>UV_INDEX</code> 环境变量设置。</p></dd><dt id="uv-add--index-strategy"><a href="#uv-add--index-strategy"><code>--index-strategy</code></a> <i>index-strategy</i></dt><dd><p>在多个索引 URL 之间解析时使用的策略。</p>
<p>默认情况下，uv 会在第一个包含给定包的索引处停止，并将解析限制在该第一个索引上存在的版本（<code>first-index</code>）。这可以防止&quot;依赖混淆&quot;攻击，即攻击者可以在备用索引上上传同名的恶意包。</p>
<p>也可以通过 <code>UV_INDEX_STRATEGY</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>first-index</code>:  仅使用第一个为给定包名返回匹配的索引的结果</li>
<li><code>unsafe-first-match</code>:  在所有索引中搜索每个包名，在转到下一个索引之前耗尽第一个索引的版本</li>
<li><code>unsafe-best-match</code>:  在所有索引中搜索每个包名，优先选择&quot;最佳&quot;版本。如果某个包版本存在于多个索引中，则仅查看第一个索引中的条目</li>
</ul></dd><dt id="uv-add--index-url"><a href="#uv-add--index-url"><code>--index-url</code></a>, <code>-i</code> <i>index-url</i></dt><dd><p>（已弃用：请改用 <code>--default-index</code>）Python 包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--extra-index-url</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-add--keyring-provider"><a href="#uv-add--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>尝试使用 <code>keyring</code> 进行索引 URL 的身份验证。</p>
<p>目前仅支持 <code>--keyring-provider subprocess</code>，它配置 uv 使用 <code>keyring</code> CLI 来处理身份验证。</p>
<p>默认为 <code>disabled</code>。</p>
<p>也可以通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disabled</code>:  不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>:  使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-add--lfs"><a href="#uv-add--lfs"><code>--lfs</code></a></dt><dd><p>从 Git 添加依赖项时是否使用 Git LFS</p>
</dd><dt id="uv-add--link-mode"><a href="#uv-add--link-mode"><code>--link-mode</code></a> <i>link-mode</i></dt><dd><p>从全局缓存安装包时使用的方法。</p>
<p>默认情况下，在 macOS 和 Linux 上为 <code>clone</code>（也称为写时复制），在 Windows 上为 <code>hardlink</code>。</p>
<p>警告：不鼓励使用 symlink 链接模式，因为它会在缓存和目标环境之间创建紧密耦合。例如，清除缓存（<code>uv cache clean</code>）将通过删除底层源文件来破坏所有已安装的包。请谨慎使用符号链接。</p>
<p>也可以通过 <code>UV_LINK_MODE</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>clone</code>:  从源克隆（即写时复制）包到目标位置</li>
<li><code>copy</code>:  从源复制包到目标位置</li>
<li><code>hardlink</code>:  从源硬链接包到目标位置</li>
<li><code>symlink</code>:  从源符号链接包到目标位置</li>
</ul></dd><dt id="uv-add--locked"><a href="#uv-add--locked"><code>--locked</code></a></dt><dd><p>断言 <code>uv.lock</code> 将保持不变 [env: UV_LOCKED=]</p>
<p>需要锁文件是最新的。如果锁文件缺失或需要更新，uv 将退出并报错。</p>
</dd><dt id="uv-add--managed-python"><a href="#uv-add--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 倾向于使用它管理的 Python 版本。但是，如果没有安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-add--marker"><a href="#uv-add--marker"><code>--marker</code></a>, <code>-m</code> <i>marker</i></dt><dd><p>将此标记（marker）应用于所有添加的包</p>
</dd><dt id="uv-add--no-binary"><a href="#uv-add--no-binary"><code>--no-binary</code></a></dt><dd><p>不安装预构建的 wheel。</p>
<p>给定的包将从源代码构建和安装。解析器仍将使用预构建的 wheel 来提取包元数据（如果可用）。</p>
<p>也可以通过 <code>UV_NO_BINARY</code> 环境变量设置。</p></dd><dt id="uv-add--no-binary-package"><a href="#uv-add--no-binary-package"><code>--no-binary-package</code></a> <i>no-binary-package</i></dt><dd><p>不为特定包安装预构建的 wheel [env: <code>UV_NO_BINARY_PACKAGE</code>=]</p>
</dd><dt id="uv-add--no-build"><a href="#uv-add--no-build"><code>--no-build</code></a></dt><dd><p>不构建源代码分发。</p>
<p>启用后，解析过程不会运行任意 Python 代码。将重用已构建源代码分发的缓存 wheel，但需要构建分发的操作将退出并报错。</p>
<p>也可以通过 <code>UV_NO_BUILD</code> 环境变量设置。</p></dd><dt id="uv-add--no-build-isolation"><a href="#uv-add--no-build-isolation"><code>--no-build-isolation</code></a></dt><dd><p>构建源代码分发时禁用隔离。</p>
<p>假设 PEP 518 指定的构建依赖已安装。</p>
<p>也可以通过 <code>UV_NO_BUILD_ISOLATION</code> 环境变量设置。</p></dd><dt id="uv-add--no-build-isolation-package"><a href="#uv-add--no-build-isolation-package"><code>--no-build-isolation-package</code></a> <i>no-build-isolation-package</i></dt><dd><p>为特定包构建源代码分发时禁用隔离。</p>
<p>假设 PEP 518 指定的该包的构建依赖已安装。</p>
</dd><dt id="uv-add--no-build-package"><a href="#uv-add--no-build-package"><code>--no-build-package</code></a> <i>no-build-package</i></dt><dd><p>不为特定包构建源代码分发 [env: <code>UV_NO_BUILD_PACKAGE</code>=]</p>
</dd><dt id="uv-add--no-cache"><a href="#uv-add--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-add--no-config"><a href="#uv-add--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-add--no-index"><a href="#uv-add--no-index"><code>--no-index</code></a></dt><dd><p>忽略注册表索引（例如 PyPI），转而依赖直接 URL 依赖项和通过 <code>--find-links</code> 提供的依赖项</p>
</dd><dt id="uv-add--no-install-local"><a href="#uv-add--no-install-local"><code>--no-install-local</code></a></dt><dd><p>不安装本地路径依赖项 [env: UV_NO_INSTALL_LOCAL=]</p>
<p>跳过当前项目、工作区成员以及任何其他本地（路径或可编辑）包。仅安装远程/索引依赖项。在 Docker 构建中很有用，可以首先缓存重量级第三方依赖项，然后单独分层本地包。</p>
<p>反向选项 <code>--only-install-local</code> 可用于<em>仅</em>安装本地包，排除所有远程依赖项。</p>
</dd><dt id="uv-add--no-install-package"><a href="#uv-add--no-install-package"><code>--no-install-package</code></a> <i>no-install-package</i></dt><dd><p>不安装指定的包。</p>
<p>默认情况下，项目的所有依赖项都会安装到环境中。<code>--no-install-package</code> 选项允许排除特定包。请注意，这可能导致环境损坏，应谨慎使用。</p>
<p>反向选项 <code>--only-install-package</code> 可用于<em>仅</em>安装指定的包，排除所有其他包。</p>
</dd><dt id="uv-add--no-install-project"><a href="#uv-add--no-install-project"><code>--no-install-project</code></a></dt><dd><p>不安装当前项目 [env: UV_NO_INSTALL_PROJECT=]</p>
<p>默认情况下，当前项目会连同其所有依赖项一起安装到环境中。<code>--no-install-project</code> 选项允许排除项目，但其所有依赖项仍会被安装。这在构建 Docker 镜像等场景中特别有用，将项目与其依赖项分开安装可以实现最佳的层缓存。</p>
<p>反向选项 <code>--only-install-project</code> 可用于<em>仅</em>安装项目本身，排除所有依赖项。</p>
</dd><dt id="uv-add--no-install-workspace"><a href="#uv-add--no-install-workspace"><code>--no-install-workspace</code></a></dt><dd><p>不安装任何工作区成员，包括当前项目 [env: UV_NO_INSTALL_WORKSPACE=]</p>
<p>默认情况下，所有工作区成员及其依赖项都会安装到环境中。<code>--no-install-workspace</code> 选项允许排除所有工作区成员，同时保留其依赖项。这在构建 Docker 镜像等场景中特别有用，将工作区与其依赖项分开安装可以实现最佳的层缓存。</p>
<p>反向选项 <code>--only-install-workspace</code> 可用于<em>仅</em>安装工作区成员，排除所有其他依赖项。</p>
</dd><dt id="uv-add--no-managed-python"><a href="#uv-add--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>取而代之，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-add--no-progress"><a href="#uv-add--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转指示器或进度条。</p>
</dd><dt id="uv-add--no-python-downloads"><a href="#uv-add--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-add--no-sources"><a href="#uv-add--no-sources"><code>--no-sources</code></a></dt><dd><p>解析依赖项时忽略 <code>tool.uv.sources</code> 表。用于根据符合标准的、可发布的包元数据进行锁定，而不使用任何工作区、Git、URL 或本地路径源</p>
<p>也可以通过 <code>UV_NO_SOURCES</code> 环境变量设置。</p></dd><dt id="uv-add--no-sources-package"><a href="#uv-add--no-sources-package"><code>--no-sources-package</code></a> <i>no-sources-package</i></dt><dd><p>不为指定包使用 <code>tool.uv.sources</code> 表中的源 [env: <code>UV_NO_SOURCES_PACKAGE</code>=]</p>
</dd><dt id="uv-add--no-sync"><a href="#uv-add--no-sync"><code>--no-sync</code></a></dt><dd><p>避免同步虚拟环境 [env: UV_NO_SYNC=]</p>
</dd><dt id="uv-add--no-workspace"><a href="#uv-add--no-workspace"><code>--no-workspace</code></a></dt><dd><p>不要将依赖项添加为工作区成员。</p>
<p>默认情况下，当添加一个本地路径且位于工作区目录内的依赖项时，uv 会将其添加为工作区成员；传递 <code>--no-workspace</code> 可改为将包添加为直接路径依赖项。</p>
</dd><dt id="uv-add--offline"><a href="#uv-add--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-add--optional"><a href="#uv-add--optional"><code>--optional</code></a> <i>optional</i></dt><dd><p>将需求添加到包的指定 extra 的可选依赖项中。</p>
<p>然后可以在使用 <code>--extra</code> 标志安装项目时激活该组。</p>
<p>要为此需求启用可选 extra，请参见 <code>--extra</code>。</p>
</dd><dt id="uv-add--package"><a href="#uv-add--package"><code>--package</code></a> <i>package</i></dt><dd><p>将依赖项添加到工作区中的特定包</p>
</dd><dt id="uv-add--prerelease"><a href="#uv-add--prerelease"><code>--prerelease</code></a> <i>prerelease</i></dt><dd><p>考虑预发布版本时使用的策略。</p>
<p>默认情况下，uv 将接受<em>仅</em>发布预发布版本的包，以及声明的约束符中包含显式预发布标记的第一方需求（<code>if-necessary-or-explicit</code>）。</p>
<p>也可以通过 <code>UV_PRERELEASE</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disallow</code>:  不允许所有预发布版本</li>
<li><code>allow</code>:  允许所有预发布版本</li>
<li><code>if-necessary</code>:  如果某个包的所有版本都是预发布版本，则允许预发布版本</li>
<li><code>explicit</code>:  对于版本需求中带有显式预发布标记的第一方包，允许预发布版本</li>
<li><code>if-necessary-or-explicit</code>:  如果某个包的所有版本都是预发布版本，或者该包的版本需求中带有显式预发布标记，则允许预发布版本</li>
</ul></dd><dt id="uv-add--project"><a href="#uv-add--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-add--python"><a href="#uv-add--python"><code>--python</code></a>, <code>-p</code> <i>python</i></dt><dd><p>用于解析和同步的 Python 解释器。</p>
<p>有关 Python 发现和支持的请求格式的详细信息，请参见 <a href="#uv-python">uv python</a>。</p>
<p>也可以通过 <code>UV_PYTHON</code> 环境变量设置。</p></dd><dt id="uv-add--quiet"><a href="#uv-add--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-add--raw"><a href="#uv-add--raw"><code>--raw</code></a>, <code>--raw-sources</code></dt><dd><p>按原样添加依赖项。</p>
<p>默认情况下，uv 会使用 <code>tool.uv.sources</code> 部分来记录 Git、本地、可编辑和直接 URL 需求的源信息。当提供 <code>--raw</code> 时，uv 会将源需求添加到 <code>project.dependencies</code> 而不是 <code>tool.uv.sources</code>。</p>
<p>此外，默认情况下，uv 会为你的依赖项添加边界约束，例如 <code>foo&gt;=1.0.0</code>。当提供 <code>--raw</code> 时，uv 将添加不带边界约束的依赖项。</p>
</dd><dt id="uv-add--refresh"><a href="#uv-add--refresh"><code>--refresh</code></a></dt><dd><p>刷新所有缓存数据</p>
</dd><dt id="uv-add--refresh-package"><a href="#uv-add--refresh-package"><code>--refresh-package</code></a> <i>refresh-package</i></dt><dd><p>刷新特定包的缓存数据</p>
</dd><dt id="uv-add--reinstall"><a href="#uv-add--reinstall"><code>--reinstall</code></a>, <code>--force-reinstall</code></dt><dd><p>重新安装所有包，无论它们是否已安装。隐含 <code>--refresh</code></p>
</dd><dt id="uv-add--reinstall-package"><a href="#uv-add--reinstall-package"><code>--reinstall-package</code></a> <i>reinstall-package</i></dt><dd><p>重新安装特定包，无论它是否已安装。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-add--requirements"><a href="#uv-add--requirements"><code>--requirements</code></a>, <code>--requirement</code>, <code>-r</code> <i>requirements</i></dt><dd><p>添加给定文件中列出的包。</p>
<p>支持以下格式：<code>requirements.txt</code>、带内联元数据的 <code>.py</code> 文件、<code>pylock.toml</code>、<code>pyproject.toml</code>、<code>setup.py</code> 和 <code>setup.cfg</code>。</p>
</dd><dt id="uv-add--resolution"><a href="#uv-add--resolution"><code>--resolution</code></a> <i>resolution</i></dt><dd><p>在给定包需求的不同兼容版本之间进行选择时使用的策略。</p>
<p>默认情况下，uv 将使用每个包的最新兼容版本（<code>highest</code>）。</p>
<p>也可以通过 <code>UV_RESOLUTION</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>highest</code>:  解析每个包的最高兼容版本</li>
<li><code>lowest</code>:  解析每个包的最低兼容版本</li>
<li><code>lowest-direct</code>:  解析任何直接依赖项的最低兼容版本，以及任何传递依赖项的最高兼容版本</li>
</ul></dd><dt id="uv-add--rev"><a href="#uv-add--rev"><code>--rev</code></a> <i>rev</i></dt><dd><p>从 Git 添加依赖项时使用的提交</p>
</dd><dt id="uv-add--script"><a href="#uv-add--script"><code>--script</code></a> <i>script</i></dt><dd><p>将依赖项添加到指定的 Python 脚本，而不是添加到项目中。</p>
<p>如果提供，uv 将根据 PEP 723 将依赖项添加到脚本的内联元数据表中。如果不存在此类内联元数据表，将创建一个新的并添加到脚本中。通过 <code>uv run</code> 执行时，uv 将为脚本创建一个临时环境，并安装所有内联依赖项。</p>
</dd><dt id="uv-add--system-certs"><a href="#uv-add--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，你可能希望使用平台的原生证书存储，特别是当你依赖系统证书存储中包含的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-add--tag"><a href="#uv-add--tag"><code>--tag</code></a> <i>tag</i></dt><dd><p>从 Git 添加依赖项时使用的标签</p>
</dd><dt id="uv-add--upgrade"><a href="#uv-add--upgrade"><code>--upgrade</code></a>, <code>-U</code></dt><dd><p>允许包升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh</code></p>
</dd><dt id="uv-add--upgrade-group"><a href="#uv-add--upgrade-group"><code>--upgrade-group</code></a> <i>upgrade-group</i></dt><dd><p>允许依赖组中所有包的升级，忽略任何现有输出文件中的固定版本</p>
</dd><dt id="uv-add--upgrade-package"><a href="#uv-add--upgrade-package"><code>--upgrade-package</code></a>, <code>-P</code> <i>upgrade-package</i></dt><dd><p>允许特定包的升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-add--verbose"><a href="#uv-add--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>你可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd><dt id="uv-add--workspace"><a href="#uv-add--workspace"><code>--workspace</code></a></dt><dd><p>将依赖项添加为工作区成员。</p>
<p>默认情况下，uv 会将位于工作区目录内的路径依赖项添加为工作区成员。当与路径依赖项一起使用时，该包将被添加到根 <code>pyproject.toml</code> 文件中的工作区 <code>members</code> 列表中。</p>
</dd></dl>
