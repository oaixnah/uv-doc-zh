---
subtitle: Authentication
---

# 认证

## Git 认证

uv 允许从 Git 安装包，并支持以下方案来认证私有仓库。

使用 SSH：

- `git+ssh://git@<hostname>/...` (例如, `git+ssh://git@github.com/astral-sh/uv`)
- `git+ssh://git@<host>/...` (例如, `git+ssh://git@github.com-key-2/astral-sh/uv`)

有关如何配置 SSH 的更多详细信息，请参阅
[GitHub SSH 文档](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh)。

使用密码或令牌：

- `git+https://<user>:<token>@<hostname>/...` (例如,
  `git+https://git:github_pat_asdf@github.com/astral-sh/uv`)
- `git+https://<token>@<hostname>/...` (例如, `git+https://github_pat_asdf@github.com/astral-sh/uv`)
- `git+https://<user>@<hostname>/...` (例如, `git+https://git@github.com/astral-sh/uv`)

使用 GitHub 个人访问令牌时，用户名是任意的。GitHub 不允许您在此类 URL 中使用您的帐户名和密码，但其他主机可能允许。

如果 URL 中没有凭据且需要认证，则会查询 [Git 凭据帮助程序](#git_1)。

!!! important

    使用 `uv add` 时，uv _不会_ 将 Git 凭据持久化到 `pyproject.toml` 或 `uv.lock`。
    这些文件通常包含在源代码控制和分发中，因此在其中包含凭据通常是不安全的。

    如果您配置了 Git 凭据帮助程序，您的凭据可能会被自动持久化，从而成功获取后续的依赖项。但是，如果您没有 Git 凭据帮助程序或项目在没有凭据种子的机器上使用，uv 将无法获取依赖项。

    您 _可以_ 通过向 `uv add` 传递 `--raw` 选项来强制 uv 持久化 Git 凭据。但是，我们强烈建议设置一个 [凭据帮助程序](#git_1) 来代替。

### Git 凭据帮助程序

Git 凭据帮助程序用于存储和检索 Git 凭据。有关更多信息，请参阅
[Git 文档](https://git-scm.com/doc/credential-helpers)。

如果您正在使用 GitHub，设置凭据帮助程序的最简单方法是[安装 `gh` CLI](https://github.com/cli/cli#installation) 并使用：

```console
$ gh auth login
```

有关更多详细信息，请参阅 [`gh auth login`](https://cli.github.com/manual/gh_auth_login) 文档。

!!! note

    当以交互方式使用 `gh auth login` 时，凭据帮助程序将自动配置。
    但是当使用 `gh auth login --with-token` 时，如 uv [GitHub Actions 指南](../guides/integration/github.md#_4) 中所示，之后需要运行 [`gh auth setup-git`](https://cli.github.com/manual/gh_auth_setup-git) 命令来配置凭据帮助程序。

## HTTP 认证

uv 在查询包注册表时支持通过 HTTP 进行凭据认证。

认证可以来自以下来源，按优先顺序排列：

- URL，例如 `https://<user>:<password>@<hostname>/...`
- [`.netrc`](https://everything.curl.dev/usingcurl/netrc) 配置文件
- [keyring](https://github.com/jaraco/keyring) 提供程序 (需要选择加入)

如果为单个索引 URL 或网络位置（方案、主机和端口）找到认证，它将被缓存到命令的持续时间内，并用于对该索引或网络位置的其他查询。认证不会在 uv 的调用之间缓存。

`.netrc` 认证默认启用，如果定义了 `NETRC` 环境变量，则会遵循该变量，否则回退到 `~/.netrc`。

要启用基于 keyring 的认证，请将 `--keyring-provider subprocess` 命令行参数传递给 uv，或设置 `UV_KEYRING_PROVIDER=subprocess`。

认证可用于在以下上下文中指定的主机：

- `[index]`
- `index-url`
- `extra-index-url`
- `find-links`
- `package @ https://...`

有关认证索引 URL 的详细信息，请参阅[索引认证文档](./indexes.md#_5)。

有关与 `pip` 的差异的详细信息，请参阅 [`pip` 兼容性指南](../pip/compatibility.md#_8)。

!!! important

    使用 `uv add` 时，uv _不会_ 将索引凭据持久化到 `pyproject.toml` 或 `uv.lock`。
    这些文件通常包含在源代码控制和分发中，因此在其中包含凭据通常是不安全的。但是，uv _将_ 持久化直接 URL 的凭据，即 `package @ https://username:password:example.com/foo.whl`，因为目前没有其他方法可以提供这些凭据。

    如果在 `uv add` 期间将凭据附加到索引 URL，uv 可能会在后续操作中无法从需要认证的索引中获取依赖项。有关索引的持久认证的详细信息，请参阅[索引认证文档](./indexes.md#_5)。

## 与备用包索引的认证

有关与流行的备用 Python 包索引进行认证的详细信息，请参阅[备用索引集成指南](../guides/integration/alternative-indexes.md)。

## 自定义 CA 证书

默认情况下，uv 从捆绑的 `webpki-roots` crate 加载证书。`webpki-roots` 是来自 Mozilla 的一组可靠的信任根，将它们包含在 uv 中可以提高可移植性和性能（尤其是在 macOS 上，读取系统信任存储会产生显著延迟）。

但是，在某些情况下，您可能希望使用平台的本机证书存储，特别是如果您依赖于公司信任根（例如，对于强制代理）并且该信任根已包含在您系统的证书存储中。要指示 uv 使用系统的信任存储，请使用 `--native-tls` 命令行标志运行 uv，或将 `UV_NATIVE_TLS` 环境变量设置为 `true`。

如果需要证书的直接路径（例如，在 CI 中），请将 `SSL_CERT_FILE` 环境变量设置为证书包的路径，以指示 uv 使用该文件而不是系统的信任存储。

如果需要客户端证书认证 (mTLS)，请将 `SSL_CLIENT_CERT` 环境变量设置为包含证书和私钥的 PEM 格式文件的路径。

最后，如果您使用的设置中希望信任自签名证书或以其他方式禁用证书验证，您可以通过 `allow-insecure-host` 配置选项指示 uv 允许对专用主机的非安全连接。例如，将以下内容添加到 `pyproject.toml` 将允许对 `example.com` 的非安全连接：

```toml
[tool.uv]
allow-insecure-host = ["example.com"]
```

`allow-insecure-host` 期望接收一个主机名（例如 `localhost`）或主机名-端口对（例如 `localhost:8080`），并且仅适用于 HTTPS 连接，因为 HTTP 连接本身就是不安全的。

请谨慎使用 `allow-insecure-host`，并且仅在受信任的环境中使用，因为它可能会因缺少证书验证而使您面临安全风险。
