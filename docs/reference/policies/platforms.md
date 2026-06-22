---
subtitle: Platform support
description: 本文档详细介绍了 uv 项目的平台支持策略，包括 Tier 1/2/3 三级支持体系、各 Linux 发行版的 glibc 与 musl 兼容性说明、Windows 和 macOS 的最低版本要求，以及官方二进制文件和 wheel 包的发布渠道。
---

# 平台支持

uv 对以下平台提供 Tier 1（第一级）支持：

- macOS (Apple Silicon)
- macOS (x86_64)
- Linux (x86_64)
- Windows (x86_64)

uv 在其 Tier 1 平台上持续进行构建、测试和开发。受 Rust 项目的启发，Tier 1 可以理解为
["保证可用"（guaranteed to work）](https://doc.rust-lang.org/beta/rustc/platform-support.html#tier-1)。

uv 对以下平台提供 Tier 2（第二级）支持
（["保证可构建"（guaranteed to build）](https://doc.rust-lang.org/beta/rustc/platform-support.html#tier-2-with-host-tools)）：

- Linux (PPC64LE)
- Linux (RISC-V64)
- Linux (aarch64)
- Linux (armv7)
- Linux (i686)
- Linux (s390x)
- Windows (arm64)

uv 对以下平台提供 Tier 3（第三级）支持
（["尽力而为"（best effort）](https://doc.rust-lang.org/beta/rustc/platform-support.html#tier-3)）：

- FreeBSD (x86_64)
- Windows (i686)

uv 在 GitHub 上为其 Tier 1 和 Tier 2 平台提供官方二进制文件，并在 [PyPI](https://pypi.org/project/uv/) 上提供预构建的 wheel 包。

Tier 2 平台会持续进行构建，但 uv 的测试套件不会在这些平台上运行，实际稳定性可能有所不同。

Tier 3 平台可能不会进行构建或测试，但 uv 会接受修复 bug 的补丁。

## Linux 版本

在 Linux 上，兼容性由 libc 版本决定。

uv 同时发布基于 glibc 和基于 musl 的发行版。

对于基于 glibc 的 Linux 发行版，uv 发布
[兼容 manylinux](https://peps.python.org/pep-0600/) 的 wheel 包和相应的二进制文件。这些制品依赖宿主机系统上可用的 glibc。在 manylinux wheel 标签中，版本号编码了该 wheel 所需的最低 glibc 版本；例如，`manylinux_2_17_x86_64` 要求 glibc 2.17 及以上版本。

uv 官方基于 glibc 的 wheel 包和二进制文件针对以下目标平台发布：

- `x86_64-unknown-linux-gnu`（`manylinux_2_17_x86_64`）
- `aarch64-unknown-linux-gnu`（`manylinux_2_28_aarch64`）
- `armv7-unknown-linux-gnueabihf`（`manylinux_2_17_armv7l`）
- `i686-unknown-linux-gnu`（`manylinux_2_17_i686`）
- `powerpc64le-unknown-linux-gnu`（`manylinux_2_17_ppc64le`）
- `riscv64gc-unknown-linux-gnu`（`manylinux_2_31_riscv64`）
- `s390x-unknown-linux-gnu`（`manylinux_2_17_s390x`）

uv 还针对以下目标平台发布基于 musl 的 wheel 包和完全静态链接的二进制文件：

- `x86_64-unknown-linux-musl`（`musllinux_1_1_x86_64`）
- `aarch64-unknown-linux-musl`（`musllinux_1_1_aarch64`）
- `armv7-unknown-linux-musleabihf`（`musllinux_1_1_armv7l`）
- `i686-unknown-linux-musl`（`musllinux_1_1_i686`）
- `riscv64gc-unknown-linux-musl`（`musllinux_1_1_riscv64`）
- `arm-unknown-linux-musleabihf`（`linux_armv6l`）

这些 wheel 包以 [兼容 musllinux](https://peps.python.org/pep-0656/) 的标签发布。然而，内嵌的 `uv` 二进制文件是完全静态链接的，不依赖宿主机系统上的 musl libc。

官方 [Docker 镜像](../../guides/integration/docker.md) 包含了这些针对 amd64 和 arm64 架构的完全静态链接的 musl uv 二进制文件。

## Windows 版本

最低支持的 Windows 版本为 Windows 10 和 Windows Server 2016，遵循
[Rust 自身的 Tier 1 支持](https://blog.rust-lang.org/2024/02/26/Windows-7.html)策略。

## macOS 版本

uv 支持 macOS 13 及以上版本（Ventura）。

已知 uv 在 macOS 12 上可以运行，但需要安装 `realpath` 可执行文件。
