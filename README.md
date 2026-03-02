[English](README.md) · [العربية](i18n/README.ar.md) · [Español](i18n/README.es.md) · [Français](i18n/README.fr.md) · [日本語](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [Tiếng Việt](i18n/README.vi.md) · [中文 (简体)](i18n/README.zh-Hans.md) · [中文（繁體）](i18n/README.zh-Hant.md) · [Deutsch](i18n/README.de.md) · [Русский](i18n/README.ru.md)


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

Documentation-first repository scaffold for maintaining a complete English README and synchronized multilingual documentation, guided by three operating principles: **sear creation tools**, **self-healing tools**, and **chain of prompt tools**.

## 🧭 Quick Navigation

| Type | Destination |
| --- | --- |
| Project summary | [Overview](#overview) |
| Core capabilities | [Features](#features) |
| Pipeline design | [Architecture](#architecture) |
| Philosophy baseline | [Philosophy at a glance](#philosophy-at-a-glance) |
| Contributor workflow | [Development Notes](#development-notes) |
| Future direction | [Roadmap](#roadmap) |
| Support this project | [Support](#-support) |

---

## 📌 Scope and Snapshot

| Item | Current state |
| --- | --- |
| Repository phase | Documentation bootstrap scaffold |
| Runtime code | Not detected in current snapshot |
| Tests/CI pipelines | Not detected in current snapshot |
| Localized docs | 10 locale files under `i18n/` |
| Pipeline artifacts | Timestamped runs under `.auto-readme-work/` |
| License file | Not present as standalone file (README badge: TBD) |
| Philosophy baseline | Sear creation + self-healing + chain of prompt tools |

## 🌍 Overview

AgInTi currently operates as a README lifecycle and localization pipeline rather than a runtime application. The root `README.md` is the canonical source, and localized variants in `i18n/` are synchronized from that canonical structure.

The project philosophy is explicit and operational, not decorative. Each README update should satisfy all three principles:

1. **Sear creation tools**: intentionally sharp creation workflows that produce high-signal, practical documentation from constrained repository evidence.
2. **Self-healing tools**: repair-oriented mechanisms that correct drift, remove duplication, and restore structural consistency.
3. **Chain of prompt tools**: staged, traceable prompt flows that preserve context-to-output lineage across pipeline runs.

This repository keeps substantive historical content through incremental updates while preserving links, commands, and support metadata.

### Philosophy at a glance

| Principle | Intent | Operational outcome |
| --- | --- | --- |
| **Sear creation tools** | Produce high-signal documentation from constrained evidence. | Sections stay practical, specific, and repository-grounded. |
| **Self-healing tools** | Repair drift, duplication, and stale structure. | Canonical and localized READMEs remain aligned and clean. |
| **Chain of prompt tools** | Keep generation stages explicit and traceable. | Pipeline artifacts preserve reproducible context and handoffs. |

## ✨ Features

- README-first documentation strategy with a canonical root document.
- Multilingual synchronization across 10 i18n README variants.
- Pipeline-driven authoring via `.auto-readme-work/<run-id>/` artifacts.
- Single-banner and single-support-panel invariants to prevent duplicate visual blocks.
- Incremental-update discipline that preserves meaningful technical history.

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

At this stage, architecture means documentation pipeline architecture, not application runtime architecture.

### Pipeline flow

1. A run-specific context is recorded in `.auto-readme-work/<run-id>/pipeline-context.md`.
2. Language navigation templates are generated (`language-nav-root.md` and `language-nav-i18n.md`).
3. Canonical README content is updated incrementally in `README.md`.
4. Localized README files in `i18n/` are aligned to canonical structure.
5. Structural quality checks enforce deduplication, link consistency, and technical-detail preservation.

### Core principles in architecture

- **Sear creation tools**: applied during content construction to keep sections concrete, complete, and repository-accurate.
- **Self-healing tools**: applied during validation to remove duplicate blocks, repair stale run references, and restore structural parity.
- **Chain of prompt tools**: applied across artifacts so each generation stage remains explicit and auditable.

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
- POSIX shell (examples use `bash`)
- Markdown-capable editor

### Assumptions

- No runnable service or application manifest is present in this repository snapshot.
- Installation/build/start instructions are therefore documentation-workflow oriented.

## 📥 Installation

No binary package or runtime build step is defined yet.

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Usage

Current usage is documentation maintenance and multilingual synchronization.

### Common inspection commands

```bash
ls -la
ls -la .auto-readme-work/20260302_124338
ls -la i18n
```

### Canonical README synchronization workflow

1. Read `.auto-readme-work/20260302_124338/pipeline-context.md`.
2. Verify language selector templates from `language-nav-root.md` and `language-nav-i18n.md`.
3. Update `README.md` incrementally as source of truth.
4. Align `i18n/README.*.md` files with the same structure and key technical details.
5. Confirm there is exactly one banner and exactly one support panel.

## ⚙️ Configuration

No runtime configuration exists yet. Documentation behavior is driven by repository artifacts.

- `pipeline-context.md`: run goals and constraints.
- `repo-structure-analysis.md`: snapshot evidence and gaps.
- `language-nav-root.md` and `language-nav-i18n.md`: navigation consistency.
- `translation-plan.txt`: locale targets and mapping.

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

- Preserve substantive sections and links from canonical README history.
- Prefer incremental edits over destructive rewrites.
- Keep one banner and one support block only.
- Keep root and i18n README structures synchronized.
- Clearly state assumptions whenever runtime or infrastructure details are unknown.
- Apply the philosophy triad as active guardrails:
  - **Sear creation tools** for high-signal drafting.
  - **Self-healing tools** for consistency repair.
  - **Chain of prompt tools** for reproducible handoff between pipeline stages.

## 🚑 Troubleshooting

### I only see Markdown files and pipeline artifacts

That is expected for the current bootstrap phase.

### Language selector lines differ between files

Use the canonical templates in:

- `.auto-readme-work/20260302_124338/language-nav-root.md`
- `.auto-readme-work/20260302_124338/language-nav-i18n.md`

### My branch is behind

```bash
git fetch origin
git pull --ff-only
```

### I want to add runtime instructions

Add build/run instructions only after introducing concrete manifests (for example: `package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`) and confirming paths in this repository.

## 🗺️ Roadmap

1. Strengthen **sear creation tools** with standardized README drafting templates, section quality gates, and clearer evidence-to-output checks.
2. Expand **self-healing tools** with automated checks for duplicate blocks, locale drift, broken internal anchors, and stale run references.
3. Formalize **chain of prompt tools** across run stages for reproducible context, generation, translation, and verification traces.
4. Add a single-command documentation maintenance flow once repo scripts are introduced.
5. Add CI checks for markdown quality, link integrity, and i18n structure parity.
6. Introduce concrete runtime components when source manifests and entrypoints are added.
7. Publish a stable licensing decision and add a standalone license file.

### Roadmap by principle focus

| Focus area | Near-term target |
| --- | --- |
| **Sear creation tools** | Improve drafting templates and evidence-backed section prompts. |
| **Self-healing tools** | Automate duplicate detection, stale anchor checks, and locale drift repair. |
| **Chain of prompt tools** | Standardize run-stage artifact contracts for reproducible multilingual outputs. |

## 🤝 Contribution

Contributions are welcome.

1. Open an issue describing the intended change.
2. Create a focused branch.
3. Keep documentation edits incremental and repository-accurate.
4. Preserve important links, commands, and substantive historical context.
5. Open a pull request with concise verification notes.

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

TBD. A standalone license file is planned but not yet present in the current snapshot.
