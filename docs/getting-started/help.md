---
subtitle: Getting help
---

# 获取帮助

## 帮助菜单

`--help` 标志可用于查看命令的帮助菜单，例如，对于 `uv`：

```console
$ uv --help
```

要查看特定命令的帮助菜单，例如，对于 `uv init`：

```console
$ uv init --help
```

使用 `--help` 标志时，uv 会显示一个精简的帮助菜单。要查看命令的更长帮助菜单，请使用 `uv help`：

```console
$ uv help
```

要查看特定命令的详细帮助菜单，例如，对于 `uv init`：

```console
$ uv help init
```

使用详细帮助菜单时，uv 会尝试使用 `less` 或 `more` 对输出进行“分页”，这样就不会一次性显示所有内容。要退出分页器，请按 `q`。

## 查看版本

寻求帮助时，确定您正在使用的 uv 版本非常重要——有时问题在较新版本中已经解决。

要检查已安装的版本：

```console
$ uv self version
```

以下命令也有效：

```console
$ uv --version      # 与 `uv self version` 输出相同
$ uv -V             # 不会包括构建提交和日期
```

!!! note "注意"

    在 uv 0.7.0 之前，使用 `uv version` 而不是 `uv self version`。

## 问题排查

参考文档包含一个针对常见问题的[故障排查指南](../reference/troubleshooting/index.md)。

## 在 GitHub 上开启一个 issue

GitHub 上的[问题跟踪器](https://github.com/astral-sh/uv/issues)是报告错误和请求功能的好地方。请务必先搜索类似的问题，因为其他人很可能也遇到了同样的问题。

## 在 Discord 上聊天

Astral 有一个 [Discord 服务器](https://discord.com/invite/astral-sh)，这里是提问、了解更多关于 uv 以及与其他社区成员互动的好地方。
