---
subtitle: Git credentials
description: 本文介绍 uv 如何通过 SSH 和 HTTP 认证从私有 Git 仓库安装包，包括 SSH 密钥配置、HTTP 基本认证令牌使用、凭证持久化策略以及 Git 凭证助手（credential helper）的设置方法。
---

# Git 凭证 {#git-credentials}

uv 支持通过 SSH 或 HTTP 认证从私有 Git 仓库安装包。

## SSH 认证 {#ssh-authentication}

要使用 SSH 密钥进行认证，请使用 `ssh://` 协议：

- `git+ssh://git@<hostname>/...`（例如 `git+ssh://git@github.com/astral-sh/uv`）
- `git+ssh://git@<host>/...`（例如 `git+ssh://git@github.com-key-2/astral-sh/uv`）

SSH 认证需要使用用户名 `git`。

有关如何配置 SSH 的更多详细信息，请参阅
[GitHub SSH 文档](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh)。

### HTTP 认证 {#http-authentication}

要通过 HTTP 基本认证（Basic authentication）使用密码或令牌（token）进行认证：

- `git+https://<user>:<token>@<hostname>/...`（例如
  `git+https://git:github_pat_asdf@github.com/astral-sh/uv`）
- `git+https://<token>@<hostname>/...`（例如 `git+https://github_pat_asdf@github.com/astral-sh/uv`）
- `git+https://<user>@<hostname>/...`（例如 `git+https://git@github.com/astral-sh/uv`）

!!! note

    当使用 GitHub 个人访问令牌（personal access token）时，用户名可以是任意的。GitHub 不允许你在类似这样的 URL 中使用账户名和密码，但其他托管平台可能允许。

如果 URL 中不包含凭证且需要认证，uv 将查询
[Git 凭证助手](#git-credential-helpers)（Git credential helper）。

## 凭证的持久化 {#persistence-of-credentials}

使用 `uv add` 时，uv **不会**将 Git 凭证持久化到 `pyproject.toml` 或 `uv.lock` 中。
这些文件通常会被纳入源代码管理和分发，因此将凭证包含在其中通常是不安全的。

如果你配置了 Git 凭证助手，你的凭证可能会被自动持久化，从而使后续对依赖项的获取能够成功。但是，如果你没有 Git 凭证助手，或者项目在未预置凭证的机器上使用，uv 将无法获取该依赖项。

你**可以**通过向 `uv add` 传递 `--raw` 选项来强制 uv 持久化 Git 凭证。不过，我们强烈建议改为设置[凭证助手](#git-credential-helpers)。

## Git 凭证助手 {#git-credential-helpers}

Git 凭证助手用于存储和检索 Git 凭证。请参阅
[Git 文档](https://git-scm.com/doc/credential-helpers)了解更多信息。

如果你正在使用 GitHub，设置凭证助手最简单的方法是
[安装 `gh` CLI](https://github.com/cli/cli#installation) 并使用：

```console
$ gh auth login
```

有关更多详细信息，请参阅 [`gh auth login`](https://cli.github.com/manual/gh_auth_login) 文档。

!!! note

    以交互方式运行 `gh auth login` 时，凭证助手会自动配置。
    但使用 `gh auth login --with-token` 时（如 uv
    [GitHub Actions 指南](../../guides/integration/github.md#private-repos)中所述），则需要在此之后运行
    [`gh auth setup-git`](https://cli.github.com/manual/gh_auth_setup-git) 命令来配置凭证助手。
