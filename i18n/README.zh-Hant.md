[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Repository](https://img.shields.io/badge/Repository-AgInTi-0f172a?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lachlanchen/AgInTi)
[![Docs](https://img.shields.io/badge/Docs-README%20Bootstrap-0ea5e9?style=for-the-badge&logo=mdbook&logoColor=white)](#aginti)
[![Localization](https://img.shields.io/badge/i18n-10%20locales-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)](#documentation-inputs-and-generated-artifacts)
[![Status](https://img.shields.io/badge/Stage-Documentation%20Pipeline-f59e0b?style=for-the-badge&logo=githubactions&logoColor=white)](#scope-and-snapshot)
[![License](https://img.shields.io/badge/License-TBD-94a3b8?style=for-the-badge&logo=readme&logoColor=white)](#license)

這是一個以 README 為先，維護完整英文 README 並同步多語文件的文件優先儲存庫腳手架。

## 🧭 快速導覽

| 類型 | 目標 |
|---|---|
| 儲存庫工作流程 | [範圍與快照](#-scope-and-snapshot) |
| 使用範例 | [使用方法](#-usage) |
| 貢獻指南 | [貢獻](#-contribution) |
| 支援這個專案 | [Support](#-support) |

---

[![Pipeline](https://img.shields.io/badge/Pipeline-.auto--readme--work-0f172a?style=flat-square&logo=githubactions&logoColor=white)](./.auto-readme-work)
[![Locales](https://img.shields.io/badge/Locales-10%20files-22c55e?style=flat-square&logo=googletranslate&logoColor=white)](./i18n)
[![Scope](https://img.shields.io/badge/Scope-Documentation-0ea5e9?style=flat-square&logo=mdbook&logoColor=white)](#documentation-inputs-and-generated-artifacts)

## 📌 總覽

| 🎯 焦點 | 🧩 目前價值 |
| --- | --- |
| 儲存庫用途 | 用於多語 README 同步的文件腳手架 |
| 核心不變條件 | 增量式編輯保留實質歷史 |
| 目前狀態 | 此儲存庫快照未偵測到執行時應用或服務 |

| ✅ 快照 | 📌 目前狀態 |
| --- | --- |
| 儲存庫階段 | 由 `.auto-readme-work/` 驅動的啟動式腳手架 |
| 本地化版本 | 10 個已翻譯的 README 變體 |
| 已驗證執行時 | 未偵測到可執行的應用或服務 |

## 📌 概述

AgInTi 是一個 **documentation-bootstrap**（文件啟動）儲存庫。

此儲存庫專注於 README 優先的文件編寫、在地化腳手架，以及用於產生一致多語文件的迭代式工作流程。

- ✅ 尚未偵測到頂層執行時原始碼樹。
- ✅ `i18n/` 包含 10 個已翻譯的 README 版本。
- ✅ `.auto-readme-work/` 儲存迭代文件更新的流程成果。
- ✅ 以增量更新方式保留既有實質內容。

## ✅ 範圍與快照

| 項目 | 目前狀態 |
|---|---|
| 🧩 原始碼 | 未偵測 |
| 🧪 測試/CI | 未偵測 |
| 📘 文件工作流程 | 由 `.auto-readme-work/` 驅動 |
| 🌐 在地化文件 | 維護 10 種語言 |
| 🔒 授權檔案 | 此快照中不存在 |

## ✨ 特性

- README-first 的文件策略。
- 以語言感知的流程，並提供根文件與在地化頁面的標準連結。
- 在定義位置去重 banner 與 support 區塊。
- 增量更新能保留既有核心段落。
- 為文件貢獻者提供可直接套用的檢查與驗證片段。

## 🗂️ 專案結構

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

## 🧱 架構與工作流程模型

在目前階段，「架構」指的是儲存庫的文件流程：

1. 每次執行都會在 `.auto-readme-work/<run-id>/pipeline-context.md` 產出情境與限制。
2. 在 `language-nav-root.md` 與 `language-nav-i18n.md` 產生語言切換樣板。
3. 以增量方式套用 README 編修，以保留實質歷史。
4. 本地化檔案依同一結構化模板同步。

## 📚 文件輸入與產生的成果

| 檔案 | 用途 |
|---|---|
| `.auto-readme-work/20260301_070633/pipeline-context.md` | 本輪作業的限制與指示來源。 |
| `.auto-readme-work/20260301_070633/translation-plan.txt` | 多語同步的語言映射。 |
| `.auto-readme-work/20260301_070633/language-nav-root.md` | `README.md` 的標準語言切換列。 |
| `.auto-readme-work/20260301_070633/language-nav-i18n.md` | 本地化 README 的標準語言切換列。 |
| `.auto-readme-work/20260301_070633/repo-structure-analysis.md` | 本次產生所使用的儲存庫快照。 |
| `README.md.auto-readme-support*` | 先前 bootstrap 輪次使用的支援清單。 |

## 🧭 儲存庫工作流程目標

此儲存庫刻意設計得輕量。長期目標是在不回退技術上下文、連結與結構的前提下，讓根 README 與已翻譯版本持續同步。

## 🧰 前置條件

- `git`（供版本庫存取）。
- POSIX shell（範例使用 `bash`）。
- 支援 Markdown 的編輯器。

### 執行時假設

目前尚未偵測到可執行產品資訊，因此尚未定義建置/執行需求。

## 📥 安裝

目前尚未提供二進位安裝或建置流程。

```bash
# Clone the repository
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ 用法

目前用途集中在文件維護與多語一致性。

### 常用指令

```bash
ls -la
ls -la .auto-readme-work/20260301_070633
ls -la i18n
```

### 典型 README 同步流程

1. 查看 `.auto-readme-work/20260301_070633/pipeline-context.md` 中的執行情境。
2. 檢查 `.auto-readme-work/20260301_070633/language-nav-*.md` 的語言切換樣板。
3. 以增量方式編修 `README.md`，不要移除既有實質章節。
4. 保持 banner 與 Support 區塊各保留一次且位於要求位置。
5. 依需要將 `i18n/README.*.md` 對齊到同一結構。

## ⚙️ 組態

目前尚無應用程式組態。儲存庫層級的文件行為由 `.auto-readme-work/` 中的流程產物與 `i18n/` 中的語系檔案定義。

- `pipeline-context.md`（限制與目標）
- `translation-plan.txt`（語系範圍與對照）
- `language-nav-root.md` 與 `language-nav-i18n.md`（語言導覽一致性）
- `README.md.auto-readme-support*`（腳手架輔助檔）

## 🧪 範例

### 範例 1：檢查語言選擇器列

```bash
cat .auto-readme-work/20260301_070633/language-nav-root.md
cat .auto-readme-work/20260301_070633/language-nav-i18n.md
```

### 範例 2：驗證支援語系與翻譯檔案

```bash
cat .auto-readme-work/20260301_070633/translation-plan.txt
```

### 範例 3：確認腳手架狀態

```bash
find . -maxdepth 2 \
  \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

## 🛠️ 開發註記

- 使用增量式編輯來保留既有技術上下文。
- 在確認具體清單檔案存在前，不要加入建置/執行步驟。
- 確保 banner 與 support 區塊只出現一次。
- 當儲存庫行為尚未明確時，請註明假設。
- 指令範例要對應現有檔案與目錄。

## 🩺 疑難排解

### 我只看到 Markdown 檔案

在目前 bootstrap 階段這是預期行為。

### 語言切換器看起來不一致

請將每個 `README.*.md` 與根語言切換列，以及 `.auto-readme-work/20260301_070633/` 內最新的 pipeline context 檔案進行比對。

### 我的分支落後

```bash
git fetch origin
git pull --ff-only
```

### 我想補充程式碼說明

僅在加入具體清單檔（例如 `package.json`、`pyproject.toml`、`Cargo.toml` 等）並確認這些資產在儲存庫中存在後，才新增建置/執行命令。

## 🗺️ 發展藍圖

- 引入具體應用／執行時元件。
- 在程式與工具鏈就緒後補充安裝、執行與部署文件。
- 增加 CI 檢查，以確保 Markdown 品質與語系一致。
- 透過明確版本化的流程保證翻譯可重現。
- 為文件與未來程式碼貢獻者補上各自的貢獻指引。

## 🤝 貢獻

歡迎提交貢獻。

1. 建立一則描述變更的 issue。
2. 開啟專用分支。
3. 保持修改精簡且為增量。
4. 保留既有實質段落。
5. 提交 pull request 並附上簡短驗證備註。

### 建議流程

```bash
git checkout -b docs/your-update
# edit README.md and/or i18n/
git add README.md
git commit -m "docs: refine README draft"
git push -u origin docs/your-update
```

## 📄 授權

本儲存庫快照尚未包含授權文件。


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
