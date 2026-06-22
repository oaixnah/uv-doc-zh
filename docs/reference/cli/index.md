---
subtitle: Commands
description: uv CLI 参考文档，涵盖 uv 命令行接口的完整命令列表，包括项目创建、依赖管理、虚拟环境、Python 版本管理、缓存管理等核心功能的用法说明。
---

# CLI 参考

## uv

一个极速的 Python 包管理器。

<h3 class="cli-reference">使用方法</h3>

```
uv [OPTIONS] <COMMAND>
```

<h3 class="cli-reference">命令</h3>

<dl class="cli-reference"><dt><a href="#uv-auth"><code>uv auth</code></a></dt><dd><p>管理认证</p></dd>
<dt><a href="#uv-run"><code>uv run</code></a></dt><dd><p>运行命令或脚本</p></dd>
<dt><a href="#uv-init"><code>uv init</code></a></dt><dd><p>创建新项目</p></dd>
<dt><a href="#uv-add"><code>uv add</code></a></dt><dd><p>添加项目依赖</p></dd>
<dt><a href="#uv-remove"><code>uv remove</code></a></dt><dd><p>移除项目依赖</p></dd>
<dt><a href="#uv-version"><code>uv version</code></a></dt><dd><p>读取或更新项目版本</p></dd>
<dt><a href="#uv-sync"><code>uv sync</code></a></dt><dd><p>更新项目环境</p></dd>
<dt><a href="#uv-lock"><code>uv lock</code></a></dt><dd><p>更新项目锁定文件</p></dd>
<dt><a href="#uv-export"><code>uv export</code></a></dt><dd><p>将项目锁定文件导出为其他格式</p></dd>
<dt><a href="#uv-tree"><code>uv tree</code></a></dt><dd><p>显示项目依赖树</p></dd>
<dt><a href="#uv-format"><code>uv format</code></a></dt><dd><p>格式化项目中的 Python 代码</p></dd>
<dt><a href="#uv-check"><code>uv check</code></a></dt><dd><p>对项目运行检查</p></dd>
<dt><a href="#uv-audit"><code>uv audit</code></a></dt><dd><p>审计项目依赖</p></dd>
<dt><a href="#uv-tool"><code>uv tool</code></a></dt><dd><p>运行和安装 Python 包提供的命令</p></dd>
<dt><a href="#uv-python"><code>uv python</code></a></dt><dd><p>管理 Python 版本和安装</p></dd>
<dt><a href="#uv-pip"><code>uv pip</code></a></dt><dd><p>使用兼容 pip 的接口管理 Python 包</p></dd>
<dt><a href="#uv-venv"><code>uv venv</code></a></dt><dd><p>创建虚拟环境</p></dd>
<dt><a href="#uv-build"><code>uv build</code></a></dt><dd><p>将 Python 包构建为源码分发包和 Wheel 包</p></dd>
<dt><a href="#uv-publish"><code>uv publish</code></a></dt><dd><p>上传分发包到索引</p></dd>
<dt><a href="#uv-workspace"><code>uv workspace</code></a></dt><dd><p>检查 uv 工作区</p></dd>
<dt><a href="#uv-cache"><code>uv cache</code></a></dt><dd><p>管理 uv 的缓存</p></dd>
<dt><a href="#uv-self"><code>uv self</code></a></dt><dd><p>管理 uv 可执行文件</p></dd>
<dt><a href="#uv-help"><code>uv help</code></a></dt><dd><p>显示命令的文档</p></dd>
</dl>
