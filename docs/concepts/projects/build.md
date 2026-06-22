---
title: 构建发行版
subtitle: Building distributions
description: 学习如何使用uv build命令构建Python项目的源码分发包(sdist)和二进制分发包(wheel)，包括构建约束配置和可复现性设置，完整指南帮助您将项目发布到PyPI等索引。
---

# 构建发行版

要将项目分发给他人（例如上传到 PyPI 等索引），你需要将其构建为可分发的格式。

Python 项目通常以源码分发包（source distribution，sdist）和二进制分发包（wheel）两种形式分发。前者通常是 `.tar.gz` 或 `.zip` 文件，包含项目源码及一些附加元数据；后者则是 `.whl` 文件，包含可直接安装的预构建产物。

!!! important

    使用 `uv build` 时，uv 充当[构建前端](https://peps.python.org/pep-0517/#terminology-and-goals)（build frontend），仅负责确定要使用的 Python 版本并调用构建后端（build backend）。构建的细节，例如包含哪些文件以及发行版文件名，由构建后端决定，具体定义见 [`[build-system]`](./config.md#build-systems)。有关构建配置的信息，请参阅相应工具的文档。

## 使用 `uv build`

`uv build` 可用于为项目构建源码分发包和二进制分发包。默认情况下，`uv build` 会在当前目录下构建项目，并将生成的构建产物放置到 `dist/` 子目录中：

```console
$ uv build
$ ls dist/
example-0.1.0-py3-none-any.whl
example-0.1.0.tar.gz
```

你可以通过向 `uv build` 提供路径来在不同目录中构建项目，例如 `uv build path/to/project`。

`uv build` 会先构建源码分发包，然后从该源码分发包构建二进制分发包（wheel）。

你可以通过 `uv build --sdist` 限制只构建源码分发包，通过 `uv build --wheel` 只构建二进制分发包，或通过 `uv build --sdist --wheel` 从源码构建两种分发包。

## 构建约束

`uv build` 接受 `--build-constraint` 参数，可用于在构建过程中约束任何构建需求的版本。与 `--require-hashes` 配合使用时，uv 将强制要求用于构建项目的依赖项与特定的已知哈希值匹配，以保证可复现性。

例如，给定以下 `constraints.txt`：

```text
setuptools==68.2.2 --hash=sha256:b454a35605876da60632df1a60f736524eb73cc47bbc9f3f1ef1b644de74fd2a
```

运行以下命令将使用指定版本的 `setuptools` 构建项目，并验证下载的 `setuptools` 发行版是否与指定的哈希值匹配：

```console
$ uv build --build-constraint constraints.txt --require-hashes
```

## 防止发布到 PyPI

如果你有不想发布的内部分发包，可以将其标记为私有：

```toml
[project]
classifiers = ["Private :: Do Not Upload"]
```

此设置会使 PyPI 拒绝你上传的包发布。它不会影响其他注册源（alternative registries）的安全或隐私设置。

我们还建议仅生成[针对项目的 PyPI API 令牌](https://pypi.org/help/#apitoken)：如果没有与项目匹配的 PyPI 令牌，就不会意外发布。
