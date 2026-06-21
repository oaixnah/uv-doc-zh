---
title: 构建和发布包
subtitle: Publishing packages
description: 一份使用 uv 构建 Python 包并将其发布到包索引（如 PyPI）的指南。
---

# 构建和发布包

uv 支持通过 `uv build` 将 Python 包构建为源码分发和二进制分发，并通过 `uv publish` 将它们上传到注册中心。

## 准备你的项目

在尝试发布项目之前，你需要确保它已经准备好被打包分发。

如果你的项目在 `pyproject.toml` 中没有包含 `[build-system]` 定义，uv 在项目的 `uv sync` 操作期间不会构建它，但在 `uv build` 期间会回退到传统的 setuptools 构建系统。

我们强烈建议配置一个构建系统。有关构建系统的更多信息，请参阅[项目配置](../concepts/projects/config.md#build-systems)文档。

## 构建你的包

使用 `uv build` 构建你的包：

```console
$ uv build
```

默认情况下，`uv build` 会构建当前目录中的项目，并将构建产物放在 `dist/` 子目录中。

你也可以使用 `uv build <SRC>` 构建指定目录中的包，或使用 `uv build --package <PACKAGE>` 构建当前工作空间中的指定包。

!!! info

    默认情况下，`uv build` 在从 `pyproject.toml` 的 `build-system.requires` 部分解析构建依赖时，会遵循 `tool.uv.sources` 配置。在发布包时，我们建议运行 `uv build --no-sources`，以确保在 `tool.uv.sources` 被禁用的情况下包也能正确构建，就像使用其他构建工具（如 [`pypa/build`](https://github.com/pypa/build)）时的情况一样。

## 更新你的版本

`uv version` 命令提供了一些便捷功能，方便你在发布包之前更新版本号。有关查看包版本的详细信息，请参阅[项目文档](./projects.md#viewing-your-version)。

要更新到精确版本，请将其作为位置参数提供：

```console
$ uv version 1.0.0
hello-world 0.7.0 => 1.0.0
```

要预览更改而不实际更新 `pyproject.toml`，请使用 `--dry-run` 标志：

```console
$ uv version 2.0.0 --dry-run
hello-world 1.0.0 => 2.0.0
$ uv version
hello-world 1.0.0
```

要按语义化版本递增包的版本，请使用 `--bump` 选项：

```console
$ uv version --bump minor
hello-world 1.2.3 => 1.3.0
```

`--bump` 选项支持以下常见的版本组件：`major`（主版本）、`minor`（次版本）、`patch`（修订版本）、`stable`（稳定版）、`alpha`、`beta`、`rc`、`post` 和 `dev`。当多次提供时，组件将按从大到小（从 `major` 到 `dev`）的顺序依次应用。

你还可以通过 `--bump <component>=<value>` 提供数值来显式设置结果组件：

```console
$ uv version --bump patch --bump dev=66463664
hello-world 0.0.1 => 0.0.2.dev66463664
```

要从稳定版迁移到预发布版本，请在递增预发布组件的同时，递增 major、minor 或 patch 组件之一：

```console
$ uv version --bump patch --bump beta
hello-world 1.3.0 => 1.3.1b1
$ uv version --bump major --bump alpha
hello-world 1.3.0 => 2.0.0a1
```

当从一个预发布版本迁移到新的预发布版本时，只需递增相关的预发布组件即可：

```console
$ uv version --bump beta
hello-world 1.3.0b1 => 1.3.0b2
```

当从预发布版本迁移到稳定版本时，可以使用 `stable` 选项来清除预发布组件：

```console
$ uv version --bump stable
hello-world 1.3.1b2 => 1.3.1
```

!!! info

    默认情况下，当 `uv version` 修改项目时，它会执行锁定和同步操作。要阻止锁定和同步，请使用 `--frozen`，或者仅阻止同步，请使用 `--no-sync`。

## 发布你的包

!!! note

    从 GitHub Actions 发布到 PyPI 的完整指南可以在 [GitHub 指南](integration/github.md#publishing-to-pypi)中找到。

使用 `uv publish` 发布你的包：

```console
$ uv publish
```

通过 `--token` 或 `UV_PUBLISH_TOKEN` 设置 PyPI 令牌，或通过 `--username` 或 `UV_PUBLISH_USERNAME` 设置用户名，并通过 `--password` 或 `UV_PUBLISH_PASSWORD` 设置密码。对于从 GitHub Actions 或其他受信任发布者（Trusted Publisher）发布到 PyPI，你无需设置任何凭据。相反，请[将受信任发布者添加到 PyPI 项目](https://docs.pypi.org/trusted-publishers/adding-a-publisher/)。

!!! note

    PyPI 不再支持使用用户名和密码发布，你需要生成一个令牌。使用令牌等价于设置 `--username __token__` 并将令牌作为密码使用。

如果你通过 `[[tool.uv.index]]` 使用自定义索引，请添加 `publish-url` 并使用 `uv publish --index <name>`。例如：

```toml
[[tool.uv.index]]
name = "testpypi"
url = "https://test.pypi.org/simple/"
publish-url = "https://test.pypi.org/legacy/"
explicit = true
```

!!! note

    使用 `uv publish --index <name>` 时，`pyproject.toml` 必须存在，即你在发布 CI 作业中需要有一个检出（checkout）步骤。

尽管 `uv publish` 会重试失败的上传，但发布仍可能在中间失败，导致部分文件已上传而部分文件仍然缺失。对于 PyPI，你可以直接重试完全相同的命令，已存在的相同文件将被忽略。对于其他注册中心，请使用 `--check-url <index url>` 并指定包所属的索引 URL（而非发布 URL）。当使用 `--index` 时，索引 URL 会被用作检查 URL。uv 将跳过上传与注册中心中完全相同的文件，并且还会处理竞态的并行上传。请注意，已存在的文件需要与之前上传到注册中心的文件完全匹配，这可以避免意外地为同一版本发布内容不同的源码分发和 wheel 文件。

### 随包上传证明（Attestations）

!!! note

    某些第三方包索引可能不支持证明（attestations），并可能拒绝包含证明的上传（而不是静默忽略它们）。如果你在上传时遇到问题，可以使用 `--no-attestations` 或 `UV_PUBLISH_NO_ATTESTATIONS` 来禁用 uv 的默认行为。

!!! tip

    `uv publish` 目前不生成证明；证明必须在发布之前单独创建。

`uv publish` 支持将[证明](https://peps.python.org/pep-0740/)上传到支持它们的注册中心，如 PyPI。

uv 将自动发现并匹配证明。例如，给定以下 `dist/` 目录，`uv publish` 会将证明与其对应的分发文件一起上传：

```console
$ ls dist/
hello_world-1.0.0-py3-none-any.whl
hello_world-1.0.0-py3-none-any.whl.publish.attestation
hello_world-1.0.0.tar.gz
hello_world-1.0.0.tar.gz.publish.attestation
```

## 安装你的包

使用 `uv run` 测试包是否可以安装和导入：

```console
$ uv run --with <PACKAGE> --no-project -- python -c "import <PACKAGE>"
```

`--no-project` 标志用于避免从本地项目目录安装包。

!!! tip

    如果你最近安装过该包，可能需要添加 `--refresh-package <PACKAGE>` 选项以避免使用缓存的包版本。

## 下一步

要了解更多关于发布包的信息，请查阅 [PyPA 指南](https://packaging.python.org/en/latest/guides/section-build-and-publish/)中关于构建和发布的内容。

或者，继续阅读关于将 uv 与其他软件集成的[指南](./integration/index.md)。
