---
subtitle: Platform support
description: 了解 uv 项目的平台支持。
---

# 平台支持

uv 为以下平台提供第 1 层支持：

- macOS (Apple Silicon)
- macOS (x86_64)
- Linux (x86_64)
- Windows (x86_64)

uv 针对其第 1 层平台进行持续构建、测试和开发。受 Rust 项目的启发，第 1 层可以被认为是[“保证能用”](https://doc.rust-lang.org/beta/rustc/platform-support.html)。

uv 为以下平台提供第 2 层支持（[“保证能构建”](https://doc.rust-lang.org/beta/rustc/platform-support.html)）：

- Linux (PPC64)
- Linux (PPC64LE)
- Linux (aarch64)
- Linux (armv7)
- Linux (i686)
- Linux (s390x)

uv 为其第 1 层和第 2 层平台向 [PyPI](https://pypi.org/project/uv/) 提供预构建的 wheel。然而，虽然第 2 层平台是持续构建的，但它们没有经过持续测试或开发，因此实际稳定性可能会有所不同。

除了第 1 层和第 2 层平台之外，已知 uv 可以在 i686 Windows 上构建，并且已知*不能*在 aarch64 Windows 上构建，但目前不认为这两个平台都受支持。支持的最低 Windows 版本是 Windows 10 和 Windows Server 2016，遵循 [Rust 自己的第 1 层支持](https://blog.rust-lang.org/2024/02/26/Windows-7.html)。

## macOS 版本

uv 支持 macOS 13+ (Ventura)。

已知 uv 可在 macOS 12 上运行，但需要安装 `realpath` 可执行文件。

## Python 支持

uv 支持并针对以下 Python 版本进行了测试：

- 3.8
- 3.9
- 3.10
- 3.11
- 3.12
- 3.13
- 3.14

uv 为以下 Python 实现提供第 1 层支持：

- CPython

与平台一样，第 1 层支持可以被认为是“保证能用”。uv 支持这些实现的托管安装，并且构建由 Astral 维护。

uv 为以下各项提供第 2 层支持：

- PyPy
- GraalPy

uv “预期可以”与这些实现一起使用。uv 还支持这些 Python 实现的托管安装，但构建不由 Astral 维护。

uv 为以下各项提供第 3 层支持：

- Pyston
- Pyodide

uv “应该可以”与这些实现一起使用，但稳定性可能会有所不同。
