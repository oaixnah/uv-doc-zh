---
subtitle: HTTP credentials
description: 本文档介绍 uv 在查询包注册表时通过 HTTP 传递凭证的认证机制，涵盖认证来源的优先级顺序（URL 内嵌、netrc 文件、uv 凭证存储、密钥环提供程序），以及 netrc 文件配置、uv 原生凭证存储、keyring 密钥环提供程序的使用方式，和凭证持久化策略与注意事项。
---

# HTTP 凭证 {#http-credentials}

uv 支持在查询包注册表时通过 HTTP 传递凭证。

认证信息可来自以下来源，按优先级顺序排列：

- URL 内嵌凭据，例如 `https://<user>:<password>@<hostname>/...`
- [netrc](#netrc-files) 配置文件
- uv 凭证存储
- [keyring 密钥环提供程序](#keyring-providers)（默认关闭）

认证可应用于以下上下文（context）中指定的主机：

- `[index]`
- `index-url`
- `extra-index-url`
- `find-links`
- `package @ https://...`

## netrc 文件 {#netrc-files}

[`.netrc`](https://everything.curl.dev/usingcurl/netrc) 文件是一种历史悠久的纯文本格式，用于在系统上存储凭证。

从 `.netrc` 文件中读取凭证始终处于启用状态。目标文件路径将优先从 `NETRC` 环境变量加载（如果已定义），否则回退到 `~/.netrc`。

## uv 凭证存储 {#the-uv-credentials-store}

uv 可以使用 [`uv auth` 命令](./cli.md)从存储中读写凭证。

凭证以明文文件形式存储在 uv 的状态目录中，例如在 Unix 系统上为 `~/.local/share/uv/credentials/credentials.toml`。该文件目前不推荐手动编辑。

!!! note

    一种安全的、系统原生的存储机制已进入[预览阶段](../preview.md)——它仍处于实验阶段，正在积极开发中。未来，这将默认成为存储机制。

    启用后，uv 将使用操作系统原生的密钥存储机制。在 macOS 上，它使用 Keychain Services（钥匙串服务）。在 Windows 上，它使用 Windows Credential Manager（Windows 凭证管理器）。在 Linux 上，它使用基于 DBus 的 Secret Service API。

    目前，uv 仅会在原生存储中搜索其自身添加到密钥存储中的凭证——不会检索其他应用程序持久化的凭证。

    设置 `UV_PREVIEW_FEATURES=native-auth` 即可使用此存储机制。

## Keyring 密钥环提供程序 {#keyring-providers}

密钥环提供程序（keyring provider）是 `pip` 引入的一个概念，允许通过与流行的 [keyring](https://github.com/jaraco/keyring) Python 包相匹配的接口来检索凭证。

"subprocess" 密钥环提供程序通过调用 `keyring` 命令来获取凭证。uv 目前不支持其他类型的密钥环提供程序。

设置 `--keyring-provider subprocess`、`UV_KEYRING_PROVIDER=subprocess` 或 `tool.uv.keyring-provider = "subprocess"` 即可使用该提供程序。

## 凭证持久化 {#persistence-of-credentials}

如果为单个索引 URL 或网络位置（scheme、host 和 port）找到了认证信息，则该信息将在命令执行期间被缓存，并用于对该索引或网络位置的其他查询。认证信息不会在 uv 的多次调用之间缓存。

使用 `uv add` 时，uv _不会_ 将索引凭证持久化到 `pyproject.toml` 或 `uv.lock` 中。这些文件通常会被纳入源代码管理和分发中，因此将凭证包含在其中通常是不安全的。然而，uv _会_ 持久化直接 URL 的凭证，例如 `package @ https://username:password:example.com/foo.whl`，因为目前没有其他方式提供这些凭证。

如果在 `uv add` 期间凭证被附加到了索引 URL，uv 在后续操作中可能无法从需要认证的索引中获取依赖项。有关索引的持久化认证详情，请参阅[索引认证文档](../indexes.md#authentication)。

## 了解更多 {#learn-more}

有关索引 URL 认证的详细信息，请参阅[索引认证文档](../indexes.md#authentication)。

有关与 `pip` 的差异详情，请参阅 [`pip` 兼容性指南](../../pip/compatibility.md#registry-authentication)。
