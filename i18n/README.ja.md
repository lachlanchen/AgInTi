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

英語版 README を正典として維持しつつ、多言語ドキュメントを同期するためのドキュメントファーストなリポジトリ基盤です。運用は **sear creation tools**、**self-healing tools**、**chain of prompt tools** の 3 原則で導かれます。

## 🧭 Quick Navigation

| 種別 | 移動先 |
| --- | --- |
| プロジェクト要約 | [Overview](#overview) |
| コア機能 | [Features](#features) |
| パイプライン設計 | [Architecture](#architecture) |
| 哲学の要点 | [Philosophy at a glance](#philosophy-at-a-glance) |
| 開発者向け運用 | [Development Notes](#development-notes) |
| 今後の方向性 | [Roadmap](#roadmap) |
| プロジェクト支援 | [Support](#-support) |

---

## 📌 Scope and Snapshot

| 項目 | 現在の状態 |
| --- | --- |
| リポジトリ段階 | ドキュメント・ブートストラップのスキャフォールド |
| 実行コード | 現在のスナップショットでは未検出 |
| テスト/CI パイプライン | 現在のスナップショットでは未検出 |
| ローカライズ済み文書 | `i18n/` 配下に 10 ロケール |
| パイプライン成果物 | `.auto-readme-work/` 配下のタイムスタンプ付き実行 |
| ライセンスファイル | 独立ファイルなし（README バッジ: TBD） |
| 哲学ベースライン | Sear creation + self-healing + chain of prompt tools |

## 🌍 Overview

AgInTi は現時点では実行アプリではなく、README のライフサイクル管理とローカライズのためのパイプラインとして機能しています。ルートの `README.md` を正典ソースとし、`i18n/` の各言語版はその構造に同期されます。

本プロジェクトの哲学は装飾ではなく、実運用ルールです。README の更新は次の 3 原則すべてを満たす必要があります。

1. **Sear creation tools**: 制約のあるリポジトリ証拠から、高密度で実用的なドキュメントを意図的に生み出す、鋭い作成ワークフロー。
2. **Self-healing tools**: ドリフト補正、重複排除、構造整合性の復元を行う修復指向メカニズム。
3. **Chain of prompt tools**: パイプライン実行全体でコンテキストから出力までの系譜を保つ、段階的で追跡可能なプロンプト連鎖。

このリポジトリは、リンク・コマンド・サポート情報を維持しながら、意味のある履歴をインクリメンタル更新で継承します。

### Philosophy at a glance

| Principle | Intent | Operational outcome |
| --- | --- | --- |
| **Sear creation tools** | 制約付き証拠から高密度な文書を生成する。 | セクションが実務的・具体的で、リポジトリ根拠に基づいた内容になる。 |
| **Self-healing tools** | ドリフト、重複、構造の陳腐化を修復する。 | 正典 README と各言語 README の整合と清潔性を維持できる。 |
| **Chain of prompt tools** | 生成段階を明示し、追跡可能に保つ。 | パイプライン成果物に再現可能な文脈と受け渡しが残る。 |

## ✨ Features

- ルート文書を正典とする README ファースト戦略。
- 10 ロケールの i18n README を同期する多言語運用。
- `.auto-readme-work/<run-id>/` 成果物に基づくパイプライン駆動編集。
- バナーとサポートパネルを単一化する不変条件で重複表示を防止。
- 重要な技術履歴を保持するインクリメンタル更新規律。

### Principle-to-feature mapping

| Core principle | How it appears in current features |
| --- | --- |
| **Sear creation tools** | リポジトリ根拠に基づく精密な README 草案と安定したセクション足場。 |
| **Self-healing tools** | バナー/サポート重複、古い参照、構造ドリフトを検出して修復する重複排除チェック。 |
| **Chain of prompt tools** | 実行単位成果物チェーン（`pipeline-context`、ナビテンプレート、翻訳計画）による再現性の確保。 |

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

現段階でのアーキテクチャは、アプリ実行基盤ではなくドキュメントパイプライン設計を指します。

### Pipeline flow

1. 実行ごとのコンテキストを `.auto-readme-work/<run-id>/pipeline-context.md` に記録する。
2. 言語ナビゲーションテンプレート（`language-nav-root.md` と `language-nav-i18n.md`）を生成する。
3. 正典 README 内容を `README.md` に対してインクリメンタル更新する。
4. `i18n/` の各 README を正典構造に合わせて同期する。
5. 重複排除、リンク整合、技術詳細保持を構造品質チェックで担保する。

### Core principles in architecture

- **Sear creation tools**: セクションを具体的・完全・リポジトリ準拠に保つため、コンテンツ構築段階で適用する。
- **Self-healing tools**: 重複ブロック削除、古い実行参照の修復、構造整合の復元のため、検証段階で適用する。
- **Chain of prompt tools**: 各生成段階を明示し監査可能にするため、成果物チェーン全体に適用する。

### Principle checkpoints by pipeline stage

| Stage | Sear creation tools | Self-healing tools | Chain of prompt tools |
| --- | --- | --- | --- |
| Context capture | 鋭い生成制約を定義する。 | 入力不足/不正を早期に検知する。 | 元プロンプトと実行メタデータを保持する。 |
| Canonical drafting | リポジトリ証拠から完全な README セクションを構築する。 | リグレッションや内容欠落を防止する。 | 生成物を前段成果物と連結する。 |
| i18n alignment | 各ロケールで構造と技術的同等性を維持する。 | ルートと i18n 間のドリフトを修正する。 | 正典意図を各翻訳版へ引き継ぐ。 |
| Final verification | 可読性と詳細保持を検証する。 | バナー/サポート重複と古い参照を除去する。 | 実行ごとの監査可能な成果物トレイルを残す。 |

## 🧾 Documentation Inputs and Generated Artifacts

| File | Purpose |
| --- | --- |
| `.auto-readme-work/20260302_124338/pipeline-context.md` | この生成パスの制約と目標。 |
| `.auto-readme-work/20260302_124338/repo-structure-analysis.md` | リポジトリ走査サマリーと推定された技術状態。 |
| `.auto-readme-work/20260302_124338/language-nav-root.md` | ルート `README.md` 向け言語選択行の正典。 |
| `.auto-readme-work/20260302_124338/language-nav-i18n.md` | i18n README 向け言語選択行の正典。 |
| `.auto-readme-work/20260302_124338/translation-plan.txt` | ロケール対応と i18n 対象ファイル計画。 |
| `.auto-readme-work/<older-run-id>/...` | 過去の README パイプライン実行コンテキスト。 |

## 🔧 Prerequisites

- `git`
- POSIX shell（例では `bash`）
- Markdown 対応エディタ

### Assumptions

- 現在のスナップショットには実行可能なサービスやアプリマニフェストが存在しません。
- そのため、インストール/ビルド/起動手順はドキュメント運用向けの内容になっています。

## 📥 Installation

現時点ではバイナリ配布やランタイムビルド手順は定義されていません。

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Usage

現在の利用目的は、ドキュメント保守と多言語同期です。

### Common inspection commands

```bash
ls -la
ls -la .auto-readme-work/20260302_124338
ls -la i18n
```

### Canonical README synchronization workflow

1. `.auto-readme-work/20260302_124338/pipeline-context.md` を読む。
2. `language-nav-root.md` と `language-nav-i18n.md` の言語セレクターテンプレートを確認する。
3. `README.md` を正典ソースとしてインクリメンタル更新する。
4. `i18n/README.*.md` を同一構造と主要技術詳細に合わせる。
5. バナーがちょうど 1 つ、サポートパネルがちょうど 1 つであることを確認する。

## ⚙️ Configuration

現時点でランタイム設定はありません。ドキュメントの振る舞いはリポジトリ成果物で駆動されます。

- `pipeline-context.md`: 実行目標と制約
- `repo-structure-analysis.md`: スナップショット証拠とギャップ
- `language-nav-root.md` と `language-nav-i18n.md`: ナビゲーション整合
- `translation-plan.txt`: ロケール対象と対応関係

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

- 正典 README の意味あるセクションとリンクを維持してください。
- 破壊的な書き換えではなくインクリメンタル編集を優先してください。
- バナーとサポートブロックは 1 つだけにしてください。
- ルート README と i18n README の構造を同期してください。
- ランタイムやインフラ詳細が不明な場合は前提を明示してください。
- 哲学トライアドを実運用ガードレールとして適用してください。
  - 高密度な草案作成には **Sear creation tools**。
  - 整合性修復には **Self-healing tools**。
  - 段階間の再現可能な受け渡しには **Chain of prompt tools**。

## 🚑 Troubleshooting

### I only see Markdown files and pipeline artifacts

現在のブートストラップ段階では想定どおりです。

### Language selector lines differ between files

以下の正典テンプレートを使用してください。

- `.auto-readme-work/20260302_124338/language-nav-root.md`
- `.auto-readme-work/20260302_124338/language-nav-i18n.md`

### My branch is behind

```bash
git fetch origin
git pull --ff-only
```

### I want to add runtime instructions

`package.json`、`pyproject.toml`、`go.mod`、`Cargo.toml` のような具体的マニフェストを追加し、実在パスを確認してからビルド/実行手順を追加してください。

## 🗺️ Roadmap

1. **sear creation tools** を強化し、README 草案テンプレート、セクション品質ゲート、証拠から出力への検証を標準化する。
2. **self-healing tools** を拡張し、重複ブロック、ロケールドリフト、壊れた内部アンカー、古い実行参照の自動検査を追加する。
3. **chain of prompt tools** を実行段階全体で形式化し、コンテキスト生成・翻訳・検証の再現可能なトレースを確立する。
4. リポジトリスクリプト導入後に、ドキュメント保守を単一コマンド化する。
5. Markdown 品質、リンク整合、i18n 構造同等性の CI チェックを追加する。
6. マニフェストとエントリポイントが追加された段階で、具体的なランタイム要素を導入する。
7. 安定したライセンス方針を公開し、独立したライセンスファイルを追加する。

### Roadmap by principle focus

| Focus area | Near-term target |
| --- | --- |
| **Sear creation tools** | 草案テンプレートと証拠ベースのセクションプロンプトを改善する。 |
| **Self-healing tools** | 重複検知、古いアンカー検査、ロケールドリフト修復を自動化する。 |
| **Chain of prompt tools** | 再現可能な多言語出力のため、実行段階成果物の契約を標準化する。 |

## 🤝 Contribution

コントリビューションを歓迎します。

1. まず意図する変更内容を Issue で共有する。
2. 変更範囲を絞ったブランチを作成する。
3. ドキュメント編集はインクリメンタルかつリポジトリ根拠に沿って行う。
4. 重要なリンク、コマンド、意味のある履歴文脈を維持する。
5. 簡潔な検証メモとともに pull request を作成する。

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

TBD. 現在のスナップショットには独立したライセンスファイルはまだ存在しません。
