---
title: uv venv
description: uv venv 命令的完整中文参考文档，涵盖虚拟环境创建的所有 CLI 选项，包括 Python 解释器选择、索引配置、缓存管理、链接模式、可重定位环境等 30 余个参数的详细说明。
---

# uv venv

创建一个虚拟环境。

默认情况下，会在工作目录中创建一个名为 `.venv` 的虚拟环境。也可以通过位置参数提供替代路径。

如果在项目中，可以通过 `UV_PROJECT_ENVIRONMENT` 环境变量更改默认环境名称；此设置仅在从项目根目录运行时生效。

如果目标路径已存在虚拟环境，它将被删除，然后创建一个新的空虚拟环境。

使用 uv 时，无需手动激活虚拟环境。uv 会在工作目录或其任意父目录中查找虚拟环境（名为 `.venv`）。

<h3 class="cli-reference">用法（Usage）</h3>

```
uv venv [OPTIONS] [PATH]
```

<h3 class="cli-reference">参数（Arguments）</h3>

<dl class="cli-reference"><dt id="uv-venv--path"><a href="#uv-venv--path"><code>PATH</code></a></dt><dd><p>要创建的虚拟环境的路径。</p>
<p>默认为工作目录中的 <code>.venv</code>。</p>
<p>相对路径将相对于工作目录进行解析。</p>
</dd></dl>

<h3 class="cli-reference">选项（Options）</h3>

<dl class="cli-reference"><dt id="uv-venv--allow-existing"><a href="#uv-venv--allow-existing"><code>--allow-existing</code></a></dt><dd><p>保留目标路径中已存在的任何文件或目录。</p>
<p>默认情况下，如果给定路径非空，<code>uv venv</code> 将报错退出。<code>--allow-existing</code> 选项则会直接写入给定路径，无论其内容如何，且不会事先清空。</p>
<p>警告：如果现有虚拟环境与新创建的虚拟环境链接到不同的 Python 解释器，此选项可能导致意外行为。</p>
</dd><dt id="uv-venv--allow-insecure-host"><a href="#uv-venv--allow-insecure-host"><code>--allow-insecure-host</code></a>, <code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机的非安全连接。</p>
<p>可以多次指定。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机-端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会根据系统证书存储进行验证。仅在安全网络中使用 <code>--allow-insecure-host</code> 并确保来源已验证，因为它绕过了 SSL 验证，可能使您面临中间人攻击（MITM）的风险。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-venv--cache-dir"><a href="#uv-venv--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上默认为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-venv--clear"><a href="#uv-venv--clear"><code>--clear</code></a>, <code>-c</code></dt><dd><p>删除目标路径中已存在的任何文件或目录 [env: UV_VENV_CLEAR=]</p>
<p>默认情况下，如果给定路径非空，<code>uv venv</code> 将报错退出。<code>--clear</code> 选项则会在创建新虚拟环境之前清空非空路径。</p>
</dd><dt id="uv-venv--color"><a href="#uv-venv--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>：仅当输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-venv--config-file"><a href="#uv-venv--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许这样做。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-venv--default-index"><a href="#uv-venv--default-index"><code>--default-index</code></a> <i>default-index</i></dt><dd><p>默认包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志指定的索引的优先级低于通过 <code>--index</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_DEFAULT_INDEX</code> 环境变量设置。</p></dd><dt id="uv-venv--directory"><a href="#uv-venv--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到给定目录。</p>
<p>相对路径以给定目录为基准进行解析。</p>
<p>参见 <code>--project</code> 以仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-venv--exclude-newer"><a href="#uv-venv--exclude-newer"><code>--exclude-newer</code></a> <i>exclude-newer</i></dt><dd><p>将候选包限制为在给定日期之前上传的版本。</p>
<p>日期与每个单独分发构件（即每个文件上传到包索引的时间）的上传时间进行比较，而非包版本的发布日期。</p>
<p>接受 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、相同格式的本地日期（例如 <code>2006-12-02</code>，基于系统配置的时区解析）、"友好"时长（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 时长（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>时长不遵循本地时区的语义，始终按固定秒数解析，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月和年等日历单位。</p>
<p>也可以通过 <code>UV_EXCLUDE_NEWER</code> 环境变量设置。</p></dd><dt id="uv-venv--exclude-newer-package"><a href="#uv-venv--exclude-newer-package"><code>--exclude-newer-package</code></a> <i>exclude-newer-package</i></dt><dd><p>将特定包的候选版本限制为在给定日期之前上传的版本。</p>
<p>接受 <code>PACKAGE=DATE</code> 格式的包-日期对，其中 <code>DATE</code> 是 RFC 3339 时间戳（例如 <code>2006-12-02T02:07:43Z</code>）、相同格式的本地日期（例如 <code>2006-12-02</code>，基于系统配置的时区解析）、"友好"时长（例如 <code>24 hours</code>、<code>1 week</code>、<code>30 days</code>）或 ISO 8601 时长（例如 <code>PT24H</code>、<code>P7D</code>、<code>P30D</code>）。</p>
<p>时长不遵循本地时区的语义，始终按固定秒数解析，假设一天为 24 小时（例如，忽略夏令时转换）。不允许使用月和年等日历单位。</p>
<p>可以为不同的包多次指定。</p>
</dd><dt id="uv-venv--extra-index-url"><a href="#uv-venv--extra-index-url"><code>--extra-index-url</code></a> <i>extra-index-url</i></dt><dd><p>（已弃用：请改用 <code>--index</code>）除 <code>--index-url</code> 之外要使用的额外包索引 URL。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引的优先级高于 <code>--index-url</code> 指定的索引（默认为 PyPI）。当提供多个 <code>--extra-index-url</code> 标志时，先指定的值优先级更高。</p>
<p>也可以通过 <code>UV_EXTRA_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-venv--find-links"><a href="#uv-venv--find-links"><code>--find-links</code></a>, <code>-f</code> <i>find-links</i></dt><dd><p>除注册表索引中的内容外，用于搜索候选分发包的位置。</p>
<p>如果是路径，目标必须是一个目录，其中顶层包含作为 wheel 文件（<code>.whl</code>）或源码分发包（例如 <code>.tar.gz</code> 或 <code>.zip</code>）的包。</p>
<p>如果是 URL，页面必须包含指向符合上述格式的包文件的扁平链接列表。</p>
<p>也可以通过 <code>UV_FIND_LINKS</code> 环境变量设置。</p></dd><dt id="uv-venv--force"><a href="#uv-venv--force"><code>--force</code></a></dt><dd><p>允许 <code>--clear</code> 删除非虚拟环境目录。</p>
<p>这将删除目标路径中的所有文件和目录。</p>
</dd><dt id="uv-venv--help"><a href="#uv-venv--help"><code>--help</code></a>, <code>-h</code></dt><dd><p>显示此命令的简明帮助信息</p>
</dd><dt id="uv-venv--index"><a href="#uv-venv--index"><code>--index</code></a> <i>index</i></dt><dd><p>解析依赖时使用的 URL，作为默认索引的补充。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志提供的所有索引的优先级高于 <code>--default-index</code> 指定的索引（默认为 PyPI）。当提供多个 <code>--index</code> 标志时，先指定的值优先级更高。</p>
<p>不支持将索引名称作为值。相对路径必须使用 <code>./</code> 或 <code>../</code>（Unix）或 <code>.\\</code>、<code>..\\</code>、<code>./</code> 或 <code>../</code>（Windows）来与索引名称区分。</p>
<p>也可以通过 <code>UV_INDEX</code> 环境变量设置。</p></dd><dt id="uv-venv--index-strategy"><a href="#uv-venv--index-strategy"><code>--index-strategy</code></a> <i>index-strategy</i></dt><dd><p>针对多个索引 URL 进行解析时使用的策略。</p>
<p>默认情况下，uv 会在第一个找到给定包的索引处停止，并将解析范围限制为该第一个索引上存在的版本（<code>first-index</code>）。这可以防止"依赖混淆"（dependency confusion）攻击，即攻击者可以在替代索引上上传同名恶意包。</p>
<p>也可以通过 <code>UV_INDEX_STRATEGY</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>first-index</code>：仅使用为给定包名返回匹配结果的第一个索引的结果</li>
<li><code>unsafe-first-match</code>：在所有索引中搜索每个包名，在移至下一个索引之前穷尽第一个索引的版本</li>
<li><code>unsafe-best-match</code>：在所有索引中搜索每个包名，优先选择找到的"最佳"版本。如果一个包版本存在于多个索引中，则仅查看第一个索引中的条目</li>
</ul></dd><dt id="uv-venv--index-url"><a href="#uv-venv--index-url"><code>--index-url</code></a>, <code>-i</code> <i>index-url</i></dt><dd><p>（已弃用：请改用 <code>--default-index</code>）Python 包索引的 URL（默认为 <a href="https://pypi.org/simple">https://pypi.org/simple</a>）。</p>
<p>接受符合 PEP 503（简单仓库 API）的仓库，或按相同格式组织的本地目录。</p>
<p>通过此标志指定的索引的优先级低于通过 <code>--extra-index-url</code> 标志指定的所有其他索引。</p>
<p>也可以通过 <code>UV_INDEX_URL</code> 环境变量设置。</p></dd><dt id="uv-venv--keyring-provider"><a href="#uv-venv--keyring-provider"><code>--keyring-provider</code></a> <i>keyring-provider</i></dt><dd><p>尝试使用 <code>keyring</code> 进行索引 URL 的身份验证。</p>
<p>目前仅支持 <code>--keyring-provider subprocess</code>，它配置 uv 使用 <code>keyring</code> CLI 来处理身份验证。</p>
<p>默认为 <code>disabled</code>。</p>
<p>也可以通过 <code>UV_KEYRING_PROVIDER</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>disabled</code>：不使用 keyring 进行凭据查找</li>
<li><code>subprocess</code>：使用 <code>keyring</code> 命令进行凭据查找</li>
</ul></dd><dt id="uv-venv--link-mode"><a href="#uv-venv--link-mode"><code>--link-mode</code></a> <i>link-mode</i></dt><dd><p>从全局缓存安装包时使用的方法。</p>
<p>此选项仅用于安装种子包（seed packages）。</p>
<p>在 macOS 和 Linux 上默认为 <code>clone</code>（也称为写时复制 Copy-on-Write），在 Windows 上默认为 <code>hardlink</code>。</p>
<p>警告：不鼓励使用符号链接（symlink）模式，因为它会在缓存和目标环境之间建立紧密耦合。例如，清除缓存（<code>uv cache clean</code>）将通过删除底层源文件来破坏所有已安装的包。请谨慎使用符号链接。</p>
<p>也可以通过 <code>UV_LINK_MODE</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>clone</code>：从源克隆（即写时复制）包到目标</li>
<li><code>copy</code>：从源复制包到目标</li>
<li><code>hardlink</code>：从源硬链接包到目标</li>
<li><code>symlink</code>：从源符号链接包到目标</li>
</ul></dd><dt id="uv-venv--managed-python"><a href="#uv-venv--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用它管理的 Python 版本。但是，如果没有安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-venv--no-cache"><a href="#uv-venv--no-cache"><code>--no-cache</code></a>, <code>--no-cache-dir</code>, <code>-n</code></dt><dd><p>避免读取或写入缓存，在操作期间改用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-venv--no-config"><a href="#uv-venv--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-venv--no-index"><a href="#uv-venv--no-index"><code>--no-index</code></a></dt><dd><p>忽略注册表索引（例如 PyPI），转而依赖直接 URL 依赖和通过 <code>--find-links</code> 提供的依赖</p>
</dd><dt id="uv-venv--no-managed-python"><a href="#uv-venv--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-venv--no-progress"><a href="#uv-venv--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转指示器或进度条。</p>
</dd><dt id="uv-venv--no-project"><a href="#uv-venv--no-project"><code>--no-project</code></a>, <code>--no-workspace</code></dt><dd><p>避免发现项目或工作区。</p>
<p>默认情况下，uv 会在当前目录或任意父目录中搜索项目，以确定虚拟环境的默认路径并检查 Python 版本约束（如有）。</p>
<p>也可以通过 <code>UV_NO_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-venv--no-python-downloads"><a href="#uv-venv--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-venv--offline"><a href="#uv-venv--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用文件。</p>
</dd><dt id="uv-venv--project"><a href="#uv-venv--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也将同样被发现。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录进行解析。</p>
<p>参见 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-venv--prompt"><a href="#uv-venv--prompt"><code>--prompt</code></a> <i>prompt</i></dt><dd><p>为虚拟环境提供替代的提示符前缀。</p>
<p>默认情况下，提示符取决于是否向 <code>uv venv</code> 提供了路径。如果提供了路径（例如 <code>uv venv project</code>），提示符将设置为目录名。如果未提供路径（<code>uv venv</code>），提示符将设置为当前目录的名称。</p>
<p>如果提供了 <code>"."</code>，则无论是否向 <code>uv venv</code> 提供了路径，都将使用当前目录名。</p>
</dd><dt id="uv-venv--python"><a href="#uv-venv--python"><code>--python</code></a>, <code>-p</code> <i>python</i></dt><dd><p>用于虚拟环境的 Python 解释器。</p>
<p>在虚拟环境创建期间，uv 不会在虚拟环境中查找 Python 解释器。</p>
<p>有关 Python 发现和支持的请求格式的详细信息，请参见 <a href="#uv-python">uv python</a>。</p>
<p>也可以通过 <code>UV_PYTHON</code> 环境变量设置。</p></dd><dt id="uv-venv--quiet"><a href="#uv-venv--quiet"><code>--quiet</code></a>, <code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项，例如 <code>-qq</code>，将启用静默模式，在此模式下 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-venv--refresh"><a href="#uv-venv--refresh"><code>--refresh</code></a></dt><dd><p>刷新所有缓存数据</p>
</dd><dt id="uv-venv--refresh-package"><a href="#uv-venv--refresh-package"><code>--refresh-package</code></a> <i>refresh-package</i></dt><dd><p>刷新特定包的缓存数据</p>
</dd><dt id="uv-venv--relocatable"><a href="#uv-venv--relocatable"><code>--relocatable</code></a></dt><dd><p>使虚拟环境可重定位 [env: UV_VENV_RELOCATABLE=]</p>
<p>可重定位的虚拟环境可以移动和重新分发，而不会使其关联的入口点（entrypoint）和激活脚本失效。</p>
<p>请注意，这仅对标准的 <code>console_scripts</code> 和 <code>gui_scripts</code> 能保证。如果其他脚本带有通用的 <code>#!python[w]</code> shebang，则可能会被调整，而二进制文件则保持原样。</p>
<p>由于使环境可重定位（通过写入相对路径而非绝对路径），入口点和脚本本身将<em>不可</em>重定位。换句话说，将这些入口点和脚本复制到环境外部的位置将无法正常工作，因为它们引用的路径是相对于环境本身的。</p>
</dd><dt id="uv-venv--seed"><a href="#uv-venv--seed"><code>--seed</code></a></dt><dd><p>将种子包（<code>pip</code>、<code>setuptools</code> 和 <code>wheel</code> 中的一个或多个）安装到虚拟环境中 [env: UV_VENV_SEED=]</p>
<p>请注意，Python 3.12+ 环境中不包含 <code>setuptools</code> 和 <code>wheel</code>。</p>
</dd></dl>