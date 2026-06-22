---
subtitle: Workspace Metadata
description: 本文介绍 uv workspace metadata 命令的用法，详细说明其导出的 JSON 依赖图结构，包括 5 种节点类型（script、workspace、package、extra、group）、多版本处理策略、冲突检测机制，以及通过标记（marker）进行平台特定依赖解析的最佳实践。
---

# 工作区元数据（Workspace Metadata）

`uv workspace metadata` 将 uv 掌握的关于工作区或 PEP 723 脚本的信息导出为 JSON，以便其他工具使用。特别是，如果你需要访问 `uv.lock` 或脚本锁文件中的信息，应优先使用此命令的输出，因为锁文件并非我们保证其稳定性的格式。通过 `--script path/to/script.py` 参数可以请求脚本的元数据。

主要结构是 `"resolution"` 字段，其中包含 `uv.lock` 所编码的依赖图（dependency graph），包含精确的包版本。

图的边（edge）是每个节点定义的 `dependencies`。这些是安装该节点时也必须安装的依赖（以及它们的 `dependencies` 递归地传递下去，需注意该图中出现循环是完全正常的）。每个依赖条目将包含一个 `id` 用于引用所指向的节点，以及一个可选的 `marker`，用于[指定该依赖在哪些平台上需要](https://packaging.python.org/en/latest/specifications/dependency-specifiers/#dependency-specifiers)（如果没有标记，则该依赖始终需要）。

图中源自包的节点由包 `name`（名称）、`version`（版本）、`source`（来源）和 `kind`（类型）唯一标识。脚本和工作区节点由其路径标识。工作区根依赖组节点由其组名和工作区路径标识。所有节点 id 应被视为不透明（opaque）的。

图中有 5 种节点类型：

- `"script"` -- PEP 723 脚本及其直接依赖
- `"workspace"` -- 工作区根及其工作区专属依赖组
- `"package"` -- 包本身
- `{ "extra": "extraname" }` -- 包定义的额外依赖（extra）
- `{ "group": "groupname" }` -- 包或工作区根定义的依赖组

（未来我们将为[构建环境](https://docs.astral.sh/uv/concepts/projects/config/#build-isolation)的依赖添加 "build" 节点。）

如果你想安装 `mypackage`，找到其 `"kind": "package"` 节点。该节点还将包含其 sdist、wheel、额外依赖（`optional_dependencies`）和依赖组（`dependency_groups`）的信息。

如果你想安装 `mypackage[myextra]`，则找到 `mypackage` 对应 `"kind": { "extra": "myextra" }` 的节点（该节点将始终依赖于 `mypackage`）。如果你想安装 `mypackage[extra1, extra2]`，则找到 `mypackage[extra1]` 和 `mypackage[extra2]` 对应的两个节点。

如果你想安装依赖组 `mypackage:mygroup`，则找到 `mypackage` 对应 `"kind": { "group": "mygroup" }` 的节点（该节点 _不会_ 依赖于 `mypackage`，因为依赖组只是你在处理包本身时可能需要的依赖列表）。

如果工作区根定义了依赖组但其本身不是一个包，则其 `"workspace"` 节点通过 `dependency_groups` 提供相应的组节点 id。

## 处理同一包的多个版本

一个包的两个版本不能安装到同一个 Python 环境中，但依赖图可能仍包含同一包的多个版本。这可能由两种不同原因导致。

第一种方式是[不同平台](https://packaging.python.org/en/latest/specifications/dependency-specifiers/#dependency-specifiers)有冲突的需求，迫使使用不同的包版本。

第二种方式是当工作区存在[冲突](https://docs.astral.sh/uv/concepts/resolution/#conflicting-dependencies)时，意味着某些工作区成员或其额外依赖是互斥的，同一时间只能安装其中一个。关于冲突的信息可以在顶层的 `conflicts` 字段中找到。

我们提供的具体保证是：**对于任何具体的[标记](https://packaging.python.org/en/latest/specifications/dependency-specifiers/#dependency-specifiers)选择，如果你选择了一组没有[冲突](https://docs.astral.sh/uv/concepts/resolution/#conflicting-dependencies)的包进行安装，那么最终要安装的包集合中将不会包含同一包的多个版本**。

如果你只想获取"此工作区使用的所有 pydantic 版本"，可以遍历节点列表并收集每个实例。然而，如果你想专门分析图并获取实际的解析结果，则可能需要查阅 `conflicts` 并了解如何为特定平台解析 `markers`。

在处理同一包的多个版本时，避免错误的最佳方法是将对依赖图的查询根植于工作区根、工作区成员或请求的脚本的操作上。这些是图的自然入口点，可以为诸如"安装工作区 `dev` 组"、"安装 `member1` 和 `member2[extra]`"或"安装此脚本声明的依赖"等操作提供一致的响应。

另一种表述方式是：尽可能避免通过遍历 `resolution` 对象来查找节点。只使用元数据其他部分提供的 id 来像访问映射（map）一样访问 `resolution`。对于工作区，工作区根是 `workspace.id`，包入口点列在 `members` 数组中。对于脚本，初始 id 是 `script.id`。从那里你可以通过跟随依赖边递归地发现其他包。

因此，与其直接在依赖图中查找 anyio 的节点，不如先决定要分析哪些工作区成员，就好像它们即将被安装一样。在遍历你要安装的依赖项的 `dependencies` 时，你可能会访问到 anyio 的一个实例，这就是你应该使用的那个。如果你访问到多个 anyio 实例，则意味着你选择了一组有冲突的待安装项，而 uv 永远不会选择这样的组合。

因此，如果你想分析安装工作区成员 `mypackage` 的 `dev` 依赖组，大致如下：

```python
member = find_by_name(metadata.members, "mypackage")
member_node = metadata.resolution[member.id]
group = find_by_name(member_node.dependency_groups, "dev")
group_node = metadata.resolution[group.id]
visit(metadata, [group_node])
```

对于工作区根上定义的依赖组，通过工作区节点查找：

```python
workspace_node = metadata.resolution[metadata.workspace.id]
group = find_by_name(workspace_node.dependency_groups, "dev")
group_node = metadata.resolution[group.id]
visit(metadata, [group_node])
```

如果你想分析两个特定工作区成员一起安装的情况，大致如下：

```python
to_analyze = []
for member_name in ["package1", "package2"]:
  member = find_by_name(metadata.members, member_name)
  member_node = metadata.resolution[member.id]
  to_analyze.append(member_node)
visit(metadata, to_analyze)
```

对于脚本，以完全相同的方式从其解析节点开始：

```python
script_node = metadata.resolution[metadata.script.id]
visit(metadata, [script_node])
```

其中 `visit` 是你喜欢的图遍历算法，例如深度优先搜索（depth-first search）：

```python
def visit(metadata: UvMetadata, to_analyze: list[Node]):
  visited = set()
  while len(to_analyze) > 0:
    node = to_analyze.pop()

    # 通过避免重复访问节点来处理循环
    if node.id in visited:
      continue
    visited.add(node.id)

    # 我们还需要分析其依赖项
    for dependency in node.dependencies:
      # 仅当边满足目标平台的标记时才跟随
      if dependency.marker and not satisfies(platform, dependency.marker):
        continue
      to_analyze.append(metadata.resolution[dependency.id])

    # 分析我们遇到的每个包节点
    if node.kind == "package":
      print(node.name, node.version, node.source)
```

## 模式（Schema）

格式的完整 JSON Schema 将在格式定稿后提供。

以下是一个带注释的、人类可读的示例：

```js
{
  // 关于此输出模式的信息
  "schema": {
    // 此输出的版本，当前为 "preview"
    "version": "preview"
  },
  // 可以找到 uv.lock 的目录
  "workspace_root": "/workspace",
  // 关于环境的信息，目前仅在使用 `--sync` 时可用
  "environment": {
    // 环境根目录的绝对路径
    "root": "/workspace/.venv"
  },
  // 关于脚本目标的信息，仅在使用 `--script` 时存在。
  // 工作区元数据改用下面的 `workspace` 和 `members` 作为图入口点。
  "script": {
    // 脚本的绝对路径
    "path": "/workspace/script.py",
    // 脚本节点在下面 `resolution` 映射中的 id
    "id": "script+/workspace/script.py"
  },
  // 关于工作区目标的信息，使用 `--script` 时省略。
  "workspace": {
    // 工作区根的绝对路径
    "path": "/workspace",
    // 工作区节点在下面 `resolution` 映射中的 id
    "id": "workspace+/workspace"
  },
  // 此工作区对 Python 版本的任何要求
  //
  // `marker` 字段都有此隐式约束，为简洁起见而省略
  "requires_python": ">=3.12",
  // 工作区成员列表
  "members": [
    {
      // 包的名称
      "name": "mypackage",
      // 包含其 pyproject.toml 的目录
      "path": "/workspace/packages/mypackage",
      // 此包信息在下面 `resolution` 映射中的 id
      "id": "mypackage==0.1.0@editable+/workspace/packages/mypackage"
    },
  ],
  // 一组互斥的工作区项集合，不能同时安装，
  // 大概是因为它们需要安装同一包的不同版本。
  //
  // 任何尝试安装属于同一集合的两个项的尝试都必须被拒绝。
  //
  // 共有 3 种项：
  //
  // * Project -- "kind": "project"
  // * Extra   -- "kind": { "extra": "extraname" }
  // * Group   -- "kind": { "group": "groupname" }
  "conflicts": {
    "sets": [
      {
        "items": [
          {
            "package": "mypackage",
            "kind": { "extra": "myextra" }
            "id": "mypackage[myextra]==0.1.0@editable+/workspace/packages/mypackage",
          }
          {
            "package": "mypackage",
            "kind": { "group": "mygroup" }
            "id": "mypackage:mygroup==0.1.0@editable+/workspace/packages/mypackage",
          }
        ]
      }
    ]
  }
  // 关于包和依赖的已解析信息。
  //
  // 此映射中的每个条目都是依赖图中的一个节点。目前
  // 依赖图中有 5 种节点，不过未来计划添加更多。
  //
  // * Scripts  -- "kind": "script"
  // * Workspaces -- "kind": "workspace"
  // * Packages -- "kind": "package"
  // * Extras   -- "kind": { "extra": "extraname" }
  // * Groups   -- "kind": { "group": "groupname" }
  //
  // 包节点包含大部分元数据，而其他节点主要只是一个依赖列表。
  // 包含不同类型的节点是为了鼓励对图的正确分析。例如，
  // `mypackage[someextra]` 的节点始终依赖于 `mypackage`，
  // 而 `mypackage:somegroup` 则不会（因为依赖组只是
  // 在处理 `mypackage` 时可能想安装的包列表）。像
  // `mypackage[extra1, extra2]` 这样的语法糖会被分解为
  // 对 `mypackage[extra1]` 和 `mypackage[extra2]` 的单独依赖。
  //
  // 此处使用的 id 是人类可读的，但应作为不透明值处理（节点中
  // 包含的相同信息以更方便的形式提供）。
  "resolution": {

    // 当使用 `--script` 请求元数据时，脚本节点存在。其依赖项
    // 是脚本声明的直接需求。
    "script+/workspace/script.py": {
      "kind": "script",
      "path": "/workspace/script.py",
      "dependencies": [
        {
          "id": "iniconfig==2.0.0@registry+https://pypi.org/simple"
        }
      ]
    },

    // 工作区节点拥有直接定义在工作区根上的元数据。
    "workspace+/workspace": {
      "kind": "workspace",
      "path": "/workspace",
      "dependencies": [],
      "dependency_groups": [
        {
          "name": "dev",
          "id": "workspace+/workspace:dev"
        }
      ]
    },

    // 此节点是定义在非包工作区根上的依赖组。
    "workspace+/workspace:dev": {
      "kind": { "group": "dev" },
      "path": "/workspace",
      "dependencies": [
        {
          "id": "iniconfig==2.0.0@registry+https://pypi.org/simple"
        }
      ]
    },

    // 此节点是一个工作区成员
    "mypackage==0.1.0@editable+/workspace/packages/mypackage": {
      // 包的名称
      "name": "mypackage",
      // 包的版本（可能缺失，因为源代码树不需要版本）
      "version": "0.1.0",
      // 包的来源，此例中是一个 editable，其相对于
      // `workspace_root` 的路径为 `./packages/mypackage`
      "source": {
        "editable": "/workspace/packages/mypackage"
      },
      // 节点的类型，此例中为 "package"（有关详细信息，请参阅上面关于 `resolution` 的文档）
      "kind": "package",
      // 要将此节点安装到环境中也必须安装的依赖项
      "dependencies": [
        {
          // 要查找详细信息的节点 id
          "id": "iniconfig==2.0.0@registry+https://pypi.org/simple"
          "marker": "marker": "sys_platform == 'linux'"
        }
      ],
      // 此包定义的额外依赖
      "optional_dependencies": [
        {
          "name": "myextra",
          "id": "mypackage[myextra]==0.1.0@editable+/workspace/packages/mypackage"
        }
      ],
      // 此包定义的依赖组
      "dependency_groups": [
        {
          "name": "mygroup",
          "id": "mypackage:mygroup==0.1.0@editable+/workspace/packages/mypackage"
        }
      ]
    },

    // 此节点是工作区成员的一个 extra
    "mypackage[myextra]==0.1.0@editable+/workspace/packages/mypackage": {
      // 这些字段将与上面的包节点匹配
      "name": "mypackage",
      "version": "0.1.0",
      "source": {
        "editable": "/workspace/packages/mypackage"
      },
      // 但这两个字段将与上面的包节点不同
      "kind": { "extra": "myextra" },
      "dependencies": [
        {
          "id": "mypackage==0.1.0@editable+/workspace/packages/mypackage"
        }
        {
          "id": "anyio==2.0.0@registry+https://pypi.org/simple"
        }
      ]
    },

    // 此节点是工作区成员的一个依赖组
    "mypackage:mygroup==0.1.0@editable+/workspace/packages/mypackage": {
      // 这些字段将与上面的包节点匹配
      "name": "mypackage",
      "version": "0.1.0",
      "source": {
        "editable": "/workspace/packages/mypackage"
      },
      // 但这两个字段将与上面的包节点不同
      "kind": { "extra": "myextra" },
      "dependencies": [
        {
          "id": "anyio==1.0.0@registry+https://pypi.org/simple"
        }
      ]
    },

    // 此节点是 PyPI 上的一个包
    "iniconfig==2.0.0@registry+https://pypi.org/simple": {
      "name": "iniconfig",
      "version": "2.0.0",
      // registry 来源如下所示
      "source": {
        "registry": {
          "url": "https://pypi.org/simple"
        }
      },
      "kind": "package",
      "dependencies": [],
      // 包的源代码分发包（source distribution）的详细信息
      "sdist": {
        // 也可能是 `path`
        "url": "https://files.pythonhosted.org/packages/d7/4b/cbd8e699e64a6f16ca3a8220661b5f83792b3017d0f79807cb8708d33913/iniconfig-2.0.0.tar.gz",
        "hashes": {
          "sha256": "2d91e135bf72d31a410b17c16da610a82cb55f6b0477d1a902134b24a455b8b3"
        },
        "size": 4646,
        "upload_time": "2023-01-07T11:08:11.254Z"
      },
      // 我们为此包找到的 wheel
      "wheels": [
        {
          // 也可能是 `path`
          "url": "https://files.pythonhosted.org/packages/ef/a6/62565a6e1cf69e10f5727360368e451d4b7f58beeac6173dc9db836a5b46/iniconfig-2.0.0-py3-none-any.whl",
          "hashes": {
            "sha256": "b6a85871a79d2e3b22d2d1b94ac2824226a63c6b741c88f7ae975f18b6778374"
          },
          "size": 5892,
          "upload_time": "2023-01-07T11:08:09.864Z",
          // 解析此文件名可以了解 wheel 支持的平台
          "filename": "iniconfig-2.0.0-py3-none-any.whl"
        }
      ]
    }

    // ...以此类推
    "anyio==1.0.0@registry+https://pypi.org/simple": { ... }
    "anyio==2.0.0@registry+https://pypi.org/simple": { ... }
  }
}
```
