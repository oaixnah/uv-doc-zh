---
title: 构建和发布包
subtitle: Publishing packages
description: 一份使用 uv 构建 Python 包并将其发布到包索引（如 PyPI）的指南。
---

# 构建和发布包

uv 支持通过 `uv build` 将 Python 包构建为源码和二进制发行版，并使用 `uv publish` 将它们上传到注册表。

## 准备你的项目以进行打包

在尝试发布你的项目之前，你需要确保它已经准备好进行分发打包。

如果你的项目在 `pyproject.toml` 中不包含 `[build-system]` 定义，uv 默认不会构建它。这意味着你的项目可能还没有准备好进行分发。在[项目概念](../concepts/projects/config.md#build-systems)文档中阅读有关声明构建系统的影响的更多信息。

!!! note

    如果你有不想发布的内部包，可以将其标记为私有：

    ```toml
    [project]
    classifiers = ["Private :: Do Not Upload"]
    ```

    此设置会使 PyPI 拒绝你上传的包的发布。它不影响备用注册表上的安全或隐私设置。

    我们还建议仅生成[每个项目的 PyPI API 令牌](https://pypi.org/help/#apitoken)：没有与项目匹配的 PyPI 令牌，它就不会被意外发布。

## 构建你的包

使用 `uv build` 构建你的包：

```console
$ uv build
```

默认情况下，`uv build` 会在当前目录中构建项目，并将构建的产物放置在 `dist/` 子目录中。

或者，`uv build <SRC>` 将在指定目录中构建包，而 `uv build --package <PACKAGE>` 将在当前工作区中构建指定的包。

!!! info

    默认情况下，`uv build` 在从 `pyproject.toml` 的 `build-system.requires` 部分解析构建依赖项时会遵循 `tool.uv.sources`。发布包时，我们建议运行 `uv build --no-sources` 以确保在禁用 `tool.uv.sources` 的情况下包能正确构建，就像使用其他构建工具（如 [`pypa/build`](https://github.com/pypa/build)）时一样。

## 发布你的包

使用 `uv publish` 发布你的包：

```console
$ uv publish
```

使用 `--token` 或 `UV_PUBLISH_TOKEN` 设置 PyPI 令牌，或使用 `--username` 或 `UV_PUBLISH_USERNAME` 设置用户名，并使用 `--password` 或 `UV_PUBLISH_PASSWORD` 设置密码。要从 GitHub Actions 发布到 PyPI，你无需设置任何凭据。相反，[向 PyPI 项目添加受信任的发布者](https://docs.pypi.org/trusted-publishers/adding-a-publisher/)。

!!! note

    PyPI 不再支持使用用户名和密码进行发布，你需要生成一个令牌。使用令牌等同于设置 `--username __token__` 并使用令牌作为密码。

如果你通过 `[[tool.uv.index]]` 使用自定义索引，请添加 `publish-url` 并使用 `uv publish --index <name>`。例如：

```toml
[[tool.uv.index]]
name = "testpypi"
url = "https://test.pypi.org/simple/"
publish-url = "https://test.pypi.org/legacy/"
explicit = true
```

!!! note

    当使用 `uv publish --index <name>` 时，`pyproject.toml` 必须存在，即你需要在发布 CI 作业中有一个检出步骤。

尽管 `uv publish` 会重试失败的上传，但有时发布可能会在中间失败，一些文件已上传，而另一些文件仍然缺失。对于 PyPI，你可以重试完全相同的命令，已存在的相同文件将被忽略。对于其他注册表，请使用 `--check-url <index url>`，其中包含包所属的索引 URL（而不是发布 URL）。当使用 `--index` 时，索引 URL 将用作检查 URL。uv 将跳过上传与注册表中文件相同的文件，并且它还将处理竞态并行上传。请注意，现有文件需要与先前上传到注册表的文件完全匹配，这可以避免意外发布具有相同版本的不同内容的源码发行版和 wheel。

## 安装你的包

使用 `uv run` 测试包是否可以安装和导入：

```console
$ uv run --with <PACKAGE> --no-project -- python -c "import <PACKAGE>"
```

`--no-project` 标志用于避免从本地项目目录安装包。

!!! tip

    如果你最近安装了该包，你可能需要包含 `--refresh-package <PACKAGE>` 选项以避免使用缓存版本的包。

## 后续步骤

要了解有关发布包的更多信息，请查看有关构建和发布的 [PyPA 指南](https://packaging.python.org/en/latest/guides/section-build-and-publish/)。

或者，继续阅读有关将 uv 与其他软件集成的[指南](./integration/index.md)。
