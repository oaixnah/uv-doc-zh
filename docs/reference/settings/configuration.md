---
subtitle: Configuration
---

## 配置

### [`add-bounds`](#add-bounds) {: #add-bounds }

添加依赖时的默认版本说明符。

当向项目添加依赖时，如果没有提供约束或 URL，会基于包的最新兼容版本添加约束。默认情况下，使用下界约束，例如 `>=1.2.3`。

当提供 `--frozen` 时，不执行解析，依赖总是在没有约束的情况下添加。

此选项处于预览状态，可能在未来的任何版本中发生变化。

**默认值**: `"lower"`

**可能的值**:

- `"lower"`: 仅下界，例如 `>=1.2.3`
- `"major"`: 允许相同的主版本，类似于 semver 插入符号，例如 `>=1.2.3, <2.0.0`
- `"minor"`: 允许相同的次版本，类似于 semver 波浪号，例如 `>=1.2.3, <1.3.0`
- `"exact"`: 固定确切版本，例如 `==1.2.3`

**Example usage**:

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

### [`allow-insecure-host`](#allow-insecure-host) {: #allow-insecure-host }

允许与主机的不安全连接。

期望接收主机名（例如 `localhost`）、主机端口对（例如 `localhost:8080`）或 URL（例如 `https://localhost`）。

警告：此列表中包含的主机将不会根据系统的证书存储进行验证。仅在具有已验证源的安全网络中使用 `--allow-insecure-host`，因为它绕过了 SSL 验证，可能使您暴露于中间人攻击。

**默认值**: `[]`

**类型**: `list[str]`

**Example usage**:

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

### [`cache-dir`](#cache-dir) {: #cache-dir }

缓存目录的路径。

在 Linux 和 macOS 上默认为 `$XDG_CACHE_HOME/uv` 或 `$HOME/.cache/uv`，在 Windows 上为 `%LOCALAPPDATA%\uv\cache`。

**默认值**: `None`

**类型**: `str`

**Example usage**:

=== "pyproject.toml"

    ```toml
    [tool.uv]
    cache-dir = "./.uv_cache"
    ```

=== "uv.toml"

    ```toml
    cache-dir = "./.uv_cache"
    ```

---

### [`cache-keys`](#cache-keys) {: #cache-keys }

为项目缓存构建时要考虑的键。

缓存键使您能够指定在修改时应触发重建的文件或目录。默认情况下，当项目目录中的 `pyproject.toml`、`setup.py` 或 `setup.cfg` 文件被修改，或者添加或删除 `src` 目录时，uv 将重建项目，即：

```toml
cache-keys = [{ file = "pyproject.toml" }, { file = "setup.py" }, { file = "setup.cfg" }, { dir = "src" }]
```

举个例子：如果项目使用动态元数据从 `requirements.txt` 文件读取其依赖项，您可以指定 `cache-keys = [{ file = "requirements.txt" }, { file = "pyproject.toml" }]` 以确保在修改 `requirements.txt` 文件时重建项目（除了监视 `pyproject.toml`）。

支持 Glob 模式，遵循 [`glob`](https://docs.rs/glob/0.3.1/glob/struct.Pattern.html) crate 的语法。例如，要在项目目录或其任何子目录中的 `.toml` 文件被修改时使缓存失效，您可以指定 `cache-keys = [{ file = "**/*.toml" }]`。请注意，使用 glob 可能会很昂贵，因为 uv 可能需要遍历文件系统来确定是否有任何文件发生了变化。

缓存键还可以包含版本控制信息。例如，如果项目使用 `setuptools_scm` 从 Git 提交读取其版本，您可以指定 `cache-keys = [{ git = { commit = true }, { file = "pyproject.toml" }]` 以在缓存键中包含当前 Git 提交哈希（除了 `pyproject.toml`）。Git 标签也通过 `cache-keys = [{ git = { commit = true, tags = true } }]` 支持。

缓存键还可以包含环境变量。例如，如果项目依赖 `MACOSX_DEPLOYMENT_TARGET` 或其他环境变量来确定其行为，您可以指定 `cache-keys = [{ env = "MACOSX_DEPLOYMENT_TARGET" }]` 以在环境变量更改时使缓存失效。

缓存键仅影响由指定它们的 `pyproject.toml` 定义的项目（而不是例如影响工作空间中的所有成员），所有路径和 glob 都被解释为相对于项目目录。

**默认值**: `[{ file = "pyproject.toml" }, { file = "setup.py" }, { file = "setup.cfg" }]`

**类型**: `list[dict]`

**Example usage**:

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

### [`check-url`](#check-url) {: #check-url }

检查索引 URL 中的现有文件以跳过重复上传。

此选项允许重试在仅上传了部分文件而非全部文件后失败的发布，并处理由于并行上传相同文件而导致的错误。

在上传之前，会检查索引。如果索引中已经存在完全相同的文件，则不会上传该文件。如果在上传过程中发生错误，会再次检查索引，以处理相同文件被并行上传两次的情况。

确切的行为会根据索引而有所不同。当上传到 PyPI 时，即使没有 `--check-url`，上传相同文件也会成功，而大多数其他索引会出错。

索引必须提供支持的哈希之一（SHA-256、SHA-384 或 SHA-512）。

**默认值**: `None`

**类型**: `str`

**Example usage**:

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

### [`compile-bytecode`](#compile-bytecode) {: #compile-bytecode }

安装后将 Python 文件编译为字节码。

默认情况下，uv 不会将 Python（`.py`）文件编译为字节码（`__pycache__/*.pyc`）；相反，编译在第一次导入模块时延迟执行。对于启动时间至关重要的用例，如 CLI 应用程序和 Docker 容器，可以启用此选项以用更长的安装时间换取更快的启动时间。

启用时，uv 将处理整个 site-packages 目录（包括当前操作未修改的包）以保持一致性。像 pip 一样，它也会忽略错误。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

### [`concurrent-builds`](#concurrent-builds) {: #concurrent-builds }

uv 在任何给定时间将并发构建的源分发的最大数量。

默认为可用 CPU 核心数。

**默认值**: `None`

**类型**: `int`

**Example usage**:

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

### [`concurrent-downloads`](#concurrent-downloads) {: #concurrent-downloads }

uv 在任何给定时间将执行的正在进行的并发下载的最大数量。

**默认值**: `50`

**类型**: `int`

**Example usage**:

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

### [`concurrent-installs`](#concurrent-installs) {: #concurrent-installs }

安装和解压包时使用的线程数。

默认为可用 CPU 核心数。

**默认值**: `None`

**类型**: `int`

**Example usage**:

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

### [`config-settings`](#config-settings) {: #config-settings }

传递给 [PEP 517](https://peps.python.org/pep-0517/) 构建后端的设置，指定为 `KEY=VALUE` 对。

**默认值**: `{}`

**类型**: `dict`

**Example usage**:

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

### [`dependency-metadata`](#dependency-metadata) {: #dependency-metadata }

项目依赖项（直接或传递）的预定义静态元数据。提供时，使解析器能够使用指定的元数据，而不是查询注册表或从源构建相关包。

元数据应遵循 [Metadata 2.3](https://packaging.python.org/en/latest/specifications/core-metadata/) 标准提供，但仅遵循以下字段：

- `name`: 包的名称。
- （可选）`version`: 包的版本。如果省略，元数据将应用于包的所有版本。
- （可选）`requires-dist`: 包的依赖项（例如 `werkzeug>=0.14`）。
- （可选）`requires-python`: 包所需的 Python 版本（例如 `>=3.10`）。
- （可选）`provides-extras`: 包提供的额外功能。

**默认值**: `[]`

**类型**: `list[dict]`

**Example usage**:

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

### [`exclude-newer`](#exclude-newer) {: #exclude-newer }

将候选包限制为在给定时间点之前上传的包。

接受 [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339.html) 的超集（例如 `2006-12-02T02:07:43Z`）。需要完整的时间戳以确保解析器在不同时区中行为一致。

**默认值**: `None`

**类型**: `str`

**Example usage**:

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

### [`extra-index-url`](#extra-index-url) {: #extra-index-url }

除了 `--index-url` 之外要使用的包索引的额外 URL。

接受符合 [PEP 503](https://peps.python.org/pep-0503/)（简单存储库 API）的存储库，或以相同格式布局的本地目录。

通过此标志提供的所有索引优先于由 [`index_url`](#index-url) 或 [`index`](#index) 指定的索引（`default = true`）。当提供多个索引时，较早的值优先。

要控制存在多个索引时 uv 的解析策略，请参阅 [`index_strategy`](#index-strategy)。

（已弃用：请使用 `index` 代替。）

**默认值**: `[]`

**类型**: `list[str]`

**Example usage**:

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

### [`find-links`](#find-links) {: #find-links }

除了在注册表索引中找到的候选分发之外，要搜索候选分发的位置。

如果是路径，目标必须是在顶层包含作为 wheel 文件（`.whl`）或源分发（例如 `.tar.gz` 或 `.zip`）的包的目录。

如果是 URL，页面必须包含指向符合上述格式的包文件的平面链接列表。

**默认值**: `[]`

**类型**: `list[str]`

**Example usage**:

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

### [`fork-strategy`](#fork-strategy) {: #fork-strategy }

在跨 Python 版本和平台选择给定包的多个版本时使用的策略。

默认情况下，uv 将优化为每个支持的 Python 版本（`requires-python`）选择每个包的最新版本，同时最小化跨平台选择的版本数量。

在 `fewest` 下，uv 将最小化每个包的选择版本数量，偏好与更广泛的支持 Python 版本或平台兼容的较旧版本。

**默认值**: `"requires-python"`

**可能的值**:

- `"fewest"`: 优化为每个包选择最少的版本数量。如果较旧版本与更广泛的支持 Python 版本或平台兼容，可能会偏好较旧版本
- `"requires-python"`: 优化为每个支持的 Python 版本选择每个包的最新支持版本

**Example usage**:

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

### [`index`](#index) {: #index }

解析依赖项时要使用的包索引。

接受符合 [PEP 503](https://peps.python.org/pep-0503/)（简单存储库 API）的存储库，或以相同格式布局的本地目录。

索引按定义顺序考虑，因此第一个定义的索引具有最高优先级。此外，此设置提供的索引比通过 [`index_url`](#index-url) 或 [`extra_index_url`](#extra-index-url) 指定的任何索引具有更高的优先级。uv 只会考虑包含给定包的第一个索引，除非指定了替代的[索引策略](#index-strategy)。

如果索引标记为 `explicit = true`，它将专门用于通过 `[tool.uv.sources]` 明确选择它的依赖项，如：

```toml
[[tool.uv.index]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cu121"
explicit = true

[tool.uv.sources]
torch = { index = "pytorch" }
```

如果索引标记为 `default = true`，它将被移动到优先级列表的末尾，因此在解析包时被赋予最低优先级。此外，将索引标记为默认将禁用 PyPI 默认索引。

**默认值**: `"[]"`

**类型**: `dict`

**Example usage**:

=== "pyproject.toml"

    ```toml
    [[tool.uv.index]]
    name = "pytorch"
    url = "https://download.pytorch.org/whl/cu121"
    ```

=== "uv.toml"

    ```toml
    [[tool.uv.index]]
    name = "pytorch"
    url = "https://download.pytorch.org/whl/cu121"
    ```

---

### [`index-strategy`](#index-strategy) {: #index-strategy }

针对多个索引 URL 进行解析时使用的策略。

默认情况下，uv 将在给定包可用的第一个索引处停止，并将解析限制为该第一个索引上存在的包（`first-index`）。这可以防止"依赖混淆"攻击，攻击者可以在备用索引中上传同名的恶意包。

**默认值**: `"first-index"`

**可能的值**:

- `"first-index"`: 仅使用第一个返回给定包名匹配的索引的结果
- `"unsafe-first-match"`: 在所有索引中搜索每个包名，在移动到下一个索引之前耗尽第一个索引的版本
- `"unsafe-best-match"`: 在所有索引中搜索每个包名，偏好找到的"最佳"版本。如果包版本在多个索引中，仅查看第一个索引的条目

**Example usage**:

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

### [`index-url`](#index-url) {: #index-url }

Python 包索引的 URL（默认：<https://pypi.org/simple>）。

接受符合 [PEP 503](https://peps.python.org/pep-0503/)（简单存储库 API）的存储库，或以相同格式布局的本地目录。

此设置提供的索引比通过 [`extra_index_url`](#extra-index-url) 或 [`index`](#index) 指定的任何索引具有更低的优先级。

（已弃用：请使用 `index` 代替。）

**默认值**: `"https://pypi.org/simple"`

**类型**: `str`

**Example usage**:

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

### [`keyring-provider`](#keyring-provider) {: #keyring-provider }

尝试使用 `keyring` 对索引 URL 进行身份验证。

目前，仅支持 `--keyring-provider subprocess`，它配置 uv 使用 `keyring` CLI 来处理身份验证。

**默认值**: `"disabled"`

**类型**: `str`

**Example usage**:

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

### [`link-mode`](#link-mode) {: #link-mode }

从全局缓存安装包时使用的方法。

在 macOS 上默认为 `clone`（也称为写时复制），在 Linux 和 Windows 上为 `hardlink`。

**默认值**: `"clone"（macOS）或 "hardlink"（Linux、Windows）`

**可能的值**:

- `"clone"`: 从 wheel 克隆（即写时复制）包到 `site-packages` 目录
- `"copy"`: 从 wheel 复制包到 `site-packages` 目录
- `"hardlink"`: 从 wheel 硬链接包到 `site-packages` 目录
- `"symlink"`: 从 wheel 符号链接包到 `site-packages` 目录

**Example usage**:

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

### [`native-tls`](#native-tls) {: #native-tls }

是否从平台的本机证书存储加载 TLS 证书。

默认情况下，uv 从捆绑的 `webpki-roots` crate 加载证书。`webpki-roots` 是来自 Mozilla 的一组可靠的信任根，在 uv 中包含它们可以提高可移植性和性能（特别是在 macOS 上）。

但是，在某些情况下，您可能希望使用平台的本机证书存储，特别是如果您依赖于系统证书存储中包含的企业信任根（例如，用于强制代理）。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

=== "pyproject.toml"

    ```toml
    [tool.uv]
    native-tls = true
    ```

=== "uv.toml"

    ```toml
    native-tls = true
    ```

---

### [`no-binary`](#no-binary) {: #no-binary }

不安装预构建的 wheel。

给定的包将从源代码构建和安装。如果可用，解析器仍将使用预构建的 wheel 来提取包元数据。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

### [`no-binary-package`](#no-binary-package) {: #no-binary-package }

不为特定包安装预构建的 wheel。

**默认值**: `[]`

**类型**: `list[str]`

**Example usage**:

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

### [`no-build`](#no-build) {: #no-build }

不构建源分发。

启用时，解析将不会运行任意 Python 代码。已构建源分发的缓存 wheel 将被重用，但需要构建分发的操作将以错误退出。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

### [`no-build-isolation`](#no-build-isolation) {: #no-build-isolation }

在构建源分发时禁用隔离。

假设 [PEP 518](https://peps.python.org/pep-0518/) 指定的构建依赖项已经安装。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

### [`no-build-isolation-package`](#no-build-isolation-package) {: #no-build-isolation-package }

为特定包构建源分发时禁用隔离。

假设包的 [PEP 518](https://peps.python.org/pep-0518/) 指定的构建依赖项已经安装。

**默认值**: `[]`

**类型**: `list[str]`

**Example usage**:

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

### [`no-build-package`](#no-build-package) {: #no-build-package }

不为特定包构建源分发。

**默认值**: `[]`

**类型**: `list[str]`

**Example usage**:

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

### [`no-cache`](#no-cache) {: #no-cache }

避免从缓存读取或写入缓存，而是在操作期间使用临时目录。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

### [`no-index`](#no-index) {: #no-index }

忽略所有注册表索引（例如 PyPI），而是依赖直接 URL 依赖项和通过 `--find-links` 提供的依赖项。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

### [`no-sources`](#no-sources) {: #no-sources }

在解析依赖项时忽略 `tool.uv.sources` 表。用于锁定符合标准的、可发布的包元数据，而不是使用任何本地或 Git 源。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

### [`offline`](#offline) {: #offline }

禁用网络访问，仅依赖本地缓存数据和本地可用文件。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

### [`prerelease`](#prerelease) {: #prerelease }

考虑预发布版本时使用的策略。

默认情况下，uv 将接受仅发布预发布版本的包的预发布版本，以及在声明的说明符中包含显式预发布标记的第一方要求（`if-necessary-or-explicit`）。

**默认值**: `"if-necessary-or-explicit"`

**可能的值**:

- `"disallow"`: 禁止所有预发布版本
- `"allow"`: 允许所有预发布版本
- `"if-necessary"`: 如果包的所有版本都是预发布版本，则允许预发布版本
- `"explicit"`: 对于在其版本要求中具有显式预发布标记的第一方包，允许预发布版本
- `"if-necessary-or-explicit"`: 如果包的所有版本都是预发布版本，或者包在其版本要求中具有显式预发布标记，则允许预发布版本

**Example usage**:

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

### [`preview`](#preview) {: #preview }

是否启用实验性预览功能。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

=== "pyproject.toml"

    ```toml
    [tool.uv]
    preview = true
    ```

=== "uv.toml"

    ```toml
    preview = true
    ```

---

### [`publish-url`](#publish-url) {: #publish-url }

用于将包发布到 Python 包索引的 URL（默认：<https://upload.pypi.org/legacy/>）。

**默认值**: `"https://upload.pypi.org/legacy/"`

**类型**: `str`

**Example usage**:

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

### [`pypy-install-mirror`](#pypy-install-mirror) {: #pypy-install-mirror }

用于下载托管 PyPy 安装的镜像 URL。

默认情况下，托管 PyPy 安装从 [downloads.python.org](https://downloads.python.org/) 下载。此变量可以设置为镜像 URL，以使用不同的 PyPy 安装源。提供的 URL 将替换例如 `https://downloads.python.org/pypy/pypy3.8-v7.3.7-osx64.tar.bz2` 中的 `https://downloads.python.org/pypy`。

可以通过使用 `file://` URL 方案从本地目录读取分发。

**默认值**: `None`

**类型**: `str`

**Example usage**:

=== "pyproject.toml"

    ```toml
    [tool.uv]
    pypy-install-mirror = "https://downloads.python.org/pypy"
    ```

=== "uv.toml"

    ```toml
    pypy-install-mirror = "https://downloads.python.org/pypy"
    ```

---

### [`python-downloads`](#python-downloads) {: #python-downloads }

是否允许 Python 下载。

**默认值**: `"automatic"`

**可能的值**:

- `"automatic"`: 在需要时自动下载托管 Python 安装
- `"manual"`: 不自动下载托管 Python 安装；需要显式安装
- `"never"`: 永远不允许 Python 下载

**Example usage**:

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

### [`python-downloads-json-url`](#python-downloads-json-url) {: #python-downloads-json-url }

指向自定义 Python 安装 JSON 的 URL。

请注意，目前仅支持本地路径。

**默认值**: `None`

**类型**: `str`

**Example usage**:

=== "pyproject.toml"

    ```toml
    [tool.uv]
    python-downloads-json-url = "/etc/uv/python-downloads.json"
    ```

=== "uv.toml"

    ```toml
    python-downloads-json-url = "/etc/uv/python-downloads.json"
    ```

---

### [`python-install-mirror`](#python-install-mirror) {: #python-install-mirror }

用于下载托管 Python 安装的镜像 URL。

默认情况下，托管 Python 安装从 [`python-build-standalone`](https://github.com/astral-sh/python-build-standalone) 下载。此变量可以设置为镜像 URL，以使用不同的 Python 安装源。提供的 URL 将替换例如 `https://github.com/astral-sh/python-build-standalone/releases/download/20240713/cpython-3.12.4%2B20240713-aarch64-apple-darwin-install_only.tar.gz` 中的 `https://github.com/astral-sh/python-build-standalone/releases/download`。

可以通过使用 `file://` URL 方案从本地目录读取分发。

**默认值**: `None`

**类型**: `str`

**Example usage**:

=== "pyproject.toml"

    ```toml
    [tool.uv]
    python-install-mirror = "https://github.com/astral-sh/python-build-standalone/releases/download"
    ```

=== "uv.toml"

    ```toml
    python-install-mirror = "https://github.com/astral-sh/python-build-standalone/releases/download"
    ```

---

### [`python-preference`](#python-preference) {: #python-preference }

是否优先使用系统上已存在的 Python 安装，还是由 uv 下载和安装的 Python 安装。

**默认值**: `"managed"`

**可能的值**:

- `"only-managed"`: 仅使用托管 Python 安装；永远不使用系统 Python 安装
- `"managed"`: 优先使用托管 Python 安装而不是系统 Python 安装
- `"system"`: 优先使用系统 Python 安装而不是托管 Python 安装
- `"only-system"`: 仅使用系统 Python 安装；永远不使用托管 Python 安装

**Example usage**:

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

### [`reinstall`](#reinstall) {: #reinstall }

重新安装所有包，无论它们是否已经安装。隐含 `refresh`。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

### [`reinstall-package`](#reinstall-package) {: #reinstall-package }

重新安装特定包，无论它是否已经安装。隐含 `refresh-package`。

**默认值**: `[]`

**类型**: `list[str]`

**Example usage**:

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

### [`required-version`](#required-version) {: #required-version }

强制要求 uv 的版本。

如果运行时 uv 的版本不满足要求，uv 将以错误退出。

接受 [PEP 440](https://peps.python.org/pep-0440/) 说明符，如 `==0.5.0` 或 `>=0.5.0`。

**默认值**: `null`

**类型**: `str`

**Example usage**:

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

### [`resolution`](#resolution) {: #resolution }

在为给定包要求选择不同兼容版本时使用的策略。

默认情况下，uv 将使用每个包的最新兼容版本（`highest`）。

**默认值**: `"highest"`

**可能的值**:

- `"highest"`: 解析每个包的最高兼容版本
- `"lowest"`: 解析每个包的最低兼容版本
- `"lowest-direct"`: 解析任何直接依赖项的最低兼容版本，以及任何传递依赖项的最高兼容版本

**Example usage**:

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

### [`trusted-publishing`](#trusted-publishing) {: #trusted-publishing }

通过 GitHub Actions 配置可信发布。

默认情况下，uv 在 GitHub Actions 中运行时检查可信发布，但如果未配置或工作流没有足够的权限（例如，来自分支的拉取请求），则忽略它。

**默认值**: `automatic`

**类型**: `str`

**Example usage**:

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

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

### [`upgrade-package`](#upgrade-package) {: #upgrade-package }

允许特定包升级，忽略任何现有输出文件中的固定版本。

接受独立包名（`ruff`）和版本说明符（`ruff<0.5.0`）。

**默认值**: `[]`

**类型**: `list[str]`

**Example usage**:

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

### `pip`

特定于 `uv pip` 命令行界面的设置。

在 `uv pip` 命名空间之外运行命令时（例如 `uv lock`、`uvx`），这些值将被忽略。

#### [`all-extras`](#pip_all-extras) {: #pip_all-extras }

<span id="all-extras"></span>

包含所有可选依赖项。

仅适用于 `pyproject.toml`、`setup.py` 和 `setup.cfg` 源。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`allow-empty-requirements`](#pip_allow-empty-requirements) {: #pip_allow-empty-requirements }

<span id="allow-empty-requirements"></span>

允许 `uv pip sync` 使用空要求，这将清除环境中的所有包。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`annotation-style`](#pip_annotation-style) {: #pip_annotation-style }

<span id="annotation-style"></span>

输出文件中包含的注释样式，用于指示每个包的来源。

**默认值**: `"split"`

**可能的值**:

- `"line"`: 在单行上呈现注释，用逗号分隔
- `"split"`: 每个注释单独一行呈现

**Example usage**:

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

#### [`break-system-packages`](#pip_break-system-packages) {: #pip_break-system-packages }

<span id="break-system-packages"></span>

允许 uv 修改 `EXTERNALLY-MANAGED` Python 安装。

警告：`--break-system-packages` 旨在用于持续集成（CI）环境，当安装到由外部包管理器（如 `apt`）管理的 Python 安装中时。应谨慎使用，因为此类 Python 安装明确建议不要由其他包管理器（如 uv 或 pip）进行修改。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`compile-bytecode`](#pip_compile-bytecode) {: #pip_compile-bytecode }

<span id="compile-bytecode"></span>

安装后将 Python 文件编译为字节码。

默认情况下，uv 不会将 Python（`.py`）文件编译为字节码（`__pycache__/*.pyc`）；相反，编译在第一次导入模块时延迟执行。对于启动时间至关重要的用例，如 CLI 应用程序和 Docker 容器，可以启用此选项以用更长的安装时间换取更快的启动时间。

启用时，uv 将处理整个 site-packages 目录（包括当前操作未修改的包）以保持一致性。与 pip 一样，它也会忽略错误。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`config-settings`](#pip_config-settings) {: #pip_config-settings }

<span id="config-settings"></span>

传递给 [PEP 517](https://peps.python.org/pep-0517/) 构建后端的设置，指定为 `KEY=VALUE` 对。

**默认值**: `{}`

**类型**: `dict`

**Example usage**:

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

#### [`custom-compile-command`](#pip_custom-compile-command) {: #pip_custom-compile-command }

<span id="custom-compile-command"></span>

包含在 `uv pip compile` 生成的输出文件顶部的标题注释。

用于反映包装 `uv pip compile` 的自定义构建脚本和命令。

**默认值**: `None`

**类型**: `str`

**Example usage**:

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

#### [`dependency-metadata`](#pip_dependency-metadata) {: #pip_dependency-metadata }

<span id="dependency-metadata"></span>

项目依赖项（直接或传递）的预定义静态元数据。提供时，使解析器能够使用指定的元数据，而不是查询注册表或从源代码构建相关包。

元数据应遵循 [Metadata 2.3](https://packaging.python.org/en/latest/specifications/core-metadata/) 标准提供，但仅遵循以下字段：

- `name`: 包的名称。
- （可选）`version`: 包的版本。如果省略，元数据将应用于包的所有版本。
- （可选）`requires-dist`: 包的依赖项（例如 `werkzeug>=0.14`）。
- （可选）`requires-python`: 包所需的 Python 版本（例如 `>=3.10`）。
- （可选）`provides-extras`: 包提供的额外功能。

**默认值**: `[]`

**类型**: `list[dict]`

**Example usage**:

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

#### [`emit-build-options`](#pip_emit-build-options) {: #pip_emit-build-options }

<span id="emit-build-options"></span>

在 `uv pip compile` 生成的输出文件中包含 `--no-binary` 和 `--only-binary` 条目。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`emit-find-links`](#pip_emit-find-links) {: #pip_emit-find-links }

<span id="emit-find-links"></span>

在 `uv pip compile` 生成的输出文件中包含 `--find-links` 条目。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`emit-index-annotation`](#pip_emit-index-annotation) {: #pip_emit-index-annotation }

<span id="emit-index-annotation"></span>

包含指示用于解析每个包的索引的注释（例如 `# from https://pypi.org/simple`）。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`emit-index-url`](#pip_emit-index-url) {: #pip_emit-index-url }

<span id="emit-index-url"></span>

在 `uv pip compile` 生成的输出文件中包含 `--index-url` 和 `--extra-index-url` 条目。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`emit-marker-expression`](#pip_emit-marker-expression) {: #pip_emit-marker-expression }

<span id="emit-marker-expression"></span>

是否发出指示固定依赖项集有效条件的标记字符串。

即使标记表达式为假，固定依赖项也可能有效，但当表达式为真时，已知要求是正确的。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`exclude-newer`](#pip_exclude-newer) {: #pip_exclude-newer }

<span id="exclude-newer"></span>

将候选包限制为在给定时间点之前上传的包。

接受 [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339.html) 的超集（例如 `2006-12-02T02:07:43Z`）。需要完整的时间戳以确保解析器在不同时区中行为一致。

**默认值**: `None`

**类型**: `str`

**Example usage**:

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

#### [`extra`](#pip_extra) {: #pip_extra }

<span id="extra"></span>

包含指定额外功能的可选依赖项；可以提供多次。

仅适用于 `pyproject.toml`、`setup.py` 和 `setup.cfg` 源。

**默认值**: `[]`

**类型**: `list[str]`

**Example usage**:

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

#### [`extra-index-url`](#pip_extra-index-url) {: #pip_extra-index-url }

<span id="extra-index-url"></span>

除了 `--index-url` 之外要使用的包索引的额外 URL。

接受符合 [PEP 503](https://peps.python.org/pep-0503/)（简单存储库 API）的存储库，或以相同格式布局的本地目录。

通过此标志提供的所有索引都优先于 [`index_url`](#index-url) 指定的索引。当提供多个索引时，较早的值优先。

要控制存在多个索引时 uv 的解析策略，请参阅 [`index_strategy`](#index-strategy)。

**默认值**: `[]`

**类型**: `list[str]`

**Example usage**:

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

#### [`find-links`](#pip_find-links) {: #pip_find-links }

<span id="find-links"></span>

除了在注册表索引中找到的候选分发之外，还要搜索候选分发的位置。

如果是路径，目标必须是在顶层包含作为 wheel 文件（`.whl`）或源分发（例如 `.tar.gz` 或 `.zip`）的包的目录。

如果是 URL，页面必须包含符合上述格式的包文件链接的平面列表。

**默认值**: `[]`

**类型**: `list[str]`

**Example usage**:

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

#### [`fork-strategy`](#pip_fork-strategy) {: #pip_fork-strategy }

<span id="fork-strategy"></span>

在跨 Python 版本和平台选择给定包的多个版本时使用的策略。

默认情况下，uv 将优化为每个支持的 Python 版本（`requires-python`）选择每个包的最新版本，同时最小化跨平台选择的版本数量。

在 `fewest` 下，uv 将最小化每个包的选择版本数量，优先选择与更广泛的支持 Python 版本或平台兼容的较旧版本。

**默认值**: `"requires-python"`

**可能的值**:

- `"fewest"`: 优化为每个包选择最少的版本数量。如果较旧版本与更广泛的支持 Python 版本或平台兼容，则可能优先选择较旧版本
- `"requires-python"`: 优化为每个支持的 Python 版本选择每个包的最新支持版本

**Example usage**:

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

#### [`generate-hashes`](#pip_generate-hashes) {: #pip_generate-hashes }

<span id="generate-hashes"></span>

在输出文件中包含分发哈希。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`group`](#pip_group) {: #pip_group }

<span id="group"></span>

包含以下依赖项组。

**默认值**: `None`

**类型**: `list[str]`

**Example usage**:

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

#### [`index-strategy`](#pip_index-strategy) {: #pip_index-strategy }

<span id="index-strategy"></span>

在针对多个索引 URL 进行解析时使用的策略。

默认情况下，uv 将在给定包可用的第一个索引处停止，并将解析限制为该第一个索引上存在的包（`first-index`）。这可以防止"依赖混淆"攻击，攻击者可以在备用索引上上传同名的恶意包。

**默认值**: `"first-index"`

**可能的值**:

- `"first-index"`: 仅使用第一个返回给定包名匹配的索引的结果
- `"unsafe-first-match"`: 在所有索引中搜索每个包名，在移动到下一个索引之前先耗尽第一个索引的版本
- `"unsafe-best-match"`: 在所有索引中搜索每个包名，优先选择找到的"最佳"版本。如果包版本在多个索引中，只查看第一个索引的条目

**Example usage**:

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

#### [`index-url`](#pip_index-url) {: #pip_index-url }

<span id="index-url"></span>

Python 包索引的 URL（默认：<https://pypi.org/simple>）。

接受符合 [PEP 503](https://peps.python.org/pep-0503/)（简单仓库 API）的仓库，或按相同格式布局的本地目录。

此设置提供的索引的优先级低于通过 [`extra_index_url`](#extra-index-url) 指定的任何索引。

**默认值**: `"https://pypi.org/simple"`

**类型**: `str`

**Example usage**:

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

#### [`keyring-provider`](#pip_keyring-provider) {: #pip_keyring-provider }

<span id="keyring-provider"></span>

尝试使用 `keyring` 对索引 URL 进行身份验证。

目前，仅支持 `--keyring-provider subprocess`，它配置 uv 使用 `keyring` CLI 来处理身份验证。

**默认值**: `disabled`

**类型**: `str`

**Example usage**:

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

#### [`link-mode`](#pip_link-mode) {: #pip_link-mode }

<span id="link-mode"></span>

从全局缓存安装包时使用的方法。

在 macOS 上默认为 `clone`（也称为写时复制），在 Linux 和 Windows 上默认为 `hardlink`。

**默认值**: `"clone" (macOS) or "hardlink" (Linux, Windows)`

**可能的值**:

- `"clone"`: 从 wheel 克隆（即写时复制）包到 `site-packages` 目录
- `"copy"`: 从 wheel 复制包到 `site-packages` 目录
- `"hardlink"`: 从 wheel 硬链接包到 `site-packages` 目录
- `"symlink"`: 从 wheel 符号链接包到 `site-packages` 目录

**Example usage**:

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

#### [`no-annotate`](#pip_no-annotate) {: #pip_no-annotate }

<span id="no-annotate"></span>

从 `uv pip compile` 生成的输出文件中排除指示每个包来源的注释注解。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`no-binary`](#pip_no-binary) {: #pip_no-binary }

<span id="no-binary"></span>

不安装预构建的 wheel。

给定的包将从源代码构建和安装。如果可用，解析器仍将使用预构建的 wheel 来提取包元数据。

可以提供多个包。使用 `:all:` 禁用所有包的二进制文件。使用 `:none:` 清除先前指定的包。

**默认值**: `[]`

**类型**: `list[str]`

**Example usage**:

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

#### [`no-build`](#pip_no-build) {: #pip_no-build }

<span id="no-build"></span>

不构建源分发。

启用时，解析将不会运行任意 Python 代码。已构建源分发的缓存 wheel 将被重用，但需要构建分发的操作将以错误退出。

`--only-binary :all:` 的别名。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`no-build-isolation`](#pip_no-build-isolation) {: #pip_no-build-isolation }

<span id="no-build-isolation"></span>

在构建源分发时禁用隔离。

假设 [PEP 518](https://peps.python.org/pep-0518/) 指定的构建依赖项已经安装。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`no-build-isolation-package`](#pip_no-build-isolation-package) {: #pip_no-build-isolation-package }

<span id="no-build-isolation-package"></span>

为特定包构建源分发时禁用隔离。

假设包的 [PEP 518](https://peps.python.org/pep-0518/) 指定的构建依赖项已经安装。

**默认值**: `[]`

**类型**: `list[str]`

**Example usage**:

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

#### [`no-deps`](#pip_no-deps) {: #pip_no-deps }

<span id="no-deps"></span>

忽略包依赖项，仅将命令行上明确列出的包添加到生成的需求文件中。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`no-emit-package`](#pip_no-emit-package) {: #pip_no-emit-package }

<span id="no-emit-package"></span>

指定要从输出解析中省略的包。其依赖项仍将包含在解析中。等同于 pip-compile 的 `--unsafe-package` 选项。

**默认值**: `[]`

**类型**: `list[str]`

**Example usage**:

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

#### [`no-extra`](#pip_no-extra) {: #pip_no-extra }

<span id="no-extra"></span>

如果提供了 `all-extras`，则排除指定的可选依赖项。

**默认值**: `[]`

**类型**: `list[str]`

**Example usage**:

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

#### [`no-header`](#pip_no-header) {: #pip_no-header }

<span id="no-header"></span>

排除 `uv pip compile` 生成的输出文件顶部的注释标头。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`no-index`](#pip_no-index) {: #pip_no-index }

<span id="no-index"></span>

忽略所有注册表索引（例如 PyPI），而是依赖直接 URL 依赖项和通过 `--find-links` 提供的依赖项。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`no-sources`](#pip_no-sources) {: #pip_no-sources }

<span id="no-sources"></span>

在解析依赖项时忽略 `tool.uv.sources` 表。用于锁定符合标准的、可发布的包元数据，而不是使用任何本地或 Git 源。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`no-strip-extras`](#pip_no-strip-extras) {: #pip_no-strip-extras }

<span id="no-strip-extras"></span>

在输出文件中包含额外依赖项。

默认情况下，uv 会剥离额外依赖项，因为额外依赖项引入的任何包已经直接作为依赖项包含在输出文件中。此外，使用 `--no-strip-extras` 生成的输出文件不能在 `install` 和 `sync` 调用中用作约束文件。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`no-strip-markers`](#pip_no-strip-markers) {: #pip_no-strip-markers }

<span id="no-strip-markers"></span>

在 `uv pip compile` 生成的输出文件中包含环境标记。

默认情况下，uv 会剥离环境标记，因为 `compile` 生成的解析仅保证对目标环境正确。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`only-binary`](#pip_only-binary) {: #pip_only-binary }

<span id="only-binary"></span>

仅使用预构建的 wheel；不构建源分发。

启用时，解析将不会运行给定包的代码。已构建源分发的缓存 wheel 将被重用，但需要构建分发的操作将以错误退出。

可以提供多个包。使用 `:all:` 禁用所有包的二进制文件。使用 `:none:` 清除先前指定的包。

**默认值**: `[]`

**类型**: `list[str]`

**Example usage**:

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

#### [`output-file`](#pip_output-file) {: #pip_output-file }

<span id="output-file"></span>

将 `uv pip compile` 生成的需求写入给定的 `requirements.txt` 文件。

如果文件已存在，在解析依赖项时将优先使用现有版本，除非同时指定了 `--upgrade`。

**默认值**: `None`

**类型**: `str`

**Example usage**:

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

#### [`prefix`](#pip_prefix) {: #pip_prefix }

<span id="prefix"></span>

将包安装到指定目录下的 `lib`、`bin` 和其他顶级文件夹中，就像该位置存在虚拟环境一样。

一般来说，优先使用 `--python` 安装到备用环境中，因为通过 `--prefix` 安装的脚本和其他工件将引用安装解释器，而不是添加到 `--prefix` 目录的任何解释器，使它们不可移植。

**默认值**: `None`

**类型**: `str`

**Example usage**:

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

#### [`prerelease`](#pip_prerelease) {: #pip_prerelease }

<span id="prerelease"></span>

考虑预发布版本时使用的策略。

默认情况下，uv 将接受仅发布预发布版本的包的预发布版本，以及在声明的说明符中包含显式预发布标记的第一方需求（`if-necessary-or-explicit`）。

**默认值**: `"if-necessary-or-explicit"`

**可能的值**:

- `"disallow"`: 禁止所有预发布版本
- `"allow"`: 允许所有预发布版本
- `"if-necessary"`: 如果包的所有版本都是预发布版本，则允许预发布版本
- `"explicit"`: 对于在其版本需求中具有显式预发布标记的第一方包，允许预发布版本
- `"if-necessary-or-explicit"`: 如果包的所有版本都是预发布版本，或者包在其版本需求中具有显式预发布标记，则允许预发布版本

**Example usage**:

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

#### [`python`](#pip_python) {: #pip_python }

<span id="python"></span>

应该安装包的 Python 解释器。

默认情况下，uv 安装到当前工作目录或任何父目录中的虚拟环境。`--python` 选项允许您指定不同的解释器，这适用于持续集成（CI）环境或其他自动化工作流。

支持的格式：

- `3.10` 在 Windows 上的注册表中查找已安装的 Python 3.10（参见 `py --list-paths`），或在 Linux 和 macOS 上查找 `python3.10`。
- `python3.10` 或 `python.exe` 在 `PATH` 中查找具有给定名称的二进制文件。
- `/home/ferris/.local/bin/python3.10` 使用给定路径的确切 Python。

**默认值**: `None`

**类型**: `str`

**Example usage**:

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

#### [`python-platform`](#pip_python-platform) {: #pip_python-platform }

<span id="python-platform"></span>

应该解析需求的平台。

表示为"目标三元组"，一个描述目标平台的字符串，包括其 CPU、供应商和操作系统名称，如 `x86_64-unknown-linux-gnu` 或 `aarch64-apple-darwin`。

**默认值**: `None`

**类型**: `str`

**Example usage**:

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

#### [`python-version`](#pip_python-version) {: #pip_python-version }

<span id="python-version"></span>

解析的需求应该支持的最低 Python 版本（例如 `3.8` 或 `3.8.17`）。

如果省略补丁版本，则假设为最低补丁版本。例如，`3.8` 映射到 `3.8.0`。

**默认值**: `None`

**类型**: `str`

**Example usage**:

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

#### [`reinstall`](#pip_reinstall) {: #pip_reinstall }

<span id="reinstall"></span>

重新安装所有包，无论它们是否已经安装。隐含 `refresh`。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`reinstall-package`](#pip_reinstall-package) {: #pip_reinstall-package }

<span id="reinstall-package"></span>

重新安装特定包，无论它是否已经安装。隐含 `refresh-package`。

**默认值**: `[]`

**类型**: `list[str]`

**Example usage**:

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

#### [`require-hashes`](#pip_require-hashes) {: #pip_require-hashes }

<span id="require-hashes"></span>

要求每个需求都有匹配的哈希。

哈希检查模式是全有或全无。如果启用，所有需求都必须提供相应的哈希或哈希集。此外，如果启用，所有需求必须固定到确切版本（例如 `==1.0.0`），或通过直接 URL 指定。

哈希检查模式引入了许多额外的约束：

- 不支持 Git 依赖项。
- 不支持可编辑安装。
- 不支持本地依赖项，除非它们指向特定的 wheel（`.whl`）或源存档（`.zip`、`.tar.gz`），而不是目录。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`resolution`](#pip_resolution) {: #pip_resolution }

<span id="resolution"></span>

在为给定包需求选择不同兼容版本时使用的策略。

默认情况下，uv 将使用每个包的最新兼容版本（`highest`）。

**默认值**: `"highest"`

**可能的值**:

- `"highest"`: 解析每个包的最高兼容版本
- `"lowest"`: 解析每个包的最低兼容版本
- `"lowest-direct"`: 解析任何直接依赖项的最低兼容版本，以及任何传递依赖项的最高兼容版本

**Example usage**:

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

#### [`strict`](#pip_strict) {: #pip_strict }

<span id="strict"></span>

验证 Python 环境，以检测缺少依赖项和其他问题的包。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`system`](#pip_system) {: #pip_system }

<span id="system"></span>

将包安装到系统 Python 环境中。

默认情况下，uv 安装到当前工作目录或任何父目录中的虚拟环境。`--system` 选项指示 uv 改为使用系统 `PATH` 中找到的第一个 Python。

警告：`--system` 适用于持续集成（CI）环境，应谨慎使用，因为它可能修改系统 Python 安装。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`target`](#pip_target) {: #pip_target }

<span id="target"></span>

将包安装到指定目录中，而不是安装到虚拟或系统 Python 环境中。包将安装在目录的顶级。

**默认值**: `None`

**类型**: `str`

**Example usage**:

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

#### [`torch-backend`](#pip_torch-backend) {: #pip_torch-backend }

<span id="torch-backend"></span>

在 PyTorch 生态系统中获取包时使用的后端。

设置后，uv 将忽略 PyTorch 生态系统中包的配置索引 URL，而是使用定义的后端。

例如，当设置为 `cpu` 时，uv 将使用仅 CPU 的 PyTorch 索引；当设置为 `cu126` 时，uv 将使用 CUDA 12.6 的 PyTorch 索引。

`auto` 模式将尝试根据当前安装的 CUDA 驱动程序检测适当的 PyTorch 索引。

此选项处于预览状态，可能在任何未来版本中更改。

**默认值**: `null`

**类型**: `str`

**Example usage**:

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

#### [`universal`](#pip_universal) {: #pip_universal }

<span id="universal"></span>

执行通用解析，尝试生成与所有操作系统、架构和 Python 实现兼容的单个 `requirements.txt` 输出文件。

在通用模式下，当前 Python 版本（或用户提供的 `--python-version`）将被视为下界。例如，`--universal --python-version 3.7` 将为 Python 3.7 及更高版本生成通用解析。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`upgrade`](#pip_upgrade) {: #pip_upgrade }

<span id="upgrade"></span>

允许包升级，忽略任何现有输出文件中的固定版本。

**默认值**: `false`

**类型**: `bool`

**Example usage**:

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

#### [`upgrade-package`](#pip_upgrade-package) {: #pip_upgrade-package }

<span id="upgrade-package"></span>

允许特定包的升级，忽略任何现有输出文件中的固定版本。

接受独立包名（`ruff`）和版本说明符（`ruff<0.5.0`）。

**默认值**: `[]`

**类型**: `list[str]`

**Example usage**:

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

#### [`verify-hashes`](#pip_verify-hashes) {: #pip_verify-hashes }

<span id="verify-hashes"></span>

验证需求文件中提供的任何哈希。

与 `--require-hashes` 不同，`--verify-hashes` 不要求所有需求都有哈希；相反，它将限制自己验证那些确实包含哈希的需求的哈希。

**默认值**: `true`

**类型**: `bool`

**Example usage**:

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

---

