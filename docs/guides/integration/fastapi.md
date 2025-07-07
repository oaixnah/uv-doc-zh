---
title: 在 FastAPI 中使用 uv
description:
  一份关于在 FastAPI 中使用 uv 管理 Python 依赖、运行应用和使用 Docker 部署的指南。
---

# 在 FastAPI 中使用 uv

[FastAPI](https://github.com/fastapi/fastapi) 是一个现代、高性能的 Python Web 框架。
你可以使用 uv 来管理你的 FastAPI 项目，包括安装依赖、管理环境、运行 FastAPI 应用等等。

!!! note

    你可以在 [uv-fastapi-example](https://github.com/astral-sh/uv-fastapi-example) 仓库中查看本指南的源代码。

## 迁移现有的 FastAPI 项目

举个例子，考虑在 [FastAPI 文档](https://fastapi.tiangolo.com/tutorial/bigger-applications/)中定义的示例应用，其结构如下：

```plaintext
project
└── app
    ├── __init__.py
    ├── main.py
    ├── dependencies.py
    ├── routers
    │   ├── __init__.py
    │   ├── items.py
    │   └── users.py
    └── internal
        ├── __init__.py
        └── admin.py
```

要在这个应用中使用 uv，请在 `project` 目录中运行：

```console
$ uv init --app
```

这将创建一个[具有应用布局的项目](../../concepts/projects/init.md#applications)和一个 `pyproject.toml` 文件。

然后，添加对 FastAPI 的依赖：

```console
$ uv add fastapi --extra standard
```

你现在应该有以下结构：

```plaintext
project
├── pyproject.toml
└── app
    ├── __init__.py
    ├── main.py
    ├── dependencies.py
    ├── routers
    │   ├── __init__.py
    │   ├── items.py
    │   └── users.py
    └── internal
        ├── __init__.py
        └── admin.py
```

`pyproject.toml` 文件的内容应该如下所示：

```toml title="pyproject.toml"
[project]
name = "uv-fastapi-example"
version = "0.1.0"
description = "FastAPI project"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "fastapi[standard]",
]
```

然后，你可以使用以下命令运行 FastAPI 应用：

```console
$ uv run fastapi dev
```

`uv run` 会自动解析和锁定项目依赖（即，在 `pyproject.toml` 旁边创建一个 `uv.lock`），创建一个虚拟环境，并在该环境中运行命令。

通过在 Web 浏览器中打开 http://127.0.0.1:8000/?token=jessica 来测试应用。

## 部署

要使用 Docker 部署 FastAPI 应用，你可以使用以下 `Dockerfile`：

```dockerfile title="Dockerfile"
FROM python:3.12-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY . /app

# Install the application dependencies.
WORKDIR /app
RUN uv sync --frozen --no-cache

# Run the application.
CMD ["/app/.venv/bin/fastapi", "run", "app/main.py", "--port", "80", "--host", "0.0.0.0"]
```

使用以下命令构建 Docker 镜像：

```console
$ docker build -t fastapi-app .
```

在本地运行 Docker 容器：

```console
$ docker run -p 8000:80 fastapi-app
```

在浏览器中访问 http://127.0.0.1:8000/?token=jessica 以验证应用是否正常运行。

!!! tip

    有关在 Docker 中使用 uv 的更多信息，请参阅 [Docker 指南](./docker.md)。
