---
title: 构建和发布包
subtitle: Publishing packages
description: 一份使用 uv 构建 Python 包并将其发布到 PyPI 等包索引的完整指南，涵盖 uv build 构建、uv version 版本管理、uv publish 发布以及证明（attestations）上传等核心功能。
---

# 构建和发布包 {#building-and-publishing-a-package}

uv 支持通过 `uv build` 将 Python 包构建为源码分发包和二进制分发包，并通过 `uv publish` 将其上传到注册中心（registry）。

## 准备你的项目 {#preparing-your-project}

在尝试发布项目之前，你需要确保项目已准备好进行打包分发。

如果你的项目在 `pyproject.toml` 中没有包含 `[build-system]` 定义，uv 在执行 `uv sync` 操作时不会构建它，但在执行 `uv build` 时会回退到传统的 setuptools 构建系统。

我们强烈建议配置构建系统。有关构建系统的更多信息，请参阅[项目配置](../concepts/projects/config.md#build-systems)文档。

## 构建你的包 {#building-your-package}

使用 `uv build` 构建你的包：

```console
$ uv build
```

默认情况下，`uv build` 会构建当前目录中的项目，并将构建产物放置在 `dist/` 子目录中。

或者，`uv build <SRC>` 将构建指定目录中的包，而 `uv build --package <PACKAGE>` 将构建当前工作空间（workspace）中的指定包。

!!! info

    默认情况下，`uv build` 在从 `pyproject.toml` 的 `build-system.requires` 部分解析构建依赖项时，会遵循 `tool.uv.sources` 的配置。在发布包时，我们建议运行 `uv build --no-sources`，以确保当 `tool.uv.sources` 被禁用时（例如使用其他构建工具如 [`pypa/build`](https://github.com/pypa/build) 时），包仍能正确构建。

## 更新版本号 {#updating-your-version}

`uv version` 命令提供了在发布包之前更新版本号的便捷方式。
[查看项目文档中关于读取包版本号的部分](./projects.md#viewing-your-version)。

要更新到精确版本号，请将其作为位置参数提供：

```console
$ uv version 1.0.0
hello-world 0.7.0 => 1.0.0
```

要预览变更而不更新 `pyproject.toml`，请使用 `--dry-run` 标志：

```console
$ uv version 2.0.0 --dry-run
hello-world 1.0.0 => 2.0.0
$ uv version
hello-world 1.0.0
```

要按语义化版本递增包的版本号，请使用 `--bump` 选项：

```console
$ uv version --bump minor
hello-world 1.2.3 => 1.3.0
```

`--bump` 选项支持以下常见的版本组件：`major`、`minor`、`patch`、`stable`、`alpha`、`beta`、`rc`、`post` 和 `dev`。当多次提供时，组件将按从大到小（`major` 到 `dev`）的顺序依次应用。

你也可以通过 `--bump <component>=<value>` 提供一个数值来显式设置结果组件：

```console
$ uv version --bump patch --bump dev=66463664
hello-world 0.0.1 => 0.0.2.dev66463664
```

要从稳定版过渡到预发布版，除了递增预发布组件外，还需要递增 major、minor 或 patch 组件之一：

```console
$ uv version --bump patch --bump beta
hello-world 1.3.0 => 1.3.1b1
$ uv version --bump major --bump alpha
hello-world 1.3.0 => 2.0.0a1
```

从预发布版过渡到新的预发布版时，只需递增相关的预发布组件即可：

```console
$ uv version --bump beta
hello-world 1.3.0b1 => 1.3.0b2
```

从预发布版过渡到稳定版时，可以使用 `stable` 选项来清除预发布组件：

```console
$ uv version --bump stable
hello-world 1.3.1b2 => 1.3.1
```

!!! info

    默认情况下，当 `uv version` 修改项目时，它会执行锁定（lock）和同步（sync）操作。要阻止锁定和同步，请使用 `--frozen`；如果只想阻止同步，请使用 `--no-sync`。

## 发布你的包 {#publishing-your-package}

!!! note

    关于从 GitHub Actions 发布到 PyPI 的完整指南，请参阅 [GitHub 指南](integration/github.md#publishing-to-pypi)。

使用 `uv publish` 发布你的包：

```console
$ uv publish
```

通过 `--token` 或 `UV_PUBLISH_TOKEN` 设置 PyPI 令牌（token），或者通过 `--username` 或 `UV_PUBLISH_USERNAME` 设置用户名，并通过 `--password` 或 `UV_PUBLISH_PASSWORD` 设置密码。对于从 GitHub Actions 或其他受信任发布者（Trusted Publisher）发布到 PyPI，你无需设置任何凭据。相反，请[为 PyPI 项目添加受信任发布者](https://docs.pypi.org/trusted-publishers/adding-a-publisher/)。

!!! note

    PyPI 已不再支持使用用户名和密码进行发布，你需要生成一个令牌。使用令牌等同于设置 `--username __token__` 并将令牌作为密码使用。

如果你通过 `[[tool.uv.index]]` 使用自定义索引，请添加 `publish-url` 并使用 `uv publish --index <name>`。例如：

```toml
[[tool.uv.index]]
name = "testpypi"
url = "https://test.pypi.org/simple/"
publish-url = "https://test.pypi.org/legacy/"
explicit = true
```

!!! note

    使用 `uv publish --index <name>` 时，`pyproject.toml` 必须存在，即你需要在发布 CI 作业中包含检出（checkout）步骤。

尽管 `uv publish` 会重试失败的上传，但发布过程仍可能在中间失败，导致部分文件已上传而部分文件缺失。对于 PyPI，你可以重试完全相同的命令，已存在的相同文件将被忽略。对于其他注册中心，请使用 `--check-url <index url>` 并指定包所属的索引 URL（而非发布 URL）。当使用 `--index` 时，索引 URL 将被用作检查 URL。uv 将跳过上传与注册中心中已有文件完全相同的文件，并且还会处理并发的竞态上传。请注意，现有文件必须与之前上传到注册中心的文件完全匹配，这可以避免意外发布同一版本的源码分发包和 wheel 包内容不一致的情况。

### 随包上传证明 {#uploading-attestations-with-your-package}

!!! note

    某些第三方包索引可能不支持证明（attestations），并且可能会拒绝包含证明的上传（而不是静默忽略它们）。如果你在上传时遇到问题，可以使用 `--no-attestations` 或 `UV_PUBLISH_NO_ATTESTATIONS` 禁用 uv 的默认行为。

!!! tip

    `uv publish` 目前不会生成证明；证明必须在发布之前单独创建。

`uv publish` 支持将[证明](https://peps.python.org/pep-0740/)上传到支持它们的注册中心（如 PyPI）。

uv 会自动发现并匹配证明。例如，给定以下 `dist/` 目录，`uv publish` 将随相应的分发包一起上传证明：

```console
$ ls dist/
hello_world-1.0.0-py3-none-any.whl
hello_world-1.0.0-py3-none-any.whl.publish.attestation
hello_world-1.0.0.tar.gz
hello_world-1.0.0.tar.gz.publish.attestation
```

## 安装你的包 {#installing-your-package}

使用 `uv run` 测试包是否可以安装和导入：

```console
$ uv run --with <PACKAGE> --no-project -- python -c "import <PACKAGE>"
```

`--no-project` 标志用于避免从本地项目目录安装包。

!!! tip

    如果你最近安装过该包，可能需要包含 `--refresh-package <PACKAGE>` 选项，以避免使用缓存的包版本。

## 下一步 {#next-steps}

要了解更多关于发布包的信息，请查阅 [PyPA 指南](https://packaging.python.org/en/latest/guides/section-build-and-publish/)中关于构建和发布的部分。

或者，继续阅读关于[将 uv 与其他软件集成](./integration/index.md)的指南。
