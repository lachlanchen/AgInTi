[English](README.md) · [العربية](i18n/README.ar.md) · [Español](i18n/README.es.md) · [Français](i18n/README.fr.md) · [日本語](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [Tiếng Việt](i18n/README.vi.md) · [中文 (简体)](i18n/README.zh-Hans.md) · [中文（繁體）](i18n/README.zh-Hant.md) · [Deutsch](i18n/README.de.md) · [Русский](i18n/README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Status](https://img.shields.io/badge/status-initializing-orange)](#aginti)
[![Docs](https://img.shields.io/badge/docs-readme_draft-blue)](#aginti)
[![Repository%20Stage](https://img.shields.io/badge/stage-bootstrap-yellow)](#aginti)
[![i18n](https://img.shields.io/badge/i18n-planned-0ea5e9)](#aginti)
[![License](https://img.shields.io/badge/license-TBD-lightgrey)](#aginti)

*Documentation-first bootstrap repository • README-first workflow • active multilingual planning.*

| Focus | Current state |
|---|---|
| Core maturity | Bootstrap scaffold (`README`-first) |
| Localization | 10 locales maintained in `i18n/` |
| Pipeline source | `.auto-readme-work/20260301_064213/` |

---

## 📌 Overview

AgInTi is currently a documentation-scaffold repository with a README-first workflow and multilingual documentation planning.

At the time of this draft, repository contents are focused on documentation coordination and language preparation, not yet on a runtime product:

- ✅ No top-level source tree is detected yet.
- ✅ `i18n/` contains translated README variants.
- ✅ `.auto-readme-work/20260301_064213/` stores the active pipeline context for this pass.
- ✅ `.auto-readme-work/20260228_184104/` is retained as a historical artifact.

### Repository snapshot

| Item | Current state |
|---|---|
| 🧩 Source code | Not detected yet |
| ⚙️ Runtime manifests | Not detected yet |
| 🧪 CI workflows | Not detected yet |
| 🧭 Documentation workspace | `.auto-readme-work/20260301_064213/` |
| 🌐 Translated docs | 10 locales in `i18n/` |

---

## 🚦 Project status

This README is an increment-only, repository-accurate first complete English draft.

- State remains bootstrap/documentation oriented.
- Substantive existing sections have been preserved and expanded rather than replaced.
- Unknowns are explicitly marked and avoid speculative claims.

If a canonical upstream README exists in a different branch or history, future updates should merge it incrementally.

---

## ✨ Features

- Documentation-first repository layout
- Centralized multilingual README pipeline under `.auto-readme-work/`
- Explicit language switcher templates and translation mapping files
- Practical command snippets for repository inspection and validation
- Strictly tracked README update process with deduplication of support/banner blocks

---

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

| File | Purpose |
|---|---|
| `.auto-readme-work/20260301_064213/pipeline-context.md` | Generation constraints and prompt context for this run. |
| `.auto-readme-work/20260301_064213/repo-structure-analysis.md` | Snapshot of detected structure and project gaps. |
| `.auto-readme-work/20260301_064213/translation-plan.txt` | Locale-to-file mapping for translated variants. |
| `.auto-readme-work/20260301_064213/language-nav-root.md` | Canonical language selector line for `README.md`. |
| `.auto-readme-work/20260301_064213/language-nav-i18n.md` | Canonical language selector line for `i18n/` files. |

---

## 🧰 Prerequisites

No runtime dependencies are required for the current repository state.

For documentation usage and maintenance, you need:

- `git`
- A POSIX shell (examples use `bash`)
- A text editor for Markdown updates

---

## 📥 Installation

There is no install/build process yet.

To inspect the repository locally:

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Usage

Current usage is documentation maintenance, auditing, and localization synchronization.

### Common workflows

```bash
ls -la
ls -la .auto-readme-work/20260301_064213
ls -la i18n
```

### Typical README workflow

1. Read the current context artifacts in `.auto-readme-work/20260301_064213/`.
2. Review source and translated README content.
3. Apply incremental edits to avoid removing existing substantive details.
4. Keep language switcher and support blocks consistent across locales.

---

## ⚙️ Configuration

No application configuration file is present yet.

Current documentation-level configuration is represented by:

- `.auto-readme-work/20260301_064213/translation-plan.txt` for locale targets
- Language switcher templates in `.auto-readme-work/20260301_064213/language-nav-root.md` and `.../language-nav-i18n.md`
- Repo structure context in `.auto-readme-work/20260301_064213/repo-structure-analysis.md`

---

## 🧪 Examples

### Example 1: Verify language switcher lines

```bash
cat .auto-readme-work/20260301_064213/language-nav-root.md
cat .auto-readme-work/20260301_064213/language-nav-i18n.md
```

### Example 2: Confirm translation scope

```bash
cat .auto-readme-work/20260301_064213/translation-plan.txt
```

### Example 3: Confirm scaffold state (expected: no manifests)

```bash
find . -maxdepth 2 \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

---

## 🛠️ Development notes

- Maintain this file as the canonical English documentation source.
- Preserve substantive sections when updating (increment-only editing policy).
- Add runtime instructions only when corresponding code, manifests, and toolchains exist.
- Keep support and banner blocks deduplicated (exactly one each).
- Update roadmap and troubleshooting as soon as functionality lands.

---

## 🩺 Troubleshooting

### I only see documentation files

That is expected in this bootstrap state; no source/runtime manifests were detected.

### Locale documentation is inconsistent

Use the latest translation plan and rerun your README sync flow to normalize structure and links.

### Local branch feels outdated

```bash
git fetch origin
git pull --ff-only
```

---

## 🗺️ Roadmap

- Add the concrete product/application layer when code is introduced.
- Expand setup, build, and run instructions from real manifests.
- Add CI workflows and docs checks.
- Extend contribution standards for code and translations.
- Keep translated READMEs synchronized and current.

---

## 🤝 Contribution

Contributions are welcome.

1. Open an issue with context and scope.
2. Create a dedicated branch.
3. Keep edits focused and incremental.
4. Preserve existing technical details and section context.
5. Open a PR with clear verification notes.

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

No `LICENSE` file is present yet.

- Status: `TBD`
- Recommended next step: add a license file and set SPDX identifier here.

## 🧾 Assumptions and preservation notes

- Repository content was evaluated from `/home/lachlan/ProjectsLFS/AgInTi` during this run.
- Runtime goals and architecture are not represented in committed files yet; this draft intentionally focuses on documented facts.
- Existing substantive sections from the prior draft were retained and expanded where useful.
- The banner and support blocks were inserted once each to satisfy the requested positions.
