---
title: 在 Bazel 中使用 uv
description: 使用 uv 为 Bazel 提供包解析能力
---

# 在 Bazel 中使用 uv

关于 uv 与 Bazel 的更广泛工作流，请参阅
[`rules_py` uv 指南](https://github.com/aspect-build/rules_py#dependency-resolution-with-uv) 或
[`rules_python` uv 指南](https://rules-python.readthedocs.io/en/latest/pypi/lock.html#uv-pip-compile-bzlmod-only)。

## 认证

Bazel 7 及更高版本通过 `--credential_helper` 选项支持凭证助手（credential helpers）。要在 Bazel 拉取操作中使用 uv 存储的凭证，首先需要对托管 Bazel 所需拉取文件的服务进行 uv 认证：

```console
uv auth login https://packages.example.com
```

然后，配置 Bazel 以调用
[`uv auth helper`](../../concepts/authentication/cli.md#using-credentials-with-external-tools) 来处理匹配的主机：

```text title=".bazelrc"
common --credential_helper=packages.example.com=%workspace%/bazel/uv-auth-helper
common --credential_helper=files.example.com=%workspace%/bazel/uv-auth-helper
```

将主机模式替换为实际提供 Bazel 将要拉取的索引和文件的主机。

最后，添加 `.bazelrc` 引用的包装脚本：

```bash title="bazel/uv-auth-helper"
#!/usr/bin/env bash
exec uv --preview-features auth-helper auth helper --protocol=bazel "$@"
```

该脚本必须具有可执行权限：

```console
chmod +x bazel/uv-auth-helper
```
