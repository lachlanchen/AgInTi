[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Status](https://img.shields.io/badge/status-initializing-orange)](#aginti)
[![Docs](https://img.shields.io/badge/docs-readme_draft-blue)](#aginti)
[![Repository%20Stage](https://img.shields.io/badge/stage-bootstrap-yellow)](#aginti)
[![i18n](https://img.shields.io/badge/i18n-planned-0ea5e9)](#aginti)
[![License](https://img.shields.io/badge/license-TBD-lightgrey)](#aginti)

*以文档为先的启动仓库 • README 优先工作流 • 持续推进多语言规划。*

| 关注点 | 当前状态 |
|---|---|
| 核心成熟度 | 启动脚手架（`README`-first） |
| 本地化 | `i18n/` 中维护 10 种语言 |
| 流水线来源 | `.auto-readme-work/20260301_064213/` |

---

## 📌 概览

AgInTi 目前是一个以文档脚手架为主的仓库，采用 README 优先工作流和多语言文档规划。

在本草稿编写时，仓库内容聚焦于文档协作和语言准备，尚未转向可运行的产品代码：

- ✅ 尚未检测到顶层源码树。
- ✅ `i18n/` 已包含多个翻译版 README。
- ✅ `.auto-readme-work/20260301_064213/` 保存了本次处理的活动流水线上下文。
- ✅ `.auto-readme-work/20260228_184104/` 作为历史记录保留。

### 仓库快照

| 条目 | 当前状态 |
|---|---|
| 🧩 源代码 | 尚未检测到 |
| ⚙️ 运行时清单 | 尚未检测到 |
| 🧪 CI 工作流 | 尚未检测到 |
| 🧭 文档工作区 | `.auto-readme-work/20260301_064213/` |
| 🌐 文档翻译 | `i18n/` 中有 10 种语言 |

---

## 🚦 项目状态

本 README 是一个增量更新、与仓库实际一致的第一份完整英文草稿。

- 仓库状态仍保持启动/文档导向。
- 保留了现有实质性章节，并在必要处扩展，而非替换。
- 未知内容均明确标注，避免推测性表述。

如果上游存在其他分支或历史中的规范 README，后续更新应进行增量合并。

---

## ✨ 特性

- 文档优先的仓库布局
- `.auto-readme-work/` 下集中化的多语言 README 流水线
- 明确的语言切换模板与翻译映射文件
- 用于仓库检查与校验的实际命令片段
- 通过去重控制，严格追踪 README 的更新流程（支持/横幅区块）

---

## 🗂️ 项目结构

```text
AgInTi/
├── .auto-readme-work/
│   ├── 20260301_064213/
│   │   ├── language-nav-root.md
│   │   ├── language-nav-i18n.md
│   │   ├── pipeline-context.md
│   │   ├── repo-structure-analysis.md
│   │   └── translation-plan.txt
│   └── 20260228_184104/
│       ├── language-nav-root.md
│       ├── language-nav-i18n.md
│       ├── pipeline-context.md
│       ├── repo-structure-analysis.md
│       ├── translated-files.txt
│       └── translation-plan.txt
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
└── README.md
```

### 关键文档输入

| 文件 | 用途 |
|---|---|
| `.auto-readme-work/20260301_064213/pipeline-context.md` | 记录本次运行的生成约束与提示上下文。 |
| `.auto-readme-work/20260301_064213/repo-structure-analysis.md` | 检测到的仓库结构与功能缺口快照。 |
| `.auto-readme-work/20260301_064213/translation-plan.txt` | 语言到文件的映射计划。 |
| `.auto-readme-work/20260301_064213/language-nav-root.md` | `README.md` 的标准语言切换行。 |
| `.auto-readme-work/20260301_064213/language-nav-i18n.md` | `i18n/` 文件的标准语言切换行。 |

---

## 🧰 先决条件

当前仓库状态不需要运行时依赖。

用于文档使用与维护，你需要：

- `git`
- 一个 POSIX shell（示例使用 `bash`）
- 用于 Markdown 更新的文本编辑器

---

## 📥 安装

目前尚无安装/构建流程。

要在本地查看仓库：

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ 使用

当前用途主要是文档维护、审核与本地化同步。

### 常见工作流

```bash
ls -la
ls -la .auto-readme-work/20260301_064213
ls -la i18n
```

### 典型 README 工作流

1. 阅读 `.auto-readme-work/20260301_064213/` 中当前上下文文件。
2. 检查源 README 与已翻译版本。
3. 采用增量编辑，避免移除现有实质性内容。
4. 在各语言版本中保持语言切换与支持区块一致。

---

## ⚙️ 配置

当前尚未发现应用级配置文件。

文档层面的配置当前由以下内容表达：

- `.auto-readme-work/20260301_064213/translation-plan.txt`（目标语言清单）
- `.auto-readme-work/20260301_064213/language-nav-root.md` 与 `.../language-nav-i18n.md` 中的语言切换模板
- `.auto-readme-work/20260301_064213/repo-structure-analysis.md` 的仓库结构上下文

---

## 🧪 示例

### 示例 1：验证语言切换行

```bash
cat .auto-readme-work/20260301_064213/language-nav-root.md
cat .auto-readme-work/20260301_064213/language-nav-i18n.md
```

### 示例 2：确认翻译范围

```bash
cat .auto-readme-work/20260301_064213/translation-plan.txt
```

### 示例 3：确认脚手架状态（预期结果：无清单）

```bash
find . -maxdepth 2 \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

---

## 🛠️ 开发说明

- 将此文件作为英文文档的规范来源。
- 更新时保留实质性章节（增量编辑策略）。
- 仅在对应代码、清单与工具链就绪后补充运行指令。
- 保持支持与 banner 区块去重（每种仅保留一次）。
- 在功能落地后尽快更新路线图与故障排查内容。

---

## 🩺 故障排查

### 我只看到了文档文件

在当前启动状态下这是预期情况；未检测到源码或运行时清单。

### 本地化文档不一致

请使用最新翻译计划并重新运行 README 同步流程以统一结构和链接。

### 本地分支看起来过时

```bash
git fetch origin
git pull --ff-only
```

---

## 🗺️ 路线图

- 在代码引入后增加具体产品/应用层。
- 基于真实清单补充安装、构建与运行说明。
- 增加 CI 工作流与文档检查。
- 完善对代码和翻译的贡献规范。
- 保持所有语言版本的 README 同步更新。

---

## 🤝 贡献

欢迎贡献。

1. 创建 issue 说明上下文与范围。
2. 新建专用分支。
3. 保持改动聚焦且增量。
4. 保留已有技术细节和章节上下文。
5. 提交 PR，并附上清晰的验证说明。

### 建议流程

```bash
git checkout -b feat/your-change
# edit README + relevant files
git add README.md

git commit -m "docs: update README"

git push -u origin feat/your-change
```

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 📄 许可

尚未提供 `LICENSE` 文件。

- 状态：`TBD`
- 建议下一步：补充许可证文件，并在此处写明准确的 SPDX 标识。

## 🧾 假设与保留说明

- 本次运行在 `/home/lachlan/ProjectsLFS/AgInTi` 上评估了仓库内容。
- 运行时目标与架构尚未在已提交文件中体现；该草稿有意聚焦于当前可验证事实。
- 已保留并扩展来自先前草稿的实质性章节。
- 已在本次请求范围内仅插入一次 banner 与支持区块。
