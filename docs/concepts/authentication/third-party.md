---
subtitle: Third-party services
description: uv 第三方服务认证指南，涵盖 Azure Artifacts、Google Artifact Registry、AWS CodeArtifact、JFrog Artifactory 等替代包索引的认证方式，以及 Hugging Face Hub 的自动认证支持，包括 HF_TOKEN 环境变量的配置与使用。
---

# 第三方服务

## 替代包索引的认证

请参阅针对主流替代 Python 包索引的认证专用指南：

- [Azure Artifacts](../../guides/integration/azure.md)
- [Google Artifact Registry](../../guides/integration/google.md)
- [AWS CodeArtifact](../../guides/integration/aws.md)
- [JFrog Artifactory](../../guides/integration/jfrog.md)

## Hugging Face 支持

uv 支持对 Hugging Face Hub 的自动认证。具体来说，如果设置了 `HF_TOKEN`
环境变量，uv 会将其传播到对 `huggingface.co` 的请求中。

这在访问 Hugging Face Datasets 中的私有脚本时特别有用。例如，你可以
运行以下命令来执行私有数据集中的 `main.py` 脚本：

```console
$ HF_TOKEN=hf_... uv run https://huggingface.co/datasets/<user>/<name>/resolve/<branch>/main.py
```

你可以通过设置 `UV_NO_HF_TOKEN=1` 环境变量来禁用自动 Hugging Face 认证。
