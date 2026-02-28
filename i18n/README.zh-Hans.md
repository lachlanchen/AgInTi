[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Repository](https://img.shields.io/badge/Repository-AgInTi-0f172a?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lachlanchen/AgInTi)
[![Docs](https://img.shields.io/badge/Docs-README%20Bootstrap-0ea5e9?style=for-the-badge&logo=mdbook&logoColor=white)](#aginti)
[![Localization](https://img.shields.io/badge/i18n-10%20locales-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)](#documentation-inputs-and-generated-artifacts)
[![Status](https://img.shields.io/badge/Stage-Documentation%20Pipeline-f59e0b?style=for-the-badge&logo=githubactions&logoColor=white)](#scope-and-snapshot)
[![License](https://img.shields.io/badge/License-TBD-94a3b8?style=for-the-badge&logo=readme&logoColor=white)](#license)

这是一个以 README 为先的仓库脚手架，用于维护完整的英文 README 并同步多语言文档。

## 🧭 快速导航

| 类型 | 目标 |
|---|---|
| 仓库工作流 | [范围和快照](#-scope-and-snapshot) |
| 用法示例 | [用法](#-usage) |
| 贡献指南 | [贡献](#-contribution) |
| 支持这个项目 | [Support](#-support) |

---

[![Pipeline](https://img.shields.io/badge/Pipeline-.auto--readme--work-0f172a?style=flat-square&logo=githubactions&logoColor=white)](./.auto-readme-work)
[![Locales](https://img.shields.io/badge/Locales-10%20files-22c55e?style=flat-square&logo=googletranslate&logoColor=white)](./i18n)
[![Scope](https://img.shields.io/badge/Scope-Documentation-0ea5e9?style=flat-square&logo=mdbook&logoColor=white)](#documentation-inputs-and-generated-artifacts)

## 📌 概览

| 🎯 关注点 | 🧩 当前价值 |
| --- | --- |
| 仓库用途 | 用于多语言 README 同步的文档脚手架 |
| 核心约束 | 增量式编辑保留实质性历史 |
| 当前状态 | 仓库快照中未检测到运行时应用或服务 |

| ✅ 快照 | 📌 当前状态 |
| --- | --- |
| 仓库阶段 | 由 `.auto-readme-work/` 驱动的启动脚手架 |
| 本地化版本 | 10 个已翻译 README 变体 |
| 已验证运行时 | 未检测到可运行应用或服务 |

## 📌 概述

AgInTi 是一个**文档启动型仓库**。

仓库聚焦于 README-first 文档策略、本地化脚手架，以及用于生成一致多语言文档的迭代式工作流产物。

- ✅ 尚未检测到顶层运行时源码树。
- ✅ `i18n/` 包含 10 个翻译后的 README 变体。
- ✅ `.auto-readme-work/` 保存迭代式文档更新的流水线产物。
- ✅ 通过增量更新保留既有实质性内容。

## ✅ 范围与快照

| 项目 | 当前状态 |
|---|---|
| 🧩 源码 | 未检测 |
| 🧪 测试/CI | 未检测 |
| 📘 文档工作流 | 由 `.auto-readme-work/` 驱动 |
| 🌐 本地化文档 | 维护 10 种语言 |
| 🔒 许可证文件 | 本快照中不存在 |

## ✨ 特性

- README-first 的文档仓库策略。
- 语言感知工作流，并为根文档与本地化页面提供规范链接。
- 在定义位置保留去重后的横幅与支持区块。
- 增量更新可保留已有核心章节。
- 为文档贡献者提供可直接使用的检查与校验片段。

## 🗂️ 项目结构

```text
AgInTi/
├── README.md
├── README.md.auto-readme-support
├── README.md.auto-readme-support.filtered
├── i18n/
│   ├── README.ar.md
│   ├── README.de.md
│   ├── README.es.md
│   ├── README.fr.md
│   ├── README.ja.md
│   ├── README.ko.md
│   ├── README.ru.md
│   ├── README.vi.md
│   ├── README.zh-Hans.md
│   └── README.zh-Hant.md
└── .auto-readme-work/
    ├── 20260228_184104/
    ├── 20260301_064213/
    ├── 20260301_064740/
    ├── 20260301_065835/
    └── 20260301_070633/
```

## 🧱 架构与工作流模型

在当前阶段，“架构”指的是仓库的文档流水线：

1. 每次运行会在 `.auto-readme-work/<run-id>/pipeline-context.md` 中生成上下文与约束。
2. 在 `language-nav-root.md` / `language-nav-i18n.md` 中生成语言切换模板。
3. 对 README 进行增量式编辑，以保留实质历史。
4. 本地化文件基于同一结构化模板进行同步。

## 📚 文档输入与生成产物

| 文件 | 用途 |
|---|---|
| `.auto-readme-work/20260301_070633/pipeline-context.md` | 本次更新的来源约束与说明。 |
| `.auto-readme-work/20260301_070633/translation-plan.txt` | 多语言同步的语言映射。 |
| `.auto-readme-work/20260301_070633/language-nav-root.md` | `README.md` 的标准语言导航行。 |
| `.auto-readme-work/20260301_070633/language-nav-i18n.md` | 本地化 README 的标准语言导航行。 |
| `.auto-readme-work/20260301_070633/repo-structure-analysis.md` | 本轮生成所使用的仓库快照。 |
| `README.md.auto-readme-support*` | 先前 bootstrap 轮次中使用的辅助支持清单。 |

## 🧭 仓库工作流目标

该仓库按设计保持轻量。长期目标是在不回退技术上下文、链接和结构的前提下，让根 README 与翻译版本持续同步。

## 🧰 前置条件

- `git`（用于仓库访问）。
- 一个 POSIX shell（示例使用 `bash`）。
- 支持 Markdown 的编辑器。

### 运行时假设

当前仓库快照尚未检测到可运行的产品清单，因此尚未定义构建/运行时要求。

## 📥 安装

目前尚无二进制安装或构建流程。

```bash
# 克隆仓库
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ 用法

当前用法聚焦于文档维护与多语言一致性。

### 常用命令

```bash
ls -la
ls -la .auto-readme-work/20260301_070633
ls -la i18n
```

### 典型 README 同步工作流

1. 查看 `.auto-readme-work/20260301_070633/pipeline-context.md` 中的运行上下文。
2. 检查 `.auto-readme-work/20260301_070633/language-nav-*.md` 中的语言切换模板。
3. 以增量方式编辑 `README.md`；不要移除现有实质性章节。
4. 保持横幅与支持区块各唯一一次且位于要求位置。
5. 视需要将 `i18n/README.*.md` 对齐到同一结构。

## ⚙️ 配置

当前尚无应用配置。仓库级文档行为由 `.auto-readme-work/` 中的工作流产物和 `i18n/` 中的本地化文件定义。

- `pipeline-context.md`（约束与目标）
- `translation-plan.txt`（语言范围与映射）
- `language-nav-root.md` 和 `language-nav-i18n.md`（语言导航一致性）
- `README.md.auto-readme-support*`（脚手架辅助文件）

## 🧪 示例

### 示例 1：检查语言选择器行

```bash
cat .auto-readme-work/20260301_070633/language-nav-root.md
cat .auto-readme-work/20260301_070633/language-nav-i18n.md
```

### 示例 2：校验支持的语言与翻译文件

```bash
cat .auto-readme-work/20260301_070633/translation-plan.txt
```

### 示例 3：确认脚手架状态

```bash
find . -maxdepth 2 \
  \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

## 🛠️ 开发说明

- 使用增量式编辑来保留既有技术上下文。
- 未检测到具体清单文件前，不要添加运行/构建步骤。
- 确保横幅和支持区块仅出现一次。
- 当仓库行为未知时，请记录假设。
- 命令示例要与现有文件和目录对应。

## 🩺 故障排查

### 我只看到 markdown 文件

在当前 bootstrap 阶段这是预期现象。

### 语言切换器看起来不一致

将每个 `README.*.md` 与根语言切换行以及 `.auto-readme-work/20260301_070633/` 中最新的 pipeline context 进行对比。

### 我的分支落后了

```bash
git fetch origin
git pull --ff-only
```

### 我想补充代码说明

仅在加入具体清单（例如 `package.json`、`pyproject.toml`、`Cargo.toml` 等）并确认仓库中存在这些资产后，才添加构建/运行命令。

## 🗺️ 路线图

- 引入具体应用/运行时组件。
- 在代码与工具链就绪后补充安装、运行和部署说明。
- 增加 CI 检查，保证 Markdown 质量与语言一致性。
- 通过显式版本化的流水线保证翻译流程可复现。
- 为文档和未来代码贡献者补充贡献指南。

## 🤝 贡献

欢迎贡献。

1. 创建 issue 说明变更。
2. 新建专用分支。
3. 保持改动精简且增量。
4. 保留现有实质性章节。
5. 提交 pull request 并附上简明的验证说明。

### 建议流程

```bash
git checkout -b docs/your-update
# 编辑 README.md 和/或 i18n/
git add README.md
git commit -m "docs: refine README draft"
git push -u origin docs/your-update
```

## 📄 许可证

本仓库快照尚未包含许可证文本。


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
