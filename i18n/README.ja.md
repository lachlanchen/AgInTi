[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Status](https://img.shields.io/badge/status-initializing-orange)](#aginti)
[![Docs](https://img.shields.io/badge/docs-readme_draft-blue)](#aginti)
[![Repository%20Stage](https://img.shields.io/badge/stage-bootstrap-yellow)](#aginti)
[![i18n](https://img.shields.io/badge/i18n-planned-0ea5e9)](#aginti)
[![License](https://img.shields.io/badge/license-TBD-lightgrey)](#aginti)

*ドキュメントファーストのブートストラップリポジトリ • READMEファーストワークフロー • アクティブな多言語計画。*

| フォーカス | 現在の状態 |
|---|---|
| コア成熟度 | Bootstrapスキャフォールド（`README`-first） |
| ローカリゼーション | `i18n/` で10言語を維持 |
| パイプライン情報源 | `.auto-readme-work/20260301_064213/` |

---

## 📌 Overview

AgInTi は現在、READMEファーストワークフローと多言語ドキュメント計画を備えた、ドキュメント優先のブートストラップリポジトリです。

このドラフト時点では、リポジトリ内容はランタイム製品よりも、ドキュメント調整と語学対応準備に焦点を当てています。

- ✅ まだトップレベルのソースツリーは検出されていません。
- ✅ `i18n/` には README の各言語版が格納されています。
- ✅ `.auto-readme-work/20260301_064213/` が今回の実行時のアクティブなパイプラインコンテキストを保持しています。
- ✅ `.auto-readme-work/20260228_184104/` は履歴として保持されています。

### Repository snapshot

| 項目 | 現在の状態 |
|---|---|
| 🧩 ソースコード | まだ検出されていません |
| ⚙️ ランタイムマニフェスト | まだ検出されていません |
| 🧪 CIワークフロー | まだ検出されていません |
| 🧭 ドキュメントワークスペース | `.auto-readme-work/20260301_064213/` |
| 🌐 翻訳済みドキュメント | `i18n/` 内の10言語 |

---

## 🚦 Project status

このREADMEは、増分のみで更新可能な、リポジトリ実態を反映した最初の完全な英語ドラフトです。

- 状態は依然としてブートストラップ／ドキュメント志向です。
- 既存の実質的なセクションは置換ではなく保持・拡張されています。
- 不明点は明示し、推測ベースの主張は避けています。

将来の更新では、別ブランチや履歴にある正規のREADMEが存在する場合、それを増分的に統合すべきです。

---

## ✨ Features

- ドキュメントファーストのリポジトリ構成
- `.auto-readme-work/` 配下での多言語READMEパイプラインを一元管理
- 明示的な言語切り替えテンプレートと翻訳マッピングファイル
- リポジトリ検証や点検のための実用的なコマンドスニペット
- サポートバナー/バナーの重複排除を含むREADME更新を厳格に追跡

## 🗂️ Project structure

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

### Key documentation inputs

| ファイル | 用途 |
|---|---|
| `.auto-readme-work/20260301_064213/pipeline-context.md` | この実行時の制約とプロンプトの文脈 |
| `.auto-readme-work/20260301_064213/repo-structure-analysis.md` | 検出された構成と未対応項目のスナップショット |
| `.auto-readme-work/20260301_064213/translation-plan.txt` | ロケールとファイルの対応表 |
| `.auto-readme-work/20260301_064213/language-nav-root.md` | `README.md` 用の標準言語セレクタ行 |
| `.auto-readme-work/20260301_064213/language-nav-i18n.md` | `i18n/` 用の標準言語セレクタ行 |

---

## 🧰 Prerequisites

現在のリポジトリ状態では、ランタイム依存は不要です。

ドキュメントの使用とメンテナンスには以下が必要です。

- `git`
- POSIX準拠シェル（例: `bash`）
- Markdown 更新用のテキストエディタ

---

## 📥 Installation

まだインストール／ビルドプロセスはありません。

ローカルでリポジトリを確認するには:

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Usage

現在の用途は、ドキュメント保守、監査、ローカライズ同期です。

### Common workflows

```bash
ls -la
ls -la .auto-readme-work/20260301_064213
ls -la i18n
```

### Typical README workflow

1. `.auto-readme-work/20260301_064213/` の現在のコンテキスト成果物を読む。
2. 元のREADMEと翻訳README内容を確認する。
3. 既存の実質情報を削除しない増分編集を適用する。
4. 言語セレクタとサポート欄をロケール間で一貫させる。

---

## ⚙️ Configuration

まだアプリケーション設定ファイルは存在しません。

現時点のドキュメントレベル設定は以下で表現されます。

- 言語ターゲット向けの `.auto-readme-work/20260301_064213/translation-plan.txt`
- `.auto-readme-work/20260301_064213/language-nav-root.md` と `.../language-nav-i18n.md` の言語セレクタテンプレート
- `.auto-readme-work/20260301_064213/repo-structure-analysis.md` のリポジトリ構成コンテキスト

---

## 🧪 Examples

### Example 1: 言語セレクタ行の検証

```bash
cat .auto-readme-work/20260301_064213/language-nav-root.md
cat .auto-readme-work/20260301_064213/language-nav-i18n.md
```

### Example 2: 翻訳対象の確認

```bash
cat .auto-readme-work/20260301_064213/translation-plan.txt
```

### Example 3: スキャフォールド状態の確認（期待値: マニフェストなし）

```bash
find . -maxdepth 2 \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

---

## 🛠️ Development notes

- このファイルを英語版ドキュメントの正本として維持します。
- 更新時には実質的なセクションを保持してください（増分のみ編集ポリシー）。
- コード・マニフェスト・ツールチェーンが存在した場合のみ実行時の手順を追加します。
- サポート欄とバナー欄は重複なく維持します（それぞれ1つだけ）。
- 機能が実装され次第、ロードマップとトラブルシューティングを更新します。

---

## 🩺 Troubleshooting

### ドキュメントファイルのみ表示される場合

このブートストラップ状態では想定される挙動です。ソースやランタイムのマニフェストは検出されていません。

### ロケール文書が不整合な場合

最新の翻訳計画を使い、README同期フローを再実行して構成とリンクを正規化してください。

### ローカルブランチが古いように感じる場合

```bash
git fetch origin
git pull --ff-only
```

---

## 🗺️ Roadmap

- コード追加時に具体的なプロダクト／アプリケーション層を追加する。
- 実在するマニフェストを用いたセットアップ、ビルド、実行手順を拡張する。
- CIワークフローとドキュメントチェックを追加する。
- コードと翻訳のための貢献基準を拡張する。
- 翻訳READMEを同期し、最新状態を維持する。

---

## 🤝 Contribution

貢献歓迎です。

1. コンテキストとスコープを明記したIssueを開く。
2. 専用ブランチを作成する。
3. 編集は焦点を絞った増分で行う。
4. 既存の技術的詳細とセクション文脈を保持する。
5. 検証結果を明記してPRを作成する。

### Suggested flow

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

## 📄 License

`LICENSE` ファイルはまだ存在しません。
