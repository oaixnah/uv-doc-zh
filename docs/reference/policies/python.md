# Python 支持

## Python 版本

uv 对以下 Python 版本提供 Tier 1 支持：

- 3.10
- 3.11
- 3.12
- 3.13
- 3.14

与[平台支持](./platforms.md)类似，Tier 1 支持可以理解为"保证可用"。uv 会持续针对这些版本进行测试。

uv 对以下版本提供 Tier 2 支持：

- 3.6
- 3.7
- 3.8
- 3.9

uv 在这些版本上"预期可正常工作"。uv 会针对这些版本进行测试，但它们已到达[生命周期终点（end-of-life）](https://devguide.python.org/versions/)，不再接收安全修复。我们不建议使用这些版本。

uv 还对 Python 3.15 的预发布版本提供 Tier 2 支持。

uv 不支持 Python 3.6 之前的版本。

## Python 实现

uv 对以下 Python 实现提供 Tier 1 支持：

- CPython

与[平台支持](./platforms.md)类似，Tier 1 支持可以理解为"保证可用"。uv 支持这些实现的托管安装，且相关构建由 Astral 维护。

uv 对以下实现提供 Tier 2 支持：

- PyPy
- GraalPy
- Pyodide

uv 在这些实现上"预期可正常工作"。uv 同样支持这些 Python 实现的托管安装，但相关构建不由 Astral 维护。

uv 对以下实现提供 Tier 3 支持：

- Pyston

uv 在这些实现上"应该可以工作"，但稳定性可能有所差异。
