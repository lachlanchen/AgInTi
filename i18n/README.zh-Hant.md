[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Status](https://img.shields.io/badge/status-initializing-orange)](#aginti)
[![Docs](https://img.shields.io/badge/docs-readme_draft-blue)](#aginti)
[![Repository%20Stage](https://img.shields.io/badge/stage-bootstrap-yellow)](#aginti)
[![i18n](https://img.shields.io/badge/i18n-planned-0ea5e9)](#aginti)
[![License](https://img.shields.io/badge/license-TBD-lightgrey)](#aginti)

*以文件為優先的啟始儲存庫 • README 優先工作流程 • 持續推進多語規劃。*

| 重點 | 當前狀態 |
|---|---|
| 核心成熟度 | 啟始腳手架（`README`-first） |
| 本地化 | `i18n/` 維護 10 種語言 |
| 流水線來源 | `.auto-readme-work/20260301_064213/` |

---

## 📌 概覽

AgInTi 目前是以文件腳手架為主的儲存庫，採用 README 優先工作流程並進行多語文件規劃。

在本草稿撰寫時，倉庫內容聚焦於文件協作和語言準備，尚未轉向可執行的產品程式碼：

- ✅ 尚未偵測到頂層原始碼樹。
- ✅ `i18n/` 包含翻譯版 README。
- ✅ `.auto-readme-work/20260301_064213/` 儲存本次處理的啟用流水線上下文。
- ✅ `.auto-readme-work/20260228_184104/` 作為歷史紀錄保留。

### 倉庫快照

| 項目 | 當前狀態 |
|---|---|
| 🧩 原始碼 | 尚未偵測到 |
| ⚙️ 執行時清單 | 尚未偵測到 |
| 🧪 CI 工作流程 | 尚未偵測到 |
| 🧭 文件工作區 | `.auto-readme-work/20260301_064213/` |
| 🌐 文件翻譯 | `i18n/` 中有 10 種語言 |

---

## 🚦 專案狀態

這份 README 是一個增量式、與倉庫實際對齊的第一份完整英文草稿。

- 狀態仍維持啟始/文件導向。
- 保留既有的實質性區段，並在必要處擴充，而非直接取代。
- 未知項目會明確標註，避免做推測性描述。

若上游在其他分支或歷史中存在正式 README，後續更新應以增量方式合併。

---

## ✨ 特性

- 文件優先的倉庫佈局
- `.auto-readme-work/` 下集中化的多語 README 流水線
- 明確的語言切換範本與翻譯對應檔
- 用於倉庫檢視與驗證的實際指令片段
- 以去重方式嚴格追蹤 README 更新流程（支援/橫幅區塊）

---

## 🗂️ 專案結構

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

### 關鍵文件輸入

| 檔案 | 用途 |
|---|---|
| `.auto-readme-work/20260301_064213/pipeline-context.md` | 記錄本次執行的生成限制與提示上下文。 |
| `.auto-readme-work/20260301_064213/repo-structure-analysis.md` | 偵測到的倉庫結構與功能缺口快照。 |
| `.auto-readme-work/20260301_064213/translation-plan.txt` | 語系與檔案映射計畫。 |
| `.auto-readme-work/20260301_064213/language-nav-root.md` | `README.md` 的標準語言切換列。 |
| `.auto-readme-work/20260301_064213/language-nav-i18n.md` | `i18n/` 檔案的標準語言切換列。 |

---

## 🧰 先決條件

目前的倉庫狀態不需要執行時相依套件。

進行文件使用與維護時，你需要：

- `git`
- POSIX shell（範例使用 `bash`）
- 用於 Markdown 更新的文字編輯器

---

## 📥 安裝

目前尚未有安裝 / 建置流程。

在本機檢視倉庫：

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ 使用

目前用途主要是文件維護、稽核與在地化同步。

### 常見工作流程

```bash
ls -la
ls -la .auto-readme-work/20260301_064213
ls -la i18n
```

### 典型 README 工作流程

1. 閱讀 `.auto-readme-work/20260301_064213/` 中目前的上下文檔。
2. 檢查來源與已翻譯的 README 內容。
3. 使用增量編輯以避免移除既有實質內容。
4. 在各語系版本中保持語言切換器與支援區塊一致。

---

## ⚙️ 組態

目前尚未存在應用程式組態檔。

目前文件層面的組態主要由以下內容表示：

- `.auto-readme-work/20260301_064213/translation-plan.txt` 的目標語系清單
- `.auto-readme-work/20260301_064213/language-nav-root.md` 與 `.../language-nav-i18n.md` 的語言切換範本
- `.auto-readme-work/20260301_064213/repo-structure-analysis.md` 的倉庫結構上下文

---

## 🧪 範例

### 範例 1：驗證語言切換行

```bash
cat .auto-readme-work/20260301_064213/language-nav-root.md
cat .auto-readme-work/20260301_064213/language-nav-i18n.md
```

### 範例 2：確認翻譯範圍

```bash
cat .auto-readme-work/20260301_064213/translation-plan.txt
```

### 範例 3：確認腳手架狀態（預期：無清單）

```bash
find . -maxdepth 2 \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

---

## 🛠️ 開發備註

- 將此檔案維持為英文文件的標準來源。
- 更新時保留實質段落（採用增量編輯策略）。
- 僅在對應程式碼、清單與工具鏈就緒後，才加入執行指令。
- 保持支援與 banner 區塊去重（各保留一份）。
- 在功能落地後盡快更新路線圖與疑難排解內容。

---

## 🩺 疑難排解

### 我只看到文件檔案

在目前的啟始狀態下這是預期行為；未偵測到程式碼或執行時清單。

### 本地化文件不一致

請使用最新的翻譯計畫並重新執行 README 同步流程，以正規化結構與連結。

### 本機分支感覺過時

```bash
git fetch origin
git pull --ff-only
```

---

## 🗺️ 路線圖

- 當程式碼引入後，新增具體的產品/應用層。
- 從真實清單補充安裝、建置與執行說明。
- 新增 CI 工作流程與文件檢查。
- 擴展程式碼與翻譯的貢獻規範。
- 維持各語言 README 的同步與最新。

---

## 🤝 貢獻

歡迎提交貢獻。

1. 建立 issue，附上背景與範圍。
2. 建立專屬分支。
3. 保持修改專注且為增量式。
4. 保留既有技術細節與段落上下文。
5. 提交 PR 並附上清楚的驗證說明。

### 建議流程

```bash
git checkout -b feat/your-change
# 編輯 README 與相關檔案
git add README.md

git commit -m "docs: update README"

git push -u origin feat/your-change
```

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 📄 授權

尚未提供 `LICENSE` 檔案。
