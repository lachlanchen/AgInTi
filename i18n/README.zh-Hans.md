[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Repository](https://img.shields.io/badge/Repository-AgInTi-0f172a?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lachlanchen/AgInTi)
[![Docs](https://img.shields.io/badge/Docs-README%20Bootstrap-0ea5e9?style=for-the-badge&logo=mdbook&logoColor=white)](#aginti)
[![Localization](https://img.shields.io/badge/i18n-10%20locales-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)](#project-structure)
[![Status](https://img.shields.io/badge/Stage-Documentation%20Pipeline-f59e0b?style=for-the-badge&logo=githubactions&logoColor=white)](#scope-and-snapshot)
[![License](https://img.shields.io/badge/License-TBD-94a3b8?style=for-the-badge&logo=readme&logoColor=white)](#license)
[![Principle-Sear%20Creation-ef4444?style=flat-square&logo=firefox&logoColor=white)](#overview)
[![Principle-Self--Healing-10b981?style=flat-square&logo=wrench&logoColor=white)](#features)
[![Principle-Chain%20of%20Prompt%20Tools-3b82f6?style=flat-square&logo=chainlink&logoColor=white)](#architecture)

这是一个以文档为先的仓库脚手架，用于维护完整的英文 README 与同步的多语言文档，并由三项运行原则驱动：**sear creation tools**、**self-healing tools**、以及 **chain of prompt tools**。

## 🧭 Quick Navigation

| Type | Destination |
| --- | --- |
| 项目摘要 | [Overview](#overview) |
| 核心能力 | [Features](#features) |
| 流水线设计 | [Architecture](#architecture) |
| 理念基线 | [Philosophy at a glance](#philosophy-at-a-glance) |
| 贡献者工作流 | [Development Notes](#development-notes) |
| 未来方向 | [Roadmap](#roadmap) |
| 支持本项目 | [Support](#-support) |

---

## 📌 Scope and Snapshot

| Item | Current state |
| --- | --- |
| 仓库阶段 | 文档引导脚手架（Documentation bootstrap scaffold） |
| 运行时代码 | 在当前快照中未检测到 |
| 测试/CI 流水线 | 在当前快照中未检测到 |
| 本地化文档 | `i18n/` 下 10 个 locale 文件 |
| 流水线产物 | `.auto-readme-work/` 下按时间戳记录的运行目录 |
| License 文件 | 尚无独立文件（README 徽章显示：TBD） |
| 理念基线 | Sear creation + self-healing + chain of prompt tools |

## 🌍 Overview

AgInTi 当前是 README 生命周期与本地化流水线，而不是运行时应用。根目录 `README.md` 是规范来源，`i18n/` 下的本地化版本由该规范结构同步生成。

本项目理念是显式且可执行的，不是装饰性口号。每一次 README 更新都应满足以下三项原则：

1. **Sear creation tools**：通过有意保持“锋利”的创作流程，在受限仓库证据基础上产出高信号、可落地的文档。
2. **Self-healing tools**：通过修复机制纠正文档漂移、消除重复内容并恢复结构一致性。
3. **Chain of prompt tools**：通过分阶段、可追溯的提示链路，在流水线运行中保留从上下文到输出的谱系关系。

该仓库通过增量更新保留有价值的历史内容，同时维持链接、命令与支持元数据的完整性。

### Philosophy at a glance

| Principle | Intent | Operational outcome |
| --- | --- | --- |
| **Sear creation tools** | 在受限证据中产出高信号文档。 | 各章节保持实用、具体、且锚定仓库事实。 |
| **Self-healing tools** | 修复漂移、重复与结构陈旧。 | 规范 README 与多语言 README 持续对齐、整洁。 |
| **Chain of prompt tools** | 让生成阶段显式且可追溯。 | 流水线产物保留可复现的上下文与交接链路。 |

## ✨ Features

- README-first 文档策略，以根文档作为规范来源。
- 对 10 个 i18n README 变体进行多语言同步。
- 通过 `.auto-readme-work/<run-id>/` 产物驱动文档编写。
- 通过“单横幅 + 单支持面板”约束，防止可视块重复。
- 通过增量更新纪律，保留有意义的技术历史。

### Principle-to-feature mapping

| Core principle | How it appears in current features |
| --- | --- |
| **Sear creation tools** | 基于仓库证据的精确 README 起草，以及稳定章节脚手架。 |
| **Self-healing tools** | 针对重复 banner/support 区块、过时引用与结构漂移的去重校验。 |
| **Chain of prompt tools** | 以运行为单位的产物链（`pipeline-context`、导航模板、翻译计划）保证输出可复现。 |

## 🗂️ Project Structure

```text
AgInTi/
├── README.md
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
    ├── 20260301_070633/
    ├── 20260302_120620/
    └── 20260302_124338/
```

## 🏗️ Architecture

在当前阶段，这里的“架构”指文档流水线架构，而不是应用运行时架构。

### Pipeline flow

1. 在 `.auto-readme-work/<run-id>/pipeline-context.md` 中记录运行上下文。
2. 生成语言导航模板（`language-nav-root.md` 与 `language-nav-i18n.md`）。
3. 对 `README.md` 进行增量更新，维持其作为事实来源的角色。
4. 将 `i18n/` 下本地化 README 对齐到规范结构。
5. 通过结构质量检查强制执行去重、链接一致性与技术细节保留。

### Core principles in architecture

- **Sear creation tools**：用于内容构建阶段，确保章节具体、完整且与仓库事实一致。
- **Self-healing tools**：用于校验阶段，移除重复区块、修复过时运行引用并恢复结构一致性。
- **Chain of prompt tools**：贯穿各类产物，确保每个生成阶段都显式、可审计。

### Principle checkpoints by pipeline stage

| Stage | Sear creation tools | Self-healing tools | Chain of prompt tools |
| --- | --- | --- | --- |
| Context capture | 定义清晰、严格的生成约束。 | 提前标记缺失/无效输入。 | 保留源提示与运行元数据。 |
| Canonical drafting | 基于仓库证据构建完整 README 章节。 | 防止回归与内容意外丢失。 | 让阶段输出可追溯到先前产物。 |
| i18n alignment | 维持多语言之间的结构与技术等价性。 | 修复根文档与 i18n 文件之间的漂移。 | 将规范意图传递到每个本地化版本。 |
| Final verification | 强制可读性与技术细节保真。 | 移除重复 banner/support 区块与过时引用。 | 为本次运行留下可审计产物链。 |

## 🧾 Documentation Inputs and Generated Artifacts

| File | Purpose |
| --- | --- |
| `.auto-readme-work/20260302_124338/pipeline-context.md` | 本轮生成的源约束与目标。 |
| `.auto-readme-work/20260302_124338/repo-structure-analysis.md` | 仓库扫描摘要与推断技术状态。 |
| `.auto-readme-work/20260302_124338/language-nav-root.md` | 根 `README.md` 的规范语言导航行。 |
| `.auto-readme-work/20260302_124338/language-nav-i18n.md` | i18n README 的规范语言导航行。 |
| `.auto-readme-work/20260302_124338/translation-plan.txt` | locale 映射与 i18n 目标文件计划。 |
| `.auto-readme-work/<older-run-id>/...` | 以往 README 流水线运行的历史上下文。 |

## 🔧 Prerequisites

- `git`
- POSIX shell（示例使用 `bash`）
- 支持 Markdown 的编辑器

### Assumptions

- 在当前仓库快照中未发现可运行服务或应用清单。
- 因此，安装/构建/启动说明目前以文档工作流为导向。

## 📥 Installation

当前尚未定义二进制包或运行时构建步骤。

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Usage

当前用法聚焦于文档维护与多语言同步。

### Common inspection commands

```bash
ls -la
ls -la .auto-readme-work/20260302_124338
ls -la i18n
```

### Canonical README synchronization workflow

1. 阅读 `.auto-readme-work/20260302_124338/pipeline-context.md`。
2. 从 `language-nav-root.md` 与 `language-nav-i18n.md` 验证语言选择模板。
3. 以 `README.md` 为事实来源进行增量更新。
4. 让 `i18n/README.*.md` 与其结构和关键技术细节保持一致。
5. 确认仅存在一个 banner 与一个 support panel。

## ⚙️ Configuration

目前尚无运行时配置。文档行为由仓库产物驱动。

- `pipeline-context.md`：运行目标与约束。
- `repo-structure-analysis.md`：快照证据与缺口。
- `language-nav-root.md` 与 `language-nav-i18n.md`：导航一致性。
- `translation-plan.txt`：locale 目标与映射。

## 🧪 Examples

### Example 1: Verify language navigation templates

```bash
cat .auto-readme-work/20260302_124338/language-nav-root.md
cat .auto-readme-work/20260302_124338/language-nav-i18n.md
```

### Example 2: Check locale plan

```bash
cat .auto-readme-work/20260302_124338/translation-plan.txt
```

### Example 3: Confirm runtime-manifest absence (current snapshot)

```bash
find . -maxdepth 2 \
  \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

## 🛠️ Development Notes

- 保留规范 README 历史中的实质章节与链接。
- 优先增量编辑，而不是破坏性重写。
- 仅保留一个 banner 与一个 support 区块。
- 保持根 README 与 i18n README 结构同步。
- 当运行时或基础设施细节未知时，明确写出假设。
- 将三项理念作为主动护栏：
  - **Sear creation tools** 用于高信号起草。
  - **Self-healing tools** 用于一致性修复。
  - **Chain of prompt tools** 用于跨流水线阶段的可复现交接。

## 🚑 Troubleshooting

### I only see Markdown files and pipeline artifacts

这在当前引导阶段属于预期现象。

### Language selector lines differ between files

请使用以下规范模板：

- `.auto-readme-work/20260302_124338/language-nav-root.md`
- `.auto-readme-work/20260302_124338/language-nav-i18n.md`

### My branch is behind

```bash
git fetch origin
git pull --ff-only
```

### I want to add runtime instructions

仅在引入并确认具体清单文件后（例如：`package.json`、`pyproject.toml`、`go.mod`、`Cargo.toml`），再添加构建/运行说明。

## 🗺️ Roadmap

1. 强化 **sear creation tools**：建立标准化 README 起草模板、章节质量闸门与更清晰的证据到输出校验。
2. 扩展 **self-healing tools**：增加重复区块、locale 漂移、内部锚点失效与过时运行引用的自动检查。
3. 规范化 **chain of prompt tools**：覆盖运行阶段的上下文、生成、翻译与验证链路，确保可复现。
4. 在引入仓库脚本后，增加单命令文档维护流程。
5. 增加 Markdown 质量、链接完整性与 i18n 结构一致性的 CI 检查。
6. 在补充源码清单与入口后，引入具体运行时组件。
7. 确定稳定许可证方案并补充独立许可证文件。

### Roadmap by principle focus

| Focus area | Near-term target |
| --- | --- |
| **Sear creation tools** | 改进起草模板与基于证据的章节提示。 |
| **Self-healing tools** | 自动化重复检测、过时锚点检查与 locale 漂移修复。 |
| **Chain of prompt tools** | 标准化运行阶段产物契约，支持可复现的多语言输出。 |

## 🤝 Contribution

欢迎贡献。

1. 先创建 issue 描述计划变更。
2. 创建聚焦单一目标的分支。
3. 保持文档修改增量且与仓库事实一致。
4. 保留重要链接、命令与实质历史上下文。
5. 提交 pull request，并附上简明验证说明。

### Suggested flow

```bash
git checkout -b docs/your-update
# edit README.md and/or i18n/README.*.md
git add README.md i18n/README.*.md
git commit -m "docs: refine README content"
git push -u origin docs/your-update
```

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 📄 License

TBD。计划补充独立许可证文件，但在当前仓库快照中尚未提供。
