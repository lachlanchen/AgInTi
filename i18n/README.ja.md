[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Repository](https://img.shields.io/badge/Repository-AgInTi-0f172a?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lachlanchen/AgInTi)
[![Docs](https://img.shields.io/badge/Docs-README%20Bootstrap-0ea5e9?style=for-the-badge&logo=mdbook&logoColor=white)](#aginti)
[![Localization](https://img.shields.io/badge/i18n-10%20locales-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)](#documentation-inputs-and-generated-artifacts)
[![Status](https://img.shields.io/badge/Stage-Documentation%20Pipeline-f59e0b?style=for-the-badge&logo=githubactions&logoColor=white)](#scope-and-snapshot)
[![License](https://img.shields.io/badge/License-TBD-94a3b8?style=for-the-badge&logo=readme&logoColor=white)](#license)

ドキュメントを最初に整備し、完全な英語版 README と同時更新された多言語ドキュメントを維持するためのリポジトリ・ブートストラップです。

## 🧭 クイックナビゲーション

| 種別 | 行き先 |
|---|---|
| リポジトリのワークフロー | [スコープとスナップショット](#-scope-and-snapshot) |
| 使用例 | [Usage](#-usage) |
| 寄稿ガイド | [Contribution](#-contribution) |
| このプロジェクトのサポート | [Support](#-support) |

---

[![Pipeline](https://img.shields.io/badge/Pipeline-.auto--readme--work-0f172a?style=flat-square&logo=githubactions&logoColor=white)](./.auto-readme-work)
[![Locales](https://img.shields.io/badge/Locales-10%20files-22c55e?style=flat-square&logo=googletranslate&logoColor=white)](./i18n)
[![Scope](https://img.shields.io/badge/Scope-Documentation-0ea5e9?style=flat-square&logo=mdbook&logoColor=white)](#documentation-inputs-and-generated-artifacts)

## 📌 一覧

| 🎯 フォーカス | 🧩 現在の値 |
| --- | --- |
| リポジトリの目的 | 多言語 README 同期のためのドキュメント・ブートストラップ |
| コア原則 | インクリメンタル編集で主要履歴を維持 |
| 現在の状態 | リポジトリスナップショットで実行時アプリ/サービスは検出されていません |

---

| ✅ スナップショット | 📌 現在の状態 |
| --- | --- |
| リポジトリフェーズ | `.auto-readme-work/` が主導するブートストラップスコープ |
| ローカライゼーション | 10 の翻訳 README |
| 検証済み実行 | 実行可能なアプリやサービスは検出されていません |

## 📌 概要

AgInTi は **documentation-bootstrap** リポジトリです。

このリポジトリは README ファーストのドキュメント化、ローカリゼーション基盤、そして一貫した多言語ドキュメントを生成するための反復的ワークフロー成果物に焦点を当てています。

- ✅ まだトップレベルの実行時ソースツリーは検出されていません。
- ✅ `i18n/` には 10 の翻訳 README が含まれています。
- ✅ `.auto-readme-work/` は反復的ドキュメント更新のためのパイプライン成果物を保持しています。
- ✅ インクリメンタル更新で既存の実質的な内容が保持されています。

## ✅ スコープとスナップショット

| 項目 | 現在の状態 |
|---|---|
| 🧩 ソースコード | 検出されません |
| 🧪 テスト/CI | 検出されません |
| 📘 ドキュメントワークフロー | `.auto-readme-work/` 駆動 |
| 🌐 ローカライズド文書 | 10 言語を維持 |
| 🔒 ライセンスファイル | このスナップショットには存在しません |

## ✨ 特徴

- README ファーストのリポジトリ文書化戦略。
- ルートとローカライズページ向けの正準リンクを持つ言語認識ワークフロー。
- 定義済み位置でバナーとサポートブロックを重複なしで維持。
- 既存の重要セクションを保持するインクリメンタル更新。
- ドキュメント貢献者向けの実用的な検査スニペット。

## 🗂️ プロジェクト構造

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

## 🧱 アーキテクチャとワークフローモデル

現時点では「アーキテクチャ」は、このリポジトリのドキュメントパイプラインを指します。

1. 制約とコンテキストは各実行ごとに `.auto-readme-work/<run-id>/pipeline-context.md` として生成されます。
2. 言語ナビゲータのテンプレートが `language-nav-root.md` / `language-nav-i18n.md` によって作成されます。
3. README の実質的な履歴を保ったまま、インクリメンタルな編集が適用されます。
4. ローカライズ済みファイルは同一の構造テンプレートから同期されます。

## 📚 ドキュメント入力と生成成果物

| ファイル | 目的 |
|---|---|
| `.auto-readme-work/20260301_070633/pipeline-context.md` | 今回の実行の制約と指示 |
| `.auto-readme-work/20260301_070633/translation-plan.txt` | 多言語同期のロケール対応表 |
| `.auto-readme-work/20260301_070633/language-nav-root.md` | `README.md` の正規言語ナビゲーション行 |
| `.auto-readme-work/20260301_070633/language-nav-i18n.md` | 翻訳済み README の正規言語ナビゲーション行 |
| `.auto-readme-work/20260301_070633/repo-structure-analysis.md` | 本生成パスで使われたリポジトリスナップショット |
| `README.md.auto-readme-support*` | 過去のブートストラップ時に使用されたサポートマニフェスト |

## 🧭 リポジトリワークフローの目標

このリポジトリは意図的に軽量です。長期目標は、技術コンテキスト・リンク・構造を毀損せずに、ルート README と翻訳版を継続的に同期し続けることです。

## 🧰 前提条件

- リポジトリへアクセスするための `git`。
- POSIX シェル（例は `bash`）。
- Markdown 対応エディタ。

### 実行時の前提

本リポジトリのスナップショットでは実行可能な成果物が検出されていないため、ビルド/ランタイム要件は未定義です。

## 📥 インストール

バイナリのインストールやビルド手順はまだありません。

```bash
# リポジトリをクローンする
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ 使い方

現時点での利用は、ドキュメント保守と多言語の整合性維持に集中しています。

### 共通コマンド

```bash
ls -la
ls -la .auto-readme-work/20260301_070633
ls -la i18n
```

### README 同期の一般的なワークフロー

1. `.auto-readme-work/20260301_070633/pipeline-context.md` で実行コンテキストを確認します。
2. `.auto-readme-work/20260301_070633/language-nav-*.md` の言語セレクター用テンプレートを確認します。
3. `README.md` をインクリメンタルに編集し、実質的な既存セクションは削除しません。
4. バナーとサポートブロックは一意に保ち、必要な位置に配置します。
5. 必要に応じて、`i18n/README.*.md` を同一構造へ揃えます。

## ⚙️ 設定

アプリケーション設定はまだありません。リポジトリレベルのドキュメント動作は、`.auto-readme-work/` のワークフロー成果物と `i18n/` のロケールファイルで定義されています。

- `pipeline-context.md`（制約と目標）
- `translation-plan.txt`（ロケール範囲とマッピング）
- `language-nav-root.md` と `language-nav-i18n.md`（ナビゲーション整合）
- `README.md.auto-readme-support*`（スカフォールディングヘルパー）

## 🧪 例

### 例 1: 言語セレクター行の確認

```bash
cat .auto-readme-work/20260301_070633/language-nav-root.md
cat .auto-readme-work/20260301_070633/language-nav-i18n.md
```

### 例 2: 対応ロケールと翻訳ファイルの確認

```bash
cat .auto-readme-work/20260301_070633/translation-plan.txt
```

### 例 3: スキャフォールディング状態の確認

```bash
find . -maxdepth 2 \
  \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

## 🛠️ 開発ノート

- インクリメンタル編集を使って既存の技術文脈を維持します。
- 具体的な成果物が存在しない限り、実行/ビルド手順を追加しないでください。
- バナーとサポートセクションを1つだけ表示されるようにしてください。
- リポジトリの挙動が不明な場合は前提条件を明示します。
- コマンド例は既存のファイルとディレクトリに紐づけてください。

## 🩺 トラブルシューティング

### Markdown ファイルしか見えない

これはこのブートストラップ段階では想定通りです。

### 言語切替の表示が不一致

各 `README.*.md` をルートの言語行と `.auto-readme-work/20260301_070633/` 内の最新パイプラインコンテキストで比較してください。

### 私のブランチが遅れている

```bash
git fetch origin
git pull --ff-only
```

### コード手順を追加したい

具体的なマニフェスト（例: `package.json`、`pyproject.toml`、`Cargo.toml` など）を追加し、資産の存在を確認してから、ビルド/実行コマンドを追加してください。

## 🗺️ ロードマップ

- 具体的なアプリケーション/実行時コンポーネントを導入する。
- コードとツールが存在したら、インストール、実行、デプロイのガイダンスを拡張する。
- Markdown 品質とロケール一致性のための CI チェックを追加する。
- 明示的なバージョン付きパイプラインで翻訳プロセスの再現性を維持する。
- 将来のコード貢献者とドキュメント貢献者の両方向けのガイダンスを追加する。

## 🤝 貢献

コントリビューションを歓迎します。

1. 変更内容を説明した Issue を作成します。
2. 専用ブランチを作成します。
3. 変更は最小限かつインクリメンタルに保ちます。
4. 既存の意味あるセクションを保持します。
5. 簡潔な検証ノート付きで pull request を提出します。

### 推奨フロー

```bash
git checkout -b docs/your-update
# edit README.md and/or i18n/
git add README.md
git commit -m "docs: refine README draft"
git push -u origin docs/your-update
```

## 📄 ライセンス

このリポジトリのスナップショットには、まだライセンスは含まれていません。


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
