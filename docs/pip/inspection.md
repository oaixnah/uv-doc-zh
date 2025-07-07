---
subtitle: Inspecting environments
---

# 检查环境

## 列出已安装的包

要列出环境中的所有包：

```console
$ uv pip list
```

以 JSON 格式列出包：

```console
$ uv pip list --format json
```

以 `requirements.txt` 格式列出环境中的所有包：

```console
$ uv pip freeze
```

## 检查一个包

要显示有关已安装包的信息，例如 `numpy`：

```console
$ uv pip show numpy
```

可以一次检查多个包。

## 验证环境

如果在多个步骤中安装，可能会在环境中安装具有冲突要求的包。

要检查环境中的冲突或缺少的依赖项：

```console
$ uv pip check
```
