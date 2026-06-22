---
title: uv init
description: uv init 命令用于创建新 Python 项目，遵循 pyproject.toml 规范。支持应用（application）、库（library）和脚本（script）三种项目类型，可配置构建后端、版本控制系统、作者信息等。本文档详细介绍了 uv init 命令的所有参数和选项用法。
---

# uv init

创建一个新项目。

遵循 `pyproject.toml` 规范。

如果目标位置已存在 `pyproject.toml`，uv 将报错退出。

如果在目标路径的任何父目录中找到 `pyproject.toml`，该项目将作为父项目的工作空间（workspace）成员添加。

某些项目状态在需要时才会创建，例如，项目虚拟环境（`.venv`）和锁文件（`uv.lock`）会在首次同步（sync）时延迟创建。

<h3 class="cli-reference">用法（Usage）</h3>

```
uv init [OPTIONS] [PATH]
```

<h3 class="cli-reference">参数（Arguments）</h3>

<dl class="cli-reference"><dt id="uv-init--path"><a href="#uv-init--path"><code>PATH</code></a></dt><dd><p>用于项目/脚本的路径。</p>
<p>初始化应用（app）或库（library）时默认为当前工作目录；初始化脚本（script）时为必需参数。接受相对路径和绝对路径。</p>
<p>如果在目标路径的任何父目录中找到 <code>pyproject.toml</code>，除非提供了 <code>--no-workspace</code>，否则该项目将作为父项目的 workspace 成员添加。</p>
</dd></dl>

<h3 class="cli-reference">选项（Options）</h3>

<dl class="cli-reference"><dt id="uv-init--allow-insecure-host"><a href="#uv-init--allow-insecure-host"><code>--allow-insecure-host</code></a>、<code>--trusted-host</code> <i>allow-insecure-host</i></dt><dd><p>允许与主机建立不安全连接。</p>
<p>可以多次提供。</p>
<p>期望接收主机名（例如 <code>localhost</code>）、主机端口对（例如 <code>localhost:8080</code>）或 URL（例如 <code>https://localhost</code>）。</p>
<p>警告：此列表中的主机将不会通过系统证书存储进行验证。仅在安全网络中使用 <code>--allow-insecure-host</code> 并确保来源可信，因为它会绕过 SSL 验证，可能使您遭受中间人攻击（MITM）。</p>
<p>也可以通过 <code>UV_INSECURE_HOST</code> 环境变量设置。</p></dd><dt id="uv-init--app"><a href="#uv-init--app"><code>--app</code></a>、<code>--application</code></dt><dd><p>创建一个应用（application）项目。</p>
<p>如果未指定 <code>--lib</code>，这是默认行为。</p>
<p>此类项目适用于 Web 服务器、脚本和命令行接口。</p>
<p>默认情况下，应用不打算作为 Python 包构建和分发。可以使用 <code>--package</code> 选项创建可分发的应用，例如，如果您想通过 PyPI 分发命令行接口。</p>
</dd><dt id="uv-init--author-from"><a href="#uv-init--author-from"><code>--author-from</code></a> <i>author-from</i></dt><dd><p>填充 <code>pyproject.toml</code> 中的 <code>authors</code> 字段。</p>
<p>默认情况下，uv 会尝试从某些来源（例如 Git）推断作者信息（<code>auto</code>）。使用 <code>--author-from git</code> 仅从 Git 配置推断。使用 <code>--author-from none</code> 则不推断作者信息。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>：从某些来源（例如 Git）自动获取作者信息</li>
<li><code>git</code>：仅从 Git 配置获取作者信息</li>
<li><code>none</code>：不推断作者信息</li>
</ul></dd><dt id="uv-init--bare"><a href="#uv-init--bare"><code>--bare</code></a></dt><dd><p>仅创建 <code>pyproject.toml</code>。</p>
<p>禁用创建额外文件，如 <code>README.md</code>、<code>src/</code> 目录树、<code>.python-version</code> 文件等。</p>
<p>仅在与 <code>--package</code> 或 <code>--build-backend</code> 结合使用时才创建 <code>[build-system]</code> 表。</p>
<p>当与 <code>--script</code> 结合使用时，脚本将仅包含内联元数据头。</p>
</dd><dt id="uv-init--build-backend"><a href="#uv-init--build-backend"><code>--build-backend</code></a> <i>build-backend</i></dt><dd><p>为项目初始化指定的构建后端（build-backend）。</p>
<p>隐式设置 <code>--package</code>。</p>
<p>也可以通过 <code>UV_INIT_BUILD_BACKEND</code> 环境变量设置。</p><p>可选值：</p>
<ul>
<li><code>uv</code>：使用 uv 作为项目构建后端</li>
<li><code>hatch</code>：使用 <a href="https://pypi.org/project/hatchling">hatchling</a> 作为项目构建后端</li>
<li><code>flit</code>：使用 <a href="https://pypi.org/project/flit-core">flit-core</a> 作为项目构建后端</li>
<li><code>pdm</code>：使用 <a href="https://pypi.org/project/pdm-backend">pdm-backend</a> 作为项目构建后端</li>
<li><code>poetry</code>：使用 <a href="https://pypi.org/project/poetry-core">poetry-core</a> 作为项目构建后端</li>
<li><code>setuptools</code>：使用 <a href="https://pypi.org/project/setuptools">setuptools</a> 作为项目构建后端</li>
<li><code>maturin</code>：使用 <a href="https://pypi.org/project/maturin">maturin</a> 作为项目构建后端</li>
<li><code>scikit</code>：使用 <a href="https://pypi.org/project/scikit-build-core">scikit-build-core</a> 作为项目构建后端</li>
</ul></dd><dt id="uv-init--cache-dir"><a href="#uv-init--cache-dir"><code>--cache-dir</code></a> <i>cache-dir</i></dt><dd><p>缓存目录的路径。</p>
<p>在 macOS 和 Linux 上默认为 <code>$XDG_CACHE_HOME/uv</code> 或 <code>$HOME/.cache/uv</code>，在 Windows 上默认为 <code>%LOCALAPPDATA%\uv\cache</code>。</p>
<p>要查看缓存目录的位置，请运行 <code>uv cache dir</code>。</p>
<p>也可以通过 <code>UV_CACHE_DIR</code> 环境变量设置。</p></dd><dt id="uv-init--color"><a href="#uv-init--color"><code>--color</code></a> <i>color-choice</i></dt><dd><p>控制输出中颜色的使用。</p>
<p>默认情况下，uv 会在写入终端时自动检测是否支持颜色。</p>
<p>可选值：</p>
<ul>
<li><code>auto</code>：仅在输出到支持颜色的终端或 TTY 时启用彩色输出</li>
<li><code>always</code>：无论检测到的环境如何，始终启用彩色输出</li>
<li><code>never</code>：禁用彩色输出</li>
</ul></dd><dt id="uv-init--config-file"><a href="#uv-init--config-file"><code>--config-file</code></a> <i>config-file</i></dt><dd><p>用于配置的 <code>uv.toml</code> 文件的路径。</p>
<p>虽然 uv 配置可以包含在 <code>pyproject.toml</code> 文件中，但在此上下文中不允许这样做。</p>
<p>也可以通过 <code>UV_CONFIG_FILE</code> 环境变量设置。</p></dd><dt id="uv-init--description"><a href="#uv-init--description"><code>--description</code></a> <i>description</i></dt><dd><p>设置项目描述</p>
</dd><dt id="uv-init--directory"><a href="#uv-init--directory"><code>--directory</code></a> <i>directory</i></dt><dd><p>在运行命令之前切换到指定目录。</p>
<p>相对路径以给定目录为基准进行解析。</p>
<p>请参阅 <code>--project</code> 以仅更改项目根目录。</p>
<p>也可以通过 <code>UV_WORKING_DIR</code> 环境变量设置。</p></dd><dt id="uv-init--help"><a href="#uv-init--help"><code>--help</code></a>、<code>-h</code></dt><dd><p>显示此命令的简明帮助信息</p>
</dd><dt id="uv-init--lib"><a href="#uv-init--lib"><code>--lib</code></a>、<code>--library</code></dt><dd><p>创建一个库（library）项目。</p>
<p>库是一个旨在作为 Python 包构建和分发的项目。</p>
</dd><dt id="uv-init--managed-python"><a href="#uv-init--managed-python"><code>--managed-python</code></a></dt><dd><p>要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]</p>
<p>默认情况下，uv 优先使用它管理的 Python 版本。但是，如果未安装 uv 管理的 Python，它将使用系统 Python 版本。此选项禁用系统 Python 版本的使用。</p>
</dd><dt id="uv-init--name"><a href="#uv-init--name"><code>--name</code></a> <i>name</i></dt><dd><p>项目名称。</p>
<p>默认为目录名称。</p>
</dd><dt id="uv-init--no-cache"><a href="#uv-init--no-cache"><code>--no-cache</code></a>、<code>--no-cache-dir</code>、<code>-n</code></dt><dd><p>避免读取或写入缓存，而是在操作期间使用临时目录</p>
<p>也可以通过 <code>UV_NO_CACHE</code> 环境变量设置。</p></dd><dt id="uv-init--no-config"><a href="#uv-init--no-config"><code>--no-config</code></a></dt><dd><p>避免发现配置文件（<code>pyproject.toml</code>、<code>uv.toml</code>）。</p>
<p>通常，配置文件会在当前目录、父目录或用户配置目录中被发现。</p>
<p>也可以通过 <code>UV_NO_CONFIG</code> 环境变量设置。</p></dd><dt id="uv-init--no-description"><a href="#uv-init--no-description"><code>--no-description</code></a></dt><dd><p>禁用项目描述</p>
</dd><dt id="uv-init--no-managed-python"><a href="#uv-init--no-managed-python"><code>--no-managed-python</code></a></dt><dd><p>禁用 uv 管理的 Python 版本的使用 [env: UV_NO_MANAGED_PYTHON=]</p>
<p>相反，uv 将在系统上搜索合适的 Python 版本。</p>
</dd><dt id="uv-init--no-package"><a href="#uv-init--no-package"><code>--no-package</code></a></dt><dd><p>不将项目设置为可作为 Python 包构建。</p>
<p>不为项目包含 <code>[build-system]</code>。</p>
<p>这是使用 <code>--app</code> 时的默认行为。</p>
</dd><dt id="uv-init--no-pin-python"><a href="#uv-init--no-pin-python"><code>--no-pin-python</code></a></dt><dd><p>不为项目创建 <code>.python-version</code> 文件。</p>
<p>默认情况下，uv 会创建一个 <code>.python-version</code> 文件，其中包含所发现 Python 解释器的次要版本，这将导致后续 uv 命令使用该版本。</p>
</dd><dt id="uv-init--no-progress"><a href="#uv-init--no-progress"><code>--no-progress</code></a></dt><dd><p>隐藏所有进度输出 [env: UV_NO_PROGRESS=]</p>
<p>例如，旋转指示器（spinner）或进度条。</p>
</dd><dt id="uv-init--no-python-downloads"><a href="#uv-init--no-python-downloads"><code>--no-python-downloads</code></a></dt><dd><p>禁用 Python 的自动下载。</p>
</dd><dt id="uv-init--no-readme"><a href="#uv-init--no-readme"><code>--no-readme</code></a></dt><dd><p>不创建 <code>README.md</code> 文件</p>
</dd><dt id="uv-init--no-workspace"><a href="#uv-init--no-workspace"><code>--no-workspace</code></a>、<code>--no-project</code></dt><dd><p>避免发现 workspace，创建一个独立项目。</p>
<p>默认情况下，uv 会在当前目录或任何父目录中搜索 workspace。</p>
</dd><dt id="uv-init--offline"><a href="#uv-init--offline"><code>--offline</code></a></dt><dd><p>禁用网络访问 [env: UV_OFFLINE=]</p>
<p>禁用后，uv 将仅使用本地缓存数据和本地可用的文件。</p>
</dd><dt id="uv-init--package"><a href="#uv-init--package"><code>--package</code></a></dt><dd><p>将项目设置为可作为 Python 包构建。</p>
<p>为项目定义 <code>[build-system]</code>。</p>
<p>这是使用 <code>--lib</code> 或 <code>--build-backend</code> 时的默认行为，或者当 <code>packaged-init</code> 预览功能启用时。未来将无条件成为默认行为。</p>
<p>当与 <code>--app</code> 一起使用时，将包含 <code>[project.scripts]</code> 入口点并使用 <code>src/</code> 项目结构。</p>
</dd><dt id="uv-init--project"><a href="#uv-init--project"><code>--project</code></a> <i>project</i></dt><dd><p>在给定目录中发现项目。</p>
<p>所有 <code>pyproject.toml</code>、<code>uv.toml</code> 和 <code>.python-version</code> 文件将通过从项目根目录向上遍历目录树来发现，项目的虚拟环境（<code>.venv</code>）也是如此。</p>
<p>其他命令行参数（如相对路径）将相对于当前工作目录解析。</p>
<p>请参阅 <code>--directory</code> 以完全更改工作目录。</p>
<p>此设置在 <code>uv pip</code> 接口中使用时无效。</p>
<p>也可以通过 <code>UV_PROJECT</code> 环境变量设置。</p></dd><dt id="uv-init--python"><a href="#uv-init--python"><code>--python</code></a>、<code>-p</code> <i>python</i></dt><dd><p>用于确定最低支持 Python 版本的 Python 解释器。</p>
<p>请参阅 <a href="#uv-python">uv python</a> 以查看支持的请求格式。</p>
<p>也可以通过 <code>UV_PYTHON</code> 环境变量设置。</p></dd><dt id="uv-init--quiet"><a href="#uv-init--quiet"><code>--quiet</code></a>、<code>-q</code></dt><dd><p>使用静默输出。</p>
<p>重复此选项（例如 <code>-qq</code>）将启用静默模式，在该模式下 uv 不会向 stdout 写入任何输出。</p>
</dd><dt id="uv-init--script"><a href="#uv-init--script"><code>--script</code></a></dt><dd><p>创建一个脚本。</p>
<p>脚本是一个独立文件，带有嵌入的元数据，枚举其依赖项以及任何 Python 版本要求，如 PEP 723 规范所定义。</p>
<p>PEP 723 脚本可以直接使用 <code>uv run</code> 执行。</p>
<p>默认情况下，添加对系统 Python 版本的要求；使用 <code>--python</code> 指定替代的 Python 版本要求。</p>
</dd><dt id="uv-init--system-certs"><a href="#uv-init--system-certs"><code>--system-certs</code></a></dt><dd><p>是否从平台的原生证书存储加载 TLS 证书 [env: UV_SYSTEM_CERTS=]</p>
<p>默认情况下，uv 使用捆绑的 Mozilla 根证书，这提高了可移植性和性能（尤其是在 macOS 上）。</p>
<p>但是，在某些情况下，您可能希望使用平台的原生证书存储，特别是当您依赖系统证书存储中包含的企业信任根（例如用于强制代理）时。</p>
</dd><dt id="uv-init--vcs"><a href="#uv-init--vcs"><code>--vcs</code></a> <i>vcs</i></dt><dd><p>为项目初始化版本控制系统。</p>
<p>默认情况下，uv 将初始化一个 Git 仓库（<code>git</code>）。使用 <code>--vcs none</code> 显式避免初始化版本控制系统。</p>
<p>可选值：</p>
<ul>
<li><code>git</code>：使用 Git 进行版本控制</li>
<li><code>none</code>：不使用任何版本控制系统</li>
</ul></dd><dt id="uv-init--verbose"><a href="#uv-init--verbose"><code>--verbose</code></a>、<code>-v</code></dt><dd><p>使用详细输出。</p>
<p>您可以使用 <code>RUST_LOG</code> 环境变量配置细粒度的日志记录。（<a href="https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives">https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#directives</a>）</p>
</dd></dl>
