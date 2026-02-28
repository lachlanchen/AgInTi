[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# AgInTi

[![Status](https://img.shields.io/badge/status-initializing-orange)](#aginti)
[![Docs](https://img.shields.io/badge/docs-readme_draft-blue)](#aginti)
[![Repository Stage](https://img.shields.io/badge/stage-bootstrap-yellow)](#aginti)
[![i18n](https://img.shields.io/badge/i18n-planned-0ea5e9)](#aginti)
[![License](https://img.shields.io/badge/license-TBD-lightgrey)](#aginti)

## 📌 概览

AgInTi 目前处于初始化/脚手架阶段。在本 README 草稿生成时，仓库主要包含：

- Git 元数据（`.git/`）
- 已为多语言 README 文件准备好的 `i18n/` 目录
- `.auto-readme-work/` 工作区，其中包含 README 生成流水线上下文和语言规划产物

在当前工作树中，尚未检测到应用源码、包清单、运行时入口点或 CI 工作流。

### 仓库快照

| 项目 | 当前状态 |
| --- | --- |
| 源代码 | 尚未检测到 |
| 运行时清单 | 尚未检测到 |
| CI 工作流 | 尚未检测到 |
| 文档工作区 | `.auto-readme-work/20260228_184104/` |
| i18n 目录 | 已存在（`i18n/`） |

## 🚦 项目状态

这是该仓库的**首个完整 README 草稿**。

- 已观测到的仓库状态：**顶层源码树尚不存在**
- 现有规范 README 基线：**本次运行期间在本地工作区未发现**
- 本文档采用的方法：保留所有已发现且与仓库实际一致的细节，并对未知项进行明确标注，而不是删除或臆造内容

如果远端分支/历史中存在规范的历史 README，应在此草稿基础上与其内容进行增量合并，而不是替换其中的实质性章节。

## ✨ 功能（当前）

当前仓库能力以文档/流水线为主：

- 位于 `.auto-readme-work/` 下的 README 生成流水线工作区
- 多语言 README 目标规划（包含英文在内共 11 种语言）
- 根目录与 `i18n/` 的语言导航模板

计划中的产品/运行时功能目前尚不明确。

## 🗂️ 项目结构

```text
AgInTi/
├── .auto-readme-work/
│   └── 20260228_184104/
│       ├── pipeline-context.md
│       ├── repo-structure-analysis.md
│       ├── language-nav-root.md
│       ├── language-nav-i18n.md
│       └── translation-plan.txt
├── .git/
└── i18n/
```

### 关键文档输入

| 文件 | 用途 |
| --- | --- |
| `.auto-readme-work/20260228_184104/pipeline-context.md` | 定义本次运行的 README 约束与生成流程上下文。 |
| `.auto-readme-work/20260228_184104/repo-structure-analysis.md` | 汇总检测到的仓库结构与已知缺口。 |
| `.auto-readme-work/20260228_184104/language-nav-root.md` | 根目录 `README.md` 的规范语言切换行。 |
| `.auto-readme-work/20260228_184104/language-nav-i18n.md` | `i18n/` 下翻译文件的规范语言切换行。 |
| `.auto-readme-work/20260228_184104/translation-plan.txt` | 翻译的语言环境到文件映射。 |

## 🧰 前置条件

按当前仓库内容使用时，不需要任何运行时前置依赖。

若进行文档工作流和仓库操作，你可能需要：

- `git`
- 与 POSIX 兼容的 shell（示例使用 `bash`）
- 文本编辑器

## 📥 安装

由于目前尚无应用/包清单，因此也没有安装/构建步骤。

克隆仓库：

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ 使用

当前的实际使用方式是进行仓库检查以及 README/i18n 文档工作。

示例：

```bash
# Show top-level files
ls -la

# Inspect auto-generated README context files
ls -la .auto-readme-work/20260228_184104

# Inspect i18n directory
ls -la i18n
```

## ⚙️ 配置

目前尚未检测到应用配置文件。

已知的仓库配置信号：

- Git 远程已配置为 `origin git@github.com:lachlanchen/AgInTi.git`
- 多语言 README 导航与目标语言映射位于 `.auto-readme-work/20260228_184104/`

## 🧪 示例

### 示例 1：验证 README 语言导航一致性

```bash
# Compare language switcher templates used by the pipeline
cat .auto-readme-work/20260228_184104/language-nav-root.md
cat .auto-readme-work/20260228_184104/language-nav-i18n.md
```

### 示例 2：确认翻译目标集合

```bash
cat .auto-readme-work/20260228_184104/translation-plan.txt
```

### 示例 3：验证仓库尚无运行时清单

```bash
# Typical manifest check (expected: none in current state)
find . -maxdepth 2 \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml \)
```

## 🛠️ 开发说明

- 仓库目前看起来处于早期引导阶段。
- README 优先的搭建工作正在进行，多语言结构已准备完毕。
- 在结构分析期间未检测到本地提交历史（分析上下文记录为 `No commits yet on main`）。
- 添加源代码时，请同步更新本 README，补充明确的设置、使用和配置说明。

## 🩺 故障排查

### 旧版本/本地副本缺少 `README.md`

如果你的本地克隆此前不包含 `README.md`，请从最新分支状态同步：

```bash
git fetch origin
git pull --ff-only
```

### 存在 `i18n/` 但缺少翻译文件

这在早期草稿阶段属于预期情况。翻译目标定义于：

- `.auto-readme-work/20260228_184104/translation-plan.txt`

### 项目运行时技术栈不明确

如果你没有看到 `src/`、清单文件或入口点，这与当前观测状态一致。待引入实现文件后再补充技术栈细节。

## 🗺️ 路线图

近期文档与项目引导目标：

- 完善英文基线 README，补充真实的项目目标与架构
- 按翻译计划在 `i18n/` 下新增各语言 README
- 引入应用源码目录结构和运行时清单文件
- 增加可复现的安装与运行命令
- 代码库成型后补充 CI 检查（lint/test/docs validation）

## 🤝 贡献

欢迎贡献。鉴于仓库仍处于早期搭建阶段：

1. 先提交 issue 描述拟议变更（文档、结构或初始代码布局）。
2. 创建功能分支。
3. 保持改动聚焦且文档化。
4. 当行为或结构变化时，同步更新 README/i18n 文档。
5. 提交 pull request，并提供清晰上下文与验证步骤。

建议的本地工作流：

```bash
git checkout -b feat/your-change
# make edits

git add .
git commit -m "Describe your change"
git push -u origin feat/your-change
```

## 💬 支持

当前仓库文件中尚未声明专门的支持、赞助或捐赠渠道。

若后续新增支持链接，请在此处补充，并在 README 后续修订中持续保留。

## 📄 许可证

当前仓库内容尚未声明许可证信息。

- 状态：`TBD`
- 建议下一步：添加 `LICENSE` 文件，并在本节写明准确的 SPDX 标识符。

## 🧾 假设与保留说明

- 本草稿基于 `/home/lachlan/ProjectsLFS/AgInTi` 当前存在的仓库文件生成。
- 生成时本地不可用既有规范 README，因此无法从其中导入实质内容。
- 根据保留策略，未知或缺失细节均会被明确标注，而非猜测或省略。
