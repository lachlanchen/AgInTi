[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# AgInTi

[![Status](https://img.shields.io/badge/status-initializing-orange)](#aginti)
[![Docs](https://img.shields.io/badge/docs-readme_draft-blue)](#aginti)
[![Repository Stage](https://img.shields.io/badge/stage-bootstrap-yellow)](#aginti)
[![i18n](https://img.shields.io/badge/i18n-planned-0ea5e9)](#aginti)
[![License](https://img.shields.io/badge/license-TBD-lightgrey)](#aginti)

## 📌 概要

AgInTi は現在、初期化/スキャフォールド段階にあります。この README ドラフト時点で、リポジトリに主に含まれているのは次の内容です。

- Git メタデータ（`.git/`）
- 多言語 README ファイル用に準備された `i18n/` ディレクトリ
- README 生成パイプラインのコンテキストと、言語計画アーティファクトを含む `.auto-readme-work/` ワークスペース

現在のワーキングツリーでは、アプリケーションのソースコード、パッケージマニフェスト、ランタイムのエントリーポイント、CI ワークフローはいずれも検出されていません。

### リポジトリスナップショット

| 項目 | 現在の状態 |
| --- | --- |
| Source code | まだ検出されていません |
| Runtime manifests | まだ検出されていません |
| CI workflows | まだ検出されていません |
| Documentation workspace | `.auto-readme-work/20260228_184104/` |
| i18n directory | 存在します（`i18n/`） |

## 🚦 プロジェクト状況

これはリポジトリの **最初の完全な README ドラフト**です。

- 確認されたリポジトリ状態: **トップレベルのソースツリーはまだありません**
- 既存の canonical README ベースライン: **この実行時点のローカルワークスペースには存在しません**
- 本 README で採用した文書化方針: 発見できたリポジトリに正確な情報は保持し、不明点は削除や創作をせず明確にラベル付けする

リモートブランチ/履歴に canonical な過去 README が存在する場合は、内容を置き換えるのではなく、このドラフトへ段階的にマージしてください。

## ✨ 機能（現状）

現在のリポジトリ機能は、ドキュメント/パイプライン指向です。

- `.auto-readme-work/` 配下の README 生成パイプラインワークスペース
- 多言語 README の対象計画（英語を含む 11 言語）
- ルートおよび `i18n/` 向けの言語ナビゲーションテンプレート

計画中の製品/ランタイム機能は、現段階では不明です。

## 🗂️ プロジェクト構成

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

### 主要ドキュメント入力

| File | Purpose |
| --- | --- |
| `.auto-readme-work/20260228_184104/pipeline-context.md` | この実行における README 制約と生成ワークフローのコンテキストを定義します。 |
| `.auto-readme-work/20260228_184104/repo-structure-analysis.md` | 検出されたリポジトリ構成と既知のギャップを要約します。 |
| `.auto-readme-work/20260228_184104/language-nav-root.md` | ルート `README.md` 向けの canonical 言語切替行です。 |
| `.auto-readme-work/20260228_184104/language-nav-i18n.md` | `i18n/` 配下の翻訳ファイル向け canonical 言語切替行です。 |
| `.auto-readme-work/20260228_184104/translation-plan.txt` | 翻訳用のロケールとファイルの対応を定義します。 |

## 🧰 前提条件

現時点では、リポジトリ内容をそのまま利用するためのランタイム前提条件はありません。

ドキュメントワークフローおよびリポジトリ操作には、通常次が必要です。

- `git`
- POSIX 互換シェル（例は `bash` を使用）
- テキストエディタ

## 📥 インストール

現時点ではアプリケーション/パッケージマニフェストが存在しないため、インストール/ビルド手順はありません。

リポジトリをクローンします。

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ 使い方

現在の実用的な用途は、リポジトリの確認と README/i18n ドキュメント作業です。

例:

```bash
# Show top-level files
ls -la

# Inspect auto-generated README context files
ls -la .auto-readme-work/20260228_184104

# Inspect i18n directory
ls -la i18n
```

## ⚙️ 設定

現時点でアプリケーション設定ファイルは検出されていません。

既知のリポジトリ設定シグナル:

- Git リモートは `origin git@github.com:lachlanchen/AgInTi.git` として設定されています
- 多言語 README のナビゲーションと対象ロケールの対応は `.auto-readme-work/20260228_184104/` にあります

## 🧪 例

### 例 1: README 言語ナビゲーションの整合性を検証する

```bash
# Compare language switcher templates used by the pipeline
cat .auto-readme-work/20260228_184104/language-nav-root.md
cat .auto-readme-work/20260228_184104/language-nav-i18n.md
```

### 例 2: 翻訳対象セットを確認する

```bash
cat .auto-readme-work/20260228_184104/translation-plan.txt
```

### 例 3: リポジトリにランタイムマニフェストがまだないことを確認する

```bash
# Typical manifest check (expected: none in current state)
find . -maxdepth 2 \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml \)
```

## 🛠️ 開発メモ

- リポジトリは初期ブートストラップ段階にあるようです。
- 多言語構成を準備した README ファーストのセットアップが進行中です。
- 構成分析時点ではローカルコミット履歴が検出されていません（分析コンテキストには `No commits yet on main` と記録）。
- ソースコードを追加する際は、具体的なセットアップ、使用方法、設定手順をこの README に反映してください。

## 🩺 トラブルシューティング

### 旧/ローカルコピーで `README.md` が欠けている

ローカルクローンに以前 `README.md` が含まれていなかった場合は、最新ブランチ状態と同期してください。

```bash
git fetch origin
git pull --ff-only
```

### `i18n/` はあるが翻訳ファイルがない

これは初期ドラフト段階では想定内です。翻訳対象は次で定義されています。

- `.auto-readme-work/20260228_184104/translation-plan.txt`

### プロジェクトのランタイムスタックが不明

`src/`、マニフェスト、エントリーポイントが見当たらない場合は、現在確認されている状態と一致します。実装ファイルが導入された時点でスタック情報を追加してください。

## 🗺️ ロードマップ

直近のドキュメント整備およびプロジェクトブートストラップ目標:

- 実際のプロジェクト目的とアーキテクチャを含む英語 README ベースラインを完成させる
- 翻訳計画に従って `i18n/` 配下に翻訳 README を追加する
- アプリケーションのソースレイアウトとランタイムマニフェストを導入する
- 再現可能なセットアップおよび実行コマンドを追加する
- コードベースができ次第、CI チェック（lint/test/docs validation）を追加する

## 🤝 コントリビュート

コントリビューションを歓迎します。リポジトリは初期セットアップ段階のため、次の流れを推奨します。

1. 変更提案（ドキュメント、構成、初期コードレイアウト）を説明する issue を作成する。
2. 機能ブランチを作成する。
3. 変更は焦点を絞り、文書化する。
4. 振る舞いまたは構成が変わる場合は README/i18n ドキュメントを更新する。
5. 背景と検証手順を明記して pull request を作成する。

推奨ローカルワークフロー:

```bash
git checkout -b feat/your-change
# make edits

git add .
git commit -m "Describe your change"
git push -u origin feat/your-change
```

## 💬 サポート

現時点では、専用サポート、スポンサー、寄付チャネルはリポジトリファイルで宣言されていません。

今後サポートリンクが追加された場合は、このセクションに追記し、README 改訂時にも保持してください。

## 📄 ライセンス

現在のリポジトリ内容では、ライセンス情報は宣言されていません。

- Status: `TBD`
- 推奨される次のステップ: `LICENSE` ファイルを追加し、このセクションを正確な SPDX 識別子で更新する。

## 🧾 前提と保持に関する注記

- このドラフトは `/home/lachlan/ProjectsLFS/AgInTi` に現在存在するリポジトリファイルから作成されています。
- 生成時点で canonical な既存 README はローカルで利用できなかったため、そこから実質的内容を取り込むことはできませんでした。
- 保持方針に従い、不明または欠落している詳細は推測や省略をせず、明示しています。
