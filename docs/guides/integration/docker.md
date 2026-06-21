---
title: 在 Docker 中使用 uv
description: 一份在 Docker 中使用 uv 管理 Python 依赖的完整指南，同时通过多阶段构建、中间层等方式优化构建时间和镜像大小。
---

# 在 Docker 中使用 uv

## 快速入门

!!! tip

    请查阅 [`uv-docker-example`](https://github.com/astral-sh/uv-docker-example) 项目，了解在 Docker 中使用 uv 构建应用的最佳实践示例。

uv 提供了两种类型的 Docker 镜像：_distroless_（无发行版）镜像，适用于[将 uv 二进制文件复制](#installing-uv)到你自己的镜像构建中；以及基于主流基础镜像的衍生镜像，适用于在容器中使用 uv。distroless 镜像仅包含 uv 二进制文件，不包含其他任何内容。而衍生镜像则包含预装了 uv 的操作系统。

例如，要在基于 Debian 的镜像中运行 uv：

```console
$ docker run --rm -it ghcr.io/astral-sh/uv:debian uv --help
```

### 可用镜像

以下 distroless 镜像可供使用：

- `ghcr.io/astral-sh/uv:latest`
- `ghcr.io/astral-sh/uv:{major}.{minor}.{patch}`，例如 `ghcr.io/astral-sh/uv:0.11.23`
- `ghcr.io/astral-sh/uv:{major}.{minor}`，例如 `ghcr.io/astral-sh/uv:0.8`（最新的补丁版本）

以下衍生镜像可供使用：

<!-- prettier-ignore -->
- 基于 `alpine:3.23`：
    - `ghcr.io/astral-sh/uv:alpine`
    - `ghcr.io/astral-sh/uv:alpine3.23`
- 基于 `alpine:3.22`：
    - `ghcr.io/astral-sh/uv:alpine3.22`
- 基于 `debian:trixie-slim`：
    - `ghcr.io/astral-sh/uv:debian-slim`
    - `ghcr.io/astral-sh/uv:trixie-slim`
- 基于 `buildpack-deps:trixie`：
    - `ghcr.io/astral-sh/uv:debian`
    - `ghcr.io/astral-sh/uv:trixie`
- 基于 `dhi.io/alpine-base:3.23`：
    - `ghcr.io/astral-sh/uv:alpine-dhi`
    - `ghcr.io/astral-sh/uv:alpine3.23-dhi`
- 基于 `dhi.io/debian-base:trixie-debian13`：
    - `ghcr.io/astral-sh/uv:debian-dhi`
    - `ghcr.io/astral-sh/uv:trixie-dhi`
- 基于 `dhi/python:3.x`：
    - `ghcr.io/astral-sh/uv:python3.14-dhi`
    - `ghcr.io/astral-sh/uv:python3.13-dhi`
    - `ghcr.io/astral-sh/uv:python3.12-dhi`
    - `ghcr.io/astral-sh/uv:python3.11-dhi`
    - `ghcr.io/astral-sh/uv:python3.10-dhi`
- 基于 `python3.x-alpine`：
    - `ghcr.io/astral-sh/uv:python3.14-alpine`
    - `ghcr.io/astral-sh/uv:python3.14-alpine3.23`
    - `ghcr.io/astral-sh/uv:python3.13-alpine`
    - `ghcr.io/astral-sh/uv:python3.13-alpine3.23`
    - `ghcr.io/astral-sh/uv:python3.12-alpine`
    - `ghcr.io/astral-sh/uv:python3.12-alpine3.23`
    - `ghcr.io/astral-sh/uv:python3.11-alpine`
    - `ghcr.io/astral-sh/uv:python3.11-alpine3.23`
    - `ghcr.io/astral-sh/uv:python3.10-alpine`
    - `ghcr.io/astral-sh/uv:python3.10-alpine3.23`
    - `ghcr.io/astral-sh/uv:python3.9-alpine`
    - `ghcr.io/astral-sh/uv:python3.9-alpine3.22`
- 基于 `python3.x-trixie`：
    - `ghcr.io/astral-sh/uv:python3.14-trixie`
    - `ghcr.io/astral-sh/uv:python3.13-trixie`
    - `ghcr.io/astral-sh/uv:python3.12-trixie`
    - `ghcr.io/astral-sh/uv:python3.11-trixie`
    - `ghcr.io/astral-sh/uv:python3.10-trixie`
    - `ghcr.io/astral-sh/uv:python3.9-trixie`
- 基于 `python3.x-slim-trixie`：
    - `ghcr.io/astral-sh/uv:python3.14-trixie-slim`
    - `ghcr.io/astral-sh/uv:python3.13-trixie-slim`
    - `ghcr.io/astral-sh/uv:python3.12-trixie-slim`
    - `ghcr.io/astral-sh/uv:python3.11-trixie-slim`
    - `ghcr.io/astral-sh/uv:python3.10-trixie-slim`
    - `ghcr.io/astral-sh/uv:python3.9-trixie-slim`
<!-- prettier-ignore-end -->

与 distroless 镜像一样，每个衍生镜像都会发布带有 uv 版本标签的镜像，格式为
`ghcr.io/astral-sh/uv:{major}.{minor}.{patch}-{base}` 和
`ghcr.io/astral-sh/uv:{major}.{minor}-{base}`，例如 `ghcr.io/astral-sh/uv:0.11.23-alpine`。

此外，从 `0.8` 版本开始，每个衍生镜像还会将 `UV_TOOL_BIN_DIR` 设置为 `/usr/local/bin`，以便 `uv tool install` 在使用默认用户时能按预期工作。

更多详情，请参阅 [GitHub Container](https://github.com/astral-sh/uv/pkgs/container/uv) 页面。

### 安装 uv

使用上述预装了 uv 的镜像，或者通过从官方 distroless Docker 镜像复制二进制文件来安装 uv：

```dockerfile title="Dockerfile"
FROM python:3.12-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
```

或者，使用安装脚本：

```dockerfile title="Dockerfile"
FROM python:3.12-slim-trixie

# 安装脚本需要 curl（和证书）来下载发布存档
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# 下载最新的安装脚本
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# 运行安装脚本然后删除它
RUN sh /uv-installer.sh && rm /uv-installer.sh

# 确保已安装的二进制文件在 `PATH` 中
ENV PATH="/root/.local/bin/:$PATH"
```

注意，这需要 `curl` 可用。

无论哪种方式，最佳实践是固定到特定的 uv 版本，例如：

```dockerfile
COPY --from=ghcr.io/astral-sh/uv:0.11.23 /uv /uvx /bin/
```

!!! tip

    虽然上面的 Dockerfile 示例固定到了特定标签，但也可以固定到特定的 SHA256。在需要可重现构建的环境中，固定特定 SHA256 被认为是最佳实践，因为标签可能会被移动到不同的提交 SHA 上。

    ```Dockerfile
    # 例如，使用之前发布版本的哈希值
    COPY --from=ghcr.io/astral-sh/uv@sha256:2381d6aa60c326b71fd40023f921a0a3b8f91b14d5db6b90402e65a635053709 /uv /uvx /bin/
    ```

或者，使用安装脚本：

```dockerfile
ADD https://astral.sh/uv/0.11.23/install.sh /uv-installer.sh
```

### 安装项目

如果你使用 uv 管理项目，可以将项目复制到镜像中并安装：

```dockerfile title="Dockerfile"
# 将项目复制到镜像中
COPY . /app

# 禁用开发依赖
ENV UV_NO_DEV=1

# 将项目同步到新环境中，并断言锁文件是最新的
WORKDIR /app
RUN uv sync --locked
```

!!! important

    最佳实践是在仓库的 [`.dockerignore` 文件](https://docs.docker.com/build/concepts/context/#dockerignore-files)中添加 `.venv`，以防止其被包含在镜像构建中。项目虚拟环境依赖于你的本地平台，应该在镜像中从头创建。

然后，默认启动你的应用：

```dockerfile title="Dockerfile"
# 假设项目提供了一个 `my_app` 命令
CMD ["uv", "run", "my_app"]
```

!!! tip

    最佳实践是使用[中间层](#intermediate-layers)将依赖安装和项目本身分开，以改善 Docker 镜像构建时间。

请参阅 [`uv-docker-example` 项目](https://github.com/astral-sh/uv-docker-example/blob/main/Dockerfile)中的完整示例。

### 使用环境

项目安装完成后，你可以通过将项目的虚拟环境二进制目录置于路径前部来_激活_它：

```dockerfile title="Dockerfile"
ENV PATH="/app/.venv/bin:$PATH"
```

或者，你可以对任何需要该环境的命令使用 `uv run`：

```dockerfile title="Dockerfile"
RUN uv run some_script.py
```

!!! tip

    或者，可以在同步之前设置 [`UV_PROJECT_ENVIRONMENT` 设置](../../concepts/projects/config.md#project-environment-path)，将项目安装到系统 Python 环境中，完全跳过环境激活步骤。

### 使用已安装的工具

要使用已安装的工具，请确保[工具 bin 目录](../../concepts/tools.md#tool-executables)在路径中：

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

    或者，可以将其设置为固定位置：

    ```dockerfile title="Dockerfile"
    ENV UV_TOOL_BIN_DIR=/opt/uv-bin/
    ```

## 在容器中开发

在开发时，将项目目录挂载到容器中非常有用。通过这种设置，对项目的更改可以立即反映到容器化服务中，而无需重新构建镜像。但是，重要的是_不要_将项目虚拟环境（`.venv`）包含在挂载中，因为虚拟环境是平台相关的，应该保留为镜像构建的那个。

### 使用 `docker run` 挂载项目

通过[匿名卷（anonymous volume）](https://docs.docker.com/engine/storage/#volumes)将项目（当前工作目录）绑定挂载到 `/app`，同时保留 `.venv` 目录：

```console
$ docker run --rm --volume .:/app --volume /app/.venv [...]
```

!!! tip

    `--rm` 标志用于确保容器退出时，容器和匿名卷都会被清理。

请参阅 [`uv-docker-example` 项目](https://github.com/astral-sh/uv-docker-example/blob/main/run.sh)中的完整示例。

### 使用 `docker compose` 配置 `watch`

使用 Docker compose 时，有更复杂的工具可用于容器开发。[`watch`](https://docs.docker.com/compose/file-watch/#compose-watch-versus-bind-mounts) 选项提供了比绑定挂载更精细的控制粒度，并支持在文件更改时触发容器化服务的更新。

!!! note

    此功能需要 Compose 2.22.0，该版本随 Docker Desktop 4.24 一起提供。

在你的 [Docker compose 文件](https://docs.docker.com/compose/compose-application-model/#the-compose-file)中配置 `watch`，以挂载项目目录但不同步项目虚拟环境，并在配置更改时重建镜像：

```yaml title="compose.yaml"
services:
  example:
    build: .

    # ...

    develop:
      # 创建 `watch` 配置以更新应用
      #
      watch:
        # 将工作目录与容器中的 `/app` 目录同步
        - action: sync
          path: .
          target: /app
          # 排除项目虚拟环境
          ignore:
            - .venv/

        # 当 `pyproject.toml` 更改时重建镜像
        - action: rebuild
          path: ./pyproject.toml
```

然后，运行 `docker compose watch` 以使用开发设置运行容器。

请参阅 [`uv-docker-example` 项目](https://github.com/astral-sh/uv-docker-example/blob/main/compose.yml)中的完整示例。

## 优化

### 编译字节码

对于生产镜像，将 Python 源文件编译为字节码通常是可取的，因为这往往能改善启动时间（代价是增加安装时间和镜像大小）。

要启用字节码编译，请使用 `--compile-bytecode` 标志：

```dockerfile title="Dockerfile"
RUN uv python install --compile-bytecode
RUN uv sync --compile-bytecode
```

或者，你可以设置 `UV_COMPILE_BYTECODE` 环境变量，以确保 Dockerfile 中的所有命令都编译字节码：

```dockerfile title="Dockerfile"
ENV UV_COMPILE_BYTECODE=1
```

!!! note

    uv 只会在 `uv python install` 期间编译_受管（managed）_ Python 版本的标准库。非受管 Python 版本的发行商决定标准库是否预编译。例如，官方的 `python` 镜像不会有已编译的标准库。

### 缓存

可以使用[缓存挂载（cache mount）](https://docs.docker.com/build/guide/mounts/#add-a-cache-mount)来提高跨构建的性能：

```dockerfile title="Dockerfile"
ENV UV_LINK_MODE=copy

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync
```

更改 [`UV_LINK_MODE`](../../reference/settings.md#link-mode) 可以消除关于无法链接文件的警告，因为缓存和同步目标位于不同的文件系统上。

如果你不挂载缓存，可以通过使用 `--no-cache` 标志或设置 `UV_NO_CACHE` 来减小镜像大小。

默认情况下，受管的 Python 安装不会在安装前缓存。设置 `UV_PYTHON_CACHE_DIR` 可以与缓存挂载结合使用：

```dockerfile title="Dockerfile"
ENV UV_PYTHON_CACHE_DIR=/root/.cache/uv/python

RUN --mount=type=cache,target=/root/.cache/uv \
    uv python install
```

!!! note

    缓存目录的位置可以通过在容器中运行 `uv cache dir` 命令来确定。

    或者，可以将缓存设置为固定位置：

    ```dockerfile title="Dockerfile"
    ENV UV_CACHE_DIR=/opt/uv-cache/
    ```

### 中间层

如果你使用 uv 管理项目，可以通过 `--no-install` 选项将传递依赖的安装移到单独的一层中，从而改善构建时间。

`uv sync --no-install-project` 将安装项目的依赖但不安装项目本身。由于项目经常变化，但其依赖通常是静态的，这可以大大节省时间。

```dockerfile title="Dockerfile"
# 安装 uv
FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 将工作目录切换到 `app` 目录
WORKDIR /app

# 安装依赖
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

# 将项目复制到镜像中
COPY . /app

# 同步项目
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked
```

请注意，`pyproject.toml` 是识别项目根目录和名称所必需的，但项目的_内容_直到最后的 `uv sync` 命令才会被复制到镜像中。

!!! tip

    如果你想从同步中移除额外的特定包，请使用 `--no-install-package <name>`。

#### 工作空间中的中间层

如果你使用[工作空间（workspace）](../../concepts/projects/workspaces.md)，则需要做一些调整：

- 在初始同步期间使用 `--frozen` 而不是 `--locked`。
- 使用 `--no-install-workspace` 标志，该标志排除项目_以及_任何工作空间成员。

```dockerfile title="Dockerfile"
# 安装 uv
FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-workspace

COPY . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked
```

uv 在没有每个工作空间成员的 `pyproject.toml` 文件的情况下无法断言 `uv.lock` 文件是最新的，因此我们在初始同步期间使用 `--frozen` 而不是 `--locked` 来跳过检查。在复制所有工作空间成员之后的下一次同步，仍然可以使用 `--locked`，并将验证锁文件对所有工作空间成员是否正确。

### 非可编辑安装

默认情况下，uv 以可编辑模式（editable mode）安装项目和工作空间成员，这样对源代码的更改会立即反映到环境中。

`uv sync` 和 `uv run` 都接受 `--no-editable` 标志，该标志指示 uv 以非可编辑模式安装项目，移除对源代码的任何依赖。

在多阶段 Docker 镜像的上下文中，`--no-editable` 可以用于在一个阶段中将项目包含在同步的虚拟环境中，然后仅将虚拟环境（而不是源代码）复制到最终镜像中。

例如：

```dockerfile title="Dockerfile"
# 安装 uv
FROM python:3.12-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 在两个阶段中都使用系统 Python
ENV UV_PYTHON_DOWNLOADS=0

# 将工作目录切换到 `app` 目录
WORKDIR /app

# 安装依赖
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-editable

# 将项目复制到中间镜像中
COPY . /app

# 同步项目
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-editable

FROM python:3.12-slim

# 复制环境，但不复制源代码
COPY --from=builder /app/.venv /app/.venv

# 运行应用
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

在这种上下文中，系统 Python 环境可以安全使用，因为容器已经是隔离的。可以使用 `--system` 标志在系统环境中安装：

```dockerfile title="Dockerfile"
RUN uv pip install --system ruff
```

要默认使用系统 Python 环境，请设置 `UV_SYSTEM_PYTHON` 变量：

```dockerfile title="Dockerfile"
ENV UV_SYSTEM_PYTHON=1
```

或者，可以创建并激活虚拟环境：

```dockerfile title="Dockerfile"
RUN uv venv /opt/venv
# 自动使用虚拟环境
ENV VIRTUAL_ENV=/opt/venv
# 将环境中的入口点置于路径前部
ENV PATH="/opt/venv/bin:$PATH"
```

当使用虚拟环境时，uv 调用中应省略 `--system` 标志：

```dockerfile title="Dockerfile"
RUN uv pip install ruff
```

### 安装 requirements 文件

要安装 requirements 文件，将其复制到容器中：

```dockerfile title="Dockerfile"
COPY requirements.txt .
RUN uv pip install -r requirements.txt
```

### 安装项目

在安装项目的同时安装 requirements 时，最佳实践是将 requirements 的复制与源代码的其余部分分开。这使得项目的依赖（不经常更改）可以与项目本身（经常更改）分开缓存。

```dockerfile title="Dockerfile"
COPY pyproject.toml .
RUN uv pip install -r pyproject.toml
COPY . .
RUN uv pip install -e .
```

## 验证镜像来源

Docker 镜像在构建过程中进行了签名，以提供其来源证明。这些证明（attestations）可用于验证镜像是否来自官方渠道。

例如，你可以使用 [GitHub CLI 工具 `gh`](https://cli.github.com/) 验证证明：

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

这告诉你，特定的 Docker 镜像是由官方的 uv GitHub 发布工作流构建的，并且自那以后没有被篡改。

GitHub 证明基于 [sigstore.dev 基础设施](https://www.sigstore.dev/)。因此，你也可以使用 [`cosign` 命令](https://github.com/sigstore/cosign) 来验证针对 `uv` 的（多平台）清单的证明 blob：

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

    这些示例使用了 `latest`，但最佳实践是验证特定版本标签的证明，例如 `ghcr.io/astral-sh/uv:0.11.23`，或者（更好的是）特定的镜像摘要，例如 `ghcr.io/astral-sh/uv:0.5.27@sha256:5adf09a5a526f380237408032a9308000d14d5947eafa687ad6c6a2476787b4f`。
