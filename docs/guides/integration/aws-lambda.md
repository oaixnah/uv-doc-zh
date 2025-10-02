---
title: 在 AWS Lambda 中使用 uv
description: 一份关于在 AWS Lambda 中使用 uv 管理 Python 依赖并通过 Docker 容器或 zip 压缩包部署无服务器函数的完整指南。
---

# 在 AWS Lambda 中使用 uv

[AWS Lambda](https://aws.amazon.com/lambda/) 是一种无服务器计算服务，可让您运行代码而无需预置或管理服务器。

您可以将 uv 与 AWS Lambda 结合使用来管理您的 Python 依赖项、构建您的部署包以及部署您的 Lambda 函数。

!!! tip

    请查看 [`uv-aws-lambda-example`](https://github.com/astral-sh/uv-aws-lambda-example) 项目，以获取在 AWS Lambda 中使用 uv 部署应用程序的最佳实践示例。

## 入门

首先，假设我们有一个最小化的 FastAPI 应用程序，其结构如下：

```plaintext
project
├── pyproject.toml
└── app
    ├── __init__.py
    └── main.py
```

其中 `pyproject.toml` 包含：

```toml title="pyproject.toml"
[project]
name = "uv-aws-lambda-example"
version = "0.1.0"
requires-python = ">=3.13"
dependencies = [
    # FastAPI is a modern web framework for building APIs with Python.
    "fastapi",
    # Mangum is a library that adapts ASGI applications to AWS Lambda and API Gateway.
    "mangum",
]

[dependency-groups]
dev = [
    # In development mode, include the FastAPI development server.
    "fastapi[standard]>=0.115",
]
```

`main.py` 文件包含：

```python title="app/main.py"
import logging

from fastapi import FastAPI
from mangum import Mangum

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = FastAPI()
handler = Mangum(app)


@app.get("/")
async def root() -> str:
    return "Hello, world!"
```

我们可以通过以下方式在本地运行此应用程序：

```console
$ uv run fastapi dev
```

然后，在 Web 浏览器中打开 http://127.0.0.1:8000/ 将显示“Hello, world!”

## 部署 Docker 镜像

要部署到 AWS Lambda，我们需要构建一个容器镜像，其中包含应用程序代码和依赖项，并放在一个输出目录中。

我们将遵循 [Docker 指南](./docker.md) 中概述的原则（特别是多阶段构建），以确保最终镜像尽可能小且缓存友好。

在第一阶段，我们将所有应用程序代码和依赖项填充到一个目录中。在第二阶段，我们会将这个目录复制到最终镜像中，并省略构建工具和其他不必要的文件。

```dockerfile title="Dockerfile"
FROM ghcr.io/astral-sh/uv:0.8.18 AS uv

# First, bundle the dependencies into the task root.
FROM public.ecr.aws/lambda/python:3.13 AS builder

# Enable bytecode compilation, to improve cold-start performance.
ENV UV_COMPILE_BYTECODE=1

# Disable installer metadata, to create a deterministic layer.
ENV UV_NO_INSTALLER_METADATA=1

# Enable copy mode to support bind mount caching.
ENV UV_LINK_MODE=copy

# Bundle the dependencies into the Lambda task root via `uv pip install --target`.
#
# Omit any local packages (`--no-emit-workspace`) and development dependencies (`--no-dev`).
# This ensures that the Docker layer cache is only invalidated when the `pyproject.toml` or `uv.lock`
# files change, but remains robust to changes in the application code.
RUN --mount=from=uv,source=/uv,target=/bin/uv \
    --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv export --frozen --no-emit-workspace --no-dev --no-editable -o requirements.txt && \
    uv pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

FROM public.ecr.aws/lambda/python:3.13

# Copy the runtime dependencies from the builder stage.
COPY --from=builder ${LAMBDA_TASK_ROOT} ${LAMBDA_TASK_ROOT}

# Copy the application code.
COPY ./app ${LAMBDA_TASK_ROOT}/app

# Set the AWS Lambda handler.
CMD ["app.main.handler"]
```

!!! tip

    要部署到基于 ARM 的 AWS Lambda 运行时，请将 `public.ecr.aws/lambda/python:3.13` 替换为 `public.ecr.aws/lambda/python:3.13-arm64`。

我们可以通过以下方式构建镜像，例如：

```console
$ uv lock
$ docker build -t fastapi-app .
```

此 Dockerfile 结构的核心优势如下：

1.  **最小的镜像大小。** 通过使用多阶段构建，我们可以确保最终镜像仅包含应用程序代码和依赖项。例如，uv 二进制文件本身不包含在最终镜像中。
2.  **最大化的缓存重用。** 通过将应用程序依赖项与应用程序代码分开安装，我们可以确保仅在依赖项更改时才使 Docker 层缓存失效。

具体来说，修改应用程序源代码后重建镜像可以重用缓存层，从而实现毫秒级构建：

```console
 => [internal] load build definition from Dockerfile                                                                 0.0s
 => => transferring dockerfile: 1.31kB                                                                               0.0s
 => [internal] load metadata for public.ecr.aws/lambda/python:3.13                                                   0.3s
 => [internal] load metadata for ghcr.io/astral-sh/uv:latest                                                         0.3s
 => [internal] load .dockerignore                                                                                    0.0s
 => => transferring context: 106B                                                                                    0.0s
 => [uv 1/1] FROM ghcr.io/astral-sh/uv:latest@sha256:ea61e006cfec0e8d81fae901ad703e09d2c6cf1aa58abcb6507d124b50286f  0.0s
 => [builder 1/2] FROM public.ecr.aws/lambda/python:3.13@sha256:f5b51b377b80bd303fe8055084e2763336ea8920d12955b23ef  0.0s
 => [internal] load build context                                                                                    0.0s
 => => transferring context: 185B                                                                                    0.0s
 => CACHED [builder 2/2] RUN --mount=from=uv,source=/uv,target=/bin/uv     --mount=type=cache,target=/root/.cache/u  0.0s
 => CACHED [stage-2 2/3] COPY --from=builder /var/task /var/task                                                     0.0s
 => CACHED [stage-2 3/3] COPY ./app /var/task                                                                        0.0s
 => exporting to image                                                                                               0.0s
 => => exporting layers                                                                                              0.0s
 => => writing image sha256:6f8f9ef715a7cda466b677a9df4046ebbb90c8e88595242ade3b4771f547652d                         0.0
```

构建后，我们可以将镜像推送到 [Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/)，例如：

```console
$ aws ecr get-login-password --region region | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com
$ docker tag fastapi-app:latest aws_account_id.dkr.ecr.region.amazonaws.com/fastapi-app:latest
$ docker push aws_account_id.dkr.ecr.region.amazonaws.com/fastapi-app:latest
```

最后，我们可以使用 AWS 管理控制台或 AWS CLI 将镜像部署到 AWS Lambda，例如：

```console
$ aws lambda create-function \
   --function-name myFunction \
   --package-type Image \
   --code ImageUri=aws_account_id.dkr.ecr.region.amazonaws.com/fastapi-app:latest \
   --role arn:aws:iam::111122223333:role/my-lambda-role
```

其中[执行角色](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html#permissions-executionrole-api)通过以下方式创建：

```console
$ aws iam create-role \
   --role-name my-lambda-role \
   --assume-role-policy-document '{"Version": "2012-10-17", "Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'
```

或者，使用以下命令更新现有函数：

```console
$ aws lambda update-function-code \
   --function-name myFunction \
   --image-uri aws_account_id.dkr.ecr.region.amazonaws.com/fastapi-app:latest \
   --publish
```

要测试 Lambda，我们可以通过 AWS 管理控制台或 AWS CLI 调用它，例如：

```console
$ aws lambda invoke \
   --function-name myFunction \
   --payload file://event.json \
   --cli-binary-format raw-in-base64-out \
   response.json
{
  "StatusCode": 200,
  "ExecutedVersion": "$LATEST"
}
```

其中 `event.json` 包含要传递给 Lambda 函数的事件负载：

```json title="event.json"
{
  "httpMethod": "GET",
  "path": "/",
  "requestContext": {},
  "version": "1.0"
}
```

`response.json` 包含 Lambda 函数的响应：

```json title="response.json"
{
  "statusCode": 200,
  "headers": {
    "content-length": "14",
    "content-type": "application/json"
  },
  "multiValueHeaders": {},
  "body": "\"Hello, world!\"",
  "isBase64Encoded": false
}
```

有关详细信息，请参阅 [AWS Lambda 文档](https://docs.aws.amazon.com/lambda/latest/dg/python-image.html)。

### 工作区支持

如果项目包含本地依赖项（例如，通过[工作区](../../concepts/projects/workspaces.md)），那么这些依赖项也必须包含在部署包中。

我们将通过扩展上述示例来开始，以包含对名为 `library` 的本地开发库的依赖。

首先，我们创建库本身：

```console
$ uv init --lib library
$ uv add ./library
```

在 `project` 目录中运行 `uv init` 将自动将 `project` 转换为工作区，并将 `library` 添加为工作区成员：

```toml title="pyproject.toml"
[project]
name = "uv-aws-lambda-example"
version = "0.1.0"
requires-python = ">=3.13"
dependencies = [
    # FastAPI is a modern web framework for building APIs with Python.
    "fastapi",
    # A local library.
    "library",
    # Mangum is a library that adapts ASGI applications to AWS Lambda and API Gateway.
    "mangum",
]

[dependency-groups]
dev = [
    # In development mode, include the FastAPI development server.
    "fastapi[standard]",
]

[tool.uv.workspace]
members = ["library"]

[tool.uv.sources]
lib = { workspace = true }
```

默认情况下，`uv init --lib` 将创建一个导出 `hello` 函数的包。我们将修改应用程序源代码以调用该函数：

```python title="app/main.py"
import logging

from fastapi import FastAPI
from mangum import Mangum

from library import hello

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = FastAPI()
handler = Mangum(app)


@app.get("/")
async def root() -> str:
    return hello()
```

我们可以通过以下方式在本地运行修改后的应用程序：

```console
$ uv run fastapi dev
```

并确认在 Web 浏览器中打开 http://127.0.0.1:8000/ 会显示“Hello from library!”（而不是“Hello, World!”）。

最后，我们将更新 Dockerfile 以在部署包中包含本地库：

```dockerfile title="Dockerfile"
FROM ghcr.io/astral-sh/uv:0.8.18 AS uv

# First, bundle the dependencies into the task root.
FROM public.ecr.aws/lambda/python:3.13 AS builder

# Enable bytecode compilation, to improve cold-start performance.
ENV UV_COMPILE_BYTECODE=1

# Disable installer metadata, to create a deterministic layer.
ENV UV_NO_INSTALLER_METADATA=1

# Enable copy mode to support bind mount caching.
ENV UV_LINK_MODE=copy

# Bundle the dependencies into the Lambda task root via `uv pip install --target`.
#
# Omit any local packages (`--no-emit-workspace`) and development dependencies (`--no-dev`).
# This ensures that the Docker layer cache is only invalidated when the `pyproject.toml` or `uv.lock`
# files change, but remains robust to changes in the application code.
RUN --mount=from=uv,source=/uv,target=/bin/uv \
    --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv export --frozen --no-emit-workspace --no-dev --no-editable -o requirements.txt && \
    uv pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# If you have a workspace, copy it over and install it too.
#
# By omitting `--no-emit-workspace`, `library` will be copied into the task root. Using a separate
# `RUN` command ensures that all third-party dependencies are cached separately and remain
# robust to changes in the workspace.
RUN --mount=from=uv,source=/uv,target=/bin/uv \
    --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=library,target=library \
    uv export --frozen --no-dev --no-editable -o requirements.txt && \
    uv pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

FROM public.ecr.aws/lambda/python:3.13

# Copy the runtime dependencies from the builder stage.
COPY --from=builder ${LAMBDA_TASK_ROOT} ${LAMBDA_TASK_ROOT}

# Copy the application code.
COPY ./app ${LAMBDA_TASK_ROOT}/app

# Set the AWS Lambda handler.
CMD ["app.main.handler"]
```

!!! tip

    要部署到基于 ARM 的 AWS Lambda 运行时，请将 `public.ecr.aws/lambda/python:3.13` 替换为 `public.ecr.aws/lambda/python:3.13-arm64`。

从那里，我们可以像以前一样构建和部署更新后的镜像。

## 部署 zip 压缩包

AWS Lambda 还支持通过 zip 压缩包进行部署。对于简单的应用程序，zip 压缩包可能比 Docker 镜像更直接、更高效；但是，zip 压缩包的大小限制为 [250 MB](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html#python-package-create-update)。

回到 FastAPI 示例，我们可以通过以下方式将应用程序依赖项打包到本地目录中以用于 AWS Lambda：

```console
$ uv export --frozen --no-dev --no-editable -o requirements.txt
$ uv pip install \
   --no-installer-metadata \
   --no-compile-bytecode \
   --python-platform x86_64-manylinux2014 \
   --python 3.13 \
   --target packages \
   -r requirements.txt
```

!!! tip

    要部署到基于 ARM 的 AWS Lambda 运行时，请将 `x86_64-manylinux2014` 替换为 `aarch64-manylinux2014`。

遵循 [AWS Lambda 文档](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html)，我们可以按如下方式将这些依赖项打包成 zip：

```console
$ cd packages
$ zip -r ../package.zip .
$ cd ..
```

最后，我们可以将应用程序代码添加到 zip 压缩包中：

```console
$ zip -r package.zip app
```

然后，我们可以通过 AWS 管理控制台或 AWS CLI 将 zip 压缩包部署到 AWS Lambda，例如：

```console
$ aws lambda create-function \
   --function-name myFunction \
   --runtime python3.13 \
   --zip-file fileb://package.zip \
   --handler app.main.handler \
   --role arn:aws:iam::111122223333:role/service-role/my-lambda-role
```

其中[执行角色](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html#permissions-executionrole-api)通过以下方式创建：

```console
$ aws iam create-role \
   --role-name my-lambda-role \
   --assume-role-policy-document '{"Version": "2012-10-17", "Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'
```

或者，使用以下命令更新现有函数：

```console
$ aws lambda update-function-code \
   --function-name myFunction \
   --zip-file fileb://package.zip
```

!!! note

    默认情况下，AWS 管理控制台假定 Lambda 入口点为 `lambda_function.lambda_handler`。如果您的应用程序使用不同的入口点，则需要在 AWS 管理控制台中对其进行修改。例如，上面的 FastAPI 应用程序使用 `app.main.handler`。

要测试 Lambda，我们可以通过 AWS 管理控制台或 AWS CLI 调用它，例如：

```console
$ aws lambda invoke \
   --function-name myFunction \
   --payload file://event.json \
   --cli-binary-format raw-in-base64-out \
   response.json
{
  "StatusCode": 200,
  "ExecutedVersion": "$LATEST"
}
```

其中 `event.json` 包含要传递给 Lambda 函数的事件负载：

```json title="event.json"
{
  "httpMethod": "GET",
  "path": "/",
  "requestContext": {},
  "version": "1.0"
}
```

`response.json` 包含 Lambda 函数的响应：

```json title="response.json"
{
  "statusCode": 200,
  "headers": {
    "content-length": "14",
    "content-type": "application/json"
  },
  "multiValueHeaders": {},
  "body": "\"Hello, world!\"",
  "isBase64Encoded": false
}
```

### 使用 Lambda 层

在使用 zip 压缩包时，AWS Lambda 还支持部署多个组合的 [Lambda 层](https://docs.aws.amazon.com/lambda/latest/dg/python-layers.html)。这些层在概念上类似于 Docker 镜像中的层，允许您将应用程序代码与依赖项分开。

特别是，我们可以为应用程序依赖项创建一个 lambda 层，并将其附加到 Lambda 函数，与应用程序代码本身分开。这种设置可以提高应用程序更新的冷启动性能，因为依赖项层可以在部署之间重用。

要创建 Lambda 层，我们将遵循类似的步骤，但创建两个单独的 zip 压缩包：一个用于应用程序代码，一个用于应用程序依赖项。

首先，我们将创建依赖项层。Lambda 层需要遵循稍微不同的结构，因此我们将使用 `--prefix` 而不是 `--target`：

```console
$ uv export --frozen --no-dev --no-editable -o requirements.txt
$ uv pip install \
   --no-installer-metadata \
   --no-compile-bytecode \
   --python-platform x86_64-manylinux2014 \
   --python 3.13 \
   --prefix packages \
   -r requirements.txt
```

然后，我们将按照 Lambda 层预期的布局对依赖项进行压缩：

```console
$ mkdir python
$ cp -r packages/lib python/
$ zip -r layer_content.zip python
```

!!! tip

    要生成确定性的 zip 压缩包，请考虑向 `zip` 传递 `-X` 标志以排除扩展属性和文件系统元数据。

并发布 Lambda 层：

```console
$ aws lambda publish-layer-version --layer-name dependencies-layer \
   --zip-file fileb://layer_content.zip \
   --compatible-runtimes python3.13 \
   --compatible-architectures "x86_64"
```

然后，我们可以像上一个示例一样创建 Lambda 函数，但省略依赖项：

```console
$ # Zip the application code.
$ zip -r app.zip app

$ # Create the Lambda function.
$ aws lambda create-function \
   --function-name myFunction \
   --runtime python3.13 \
   --zip-file fileb://app.zip \
   --handler app.main.handler \
   --role arn:aws:iam::111122223333:role/service-role/my-lambda-role
```

最后，我们可以使用 `publish-layer-version` 步骤返回的 ARN 将依赖项层附加到 Lambda 函数：

```console
$ aws lambda update-function-configuration --function-name myFunction \
    --cli-binary-format raw-in-base64-out \
    --layers "arn:aws:lambda:region:111122223333:layer:dependencies-layer:1"
```

当应用程序依赖项发生更改时，可以通过重新发布层并更新 Lambda 函数配置来独立于应用程序更新层：

```console
$ # Update the dependencies in the layer.
$ aws lambda publish-layer-version --layer-name dependencies-layer \
   --zip-file fileb://layer_content.zip \
   --compatible-runtimes python3.13 \
   --compatible-architectures "x86_64"

$ # Update the Lambda function configuration.
$ aws lambda update-function-configuration --function-name myFunction \
    --cli-binary-format raw-in-base64-out \
    --layers "arn:aws:lambda:region:111122223333:layer:dependencies-layer:2"
```
