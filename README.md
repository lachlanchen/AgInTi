[English](README.md) · [العربية](i18n/README.ar.md) · [Español](i18n/README.es.md) · [Français](i18n/README.fr.md) · [日本語](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [Tiếng Việt](i18n/README.vi.md) · [中文 (简体)](i18n/README.zh-Hans.md) · [中文（繁體）](i18n/README.zh-Hant.md) · [Deutsch](i18n/README.de.md) · [Русский](i18n/README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Repository](https://img.shields.io/badge/Repository-AgInTi-0f172a?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lachlanchen/AgInTi)
[![Docs](https://img.shields.io/badge/Docs-README%20Bootstrap-0ea5e9?style=for-the-badge&logo=mdbook&logoColor=white)](#aginti)
[![Localization](https://img.shields.io/badge/i18n-10%20locales-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)](#documentation-inputs-and-generated-artifacts)
[![Status](https://img.shields.io/badge/Stage-Documentation%20Pipeline-f59e0b?style=for-the-badge&logo=githubactions&logoColor=white)](#scope-and-snapshot)
[![License](https://img.shields.io/badge/License-TBD-94a3b8?style=for-the-badge&logo=readme&logoColor=white)](#license)

Documentation-first repository scaffold for maintaining a complete English README and synchronized multilingual documentation.

## 🧭 Quick navigation

| Type | Destination |
|---|---|
| Repository workflow | [Scope and snapshot](#-scope-and-snapshot) |
| Usage examples | [Usage](#-usage) |
| Contribution guide | [Contribution](#-contribution) |
| Support this project | [Support](#-support) |

---

[![Pipeline](https://img.shields.io/badge/Pipeline-.auto--readme--work-0f172a?style=flat-square&logo=githubactions&logoColor=white)](./.auto-readme-work)
[![Locales](https://img.shields.io/badge/Locales-10%20files-22c55e?style=flat-square&logo=googletranslate&logoColor=white)](./i18n)
[![Scope](https://img.shields.io/badge/Scope-Documentation-0ea5e9?style=flat-square&logo=mdbook&logoColor=white)](#documentation-inputs-and-generated-artifacts)

## 📌 At a glance

| 🎯 Focus | 🧩 Current value |
| --- | --- |
| Repository purpose | Documentation bootstrap for multilingual README synchronization |
| Core invariant | Incremental edits preserve substantive history |
| Current state | No runtime app/service detected in repository snapshot |

---

| ✅ Snapshot | 📌 Current state |
| --- | --- |
| Repository phase | Bootstrap scaffold driven by `.auto-readme-work/` |
| Localizations | 10 translated README variants |
| Verified runtime | No runnable app or service detected |

## 📌 Overview

AgInTi is a **documentation-bootstrap** repository.

The repository focuses on README-first documentation, localization scaffolding, and iterative workflow artifacts used to generate consistent multilingual documentation.

- ✅ No top-level runtime source tree is detected yet.
- ✅ `i18n/` contains 10 translated README variants.
- ✅ `.auto-readme-work/` stores pipeline artifacts for iterative documentation updates.
- ✅ Existing content is preserved using incremental updates.

## ✅ Scope and snapshot

| Item | Current state |
|---|---|
| 🧩 Source code | Not detected |
| 🧪 Tests/CI | Not detected |
| 📘 Documentation workflow | `.auto-readme-work/` driven |
| 🌐 Localized docs | 10 locales maintained |
| 🔒 License file | Not present in this snapshot |

## ✨ Features

- README-first repository documentation strategy.
- Language-aware workflow with canonical links for root and localized pages.
- Deduplicated banner and support blocks at defined positions.
- Incremental updates that preserve substantive sections.
- Practical inspection and verification snippets for documentation contributors.

## 🗂️ Project structure

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

## 🧱 Architecture and workflow model

At this stage, “architecture” is the repository’s documentation pipeline:

1. Context and constraints are produced per run in `.auto-readme-work/<run-id>/pipeline-context.md`.
2. Language navigator templates are produced in `language-nav-root.md` / `language-nav-i18n.md`.
3. README edits are applied incrementally to keep substantive history intact.
4. Localized files are synchronized from the same structural template.

## 📚 Documentation inputs and generated artifacts

| File | Purpose |
|---|---|
| `.auto-readme-work/20260301_070633/pipeline-context.md` | Source constraints and instructions for this pass. |
| `.auto-readme-work/20260301_070633/translation-plan.txt` | Locale mapping for multilingual synchronization. |
| `.auto-readme-work/20260301_070633/language-nav-root.md` | Canonical language navigation line for `README.md`. |
| `.auto-readme-work/20260301_070633/language-nav-i18n.md` | Canonical language navigation line for translated READMEs. |
| `.auto-readme-work/20260301_070633/repo-structure-analysis.md` | Repository snapshot used for this generation pass. |
| `README.md.auto-readme-support*` | Auxiliary support manifests used during prior bootstrap passes. |

## 🧭 Repository workflow goals

This repository is intentionally thin by design. The long-term objective is to keep the root README and translated variants synchronized without regressing technical context, links, and structure.

## 🧰 Prerequisites

- `git` for repository access.
- A POSIX shell (examples use `bash`).
- A Markdown-aware editor.

### Runtime assumptions

No build/runtime requirements are defined yet because no runnable product manifests were detected in this repository snapshot.

## 📥 Installation

There is no binary install or build process yet.

```bash
# Clone the repository
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Usage

Current usage focuses on documentation maintenance and multilingual consistency.

### Common commands

```bash
ls -la
ls -la .auto-readme-work/20260301_070633
ls -la i18n
```

### Typical README sync workflow

1. Review run context in `.auto-readme-work/20260301_070633/pipeline-context.md`.
2. Check language switcher templates in `.auto-readme-work/20260301_070633/language-nav-*.md`.
3. Edit `README.md` incrementally; do not remove substantive historical sections.
4. Keep banner and support blocks unique and in required positions.
5. Align translated files under `i18n/README.*.md` to the same structure where needed.

## ⚙️ Configuration

No application configuration exists yet. Repository-level documentation behavior is defined by workflow artifacts in `.auto-readme-work/` and locale files in `i18n/`.

- `pipeline-context.md` (constraints and goals)
- `translation-plan.txt` (locale scope and mapping)
- `language-nav-root.md` and `language-nav-i18n.md` (navigation consistency)
- `README.md.auto-readme-support*` (scaffolding helpers)

## 🧪 Examples

### Example 1: Check language selector lines

```bash
cat .auto-readme-work/20260301_070633/language-nav-root.md
cat .auto-readme-work/20260301_070633/language-nav-i18n.md
```

### Example 2: Validate supported locales and translation files

```bash
cat .auto-readme-work/20260301_070633/translation-plan.txt
```

### Example 3: Confirm scaffold status

```bash
find . -maxdepth 2 \
  \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

## 🛠️ Development notes

- Use increment-only edits to preserve prior technical context.
- Do not add runtime installation/build steps unless concrete manifest files are present.
- Ensure banner and support sections appear only once.
- State assumptions when repository behavior is unknown.
- Keep command examples tied to existing files and directories.

## 🩺 Troubleshooting

### I only see markdown files

That is expected in this bootstrap stage.

### Language switcher looks inconsistent

Compare each `README.*.md` against the root language line and the latest pipeline context files in `.auto-readme-work/20260301_070633/`.

### My branch is behind

```bash
git fetch origin
git pull --ff-only
```

### I want to add code instructions

Only add build/run commands after adding concrete manifests (for example `package.json`, `pyproject.toml`, `Cargo.toml`, etc.) and confirming those assets exist in the repository.

## 🗺️ Roadmap

- Introduce concrete application/runtime components.
- Expand installation, runtime, and deployment guidance once code and tooling exist.
- Add CI checks for markdown quality and locale parity.
- Keep translation process reproducible via explicit versioned pipelines.
- Add contribution guidance for both documentation and future code contributors.

## 🤝 Contribution

Contributions are welcome.

1. Create an issue describing the change.
2. Open a dedicated branch.
3. Keep changes minimal and incremental.
4. Preserve existing meaningful sections.
5. Submit a pull request with concise verification notes.

### Suggested flow

```bash
git checkout -b docs/your-update
# edit README.md and/or i18n/
git add README.md
git commit -m "docs: refine README draft"
git push -u origin docs/your-update
```

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 📄 License

License is not yet included in this repository snapshot.
