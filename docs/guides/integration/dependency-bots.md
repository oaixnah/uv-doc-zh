---
title: 将 uv 与依赖机器人配合使用
description: 一份关于将 uv 与 Renovate 和 Dependabot 等依赖机器人配合使用的指南。
---

# 依赖机器人

定期更新依赖项被认为是最佳实践，以避免暴露于漏洞、限制依赖项之间的不兼容性，并避免从过旧版本升级时进行复杂的升级。各种工具可以通过创建自动化的拉取请求来帮助保持最新状态。其中一些支持 uv，或者正在进行支持工作。

## Renovate

uv 由 [Renovate](https://github.com/renovatebot/renovate) 支持。

### `uv.lock` 输出

Renovate 使用 `uv.lock` 文件的存在来确定 uv 用于管理依赖项，并将建议对[项目依赖项](../../concepts/projects/dependencies.md#_8)、[可选依赖项](../../concepts/projects/dependencies.md#_16)和[开发依赖项](../../concepts/projects/dependencies.md#_17)进行升级。Renovate 将同时更新 `pyproject.toml` 和 `uv.lock` 文件。

锁文件也可以定期刷新（例如更新传递性依赖项），方法是启用 [`lockFileMaintenance`](https://docs.renovatebot.com/configuration-options/#lockfilemaintenance) 选项：

```jsx title="renovate.json5"
{
  $schema: "https://docs.renovatebot.com/renovate-schema.json",
  lockFileMaintenance: {
    enabled: true,
  },
}
```

### 内联脚本元数据

Renovate 支持更新使用[脚本内联元数据](../scripts.md/#_2)定义的依赖项。

由于它无法自动检测哪些 Python 文件使用脚本内联元数据，因此需要使用 [`fileMatch`](https://docs.renovatebot.com/configuration-options/#filematch) 明确定义它们的位置，如下所示：

```jsx title="renovate.json5"
{
  $schema: "https://docs.renovatebot.com/renovate-schema.json",
  pep723: {
    fileMatch: [
      "scripts/generate_docs\\.py",
      "scripts/run_server\\.py",
    ],
  },
}
```

## Dependabot

Dependabot 已宣布支持 uv，但仍有一些用例尚无法正常工作。有关更新，请参阅 [astral-sh/uv#2512](https://github.com/astral-sh/uv/issues/2512)。

Dependabot 支持更新 `uv.lock` 文件。要启用它，请将 uv `package-ecosystem` 添加到 `dependabot.yml` 中的 `updates` 列表中：

```yaml title="dependabot.yml"
version: 2

updates:
  - package-ecosystem: "uv"
    directory: "/"
    schedule:
      interval: "weekly"
```
