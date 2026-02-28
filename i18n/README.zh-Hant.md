[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# AgInTi

[![Status](https://img.shields.io/badge/status-initializing-orange)](#aginti)
[![Docs](https://img.shields.io/badge/docs-readme_draft-blue)](#aginti)
[![Repository Stage](https://img.shields.io/badge/stage-bootstrap-yellow)](#aginti)
[![i18n](https://img.shields.io/badge/i18n-planned-0ea5e9)](#aginti)
[![License](https://img.shields.io/badge/license-TBD-lightgrey)](#aginti)

## 📌 概覽

AgInTi 目前處於初始化／腳手架階段。在此 README 草稿撰寫時，儲存庫主要包含：

- Git 中繼資料（`.git/`）
- 已為多語 README 檔案準備好的 `i18n/` 目錄
- 一個 `.auto-readme-work/` 工作區，內含 README 產生流程脈絡與語言規劃產物

在目前工作樹中，尚未偵測到應用程式原始碼、套件清單、執行期進入點或 CI 工作流程。

### 儲存庫快照

| 項目 | 目前狀態 |
| --- | --- |
| 原始碼 | 尚未偵測到 |
| 執行期清單 | 尚未偵測到 |
| CI 工作流程 | 尚未偵測到 |
| 文件工作區 | `.auto-readme-work/20260228_184104/` |
| i18n 目錄 | 已存在（`i18n/`） |

## 🚦 專案狀態

這是儲存庫的**第一版完整 README 草稿**。

- 觀察到的儲存庫狀態：**尚無頂層原始碼樹**
- 既有的正典 README 基線：**本次執行時在本機工作區中不存在**
- 此處採用的文件方法：保留所有已發現且與儲存庫一致的細節，並清楚標示未知資訊，而非刪除或捏造內容

如果遠端分支／歷史中存在正典歷史 README，應將此草稿與該內容逐步合併，而不是替換實質章節。

## ✨ 功能（目前）

目前儲存庫能力以文件／流程為主：

- 位於 `.auto-readme-work/` 的 README 產生流程工作區
- 多語 README 目標規劃（含英文共 11 種語言）
- 根目錄與 `i18n/` 的語言導覽範本

現階段尚不清楚規劃中的產品／執行期功能。

## 🗂️ 專案結構

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

### 主要文件輸入

| 檔案 | 用途 |
| --- | --- |
| `.auto-readme-work/20260228_184104/pipeline-context.md` | 定義本次執行的 README 限制條件與產生流程脈絡。 |
| `.auto-readme-work/20260228_184104/repo-structure-analysis.md` | 彙整偵測到的儲存庫結構與已知缺口。 |
| `.auto-readme-work/20260228_184104/language-nav-root.md` | 根目錄 `README.md` 的正典語言切換列。 |
| `.auto-readme-work/20260228_184104/language-nav-i18n.md` | `i18n/` 下翻譯檔案的正典語言切換列。 |
| `.auto-readme-work/20260228_184104/translation-plan.txt` | 翻譯的語系對應檔案映射。 |

## 🧰 先決條件

目前按現狀使用儲存庫內容不需要執行期先決條件。

若要進行文件工作流程與儲存庫操作，你可能需要：

- `git`
- POSIX 相容 shell（範例使用 `bash`）
- 文字編輯器

## 📥 安裝

由於尚無應用程式／套件清單，暫時沒有安裝／建置步驟。

複製儲存庫：

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ 使用方式

目前實際使用方式是儲存庫檢視與 README/i18n 文件工作。

範例：

```bash
# Show top-level files
ls -la

# Inspect auto-generated README context files
ls -la .auto-readme-work/20260228_184104

# Inspect i18n directory
ls -la i18n
```

## ⚙️ 設定

目前尚未偵測到應用程式設定檔。

已知的儲存庫設定訊號：

- Git remote 設為 `origin git@github.com:lachlanchen/AgInTi.git`
- `.auto-readme-work/20260228_184104/` 中的多語 README 導覽與目標語系映射

## 🧪 範例

### 範例 1：驗證 README 語言導覽一致性

```bash
# Compare language switcher templates used by the pipeline
cat .auto-readme-work/20260228_184104/language-nav-root.md
cat .auto-readme-work/20260228_184104/language-nav-i18n.md
```

### 範例 2：確認翻譯目標集合

```bash
cat .auto-readme-work/20260228_184104/translation-plan.txt
```

### 範例 3：驗證儲存庫尚無執行期清單

```bash
# Typical manifest check (expected: none in current state)
find . -maxdepth 2 \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml \)
```

## 🛠️ 開發備註

- 儲存庫看起來仍在早期 bootstrap 階段。
- 以 README 為先的初始化正在進行，且多語結構已準備好。
- 在結構分析期間未偵測到本機提交歷史（分析脈絡中記錄為 `No commits yet on main`）。
- 新增原始碼時，請以具體的設定、使用與設定說明更新此 README。

## 🩺 疑難排解

### 較舊／本機副本缺少 `README.md`

如果你的本機 clone 先前不包含 `README.md`，請與最新分支狀態同步：

```bash
git fetch origin
git pull --ff-only
```

### `i18n/` 已存在但缺少翻譯檔

這在早期草稿階段屬於預期情況。翻譯目標定義於：

- `.auto-readme-work/20260228_184104/translation-plan.txt`

### 專案執行期技術棧不明確

若你看不到 `src/`、清單檔或進入點，這與目前觀察狀態一致。引入實作檔案後再補上技術棧細節。

## 🗺️ 路線圖

近期文件與專案 bootstrap 目標：

- 以真實專案目的與架構完善英文基線 README
- 依翻譯計畫在 `i18n/` 下新增翻譯 README 檔案
- 引入應用程式原始碼佈局與執行期清單
- 新增可重現的設定與執行指令
- 程式碼庫建立後加入 CI 檢查（lint/test/docs validation）

## 🤝 貢獻

歡迎貢獻。由於儲存庫仍在早期建置階段：

1. 開啟 issue 說明提議變更（文件、結構或初始程式碼佈局）。
2. 建立功能分支。
3. 讓變更聚焦且有文件化。
4. 只要行為或結構變更，就同步更新 README/i18n 文件。
5. 提交含清楚脈絡與驗證步驟的 pull request。

建議的本機流程：

```bash
git checkout -b feat/your-change
# make edits

git add .
git commit -m "Describe your change"
git push -u origin feat/your-change
```

## 💬 支援

目前儲存庫檔案中尚未宣告專屬支援、贊助或捐款管道。

若後續新增支援連結，請在此加入並於 README 修訂時持續保留。

## 📄 授權

目前儲存庫內容尚未宣告授權資訊。

- 狀態：`TBD`
- 建議下一步：新增 `LICENSE` 檔案，並在本節填入確切 SPDX 識別碼。

## 🧾 假設與保留說明

- 本草稿是根據 `/home/lachlan/ProjectsLFS/AgInTi` 目前存在的儲存庫檔案建立。
- 產生當下本機無可用的既有正典 README；因此無法自其中匯入實質內容。
- 依保留政策，未知或缺漏細節會明確標示，而非臆測或省略。
