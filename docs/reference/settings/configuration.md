---
subtitle: Configuration
description: 本文档是 uv 包管理器的完整配置参考，涵盖所有可用的配置选项，包括依赖项解析策略、索引管理、缓存控制、构建选项、Python 安装管理、pip 接口特定设置以及审计功能等，支持通过 pyproject.toml 和 uv.toml 进行配置。
---

# 配置

## [`add-bounds`](#add-bounds) {: #add-bounds }

添加依赖项时的默认版本约束符。

向项目添加依赖项时，如果未提供约束或 URL，则会根据该包的最新兼容版本添加约束。默认情况下，使用下限约束，例如 `>=1.2.3`。

当提供 `--frozen` 参数时，不会执行解析，并且依赖项始终不带约束地添加。

此选项为预览功能，在未来的任何版本中都可能发生变化。

**默认值**：`"lower"`

**可选值**：

- `"lower"`：仅下限，例如 `>=1.2.3`
- `"major"`：允许相同的主版本号，类似于 semver 的插入符（caret），例如 `>=1.2.3, <2.0.0`
- `"minor"`：允许相同的次版本号，类似于 semver 的波浪号（tilde），例如 `>=1.2.3, <1.3.0`
- `"exact"`：精确锁定版本，例如 `==1.2.3`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    add-bounds = "major"
    ```

=== "uv.toml"

    ```toml
    add-bounds = "major"
    ```

---

## [`allow-insecure-host`](#allow-insecure-host) {: #allow-insecure-host }

允许到主机的非安全连接。

期望接收主机名（例如 `localhost`）、主机-端口对（例如 `localhost:8080`）或 URL（例如 `https://localhost`）。

警告：此列表中的主机将不会根据系统证书存储进行验证。仅在安全的网络环境中使用 `--allow-insecure-host`，并确保来源可信，因为它会绕过 SSL 验证，可能使您遭受中间人（MITM）攻击。

**默认值**：`[]`

**类型**：`list[str]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    allow-insecure-host = ["localhost:8080"]
    ```

=== "uv.toml"

    ```toml
    allow-insecure-host = ["localhost:8080"]
    ```

---

## [`cache-dir`](#cache-dir) {: #cache-dir }

缓存目录的路径。

在 Linux 和 macOS 上默认为 `$XDG_CACHE_HOME/uv` 或 `$HOME/.cache/uv`，在 Windows 上为 `%LOCALAPPDATA%\uv\cache`。

**默认值**：`None`

**类型**：`str`

**使用示例**：

```toml title="uv.toml"

cache-dir = "./.uv_cache"
```

---

## [`cache-keys`](#cache-keys) {: #cache-keys }

缓存项目构建时考虑的键。

缓存键允许您指定修改后应触发重新构建的文件或目录。默认情况下，当项目目录中的 `pyproject.toml`、`setup.py` 或 `setup.cfg` 文件被修改，或者 `src` 目录被添加或移除时，uv 会重新构建项目，即：

```toml
cache-keys = [{ file = "pyproject.toml" }, { file = "setup.py" }, { file = "setup.cfg" }, { dir = "src" }]
```

例如：如果项目使用动态元数据从 `requirements.txt` 文件读取其依赖项，您可以指定 `cache-keys = [{ file = "requirements.txt" }, { file = "pyproject.toml" }]` 来确保在 `requirements.txt` 文件被修改时（除了监视 `pyproject.toml`）重新构建项目。

支持 glob 模式，遵循 [`glob`](https://docs.rs/glob/0.3.1/glob/struct.Pattern.html) crate 的语法。例如，要在项目目录或其任何子目录中的 `.toml` 文件被修改时使缓存失效，您可以指定 `cache-keys = [{ file = "**/*.toml" }]`。请注意，使用 glob 可能会带来性能开销，因为 uv 可能需要遍历文件系统来确定是否有文件发生了变化。

缓存键还可以包含版本控制信息。例如，如果项目使用 `setuptools_scm` 从 Git 提交读取其版本，您可以指定 `cache-keys = [{ git = { commit = true }, { file = "pyproject.toml" }]` 来将当前 Git 提交哈希包含在缓存键中（除了 `pyproject.toml`）。也支持 Git 标签，通过 `cache-keys = [{ git = { commit = true, tags = true } }]` 指定。

缓存键还可以包含环境变量。例如，如果项目依赖 `MACOSX_DEPLOYMENT_TARGET` 或其他环境变量来确定其行为，您可以指定 `cache-keys = [{ env = "MACOSX_DEPLOYMENT_TARGET" }]` 来在环境变量变化时使缓存失效。

缓存键仅影响其所在 `pyproject.toml` 定义的项目（而不是影响工作区中的所有成员），并且所有路径和 glob 都相对于项目目录进行解释。

**默认值**：`[{ file = "pyproject.toml" }, { file = "setup.py" }, { file = "setup.cfg" }]`

**类型**：`list[dict]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    cache-keys = [{ file = "pyproject.toml" }, { file = "requirements.txt" }, { git = { commit = true } }]
    ```

=== "uv.toml"

    ```toml
    cache-keys = [{ file = "pyproject.toml" }, { file = "requirements.txt" }, { git = { commit = true } }]
    ```

---

## [`check-url`](#check-url) {: #check-url }

检查索引 URL 中是否存在已有文件，以跳过重复上传。

此选项允许重试那些仅部分文件上传成功而失败的发布，并处理由于同一文件的并行上传导致的错误。

上传前，会检查索引。如果索引中已存在完全相同的文件，则不会上传该文件。如果上传过程中发生错误，会再次检查索引，以处理相同文件被并行上传两次的情况。

具体行为因索引而异。上传到 PyPI 时，即使没有 `--check-url`，上传相同文件也会成功，而大多数其他索引会报错。

索引必须提供支持的哈希算法之一（SHA-256、SHA-384 或 SHA-512）。

**默认值**：`None`

**类型**：`str`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    check-url = "https://test.pypi.org/simple"
    ```

=== "uv.toml"

    ```toml
    check-url = "https://test.pypi.org/simple"
    ```

---

## [`compile-bytecode`](#compile-bytecode) {: #compile-bytecode }

安装后将 Python 文件编译为字节码。

默认情况下，uv 不会将 Python（`.py`）文件编译为字节码（`__pycache__/*.pyc`）；相反，编译会在首次导入模块时延迟执行。对于启动时间至关重要的用例，如 CLI 应用程序和 Docker 容器，可以启用此选项以换取更长的安装时间，从而获得更快的启动速度。

启用后，uv 将处理整个 site-packages 目录（包括当前操作未修改的包）以保持一致性。与 pip 类似，它也会忽略错误。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    compile-bytecode = true
    ```

=== "uv.toml"

    ```toml
    compile-bytecode = true
    ```

---

## [`concurrent-builds`](#concurrent-builds) {: #concurrent-builds }

uv 在任何给定时间并发构建源分发包的最大数量。

默认为可用 CPU 核心数。

**默认值**：`None`

**类型**：`int`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    concurrent-builds = 4
    ```

=== "uv.toml"

    ```toml
    concurrent-builds = 4
    ```

---

## [`concurrent-downloads`](#concurrent-downloads) {: #concurrent-downloads }

uv 在任何给定时间执行的最大并发下载数。

**默认值**：`50`

**类型**：`int`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    concurrent-downloads = 4
    ```

=== "uv.toml"

    ```toml
    concurrent-downloads = 4
    ```

---

## [`concurrent-installs`](#concurrent-installs) {: #concurrent-installs }

安装和解压包时使用的线程数。

默认为可用 CPU 核心数。

**默认值**：`None`

**类型**：`int`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    concurrent-installs = 4
    ```

=== "uv.toml"

    ```toml
    concurrent-installs = 4
    ```

---

## [`config-settings`](#config-settings) {: #config-settings }

传递给 [PEP 517](https://peps.python.org/pep-0517/) 构建后端的设置，以 `KEY=VALUE` 对形式指定。

**默认值**：`{}`

**类型**：`dict`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    config-settings = { editable_mode = "compat" }
    ```

=== "uv.toml"

    ```toml
    config-settings = { editable_mode = "compat" }
    ```

---

## [`config-settings-package`](#config-settings-package) {: #config-settings-package }

传递给特定包的 [PEP 517](https://peps.python.org/pep-0517/) 构建后端的设置，以 `KEY=VALUE` 对形式指定。

接受从包名到字符串键值对的映射。

**默认值**：`{}`

**类型**：`dict`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    config-settings-package = { numpy = { editable_mode = "compat" } }
    ```

=== "uv.toml"

    ```toml
    config-settings-package = { numpy = { editable_mode = "compat" } }
    ```

---

## [`dependency-metadata`](#dependency-metadata) {: #dependency-metadata }

项目依赖项（直接或传递依赖）的预定义静态元数据。提供后，解析器可以使用指定的元数据，而无需查询注册表或从源代码构建相关包。

元数据应遵循 [Metadata 2.3](https://packaging.python.org/en/latest/specifications/core-metadata/) 标准，但仅以下字段会被使用：

- `name`：包的名称。
- （可选）`version`：包的版本。如果省略，元数据将应用于包的所有版本。
- （可选）`requires-dist`：包的依赖项（例如 `werkzeug>=0.14`）。
- （可选）`requires-python`：包所需的 Python 版本（例如 `>=3.10`）。
- （可选）`provides-extra`：包提供的 extras。

**默认值**：`[]`

**类型**：`list[dict]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    dependency-metadata = [
        { name = "flask", version = "1.0.0", requires-dist = ["werkzeug"], requires-python = ">=3.6" },
    ]
    ```

=== "uv.toml"

    ```toml
    dependency-metadata = [
        { name = "flask", version = "1.0.0", requires-dist = ["werkzeug"], requires-python = ">=3.6" },
    ]
    ```

---

## [`exclude-newer`](#exclude-newer) {: #exclude-newer }

将候选包限制为在给定日期之前上传的版本。

日期与每个单独分发包构件的上传时间（即每个文件上传到包索引的时间）进行比较，而不是包版本的发布日期。

接受 RFC 3339 时间戳（例如 `2006-12-02T02:07:43Z`）、"友好"时长（例如 `24 hours`、`1 week`、`30 days`）或 ISO 8601 时长（例如 `PT24H`、`P7D`、`P30D`）。

时长不遵循本地时区的语义，始终以一天为 24 小时解析为固定秒数（例如，忽略夏令时转换）。不允许使用月和年等日历单位。

**默认值**：`None`

**类型**：`str`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    exclude-newer = "2006-12-02T02:07:43Z"
    ```

=== "uv.toml"

    ```toml
    exclude-newer = "2006-12-02T02:07:43Z"
    ```

---

## [`exclude-newer-package`](#exclude-newer-package) {: #exclude-newer-package }

将特定包的候选包限制为在给定日期之前上传的版本。

接受 `PACKAGE = "DATE"` 对的字典格式，其中 `DATE` 是 RFC 3339 时间戳（例如 `2006-12-02T02:07:43Z`）、"友好"时长（例如 `24 hours`、`1 week`、`30 days`）或 ISO 8601 时长（例如 `PT24H`、`P7D`、`P30D`）。

时长不遵循本地时区的语义，始终以一天为 24 小时解析为固定秒数（例如，忽略夏令时转换）。不允许使用月和年等日历单位。

将包设置为 `false` 可使其完全不受全局 [`exclude-newer`](#exclude-newer) 约束的影响。

**默认值**：`None`

**类型**：`dict`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    exclude-newer-package = { tqdm = "2022-04-04T00:00:00Z", markupsafe = false }
    ```

=== "uv.toml"

    ```toml
    exclude-newer-package = { tqdm = "2022-04-04T00:00:00Z", markupsafe = false }
    ```

---

## [`extra-build-dependencies`](#extra-build-dependencies) {: #extra-build-dependencies }

包的额外构建依赖项。

这允许使用额外的包来扩展项目依赖项的 PEP 517 构建环境。这对于那些假定存在某些包（如 `pip`）但未将其声明为构建依赖项的包非常有用。

**默认值**：`[]`

**类型**：`dict`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    extra-build-dependencies = { pytest = ["setuptools"] }
    ```

=== "uv.toml"

    ```toml
    extra-build-dependencies = { pytest = ["setuptools"] }
    ```

---

## [`extra-build-variables`](#extra-build-variables) {: #extra-build-variables }

构建特定包时设置的额外环境变量。

构建指定包时，环境变量将被添加到构建环境中。

**默认值**：`{}`

**类型**：`dict[str, dict[str, str]]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    extra-build-variables = { flash-attn = { FLASH_ATTENTION_SKIP_CUDA_BUILD = "TRUE" } }
    ```

=== "uv.toml"

    ```toml
    extra-build-variables = { flash-attn = { FLASH_ATTENTION_SKIP_CUDA_BUILD = "TRUE" } }
    ```

---

## [`extra-index-url`](#extra-index-url) {: #extra-index-url }

除 `--index-url` 之外使用的额外包索引 URL。

接受符合 [PEP 503](https://peps.python.org/pep-0503/)（简单仓库 API）的仓库，或以相同格式组织的本地目录。

通过此标志提供的所有索引优先级高于 [`index_url`](#index-url) 或带有 `default = true` 的 [`index`](#index) 指定的索引。当提供多个索引时，较早的值优先级更高。

要控制多个索引存在时 uv 的解析策略，请参阅 [`index_strategy`](#index-strategy)。

（已弃用：请改用 `index`。）

**默认值**：`[]`

**类型**：`list[str]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    extra-index-url = ["https://download.pytorch.org/whl/cpu"]
    ```

=== "uv.toml"

    ```toml
    extra-index-url = ["https://download.pytorch.org/whl/cpu"]
    ```

---

## [`find-links`](#find-links) {: #find-links }

除注册表索引中找到的之外，用于搜索候选分发包的位置。

如果是路径，目标必须是一个目录，其中包含顶层为 wheel 文件（`.whl`）或源分发包（例如 `.tar.gz` 或 `.zip`）的包。

如果是 URL，页面必须包含指向符合上述格式的包文件的扁平链接列表。

**默认值**：`[]`

**类型**：`list[str]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    find-links = ["https://download.pytorch.org/whl/torch_stable.html"]
    ```

=== "uv.toml"

    ```toml
    find-links = ["https://download.pytorch.org/whl/torch_stable.html"]
    ```

---

## [`fork-strategy`](#fork-strategy) {: #fork-strategy }

在跨 Python 版本和平台时为给定包选择多个版本所使用的策略。

默认情况下，uv 会优化为每个受支持的 Python 版本（`requires-python`）选择每个包的最新版本，同时最小化跨平台选择的版本数量。

在 `fewest` 策略下，uv 将最小化每个包选择的版本数量，优先选择与更广泛受支持的 Python 版本或平台兼容的旧版本。

**默认值**：`"requires-python"`

**可选值**：

- `"fewest"`：优化为每个包选择最少数量的版本。如果旧版本与更广泛受支持的 Python 版本或平台兼容，可能会被优先选择
- `"requires-python"`：优化为每个受支持的 Python 版本选择每个包的最新支持版本

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    fork-strategy = "fewest"
    ```

=== "uv.toml"

    ```toml
    fork-strategy = "fewest"
    ```

---

## [`http-proxy`](#http-proxy) {: #http-proxy }

要使用的 HTTP 代理的 URL。

**默认值**：`None`

**类型**：`str`

**使用示例**：

```toml title="uv.toml"

http-proxy = "http://proxy.example.com"
```

---

## [`https-proxy`](#https-proxy) {: #https-proxy }

要使用的 HTTPS 代理的 URL。

**默认值**：`None`

**类型**：`str`

**使用示例**：

```toml title="uv.toml"

https-proxy = "https://proxy.example.com"
```

---

## [`index`](#index) {: #index }

解析依赖项时使用的包索引。

接受符合 [PEP 503](https://peps.python.org/pep-0503/)（简单仓库 API）的仓库，或以相同格式组织的本地目录。

索引按定义顺序依次考虑，因此最先定义的索引具有最高优先级。此外，此设置提供的索引优先级高于通过 [`index_url`](#index-url) 或 [`extra_index_url`](#extra-index-url) 指定的任何索引。除非指定了替代的[索引策略](#index-strategy)，否则 uv 只会考虑包含给定包的第一个索引。

如果索引被标记为 `explicit = true`，它将专门用于那些通过 `[tool.uv.sources]` 显式选择它的依赖项，如下所示：

```toml
[[tool.uv.index]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cu130"
explicit = true

[tool.uv.sources]
torch = { index = "pytorch" }
```

如果索引被标记为 `default = true`，它将被移动到优先级列表的末尾，因此在解析包时被赋予最低优先级。此外，将索引标记为 default 将禁用 PyPI 默认索引。

**默认值**：`"[]"`

**类型**：`dict`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [[tool.uv.index]]
    name = "pytorch"
    url = "https://download.pytorch.org/whl/cu130"
    ```

=== "uv.toml"

    ```toml
    [[tool.uv.index]]
    name = "pytorch"
    url = "https://download.pytorch.org/whl/cu130"
    ```

---

## [`index-strategy`](#index-strategy) {: #index-strategy }

针对多个索引 URL 进行解析时使用的策略。

默认情况下，uv 会在找到给定包的第一个索引处停止，并将解析结果限制在该第一个索引上存在的版本（`first-index`）。这可以防止"依赖混淆"攻击，即攻击者可以在替代索引上上传同名的恶意包。

**默认值**：`"first-index"`

**可选值**：

- `"first-index"`：仅使用第一个返回给定包名匹配项的索引的结果
- `"unsafe-first-match"`：在所有索引中搜索每个包名，在移向下一个索引之前穷尽第一个索引的版本
- `"unsafe-best-match"`：在所有索引中搜索每个包名，优先选择找到的"最佳"版本。如果某个包版本存在于多个索引中，则仅查看第一个索引的条目

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    index-strategy = "unsafe-best-match"
    ```

=== "uv.toml"

    ```toml
    index-strategy = "unsafe-best-match"
    ```

---

## [`index-url`](#index-url) {: #index-url }

Python 包索引的 URL（默认：<https://pypi.org/simple>）。

接受符合 [PEP 503](https://peps.python.org/pep-0503/)（简单仓库 API）的仓库，或以相同格式组织的本地目录。

此设置提供的索引优先级低于通过 [`extra_index_url`](#extra-index-url) 或 [`index`](#index) 指定的任何索引。

（已弃用：请改用 `index`。）

**默认值**：`"https://pypi.org/simple"`

**类型**：`str`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    index-url = "https://test.pypi.org/simple"
    ```

=== "uv.toml"

    ```toml
    index-url = "https://test.pypi.org/simple"
    ```

---

## [`keyring-provider`](#keyring-provider) {: #keyring-provider }

尝试使用 `keyring` 进行索引 URL 的身份验证。

目前仅支持 `--keyring-provider subprocess`，它配置 uv 使用 `keyring` CLI 来处理身份验证。

**默认值**：`"disabled"`

**类型**：`str`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    keyring-provider = "subprocess"
    ```

=== "uv.toml"

    ```toml
    keyring-provider = "subprocess"
    ```

---

## [`link-mode`](#link-mode) {: #link-mode }

从全局缓存安装包时使用的方法。

在 macOS 和 Linux 上默认为 `clone`（也称为写时复制），在 Windows 上默认为 `hardlink`。

警告：不鼓励使用 symlink 链接模式，因为它会在缓存和目标环境之间创建紧密耦合。例如，清除缓存（`uv cache clean`）将通过移除底层源文件而破坏所有已安装的包。请谨慎使用 symlink。

**默认值**：`"clone"`（macOS、Linux）或 `"hardlink"`（Windows）

**可选值**：

- `"clone"`：将包从源克隆（即写时复制）到目标
- `"copy"`：将包从源复制到目标
- `"hardlink"`：将包从源硬链接到目标
- `"symlink"`：将包从源符号链接到目标

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    link-mode = "copy"
    ```

=== "uv.toml"

    ```toml
    link-mode = "copy"
    ```

---

## [`native-tls`](#native-tls) {: #native-tls }

!!! warning "已弃用"
    此选项已弃用，请改用 `system-certs`。

是否从平台的原生证书存储加载 TLS 证书。

默认情况下，uv 使用捆绑的 Mozilla 根证书。启用后，将改为从平台的原生证书存储加载证书。

（已弃用：请改用 `system-certs`。）

**默认值**：`false`

**类型**：`bool`

**使用示例**：

```toml title="uv.toml"

native-tls = true
```

---

## [`no-binary`](#no-binary) {: #no-binary }

不安装预构建的 wheel。

给定的包将从源代码构建和安装。解析器仍将使用预构建的 wheel 来提取包元数据（如果可用）。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    no-binary = true
    ```

=== "uv.toml"

    ```toml
    no-binary = true
    ```

---

## [`no-binary-package`](#no-binary-package) {: #no-binary-package }

不为特定包安装预构建的 wheel。

**默认值**：`[]`

**类型**：`list[str]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    no-binary-package = ["ruff"]
    ```

=== "uv.toml"

    ```toml
    no-binary-package = ["ruff"]
    ```

---

## [`no-build`](#no-build) {: #no-build }

不构建源分发包。

启用后，解析将不会运行任意 Python 代码。已构建的源分发包的缓存 wheel 将被重用，但需要构建分发包的操作将以错误退出。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    no-build = true
    ```

=== "uv.toml"

    ```toml
    no-build = true
    ```

---

## [`no-build-isolation`](#no-build-isolation) {: #no-build-isolation }

构建源分发包时禁用隔离。

假定 [PEP 518](https://peps.python.org/pep-0518/) 指定的构建依赖项已经安装。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    no-build-isolation = true
    ```

=== "uv.toml"

    ```toml
    no-build-isolation = true
    ```

---

## [`no-build-isolation-package`](#no-build-isolation-package) {: #no-build-isolation-package }

为特定包构建源分发包时禁用隔离。

假定这些包的 [PEP 518](https://peps.python.org/pep-0518/) 指定的构建依赖项已经安装。

**默认值**：`[]`

**类型**：`list[str]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    no-build-isolation-package = ["package1", "package2"]
    ```

=== "uv.toml"

    ```toml
    no-build-isolation-package = ["package1", "package2"]
    ```

---

## [`no-build-package`](#no-build-package) {: #no-build-package }

不为特定包构建源分发包。

**默认值**：`[]`

**类型**：`list[str]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    no-build-package = ["ruff"]
    ```

=== "uv.toml"

    ```toml
    no-build-package = ["ruff"]
    ```

---

## [`no-cache`](#no-cache) {: #no-cache }

避免读取或写入缓存，而是在操作期间使用临时目录。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    no-cache = true
    ```

=== "uv.toml"

    ```toml
    no-cache = true
    ```

---

## [`no-index`](#no-index) {: #no-index }

忽略所有注册表索引（例如 PyPI），改为依赖直接 URL 依赖项和通过 `--find-links` 提供的依赖项。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    no-index = true
    ```

=== "uv.toml"

    ```toml
    no-index = true
    ```

---

## [`no-proxy`](#no-proxy) {: #no-proxy }

要从代理中排除的主机列表。

**默认值**：`None`

**类型**：`list[str]`

**使用示例**：

```toml title="uv.toml"

no-proxy = ["localhost", "127.0.0.1"]
```

---

## [`no-sources`](#no-sources) {: #no-sources }

解析依赖项时忽略 `tool.uv.sources` 表。用于根据符合标准的、可发布的包元数据进行锁定，而不是使用任何本地或 Git 源。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    no-sources = true
    ```

=== "uv.toml"

    ```toml
    no-sources = true
    ```

---

## [`no-sources-package`](#no-sources-package) {: #no-sources-package }

忽略指定包的 `tool.uv.sources`。

**默认值**：`[]`

**类型**：`list[str]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    no-sources-package = ["ruff"]
    ```

=== "uv.toml"

    ```toml
    no-sources-package = ["ruff"]
    ```

---

## [`offline`](#offline) {: #offline }

禁用网络访问，仅依赖本地缓存数据和本地可用文件。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    offline = true
    ```

=== "uv.toml"

    ```toml
    offline = true
    ```

---

## [`prerelease`](#prerelease) {: #prerelease }

考虑预发布版本时使用的策略。

默认情况下，uv 将接受那些*仅*发布预发布版本的包的预发布版本，以及在声明的约束符中包含显式预发布标记的第一方需求（`if-necessary-or-explicit`）。

**默认值**：`"if-necessary-or-explicit"`

**可选值**：

- `"disallow"`：禁止所有预发布版本
- `"allow"`：允许所有预发布版本
- `"if-necessary"`：如果包的所有版本都是预发布版本，则允许预发布版本
- `"explicit"`：对于版本需求中包含显式预发布标记的第一方包，允许预发布版本
- `"if-necessary-or-explicit"`：如果包的所有版本都是预发布版本，或者包的版本需求中包含显式预发布标记，则允许预发布版本

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    prerelease = "allow"
    ```

=== "uv.toml"

    ```toml
    prerelease = "allow"
    ```

---

## [`preview-features`](#preview-features) {: #preview-features }

是否启用特定或全部实验性预览功能。

未知的功能名称将被忽略并发出警告。

**默认值**：`false`

**类型**：`bool | list[str]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    preview-features = true
    # 或
    preview-features = ["python-upgrade"]
    ```

=== "uv.toml"

    ```toml
    preview-features = true
    # 或
    preview-features = ["python-upgrade"]
    ```

---

## [`publish-url`](#publish-url) {: #publish-url }

用于将包发布到 Python 包索引的 URL（默认：<https://upload.pypi.org/legacy/>）。

**默认值**：`"https://upload.pypi.org/legacy/"`

**类型**：`str`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    publish-url = "https://test.pypi.org/legacy/"
    ```

=== "uv.toml"

    ```toml
    publish-url = "https://test.pypi.org/legacy/"
    ```

---

## [`pypy-install-mirror`](#pypy-install-mirror) {: #pypy-install-mirror }

用于下载托管的 PyPy 安装的镜像 URL。

默认情况下，托管的 PyPy 安装从 [downloads.python.org](https://downloads.python.org/) 下载。此变量可以设置为镜像 URL，以使用不同的源来获取 PyPy 安装。提供的 URL 将替换例如 `https://downloads.python.org/pypy/pypy3.8-v7.3.7-osx64.tar.bz2` 中的 `https://downloads.python.org/pypy`。

可以使用 `file://` URL 方案从本地目录读取分发包。

**默认值**：`None`

**类型**：`str`

**使用示例**：

```toml title="uv.toml"

pypy-install-mirror = "https://downloads.python.org/pypy"
```

---

## [`python-downloads`](#python-downloads) {: #python-downloads }

是否允许下载 Python。

**默认值**：`"automatic"`

**可选值**：

- `"automatic"`：在需要时自动下载托管的 Python 安装
- `"manual"`：不自动下载托管的 Python 安装；需要显式安装
- `"never"`：永远不允许 Python 下载

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    python-downloads = "manual"
    ```

=== "uv.toml"

    ```toml
    python-downloads = "manual"
    ```

---

## [`python-downloads-json-url`](#python-downloads-json-url) {: #python-downloads-json-url }

指向自定义 Python 安装 JSON 的 URL。

**默认值**：`None`

**类型**：`str`

**使用示例**：

```toml title="uv.toml"

python-downloads-json-url = "/etc/uv/python-downloads.json"
```

---

## [`python-install-mirror`](#python-install-mirror) {: #python-install-mirror }

用于下载托管 Python 安装的镜像 URL。

默认情况下，托管的 Python 安装从 [`python-build-standalone`](https://github.com/astral-sh/python-build-standalone) 下载。此变量可以设置为镜像 URL，以使用不同的源来获取 Python 安装。提供的 URL 将替换例如 `https://github.com/astral-sh/python-build-standalone/releases/download/20240713/cpython-3.12.4%2B20240713-aarch64-apple-darwin-install_only.tar.gz` 中的 `https://github.com/astral-sh/python-build-standalone/releases/download`。

可以使用 `file://` URL 方案从本地目录读取分发包。

**默认值**：`None`

**类型**：`str`

**使用示例**：

```toml title="uv.toml"

python-install-mirror = "https://github.com/astral-sh/python-build-standalone/releases/download"
```

---

## [`python-preference`](#python-preference) {: #python-preference }

是优先使用系统上已存在的 Python 安装，还是优先使用由 uv 下载和安装的 Python。

**默认值**：`"managed"`

**可选值**：

- `"only-managed"`：仅使用托管的 Python 安装；从不使用系统 Python 安装
- `"managed"`：优先使用托管的 Python 安装而非系统 Python 安装
- `"system"`：优先使用系统 Python 安装而非托管的 Python 安装
- `"only-system"`：仅使用系统 Python 安装；从不使用托管的 Python 安装

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    python-preference = "managed"
    ```

=== "uv.toml"

    ```toml
    python-preference = "managed"
    ```

---

## [`reinstall`](#reinstall) {: #reinstall }

重新安装所有包，无论它们是否已安装。隐含 `refresh`。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    reinstall = true
    ```

=== "uv.toml"

    ```toml
    reinstall = true
    ```

---

## [`reinstall-package`](#reinstall-package) {: #reinstall-package }

重新安装特定包，无论它是否已安装。隐含 `refresh-package`。

**默认值**：`[]`

**类型**：`list[str]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    reinstall-package = ["ruff"]
    ```

=== "uv.toml"

    ```toml
    reinstall-package = ["ruff"]
    ```

---

## [`required-version`](#required-version) {: #required-version }

强制要求 uv 的版本。

如果 uv 的版本在运行时不符合要求，uv 将以错误退出。

接受 [PEP 440](https://peps.python.org/pep-0440/) 约束符，如 `==0.5.0` 或 `>=0.5.0`。

**默认值**：`null`

**类型**：`str`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    required-version = ">=0.5.0"
    ```

=== "uv.toml"

    ```toml
    required-version = ">=0.5.0"
    ```

---

## [`resolution`](#resolution) {: #resolution }

在给定包需求的不同兼容版本之间进行选择时使用的策略。

默认情况下，uv 将使用每个包的最新兼容版本（`highest`）。

**默认值**：`"highest"`

**可选值**：

- `"highest"`：解析每个包的最高兼容版本
- `"lowest"`：解析每个包的最低兼容版本
- `"lowest-direct"`：解析任何直接依赖项的最低兼容版本，以及任何传递依赖项的最高兼容版本

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    resolution = "lowest-direct"
    ```

=== "uv.toml"

    ```toml
    resolution = "lowest-direct"
    ```

---

## [`system-certs`](#system-certs) {: #system-certs }

是否从平台的原生证书存储加载 TLS 证书。

默认情况下，uv 使用捆绑的 Mozilla 根证书。启用后，将改为从平台的原生证书存储加载证书。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

```toml title="uv.toml"

system-certs = true
```

---

## [`torch-backend`](#torch-backend) {: #torch-backend }

获取 PyTorch 生态系统中的包时使用的后端。

设置后，uv 将忽略为 PyTorch 生态系统中的包配置的索引 URL，而使用定义的后端。

例如，当设置为 `cpu` 时，uv 将使用仅 CPU 的 PyTorch 索引；当设置为 `cu126` 时，uv 将使用适用于 CUDA 12.6 的 PyTorch 索引。

`auto` 模式将尝试根据当前安装的 CUDA 驱动程序检测适当的 PyTorch 索引。

此设置仅对 `uv pip` 命令生效。

此选项为预览功能，在未来的任何版本中都可能发生变化。

**默认值**：`null`

**类型**：`str`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    torch-backend = "auto"
    ```

=== "uv.toml"

    ```toml
    torch-backend = "auto"
    ```

---

## [`trusted-publishing`](#trusted-publishing) {: #trusted-publishing }

配置可信发布（trusted publishing）。

默认情况下，uv 在受支持的环境中运行时检查可信发布，但如果未配置则忽略它。

uv 支持的可信发布环境包括 GitHub Actions 和 GitLab CI/CD。

**默认值**：`automatic`

**类型**：`str`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    trusted-publishing = "always"
    ```

=== "uv.toml"

    ```toml
    trusted-publishing = "always"
    ```

---

### [`upgrade`](#upgrade) {: #upgrade }

允许包升级，忽略任何现有输出文件中的固定版本。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    upgrade = true
    ```

=== "uv.toml"

    ```toml
    upgrade = true
    ```

---

## [`upgrade-package`](#upgrade-package) {: #upgrade-package }

允许特定包升级，忽略任何现有输出文件中的固定版本。

接受独立的包名（`ruff`）和版本约束符（`ruff<0.5.0`）。

**默认值**：`[]`

**类型**：`list[str]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv]
    upgrade-package = ["ruff"]
    ```

=== "uv.toml"

    ```toml
    upgrade-package = ["ruff"]
    ```

---

## `audit`

### [`ignore`](#audit_ignore) {: #audit_ignore }
<span id="ignore"></span>

审计期间要忽略的漏洞 ID 列表。

匹配任何提供的 ID（包括别名）的漏洞将从审计结果中排除。

**默认值**：`[]`

**类型**：`list[str]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.audit]
    ignore = ["PYSEC-2022-43017", "GHSA-5239-wwwm-4pmq"]
    ```

=== "uv.toml"

    ```toml
    [audit]
    ignore = ["PYSEC-2022-43017", "GHSA-5239-wwwm-4pmq"]
    ```

---

### [`ignore-until-fixed`](#audit_ignore-until-fixed) {: #audit_ignore-until-fixed }
<span id="ignore-until-fixed"></span>

审计期间要忽略的漏洞 ID 列表，但仅在尚无修复版本时忽略。

匹配任何提供的 ID（包括别名）的漏洞只要没有已知的修复版本，就会从审计结果中排除。一旦修复版本可用，该漏洞将再次被报告。

**默认值**：`[]`

**类型**：`list[str]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.audit]
    ignore-until-fixed = ["PYSEC-2022-43017"]
    ```

=== "uv.toml"

    ```toml
    [audit]
    ignore-until-fixed = ["PYSEC-2022-43017"]
    ```

---

## `pip`

特定于 `uv pip` 命令行接口的设置。

这些值在运行 `uv pip` 命名空间之外的命令（例如 `uv lock`、`uvx`）时将被忽略。

### [`all-extras`](#pip_all-extras) {: #pip_all-extras }
<span id="all-extras"></span>

包含所有可选依赖项。

仅适用于 `pyproject.toml`、`setup.py` 和 `setup.cfg` 源。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    all-extras = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    all-extras = true
    ```

---

### [`allow-empty-requirements`](#pip_allow-empty-requirements) {: #pip_allow-empty-requirements }
<span id="allow-empty-requirements"></span>

允许 `uv pip sync` 使用空的需求列表，这将清除环境中的所有包。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    allow-empty-requirements = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    allow-empty-requirements = true
    ```

---

### [`annotation-style`](#pip_annotation-style) {: #pip_annotation-style }
<span id="annotation-style"></span>

输出文件中包含的注释标注的样式，用于指示每个包的来源。

**默认值**：`"split"`

**可选值**：

- `"line"`：将标注呈现在单行，以逗号分隔
- `"split"`：将每个标注呈现在单独的行上

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    annotation-style = "line"
    ```

=== "uv.toml"

    ```toml
    [pip]
    annotation-style = "line"
    ```

---

### [`break-system-packages`](#pip_break-system-packages) {: #pip_break-system-packages }
<span id="break-system-packages"></span>

允许 uv 修改 `EXTERNALLY-MANAGED` Python 安装。

警告：`--break-system-packages` 旨在用于持续集成（CI）环境中，当安装到由外部包管理器（如 `apt`）管理的 Python 安装中时使用。应谨慎使用，因为此类 Python 安装明确建议不要由其他包管理器（如 uv 或 pip）进行修改。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    break-system-packages = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    break-system-packages = true
    ```

---

### [`compile-bytecode`](#pip_compile-bytecode) {: #pip_compile-bytecode }
<span id="compile-bytecode"></span>

安装后将 Python 文件编译为字节码。

默认情况下，uv 不会将 Python（`.py`）文件编译为字节码（`__pycache__/*.pyc`）；相反，编译会在首次导入模块时延迟执行。对于启动时间至关重要的用例，如 CLI 应用程序和 Docker 容器，可以启用此选项以换取更长的安装时间，从而获得更快的启动速度。

启用后，uv 将处理整个 site-packages 目录（包括当前操作未修改的包）以保持一致性。与 pip 类似，它也会忽略错误。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    compile-bytecode = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    compile-bytecode = true
    ```

---

### [`config-settings`](#pip_config-settings) {: #pip_config-settings }
<span id="config-settings"></span>

传递给 [PEP 517](https://peps.python.org/pep-0517/) 构建后端的设置，以 `KEY=VALUE` 对形式指定。

**默认值**：`{}`

**类型**：`dict`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    config-settings = { editable_mode = "compat" }
    ```

=== "uv.toml"

    ```toml
    [pip]
    config-settings = { editable_mode = "compat" }
    ```

---

### [`config-settings-package`](#pip_config-settings-package) {: #pip_config-settings-package }
<span id="config-settings-package"></span>

传递给特定包的 [PEP 517](https://peps.python.org/pep-0517/) 构建后端的设置，以 `KEY=VALUE` 对形式指定。

**默认值**：`{}`

**类型**：`dict`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    config-settings-package = { numpy = { editable_mode = "compat" } }
    ```

=== "uv.toml"

    ```toml
    [pip]
    config-settings-package = { numpy = { editable_mode = "compat" } }
    ```

---

### [`custom-compile-command`](#pip_custom-compile-command) {: #pip_custom-compile-command }
<span id="custom-compile-command"></span>

在 `uv pip compile` 生成的输出文件顶部包含的标题注释。

用于反映包装 `uv pip compile` 的自定义构建脚本和命令。

**默认值**：`None`

**类型**：`str`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    custom-compile-command = "./custom-uv-compile.sh"
    ```

=== "uv.toml"

    ```toml
    [pip]
    custom-compile-command = "./custom-uv-compile.sh"
    ```

---

### [`dependency-metadata`](#pip_dependency-metadata) {: #pip_dependency-metadata }
<span id="dependency-metadata"></span>

项目依赖项（直接或传递依赖）的预定义静态元数据。提供后，解析器可以使用指定的元数据，而无需查询注册表或从源代码构建相关包。

元数据应遵循 [Metadata 2.3](https://packaging.python.org/en/latest/specifications/core-metadata/) 标准，但仅以下字段会被使用：

- `name`：包的名称。
- （可选）`version`：包的版本。如果省略，元数据将应用于包的所有版本。
- （可选）`requires-dist`：包的依赖项（例如 `werkzeug>=0.14`）。
- （可选）`requires-python`：包所需的 Python 版本（例如 `>=3.10`）。
- （可选）`provides-extra`：包提供的 extras。

**默认值**：`[]`

**类型**：`list[dict]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    dependency-metadata = [
        { name = "flask", version = "1.0.0", requires-dist = ["werkzeug"], requires-python = ">=3.6" },
    ]
    ```

=== "uv.toml"

    ```toml
    [pip]
    dependency-metadata = [
        { name = "flask", version = "1.0.0", requires-dist = ["werkzeug"], requires-python = ">=3.6" },
    ]
    ```

---

### [`emit-build-options`](#pip_emit-build-options) {: #pip_emit-build-options }
<span id="emit-build-options"></span>

在 `uv pip compile` 生成的输出文件中包含 `--no-binary` 和 `--only-binary` 条目。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    emit-build-options = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    emit-build-options = true
    ```

---

### [`emit-find-links`](#pip_emit-find-links) {: #pip_emit-find-links }
<span id="emit-find-links"></span>

在 `uv pip compile` 生成的输出文件中包含 `--find-links` 条目。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    emit-find-links = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    emit-find-links = true
    ```

---

### [`emit-index-annotation`](#pip_emit-index-annotation) {: #pip_emit-index-annotation }
<span id="emit-index-annotation"></span>

包含注释标注，指示用于解析每个包的索引（例如 `# from https://pypi.org/simple`）。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    emit-index-annotation = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    emit-index-annotation = true
    ```

---

### [`emit-index-url`](#pip_emit-index-url) {: #pip_emit-index-url }
<span id="emit-index-url"></span>

在 `uv pip compile` 生成的输出文件中包含 `--index-url` 和 `--extra-index-url` 条目。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    emit-index-url = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    emit-index-url = true
    ```

---

### [`emit-marker-expression`](#pip_emit-marker-expression) {: #pip_emit-marker-expression }
<span id="emit-marker-expression"></span>

是否输出一个标记字符串，指示固定依赖项集在何种条件下有效。

即使标记表达式为 false，固定依赖项可能仍然有效，但当表达式为 true 时，已知需求是正确的。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    emit-marker-expression = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    emit-marker-expression = true
    ```

---

### [`exclude-newer`](#pip_exclude-newer) {: #pip_exclude-newer }
<span id="exclude-newer"></span>

将候选包限制为在给定时间点之前上传的版本。

日期与每个单独分发包构件的上传时间（即每个文件上传到包索引的时间）进行比较，而不是包版本的发布日期。

接受 RFC 3339 时间戳（例如 `2006-12-02T02:07:43Z`）、"友好"时长（例如 `24 hours`、`1 week`、`30 days`）或 ISO 8601 时长（例如 `PT24H`、`P7D`、`P30D`）。

时长不遵循本地时区的语义，始终以一天为 24 小时解析为固定秒数（例如，忽略夏令时转换）。不允许使用月和年等日历单位。

**默认值**：`None`

**类型**：`str`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    exclude-newer = "2006-12-02T02:07:43Z"
    ```

=== "uv.toml"

    ```toml
    [pip]
    exclude-newer = "2006-12-02T02:07:43Z"
    ```

---

### [`exclude-newer-package`](#pip_exclude-newer-package) {: #pip_exclude-newer-package }
<span id="exclude-newer-package"></span>

将特定包的候选包限制为在给定日期之前上传的版本。

接受 `PACKAGE = "DATE"` 对的字典格式，其中 `DATE` 是 RFC 3339 时间戳（例如 `2006-12-02T02:07:43Z`）、"友好"时长（例如 `24 hours`、`1 week`、`30 days`）或 ISO 8601 时长（例如 `PT24H`、`P7D`、`P30D`）。

时长不遵循本地时区的语义，始终以一天为 24 小时解析为固定秒数（例如，忽略夏令时转换）。不允许使用月和年等日历单位。

将包设置为 `false` 可使其完全不受全局 [`exclude-newer`](#exclude-newer) 约束的影响。

**默认值**：`None`

**类型**：`dict`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    exclude-newer-package = { tqdm = "2022-04-04T00:00:00Z", markupsafe = false }
    ```

=== "uv.toml"

    ```toml
    [pip]
    exclude-newer-package = { tqdm = "2022-04-04T00:00:00Z", markupsafe = false }
    ```

---

### [`extra`](#pip_extra) {: #pip_extra }
<span id="extra"></span>

包含来自指定 extra 的可选依赖项；可以多次提供。

仅适用于 `pyproject.toml`、`setup.py` 和 `setup.cfg` 源。

**默认值**：`[]`

**类型**：`list[str]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    extra = ["dev", "docs"]
    ```

=== "uv.toml"

    ```toml
    [pip]
    extra = ["dev", "docs"]
    ```

---

### [`extra-build-dependencies`](#pip_extra-build-dependencies) {: #pip_extra-build-dependencies }
<span id="extra-build-dependencies"></span>

包的额外构建依赖项。

这允许使用额外的包来扩展项目依赖项的 PEP 517 构建环境。这对于那些假定存在某些包（如 `pip`）但未将其声明为构建依赖项的包非常有用。

**默认值**：`[]`

**类型**：`dict`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    extra-build-dependencies = { pytest = ["setuptools"] }
    ```

=== "uv.toml"

    ```toml
    [pip]
    extra-build-dependencies = { pytest = ["setuptools"] }
    ```

---

### [`extra-build-variables`](#pip_extra-build-variables) {: #pip_extra-build-variables }
<span id="extra-build-variables"></span>

构建特定包时设置的额外环境变量。

构建指定包时，环境变量将被添加到构建环境中。

**默认值**：`{}`

**类型**：`dict[str, dict[str, str]]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    extra-build-variables = { flash-attn = { FLASH_ATTENTION_SKIP_CUDA_BUILD = "TRUE" } }
    ```

=== "uv.toml"

    ```toml
    [pip]
    extra-build-variables = { flash-attn = { FLASH_ATTENTION_SKIP_CUDA_BUILD = "TRUE" } }
    ```

---

### [`extra-index-url`](#pip_extra-index-url) {: #pip_extra-index-url }
<span id="extra-index-url"></span>

除 `--index-url` 之外使用的额外包索引 URL。

接受符合 [PEP 503](https://peps.python.org/pep-0503/)（简单仓库 API）的仓库，或以相同格式组织的本地目录。

通过此标志提供的所有索引优先级高于 [`index_url`](#index-url) 指定的索引。当提供多个索引时，较早的值优先级更高。

要控制多个索引存在时 uv 的解析策略，请参阅 [`index_strategy`](#index-strategy)。

**默认值**：`[]`

**类型**：`list[str]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    extra-index-url = ["https://download.pytorch.org/whl/cpu"]
    ```

=== "uv.toml"

    ```toml
    [pip]
    extra-index-url = ["https://download.pytorch.org/whl/cpu"]
    ```

---

### [`find-links`](#pip_find-links) {: #pip_find-links }
<span id="find-links"></span>

除注册表索引中找到的之外，用于搜索候选分发包的位置。

如果是路径，目标必须是一个目录，其中包含顶层为 wheel 文件（`.whl`）或源分发包（例如 `.tar.gz` 或 `.zip`）的包。

如果是 URL，页面必须包含指向符合上述格式的包文件的扁平链接列表。

**默认值**：`[]`

**类型**：`list[str]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    find-links = ["https://download.pytorch.org/whl/torch_stable.html"]
    ```

=== "uv.toml"

    ```toml
    [pip]
    find-links = ["https://download.pytorch.org/whl/torch_stable.html"]
    ```

---

### [`fork-strategy`](#pip_fork-strategy) {: #pip_fork-strategy }
<span id="fork-strategy"></span>

在跨 Python 版本和平台时为给定包选择多个版本所使用的策略。

默认情况下，uv 会优化为每个受支持的 Python 版本（`requires-python`）选择每个包的最新版本，同时最小化跨平台选择的版本数量。

在 `fewest` 策略下，uv 将最小化每个包选择的版本数量，优先选择与更广泛受支持的 Python 版本或平台兼容的旧版本。

**默认值**：`"requires-python"`

**可选值**：

- `"fewest"`：优化为每个包选择最少数量的版本。如果旧版本与更广泛受支持的 Python 版本或平台兼容，可能会被优先选择
- `"requires-python"`：优化为每个受支持的 Python 版本选择每个包的最新支持版本

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    fork-strategy = "fewest"
    ```

=== "uv.toml"

    ```toml
    [pip]
    fork-strategy = "fewest"
    ```

---

### [`generate-hashes`](#pip_generate-hashes) {: #pip_generate-hashes }
<span id="generate-hashes"></span>

在输出文件中包含分发包哈希。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    generate-hashes = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    generate-hashes = true
    ```

---

### [`group`](#pip_group) {: #pip_group }
<span id="group"></span>

包含以下依赖组。

**默认值**：`None`

**类型**：`list[str]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    group = ["dev", "docs"]
    ```

=== "uv.toml"

    ```toml
    [pip]
    group = ["dev", "docs"]
    ```

---

### [`index-strategy`](#pip_index-strategy) {: #pip_index-strategy }
<span id="index-strategy"></span>

针对多个索引 URL 进行解析时使用的策略。

默认情况下，uv 会在找到给定包的第一个索引处停止，并将解析结果限制在该第一个索引上存在的版本（`first-index`）。这可以防止"依赖混淆"攻击，即攻击者可以在替代索引上上传同名的恶意包。

**默认值**：`"first-index"`

**可选值**：

- `"first-index"`：仅使用第一个返回给定包名匹配项的索引的结果
- `"unsafe-first-match"`：在所有索引中搜索每个包名，在移向下一个索引之前穷尽第一个索引的版本
- `"unsafe-best-match"`：在所有索引中搜索每个包名，优先选择找到的"最佳"版本。如果某个包版本存在于多个索引中，则仅查看第一个索引的条目

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    index-strategy = "unsafe-best-match"
    ```

=== "uv.toml"

    ```toml
    [pip]
    index-strategy = "unsafe-best-match"
    ```

---

### [`index-url`](#pip_index-url) {: #pip_index-url }
<span id="index-url"></span>

Python 包索引的 URL（默认：<https://pypi.org/simple>）。

接受符合 [PEP 503](https://peps.python.org/pep-0503/)（简单仓库 API）的仓库，或以相同格式组织的本地目录。

此设置提供的索引优先级低于通过 [`extra_index_url`](#extra-index-url) 指定的任何索引。

**默认值**：`"https://pypi.org/simple"`

**类型**：`str`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    index-url = "https://test.pypi.org/simple"
    ```

=== "uv.toml"

    ```toml
    [pip]
    index-url = "https://test.pypi.org/simple"
    ```

---

### [`keyring-provider`](#pip_keyring-provider) {: #pip_keyring-provider }
<span id="keyring-provider"></span>

尝试使用 `keyring` 进行索引 URL 的身份验证。

目前仅支持 `--keyring-provider subprocess`，它配置 uv 使用 `keyring` CLI 来处理身份验证。

**默认值**：`disabled`

**类型**：`str`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    keyring-provider = "subprocess"
    ```

=== "uv.toml"

    ```toml
    [pip]
    keyring-provider = "subprocess"
    ```

---

### [`link-mode`](#pip_link-mode) {: #pip_link-mode }
<span id="link-mode"></span>

从全局缓存安装包时使用的方法。

在 macOS 和 Linux 上默认为 `clone`（也称为写时复制，Copy-on-Write），在 Windows 上默认为 `hardlink`。

警告：不鼓励使用 symlink 链接模式，因为它会在缓存和目标环境之间创建紧密耦合。例如，清除缓存（`uv cache clean`）将通过移除底层源文件而破坏所有已安装的包。请谨慎使用 symlink。

**默认值**：`"clone"`（macOS、Linux）或 `"hardlink"`（Windows）

**可选值**：

- `"clone"`：将包从源克隆（即写时复制，Copy-on-Write）到目标
- `"copy"`：将包从源复制到目标
- `"hardlink"`：将包从源硬链接到目标
- `"symlink"`：将包从源符号链接到目标

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    link-mode = "copy"
    ```

=== "uv.toml"

    ```toml
    [pip]
    link-mode = "copy"
    ```

---

### [`no-annotate`](#pip_no-annotate) {: #pip_no-annotate }
<span id="no-annotate"></span>

从 `uv pip compile` 生成的输出文件中排除指示每个包来源的注释标注。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    no-annotate = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    no-annotate = true
    ```

---

### [`no-binary`](#pip_no-binary) {: #pip_no-binary }
<span id="no-binary"></span>

不安装预构建的 wheel。

给定的包将从源代码构建和安装。解析器仍将使用预构建的 wheel 来提取包元数据（如果可用）。

可以指定多个包。使用 `:all:` 禁用所有包的二进制文件。使用 `:none:` 清除之前指定的包。

**默认值**：`[]`

**类型**：`list[str]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    no-binary = ["ruff"]
    ```

=== "uv.toml"

    ```toml
    [pip]
    no-binary = ["ruff"]
    ```

---

### [`no-build`](#pip_no-build) {: #pip_no-build }
<span id="no-build"></span>

不构建源分发包。

启用后，解析将不会运行任意 Python 代码。已构建的源分发包的缓存 wheel 将被重用，但需要构建分发包的操作将以错误退出。

是 `--only-binary :all:` 的别名。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    no-build = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    no-build = true
    ```

---

### [`no-build-isolation`](#pip_no-build-isolation) {: #pip_no-build-isolation }
<span id="no-build-isolation"></span>

构建源分发包时禁用隔离。

假定 [PEP 518](https://peps.python.org/pep-0518/) 指定的构建依赖项已经安装。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    no-build-isolation = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    no-build-isolation = true
    ```

---

### [`no-build-isolation-package`](#pip_no-build-isolation-package) {: #pip_no-build-isolation-package }
<span id="no-build-isolation-package"></span>

为特定包构建源分发包时禁用隔离。

假定这些包的 [PEP 518](https://peps.python.org/pep-0518/) 指定的构建依赖项已经安装。

**默认值**：`[]`

**类型**：`list[str]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    no-build-isolation-package = ["package1", "package2"]
    ```

=== "uv.toml"

    ```toml
    [pip]
    no-build-isolation-package = ["package1", "package2"]
    ```

---

### [`no-deps`](#pip_no-deps) {: #pip_no-deps }
<span id="no-deps"></span>

忽略包依赖项，仅将命令行上显式列出的包添加到生成的 requirements 文件中。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    no-deps = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    no-deps = true
    ```

---

### [`no-emit-package`](#pip_no-emit-package) {: #pip_no-emit-package }
<span id="no-emit-package"></span>

指定要从输出解析结果中省略的包。其依赖项仍将包含在解析结果中。等同于 pip-compile 的 `--unsafe-package` 选项。

**默认值**：`[]`

**类型**：`list[str]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    no-emit-package = ["ruff"]
    ```

=== "uv.toml"

    ```toml
    [pip]
    no-emit-package = ["ruff"]
    ```

---

### [`no-extra`](#pip_no-extra) {: #pip_no-extra }
<span id="no-extra"></span>

如果提供了 `all-extras`，则排除指定的可选依赖项。

**默认值**：`[]`

**类型**：`list[str]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    all-extras = true
    no-extra = ["dev", "docs"]
    ```

=== "uv.toml"

    ```toml
    [pip]
    all-extras = true
    no-extra = ["dev", "docs"]
    ```

---

### [`no-header`](#pip_no-header) {: #pip_no-header }
<span id="no-header"></span>

从 `uv pip compile` 生成的输出文件顶部排除注释标题。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    no-header = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    no-header = true
    ```

---

### [`no-index`](#pip_no-index) {: #pip_no-index }
<span id="no-index"></span>

忽略所有注册表索引（例如 PyPI），改为依赖直接 URL 依赖项和通过 `--find-links` 提供的依赖项。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    no-index = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    no-index = true
    ```

---

### [`no-sources`](#pip_no-sources) {: #pip_no-sources }
<span id="no-sources"></span>

解析依赖项时忽略 `tool.uv.sources` 表。用于根据符合标准的、可发布的包元数据进行锁定，而不是使用任何本地或 Git 源。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    no-sources = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    no-sources = true
    ```

---

### [`no-sources-package`](#pip_no-sources-package) {: #pip_no-sources-package }
<span id="no-sources-package"></span>

忽略指定包的 `tool.uv.sources`。

**默认值**：`[]`

**类型**：`list[str]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    no-sources-package = ["ruff"]
    ```

=== "uv.toml"

    ```toml
    [pip]
    no-sources-package = ["ruff"]
    ```

---

### [`no-strip-extras`](#pip_no-strip-extras) {: #pip_no-strip-extras }
<span id="no-strip-extras"></span>

在输出文件中包含 extras。

默认情况下，uv 会去除 extras，因为 extras 引入的任何包已经作为依赖项直接包含在输出文件中。此外，使用 `--no-strip-extras` 生成的输出文件不能用作 `install` 和 `sync` 调用中的约束文件。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    no-strip-extras = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    no-strip-extras = true
    ```

---

### [`no-strip-markers`](#pip_no-strip-markers) {: #pip_no-strip-markers }
<span id="no-strip-markers"></span>

在 `uv pip compile` 生成的输出文件中包含环境标记（environment markers）。

默认情况下，uv 会去除环境标记，因为 `compile` 生成的解析结果仅保证对目标环境正确。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    no-strip-markers = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    no-strip-markers = true
    ```

---

### [`only-binary`](#pip_only-binary) {: #pip_only-binary }
<span id="only-binary"></span>

仅使用预构建的 wheel；不构建源分发包。

启用后，解析将不会运行给定包的代码。已构建的源分发包的缓存 wheel 将被重用，但需要构建分发包的操作将以错误退出。

可以指定多个包。使用 `:all:` 禁用所有包的二进制文件。使用 `:none:` 清除之前指定的包。

**默认值**：`[]`

**类型**：`list[str]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    only-binary = ["ruff"]
    ```

=== "uv.toml"

    ```toml
    [pip]
    only-binary = ["ruff"]
    ```

---

### [`output-file`](#pip_output-file) {: #pip_output-file }
<span id="output-file"></span>

将 `uv pip compile` 生成的 requirements 写入给定的 `requirements.txt` 文件。

如果文件已存在，在解析依赖项时将优先使用现有版本，除非同时指定了 `--upgrade`。

**默认值**：`None`

**类型**：`str`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    output-file = "requirements.txt"
    ```

=== "uv.toml"

    ```toml
    [pip]
    output-file = "requirements.txt"
    ```

---

### [`prefix`](#pip_prefix) {: #pip_prefix }
<span id="prefix"></span>

将包安装到指定目录下的 `lib`、`bin` 和其他顶层文件夹中，就像在该位置存在虚拟环境一样。

通常，建议使用 `--python` 来安装到替代环境中，因为通过 `--prefix` 安装的脚本和其他构件将引用安装的解释器，而不是添加到 `--prefix` 目录中的任何解释器，导致它们不可移植。

**默认值**：`None`

**类型**：`str`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    prefix = "./prefix"
    ```

=== "uv.toml"

    ```toml
    [pip]
    prefix = "./prefix"
    ```

---

### [`prerelease`](#pip_prerelease) {: #pip_prerelease }
<span id="prerelease"></span>

考虑预发布版本时使用的策略。

默认情况下，uv 将接受那些*仅*发布预发布版本的包的预发布版本，以及在声明的约束符中包含显式预发布标记的第一方需求（`if-necessary-or-explicit`）。

**默认值**：`"if-necessary-or-explicit"`

**可选值**：

- `"disallow"`：禁止所有预发布版本
- `"allow"`：允许所有预发布版本
- `"if-necessary"`：如果包的所有版本都是预发布版本，则允许预发布版本
- `"explicit"`：对于版本需求中包含显式预发布标记的第一方包，允许预发布版本
- `"if-necessary-or-explicit"`：如果包的所有版本都是预发布版本，或者包的版本需求中包含显式预发布标记，则允许预发布版本

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    prerelease = "allow"
    ```

=== "uv.toml"

    ```toml
    [pip]
    prerelease = "allow"
    ```

---

### [`python`](#pip_python) {: #pip_python }
<span id="python"></span>

包应安装到的 Python 解释器。

默认情况下，uv 安装到当前工作目录或任何父目录中的虚拟环境。`--python` 选项允许您指定不同的解释器，旨在用于持续集成（CI）环境或其他自动化工作流。

支持的格式：
- `3.10` 在 Windows 上查找注册表中已安装的 Python 3.10（参见 `py --list-paths`），或在 Linux 和 macOS 上查找 `python3.10`。
- `python3.10` 或 `python.exe` 在 `PATH` 中查找具有给定名称的二进制文件。
- `/home/ferris/.local/bin/python3.10` 使用给定路径的精确 Python。

**默认值**：`None`

**类型**：`str`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    python = "3.10"
    ```

=== "uv.toml"

    ```toml
    [pip]
    python = "3.10"
    ```

---

### [`python-platform`](#pip_python-platform) {: #pip_python-platform }
<span id="python-platform"></span>

应为其解析需求的目标平台。

表示为"目标三元组"，一个描述目标平台的字符串，包括其 CPU、供应商和操作系统名称，如 `x86_64-unknown-linux-gnu` 或 `aarch64-apple-darwin`。

**默认值**：`None`

**类型**：`str`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    python-platform = "x86_64-unknown-linux-gnu"
    ```

=== "uv.toml"

    ```toml
    [pip]
    python-platform = "x86_64-unknown-linux-gnu"
    ```

---

### [`python-version`](#pip_python-version) {: #pip_python-version }
<span id="python-version"></span>

已解析的需求应支持的最低 Python 版本（例如 `3.8` 或 `3.8.17`）。

如果省略补丁版本，则假定为最低补丁版本。例如，`3.8` 映射为 `3.8.0`。

**默认值**：`None`

**类型**：`str`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    python-version = "3.8"
    ```

=== "uv.toml"

    ```toml
    [pip]
    python-version = "3.8"
    ```

---

### [`reinstall`](#pip_reinstall) {: #pip_reinstall }
<span id="reinstall"></span>

重新安装所有包，无论它们是否已安装。隐含 `refresh`。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    reinstall = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    reinstall = true
    ```

---

### [`reinstall-package`](#pip_reinstall-package) {: #pip_reinstall-package }
<span id="reinstall-package"></span>

重新安装特定包，无论它是否已安装。隐含 `refresh-package`。

**默认值**：`[]`

**类型**：`list[str]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    reinstall-package = ["ruff"]
    ```

=== "uv.toml"

    ```toml
    [pip]
    reinstall-package = ["ruff"]
    ```

---

### [`require-hashes`](#pip_require-hashes) {: #pip_require-hashes }
<span id="require-hashes"></span>

要求每个需求都有匹配的哈希。

哈希检查模式是全有或全无的。如果启用，*所有*需求必须提供相应的哈希或哈希集。此外，如果启用，*所有*需求必须要么被固定到精确版本（例如 `==1.0.0`），要么通过直接 URL 指定。

哈希检查模式引入了若干额外限制：

- 不支持 Git 依赖项。
- 不支持可编辑安装。
- 不支持本地依赖项，除非它们指向特定的 wheel（`.whl`）或源归档文件（`.zip`、`.tar.gz`），而不是目录。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    require-hashes = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    require-hashes = true
    ```

---

### [`resolution`](#pip_resolution) {: #pip_resolution }
<span id="resolution"></span>

在给定包需求的不同兼容版本之间进行选择时使用的策略。

默认情况下，uv 将使用每个包的最新兼容版本（`highest`）。

**默认值**：`"highest"`

**可选值**：

- `"highest"`：解析每个包的最高兼容版本
- `"lowest"`：解析每个包的最低兼容版本
- `"lowest-direct"`：解析任何直接依赖项的最低兼容版本，以及任何传递依赖项的最高兼容版本

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    resolution = "lowest-direct"
    ```

=== "uv.toml"

    ```toml
    [pip]
    resolution = "lowest-direct"
    ```

---

### [`strict`](#pip_strict) {: #pip_strict }
<span id="strict"></span>

验证 Python 环境，以检测缺少依赖项的包和其他问题。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    strict = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    strict = true
    ```

---

### [`system`](#pip_system) {: #pip_system }
<span id="system"></span>

将包安装到系统 Python 环境中。

默认情况下，uv 安装到当前工作目录或任何父目录中的虚拟环境。`--system` 选项指示 uv 改为使用系统 `PATH` 中找到的第一个 Python。

警告：`--system` 旨在用于持续集成（CI）环境中，应谨慎使用，因为它可能会修改系统 Python 安装。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    system = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    system = true
    ```

---

### [`target`](#pip_target) {: #pip_target }
<span id="target"></span>

将包安装到指定目录中，而不是安装到虚拟环境或系统 Python 环境中。包将安装在该目录的顶层。

**默认值**：`None`

**类型**：`str`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    target = "./target"
    ```

=== "uv.toml"

    ```toml
    [pip]
    target = "./target"
    ```

---

### [`torch-backend`](#pip_torch-backend) {: #pip_torch-backend }
<span id="torch-backend"></span>

获取 PyTorch 生态系统中的包时使用的后端。

设置后，uv 将忽略为 PyTorch 生态系统中的包配置的索引 URL，而使用定义的后端。

例如，当设置为 `cpu` 时，uv 将使用仅 CPU 的 PyTorch 索引；当设置为 `cu126` 时，uv 将使用适用于 CUDA 12.6 的 PyTorch 索引。

`auto` 模式将尝试根据当前安装的 CUDA 驱动程序检测适当的 PyTorch 索引。

此设置仅对 `uv pip` 命令生效。

此选项为预览功能，在未来的任何版本中都可能发生变化。

**默认值**：`null`

**类型**：`str`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    torch-backend = "auto"
    ```

=== "uv.toml"

    ```toml
    [pip]
    torch-backend = "auto"
    ```

---

### [`universal`](#pip_universal) {: #pip_universal }
<span id="universal"></span>

执行通用解析，尝试生成一个与所有操作系统、架构和 Python 实现兼容的单一 `requirements.txt` 输出文件。

在通用模式下，当前 Python 版本（或用户提供的 `--python-version`）将被视为下限。例如，`--universal --python-version 3.7` 将生成适用于 Python 3.7 及更高版本的通用解析。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    universal = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    universal = true
    ```

---

### [`upgrade`](#pip_upgrade) {: #pip_upgrade }
<span id="upgrade"></span>

允许包升级，忽略任何现有输出文件中的固定版本。

**默认值**：`false`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    upgrade = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    upgrade = true
    ```

---

### [`upgrade-package`](#pip_upgrade-package) {: #pip_upgrade-package }
<span id="upgrade-package"></span>

允许特定包升级，忽略任何现有输出文件中的固定版本。

接受独立的包名（`ruff`）和版本约束符（`ruff<0.5.0`）。

**默认值**：`[]`

**类型**：`list[str]`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    upgrade-package = ["ruff"]
    ```

=== "uv.toml"

    ```toml
    [pip]
    upgrade-package = ["ruff"]
    ```

---

### [`verify-hashes`](#pip_verify-hashes) {: #pip_verify-hashes }
<span id="verify-hashes"></span>

验证 requirements 文件中提供的任何哈希。

与 `--require-hashes` 不同，`--verify-hashes` 不要求所有需求都有哈希；相反，它仅验证那些确实包含哈希的需求。

**默认值**：`true`

**类型**：`bool`

**使用示例**：

=== "pyproject.toml"

    ```toml
    [tool.uv.pip]
    verify-hashes = true
    ```

=== "uv.toml"

    ```toml
    [pip]
    verify-hashes = true
    ```