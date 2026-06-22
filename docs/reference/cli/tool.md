---
title: uv tool
description: uv tool 命令行参考文档，详细介绍了 uv 工具管理子命令的用法，包括 uv tool run（运行 Python 包命令）、uv tool install（安装工具）、uv tool upgrade（升级工具）、uv tool list（列出已安装工具）、uv tool uninstall（卸载工具）、uv tool update-shell（更新 PATH 配置）和 uv tool dir（显示工具目录路径），涵盖所有选项参数、环境变量配置、PyTorch 后端选择、平台目标指定等高级功能。
---

# uv tool

运行和安装由 Python 包提供的命令

<h3 class="cli-reference">用法</h3>

```
uv tool [OPTIONS] <COMMAND>
```

<h3 class="cli-reference">命令</h3>

<dl class="cli-reference"><dt><a href="#uv-tool-run"><code>uv tool run</code></a></dt><dd><p>运行由 Python 包提供的命令</p></dd>
<dt><a href="#uv-tool-install"><code>uv tool install</code></a></dt><dd><p>安装由 Python 包提供的命令</p></dd>
<dt><a href="#uv-tool-upgrade"><code>uv tool upgrade</code></a></dt><dd><p>升级已安装的工具</p></dd>
<dt><a href="#uv-tool-list"><code>uv tool list</code></a></dt><dd><p>列出已安装的工具</p></dd>
<dt><a href="#uv-tool-uninstall"><code>uv tool uninstall</code></a></dt><dd><p>卸载工具</p></dd>
<dt><a href="#uv-tool-update-shell"><code>uv tool update-shell</code></a></dt><dd><p>确保工具可执行文件目录在 <code>PATH</code> 中</p></dd>
<dt><a href="#uv-tool-dir"><code>uv tool dir</code></a></dt><dd><p>显示 uv 工具目录的路径</p></dd>
</dl>

### uv tool run

运行由 Python 包提供的命令。

默认情况下，要安装的包名称假定与命令名称相同。

命令名称可以包含精确版本，格式为 `<package>@<version>`，例如 `uv tool run ruff@0.3.0`。如果需要更复杂的版本指定，或者命令由其他包提供，请使用 `--from`。

`uvx` 可用于调用 Python，例如通过 `uvx python` 或 `uvx python@<version>`。Python 解释器将在隔离的虚拟环境中启动。

如果该工具之前已安装（即通过 `uv tool install`），则将使用已安装的版本，除非请求了特定版本或使用了 `--isolated` 标志。

`uvx` 是 `uv tool run` 的便捷别名，其行为完全相同。

如果未提供命令，则显示已安装的工具。

包会被安装到 uv 缓存目录中的一个临时虚拟环境中。

<h3 class="cli-reference">用法</h3>

```
uv tool run [OPTIONS] [COMMAND]
```

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-tool-run--allow-insecure-host"><a href="#uv-tool-run--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许连接到不安全的主机。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统的证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您面临中间人攻击（MITM）的风险。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-tool-run--build-constraints"><a href="#uv-tool-run--build-constraints"><code>--build-constraints</code></a>, <code>--build-constraint</code>, <code>-b</code> <i>build-constraints</i></dt><dd><p>在构建源码分发包时，使用给定的 requirements 文件约束构建依赖项。</p>
<p>约束文件是类似 <code>requirements.txt</code> 的文件，仅控制所安装依赖项的<em>版本</em>。但是，在约束文件中包含某个包<em>不会</em>触发该包的安装。</p>
<p>也可以通过 <code>UV_BUILD_CONSTRAINT</code> 环境变量设置。</p></dd><dt id="uv-tool-run--cache-dir"><a href="#uv-tool-run--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-tool-run--color"><a href="#uv-tool-run--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可能的值：</p>
<ul>
<li><code>auto</code>：仅当输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-tool-run--compile-bytecode"><a href="#uv-tool-run--compile-bytecode"><code>--compile-bytecode</code></a>, <code>--compile</code></dt><dd><p>安装后将 Python 文件编译为字节码。</p>
<p>默认情况下，uv 不会将 Python（<code>.py</code>）文件编译为字节码（<code>__pycache__/*.pyc</code>）；相反，编译会在首次导入模块时延迟执行。对于启动时间至关重要的用例（如 CLI 应用程序和 Docker 容器），可以启用此选项，以较长的安装时间换取更快的启动时间。</p>
<p>启用后，uv 将处理整个 site-packages 目录（包括当前操作未修改的包）以保持一致性。与 pip 类似，它也会忽略错误。</p>
<p>也可以通过 <code>UV_COMPILE_BYTECODE</code> 环境变量设置。</p></dd><dt id="uv-tool-run--config-file"><a href="#uv-tool-run--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许使用。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-tool-run--config-setting"><a href="#uv-tool-run--config-setting"><code>--config-setting</code></a>, <code>--config-settings</code>, <code>-C</code> <i>config-setting</i></dt><dd><p>传递给 PEP 517 构建后端的设置，以 <code>KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-tool-run--config-settings-package"><a href="#uv-tool-run--config-settings-package"><code>--config-settings-package</code></a>, <code>--config-settings-package</code> <i>config-settings-package</i></dt><dd><p>为特定包传递给 PEP 517 构建后端的设置，以 <code>PACKAGE:KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-tool-run--constraints"><a href="#uv-tool-run--constraints"><code>--constraints</code></a>, <code>--constraint</code>, <code>-c</code> <i>constraints</i></dt><dd><p>使用给定的 requirements 文件约束版本。</p>
<p>约束文件是类似 <code>requirements.txt</code> 的文件，仅控制所安装依赖项的<em>版本</em>。但是，在约束文件中包含某个包<em>不会</em>触发该包的安装。</p>
<p>这等同于 pip 的 <code>--constraint</code> 选项。</p>
<p>也可以通过 <code>UV_CONSTRAINT</code> 环境变量设置。</p></dd><dt id="uv-tool-run--default-index"><a href="#uv-tool-run--default-index"><code>--default-index</code></a> <i>default-index</i></dt><dd><p>默认包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或以相同格式组织的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--index</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_DEFAULT_INDEX</code> 环境变量设置。</p></dd><dt id="uv-tool-run--directory"><a href="#uv-tool-run--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到给定目录。</p>
<p>相对路径以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 以仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-tool-run--env-file"><a href="#uv-tool-run--env-file"><code>--env-file</code></a> <i>env-file</i></dt><dd><p>从 <code>.env</code> 文件加载环境变量。</p>
<p>可以多次提供，后续文件会覆盖先前文件中定义的值。</p>
<p>也可以通过 <code>UV_ENV_FILE</code> 环境变量设置。</p></dd><dt id="uv-tool-run--exclude-newer"><a href="#uv-tool-run--exclude-newer"><code>--exclude-newer</code></a> <i>exclude-newer</i></dt><dd><p>将候选包限制为在给定日期之前上传的版本。</p>
<p>日期与每个分发包构件的上传时间（即每个文件上传到包索引的时间）进行比较，而非包版本的发布日期。</p>
<p>接受 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、基于系统配置时区解析的相同格式的本地日期（例如 <code>2006-12-02</code>）、"友好"持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不考虑本地时区的语义，始终解析为固定的秒数，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月份和年份等日历单位。</p>
<p>也可以通过 <code>UV_EXCLUDE_NEWER</code> 环境变量设置。</p></dd><dt id="uv-tool-run--exclude-newer-package"><a href="#uv-tool-run--exclude-newer-package"><code>--exclude-newer-package</code></a> <i>exclude-newer-package</i></dt><dd><p>将特定包的候选包限制为在给定日期之前上传的版本。</p>
<p>接受 <code>PACKAGE=DATE</code> 格式的包-日期对，其中 <code>DATE</code> 是 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、基于系统配置时区解析的相同格式的本地日期（例如 <code>2006-12-02</code>）、"友好"持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不考虑本地时区的语义，始终解析为固定的秒数，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月份和年份等日历单位。</p>
<p>可以为不同的包多次提供。</p>
</dd><dt id="uv-tool-run--extra-index-url"><a href="#uv-tool-run--extra-index-url"><code>--extra-index-url</code></a> <i>extra-index-url</i></dt><dd><p>（已弃用：请改用 <code>--index</code>）除 <code>--index-url</code> 之外，要使用的额外包索引 URL。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或以相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--index-url</code>（默认为 PyPI）指定的索引。当提供多个 <code>--extra-index-url</code> 标志时，较早的值优先。</p>
<p>也可以通过 <code>UV_EXTRA_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-tool-run--find-links"><a href="#uv-tool-run--find-links"><code>--find-links</code></a>, <code>-f</code> <i>find-links</i></dt><dd><p>除注册表索引中找到的分发包外，还要搜索候选分发包的位置。</p>
<p>如果是路径，目标必须是一个目录，其中包含顶层 wheel 文件（<code>.whl</code>）或源码分发包（例如 <code>.tar.gz</code> 或 <code>.zip</code>）。</p>
<p>如果是 URL，页面必须包含指向符合上述格式的包文件的扁平链接列表。</p>
<p>也可以通过 <code>UV_FIND_LINKS</code> 环境变量设置。</p></dd><dt id="uv-tool-run--fork-strategy"><a href="#uv-tool-run--fork-strategy"><code>--fork-strategy</code></a> <i>fork-strategy</i></dt><dd><p>在跨 Python 版本和平台为给定包选择多个版本时使用的策略。</p>
<p>默认情况下，uv 会优化为每个支持的 Python 版本（<code>requires-python</code>）选择每个包的最新版本，同时最小化跨平台选择的版本数量。</p>
<p>在 <code>fewest</code> 策略下，uv 将最小化每个包选择的版本数量，优先选择与更广泛支持的 Python 版本或平台兼容的旧版本。</p>
<p>也可以通过 <code>UV_FORK_STRATEGY</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>fewest</code>：优化为每个包选择最少数量的版本。如果旧版本与更广泛支持的 Python 版本或平台兼容，则可能优先选择旧版本</li>
<li><code>requires-python</code>：为每个支持的 Python 版本优化选择每个包的最新支持版本</li>
</ul></dd><dt id="uv-tool-run--from"><a href="#uv-tool-run--from"><code>--from</code></a> <i>from</i></dt><dd><p>使用给定的包来提供命令。</p>
<p>默认情况下，包名称假定与命令名称匹配。</p>
</dd><dt id="uv-tool-run--help"><a href="#uv-tool-run--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简要帮助</p>
</dd><dt id="uv-tool-run--index"><a href="#uv-tool-run--index"><code>--index</code></a> <i>index</i></dt><dd><p>解析依赖项时使用的 URL，除默认索引之外。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或以相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--default-index</code>（默认为 PyPI）指定的索引。当提供多个 <code>--index</code> 标志时，较早的值优先。</p>
<p>不支持索引名称作为值。相对路径必须通过 <code>./</code> 或 <code>../</code>（Unix）或 <code>.\\</code>、<code>..\\</code>、<code>./</code> 或 <code>../</code>（Windows）与索引名称区分开来。</p>
<p>也可以通过 <code>UV_INDEX</code> 环境变量设置。</p></dd><dt id="uv-tool-run--index-strategy"><a href="#uv-tool-run--index-strategy"><code>--index-strategy</code></a> <i>index-strategy</i></dt><dd><p>针对多个索引 URL 进行解析时使用的策略。</p>
<p>默认情况下，uv 会在第一个找到给定包的索引处停止，并将解析限制为该第一个索引上存在的版本（<code>first-index</code>）。这可以防止"依赖混淆"攻击，即攻击者可以在备用索引上以相同名称上传恶意包。</p>
<p>也可以通过 <code>UV_INDEX_STRATEGY</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>first-index</code>：仅使用第一个返回给定包名匹配结果的索引</li>
<li><code>unsafe-first-match</code>：在所有索引中搜索每个包名，先穷尽第一个索引的版本，然后再转到下一个</li>
<li><code>unsafe-best-match</code>：在所有索引中搜索每个包名，优先选择找到的"最佳"版本。如果一个包版本存在于多个索引中，则只查看第一个索引的条目</li>
</ul></dd><dt id="uv-tool-run--index-url"><a href="#uv-tool-run--index-url"><code>--index-url</code></a>, <code>-i</code> <i>index-url</i></dt><dd><p>（已弃用：请改用 <code>--default-index</code>）Python 包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或以相同格式组织的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--extra-index-url</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-tool-run--isolated"><a href="#uv-tool-run--isolated"><code>--isolated</code></a></dt><dd><p>在隔离的虚拟环境中运行工具，忽略任何已安装的工具 [env: UV_ISOLATED=]</p>
</dd><dt id="uv-tool-run--keyring-provider"><a href="#uv-tool-run--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>尝试使用 <code>keyring</code> 进行索引 URL 的身份验证。</p>
<p>目前仅支持 <code>--keyring-provider subprocess</code>，它配置 uv 使用 <code>keyring</code> CLI 来处理身份验证。</p>
<p>默认为 <code>disabled</code>。</p>
<p>也可以通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>disabled</code>：不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>：使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-tool-run--lfs"><a href="#uv-tool-run--lfs"><code>--lfs</code></a></dt><dd><p>从 Git 添加依赖项时是否使用 Git LFS</p>
</dd><dt id="uv-tool-run--link-mode"><a href="#uv-tool-run--link-mode"><code>--link-mode</code></a> <i>link-mode</i></dt><dd><p>从全局缓存安装包时使用的方法。</p>
<p>在 macOS 和 Linux 上默认为 <code>clone</code>（也称为写时复制），在 Windows 上默认为 <code>hardlink</code>。</p>
<p>警告：不鼓励使用 symlink 链接模式，因为它会在缓存和目标环境之间创建紧密耦合。例如，清除缓存（<code>uv cache clean</code>）将通过删除底层源文件来破坏所有已安装的包。请谨慎使用符号链接。</p>
<p>也可以通过 <code>UV_LINK_MODE</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>clone</code>：将包从源克隆（即写时复制）到目标</li>
<li><code>copy</code>：将包从源复制到目标</li>
<li><code>hardlink</code>：将包从源硬链接到目标</li>
<li><code>symlink</code>：将包从源符号链接到目标</li>
</ul></dd><dt id="uv-tool-run--managed-python"><a href="#uv-tool-run--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用它管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-tool-run--no-binary"><a href="#uv-tool-run--no-binary"><code>--no-binary</code></a></dt><dd><p>不安装预编译的 wheel。</p>
<p>给定的包将从源码构建和安装。解析器仍将使用预编译的 wheel 来提取包元数据（如果可用）。</p>
<p>也可以通过 <code>UV_NO_BINARY</code> 环境变量设置。</p></dd><dt id="uv-tool-run--no-binary-package"><a href="#uv-tool-run--no-binary-package"><code>--no-binary-package</code></a> <i>no-binary-package</i></dt><dd><p>不为特定包安装预编译的 wheel [env: <code>UV_NO_BINARY_PACKAGE</code>=]</p>
</dd><dt id="uv-tool-run--no-build"><a href="#uv-tool-run--no-build"><code>--no-build</code></a></dt><dd><p>不构建源码分发包。</p>
<p>启用后，解析将不会运行任意 Python 代码。已构建的源码分发包的缓存 wheel 将被重用，但需要构建分发包的操作将退出并报错。</p>
<p>也可以通过 <code>UV_NO_BUILD</code> 环境变量设置。</p></dd><dt id="uv-tool-run--no-build-isolation"><a href="#uv-tool-run--no-build-isolation"><code>--no-build-isolation</code></a></dt><dd><p>构建源码分发包时禁用隔离。</p>
<p>假定 PEP 518 指定的构建依赖项已安装。</p>
<p>也可以通过 <code>UV_NO_BUILD_ISOLATION</code> 环境变量设置。</p></dd><dt id="uv-tool-run--no-build-isolation-package"><a href="#uv-tool-run--no-build-isolation-package"><code>--no-build-isolation-package</code></a> <i>no-build-isolation-package</i></dt><dd><p>为特定包构建源码分发包时禁用隔离。</p>
<p>假定该包的 PEP 518 构建依赖项已安装。</p>
</dd><dt id="uv-tool-run--no-build-package"><a href="#uv-tool-run--no-build-package"><code>--no-build-package</code></a> <i>no-build-package</i></dt><dd><p>不为特定包构建源码分发包 [env: <code>UV_NO_BUILD_PACKAGE</code>=]</p>
</dd><dt id="uv-tool-run--no-cache"><a href="#uv-tool-run--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，在操作期间改用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-tool-run--no-config"><a href="#uv-tool-run--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>正常情况下，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-tool-run--no-env-file"><a href="#uv-tool-run--no-env-file"><code>--no-env-file</code></a></dt><dd><p>避免从 <code>.env</code> 文件读取环境变量 [env: UV_NO_ENV_FILE=]</p>
</dd><dt id="uv-tool-run--no-index"><a href="#uv-tool-run--no-index"><code>--no-index</code></a></dt><dd><p>忽略注册表索引（例如 PyPI），转而依赖直接 URL 依赖项和通过 <code>--find-links</code> 提供的依赖项</p>
</dd><dt id="uv-tool-run--no-managed-python"><a href="#uv-tool-run--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-tool-run--no-progress"><a href="#uv-tool-run--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转指示器或进度条。</p>
</dd><dt id="uv-tool-run--no-python-downloads"><a href="#uv-tool-run--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-tool-run--no-sources"><a href="#uv-tool-run--no-sources"><code>--no-sources</code></a></dt><dd><p>解析依赖项时忽略 <code>tool.uv.sources</code> 表。用于根据符合标准、可发布的包元数据进行锁定，而不是使用任何工作区、Git、URL 或本地路径源</p>
<p>也可以通过 <code>UV_NO_SOURCES</code> 环境变量设置。</p></dd><dt id="uv-tool-run--no-sources-package"><a href="#uv-tool-run--no-sources-package"><code>--no-sources-package</code></a> <i>no-sources-package</i></dt><dd><p>不为指定包使用 <code>tool.uv.sources</code> 表中的源 [env: <code>UV_NO_SOURCES_PACKAGE</code>=]</p>
</dd><dt id="uv-tool-run--offline"><a href="#uv-tool-run--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-tool-run--overrides"><a href="#uv-tool-run--overrides"><code>--overrides</code></a>, <code>--override</code> <i>overrides</i></dt><dd><p>使用给定的 requirements 文件覆盖版本。</p>
<p>覆盖文件是类似 <code>requirements.txt</code> 的文件，强制安装特定版本的需求，无论任何组成包声明了什么需求，也无论这是否会被视为无效的解析。</p>
<p>约束是<em>附加性的</em>，即它们与组成包的需求相结合；而覆盖是<em>绝对性的</em>，即它们完全替换组成包的需求。</p>
<p>也可以通过 <code>UV_OVERRIDE</code> 环境变量设置。</p></dd><dt id="uv-tool-run--prerelease"><a href="#uv-tool-run--prerelease"><code>--prerelease</code></a> <i>prerelease</i></dt><dd><p>考虑预发布版本时使用的策略。</p>
<p>默认情况下，uv 将接受<em>仅</em>发布预发布版本的包的预发布版本，以及声明的版本说明符中包含显式预发布标记的第一方依赖项（<code>if-necessary-or-explicit</code>）。</p>
<p>也可以通过 <code>UV_PRERELEASE</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>disallow</code>：禁止所有预发布版本</li>
<li><code>allow</code>：允许所有预发布版本</li>
<li><code>if-necessary</code>：如果包的所有版本都是预发布版本，则允许预发布版本</li>
<li><code>explicit</code>：允许版本要求中包含显式预发布标记的第一方包的预发布版本</li>
<li><code>if-necessary-or-explicit</code>：如果包的所有版本都是预发布版本，或者包在其版本要求中有显式预发布标记，则允许预发布版本</li>
</ul></dd><dt id="uv-tool-run--project"><a href="#uv-tool-run--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-tool-run--python"><a href="#uv-tool-run--python"><code>--python</code></a>, <code>-p</code> <i>python</i></dt><dd><p>用于构建运行环境的 Python 解释器。</p>
<p>有关 Python 发现和支持的请求格式的详细信息，请参见 <a href="#uv-python">uv python</a>。</p>
<p>也可以通过 <code>UV_PYTHON</code> 环境变量设置。</p></dd><dt id="uv-tool-run--python-platform"><a href="#uv-tool-run--python-platform"><code>--python-platform</code></a> <i>python-platform</i></dt><dd><p>应为其安装依赖项的平台。</p>
<p>表示为"目标三元组"，一个描述目标平台的字符串，包含其 CPU、供应商和操作系统名称，如 <code>x86_64-unknown-linux-gnu</code> 或 <code>aarch64-apple-darwin</code>。</p>
<p>当目标为 macOS（Darwin）时，默认最低版本为 <code>13.0</code>。使用 <code>MACOSX_DEPLOYMENT_TARGET</code> 指定不同的最低版本，例如 <code>14.0</code>。</p>
<p>当目标为 iOS 时，默认最低版本为 <code>13.0</code>。使用 <code>IPHONEOS_DEPLOYMENT_TARGET</code> 指定不同的最低版本，例如 <code>14.0</code>。</p>
<p>当目标为 Android 时，默认最低 Android API 级别为 <code>24</code>。使用 <code>ANDROID_API_LEVEL</code> 指定不同的最低版本，例如 <code>26</code>。</p>
<p>警告：指定后，uv 将选择与<em>目标</em>平台兼容的 wheel；因此，已安装的分发包可能与<em>当前</em>平台不兼容。相反，从源码构建的任何分发包可能与<em>目标</em>平台不兼容，因为它们将针对<em>当前</em>平台构建。<code>--python-platform</code> 选项适用于高级用例。</p>
<p>可能的值：</p>
<ul>
<li><code>windows</code>：<code>x86_64-pc-windows-msvc</code> 的别名，Windows 的默认目标</li>
<li><code>linux</code>：<code>x86_64-unknown-linux-gnu</code> 的别名，Linux 的默认目标</li>
<li><code>macos</code>：<code>aarch64-apple-darwin</code> 的别名，macOS 的默认目标</li>
<li><code>x86_64-pc-windows-msvc</code>：64 位 x86 Windows 目标</li>
<li><code>aarch64-pc-windows-msvc</code>：ARM64 Windows 目标</li>
<li><code>i686-pc-windows-msvc</code>：32 位 x86 Windows 目标</li>
<li><code>x86_64-unknown-linux-gnu</code>：x86 Linux 目标。等同于 <code>x86_64-manylinux_2_28</code></li>
<li><code>aarch64-apple-darwin</code>：基于 ARM 的 macOS 目标，如 Apple Silicon 设备所示</li>
<li><code>x86_64-apple-darwin</code>：x86 macOS 目标</li>
<li><code>aarch64-unknown-linux-gnu</code>：ARM64 Linux 目标。等同于 <code>aarch64-manylinux_2_28</code></li>
<li><code>aarch64-unknown-linux-musl</code>：ARM64 Linux 目标</li>
<li><code>x86_64-unknown-linux-musl</code>：<code>x86_64</code> Linux 目标</li>
<li><code>riscv64-unknown-linux</code>：RISCV64 Linux 目标</li>
<li><code>x86_64-manylinux2014</code>：<code>manylinux2014</code> 平台的 <code>x86_64</code> 目标。等同于 <code>x86_64-manylinux_2_17</code></li>
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
<li><code>aarch64-manylinux2014</code>：<code>manylinux2014</code> 平台的 ARM64 目标。等同于 <code>aarch64-manylinux_2_17</code></li>
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
</ul></dd><dt id="uv-tool-run--quiet"><a href="#uv-tool-run--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，uv 将不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-tool-run--refresh"><a href="#uv-tool-run--refresh"><code>--refresh</code></a></dt><dd><p>刷新所有缓存数据</p>
</dd><dt id="uv-tool-run--refresh-package"><a href="#uv-tool-run--refresh-package"><code>--refresh-package</code></a> <i>refresh-package</i></dt><dd><p>刷新特定包的缓存数据</p>
</dd><dt id="uv-tool-run--reinstall"><a href="#uv-tool-run--reinstall"><code>--reinstall</code></a>, <code>--force-reinstall</code></dt><dd><p>重新安装所有包，无论它们是否已安装。隐含 <code>--refresh</code></p>
</dd><dt id="uv-tool-run--reinstall-package"><a href="#uv-tool-run--reinstall-package"><code>--reinstall-package</code></a> <i>reinstall-package</i></dt><dd><p>重新安装特定包，无论它是否已安装。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-tool-run--resolution"><a href="#uv-tool-run--resolution"><code>--resolution</code></a> <i>resolution</i></dt><dd><p>在给定包的不同兼容版本之间进行选择时使用的策略。</p>
<p>默认情况下，uv 将使用每个包的最新兼容版本（<code>highest</code>）。</p>
<p>也可以通过 <code>UV_RESOLUTION</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>highest</code>：解析每个包的最高兼容版本</li>
<li><code>lowest</code>：解析每个包的最低兼容版本</li>
<li><code>lowest-direct</code>：解析任何直接依赖项的最低兼容版本，以及任何传递依赖项的最高兼容版本</li>
</ul></dd><dt id="uv-tool-run--system-certs"><a href="#uv-tool-run--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能希望使用平台的原生证书存储，特别是当您依赖系统证书存储中包含的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-tool-run--torch-backend"><a href="#uv-tool-run--torch-backend"><code>--torch-backend</code></a> <i>torch-backend</i></dt><dd><p>获取 PyTorch 生态系统中的包时使用的后端（例如 <code>cpu</code>、<code>cu126</code> 或 <code>auto</code>）</p>
<p>设置后，uv 将忽略 PyTorch 生态系统中包的已配置索引 URL，转而使用定义的后端。</p>
<p>例如，当设置为 <code>cpu</code> 时，uv 将使用仅 CPU 的 PyTorch 索引；当设置为 <code>cu126</code> 时，uv 将使用 CUDA 12.6 的 PyTorch 索引。</p>
<p><code>auto</code> 模式将尝试根据当前安装的 CUDA 驱动程序检测适当的 PyTorch 索引。</p>
<p>此选项处于预览阶段，可能在任何未来版本中发生更改。</p>
<p>也可以通过 <code>UV_TORCH_BACKEND</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>auto</code>：根据操作系统和 CUDA 驱动程序版本选择适当的 PyTorch 索引</li>
<li><code>cpu</code>：使用仅 CPU 的 PyTorch 索引</li>
<li><code>cu130</code>：使用 CUDA 13.0 的 PyTorch 索引</li>
<li><code>cu129</code>：使用 CUDA 12.9 的 PyTorch 索引</li>
<li><code>cu128</code>：使用 CUDA 12.8 的 PyTorch 索引</li>
<li><code>cu126</code>：使用 CUDA 12.6 的 PyTorch 索引</li>
<li><code>cu125</code>：使用 CUDA 12.5 的 PyTorch 索引</li>
<li><code>cu124</code>：使用 CUDA 12.4 的 PyTorch 索引</li>
<li><code>cu123</code>：使用 CUDA 12.3 的 PyTorch 索引</li>
<li><code>cu122</code>：使用 CUDA 12.2 的 PyTorch 索引</li>
<li><code>cu121</code>：使用 CUDA 12.1 的 PyTorch 索引</li>
<li><code>cu120</code>：使用 CUDA 12.0 的 PyTorch 索引</li>
<li><code>cu118</code>：使用 CUDA 11.8 的 PyTorch 索引</li>
<li><code>cu117</code>：使用 CUDA 11.7 的 PyTorch 索引</li>
<li><code>cu116</code>：使用 CUDA 11.6 的 PyTorch 索引</li>
<li><code>cu115</code>：使用 CUDA 11.5 的 PyTorch 索引</li>
<li><code>cu114</code>：使用 CUDA 11.4 的 PyTorch 索引</li>
<li><code>cu113</code>：使用 CUDA 11.3 的 PyTorch 索引</li>
<li><code>cu112</code>：使用 CUDA 11.2 的 PyTorch 索引</li>
<li><code>cu111</code>：使用 CUDA 11.1 的 PyTorch 索引</li>
<li><code>cu110</code>：使用 CUDA 11.0 的 PyTorch 索引</li>
<li><code>cu102</code>：使用 CUDA 10.2 的 PyTorch 索引</li>
<li><code>cu101</code>：使用 CUDA 10.1 的 PyTorch 索引</li>
<li><code>cu100</code>：使用 CUDA 10.0 的 PyTorch 索引</li>
<li><code>cu92</code>：使用 CUDA 9.2 的 PyTorch 索引</li>
<li><code>cu91</code>：使用 CUDA 9.1 的 PyTorch 索引</li>
<li><code>cu90</code>：使用 CUDA 9.0 的 PyTorch 索引</li>
<li><code>cu80</code>：使用 CUDA 8.0 的 PyTorch 索引</li>
<li><code>rocm7.2</code>：使用 ROCm 7.2 的 PyTorch 索引</li>
<li><code>rocm7.1</code>：使用 ROCm 7.1 的 PyTorch 索引</li>
<li><code>rocm7.0</code>：使用 ROCm 7.0 的 PyTorch 索引</li>
<li><code>rocm6.4</code>：使用 ROCm 6.4 的 PyTorch 索引</li>
<li><code>rocm6.3</code>：使用 ROCm 6.3 的 PyTorch 索引</li>
<li><code>rocm6.2.4</code>：使用 ROCm 6.2.4 的 PyTorch 索引</li>
<li><code>rocm6.2</code>：使用 ROCm 6.2 的 PyTorch 索引</li>
<li><code>rocm6.1</code>：使用 ROCm 6.1 的 PyTorch 索引</li>
<li><code>rocm6.0</code>：使用 ROCm 6.0 的 PyTorch 索引</li>
<li><code>rocm5.7</code>：使用 ROCm 5.7 的 PyTorch 索引</li>
<li><code>rocm5.6</code>：使用 ROCm 5.6 的 PyTorch 索引</li>
<li><code>rocm5.5</code>：使用 ROCm 5.5 的 PyTorch 索引</li>
<li><code>rocm5.4.2</code>：使用 ROCm 5.4.2 的 PyTorch 索引</li>
<li><code>rocm5.4</code>：使用 ROCm 5.4 的 PyTorch 索引</li>
<li><code>rocm5.3</code>：使用 ROCm 5.3 的 PyTorch 索引</li>
<li><code>rocm5.2</code>：使用 ROCm 5.2 的 PyTorch 索引</li>
<li><code>rocm5.1.1</code>：使用 ROCm 5.1.1 的 PyTorch 索引</li>
<li><code>rocm4.2</code>：使用 ROCm 4.2 的 PyTorch 索引</li>
<li><code>rocm4.1</code>：使用 ROCm 4.1 的 PyTorch 索引</li>
<li><code>rocm4.0.1</code>：使用 ROCm 4.0.1 的 PyTorch 索引</li>
<li><code>xpu</code>：使用 Intel XPU 的 PyTorch 索引</li>
</ul></dd><dt id="uv-tool-run--upgrade"><a href="#uv-tool-run--upgrade"><code>--upgrade</code></a>, <code>-U</code></dt><dd><p>允许包升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh</code></p>
</dd><dt id="uv-tool-run--upgrade-group"><a href="#uv-tool-run--upgrade-group"><code>--upgrade-group</code></a> <i>upgrade-group</i></dt><dd><p>允许依赖组中所有包的升级，忽略任何现有输出文件中的固定版本</p>
</dd><dt id="uv-tool-run--upgrade-package"><a href="#uv-tool-run--upgrade-package"><code>--upgrade-package</code></a>, <code>-P</code> <i>upgrade-package</i></dt><dd><p>允许特定包的升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-tool-run--verbose"><a href="#uv-tool-run--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd><dt id="uv-tool-run--with"><a href="#uv-tool-run--with"><code>--with</code></a>, <code>-w</code> <i>with</i></dt><dd><p>使用给定的已安装包运行</p>
</dd><dt id="uv-tool-run--with-editable"><a href="#uv-tool-run--with-editable"><code>--with-editable</code></a> <i>with-editable</i></dt><dd><p>使用以可编辑模式安装的给定包运行</p>
<p>在项目中使用时，这些依赖项将在单独的临时环境中叠加在 uv 工具环境之上。这些依赖项允许与指定的依赖项冲突。</p>
</dd><dt id="uv-tool-run--with-requirements"><a href="#uv-tool-run--with-requirements"><code>--with-requirements</code></a> <i>with-requirements</i></dt><dd><p>使用给定文件中列出的包运行。</p>
<p>支持以下格式：<code>requirements.txt</code>、带有内联元数据的 <code>.py</code> 文件和 <code>pylock.toml</code>。</p>
</dd></dl>

### uv tool install

安装由 Python 包提供的命令。

包会被安装到 uv 工具目录中的隔离虚拟环境。可执行文件被链接到工具可执行文件目录，该目录根据 XDG 标准确定，可以通过 `uv tool dir --bin` 获取。

如果该工具之前已安装，现有工具通常会被替换。

<h3 class="cli-reference">用法</h3>

```
uv tool install [OPTIONS] <PACKAGE>
```

<h3 class="cli-reference">参数</h3>

<dl class="cli-reference"><dt id="uv-tool-install--package"><a href="#uv-tool-install--package"><code>PACKAGE</code></a></dt><dd><p>要从中安装命令的包</p>
</dd></dl>

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-tool-install--allow-insecure-host"><a href="#uv-tool-install--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许连接到不安全的主机。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统的证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您面临中间人攻击（MITM）的风险。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-tool-install--build-constraints"><a href="#uv-tool-install--build-constraints"><code>--build-constraints</code></a>, <code>--build-constraint</code>, <code>-b</code> <i>build-constraints</i></dt><dd><p>在构建源码分发包时，使用给定的 requirements 文件约束构建依赖项。</p>
<p>约束文件是类似 <code>requirements.txt</code> 的文件，仅控制所安装依赖项的<em>版本</em>。但是，在约束文件中包含某个包<em>不会</em>触发该包的安装。</p>
<p>也可以通过 <code>UV_BUILD_CONSTRAINT</code> 环境变量设置。</p></dd><dt id="uv-tool-install--cache-dir"><a href="#uv-tool-install--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-tool-install--color"><a href="#uv-tool-install--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可能的值：</p>
<ul>
<li><code>auto</code>：仅当输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-tool-install--compile-bytecode"><a href="#uv-tool-install--compile-bytecode"><code>--compile-bytecode</code></a>, <code>--compile</code></dt><dd><p>安装后将 Python 文件编译为字节码。</p>
<p>默认情况下，uv 不会将 Python（<code>.py</code>）文件编译为字节码（<code>__pycache__/*.pyc</code>）；相反，编译会在首次导入模块时延迟执行。对于启动时间至关重要的用例（如 CLI 应用程序和 Docker 容器），可以启用此选项，以较长的安装时间换取更快的启动时间。</p>
<p>启用后，uv 将处理整个 site-packages 目录（包括当前操作未修改的包）以保持一致性。与 pip 类似，它也会忽略错误。</p>
<p>也可以通过 <code>UV_COMPILE_BYTECODE</code> 环境变量设置。</p></dd><dt id="uv-tool-install--config-file"><a href="#uv-tool-install--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许使用。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-tool-install--config-setting"><a href="#uv-tool-install--config-setting"><code>--config-setting</code></a>, <code>--config-settings</code>, <code>-C</code> <i>config-setting</i></dt><dd><p>传递给 PEP 517 构建后端的设置，以 <code>KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-tool-install--config-settings-package"><a href="#uv-tool-install--config-settings-package"><code>--config-settings-package</code></a>, <code>--config-settings-package</code> <i>config-settings-package</i></dt><dd><p>为特定包传递给 PEP 517 构建后端的设置，以 <code>PACKAGE:KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-tool-install--constraints"><a href="#uv-tool-install--constraints"><code>--constraints</code></a>, <code>--constraint</code>, <code>-c</code> <i>constraints</i></dt><dd><p>使用给定的 requirements 文件约束版本。</p>
<p>约束文件是类似 <code>requirements.txt</code> 的文件，仅控制所安装依赖项的<em>版本</em>。但是，在约束文件中包含某个包<em>不会</em>触发该包的安装。</p>
<p>这等同于 pip 的 <code>--constraint</code> 选项。</p>
<p>也可以通过 <code>UV_CONSTRAINT</code> 环境变量设置。</p></dd><dt id="uv-tool-install--default-index"><a href="#uv-tool-install--default-index"><code>--default-index</code></a> <i>default-index</i></dt><dd><p>默认包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或以相同格式组织的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--index</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_DEFAULT_INDEX</code> 环境变量设置。</p></dd><dt id="uv-tool-install--directory"><a href="#uv-tool-install--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到给定目录。</p>
<p>相对路径以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 以仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-tool-install--editable"><a href="#uv-tool-install--editable"><code>--editable</code></a>, <code>-e</code></dt><dd><p>以可编辑模式安装目标包，这样对包源码目录的更改无需重新安装即可反映</p>
</dd><dt id="uv-tool-install--exclude-newer"><a href="#uv-tool-install--exclude-newer"><code>--exclude-newer</code></a> <i>exclude-newer</i></dt><dd><p>将候选包限制为在给定日期之前上传的版本。</p>
<p>日期与每个分发包构件的上传时间（即每个文件上传到包索引的时间）进行比较，而非包版本的发布日期。</p>
<p>接受 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、基于系统配置时区解析的相同格式的本地日期（例如 <code>2006-12-02</code>）、"友好"持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不考虑本地时区的语义，始终解析为固定的秒数，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月份和年份等日历单位。</p>
<p>也可以通过 <code>UV_EXCLUDE_NEWER</code> 环境变量设置。</p></dd><dt id="uv-tool-install--exclude-newer-package"><a href="#uv-tool-install--exclude-newer-package"><code>--exclude-newer-package</code></a> <i>exclude-newer-package</i></dt><dd><p>将特定包的候选包限制为在给定日期之前上传的版本。</p>
<p>接受 <code>PACKAGE=DATE</code> 格式的包-日期对，其中 <code>DATE</code> 是 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、基于系统配置时区解析的相同格式的本地日期（例如 <code>2006-12-02</code>）、"友好"持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不考虑本地时区的语义，始终解析为固定的秒数，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月份和年份等日历单位。</p>
<p>可以为不同的包多次提供。</p>
</dd><dt id="uv-tool-install--excludes"><a href="#uv-tool-install--excludes"><code>--excludes</code></a>, <code>--exclude</code> <i>excludes</i></dt><dd><p>使用给定的 requirements 文件从解析中排除包。</p>
<p>排除文件是类似 <code>requirements.txt</code> 的文件，指定要从解析中排除的包。当包被排除时，它将完全从依赖项列表中省略，并且在解析阶段其自身的依赖项也将被忽略。排除是无条件的，需求说明符和标记将被忽略；提供的文件中列出的任何包都将从所有已解析的环境中省略。</p>
<p>也可以通过 <code>UV_EXCLUDE</code> 环境变量设置。</p></dd><dt id="uv-tool-install--extra-index-url"><a href="#uv-tool-install--extra-index-url"><code>--extra-index-url</code></a> <i>extra-index-url</i></dt><dd><p>（已弃用：请改用 <code>--index</code>）除 <code>--index-url</code> 之外，要使用的额外包索引 URL。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或以相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--index-url</code>（默认为 PyPI）指定的索引。当提供多个 <code>--extra-index-url</code> 标志时，较早的值优先。</p>
<p>也可以通过 <code>UV_EXTRA_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-tool-install--find-links"><a href="#uv-tool-install--find-links"><code>--find-links</code></a>, <code>-f</code> <i>find-links</i></dt><dd><p>除注册表索引中找到的分发包外，还要搜索候选分发包的位置。</p>
<p>如果是路径，目标必须是一个目录，其中包含顶层 wheel 文件（<code>.whl</code>）或源码分发包（例如 <code>.tar.gz</code> 或 <code>.zip</code>）。</p>
<p>如果是 URL，页面必须包含指向符合上述格式的包文件的扁平链接列表。</p>
<p>也可以通过 <code>UV_FIND_LINKS</code> 环境变量设置。</p></dd><dt id="uv-tool-install--force"><a href="#uv-tool-install--force"><code>--force</code></a></dt><dd><p>强制安装工具。</p>
<p>将重新创建工具的任何现有环境，并替换可执行文件目录中任何同名的现有入口点。</p>
</dd><dt id="uv-tool-install--fork-strategy"><a href="#uv-tool-install--fork-strategy"><code>--fork-strategy</code></a> <i>fork-strategy</i></dt><dd><p>在跨 Python 版本和平台为给定包选择多个版本时使用的策略。</p>
<p>默认情况下，uv 会优化为每个支持的 Python 版本（<code>requires-python</code>）选择每个包的最新版本，同时最小化跨平台选择的版本数量。</p>
<p>在 <code>fewest</code> 策略下，uv 将最小化每个包选择的版本数量，优先选择与更广泛支持的 Python 版本或平台兼容的旧版本。</p>
<p>也可以通过 <code>UV_FORK_STRATEGY</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>fewest</code>：优化为每个包选择最少数量的版本。如果旧版本与更广泛支持的 Python 版本或平台兼容，则可能优先选择旧版本</li>
<li><code>requires-python</code>：为每个支持的 Python 版本优化选择每个包的最新支持版本</li>
</ul></dd><dt id="uv-tool-install--help"><a href="#uv-tool-install--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简要帮助</p>
</dd><dt id="uv-tool-install--index"><a href="#uv-tool-install--index"><code>--index</code></a> <i>index</i></dt><dd><p>解析依赖项时使用的 URL，除默认索引之外。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或以相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--default-index</code>（默认为 PyPI）指定的索引。当提供多个 <code>--index</code> 标志时，较早的值优先。</p>
<p>不支持索引名称作为值。相对路径必须通过 <code>./</code> 或 <code>../</code>（Unix）或 <code>.\\</code>、<code>..\\</code>、<code>./</code> 或 <code>../</code>（Windows）与索引名称区分开来。</p>
<p>也可以通过 <code>UV_INDEX</code> 环境变量设置。</p></dd><dt id="uv-tool-install--index-strategy"><a href="#uv-tool-install--index-strategy"><code>--index-strategy</code></a> <i>index-strategy</i></dt><dd><p>针对多个索引 URL 进行解析时使用的策略。</p>
<p>默认情况下，uv 会在第一个找到给定包的索引处停止，并将解析限制为该第一个索引上存在的版本（<code>first-index</code>）。这可以防止"依赖混淆"攻击，即攻击者可以在备用索引上以相同名称上传恶意包。</p>
<p>也可以通过 <code>UV_INDEX_STRATEGY</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>first-index</code>：仅使用第一个返回给定包名匹配结果的索引</li>
<li><code>unsafe-first-match</code>：在所有索引中搜索每个包名，先穷尽第一个索引的版本，然后再转到下一个</li>
<li><code>unsafe-best-match</code>：在所有索引中搜索每个包名，优先选择找到的"最佳"版本。如果一个包版本存在于多个索引中，则只查看第一个索引的条目</li>
</ul></dd><dt id="uv-tool-install--index-url"><a href="#uv-tool-install--index-url"><code>--index-url</code></a>, <code>-i</code> <i>index-url</i></dt><dd><p>（已弃用：请改用 <code>--default-index</code>）Python 包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或以相同格式组织的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--extra-index-url</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-tool-install--keyring-provider"><a href="#uv-tool-install--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>尝试使用 <code>keyring</code> 进行索引 URL 的身份验证。</p>
<p>目前仅支持 <code>--keyring-provider subprocess</code>，它配置 uv 使用 <code>keyring</code> CLI 来处理身份验证。</p>
<p>默认为 <code>disabled</code>。</p>
<p>也可以通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>disabled</code>：不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>：使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-tool-install--link-mode"><a href="#uv-tool-install--link-mode"><code>--link-mode</code></a> <i>link-mode</i></dt><dd><p>从全局缓存安装包时使用的方法。</p>
<p>在 macOS 和 Linux 上默认为 <code>clone</code>（也称为写时复制），在 Windows 上默认为 <code>hardlink</code>。</p>
<p>警告：不鼓励使用 symlink 链接模式，因为它会在缓存和目标环境之间创建紧密耦合。例如，清除缓存（<code>uv cache clean</code>）将通过删除底层源文件来破坏所有已安装的包。请谨慎使用符号链接。</p>
<p>也可以通过 <code>UV_LINK_MODE</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>clone</code>：将包从源克隆（即写时复制）到目标</li>
<li><code>copy</code>：将包从源复制到目标</li>
<li><code>hardlink</code>：将包从源硬链接到目标</li>
<li><code>symlink</code>：将包从源符号链接到目标</li>
</ul></dd><dt id="uv-tool-install--managed-python"><a href="#uv-tool-install--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用它管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-tool-install--no-binary"><a href="#uv-tool-install--no-binary"><code>--no-binary</code></a></dt><dd><p>不安装预编译的 wheel。</p>
<p>给定的包将从源码构建和安装。解析器仍将使用预编译的 wheel 来提取包元数据（如果可用）。</p>
<p>也可以通过 <code>UV_NO_BINARY</code> 环境变量设置。</p></dd><dt id="uv-tool-install--no-binary-package"><a href="#uv-tool-install--no-binary-package"><code>--no-binary-package</code></a> <i>no-binary-package</i></dt><dd><p>不为特定包安装预编译的 wheel [env: <code>UV_NO_BINARY_PACKAGE</code>=]</p>
</dd><dt id="uv-tool-install--no-build"><a href="#uv-tool-install--no-build"><code>--no-build</code></a></dt><dd><p>不构建源码分发包。</p>
<p>启用后，解析将不会运行任意 Python 代码。已构建的源码分发包的缓存 wheel 将被重用，但需要构建分发包的操作将退出并报错。</p>
<p>也可以通过 <code>UV_NO_BUILD</code> 环境变量设置。</p></dd><dt id="uv-tool-install--no-build-isolation"><a href="#uv-tool-install--no-build-isolation"><code>--no-build-isolation</code></a></dt><dd><p>构建源码分发包时禁用隔离。</p>
<p>假定 PEP 518 指定的构建依赖项已安装。</p>
<p>也可以通过 <code>UV_NO_BUILD_ISOLATION</code> 环境变量设置。</p></dd><dt id="uv-tool-install--no-build-isolation-package"><a href="#uv-tool-install--no-build-isolation-package"><code>--no-build-isolation-package</code></a> <i>no-build-isolation-package</i></dt><dd><p>为特定包构建源码分发包时禁用隔离。</p>
<p>假定该包的 PEP 518 构建依赖项已安装。</p>
</dd><dt id="uv-tool-install--no-build-package"><a href="#uv-tool-install--no-build-package"><code>--no-build-package</code></a> <i>no-build-package</i></dt><dd><p>不为特定包构建源码分发包 [env: <code>UV_NO_BUILD_PACKAGE</code>=]</p>
</dd><dt id="uv-tool-install--no-cache"><a href="#uv-tool-install--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，在操作期间改用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-tool-install--no-config"><a href="#uv-tool-install--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>正常情况下，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-tool-install--no-index"><a href="#uv-tool-install--no-index"><code>--no-index</code></a></dt><dd><p>忽略注册表索引（例如 PyPI），转而依赖直接 URL 依赖项和通过 <code>--find-links</code> 提供的依赖项</p>
</dd><dt id="uv-tool-install--no-managed-python"><a href="#uv-tool-install--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-tool-install--no-progress"><a href="#uv-tool-install--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转指示器或进度条。</p>
</dd><dt id="uv-tool-install--no-python-downloads"><a href="#uv-tool-install--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-tool-install--no-sources"><a href="#uv-tool-install--no-sources"><code>--no-sources</code></a></dt><dd><p>解析依赖项时忽略 <code>tool.uv.sources</code> 表。用于根据符合标准、可发布的包元数据进行锁定，而不是使用任何工作区、Git、URL 或本地路径源</p>
<p>也可以通过 <code>UV_NO_SOURCES</code> 环境变量设置。</p></dd><dt id="uv-tool-install--no-sources-package"><a href="#uv-tool-install--no-sources-package"><code>--no-sources-package</code></a> <i>no-sources-package</i></dt><dd><p>不为指定包使用 <code>tool.uv.sources</code> 表中的源 [env: <code>UV_NO_SOURCES_PACKAGE</code>=]</p>
</dd><dt id="uv-tool-install--offline"><a href="#uv-tool-install--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-tool-install--overrides"><a href="#uv-tool-install--overrides"><code>--overrides</code></a>, <code>--override</code> <i>overrides</i></dt><dd><p>使用给定的 requirements 文件覆盖版本。</p>
<p>覆盖文件是类似 <code>requirements.txt</code> 的文件，强制安装特定版本的需求，无论任何组成包声明了什么需求，也无论这是否会被视为无效的解析。</p>
<p>约束是<em>附加性的</em>，即它们与组成包的需求相结合；而覆盖是<em>绝对性的</em>，即它们完全替换组成包的需求。</p>
<p>也可以通过 <code>UV_OVERRIDE</code> 环境变量设置。</p></dd><dt id="uv-tool-install--prerelease"><a href="#uv-tool-install--prerelease"><code>--prerelease</code></a> <i>prerelease</i></dt><dd><p>考虑预发布版本时使用的策略。</p>
<p>默认情况下，uv 将接受<em>仅</em>发布预发布版本的包的预发布版本，以及声明的版本说明符中包含显式预发布标记的第一方依赖项（<code>if-necessary-or-explicit</code>）。</p>
<p>也可以通过 <code>UV_PRERELEASE</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>disallow</code>：禁止所有预发布版本</li>
<li><code>allow</code>：允许所有预发布版本</li>
<li><code>if-necessary</code>：如果包的所有版本都是预发布版本，则允许预发布版本</li>
<li><code>explicit</code>：允许版本要求中包含显式预发布标记的第一方包的预发布版本</li>
<li><code>if-necessary-or-explicit</code>：如果包的所有版本都是预发布版本，或者包在其版本要求中有显式预发布标记，则允许预发布版本</li>
</ul></dd><dt id="uv-tool-install--project"><a href="#uv-tool-install--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-tool-install--python"><a href="#uv-tool-install--python"><code>--python</code></a>, <code>-p</code> <i>python</i></dt><dd><p>用于构建工具环境的 Python 解释器。</p>
<p>有关 Python 发现和支持的请求格式的详细信息，请参见 <a href="#uv-python">uv python</a>。</p>
<p>也可以通过 <code>UV_PYTHON</code> 环境变量设置。</p></dd><dt id="uv-tool-install--python-platform"><a href="#uv-tool-install--python-platform"><code>--python-platform</code></a> <i>python-platform</i></dt><dd><p>应为其安装依赖项的平台。</p>
<p>表示为"目标三元组"，一个描述目标平台的字符串，包含其 CPU、供应商和操作系统名称，如 <code>x86_64-unknown-linux-gnu</code> 或 <code>aarch64-apple-darwin</code>。</p>
<p>当目标为 macOS（Darwin）时，默认最低版本为 <code>13.0</code>。使用 <code>MACOSX_DEPLOYMENT_TARGET</code> 指定不同的最低版本，例如 <code>14.0</code>。</p>
<p>当目标为 iOS 时，默认最低版本为 <code>13.0</code>。使用 <code>IPHONEOS_DEPLOYMENT_TARGET</code> 指定不同的最低版本，例如 <code>14.0</code>。</p>
<p>当目标为 Android 时，默认最低 Android API 级别为 <code>24</code>。使用 <code>ANDROID_API_LEVEL</code> 指定不同的最低版本，例如 <code>26</code>。</p>
<p>警告：指定后，uv 将选择与<em>目标</em>平台兼容的 wheel；因此，已安装的分发包可能与<em>当前</em>平台不兼容。相反，从源码构建的任何分发包可能与<em>目标</em>平台不兼容，因为它们将针对<em>当前</em>平台构建。<code>--python-platform</code> 选项适用于高级用例。</p>
<p>可能的值：</p>
<ul>
<li><code>windows</code>：<code>x86_64-pc-windows-msvc</code> 的别名，Windows 的默认目标</li>
<li><code>linux</code>：<code>x86_64-unknown-linux-gnu</code> 的别名，Linux 的默认目标</li>
<li><code>macos</code>：<code>aarch64-apple-darwin</code> 的别名，macOS 的默认目标</li>
<li><code>x86_64-pc-windows-msvc</code>：64 位 x86 Windows 目标</li>
<li><code>aarch64-pc-windows-msvc</code>：ARM64 Windows 目标</li>
<li><code>i686-pc-windows-msvc</code>：32 位 x86 Windows 目标</li>
<li><code>x86_64-unknown-linux-gnu</code>：x86 Linux 目标。等同于 <code>x86_64-manylinux_2_28</code></li>
<li><code>aarch64-apple-darwin</code>：基于 ARM 的 macOS 目标，如 Apple Silicon 设备所示</li>
<li><code>x86_64-apple-darwin</code>：x86 macOS 目标</li>
<li><code>aarch64-unknown-linux-gnu</code>：ARM64 Linux 目标。等同于 <code>aarch64-manylinux_2_28</code></li>
<li><code>aarch64-unknown-linux-musl</code>：ARM64 Linux 目标</li>
<li><code>x86_64-unknown-linux-musl</code>：<code>x86_64</code> Linux 目标</li>
<li><code>riscv64-unknown-linux</code>：RISCV64 Linux 目标</li>
<li><code>x86_64-manylinux2014</code>：<code>manylinux2014</code> 平台的 <code>x86_64</code> 目标。等同于 <code>x86_64-manylinux_2_17</code></li>
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
<li><code>aarch64-manylinux2014</code>：<code>manylinux2014</code> 平台的 ARM64 目标。等同于 <code>aarch64-manylinux_2_17</code></li>
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
</ul></dd><dt id="uv-tool-install--quiet"><a href="#uv-tool-install--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，uv 将不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-tool-install--refresh"><a href="#uv-tool-install--refresh"><code>--refresh</code></a></dt><dd><p>刷新所有缓存数据</p>
</dd><dt id="uv-tool-install--refresh-package"><a href="#uv-tool-install--refresh-package"><code>--refresh-package</code></a> <i>refresh-package</i></dt><dd><p>刷新特定包的缓存数据</p>
</dd><dt id="uv-tool-install--reinstall"><a href="#uv-tool-install--reinstall"><code>--reinstall</code></a>, <code>--force-reinstall</code></dt><dd><p>重新安装所有包，无论它们是否已安装。隐含 <code>--refresh</code></p>
</dd><dt id="uv-tool-install--reinstall-package"><a href="#uv-tool-install--reinstall-package"><code>--reinstall-package</code></a> <i>reinstall-package</i></dt><dd><p>重新安装特定包，无论它是否已安装。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-tool-install--resolution"><a href="#uv-tool-install--resolution"><code>--resolution</code></a> <i>resolution</i></dt><dd><p>在给定包的不同兼容版本之间进行选择时使用的策略。</p>
<p>默认情况下，uv 将使用每个包的最新兼容版本（<code>highest</code>）。</p>
<p>也可以通过 <code>UV_RESOLUTION</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>highest</code>：解析每个包的最高兼容版本</li>
<li><code>lowest</code>：解析每个包的最低兼容版本</li>
<li><code>lowest-direct</code>：解析任何直接依赖项的最低兼容版本，以及任何传递依赖项的最高兼容版本</li>
</ul></dd><dt id="uv-tool-install--system-certs"><a href="#uv-tool-install--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能希望使用平台的原生证书存储，特别是当您依赖系统证书存储中包含的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-tool-install--torch-backend"><a href="#uv-tool-install--torch-backend"><code>--torch-backend</code></a> <i>torch-backend</i></dt><dd><p>获取 PyTorch 生态系统中的包时使用的后端（例如 <code>cpu</code>、<code>cu126</code> 或 <code>auto</code>）</p>
<p>设置后，uv 将忽略 PyTorch 生态系统中包的已配置索引 URL，转而使用定义的后端。</p>
<p>例如，当设置为 <code>cpu</code> 时，uv 将使用仅 CPU 的 PyTorch 索引；当设置为 <code>cu126</code> 时，uv 将使用 CUDA 12.6 的 PyTorch 索引。</p>
<p><code>auto</code> 模式将尝试根据当前安装的 CUDA 驱动程序检测适当的 PyTorch 索引。</p>
<p>此选项处于预览阶段，可能在任何未来版本中发生更改。</p>
<p>也可以通过 <code>UV_TORCH_BACKEND</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>auto</code>：根据操作系统和 CUDA 驱动程序版本选择适当的 PyTorch 索引</li>
<li><code>cpu</code>：使用仅 CPU 的 PyTorch 索引</li>
<li><code>cu130</code>：使用 CUDA 13.0 的 PyTorch 索引</li>
<li><code>cu129</code>：使用 CUDA 12.9 的 PyTorch 索引</li>
<li><code>cu128</code>：使用 CUDA 12.8 的 PyTorch 索引</li>
<li><code>cu126</code>：使用 CUDA 12.6 的 PyTorch 索引</li>
<li><code>cu125</code>：使用 CUDA 12.5 的 PyTorch 索引</li>
<li><code>cu124</code>：使用 CUDA 12.4 的 PyTorch 索引</li>
<li><code>cu123</code>：使用 CUDA 12.3 的 PyTorch 索引</li>
<li><code>cu122</code>：使用 CUDA 12.2 的 PyTorch 索引</li>
<li><code>cu121</code>：使用 CUDA 12.1 的 PyTorch 索引</li>
<li><code>cu120</code>：使用 CUDA 12.0 的 PyTorch 索引</li>
<li><code>cu118</code>：使用 CUDA 11.8 的 PyTorch 索引</li>
<li><code>cu117</code>：使用 CUDA 11.7 的 PyTorch 索引</li>
<li><code>cu116</code>：使用 CUDA 11.6 的 PyTorch 索引</li>
<li><code>cu115</code>：使用 CUDA 11.5 的 PyTorch 索引</li>
<li><code>cu114</code>：使用 CUDA 11.4 的 PyTorch 索引</li>
<li><code>cu113</code>：使用 CUDA 11.3 的 PyTorch 索引</li>
<li><code>cu112</code>：使用 CUDA 11.2 的 PyTorch 索引</li>
<li><code>cu111</code>：使用 CUDA 11.1 的 PyTorch 索引</li>
<li><code>cu110</code>：使用 CUDA 11.0 的 PyTorch 索引</li>
<li><code>cu102</code>：使用 CUDA 10.2 的 PyTorch 索引</li>
<li><code>cu101</code>：使用 CUDA 10.1 的 PyTorch 索引</li>
<li><code>cu100</code>：使用 CUDA 10.0 的 PyTorch 索引</li>
<li><code>cu92</code>：使用 CUDA 9.2 的 PyTorch 索引</li>
<li><code>cu91</code>：使用 CUDA 9.1 的 PyTorch 索引</li>
<li><code>cu90</code>：使用 CUDA 9.0 的 PyTorch 索引</li>
<li><code>cu80</code>：使用 CUDA 8.0 的 PyTorch 索引</li>
<li><code>rocm7.2</code>：使用 ROCm 7.2 的 PyTorch 索引</li>
<li><code>rocm7.1</code>：使用 ROCm 7.1 的 PyTorch 索引</li>
<li><code>rocm7.0</code>：使用 ROCm 7.0 的 PyTorch 索引</li>
<li><code>rocm6.4</code>：使用 ROCm 6.4 的 PyTorch 索引</li>
<li><code>rocm6.3</code>：使用 ROCm 6.3 的 PyTorch 索引</li>
<li><code>rocm6.2.4</code>：使用 ROCm 6.2.4 的 PyTorch 索引</li>
<li><code>rocm6.2</code>：使用 ROCm 6.2 的 PyTorch 索引</li>
<li><code>rocm6.1</code>：使用 ROCm 6.1 的 PyTorch 索引</li>
<li><code>rocm6.0</code>：使用 ROCm 6.0 的 PyTorch 索引</li>
<li><code>rocm5.7</code>：使用 ROCm 5.7 的 PyTorch 索引</li>
<li><code>rocm5.6</code>：使用 ROCm 5.6 的 PyTorch 索引</li>
<li><code>rocm5.5</code>：使用 ROCm 5.5 的 PyTorch 索引</li>
<li><code>rocm5.4.2</code>：使用 ROCm 5.4.2 的 PyTorch 索引</li>
<li><code>rocm5.4</code>：使用 ROCm 5.4 的 PyTorch 索引</li>
<li><code>rocm5.3</code>：使用 ROCm 5.3 的 PyTorch 索引</li>
<li><code>rocm5.2</code>：使用 ROCm 5.2 的 PyTorch 索引</li>
<li><code>rocm5.1.1</code>：使用 ROCm 5.1.1 的 PyTorch 索引</li>
<li><code>rocm4.2</code>：使用 ROCm 4.2 的 PyTorch 索引</li>
<li><code>rocm4.1</code>：使用 ROCm 4.1 的 PyTorch 索引</li>
<li><code>rocm4.0.1</code>：使用 ROCm 4.0.1 的 PyTorch 索引</li>
<li><code>xpu</code>：使用 Intel XPU 的 PyTorch 索引</li>
</ul></dd><dt id="uv-tool-install--upgrade"><a href="#uv-tool-install--upgrade"><code>--upgrade</code></a>, <code>-U</code></dt><dd><p>允许包升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh</code></p>
</dd><dt id="uv-tool-install--upgrade-group"><a href="#uv-tool-install--upgrade-group"><code>--upgrade-group</code></a> <i>upgrade-group</i></dt><dd><p>允许依赖组中所有包的升级，忽略任何现有输出文件中的固定版本</p>
</dd><dt id="uv-tool-install--upgrade-package"><a href="#uv-tool-install--upgrade-package"><code>--upgrade-package</code></a>, <code>-P</code> <i>upgrade-package</i></dt><dd><p>允许特定包的升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-tool-install--verbose"><a href="#uv-tool-install--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd><dt id="uv-tool-install--with"><a href="#uv-tool-install--with"><code>--with</code></a>, <code>-w</code> <i>with</i></dt><dd><p>包含以下额外的依赖项</p>
</dd><dt id="uv-tool-install--with-editable"><a href="#uv-tool-install--with-editable"><code>--with-editable</code></a> <i>with-editable</i></dt><dd><p>以可编辑模式包含给定的包</p>
</dd><dt id="uv-tool-install--with-executables-from"><a href="#uv-tool-install--with-executables-from"><code>--with-executables-from</code></a> <i>with-executables-from</i></dt><dd><p>从以下包安装可执行文件</p>
</dd><dt id="uv-tool-install--with-requirements"><a href="#uv-tool-install--with-requirements"><code>--with-requirements</code></a> <i>with-requirements</i></dt><dd><p>使用给定文件中列出的包运行。</p>
<p>支持以下格式：<code>requirements.txt</code>、带有内联元数据的 <code>.py</code> 文件和 <code>pylock.toml</code>。</p>
</dd></dl>

### uv tool upgrade

升级已安装的工具。

如果工具在安装时带有版本约束，升级时将遵守这些约束——要升级到超出最初提供约束的版本，请再次使用 `uv tool install`。

如果工具在安装时带有特定设置，升级时将遵守这些设置。例如，如果在安装期间提供了 `--prereleases allow`，升级时将继续遵守该设置。

<h3 class="cli-reference">用法</h3>

```
uv tool upgrade [OPTIONS] <NAME>...
```

<h3 class="cli-reference">参数</h3>

<dl class="cli-reference"><dt id="uv-tool-upgrade--name"><a href="#uv-tool-upgrade--name"><code>NAME</code></a></dt><dd><p>要升级的工具名称，可附带可选的版本说明符</p>
</dd></dl>

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-tool-upgrade--all"><a href="#uv-tool-upgrade--all"><code>--all</code></a></dt><dd><p>升级所有工具</p>
</dd><dt id="uv-tool-upgrade--allow-insecure-host"><a href="#uv-tool-upgrade--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许连接到不安全的主机。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统的证书存储进行验证。仅在具有已验证来源的安全网络中使用 <code>--allow-insecure-host</code>，因为它会绕过 SSL 验证，可能使您面临中间人攻击（MITM）的风险。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-tool-upgrade--cache-dir"><a href="#uv-tool-upgrade--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-tool-upgrade--color"><a href="#uv-tool-upgrade--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可能的值：</p>
<ul>
<li><code>auto</code>：仅当输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-tool-upgrade--compile-bytecode"><a href="#uv-tool-upgrade--compile-bytecode"><code>--compile-bytecode</code></a>, <code>--compile</code></dt><dd><p>安装后将 Python 文件编译为字节码。</p>
<p>默认情况下，uv 不会将 Python（<code>.py</code>）文件编译为字节码（<code>__pycache__/*.pyc</code>）；相反，编译会在首次导入模块时延迟执行。对于启动时间至关重要的用例（如 CLI 应用程序和 Docker 容器），可以启用此选项，以较长的安装时间换取更快的启动时间。</p>
<p>启用后，uv 将处理整个 site-packages 目录（包括当前操作未修改的包）以保持一致性。与 pip 类似，它也会忽略错误。</p>
<p>也可以通过 <code>UV_COMPILE_BYTECODE</code> 环境变量设置。</p></dd><dt id="uv-tool-upgrade--config-file"><a href="#uv-tool-upgrade--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许使用。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-tool-upgrade--config-setting"><a href="#uv-tool-upgrade--config-setting"><code>--config-setting</code></a>, <code>--config-settings</code>, <code>-C</code> <i>config-setting</i></dt><dd><p>传递给 PEP 517 构建后端的设置，以 <code>KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-tool-upgrade--config-setting-package"><a href="#uv-tool-upgrade--config-setting-package"><code>--config-setting-package</code></a>, <code>--config-settings-package</code> <i>config-setting-package</i></dt><dd><p>为特定包传递给 PEP 517 构建后端的设置，以 <code>PACKAGE:KEY=VALUE</code> 对的形式指定</p>
</dd><dt id="uv-tool-upgrade--default-index"><a href="#uv-tool-upgrade--default-index"><code>--default-index</code></a> <i>default-index</i></dt><dd><p>默认包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或以相同格式组织的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--index</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_DEFAULT_INDEX</code> 环境变量设置。</p></dd><dt id="uv-tool-upgrade--directory"><a href="#uv-tool-upgrade--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到给定目录。</p>
<p>相对路径以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 以仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-tool-upgrade--exclude-newer"><a href="#uv-tool-upgrade--exclude-newer"><code>--exclude-newer</code></a> <i>exclude-newer</i></dt><dd><p>将候选包限制为在给定日期之前上传的版本。</p>
<p>日期与每个分发包构件的上传时间（即每个文件上传到包索引的时间）进行比较，而非包版本的发布日期。</p>
<p>接受 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、基于系统配置时区解析的相同格式的本地日期（例如 <code>2006-12-02</code>）、"友好"持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不考虑本地时区的语义，始终解析为固定的秒数，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月份和年份等日历单位。</p>
<p>也可以通过 <code>UV_EXCLUDE_NEWER</code> 环境变量设置。</p></dd><dt id="uv-tool-upgrade--exclude-newer-package"><a href="#uv-tool-upgrade--exclude-newer-package"><code>--exclude-newer-package</code></a> <i>exclude-newer-package</i></dt><dd><p>将特定包的候选包限制为在给定日期之前上传的版本。</p>
<p>接受 <code>PACKAGE=DATE</code> 格式的包-日期对，其中 <code>DATE</code> 是 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、基于系统配置时区解析的相同格式的本地日期（例如 <code>2006-12-02</code>）、"友好"持续时间（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 持续时间（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>持续时间不考虑本地时区的语义，始终解析为固定的秒数，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月份和年份等日历单位。</p>
<p>可以为不同的包多次提供。</p>
</dd><dt id="uv-tool-upgrade--extra-index-url"><a href="#uv-tool-upgrade--extra-index-url"><code>--extra-index-url</code></a> <i>extra-index-url</i></dt><dd><p>（已弃用：请改用 <code>--index</code>）除 <code>--index-url</code> 之外，要使用的额外包索引 URL。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或以相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--index-url</code>（默认为 PyPI）指定的索引。当提供多个 <code>--extra-index-url</code> 标志时，较早的值优先。</p>
<p>也可以通过 <code>UV_EXTRA_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-tool-upgrade--find-links"><a href="#uv-tool-upgrade--find-links"><code>--find-links</code></a>, <code>-f</code> <i>find-links</i></dt><dd><p>除注册表索引中找到的分发包外，还要搜索候选分发包的位置。</p>
<p>如果是路径，目标必须是一个目录，其中包含顶层 wheel 文件（<code>.whl</code>）或源码分发包（例如 <code>.tar.gz</code> 或 <code>.zip</code>）。</p>
<p>如果是 URL，页面必须包含指向符合上述格式的包文件的扁平链接列表。</p>
<p>也可以通过 <code>UV_FIND_LINKS</code> 环境变量设置。</p></dd><dt id="uv-tool-upgrade--fork-strategy"><a href="#uv-tool-upgrade--fork-strategy"><code>--fork-strategy</code></a> <i>fork-strategy</i></dt><dd><p>在跨 Python 版本和平台为给定包选择多个版本时使用的策略。</p>
<p>默认情况下，uv 会优化为每个支持的 Python 版本（<code>requires-python</code>）选择每个包的最新版本，同时最小化跨平台选择的版本数量。</p>
<p>在 <code>fewest</code> 策略下，uv 将最小化每个包选择的版本数量，优先选择与更广泛支持的 Python 版本或平台兼容的旧版本。</p>
<p>也可以通过 <code>UV_FORK_STRATEGY</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>fewest</code>：优化为每个包选择最少数量的版本。如果旧版本与更广泛支持的 Python 版本或平台兼容，则可能优先选择旧版本</li>
<li><code>requires-python</code>：为每个支持的 Python 版本优化选择每个包的最新支持版本</li>
</ul></dd><dt id="uv-tool-upgrade--help"><a href="#uv-tool-upgrade--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简要帮助</p>
</dd><dt id="uv-tool-upgrade--index"><a href="#uv-tool-upgrade--index"><code>--index</code></a> <i>index</i></dt><dd><p>解析依赖项时使用的 URL，除默认索引之外。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或以相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引优先级高于 <code>--default-index</code>（默认为 PyPI）指定的索引。当提供多个 <code>--index</code> 标志时，较早的值优先。</p>
<p>不支持索引名称作为值。相对路径必须通过 <code>./</code> 或 <code>../</code>（Unix）或 <code>.\\</code>、<code>..\\</code>、<code>./</code> 或 <code>../</code>（Windows）与索引名称区分开来。</p>
<p>也可以通过 <code>UV_INDEX</code> 环境变量设置。</p></dd><dt id="uv-tool-upgrade--index-strategy"><a href="#uv-tool-upgrade--index-strategy"><code>--index-strategy</code></a> <i>index-strategy</i></dt><dd><p>针对多个索引 URL 进行解析时使用的策略。</p>
<p>默认情况下，uv 会在第一个找到给定包的索引处停止，并将解析限制为该第一个索引上存在的版本（<code>first-index</code>）。这可以防止"依赖混淆"攻击，即攻击者可以在备用索引上以相同名称上传恶意包。</p>
<p>也可以通过 <code>UV_INDEX_STRATEGY</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>first-index</code>：仅使用第一个返回给定包名匹配结果的索引</li>
<li><code>unsafe-first-match</code>：在所有索引中搜索每个包名，先穷尽第一个索引的版本，然后再转到下一个</li>
<li><code>unsafe-best-match</code>：在所有索引中搜索每个包名，优先选择找到的"最佳"版本。如果一个包版本存在于多个索引中，则只查看第一个索引的条目</li>
</ul></dd><dt id="uv-tool-upgrade--index-url"><a href="#uv-tool-upgrade--index-url"><code>--index-url</code></a>, <code>-i</code> <i>index-url</i></dt><dd><p>（已弃用：请改用 <code>--default-index</code>）Python 包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或以相同格式组织的本地目录。</p>
<p>此标志指定的索引优先级低于通过 <code>--extra-index-url</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-tool-upgrade--keyring-provider"><a href="#uv-tool-upgrade--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>尝试使用 <code>keyring</code> 进行索引 URL 的身份验证。</p>
<p>目前仅支持 <code>--keyring-provider subprocess</code>，它配置 uv 使用 <code>keyring</code> CLI 来处理身份验证。</p>
<p>默认为 <code>disabled</code>。</p>
<p>也可以通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>disabled</code>：不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>：使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-tool-upgrade--link-mode"><a href="#uv-tool-upgrade--link-mode"><code>--link-mode</code></a> <i>link-mode</i></dt><dd><p>从全局缓存安装包时使用的方法。</p>
<p>在 macOS 和 Linux 上默认为 <code>clone</code>（也称为写时复制），在 Windows 上默认为 <code>hardlink</code>。</p>
<p>警告：不鼓励使用 symlink 链接模式，因为它会在缓存和目标环境之间创建紧密耦合。例如，清除缓存（<code>uv cache clean</code>）将通过删除底层源文件来破坏所有已安装的包。请谨慎使用符号链接。</p>
<p>也可以通过 <code>UV_LINK_MODE</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>clone</code>：将包从源克隆（即写时复制）到目标</li>
<li><code>copy</code>：将包从源复制到目标</li>
<li><code>hardlink</code>：将包从源硬链接到目标</li>
<li><code>symlink</code>：将包从源符号链接到目标</li>
</ul></dd><dt id="uv-tool-upgrade--managed-python"><a href="#uv-tool-upgrade--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用它管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-tool-upgrade--no-binary"><a href="#uv-tool-upgrade--no-binary"><code>--no-binary</code></a></dt><dd><p>不安装预编译的 wheel。</p>
<p>给定的包将从源码构建和安装。解析器仍将使用预编译的 wheel 来提取包元数据（如果可用）。</p>
<p>也可以通过 <code>UV_NO_BINARY</code> 环境变量设置。</p></dd><dt id="uv-tool-upgrade--no-binary-package"><a href="#uv-tool-upgrade--no-binary-package"><code>--no-binary-package</code></a> <i>no-binary-package</i></dt><dd><p>不为特定包安装预编译的 wheel [env: <code>UV_NO_BINARY_PACKAGE</code>=]</p>
</dd><dt id="uv-tool-upgrade--no-build"><a href="#uv-tool-upgrade--no-build"><code>--no-build</code></a></dt><dd><p>不构建源码分发包。</p>
<p>启用后，解析将不会运行任意 Python 代码。已构建的源码分发包的缓存 wheel 将被重用，但需要构建分发包的操作将退出并报错。</p>
<p>也可以通过 <code>UV_NO_BUILD</code> 环境变量设置。</p></dd><dt id="uv-tool-upgrade--no-build-isolation"><a href="#uv-tool-upgrade--no-build-isolation"><code>--no-build-isolation</code></a></dt><dd><p>构建源码分发包时禁用隔离。</p>
<p>假定 PEP 518 指定的构建依赖项已安装。</p>
<p>也可以通过 <code>UV_NO_BUILD_ISOLATION</code> 环境变量设置。</p></dd><dt id="uv-tool-upgrade--no-build-isolation-package"><a href="#uv-tool-upgrade--no-build-isolation-package"><code>--no-build-isolation-package</code></a> <i>no-build-isolation-package</i></dt><dd><p>为特定包构建源码分发包时禁用隔离。</p>
<p>假定该包的 PEP 518 构建依赖项已安装。</p>
</dd><dt id="uv-tool-upgrade--no-build-package"><a href="#uv-tool-upgrade--no-build-package"><code>--no-build-package</code></a> <i>no-build-package</i></dt><dd><p>不为特定包构建源码分发包 [env: <code>UV_NO_BUILD_PACKAGE</code>=]</p>
</dd><dt id="uv-tool-upgrade--no-cache"><a href="#uv-tool-upgrade--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，在操作期间改用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-tool-upgrade--no-config"><a href="#uv-tool-upgrade--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>正常情况下，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-tool-upgrade--no-index"><a href="#uv-tool-upgrade--no-index"><code>--no-index</code></a></dt><dd><p>忽略注册表索引（例如 PyPI），转而依赖直接 URL 依赖项和通过 <code>--find-links</code> 提供的依赖项</p>
</dd><dt id="uv-tool-upgrade--no-managed-python"><a href="#uv-tool-upgrade--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-tool-upgrade--no-progress"><a href="#uv-tool-upgrade--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转指示器或进度条。</p>
</dd><dt id="uv-tool-upgrade--no-python-downloads"><a href="#uv-tool-upgrade--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-tool-upgrade--no-sources"><a href="#uv-tool-upgrade--no-sources"><code>--no-sources</code></a></dt><dd><p>解析依赖项时忽略 <code>tool.uv.sources</code> 表。用于根据符合标准、可发布的包元数据进行锁定，而不是使用任何工作区、Git、URL 或本地路径源</p>
<p>也可以通过 <code>UV_NO_SOURCES</code> 环境变量设置。</p></dd><dt id="uv-tool-upgrade--no-sources-package"><a href="#uv-tool-upgrade--no-sources-package"><code>--no-sources-package</code></a> <i>no-sources-package</i></dt><dd><p>不为指定包使用 <code>tool.uv.sources</code> 表中的源 [env: <code>UV_NO_SOURCES_PACKAGE</code>=]</p>
</dd><dt id="uv-tool-upgrade--offline"><a href="#uv-tool-upgrade--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-tool-upgrade--prerelease"><a href="#uv-tool-upgrade--prerelease"><code>--prerelease</code></a> <i>prerelease</i></dt><dd><p>考虑预发布版本时使用的策略。</p>
<p>默认情况下，uv 将接受<em>仅</em>发布预发布版本的包的预发布版本，以及声明的版本说明符中包含显式预发布标记的第一方依赖项（<code>if-necessary-or-explicit</code>）。</p>
<p>也可以通过 <code>UV_PRERELEASE</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>disallow</code>：禁止所有预发布版本</li>
<li><code>allow</code>：允许所有预发布版本</li>
<li><code>if-necessary</code>：如果包的所有版本都是预发布版本，则允许预发布版本</li>
<li><code>explicit</code>：允许版本要求中包含显式预发布标记的第一方包的预发布版本</li>
<li><code>if-necessary-or-explicit</code>：如果包的所有版本都是预发布版本，或者包在其版本要求中有显式预发布标记，则允许预发布版本</li>
</ul></dd><dt id="uv-tool-upgrade--python"><a href="#uv-tool-upgrade--python"><code>--python</code></a>, <code>-p</code> <i>python</i></dt><dd><p>用于构建工具环境的 Python 解释器。</p>
<p>有关 Python 发现和支持的请求格式的详细信息，请参见 <a href="#uv-python">uv python</a>。</p>
<p>也可以通过 <code>UV_PYTHON</code> 环境变量设置。</p></dd><dt id="uv-tool-upgrade--python-platform"><a href="#uv-tool-upgrade--python-platform"><code>--python-platform</code></a> <i>python-platform</i></dt><dd><p>应为其安装依赖项的平台。</p>
<p>表示为"目标三元组"，一个描述目标平台的字符串，包含其 CPU、供应商和操作系统名称，如 <code>x86_64-unknown-linux-gnu</code> 或 <code>aarch64-apple-darwin</code>。</p>
<p>当目标为 macOS（Darwin）时，默认最低版本为 <code>13.0</code>。使用 <code>MACOSX_DEPLOYMENT_TARGET</code> 指定不同的最低版本，例如 <code>14.0</code>。</p>
<p>当目标为 iOS 时，默认最低版本为 <code>13.0</code>。使用 <code>IPHONEOS_DEPLOYMENT_TARGET</code> 指定不同的最低版本，例如 <code>14.0</code>。</p>
<p>当目标为 Android 时，默认最低 Android API 级别为 <code>24</code>。使用 <code>ANDROID_API_LEVEL</code> 指定不同的最低版本，例如 <code>26</code>。</p>
<p>警告：指定后，uv 将选择与<em>目标</em>平台兼容的 wheel；因此，已安装的分发包可能与<em>当前</em>平台不兼容。相反，从源码构建的任何分发包可能与<em>目标</em>平台不兼容，因为它们将针对<em>当前</em>平台构建。<code>--python-platform</code> 选项适用于高级用例。</p>
<p>可能的值：</p>
<ul>
<li><code>windows</code>：<code>x86_64-pc-windows-msvc</code> 的别名，Windows 的默认目标</li>
<li><code>linux</code>：<code>x86_64-unknown-linux-gnu</code> 的别名，Linux 的默认目标</li>
<li><code>macos</code>：<code>aarch64-apple-darwin</code> 的别名，macOS 的默认目标</li>
<li><code>x86_64-pc-windows-msvc</code>：64 位 x86 Windows 目标</li>
<li><code>aarch64-pc-windows-msvc</code>：ARM64 Windows 目标</li>
<li><code>i686-pc-windows-msvc</code>：32 位 x86 Windows 目标</li>
<li><code>x86_64-unknown-linux-gnu</code>：x86 Linux 目标。等同于 <code>x86_64-manylinux_2_28</code></li>
<li><code>aarch64-apple-darwin</code>：基于 ARM 的 macOS 目标，如 Apple Silicon 设备所示</li>
<li><code>x86_64-apple-darwin</code>：x86 macOS 目标</li>
<li><code>aarch64-unknown-linux-gnu</code>：ARM64 Linux 目标。等同于 <code>aarch64-manylinux_2_28</code></li>
<li><code>aarch64-unknown-linux-musl</code>：ARM64 Linux 目标</li>
<li><code>x86_64-unknown-linux-musl</code>：<code>x86_64</code> Linux 目标</li>
<li><code>riscv64-unknown-linux</code>：RISCV64 Linux 目标</li>
<li><code>x86_64-manylinux2014</code>：<code>manylinux2014</code> 平台的 <code>x86_64</code> 目标。等同于 <code>x86_64-manylinux_2_17</code></li>
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
<li><code>aarch64-manylinux2014</code>：<code>manylinux2014</code> 平台的 ARM64 目标。等同于 <code>aarch64-manylinux_2_17</code></li>
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
</ul></dd><dt id="uv-tool-upgrade--quiet"><a href="#uv-tool-upgrade--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，uv 将不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-tool-upgrade--refresh"><a href="#uv-tool-upgrade--refresh"><code>--refresh</code></a></dt><dd><p>刷新所有缓存数据</p>
</dd><dt id="uv-tool-upgrade--refresh-package"><a href="#uv-tool-upgrade--refresh-package"><code>--refresh-package</code></a> <i>refresh-package</i></dt><dd><p>刷新特定包的缓存数据</p>
</dd><dt id="uv-tool-upgrade--reinstall"><a href="#uv-tool-upgrade--reinstall"><code>--reinstall</code></a>, <code>--force-reinstall</code></dt><dd><p>重新安装所有包，无论它们是否已安装。隐含 <code>--refresh</code></p>
</dd><dt id="uv-tool-upgrade--reinstall-package"><a href="#uv-tool-upgrade--reinstall-package"><code>--reinstall-package</code></a> <i>reinstall-package</i></dt><dd><p>重新安装特定包，无论它是否已安装。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-tool-upgrade--resolution"><a href="#uv-tool-upgrade--resolution"><code>--resolution</code></a> <i>resolution</i></dt><dd><p>在给定包的不同兼容版本之间进行选择时使用的策略。</p>
<p>默认情况下，uv 将使用每个包的最新兼容版本（<code>highest</code>）。</p>
<p>也可以通过 <code>UV_RESOLUTION</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>highest</code>：解析每个包的最高兼容版本</li>
<li><code>lowest</code>：解析每个包的最低兼容版本</li>
<li><code>lowest-direct</code>：解析任何直接依赖项的最低兼容版本，以及任何传递依赖项的最高兼容版本</li>
</ul></dd><dt id="uv-tool-upgrade--system-certs"><a href="#uv-tool-upgrade--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能希望使用平台的原生证书存储，特别是当您依赖系统证书存储中包含的企业信任根（例如，用于强制代理）时。</p>
</dd><dt id="uv-tool-upgrade--torch-backend"><a href="#uv-tool-upgrade--torch-backend"><code>--torch-backend</code></a> <i>torch-backend</i></dt><dd><p>获取 PyTorch 生态系统中的包时使用的后端（例如 <code>cpu</code>、<code>cu126</code> 或 <code>auto</code>）</p>
<p>设置后，uv 将忽略 PyTorch 生态系统中包的已配置索引 URL，转而使用定义的后端。</p>
<p>例如，当设置为 <code>cpu</code> 时，uv 将使用仅 CPU 的 PyTorch 索引；当设置为 <code>cu126</code> 时，uv 将使用 CUDA 12.6 的 PyTorch 索引。</p>
<p><code>auto</code> 模式将尝试根据当前安装的 CUDA 驱动程序检测适当的 PyTorch 索引。</p>
<p>此选项处于预览阶段，可能在任何未来版本中发生更改。</p>
<p>也可以通过 <code>UV_TORCH_BACKEND</code> 环境变量设置。</p><p>可能的值：</p>
<ul>
<li><code>auto</code>：根据操作系统和 CUDA 驱动程序版本选择适当的 PyTorch 索引</li>
<li><code>cpu</code>：使用仅 CPU 的 PyTorch 索引</li>
<li><code>cu130</code>：使用 CUDA 13.0 的 PyTorch 索引</li>
<li><code>cu129</code>：使用 CUDA 12.9 的 PyTorch 索引</li>
<li><code>cu128</code>：使用 CUDA 12.8 的 PyTorch 索引</li>
<li><code>cu126</code>：使用 CUDA 12.6 的 PyTorch 索引</li>
<li><code>cu125</code>：使用 CUDA 12.5 的 PyTorch 索引</li>
<li><code>cu124</code>：使用 CUDA 12.4 的 PyTorch 索引</li>
<li><code>cu123</code>：使用 CUDA 12.3 的 PyTorch 索引</li>
<li><code>cu122</code>：使用 CUDA 12.2 的 PyTorch 索引</li>
<li><code>cu121</code>：使用 CUDA 12.1 的 PyTorch 索引</li>
<li><code>cu120</code>：使用 CUDA 12.0 的 PyTorch 索引</li>
<li><code>cu118</code>：使用 CUDA 11.8 的 PyTorch 索引</li>
<li><code>cu117</code>：使用 CUDA 11.7 的 PyTorch 索引</li>
<li><code>cu116</code>：使用 CUDA 11.6 的 PyTorch 索引</li>
<li><code>cu115</code>：使用 CUDA 11.5 的 PyTorch 索引</li>
<li><code>cu114</code>：使用 CUDA 11.4 的 PyTorch 索引</li>
<li><code>cu113</code>：使用 CUDA 11.3 的 PyTorch 索引</li>
<li><code>cu112</code>：使用 CUDA 11.2 的 PyTorch 索引</li>
<li><code>cu111</code>：使用 CUDA 11.1 的 PyTorch 索引</li>
<li><code>cu110</code>：使用 CUDA 11.0 的 PyTorch 索引</li>
<li><code>cu102</code>：使用 CUDA 10.2 的 PyTorch 索引</li>
<li><code>cu101</code>：使用 CUDA 10.1 的 PyTorch 索引</li>
<li><code>cu100</code>：使用 CUDA 10.0 的 PyTorch 索引</li>
<li><code>cu92</code>：使用 CUDA 9.2 的 PyTorch 索引</li>
<li><code>cu91</code>：使用 CUDA 9.1 的 PyTorch 索引</li>
<li><code>cu90</code>：使用 CUDA 9.0 的 PyTorch 索引</li>
<li><code>cu80</code>：使用 CUDA 8.0 的 PyTorch 索引</li>
<li><code>rocm7.2</code>：使用 ROCm 7.2 的 PyTorch 索引</li>
<li><code>rocm7.1</code>：使用 ROCm 7.1 的 PyTorch 索引</li>
<li><code>rocm7.0</code>：使用 ROCm 7.0 的 PyTorch 索引</li>
<li><code>rocm6.4</code>：使用 ROCm 6.4 的 PyTorch 索引</li>
<li><code>rocm6.3</code>：使用 ROCm 6.3 的 PyTorch 索引</li>
<li><code>rocm6.2.4</code>：使用 ROCm 6.2.4 的 PyTorch 索引</li>
<li><code>rocm6.2</code>：使用 ROCm 6.2 的 PyTorch 索引</li>
<li><code>rocm6.1</code>：使用 ROCm 6.1 的 PyTorch 索引</li>
<li><code>rocm6.0</code>：使用 ROCm 6.0 的 PyTorch 索引</li>
<li><code>rocm5.7</code>：使用 ROCm 5.7 的 PyTorch 索引</li>
<li><code>rocm5.6</code>：使用 ROCm 5.6 的 PyTorch 索引</li>
<li><code>rocm5.5</code>：使用 ROCm 5.5 的 PyTorch 索引</li>
<li><code>rocm5.4.2</code>：使用 ROCm 5.4.2 的 PyTorch 索引</li>
<li><code>rocm5.4</code>：使用 ROCm 5.4 的 PyTorch 索引</li>
<li><code>rocm5.3</code>：使用 ROCm 5.3 的 PyTorch 索引</li>
<li><code>rocm5.2</code>：使用 ROCm 5.2 的 PyTorch 索引</li>
<li><code>rocm5.1.1</code>：使用 ROCm 5.1.1 的 PyTorch 索引</li>
<li><code>rocm4.2</code>：使用 ROCm 4.2 的 PyTorch 索引</li>
<li><code>rocm4.1</code>：使用 ROCm 4.1 的 PyTorch 索引</li>
<li><code>rocm4.0.1</code>：使用 ROCm 4.0.1 的 PyTorch 索引</li>
<li><code>xpu</code>：使用 Intel XPU 的 PyTorch 索引</li>
</ul></dd><dt id="uv-tool-upgrade--upgrade"><a href="#uv-tool-upgrade--upgrade"><code>--upgrade</code></a>, <code>-U</code></dt><dd><p>允许包升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh</code></p>
</dd><dt id="uv-tool-upgrade--upgrade-group"><a href="#uv-tool-upgrade--upgrade-group"><code>--upgrade-group</code></a> <i>upgrade-group</i></dt><dd><p>允许依赖组中所有包的升级，忽略任何现有输出文件中的固定版本</p>
</dd><dt id="uv-tool-upgrade--upgrade-package"><a href="#uv-tool-upgrade--upgrade-package"><code>--upgrade-package</code></a>, <code>-P</code> <i>upgrade-package</i></dt><dd><p>允许特定包的升级，忽略任何现有输出文件中的固定版本。隐含 <code>--refresh-package</code></p>
</dd><dt id="uv-tool-upgrade--verbose"><a href="#uv-tool-upgrade--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>

### uv tool list

列出已安装的工具。

<h3 class="cli-reference">用法</h3>

```
uv tool list [OPTIONS]
```

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-tool-list--cache-dir"><a href="#uv-tool-list--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-tool-list--color"><a href="#uv-tool-list--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可能的值：</p>
<ul>
<li><code>auto</code>：仅当输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-tool-list--config-file"><a href="#uv-tool-list--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许使用。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-tool-list--directory"><a href="#uv-tool-list--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到给定目录。</p>
<p>相对路径以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 以仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-tool-list--help"><a href="#uv-tool-list--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简要帮助</p>
</dd><dt id="uv-tool-list--no-config"><a href="#uv-tool-list--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>正常情况下，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-tool-list--no-progress"><a href="#uv-tool-list--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转指示器或进度条。</p>
</dd><dt id="uv-tool-list--quiet"><a href="#uv-tool-list--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，uv 将不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-tool-list--show-paths"><a href="#uv-tool-list--show-paths"><code>--show-paths</code></a></dt><dd><p>显示每个工具的安装路径</p>
</dd><dt id="uv-tool-list--show-version-specifiers"><a href="#uv-tool-list--show-version-specifiers"><code>--show-version-specifiers</code></a></dt><dd><p>显示每个工具最初安装时使用的版本说明符</p>
</dd><dt id="uv-tool-list--verbose"><a href="#uv-tool-list--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>

### uv tool uninstall

卸载已安装的工具。

<h3 class="cli-reference">用法</h3>

```
uv tool uninstall [OPTIONS] <NAME>...
```

<h3 class="cli-reference">参数</h3>

<dl class="cli-reference"><dt id="uv-tool-uninstall--name"><a href="#uv-tool-uninstall--name"><code>NAME</code></a></dt><dd><p>要卸载的工具名称</p>
</dd></dl>

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-tool-uninstall--all"><a href="#uv-tool-uninstall--all"><code>--all</code></a></dt><dd><p>卸载所有工具</p>
</dd><dt id="uv-tool-uninstall--cache-dir"><a href="#uv-tool-uninstall--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-tool-uninstall--color"><a href="#uv-tool-uninstall--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可能的值：</p>
<ul>
<li><code>auto</code>：仅当输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-tool-uninstall--config-file"><a href="#uv-tool-uninstall--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许使用。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-tool-uninstall--directory"><a href="#uv-tool-uninstall--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到给定目录。</p>
<p>相对路径以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 以仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-tool-uninstall--help"><a href="#uv-tool-uninstall--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简要帮助</p>
</dd><dt id="uv-tool-uninstall--no-config"><a href="#uv-tool-uninstall--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>正常情况下，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-tool-uninstall--no-progress"><a href="#uv-tool-uninstall--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转指示器或进度条。</p>
</dd><dt id="uv-tool-uninstall--quiet"><a href="#uv-tool-uninstall--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，uv 将不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-tool-uninstall--verbose"><a href="#uv-tool-uninstall--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>

### uv tool update-shell

确保 `uv tool` 目录在 PATH 上。如果目录不在 PATH 上，则尝试将其添加到相关的 shell 配置中。

强烈建议在安装工具后运行此命令。

不能保证 uv 对 shell 配置文件的修改总能成功，或者安全地应用。如果标准 shell 配置已有其他管理系统，或在 `uv tool update-shell` 失败的边缘情况下，shell 配置可能会损坏。使用 `uv tool update-shell` 需自行承担风险。关于 shell 配置，请查阅文档或 shell 手册。

<h3 class="cli-reference">用法</h3>

```
uv tool update-shell [OPTIONS]
```

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-tool-update-shell--cache-dir"><a href="#uv-tool-update-shell--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-tool-update-shell--color"><a href="#uv-tool-update-shell--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可能的值：</p>
<ul>
<li><code>auto</code>：仅当输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-tool-update-shell--config-file"><a href="#uv-tool-update-shell--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许使用。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-tool-update-shell--directory"><a href="#uv-tool-update-shell--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到给定目录。</p>
<p>相对路径以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 以仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-tool-update-shell--help"><a href="#uv-tool-update-shell--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简要帮助</p>
</dd><dt id="uv-tool-update-shell--no-config"><a href="#uv-tool-update-shell--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>正常情况下，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-tool-update-shell--no-progress"><a href="#uv-tool-update-shell--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转指示器或进度条。</p>
</dd><dt id="uv-tool-update-shell--quiet"><a href="#uv-tool-update-shell--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，uv 将不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-tool-update-shell--verbose"><a href="#uv-tool-update-shell--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>

### uv tool dir

显示 uv 工具目录的路径。

如果目录不存在，将创建它。

<h3 class="cli-reference">用法</h3>

```
uv tool dir [OPTIONS]
```

<h3 class="cli-reference">选项</h3>

<dl class="cli-reference"><dt id="uv-tool-dir--bin"><a href="#uv-tool-dir--bin"><code>--bin</code></a></dt><dd><p>显示工具可执行文件安装的目录，而不是工具虚拟环境目录</p>
</dd><dt id="uv-tool-dir--cache-dir"><a href="#uv-tool-dir--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-tool-dir--color"><a href="#uv-tool-dir--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可能的值：</p>
<ul>
<li><code>auto</code>：仅当输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-tool-dir--config-file"><a href="#uv-tool-dir--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许使用。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-tool-dir--directory"><a href="#uv-tool-dir--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到给定目录。</p>
<p>相对路径以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 以仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-tool-dir--help"><a href="#uv-tool-dir--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简要帮助</p>
</dd><dt id="uv-tool-dir--no-config"><a href="#uv-tool-dir--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>正常情况下，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-tool-dir--no-progress"><a href="#uv-tool-dir--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转指示器或进度条。</p>
</dd><dt id="uv-tool-dir--quiet"><a href="#uv-tool-dir--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，uv 将不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-tool-dir--verbose"><a href="#uv-tool-dir--verbose"><code>--verbose</code></a>, <code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>
