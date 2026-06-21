---
title: JFrog Artifactory
description: 使用 uv 与 JFrog Artifactory 集成，用于安装和发布 Python 包。
---

# JFrog Artifactory

uv 可以从 JFrog Artifactory 安装包，可以使用用户名和密码，也可以使用 JWT 令牌。

要使用它，请将索引添加到您的项目中：

```toml title="pyproject.toml"
[[tool.uv.index]]
name = "private-registry"
url = "https://<organization>.jfrog.io/artifactory/api/pypi/<repository>/simple"
```

## 使用用户名和密码进行身份验证

```bash
export UV_INDEX_PRIVATE_REGISTRY_USERNAME="<username>"
export UV_INDEX_PRIVATE_REGISTRY_PASSWORD="<password>"
```

## 使用 JWT 令牌进行身份验证

```bash
export UV_INDEX_PRIVATE_REGISTRY_USERNAME=""
export UV_INDEX_PRIVATE_REGISTRY_PASSWORD="$JFROG_JWT_TOKEN"
```

!!! note

    将环境变量名称中的 `PRIVATE_REGISTRY` 替换为您在 `pyproject.toml` 中定义的实际索引名称。

## 发布包

为您的索引定义添加一个 `publish-url`：

```toml title="pyproject.toml"
[[tool.uv.index]]
name = "private-registry"
url = "https://<organization>.jfrog.io/artifactory/api/pypi/<repository>/simple"
publish-url = "https://<organization>.jfrog.io/artifactory/api/pypi/<repository>"
```

!!! important

    如果您将 `--token "$JFROG_TOKEN"` 或 `UV_PUBLISH_TOKEN` 与 JFrog 一起使用，您将收到 401 未授权错误，因为 JFrog 需要一个空用户名，但当使用 `--token` 时，uv 会将 `__token__` 作为用户名传递。

要进行身份验证，请将您的令牌作为密码传递，并将用户名设置为空字符串：

```bash
uv publish --index <index_name> -u "" -p "$JFROG_TOKEN"
```

或者，您可以设置环境变量：

```bash
export UV_PUBLISH_USERNAME=""
export UV_PUBLISH_PASSWORD="$JFROG_TOKEN"
uv publish --index private-registry
```

!!! note

    发布环境变量（`UV_PUBLISH_USERNAME` 和 `UV_PUBLISH_PASSWORD`）不包含索引名称。
