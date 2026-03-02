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

以文件為先的儲存庫框架，用於維護完整的英文 README 與同步的多語文件，並由三項運作原則引導：**sear creation tools**、**self-healing tools**、**chain of prompt tools**。

## 🧭 快速導覽

| 類型 | 目的地 |
| --- | --- |
| 專案摘要 | [Overview](#overview) |
| 核心能力 | [Features](#features) |
| 流水線設計 | [Architecture](#architecture) |
| 理念基線 | [Philosophy at a glance](#philosophy-at-a-glance) |
| 貢獻者流程 | [Development Notes](#development-notes) |
| 未來方向 | [Roadmap](#roadmap) |
| 支持此專案 | [Support](#-support) |

---

## 📌 範圍與快照

| 項目 | 目前狀態 |
| --- | --- |
| 儲存庫階段 | 文件啟動框架 |
| Runtime 程式碼 | 在目前快照中未偵測到 |
| 測試/CI 流水線 | 在目前快照中未偵測到 |
| 本地化文件 | `i18n/` 下有 10 個 locale 檔案 |
| 流水線產物 | `.auto-readme-work/` 下有時間戳執行紀錄 |
| 授權檔案 | 尚未以獨立檔案存在（README badge: TBD） |
| 理念基線 | Sear creation + self-healing + chain of prompt tools |

## 🌍 Overview

AgInTi 目前是 README 生命週期與在地化流水線，而非執行階段應用程式。根目錄 `README.md` 是正典來源，`i18n/` 中的在地化版本會依此正典結構同步。

專案理念是明確且可操作的，不是裝飾性口號。每次 README 更新都應同時滿足以下三項原則：

1. **Sear creation tools**：有意識地採用銳利的創作工作流，從受限的儲存庫證據中產出高訊號、可落地的文件。
2. **Self-healing tools**：以修復為導向的機制，用於修正漂移、移除重複並恢復結構一致性。
3. **Chain of prompt tools**：分階段且可追溯的提示流程，確保在流水線執行中保留從上下文到輸出的脈絡血緣。

此儲存庫透過增量更新保留實質歷史內容，同時維持連結、命令與支援中繼資料。

### Philosophy at a glance

| Principle | Intent | Operational outcome |
| --- | --- | --- |
| **Sear creation tools** | Produce high-signal documentation from constrained evidence. | Sections stay practical, specific, and repository-grounded. |
| **Self-healing tools** | Repair drift, duplication, and stale structure. | Canonical and localized READMEs remain aligned and clean. |
| **Chain of prompt tools** | Keep generation stages explicit and traceable. | Pipeline artifacts preserve reproducible context and handoffs. |

## ✨ Features

- 以 README 為核心的文件策略，並以根文件作為正典。
- 10 個 i18n README 版本的多語同步。
- 透過 `.auto-readme-work/<run-id>/` 產物進行流水線化撰寫。
- 「單一 banner + 單一 support panel」不變式，避免重複視覺區塊。
- 以增量更新紀律保留有意義的技術歷史。

### Principle-to-feature mapping

| Core principle | How it appears in current features |
| --- | --- |
| **Sear creation tools** | Precise README drafting from repo-grounded evidence and stable section scaffolds. |
| **Self-healing tools** | Deduplication checks for repeated banner/support blocks, stale references, and structure drift. |
| **Chain of prompt tools** | Run-specific artifact chain (`pipeline-context`, nav templates, translation plan) for reproducible output. |

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

在目前階段，architecture 指的是文件流水線架構，而不是應用程式執行架構。

### Pipeline flow

1. 在 `.auto-readme-work/<run-id>/pipeline-context.md` 記錄每次執行的上下文。
2. 產生語言導覽範本（`language-nav-root.md` 與 `language-nav-i18n.md`）。
3. 以增量方式更新正典內容 `README.md`。
4. 讓 `i18n/` 的在地化 README 檔案與正典結構對齊。
5. 透過結構品質檢查來確保去重、連結一致與技術細節保留。

### Core principles in architecture

- **Sear creation tools**：套用於內容建構階段，使章節保持具體、完整且符合儲存庫現況。
- **Self-healing tools**：套用於驗證階段，移除重複區塊、修復過期執行參照並恢復結構一致。
- **Chain of prompt tools**：套用於整體產物鏈，讓每個生成階段都明確且可稽核。

### Principle checkpoints by pipeline stage

| Stage | Sear creation tools | Self-healing tools | Chain of prompt tools |
| --- | --- | --- | --- |
| Context capture | Define sharp generation constraints. | Flag missing/invalid inputs early. | Preserve source prompt and run metadata. |
| Canonical drafting | Build complete README sections from repo evidence. | Prevent regressions and accidental content loss. | Keep stage outputs linked to prior artifacts. |
| i18n alignment | Maintain structure and technical parity across locales. | Correct drift between root and i18n files. | Carry canonical intent into each localized variant. |
| Final verification | Enforce readability and detail preservation. | Remove duplicate banner/support blocks and stale references. | Leave an auditable artifact trail for the run. |

## 🧾 Documentation Inputs and Generated Artifacts

| File | Purpose |
| --- | --- |
| `.auto-readme-work/20260302_124338/pipeline-context.md` | Source constraints and goals for this generation pass. |
| `.auto-readme-work/20260302_124338/repo-structure-analysis.md` | Repository scan summary and inferred technical state. |
| `.auto-readme-work/20260302_124338/language-nav-root.md` | Canonical language options line for root `README.md`. |
| `.auto-readme-work/20260302_124338/language-nav-i18n.md` | Canonical language options line for i18n README files. |
| `.auto-readme-work/20260302_124338/translation-plan.txt` | Locale mapping and i18n target file plan. |
| `.auto-readme-work/<older-run-id>/...` | Historical run context for prior README pipeline passes. |

## 🔧 Prerequisites

- `git`
- POSIX shell (範例使用 `bash`)
- 支援 Markdown 的編輯器

### Assumptions

- 在目前儲存庫快照中，尚未發現可執行服務或應用程式 manifest。
- 因此安裝/建置/啟動說明以文件工作流程為導向。

## 📥 Installation

目前尚未定義二進位套件或 runtime 建置步驟。

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Usage

目前用法是維護文件與同步多語內容。

### Common inspection commands

```bash
ls -la
ls -la .auto-readme-work/20260302_124338
ls -la i18n
```

### Canonical README synchronization workflow

1. 讀取 `.auto-readme-work/20260302_124338/pipeline-context.md`。
2. 檢查來自 `language-nav-root.md` 與 `language-nav-i18n.md` 的語言選單範本。
3. 以 `README.md` 作為單一真實來源進行增量更新。
4. 讓 `i18n/README.*.md` 與相同結構與關鍵技術細節對齊。
5. 確認 banner 恰好一個、support panel 也恰好一個。

## ⚙️ Configuration

目前尚無 runtime 設定。文件行為由儲存庫產物驅動。

- `pipeline-context.md`：執行目標與限制。
- `repo-structure-analysis.md`：快照證據與缺口。
- `language-nav-root.md` 與 `language-nav-i18n.md`：導覽一致性。
- `translation-plan.txt`：語系目標與對應。

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

- 保留正典 README 歷史中的實質段落與連結。
- 優先採用增量編輯，避免破壞式重寫。
- 僅保留一個 banner 與一個 support 區塊。
- 維持 root 與 i18n README 結構同步。
- 只要 runtime 或基礎設施細節未知，就要清楚註明假設。
- 將三元理念作為主動護欄：
  - **Sear creation tools** 用於高訊號草擬。
  - **Self-healing tools** 用於一致性修復。
  - **Chain of prompt tools** 用於在流水線階段之間可重現地交接。

## 🚑 Troubleshooting

### I only see Markdown files and pipeline artifacts

在目前的啟動階段，這是預期結果。

### Language selector lines differ between files

請使用以下正典範本：

- `.auto-readme-work/20260302_124338/language-nav-root.md`
- `.auto-readme-work/20260302_124338/language-nav-i18n.md`

### My branch is behind

```bash
git fetch origin
git pull --ff-only
```

### I want to add runtime instructions

僅在引入明確 manifest（例如：`package.json`、`pyproject.toml`、`go.mod`、`Cargo.toml`）並確認本儲存庫路徑後，再新增 build/run 說明。

## 🗺️ Roadmap

1. 強化 **sear creation tools**：導入標準化 README 草擬範本、章節品質閘門，以及更清楚的 evidence-to-output 檢查。
2. 擴展 **self-healing tools**：加入自動檢查以偵測重複區塊、locale 漂移、失效內部錨點與過期執行參照。
3. 正式化跨執行階段的 **chain of prompt tools**，確保上下文、生成、翻譯與驗證軌跡可重現。
4. 在導入儲存庫腳本後，提供單一命令的文件維護流程。
5. 新增 CI 檢查，涵蓋 Markdown 品質、連結完整性與 i18n 結構一致。
6. 在加入來源 manifest 與 entrypoint 後，導入具體 runtime 元件。
7. 公布穩定授權決策，並新增獨立授權檔案。

### Roadmap by principle focus

| Focus area | Near-term target |
| --- | --- |
| **Sear creation tools** | Improve drafting templates and evidence-backed section prompts. |
| **Self-healing tools** | Automate duplicate detection, stale anchor checks, and locale drift repair. |
| **Chain of prompt tools** | Standardize run-stage artifact contracts for reproducible multilingual outputs. |

## 🤝 Contribution

歡迎貢獻。

1. 開啟 issue 說明你打算做的變更。
2. 建立聚焦的分支。
3. 保持文件編輯為增量且與儲存庫現況一致。
4. 保留重要連結、命令與實質歷史脈絡。
5. 以精簡的驗證說明提交 pull request。

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

TBD。已規劃新增獨立授權檔案，但在目前快照中尚未提供。
