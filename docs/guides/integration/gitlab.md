---
title: 在 GitLab CI/CD 中使用 uv
description: 一份在 GitLab CI/CD 中使用 uv 的指南，内容包括安装、设置 Python、安装依赖项等。
---

# 在 GitLab CI/CD 中使用 uv

## 使用 uv 镜像

Astral 提供了预装 uv 的 [Docker 镜像](docker.md#available-images)。请选择适合你工作流的变体版本。

```yaml title=".gitlab-ci.yml"
variables:
  UV_VERSION: "0.11.23"
  PYTHON_VERSION: "3.12"
  BASE_LAYER: trixie-slim
  # GitLab CI 会为构建目录创建一个独立的挂载点，
  # 因此我们需要使用复制而非硬链接。
  UV_LINK_MODE: copy

uv:
  image: ghcr.io/astral-sh/uv:$UV_VERSION-python$PYTHON_VERSION-$BASE_LAYER
  script:
    # 你的 `uv` 命令
```

!!! note

    如果你使用的是 distroless 镜像，则必须指定入口点（entrypoint）：
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
    # 你的 `uv` 命令
  after_script:
    - uv cache prune --ci
```

有关配置缓存的更多详细信息，请参阅 [GitLab 缓存文档](https://docs.gitlab.com/ee/ci/caching/)。

建议在作业结束时使用 `uv cache prune --ci` 来减小缓存大小。更多细节请参阅 [uv 缓存文档](../../concepts/cache.md#caching-in-continuous-integration)。

## 使用 `uv pip`

如果使用 `uv pip` 接口而非 uv 项目接口，uv 默认需要虚拟环境。要允许将包安装到系统环境中，请在所有 uv 调用中使用 `--system` 标志，或设置 `UV_SYSTEM_PYTHON` 变量。

`UV_SYSTEM_PYTHON` 变量可以在不同作用域中定义。你可以在[这里](https://docs.gitlab.com/ee/ci/variables/)阅读更多关于 GitLab 中变量及其优先级的工作方式。

要在整个工作流中启用，可以在顶层定义：

```yaml title=".gitlab-ci.yml"
variables:
  UV_SYSTEM_PYTHON: 1

# [...]
```

要再次退出此模式，可以在任何 uv 调用中使用 `--no-system` 标志。

在持久化缓存时，你可能希望使用 `requirements.txt` 或 `pyproject.toml` 作为缓存键文件，而不是 `uv.lock`。
