---
title: 导出锁文件
subtitle: Exporting Lockfile
description: 了解如何使用 uv export 将锁文件导出为 requirements.txt、pylock.toml 和 CycloneDX SBOM 等不同格式，以便与其他工具和工作流集成。
---

# 导出锁文件 {#exporting-a-lockfile}

uv 可以将锁文件（lockfile）导出为不同格式，以便与其他工具和工作流集成。`uv export` 命令支持多种输出格式，每种格式适用于不同的用例。

有关锁文件及其创建方式的更多详细信息，请参阅[项目结构](./layout.md)和[锁定与同步](./sync.md)文档。

## 导出格式概览 {#overview-of-export-formats}

uv 支持三种导出格式：

- `requirements.txt`：传统的兼容 pip 的
  [requirements 文件格式](https://pip.pypa.io/en/stable/reference/requirements-file-format/)。
- `pylock.toml`：[PEP 751](https://peps.python.org/pep-0751/) 中定义的标准化 Python 锁文件格式。
- `CycloneDX`：行业标准的[软件物料清单（SBOM）](https://cyclonedx.org/)格式。

可以通过 `--format` 标志指定格式：

```console
$ uv export --format requirements.txt
$ uv export --format pylock.toml
$ uv export --format cyclonedx1.5
```

!!! tip

    默认情况下，`uv export` 会将结果输出到标准输出（stdout）。使用 `--output-file` 可以将任何格式写入文件：

    ```console
    $ uv export --format requirements.txt --output-file requirements.txt
    $ uv export --format pylock.toml --output-file pylock.toml
    $ uv export --format cyclonedx1.5 --output-file sbom.json
    ```

## `requirements.txt` 格式 {#requirementstxt-format}

`requirements.txt` 格式是 Python 依赖项支持最广泛的格式。它可以与 `pip` 及其他 Python 包管理器配合使用。

### 基本用法 {#basic-usage}

```console
$ uv export --format requirements.txt
```

生成的 `requirements.txt` 文件可以通过 `uv pip install` 安装，也可以使用 `pip` 等其他工具安装。

!!! note

    一般来说，我们不建议同时使用 `uv.lock` 和 `requirements.txt` 文件。`uv.lock` 格式更强大，包含一些无法在 `requirements.txt` 中表达的功能。如果您发现自己需要导出 `uv.lock` 文件，请考虑提交一个 issue 来讨论您的用例。

## `pylock.toml` 格式 {#pylocktoml-format}

[PEP 751](https://peps.python.org/pep-0751/) 定义了一种基于 TOML 的 Python 依赖项锁文件格式。uv 可以将项目的依赖锁文件导出为此格式。

### 基本用法 {#basic-usage_1}

```console
$ uv export --format pylock.toml
```

## CycloneDX SBOM 格式 {#cyclonedx-sbom-format}

uv 可以将项目的依赖锁文件导出为 CycloneDX 格式的软件物料清单（SBOM）。SBOM 提供了应用程序中所有软件组件的全面清单，对于安全审计、合规性和供应链透明度非常有用。

!!! important

    导出为 CycloneDX 格式的支持处于[预览阶段](../preview.md)，在未来的任何版本中都可能发生变化。

### 什么是 CycloneDX？ {#what-is-cyclonedx}

[CycloneDX](https://cyclonedx.org/) 是一种用于创建软件物料清单的行业标准格式。CycloneDX 是机器可读的，并被安全扫描工具、漏洞数据库和软件成分分析（SCA）平台广泛支持。

### 基本用法 {#basic-usage_2}

要将项目的锁文件导出为 CycloneDX SBOM：

```console
$ uv export --format cyclonedx1.5
```

这将生成一个 JSON 编码的 CycloneDX v1.5 文档，其中包含您的项目及其所有依赖项。

### SBOM 结构 {#sbom-structure}

生成的 SBOM 遵循 [CycloneDX 规范](https://cyclonedx.org/specification/overview/)。uv 还会在组件上包含以下自定义属性：

- `uv:package:marker`：环境标记（例如 `python_version >= "3.8"`）
- `uv:workspace:path`：工作空间成员的相对路径

## 下一步 {#next-steps}

要了解更多关于锁文件和导出的信息，请参阅[锁定与同步](./sync.md)文档和[命令参考](../../reference/cli/export.md)。

或者，继续阅读了解如何[构建项目并将其发布到包索引](../../guides/package.md)。
