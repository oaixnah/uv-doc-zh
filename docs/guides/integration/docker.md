---
title: 在 Docker 中使用 uv
description: 一份在 Docker 中使用 uv 管理 Python 依赖的完整指南，同时通过多阶段构建、中间层等方式优化构建时间和镜像大小。
---

# 在 Docker 中使用 uv

## 入门

!!! tip

    请查看 [`uv-docker-example`](https://github.com/astral-sh/uv-docker-example) 项目，了解在 Docker 中使用 uv 构建应用程序的最佳实践示例。

uv 提供了 _distroless_ Docker 镜像和从流行基础镜像派生的镜像。前者可用于将 [uv 二进制文件](#uv) 复制到你自己的镜像构建中，后者则适用于在容器中使用 uv。distroless 镜像除了 uv 二进制文件外不包含任何其他内容。相比之下，派生镜像则包含了预装 uv 的操作系统。

例如，使用基于 Debian 的镜像在容器中运行 uv：

```console
$ docker run --rm -it ghcr.io/astral-sh/uv:debian uv --help
```

### 可用镜像

提供以下 distroless 镜像：

- `ghcr.io/astral-sh/uv:latest`
- `ghcr.io/astral-sh/uv:{major}.{minor}.{patch}`，例如 `ghcr.io/astral-sh/uv:0.8.18`
- `ghcr.io/astral-sh/uv:{major}.{minor}`，例如 `ghcr.io/astral-sh/uv:0.8` (最新的补丁版本)

并提供以下派生镜像：

<!-- prettier-ignore -->
- 基于 `alpine:3.21`:
    - `ghcr.io/astral-sh/uv:alpine`
    - `ghcr.io/astral-sh/uv:alpine3.21`
- 基于 `debian:bookworm-slim`:
    - `ghcr.io/astral-sh/uv:debian-slim`
    - `ghcr.io/astral-sh/uv:bookworm-slim`
- 基于 `buildpack-deps:bookworm`:
    - `ghcr.io/astral-sh/uv:debian`
    - `ghcr.io/astral-sh/uv:bookworm`
- 基于 `python3.x-alpine`:
    - `ghcr.io/astral-sh/uv:python3.14-rc-alpine`
    - `ghcr.io/astral-sh/uv:python3.13-alpine`
    - `ghcr.io/astral-sh/uv:python3.12-alpine`
    - `ghcr.io/astral-sh/uv:python3.11-alpine`
    - `ghcr.io/astral-sh/uv:python3.10-alpine`
    - `ghcr.io/astral-sh/uv:python3.9-alpine`
    - `ghcr.io/astral-sh/uv:python3.8-alpine`
- 基于 `python3.x-bookworm`:
    - `ghcr.io/astral-sh/uv:python3.14-rc-bookworm`
    - `ghcr.io/astral-sh/uv:python3.13-bookworm`
    - `ghcr.io/astral-sh/uv:python3.12-bookworm`
    - `ghcr.io/astral-sh/uv:python3.11-bookworm`
    - `ghcr.io/astral-sh/uv:python3.10-bookworm`
    - `ghcr.io/astral-sh/uv:python3.9-bookworm`
    - `ghcr.io/astral-sh/uv:python3.8-bookworm`
- 基于 `python3.x-slim-bookworm`:
    - `ghcr.io/astral-sh/uv:python3.14-rc-bookworm-slim`
    - `ghcr.io/astral-sh/uv:python3.13-bookworm-slim`
    - `ghcr.io/astral-sh/uv:python3.12-bookworm-slim`
    - `ghcr.io/astral-sh/uv:python3.11-bookworm-slim`
    - `ghcr.io/astral-sh/uv:python3.10-bookworm-slim`
    - `ghcr.io/astral-sh/uv:python3.9-bookworm-slim`
    - `ghcr.io/astral-sh/uv:python3.8-bookworm-slim`
<!-- prettier-ignore-end -->

与 distroless 镜像一样，每个派生镜像都以 `ghcr.io/astral-sh/uv:{major}.{minor}.{patch}-{base}` 和 `ghcr.io/astral-sh/uv:{major}.{minor}-{base}` 的形式发布 uv 版本标签，例如 `ghcr.io/astral-sh/uv:0.8.18-alpine`。

更多详情，请参阅 [GitHub Container](https://github.com/astral-sh/uv/pkgs/container/uv) 页面。

### 安装 uv

使用上面预装了 uv 的镜像之一，或者通过从官方 distroless Docker 镜像复制二进制文件来安装 uv：

```dockerfile title="Dockerfile"
FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
```

或者，使用安装程序：

```dockerfile title="Dockerfile"
FROM python:3.12-slim-bookworm

# 安装程序需要 curl（和证书）来下载发布归档
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# 下载最新的安装程序
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# 运行安装程序然后删除它
RUN sh /uv-installer.sh && rm /uv-installer.sh

# 确保安装的二进制文件在 `PATH` 中
ENV PATH="/root/.local/bin/:$PATH"
```

请注意，这需要 `curl` 可用。

在任何一种情况下，最佳实践是固定到特定的 uv 版本，例如：

```dockerfile
COPY --from=ghcr.io/astral-sh/uv:0.8.18 /uv /uvx /bin/
```

!!! tip

    虽然上面的 Dockerfile 示例固定了特定的标签，但也可以固定特定的 SHA256。在需要可复现构建的环境中，固定特定的 SHA256 被认为是最佳实践，因为标签可以在不同的提交 SHA 之间移动。

    ```Dockerfile
    # 例如，使用先前版本的哈希
    COPY --from=ghcr.io/astral-sh/uv@sha256:2381d6aa60c326b71fd40023f921a0a3b8f91b14d5db6b90402e65a635053709 /uv /uvx /bin/
    ```

或者，使用安装程序：

```dockerfile
ADD https://astral.sh/uv/0.8.18/install.sh /uv-installer.sh
```

### 安装项目

如果你使用 uv 管理你的项目，你可以将其复制到镜像中并安装：

```dockerfile title="Dockerfile"
# 将项目复制到镜像中
ADD . /app

# 将项目同步到一个新环境中，并断言锁文件是最新的
WORKDIR /app
RUN uv sync --locked
```

!!! important

    最佳实践是将 `.venv` 添加到仓库中的 [`.dockerignore` 文件](https://docs.docker.com/build/concepts/context/#dockerignore-files) 中，以防止它被包含在镜像构建中。项目虚拟环境依赖于你的本地平台，应该在镜像中从头开始创建。

然后，默认启动你的应用程序：

```dockerfile title="Dockerfile"
# 假设项目提供了一个 `my_app` 命令
CMD ["uv", "run", "my_app"]
```

!!! tip

    最佳实践是使用[中间层](#_10)来分离依赖项和项目本身的安装，以改善 Docker 镜像的构建时间。

请参阅 [`uv-docker-example` 项目](https://github.com/astral-sh/uv-docker-example/blob/main/Dockerfile)中的完整示例。

### 使用环境

项目安装后，你可以通过将其二进制目录放在路径的前面来 _激活_ 项目虚拟环境：

```dockerfile title="Dockerfile"
ENV PATH="/app/.venv/bin:$PATH"
```

或者，你可以为任何需要环境的命令使用 `uv run`：

```dockerfile title="Dockerfile"
RUN uv run some_script.py
```

!!! tip

    或者，可以在同步之前设置 [`UV_PROJECT_ENVIRONMENT` 设置](../../concepts/projects/config.md#_9)，以安装到系统 Python 环境并完全跳过环境激活。

### 使用已安装的工具

要使用已安装的工具，请确保[工具 bin 目录](../../concepts/tools.md#bin)在路径上：

```dockerfile title="Dockerfile"
ENV PATH=/root/.local/bin:$PATH
RUN uv tool install cowsay
```

```console
$ docker run -it $(docker build -q .) /bin/bash -c "cowsay -t hello"
  _____
| hello |
  =====
     \
      \
        ^__^
        (oo)\_______
        (__)\       )\/\
            ||----w |
            ||     ||
```

!!! note

    工具 bin 目录的位置可以通过在容器中运行 `uv tool dir --bin` 命令来确定。

    或者，可以将其设置为一个常量位置：

    ```dockerfile title="Dockerfile"
    ENV UV_TOOL_BIN_DIR=/opt/uv-bin/
    ```

### 在 ARM musl 镜像中安装 Python

虽然在镜像中没有可用的兼容 Python 版本时，uv 会尝试[安装一个兼容的 Python 版本](../install-python.md)，但 uv 尚不支持为 ARM 上的 musl Linux 安装 Python。例如，如果你在 ARM 机器上使用 Alpine Linux 基础镜像，你可能需要使用系统包管理器添加它：

```shell
apk add --no-cache python3~=3.12
```

## 在容器中开发

在开发时，将项目目录挂载到容器中是很有用的。通过这种设置，对项目的更改可以立即反映在容器化服务中，而无需重建镜像。然而，重要的是 _不要_ 将项目虚拟环境 (`.venv`) 包含在挂载中，因为虚拟环境是平台特定的，应该保留为镜像构建的那个。

### 使用 `docker run` 挂载项目

将项目（在工作目录中）绑定挂载到 `/app`，同时使用[匿名卷](https://docs.docker.com/engine/storage/#volumes)保留 `.venv` 目录：

```console
$ docker run --rm --volume .:/app --volume /app/.venv [...]
```

!!! tip

    包含 `--rm` 标志是为了确保在容器退出时清理容器和匿名卷。

请参阅 [`uv-docker-example` 项目](https://github.com/astral-sh/uv-docker-example/blob/main/run.sh)中的完整示例。

### 使用 `docker compose` 配置 `watch`

当使用 Docker compose 时，有更复杂的工具可用于容器开发。[`watch`](https://docs.docker.com/compose/file-watch/#compose-watch-versus-bind-mounts) 选项允许比绑定挂载更精细的粒度，并支持在文件更改时触发对容器化服务的更新。

!!! note

    此功能需要 Compose 2.22.0，该版本与 Docker Desktop 4.24 捆绑在一起。

在你的 [Docker compose 文件](https://docs.docker.com/compose/compose-application-model/#the-compose-file)中配置 `watch`，以挂载项目目录而不同步项目虚拟环境，并在配置更改时重建镜像：

```yaml title="compose.yaml"
services:
  example:
    build: .

    # ...

    develop:
      # 创建一个 `watch` 配置来更新应用
      #
      watch:
        # 将工作目录与容器中的 `/app` 目录同步
        - action: sync
          path: .
          target: /app
          # 排除项目虚拟环境
          ignore:
            - .venv/

        # 在 `pyproject.toml` 更改时重建镜像
        - action: rebuild
          path: ./pyproject.toml
```

然后，运行 `docker compose watch` 以使用开发设置运行容器。

请参阅 [`uv-docker-example` 项目](https://github.com/astral-sh/uv-docker-example/blob/main/compose.yml)中的完整示例。

## 优化

### 编译字节码

将 Python 源文件编译为字节码通常对于生产镜像来说是可取的，因为它往往能提高启动时间（以增加安装时间为代价）。

要启用字节码编译，请使用 `--compile-bytecode` 标志：

```dockerfile title="Dockerfile"
RUN uv sync --compile-bytecode
```

或者，你可以设置 `UV_COMPILE_BYTECODE` 环境变量，以确保 Dockerfile 中的所有命令都编译字节码：

```dockerfile title="Dockerfile"
ENV UV_COMPILE_BYTECODE=1
```

### 缓存

可以使用[缓存挂载](https://docs.docker.com/build/guide/mounts/#add-a-cache-mount)来提高跨构建的性能：

```dockerfile title="Dockerfile"
ENV UV_LINK_MODE=copy

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync
```

更改默认的 [`UV_LINK_MODE`](../../reference/settings/configuration.md#link-mode) 可以消除关于无法使用硬链接的警告，因为缓存和同步目标位于不同的文件系统上。

如果你不挂载缓存，可以通过使用 `--no-cache` 标志或设置 `UV_NO_CACHE` 来减小镜像大小。

!!! note

    缓存目录的位置可以通过在容器中运行 `uv cache dir` 命令来确定。

    或者，可以将缓存设置为一个常量位置：

    ```dockerfile title="Dockerfile"
    ENV UV_CACHE_DIR=/opt/uv-cache/
    ```

### 中间层

如果你使用 uv 管理你的项目，你可以通过 `--no-install` 选项将你的传递依赖项安装移动到其自己的层中，从而提高构建时间。

`uv sync --no-install-project` 将安装项目的依赖项，但不会安装项目本身。由于项目经常更改，但其依赖项通常是静态的，这可以节省大量时间。

```dockerfile title="Dockerfile"
# 安装 uv
FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 将工作目录更改为 `app` 目录
WORKDIR /app

# 安装依赖项
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

# 将项目复制到镜像中
ADD . /app

# 同步项目
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked
```

请注意，`pyproject.toml` 是识别项目根和名称所必需的，但项目 _内容_ 在最后的 `uv sync` 命令之前不会被复制到镜像中。

!!! tip

    如果你正在使用[工作区](../../concepts/projects/workspaces.md)，那么请使用 `--no-install-workspace` 标志，它会排除项目 _和_ 任何工作区成员。

    如果你想从同步中移除特定的包，请使用 `--no-install-package <name>`。

### 非可编辑安装

默认情况下，uv 以可编辑模式安装项目和工作区成员，这样对源代码的更改会立即反映在环境中。

`uv sync` 和 `uv run` 都接受一个 `--no-editable` 标志，它指示 uv 以非可编辑模式安装项目，从而移除对源代码的任何依赖。

在多阶段 Docker 镜像的上下文中，`--no-editable` 可用于将项目包含在一个阶段的同步虚拟环境中，然后仅将虚拟环境（而不是源代码）复制到最终镜像中。

例如：

```dockerfile title="Dockerfile"
# 安装 uv
FROM python:3.12-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 将工作目录更改为 `app` 目录
WORKDIR /app

# 安装依赖项
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-editable

# 将项目复制到中间镜像中
ADD . /app

# 同步项目
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-editable

FROM python:3.12-slim

# 复制环境，但不复制源代码
COPY --from=builder --chown=app:app /app/.venv /app/.venv

# 运行应用程序
CMD ["/app/.venv/bin/hello"]
```

### 临时使用 uv

如果最终镜像中不需要 uv，可以在每次调用时挂载二进制文件：

```dockerfile title="Dockerfile"
RUN --mount=from=ghcr.io/astral-sh/uv,source=/uv,target=/bin/uv \
    uv sync
```

## 使用 pip 接口

### 安装包

在这种情况下，使用系统 Python 环境是安全的，因为容器已经是隔离的。可以使用 `--system` 标志在系统环境中安装：

```dockerfile title="Dockerfile"
RUN uv pip install --system ruff
```

要默认使用系统 Python 环境，请设置 `UV_SYSTEM_PYTHON` 变量：

```dockerfile title="Dockerfile"
ENV UV_SYSTEM_PYTHON=1
```

或者，可以创建并激活一个虚拟环境：

```dockerfile title="Dockerfile"
RUN uv venv /opt/venv
# 自动使用虚拟环境
ENV VIRTUAL_ENV=/opt/venv
# 将环境中的入口点放在路径的前面
ENV PATH="/opt/venv/bin:$PATH"
```

当使用虚拟环境时，应从 uv 调用中省略 `--system` 标志：

```dockerfile title="Dockerfile"
RUN uv pip install ruff
```

### 安装需求

要安装需求文件，请将它们复制到容器中：

```dockerfile title="Dockerfile"
COPY requirements.txt .
RUN uv pip install -r requirements.txt
```

### 安装项目

在与需求一起安装项目时，最佳实践是将复制需求与其余源代码分开。这允许项目的依赖项（不经常更改）与项目本身（非常频繁地更改）分开缓存。

```dockerfile title="Dockerfile"
COPY pyproject.toml .
RUN uv pip install -r pyproject.toml
COPY . .
RUN uv pip install -e .
```

## 验证镜像来源

Docker 镜像在构建过程中被签名，以提供其来源的证明。这些证明可用于验证镜像是否由官方渠道生成。

例如，你可以使用 [GitHub CLI 工具 `gh`](https://cli.github.com/) 来验证证明：

```console
$ gh attestation verify --owner astral-sh oci://ghcr.io/astral-sh/uv:latest
Loaded digest sha256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx for oci://ghcr.io/astral-sh/uv:latest
Loaded 1 attestation from GitHub API

The following policy criteria will be enforced:
- OIDC Issuer must match:................... https://token.actions.githubusercontent.com
- Source Repository Owner URI must match:... https://github.com/astral-sh
- Predicate type must match:................ https://slsa.dev/provenance/v1
- Subject Alternative Name must match regex: (?i)^https://github.com/astral-sh/

✓ Verification succeeded!

sha256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx was attested by:
REPO          PREDICATE_TYPE                  WORKFLOW
astral-sh/uv  https://slsa.dev/provenance/v1  .github/workflows/build-docker.yml@refs/heads/main
```

这告诉你特定的 Docker 镜像是由官方 uv GitHub 发布工作流构建的，并且此后没有被篡改过。

GitHub 证明建立在 [sigstore.dev 基础设施](https://www.sigstore.dev/)之上。因此，你也可以使用 [`cosign` 命令](https://github.com/sigstore/cosign)来根据 `uv` 的（多平台）清单验证证明 blob：

```console
$ REPO=astral-sh/uv
$ gh attestation download --repo $REPO oci://ghcr.io/${REPO}:latest
Wrote attestations to file sha256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.jsonl.
Any previous content has been overwritten

The trusted metadata is now available at sha256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.jsonl
$ docker buildx imagetools inspect ghcr.io/${REPO}:latest --format "{{json .Manifest}}" > manifest.json
$ cosign verify-blob-attestation \
    --new-bundle-format \
    --bundle "$(jq -r .digest manifest.json).jsonl"  \
    --certificate-oidc-issuer="https://token.actions.githubusercontent.com" \
    --certificate-identity-regexp="^https://github\.com/${REPO}/.*" \
    <(jq -j '.|del(.digest,.size)' manifest.json)
Verified OK
```

!!! tip

    这些示例使用 `latest`，但最佳实践是验证特定版本标签的证明，例如 `ghcr.io/astral-sh/uv:0.8.18`，或者（甚至更好）特定的镜像摘要，例如 `ghcr.io/astral-sh/uv:0.8.18@sha256:5adf09a5a526f380237408032a9308000d14d5947eafa687ad6c6a2476787b4f`。
