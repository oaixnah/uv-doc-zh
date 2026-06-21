---
title: 在 Dependabot 中使用 uv
description: 使用 uv 与 Dependabot 依赖机器人的指南。
---

# Dependabot

定期更新依赖是公认的最佳实践，这样可以避免暴露于漏洞之中、减少依赖之间的不兼容性，并避免从过旧版本升级时带来的复杂升级过程。

Dependabot 已宣布支持 uv，但某些使用场景尚未完全就绪。有关最新进展，请参阅 [astral-sh/uv#2512](https://github.com/astral-sh/uv/issues/2512)。

Dependabot 支持更新 `uv.lock` 文件。要启用此功能，请将 uv 的 `package-ecosystem` 添加到 `dependabot.yml` 中的 `updates` 列表：

```yaml title="dependabot.yml"
version: 2

updates:
  - package-ecosystem: "uv"
    directory: "/"
    schedule:
      interval: "weekly"
```

## 依赖冷却期

如果你使用了 [`exclude-newer`](../../reference/settings.md#exclude-newer) 选项，建议同时在 Dependabot 中设置等效的 [`cooldown`](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference#cooldown-) 选项，以避免出现 uv 无法锁定依赖的拉取请求（Pull Request）。

例如，如果你将 `exclude-newer` 设置为 `1 week`，可以按如下方式配置：

```yaml title="dependabot.yml"
version: 2

updates:
  - package-ecosystem: "uv"
    directory: "/"
    schedule:
      interval: "weekly"
    cooldown:
      default-days: 7
```
