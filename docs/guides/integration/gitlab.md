---
title: 在 GitLab CI/CD 中使用 uv
description: 一份在 GitLab CI/CD 中使用 uv 的指南，内容包括安装、设置 Python、安装依赖项等。
---

# 在 GitLab CI/CD 中使用 uv

## 使用 uv 镜像

Astral 提供了预装 uv 的 [Docker 镜像](docker.md#_2)。
请选择适合您工作流程的变体。

```yaml title="gitlab-ci.yml"
variables:
  UV_VERSION: "0.5"
  PYTHON_VERSION: "3.12"
  BASE_LAYER: bookworm-slim
  # GitLab CI 为构建目录创建了一个单独的挂载点，
  # 因此我们需要复制而不是使用硬链接。
  UV_LINK_MODE: copy

uv:
  image: ghcr.io/astral-sh/uv:$UV_VERSION-python$PYTHON_VERSION-$BASE_LAYER
  script:
    # 您的 `uv` 命令
```

!!! note

    如果您使用的是 distroless 镜像，则必须指定入口点：
    ```yaml
    uv:
      image:
        name: ghcr.io/astral-sh/uv:$UV_VERSION
        entrypoint: [""]
      # ...
    ```

## 缓存

在工作流运行之间持久化 uv 缓存可以提高性能。

```yaml
uv-install:
  variables:
    UV_CACHE_DIR: .uv-cache
  cache:
    - key:
        files:
          - uv.lock
      paths:
        - $UV_CACHE_DIR
  script:
    # 您的 `uv` 命令
    - uv cache prune --ci
```

有关配置缓存的更多详细信息，请参阅 [GitLab 缓存文档](https://docs.gitlab.com/ee/ci/caching/)。

建议在作业结束时使用 `uv cache prune --ci` 来减小缓存大小。有关更多详细信息，请参阅 [uv 缓存文档](../../concepts/cache.md#_5)。

## 使用 `uv pip`

如果使用 `uv pip` 接口而不是 uv 项目接口，uv 默认需要一个虚拟环境。要允许将包安装到系统环境中，请在所有 uv 调用中使用 `--system` 标志或设置 `UV_SYSTEM_PYTHON` 变量。

`UV_SYSTEM_PYTHON` 变量可以在不同的范围内定义。您可以在[此处](https://docs.gitlab.com/ee/ci/variables/)阅读有关 GitLab 中变量及其优先级如何工作的更多信息。

通过在顶层定义它来为整个工作流选择加入：

```yaml title="gitlab-ci.yml"
variables:
  UV_SYSTEM_PYTHON: 1

# [...]
```

要再次选择退出，可以在任何 uv 调用中使用 `--no-system` 标志。

在持久化缓存时，您可能希望使用 `requirements.txt` 或 `pyproject.toml` 作为缓存键文件，而不是 `uv.lock`。
