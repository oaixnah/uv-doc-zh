---
subtitle: Compatibility with pip
description: 本文档详细介绍了 uv 与 pip 和 pip-tools 之间的兼容性，涵盖配置文件、预发布版本处理、多索引包解析、PEP 517 构建隔离、虚拟环境默认行为、解析策略差异、字节码编译、严格性规范执行等已知差异，并提供相应的解决方法和未来兼容性声明。
---

# 与 `pip` 和 `pip-tools` 的兼容性

uv 被设计为常见 `pip` 和 `pip-tools` 工作流的直接替代品（drop-in replacement）。

通俗地说，其意图是让现有的 `pip` 和 `pip-tools` 用户可以在无需对其打包工作流做出重大变更的情况下切换到 uv；并且在大多数情况下，将 `pip install` 替换为 `uv pip install` 应该可以"直接运行"。

然而，uv _并非_ 旨在成为 `pip` 的 _完全精确_ 克隆，你越是偏离常见的 `pip` 工作流，就越有可能遇到行为上的差异。在某些情况下，这些差异可能是已知且有意的；在其他情况下，它们可能是实现细节导致的；还有一些情况，它们可能是 bug。

本文档概述了 uv 与 `pip` 之间的已知差异，以及相关的理由、解决方法，以及未来兼容性的意图声明。

## 配置文件和环境变量

uv 不会读取特定于 `pip` 的配置文件或环境变量，如 `pip.conf` 或 `PIP_INDEX_URL`。

读取其他工具专用的配置文件和环境变量存在若干缺点：

1. 它需要与目标工具实现 bug 级别的兼容性，因为用户最终会依赖格式、解析器等方面的 bug。
2. 如果目标工具以某种方式 _更改_ 了格式，uv 就不得不以等效的方式进行更改。
3. 如果该配置以某种方式带有版本控制，uv 就需要知道用户期望使用 _哪个版本_ 的目标工具。
4. 它阻止 uv 引入任何目标工具中不存在的设置或配置，否则 `pip.conf`（或类似文件）将不再能被 `pip` 使用。
5. 它可能导致用户困惑，因为 uv 会读取实际上不影响其行为的设置，而许多用户可能 _并不_ 期望 uv 读取其他工具专用的配置文件。

相反，uv 支持自己的环境变量，如 `UV_INDEX_URL`。uv 还支持在 `uv.toml` 文件或 `pyproject.toml` 的 `[tool.uv.pip]` 部分中持久化配置。有关更多信息，请参见[配置文件](../concepts/configuration-files.md)。

## 预发布版本兼容性

默认情况下，uv 在两种情况下会在依赖解析期间接受预发布版本（pre-release versions）：

1. 如果包是直接依赖项，且其版本标记包含预发布说明符（例如 `flask>=2.0.0rc1`）。
2. 如果某个包的 _所有_ 已发布版本都是预发布版本。

如果依赖解析由于传递性预发布版本而失败，uv 将提示用户使用 `--prerelease allow` 重新运行，以允许所有依赖项的预发布版本。

或者，你可以将传递性依赖项添加到 `requirements.in` 文件中，并带上预发布说明符（例如 `flask>=2.0.0rc1`），以选择对该特定依赖项支持预发布版本。

总之，uv 需要预先知道解析器是否应该接受某个包的预发布版本。而 `pip` 则尊重传递性依赖项中的预发布标识符，如果没有稳定版本满足依赖项要求，则允许使用传递性依赖项的预发布版本。

!!! note

    在 pip 26.0 之前，此行为并不一致。

预发布版本是[出了名的难以建模](https://pubgrub-rs-guide.netlify.app/limitations/prerelease_versions)，并且是打包工具中常见的 bug 来源。uv 对预发布版本的处理是 _有意_ 受限的，并且 _有意_ 要求用户主动选择加入（opt-in）预发布版本，以确保正确性。

在未来，uv _可能_ 会支持传递性依赖项中的预发布标识符。然而，这很可能取决于 Python 打包规范的演进。现有的 PEP [并未涵盖"依赖解析"](https://discuss.python.org/t/handling-of-pre-releases-when-backtracking/40505/17)，而是专注于 _单个_ 版本说明符的行为。

## 存在于多个索引中的包

在 uv 和 `pip` 中，用户都可以指定多个包索引，从中搜索给定包的可用版本。然而，uv 和 `pip` 在处理存在于多个索引中的包时有所不同。

例如，假设某公司在私有索引（`--extra-index-url`）上发布了内部版本的 `requests`，但同时也默认允许从 PyPI 安装包。在这种情况下，私有的 `requests` 将与 PyPI 上的公共 [`requests`](https://pypi.org/project/requests/) 发生冲突。

当 uv 跨多个索引搜索包时，它会按顺序遍历索引（优先选择 `--extra-index-url` 而非默认索引），并在找到匹配项后立即停止搜索。这意味着，如果一个包存在于多个索引中，uv 将把候选版本限制在包含该包的第一个索引中存在的版本。

而 `pip` 则会合并所有索引的候选版本，并从合并后的集合中选择最佳版本，尽管它对[搜索索引的顺序不做任何保证](https://github.com/pypa/pip/issues/5045#issuecomment-369521345)，并且期望包在名称和版本上是唯一的，即使跨索引也是如此。

uv 的行为意味着，如果一个包存在于内部索引中，则它应始终从内部索引安装，而绝不会从 PyPI 安装。其目的是防止"依赖混淆"（dependency confusion）攻击，即攻击者在 PyPI 上发布一个与内部包同名的恶意包，从而导致安装恶意包而非内部包。例如，参见 2022 年 12 月的[`torchtriton` 攻击](https://pytorch.org/blog/compromised-nightly-dependency/)事件。

从 v0.1.39 开始，用户可以通过 `--index-strategy` 命令行选项或 `UV_INDEX_STRATEGY` 环境变量选择加入 `pip` 风格的多索引行为，该选项支持以下值：

- `first-index`（默认）：跨所有索引搜索每个包，将候选版本限制在包含该包的第一个索引中存在的版本，优先选择 `--extra-index-url` 索引而非默认索引 URL。
- `unsafe-first-match`：跨所有索引搜索每个包，但优先选择包含兼容版本的第一个索引，即使其他索引上有更新的版本。
- `unsafe-best-match`：跨所有索引搜索每个包，并从合并的候选版本集合中选择最佳版本。

虽然 `unsafe-best-match` 最接近 `pip` 的行为，但它使用户面临"依赖混淆"攻击的风险。

uv 还支持将包固定到专用索引（参见：[_索引_](../concepts/indexes.md#pinning-a-package-to-an-index)），从而使给定包 _始终_ 从特定索引安装。

## PEP 517 构建隔离

uv 默认使用 [PEP 517](https://peps.python.org/pep-0517/) 构建隔离（类似于 `pip install --use-pep517`），遵循 `pypa/build` 的做法，并预期 `pip` 在未来会默认采用 PEP 517 构建（[pypa/pip#9175](https://github.com/pypa/pip/issues/9175)）。

如果包由于缺少构建时依赖项而无法安装，请尝试使用该包的更新版本；如果问题仍然存在，请考虑向包维护者提交问题，请求他们更新打包设置，以声明正确的 PEP 517 构建时依赖项。

作为一种应急手段，你可以预装包的构建依赖项，然后使用 `--no-build-isolation` 运行 `uv pip install`，如下所示：

```shell
uv pip install wheel && uv pip install --no-build-isolation biopython==1.77
```

有关已知在 PEP 517 构建隔离下失败的包列表，请参见 [#2252](https://github.com/astral-sh/uv/issues/2252)。

## 传递性 URL 依赖项

虽然 uv 包含对 URL 依赖项（例如 `ruff @ https://...`）的一流支持，但它在处理 _传递性_ URL 依赖项方面与 pip 有两个不同之处。

首先，uv 假设非 URL 依赖项不会将 URL 依赖项引入解析中。换句话说，它假设从注册表获取的依赖项本身不依赖于 URL。如果非 URL 依赖项 _确实_ 引入了 URL 依赖项，uv 将在解析期间拒绝该 URL 依赖项。（注意，PyPI 不允许已发布的包依赖 URL 依赖项；其他注册表可能更宽松。）

其次，如果约束（`--constraint`）或覆盖（`--override`）是使用直接 URL 依赖项定义的，并且受约束的包有自己的直接 URL 依赖项，uv _可能_ 会在解析期间拒绝该传递性直接 URL 依赖项，前提是该 URL 在输入需求集合的其他地方没有被引用。

如果 uv 拒绝了传递性 URL 依赖项，最佳做法是将该 URL 依赖项作为直接依赖项添加到相关的 `pyproject.toml` 或 `requirement.in` 文件中，因为上述约束不适用于直接依赖项。

## 默认使用虚拟环境

`uv pip install` 和 `uv pip sync` 被设计为默认与虚拟环境配合使用。

具体来说，uv 将始终将包安装到当前激活的虚拟环境中，或者搜索当前目录或任何父目录中名为 `.venv` 的虚拟环境（即使该环境未被激活）。

这与 `pip` 不同，`pip` 在没有激活虚拟环境时会将包安装到全局环境中，并且不会搜索未激活的虚拟环境。

在 uv 中，你可以通过 `--python /path/to/python` 选项提供 Python 可执行文件的路径来安装到非虚拟环境中，或者通过 `--system` 标志安装到 `PATH` 中找到的第一个 Python 解释器中，类似于 `pip`。

换句话说，uv 反转了默认行为，要求显式选择加入（opt-in）才能安装到系统 Python 中，这可能导致破坏和其他复杂问题，并且只应在有限的情况下进行。

有关更多信息，请参见["使用任意 Python 环境"](./environments.md#using-arbitrary-python-environments)。

## 解析策略

对于一组给定的依赖项说明符，通常不存在单一的"正确"包集合可供安装。相反，存在许多满足说明符的有效包集合。

`pip` 和 uv 都不保证将安装的 _确切_ 包集合；只保证解析结果是一致的、确定性的，并且符合说明符。因此，在某些情况下，`pip` 和 uv 会产生不同的解析结果；然而，两种解析结果 _应该_ 都是同样有效的。

例如，考虑以下情况：

```python title="requirements.in"
starlette
fastapi
```

在撰写本文时，最新的 `starlette` 版本是 `0.37.2`，最新的 `fastapi` 版本是 `0.110.0`。然而，`fastapi==0.110.0` 也依赖于 `starlette`，并引入了一个上限约束：`starlette>=0.36.3,<0.37.0`。

如果解析器优先选择包含最新版本的 `starlette`，则需要使用排除了 `starlette` 上限约束的旧版本 `fastapi`。实际上，这需要回退到 `fastapi==0.1.17`：

```python title="requirements.txt"
# This file was autogenerated by uv via the following command:
#    uv pip compile requirements.in
annotated-types==0.6.0
    # via pydantic
anyio==4.3.0
    # via starlette
fastapi==0.1.17
idna==3.6
    # via anyio
pydantic==2.6.3
    # via fastapi
pydantic-core==2.16.3
    # via pydantic
sniffio==1.3.1
    # via anyio
starlette==0.37.2
    # via fastapi
typing-extensions==4.10.0
    # via
    #   pydantic
    #   pydantic-core
```

或者，如果解析器优先选择包含最新版本的 `fastapi`，则需要使用满足上限约束的旧版本 `starlette`。实际上，这需要回退到 `starlette==0.36.3`：

```python title="requirements.txt"
# This file was autogenerated by uv via the following command:
#    uv pip compile requirements.in
annotated-types==0.6.0
    # via pydantic
anyio==4.3.0
    # via starlette
fastapi==0.110.0
idna==3.6
    # via anyio
pydantic==2.6.3
    # via fastapi
pydantic-core==2.16.3
    # via pydantic
sniffio==1.3.1
    # via anyio
starlette==0.36.3
    # via fastapi
typing-extensions==4.10.0
    # via
    #   fastapi
    #   pydantic
    #   pydantic-core
```

当 uv 的解析结果以不理想的方式与 `pip` 不同时，通常表明说明符过于宽松，用户应考虑收紧它们。例如，在 `starlette` 和 `fastapi` 的情况下，用户可以要求 `fastapi>=0.110.0`。

## `pip check`

目前，`uv pip check` 会显示以下诊断信息：

- 包没有 `METADATA` 文件，或 `METADATA` 文件无法解析。
- 包的 `Requires-Python` 与正在运行的 Python 解释器的版本不匹配。
- 包依赖于未安装的包。
- 包依赖于已安装的包，但版本不兼容。
- 虚拟环境中安装了多个版本的包。

在某些情况下，`uv pip check` 会显示 `pip check` 不会显示的诊断信息，反之亦然。例如，与 `uv pip check` 不同，`pip check` _不会_ 在当前环境中安装了多个版本的包时发出警告。

## `--user` 和 `user` 安装方案

uv 不支持 `--user` 标志，该标志基于 `user` 安装方案来安装包。相反，我们建议使用虚拟环境来隔离包安装。

此外，如果 pip 检测到用户对目标目录没有写入权限，它会回退到 `user` 安装方案，这在某些系统上安装到系统 Python 时会发生。uv 不实现任何此类回退。

有关更多信息，请参见 [#2077](https://github.com/astral-sh/uv/issues/2077)。

## `--only-binary` 强制执行

`--only-binary` 参数用于将安装限制为预构建的二进制分发包。当提供 `--only-binary :all:` 时，pip 和 uv 都会拒绝从 PyPI 和其他注册表构建源分发包（source distributions）。

然而，当依赖项以直接 URL 的形式提供时（例如 `uv pip install https://...`），pip _不会_ 强制执行 `--only-binary`，并且会为所有此类包构建源分发包。

而 uv _会_ 对直接 URL 依赖项强制执行 `--only-binary`，但有一个例外：对于 `uv pip install https://... --only-binary flask`，如果 uv 无法事先推断出包名，它 _将_ 构建给定 URL 的源分发包，因为在不构建元数据的情况下，uv 无法确定该包是否被"允许"。

pip 和 uv 都允许在提供 `--only-binary` 时构建和安装可编辑需求（editable requirements）。例如，`uv pip install -e . --only-binary :all:` 是允许的。

## `--no-binary` 强制执行

`--no-binary` 参数用于将安装限制为源分发包。当提供 `--no-binary` 时，uv 将拒绝安装预构建的二进制分发包，但 _会_ 重用本地缓存中已存在的任何二进制分发包。

此外，与 pip 不同，uv 的解析器在提供 `--no-binary` 时仍然会从预构建的二进制分发包中读取元数据。

## `manylinux_compatible` 强制执行

[PEP 600](https://peps.python.org/pep-0600/#package-installers) 描述了一种机制，Python 发行版可以通过在 `_manylinux` 标准库模块上定义 `manylinux_compatible` 函数来选择退出 `manylinux` 兼容性。

uv 会尊重 `manylinux_compatible`，但仅针对当前 glibc 版本进行测试，并全局应用 `manylinux_compatible` 的返回值。

换句话说，如果 `manylinux_compatible` 返回 `True`，uv 将把系统视为 `manylinux` 兼容；如果返回 `False`，uv 将把系统视为 `manylinux` 不兼容，而不会为每个 glibc 版本调用 `manylinux_compatible`。

这种方法并非对规范的完整实现，但与常见的覆盖式 `manylinux_compatible` 实现兼容，例如 [`no-manylinux`](https://pypi.org/project/no-manylinux/)：

```python
from __future__ import annotations
manylinux1_compatible = False
manylinux2010_compatible = False
manylinux2014_compatible = False


def manylinux_compatible(*_, **__):  # PEP 600
    return False
```

## 字节码编译

与 `pip` 不同，uv 默认不会在安装期间将 `.py` 文件编译为 `.pyc` 文件（即 uv 不会创建或填充 `__pycache__` 目录）。要在安装期间启用字节码编译，请向 `uv pip install` 或 `uv pip sync` 传递 `--compile-bytecode` 标志，或将 `UV_COMPILE_BYTECODE` 环境变量设置为 `1`。

跳过字节码编译在某些工作流中可能是不理想的；例如，我们建议在 [Docker 构建](../guides/integration/docker.md)中启用字节码编译，以缩短启动时间（代价是增加构建时间）。

由于字节码编译会抑制 Python 解释器发出的各种警告，在极少数情况下，你可能会在运行使用 uv 安装的 Python 代码时看到 `SyntaxWarning` 或 `DeprecationWarning` 消息，而这些消息在使用 `pip` 时不会出现。这些是有效的警告，但通常被字节码编译过程隐藏，可以忽略它们、在上游修复它们，或通过在 uv 中启用字节码编译来同样地抑制它们。

## 严格性和规范执行

uv 往往比 `pip` 更严格，并且通常会拒绝 `pip` 会安装的包。例如，uv 拒绝包含无效 URL 片段的 HTML 索引（参见：[PEP 503](https://peps.python.org/pep-0503/)），而 `pip` 会忽略此类片段。

在某些情况下，uv 会对已知存在特定规范合规问题的流行包实现宽松处理。

如果 uv 因规范违规而拒绝 `pip` 会安装的包，最佳做法是首先尝试安装该包的更新版本；如果失败，则向包维护者报告问题。

## `pip` 命令行选项和子命令

uv 不支持完整的 `pip` 命令行选项和子命令集，尽管它确实支持其中很大一部分。

缺失的选项和子命令会根据用户需求度和实现复杂度进行优先级排序，并通常在单独的问题中跟踪。例如：

- [`--trusted-host`](https://github.com/astral-sh/uv/issues/1339)
- [`--user`](https://github.com/astral-sh/uv/issues/2077)

如果你遇到缺失的选项或子命令，请搜索问题跟踪器，查看是否已有相关报告；如果没有，请考虑打开一个新问题。欢迎为任何现有问题点赞以表达你的兴趣。

## 注册表认证

uv 不支持 `pip` 的 `--keyring-provider` 的 `auto` 或 `import` 选项。目前，仅支持 `subprocess` 选项。

与 `pip` 不同，uv 默认不启用 keyring 认证。

与 `pip` 不同，uv 不会等待请求返回 HTTP 401 后再搜索认证信息。uv 会将认证信息附加到所有有可用凭据的主机的请求中。

## `egg` 支持

uv 不支持 `pip` 中被视为遗留或已弃用的功能。例如，uv 不支持 `.egg` 格式的分发包。

然而，uv 确实对以下内容有部分支持：(1) `.egg-info` 格式的分发包（偶尔出现在 Docker 镜像和 Conda 环境中）和 (2) 遗留的可编辑 `.egg-link` 格式的分发包。

具体来说，uv 不支持安装新的 `.egg-info` 或 `.egg-link` 格式的分发包，但会在解析期间识别任何此类现有分发包，通过 `uv pip list` 和 `uv pip freeze` 列出它们，并通过 `uv pip uninstall` 卸载它们。

## 构建约束

当通过 `--constraint`（或 `UV_CONSTRAINT`）提供约束时，uv _不会_ 在解析构建依赖项（即构建源分发包）时应用这些约束。相反，构建约束应通过专用的 `--build-constraint`（或 `UV_BUILD_CONSTRAINT`）选项提供。

## 包名规范化

uv 使用 [PEP 503](https://peps.python.org/pep-0503/) 规范化的包名，而 `pip` 则保留注册表上发布的逐字包名。

例如，`uv pip list` 显示规范化的包名（如 `docstring-parser`），而 `pip list` 显示非规范化的包名（如 `docstring_parser`）：

```shell
(venv) $ diff --side-by-side  <(pip list) <(uv pip list)
Package          Version					Package          Version
---------------- -------					---------------- -------
docstring_parser 0.16					      |	docstring-parser 0.16
jaraco.classes   3.4.0					      |	jaraco-classes   3.4.0
more-itertools   10.7.0				    		more-itertools   10.7.0
pip              25.1					    	pip              25.1
PyMuPDFb         1.24.10				      |	pymupdfb         1.24.10
PyPDF2           3.0.1					      |	pypdf2           3.0.1
```
