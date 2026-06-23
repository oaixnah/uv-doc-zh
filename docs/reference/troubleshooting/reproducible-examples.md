---
subtitle: Reproducible examples
description: 了解如何为 uv 项目创建最小可复现例子（MRE），包括 Docker 镜像、脚本和 Git 仓库三种策略，帮助开发者高效报告和修复 bug。
---

# 可复现例子 {#reproducible-examples}

## 为什么可复现例子很重要 {#why-reproducible-examples-are-important}

最小可复现例子（Minimal Reproducible Example，简称 MRE）对于修复 bug 至关重要。如果没有一个可用于复现问题的例子，维护者就无法调试它，也无法测试修复是否有效。如果例子不够最小化，即包含大量与问题无关的内容，维护者可能需要花费更长的时间才能定位问题的根本原因。

## 如何编写可复现例子 {#how-to-write-a-reproducible-example}

编写可复现例子时，目标是提供他人在其环境中复现该问题所需的所有上下文。这包括：

- 你使用的平台（例如操作系统和架构）
- 任何相关的系统状态（例如显式设置的环境变量）
- uv 的版本
- 其他相关工具的版本
- 相关文件（`uv.lock`、`pyproject.toml` 等）
- 要运行的命令

为确保你的复现例子是最小化的，请尽可能移除多余的依赖、设置和文件。在分享之前，务必亲自测试你的复现例子。我们建议在复现例子中包含详细（verbose）日志；它们在你的机器上可能会有关键性的差异。对于非常长的日志，使用 [Gist](https://gist.github.com) 会很有帮助。

下面，我们将介绍几种创建和分享可复现例子的具体[策略](#strategies-for-reproducible-examples)。

!!! tip

    [Stack Overflow](https://stackoverflow.com/help/minimal-reproducible-example) 上有一篇关于创建 MRE 基础知识的优秀指南。

## 可复现例子的策略 {#strategies-for-reproducible-examples}

### Docker 镜像 {#docker-image}

编写 Docker 镜像通常是分享可复现例子的最佳方式，因为它完全自包含（self-contained）。这意味着复现者系统的状态不会影响问题。

!!! note

    使用 Docker 镜像仅在问题可在 Linux 上复现时才可行。在使用 macOS 时，建议先确认你的镜像在 Linux 上是否无法复现——但有些 bug 确实只针对特定操作系统。虽然使用 Docker 运行 Windows 容器是可行的，但并不常见。这类 bug 建议改用[脚本](#script)方式报告。

在使用 uv 编写 Docker MRE 时，最好从 [uv 的 Docker 镜像](../../guides/integration/docker.md#available-images)之一开始。这样做时，请务必锁定到 uv 的特定版本。

```Dockerfile
FROM ghcr.io/astral-sh/uv:0.5.24-debian-slim
```

虽然 Docker 镜像与系统隔离，但构建默认会使用你系统的架构。在分享复现例子时，你可以显式设置平台（platform），以确保复现者获得预期的行为。uv 发布了 `linux/amd64`（例如 Intel 或 AMD）和 `linux/arm64`（例如 Apple M 系列或 ARM）的镜像。

```Dockerfile
FROM --platform=linux/amd64 ghcr.io/astral-sh/uv:0.5.24-debian-slim
```

Docker 镜像最适合复现可以通过命令构建的问题，例如：

```Dockerfile
FROM --platform=linux/amd64 ghcr.io/astral-sh/uv:0.5.24-debian-slim

RUN uv init /mre
WORKDIR /mre
RUN uv add pydantic
RUN uv sync
RUN uv run -v python -c "import pydantic"
```

不过，你也可以在镜像中内联写入文件：

```Dockerfile
FROM --platform=linux/amd64 ghcr.io/astral-sh/uv:0.5.24-debian-slim

COPY <<EOF /mre/pyproject.toml
[project]
name = "example"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = ["pydantic"]
EOF

WORKDIR /mre
RUN uv lock
```

如果需要写入很多文件，更好的做法是创建并发布一个 [Git 仓库](#git-repository)。你也可以组合使用这些方法，在仓库中包含一个 `Dockerfile`。

在分享 Docker 复现例子时，包含构建日志会很有帮助。你可以通过禁用缓存和美化输出来查看构建步骤的更多输出：

```console
docker build . --progress plain --no-cache
```

### 脚本 {#script}

在报告无法在[容器](#docker-image)中复现的特定平台 bug 时，最佳实践是包含一个脚本，展示可用于复现 bug 的命令，例如：

```bash
uv init
uv add pydantic
uv sync
uv run -v python -c "import pydantic"
```

如果你的复现需要很多文件，请使用 [Git 仓库](#git-repository)来分享它们。

除了脚本之外，还需要包含失败时的*详细*日志（即带有 `-v` 标志的日志）以及完整的错误信息。

每当脚本依赖外部状态时，请务必分享这些信息。例如，如果你在 Windows 上编写了脚本，且它使用了通过 `choco` 安装的 Python 版本，并在 PowerShell 6.2 上运行，请在报告中包含这些信息。

### Git 仓库 {#git-repository}

在分享 Git 仓库复现例子时，请包含一个能复现问题的[脚本](#script)，或者更好的做法是包含一个 [Dockerfile](#docker-image)。脚本的第一步应该是克隆仓库并检出到特定的提交（commit）：

```console
$ git clone https://github.com/<user>/<project>.git
$ cd <project>
$ git checkout <commit>
$ <产生错误的命令>
```

你可以通过 [GitHub 网页界面](https://github.com/new)或 `gh` CLI 快速创建新仓库：

```console
$ gh repo create uv-mre-1234 --clone
```

使用 Git 仓库进行复现时，请记住要*最小化*内容，排除与复现问题无关的文件或设置。
