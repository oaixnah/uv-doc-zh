---
title: 构建项目发行版
subtitle: Building distributions
---

# 构建分发版

要将您的项目分发给其他人（例如，上传到像 PyPI 这样的索引），您需要将其构建为可分发的格式。

Python 项目通常以源码分发包（sdist）和二进制分发包（wheel）两种形式分发。前者通常是一个包含项目源代码和一些附加元数据的 `.tar.gz` 或 `.zip` 文件，而后者是一个包含可直接安装的预构建构件的 `.whl` 文件。

!!! important

    当使用 `uv build` 时，uv 充当[构建前端](https://peps.python.org/pep-0517/#terminology-and-goals)，仅确定要使用的 Python 版本并调用构建后端。构建的细节，例如包含的文件和分发包文件名，由构建后端确定，如 [`[build-system]`](./config.md#build-systems) 中所定义。有关构建配置的信息可以在相应工具的文档中找到。

## 使用 `uv build`

`uv build` 可用于为您的项目构建源码分发包和二进制分发包。默认情况下，`uv build` 将在当前目录中构建项目，并将构建的构件放置在 `dist/` 子目录中：

```console
$ uv build
$ ls dist/
example-0.1.0-py3-none-any.whl
example-0.1.0.tar.gz
```

您可以通过向 `uv build` 提供路径来在不同目录中构建项目，例如 `uv build path/to/project`。

`uv build` 将首先构建一个源码分发包，然后从该源码分发包构建一个二进制分发包（wheel）。

您可以使用 `uv build --sdist` 将 `uv build` 限制为仅构建源码分发包，使用 `uv build --wheel` 仅构建二进制分发包，或使用 `uv build --sdist --wheel` 从源码构建两种分发包。

## 构建约束

`uv build` 接受 `--build-constraint`，可用于在构建过程中约束任何构建依赖项的版本。当与 `--require-hashes` 结合使用时，uv 将强制用于构建项目的依赖项与特定的、已知的哈希值匹配，以实现可复现性。

例如，给定以下 `constraints.txt`：

```text
setuptools==68.2.2 --hash=sha256:b454a35605876da60632df1a60f736524eb73cc47bbc9f3f1ef1b644de74fd2a
```

运行以下命令将使用指定版本的 `setuptools` 构建项目，并验证下载的 `setuptools` 分发包是否与指定的哈希值匹配：

```console
$ uv build --build-constraint constraints.txt --require-hashes
```
