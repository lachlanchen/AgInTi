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

Dépôt orienté documentation en priorité, conçu pour maintenir un README anglais complet et une documentation multilingue synchronisée, guidée par trois principes de fonctionnement : **sear creation tools**, **self-healing tools** et **chain of prompt tools**.

## 🧭 Quick Navigation

| Type | Destination |
| --- | --- |
| Résumé du projet | [Overview](#overview) |
| Capacités principales | [Features](#features) |
| Conception du pipeline | [Architecture](#architecture) |
| Base philosophique | [Philosophy at a glance](#philosophy-at-a-glance) |
| Flux contributeur | [Development Notes](#development-notes) |
| Direction future | [Roadmap](#roadmap) |
| Soutenir le projet | [Support](#-support) |

---

## 📌 Scope and Snapshot

| Item | Current state |
| --- | --- |
| Phase du dépôt | Documentation bootstrap scaffold |
| Code d'exécution | Non détecté dans l'instantané actuel |
| Tests/pipelines CI | Non détectés dans l'instantané actuel |
| Docs localisées | 10 fichiers de locale sous `i18n/` |
| Artéfacts pipeline | Exécutions horodatées sous `.auto-readme-work/` |
| Fichier de licence | Absent en fichier autonome (badge README : TBD) |
| Base philosophique | Sear creation + self-healing + chain of prompt tools |

## 🌍 Overview

AgInTi fonctionne actuellement comme un pipeline de cycle de vie README et de localisation, plutôt que comme une application d'exécution. Le `README.md` racine est la source canonique, et les variantes localisées dans `i18n/` sont synchronisées depuis cette structure canonique.

La philosophie du projet est explicite et opérationnelle, pas décorative. Chaque mise à jour du README doit satisfaire les trois principes suivants :

1. **Sear creation tools** : des workflows de création volontairement affûtés qui produisent une documentation pratique et à fort signal à partir d'éléments de dépôt contraints.
2. **Self-healing tools** : des mécanismes orientés réparation qui corrigent les dérives, éliminent les duplications et restaurent la cohérence structurelle.
3. **Chain of prompt tools** : des flux de prompts par étapes et traçables qui préservent la filiation contexte-vers-sortie à travers les exécutions du pipeline.

Ce dépôt conserve le contenu historique substantiel via des mises à jour incrémentales, tout en préservant les liens, commandes et métadonnées de support.

### Philosophy at a glance

| Principle | Intent | Operational outcome |
| --- | --- | --- |
| **Sear creation tools** | Produire une documentation à fort signal depuis des preuves contraintes. | Les sections restent pratiques, spécifiques et ancrées dans le dépôt. |
| **Self-healing tools** | Réparer la dérive, la duplication et les structures obsolètes. | Les README canonique et localisés restent alignés et propres. |
| **Chain of prompt tools** | Garder des étapes de génération explicites et traçables. | Les artéfacts du pipeline conservent un contexte et des relais reproductibles. |

## ✨ Features

- Stratégie documentaire README-first avec un document racine canonique.
- Synchronisation multilingue sur 10 variantes README i18n.
- Rédaction pilotée par pipeline via les artéfacts `.auto-readme-work/<run-id>/`.
- Invariants « une seule bannière » et « un seul panneau de support » pour éviter les blocs visuels dupliqués.
- Discipline de mise à jour incrémentale qui préserve l'historique technique utile.

### Principle-to-feature mapping

| Core principle | How it appears in current features |
| --- | --- |
| **Sear creation tools** | Rédaction README précise à partir de preuves ancrées dépôt et de gabarits de section stables. |
| **Self-healing tools** | Vérifications de déduplication pour blocs bannière/support répétés, références obsolètes et dérive structurelle. |
| **Chain of prompt tools** | Chaîne d'artéfacts spécifique à l'exécution (`pipeline-context`, modèles de navigation, plan de traduction) pour une sortie reproductible. |

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

À ce stade, l'architecture signifie l'architecture du pipeline de documentation, et non une architecture d'exécution applicative.

### Pipeline flow

1. Un contexte spécifique à l'exécution est enregistré dans `.auto-readme-work/<run-id>/pipeline-context.md`.
2. Les modèles de navigation linguistique sont générés (`language-nav-root.md` et `language-nav-i18n.md`).
3. Le contenu README canonique est mis à jour de manière incrémentale dans `README.md`.
4. Les fichiers README localisés dans `i18n/` sont alignés sur la structure canonique.
5. Des contrôles qualité structurels imposent la déduplication, la cohérence des liens et la préservation des détails techniques.

### Core principles in architecture

- **Sear creation tools** : appliqué pendant la construction du contenu pour garder des sections concrètes, complètes et fidèles au dépôt.
- **Self-healing tools** : appliqué pendant la validation pour supprimer les blocs dupliqués, corriger les références d'exécution obsolètes et restaurer la parité structurelle.
- **Chain of prompt tools** : appliqué à travers les artéfacts pour que chaque étape de génération reste explicite et auditable.

### Principle checkpoints by pipeline stage

| Stage | Sear creation tools | Self-healing tools | Chain of prompt tools |
| --- | --- | --- | --- |
| Context capture | Définir des contraintes de génération nettes. | Signaler tôt les entrées manquantes/invalides. | Préserver le prompt source et les métadonnées d'exécution. |
| Canonical drafting | Construire des sections README complètes depuis les preuves du dépôt. | Éviter les régressions et les pertes de contenu accidentelles. | Garder les sorties d'étape liées aux artéfacts précédents. |
| i18n alignment | Maintenir structure et parité technique entre locales. | Corriger la dérive entre fichiers racine et i18n. | Porter l'intention canonique dans chaque variante localisée. |
| Final verification | Imposer lisibilité et préservation des détails. | Supprimer bannière/support dupliqués et références obsolètes. | Laisser une trace d'artéfacts auditable pour l'exécution. |

## 🧾 Documentation Inputs and Generated Artifacts

| File | Purpose |
| --- | --- |
| `.auto-readme-work/20260302_124338/pipeline-context.md` | Contraintes source et objectifs pour cette passe de génération. |
| `.auto-readme-work/20260302_124338/repo-structure-analysis.md` | Résumé du scan du dépôt et état technique inféré. |
| `.auto-readme-work/20260302_124338/language-nav-root.md` | Ligne canonique d'options de langue pour `README.md` racine. |
| `.auto-readme-work/20260302_124338/language-nav-i18n.md` | Ligne canonique d'options de langue pour les README i18n. |
| `.auto-readme-work/20260302_124338/translation-plan.txt` | Mapping des locales et plan des fichiers i18n cibles. |
| `.auto-readme-work/<older-run-id>/...` | Contexte historique d'exécution pour les passes pipeline README précédentes. |

## 🔧 Prerequisites

- `git`
- Shell POSIX (les exemples utilisent `bash`)
- Éditeur compatible Markdown

### Assumptions

- Aucun service exécutable ou manifeste applicatif n'est présent dans cet instantané du dépôt.
- Les instructions d'installation/build/start sont donc orientées workflow documentaire.

## 📥 Installation

Aucun package binaire ni étape de build d'exécution n'est encore défini.

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Usage

L'usage actuel concerne la maintenance documentaire et la synchronisation multilingue.

### Common inspection commands

```bash
ls -la
ls -la .auto-readme-work/20260302_124338
ls -la i18n
```

### Canonical README synchronization workflow

1. Lire `.auto-readme-work/20260302_124338/pipeline-context.md`.
2. Vérifier les modèles de sélecteur de langue depuis `language-nav-root.md` et `language-nav-i18n.md`.
3. Mettre à jour `README.md` de façon incrémentale comme source de vérité.
4. Aligner les fichiers `i18n/README.*.md` sur la même structure et les mêmes détails techniques clés.
5. Confirmer qu'il y a exactement une bannière et exactement un panneau de support.

## ⚙️ Configuration

Aucune configuration d'exécution n'existe encore. Le comportement documentaire est piloté par les artéfacts du dépôt.

- `pipeline-context.md` : objectifs et contraintes d'exécution.
- `repo-structure-analysis.md` : preuves d'instantané et écarts.
- `language-nav-root.md` et `language-nav-i18n.md` : cohérence de navigation.
- `translation-plan.txt` : cibles de locales et mapping.

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

- Préserver les sections substantielles et les liens issus de l'historique README canonique.
- Préférer des modifications incrémentales plutôt que des réécritures destructrices.
- Conserver une seule bannière et un seul bloc de support.
- Garder les structures README racine et i18n synchronisées.
- Énoncer clairement les hypothèses lorsque des détails d'exécution ou d'infrastructure sont inconnus.
- Appliquer le triptyque philosophique comme garde-fou actif :
  - **Sear creation tools** pour une rédaction à fort signal.
  - **Self-healing tools** pour la réparation de cohérence.
  - **Chain of prompt tools** pour un relais reproductible entre étapes pipeline.

## 🚑 Troubleshooting

### I only see Markdown files and pipeline artifacts

C'est attendu pour la phase bootstrap actuelle.

### Language selector lines differ between files

Utiliser les modèles canoniques dans :

- `.auto-readme-work/20260302_124338/language-nav-root.md`
- `.auto-readme-work/20260302_124338/language-nav-i18n.md`

### My branch is behind

```bash
git fetch origin
git pull --ff-only
```

### I want to add runtime instructions

Ajouter des instructions build/run uniquement après avoir introduit des manifestes concrets (par exemple : `package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`) et confirmé les chemins dans ce dépôt.

## 🗺️ Roadmap

1. Renforcer **sear creation tools** avec des gabarits standardisés de rédaction README, des garde-fous qualité par section et des contrôles plus clairs preuve-vers-sortie.
2. Étendre **self-healing tools** avec des vérifications automatisées des blocs dupliqués, de la dérive de locales, des ancres internes cassées et des références d'exécution obsolètes.
3. Formaliser **chain of prompt tools** entre les étapes d'exécution pour des traces reproductibles de contexte, génération, traduction et vérification.
4. Ajouter un flux de maintenance documentaire en une seule commande dès l'introduction de scripts du dépôt.
5. Ajouter des contrôles CI pour la qualité Markdown, l'intégrité des liens et la parité structurelle i18n.
6. Introduire des composants d'exécution concrets lorsque les manifestes source et points d'entrée seront ajoutés.
7. Publier une décision de licence stable et ajouter un fichier de licence autonome.

### Roadmap by principle focus

| Focus area | Near-term target |
| --- | --- |
| **Sear creation tools** | Améliorer les gabarits de rédaction et les prompts de section appuyés sur des preuves. |
| **Self-healing tools** | Automatiser la détection de doublons, les vérifications d'ancres obsolètes et la réparation de dérive des locales. |
| **Chain of prompt tools** | Standardiser les contrats d'artéfacts par étape d'exécution pour des sorties multilingues reproductibles. |

## 🤝 Contribution

Les contributions sont bienvenues.

1. Ouvrir une issue décrivant le changement visé.
2. Créer une branche ciblée.
3. Garder des modifications documentaires incrémentales et fidèles au dépôt.
4. Préserver les liens, commandes et contexte historique substantiel importants.
5. Ouvrir une pull request avec des notes de vérification concises.

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

TBD. Un fichier de licence autonome est prévu, mais n'est pas encore présent dans l'instantané actuel.
