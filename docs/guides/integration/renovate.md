---
title: 在 Renovate 中使用 uv
description: 在 Renovate 依赖机器人中使用 uv 的指南。
---

# Renovate

定期更新依赖被广泛认为是最佳实践，这样可以避免暴露于安全漏洞、减少依赖之间的不兼容性，以及避免从过旧版本进行复杂的升级。

uv 已获得 [Renovate](https://github.com/renovatebot/renovate) 的支持。

## `uv.lock` 输出

Renovate 通过检测 `uv.lock` 文件的存在来判断项目是否使用 uv 管理依赖，并会为[项目依赖（project dependencies）](../../concepts/projects/dependencies.md#project-dependencies)、[可选依赖（optional dependencies）](../../concepts/projects/dependencies.md#optional-dependencies)和[开发依赖（development dependencies）](../../concepts/projects/dependencies.md#development-dependencies)建议升级。Renovate 会同时更新 `pyproject.toml` 和 `uv.lock` 文件。

还可以通过启用 [`lockFileMaintenance`](https://docs.renovatebot.com/configuration-options/#lockfilemaintenance) 选项来定期刷新锁文件（例如更新传递依赖）：

```jsx title="renovate.json5"
{
  $schema: "https://docs.renovatebot.com/renovate-schema.json",
  lockFileMaintenance: {
    enabled: true,
  },
}
```

## 内联脚本元数据

Renovate 支持更新通过[内联脚本元数据（inline script metadata）](../scripts.md/#declaring-script-dependencies)定义的依赖。

由于 Renovate 无法自动检测哪些 Python 文件使用了内联脚本元数据，因此需要通过 [`managerFilePatterns`](https://docs.renovatebot.com/configuration-options/#managerfilepatterns) 显式指定这些文件的位置，示例如下：

```jsx title="renovate.json5"
{
  $schema: "https://docs.renovatebot.com/renovate-schema.json",
  pep723: {
    managerFilePatterns: [
      "docs/build.py",
      "scripts/**/*.py",
    ],
  },
}
```

!!! note

    Renovate 尚不支持更新与脚本关联的锁文件（https://github.com/renovatebot/renovate/issues/33591），因此如果你在脚本中依赖此功能，则需要手动更新锁文件。

## 依赖冷却期

如果你使用了 [`exclude-newer`](../../reference/settings.md#exclude-newer) 选项，建议同时在 Renovate 中设置等效的 [`minimumReleaseAge`](https://docs.renovatebot.com/configuration-options/#minimumreleaseage) 选项，以避免出现 uv 无法锁定依赖的拉取请求。

例如，如果你已将 `exclude-newer` 设置为 `1 week`，可以进行如下配置：

```jsx title="renovate.json5"
{
  $schema: "https://docs.renovatebot.com/renovate-schema.json",

  // 仅为 PyPI 启用。
  packageRules: [
    {
      matchDatasources: ["pypi"],
      minimumReleaseAge: "1 week",
    },
  ],

  // 或为所有生态系统启用。
  minimumReleaseAge: "1 week",
}
```
