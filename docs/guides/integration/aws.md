---
title: AWS CodeArtifact
description: 使用 uv 与 AWS CodeArtifact 集成，实现 Python 包的安装与发布。
---

# AWS CodeArtifact

uv 可以从
[AWS CodeArtifact](https://docs.aws.amazon.com/codeartifact/latest/ug/using-python.html) 安装包，方式有两种：使用访问令牌（access token），或使用 [`keyring`](https://github.com/jaraco/keyring) 包。

!!! note

    本指南假定已安装 [`awscli`](https://aws.amazon.com/cli/) 并完成身份验证。

索引可以按如下方式声明：

```toml title="pyproject.toml"
[[tool.uv.index]]
name = "private-registry"
url = "https://<DOMAIN>-<ACCOUNT_ID>.d.codeartifact.<REGION>.amazonaws.com/pypi/<REPOSITORY>/simple/"
```

## 使用 AWS 访问令牌进行身份验证

凭据可以通过 "Basic" HTTP 认证方案提供。将访问令牌包含在 URL 的密码字段中。用户名必须为 `aws`，否则认证将失败。

使用 `awscli` 生成令牌：

```bash
export AWS_CODEARTIFACT_TOKEN="$(
    aws codeartifact get-authorization-token \
    --domain <DOMAIN> \
    --domain-owner <ACCOUNT_ID> \
    --query authorizationToken \
    --output text
)"
```

!!! note

    你可能需要传递额外参数（如 `--region`）才能正确生成令牌，以上仅为基本示例。

然后为索引设置凭据：

```bash
export UV_INDEX_PRIVATE_REGISTRY_USERNAME=aws
export UV_INDEX_PRIVATE_REGISTRY_PASSWORD="$AWS_CODEARTIFACT_TOKEN"
```

!!! note

    `PRIVATE_REGISTRY` 应与你在 `pyproject.toml` 中定义的索引名称一致。

## 使用 `keyring` 和 `keyrings.codeartifact` 进行身份验证

你也可以使用 [`keyring`](https://github.com/jaraco/keyring) 包及其 [`keyrings.codeartifact` 插件](https://github.com/jmkeyes/keyrings.codeartifact) 对 Artifact Registry 进行身份验证。由于这两个包是向 Artifact Registry 认证所必需的，因此必须从 Artifact Registry 以外的源预先安装。

`keyrings.codeartifact` 插件封装了 [boto3](https://pypi.org/project/boto3/)，用于生成短期访问令牌，将其安全存储在系统密钥环（keyring）中，并在令牌过期时自动刷新。

uv 仅支持在[子进程模式](../../reference/settings.md#keyring-provider) 下使用 `keyring` 包。`keyring` 可执行文件必须位于 `PATH` 中，即全局安装或安装在当前激活的环境中。`keyring` CLI 要求 URL 中包含用户名，且用户名必须为 `aws`。

```bash
# 从公共 PyPI 预安装 keyring 和 AWS CodeArtifact 插件
uv tool install keyring --with keyrings.codeartifact

# 启用 keyring 认证
export UV_KEYRING_PROVIDER=subprocess

# 设置索引的用户名
export UV_INDEX_PRIVATE_REGISTRY_USERNAME=aws
```

!!! note

    [`tool.uv.keyring-provider`](../../reference/settings.md#keyring-provider) 设置可用于在 `uv.toml` 或 `pyproject.toml` 中启用 keyring。

    同样，索引的用户名也可以直接添加到索引 URL 中。

## 发布包

如果你还想将自己的包发布到 AWS CodeArtifact，可以使用 `uv publish`，如 [构建与发布指南](../package.md) 中所述。

首先，为你想要发布包的索引添加 `publish-url`。例如：

```toml title="pyproject.toml" hl_lines="4"
[[tool.uv.index]]
name = "private-registry"
url = "https://<DOMAIN>-<ACCOUNT_ID>.d.codeartifact.<REGION>.amazonaws.com/pypi/<REPOSITORY>/simple/"
publish-url = "https://<DOMAIN>-<ACCOUNT_ID>.d.codeartifact.<REGION>.amazonaws.com/pypi/<REPOSITORY>/"
```

然后，配置凭据（如果未使用 keyring）：

```bash
export UV_PUBLISH_USERNAME=aws
export UV_PUBLISH_PASSWORD="$AWS_CODEARTIFACT_TOKEN"
```

接着发布包：

```bash
uv publish --index private-registry
```

要在不向项目中添加 `publish-url` 的情况下使用 `uv publish`，可以设置 `UV_PUBLISH_URL`：

```bash
export UV_PUBLISH_URL=https://<DOMAIN>-<ACCOUNT_ID>.d.codeartifact.<REGION>.amazonaws.com/pypi/<REPOSITORY>/
uv publish
```

请注意，此方法不太推荐，因为在上传制品之前，uv 无法检查该包是否已发布。
