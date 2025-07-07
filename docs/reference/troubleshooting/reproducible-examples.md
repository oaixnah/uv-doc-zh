---
subtitle: Reproducible examples
---

# 可复现的例子

## 为什么可复现的例子很重要

一个最小可复现例子（MRE）对于修复 bug 至关重要。如果没有可用于复现问题的例子，维护者就无法调试或测试问题是否已修复。如果例子不是最小的，即包含大量与问题无关的内容，维护者可能需要更长的时间来确定问题的根本原因。

## 如何编写可复现的例子

在编写可复现的例子时，目标是提供所有必要的上下文，以便其他人可以复现你的例子。这包括：

- 你正在使用的平台（例如，操作系统和架构）
- 任何相关的系统状态（例如，明确设置的环境变量）
- uv 的版本
- 其他相关工具的版本
- 相关文件（`uv.lock`、`pyproject.toml` 等）
- 要运行的命令

为确保你的复现是最小的，请尽可能多地删除不必要的依赖项、设置和文件。在分享之前，请务必测试你的复现。我们建议在你的复现中包含详细的日志；它们在你的机器上可能会有关键性的差异。对于非常长的日志，使用 [Gist](https://gist.github.com) 会很有帮助。

下面，我们将介绍几种创建和分享可复现例子的具体[策略](#_4)。

!!! tip

    [Stack Overflow](https://stackoverflow.com/help/minimal-reproducible-example) 上有一篇关于创建 MRE 基础知识的优秀指南。

## 可复现例子的策略

### Docker 镜像

编写 Docker 镜像通常是分享可复现例子的最佳方式，因为它是完全自包含的。这意味着复现者的系统状态不会影响问题。

!!! note

    使用 Docker 镜像仅在问题可在 Linux 上复现时才可行。在使用 macOS 时，最好确保你的镜像在 Linux 上是不可复现的，但有些 bug 确实是特定于操作系统的。虽然使用 Docker 运行 Windows 容器是可行的，但这并不常见。这类 bug 预计会以[脚本](#脚本)的形式报告。

在使用 uv 编写 Docker MRE 时，最好从 [uv 的 Docker 镜像](../../guides/integration/docker.md#_2)之一开始。这样做时，请务必固定到 uv 的特定版本。

```Dockerfile
FROM ghcr.io/astral-sh/uv:0.5.24-debian-slim
```

虽然 Docker 镜像与系统隔离，但默认情况下，构建将使用你系统的架构。在分享复现时，你可以明确设置平台，以确保复现者获得预期的行为。uv 为 `linux/amd64`（例如，Intel 或 AMD）和 `linux/arm64`（例如，Apple M 系列或 ARM）发布了镜像。

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

但是，你也可以在镜像中内联写入文件：

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

如果你需要写入许多文件，最好创建并发布一个 [Git 仓库](#git)。你可以将这些方法结合起来，并在仓库中包含一个 `Dockerfile`。

在分享 Docker 复现时，包含构建日志会很有帮助。通过禁用缓存和精美输出，你可以看到构建步骤的更多输出：

```console
docker build . --progress plain --no-cache
```

### 脚本

在报告无法在[容器](#docker)中复现的平台特定 bug 时，最佳实践是包含一个显示可用于复现 bug 的命令的脚本，例如：

```bash
uv init
uv add pydantic
uv sync
uv run -v python -c "import pydantic"
```

如果你的复现需要许多文件，请使用 [Git 仓库](#git-仓库)来分享它们。

除了脚本之外，还应包括失败的_详细_日志（即带有 `-v` 标志）和完整的错误消息。

每当脚本依赖于外部状态时，请务必分享该信息。例如，如果你在 Windows 上编写脚本，并且它使用了你用 `choco` 安装的 Python 版本并在 PowerShell 6.2 上运行，请在报告中包含这些信息。

### Git 仓库

在分享 Git 仓库复现时，请包含一个复现问题的[脚本](#_5)，或者更好的是，一个 [Dockerfile](#docker)。脚本的第一步应该是克隆仓库并检出特定的提交：

```console
$ git clone https://github.com/<user>/<project>.git
$ cd <project>
$ git checkout <commit>
$ <commands to produce error>
```

你可以使用 [GitHub UI](https://github.com/new) 或 `gh` CLI 快速创建一个新仓库：

```console
$ gh repo create uv-mre-1234 --clone
```

在使用 Git 仓库进行复现时，请记住通过排除不需要复现问题的文件或设置来_最小化_内容。
