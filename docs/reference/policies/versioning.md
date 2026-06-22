---
subtitle: Versioning
description: 了解 uv 项目的自定义版本控制方案，包括破坏性变更与次版本号的关系、Crate 版本控制策略、缓存版本控制以及锁文件（uv.lock）的 schema 版本管理规则。
---

# 版本控制（Versioning）

uv 在生产环境中被广泛使用，是一款稳定的软件。

uv 采用自定义的版本控制方案：次版本号（minor version）在发生破坏性变更时递增，补丁版本号（patch version）在错误修复、功能增强和其他非破坏性变更时递增。

我们对向后不兼容变更的谨慎程度与其预期的实际影响成正比，而非取决于任意版本号策略的硬性规定。我们重视快速迭代新功能的能力，并将*可能*具有破坏性的变更集中到明确标注的版本中发布。

uv 的更新日志可在 [GitHub 上查看](https://github.com/astral-sh/uv/blob/main/CHANGELOG.md)。

## Crate 版本控制

uv 的 crate 发布在 [crates.io](https://crates.io) 上。以下 crate 遵循正常的 uv 版本控制策略：

- `uv`
- `uv-build`
- `uv-version`

`uv` 和 `uv-build` crate 的版本号跟随二进制命令行接口的版本。这些 crate 的 Rust 接口**不**遵循语义化版本控制（Semantic Versioning）。

uv 的其余 crate **不提供任何稳定性保证**。其 Rust 接口被视为内部实现且不稳定。因此，这些 crate 的版本号格式为 `0.0.x`，补丁版本号在每次 uv 发布时递增，无论该 crate 是否有变更。

## 缓存版本控制

缓存版本被视为 uv 的内部实现细节，因此可能在次版本或补丁版本中发生变更。详见[缓存版本控制](../../concepts/cache.md#cache-versioning)。

## 锁文件版本控制

`uv.lock` 的 schema 版本被视为公共 API 的一部分，因此只会在次版本发布中作为破坏性变更递增。详见[锁文件版本控制](../../concepts/resolution.md#lockfile-versioning)。
