[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Repository](https://img.shields.io/badge/Repository-AgInTi-0f172a?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lachlanchen/AgInTi)
[![Docs](https://img.shields.io/badge/Docs-README%20Bootstrap-0ea5e9?style=for-the-badge&logo=mdbook&logoColor=white)](#aginti)
[![Localization](https://img.shields.io/badge/i18n-10%20locales-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)](#documentation-inputs-and-generated-artifacts)
[![Status](https://img.shields.io/badge/Stage-Documentation%20Pipeline-f59e0b?style=for-the-badge&logo=githubactions&logoColor=white)](#scope-and-snapshot)
[![License](https://img.shields.io/badge/License-TBD-94a3b8?style=for-the-badge&logo=readme&logoColor=white)](#license)

Référentiel de documentation-first pour maintenir un README principal en anglais complet et une documentation multilingue synchronisée.

## 🧭 Navigation rapide

| Type | Destination |
|---|---|
| Flux du dépôt | [Portée et instantané](#-scope-and-snapshot) |
| Cas d'utilisation | [Utilisation](#-usage) |
| Guide de contribution | [Contribution](#-contribution) |
| Soutien au projet | [Support](#-support) |

---

[![Pipeline](https://img.shields.io/badge/Pipeline-.auto--readme--work-0f172a?style=flat-square&logo=githubactions&logoColor=white)](./.auto-readme-work)
[![Locales](https://img.shields.io/badge/Locales-10%20files-22c55e?style=flat-square&logo=googletranslate&logoColor=white)](./i18n)
[![Scope](https://img.shields.io/badge/Scope-Documentation-0ea5e9?style=flat-square&logo=mdbook&logoColor=white)](#documentation-inputs-and-generated-artifacts)

## 📌 Vue d'ensemble

| 🎯 Focus | 🧩 Valeur actuelle |
| --- | --- |
| Objectif du dépôt | Scaffolding de documentation pour synchronisation multilingue des README |
| Invariant central | Les mises à jour incrémentielles préservent l'historique de fond |
| État actuel | Aucun runtime/app détecté dans l'instantané du dépôt |

| ✅ Snapshot | 📌 État actuel |
| --- | --- |
| Phase du dépôt | Scaffolding de démarrage piloté par `.auto-readme-work/` |
| Localisations | 10 variantes de README traduites |
| Runtime vérifié | Aucun runtime exécutable détecté |

## 📌 Présentation

AgInTi est un dépôt de **documentation-bootstrap**.

Le dépôt se concentre sur la documentation-first, l’ossature de localisations et les artefacts de workflow itératif utilisés pour générer une documentation multilingue cohérente.

- ✅ Aucun arbre de code source principal n'est détecté actuellement.
- ✅ `i18n/` contient 10 variantes de README traduites.
- ✅ `.auto-readme-work/` stocke les artefacts de pipeline pour des mises à jour de documentation incrémentielles.
- ✅ Le contenu substantiel existant est préservé via des mises à jour incrémentielles.

## ✅ Portée et instantané

| Élément | État actuel |
|---|---|
| 🧩 Code source | Non détecté |
| 🧪 Tests/CI | Non détecté |
| 📘 Workflow documentaire | Piloté par `.auto-readme-work/` |
| 🌐 Docs localisées | 10 locales maintenues |
| 🔒 Fichier de licence | Non présent dans cet instantané |

## ✨ Fonctionnalités

- Stratégie de documentation centrée sur le README-first.
- Workflow sensible aux langues avec liens canoniques pour la page racine et les pages localisées.
- Blocs de bannière et de support dédupliqués à des positions définies.
- Mises à jour incrémentielles qui préservent les sections substantielles.
- Extraits de vérification pratiques pour les contributeurs à la documentation.

## 🗂️ Structure du projet

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

## 🧱 Modèle d'architecture et de workflow

À ce stade, « architecture » correspond au pipeline de documentation du dépôt :

1. Le contexte et les contraintes sont produits à chaque exécution dans `.auto-readme-work/<run-id>/pipeline-context.md`.
2. Les modèles de sélecteur de langue sont produits dans `language-nav-root.md` / `language-nav-i18n.md`.
3. Les modifications du README sont appliquées de manière incrémentielle pour garder intacte l'histoire substantielle.
4. Les fichiers localisés sont synchronisés depuis le même modèle structurel.

## 📚 Entrées de documentation et artefacts générés

| Fichier | Objectif |
|---|---|
| `.auto-readme-work/20260301_070633/pipeline-context.md` | Contraintes et instructions pour cette passe. |
| `.auto-readme-work/20260301_070633/translation-plan.txt` | Cartographie des locales pour la synchronisation multilingue. |
| `.auto-readme-work/20260301_070633/language-nav-root.md` | Ligne de navigation des langues canonique pour `README.md`. |
| `.auto-readme-work/20260301_070633/language-nav-i18n.md` | Ligne de navigation des langues canonique pour les READMEs traduits. |
| `.auto-readme-work/20260301_070633/repo-structure-analysis.md` | Instantané du dépôt utilisé pour ce cycle de génération. |
| `README.md.auto-readme-support*` | Manifestes de support auxiliaires utilisés lors des passages précédents du bootstrap. |

## 🧭 Objectifs du workflow du dépôt

Ce dépôt est volontairement minimal. L'objectif à long terme est de garder le README racine et les variantes traduites synchronisés sans régression de contexte technique, de liens et de structure.

## 🧰 Prérequis

- `git` pour l'accès au dépôt.
- Un shell POSIX (les exemples utilisent `bash`).
- Un éditeur Markdown-aware.

### Hypothèses d'exécution

Aucune exigence de build/runtime n'est encore définie car aucun manifeste de produit exécutable n'a été détecté dans cet instantané de dépôt.

## 📥 Installation

Aucun processus d'installation binaire ou de build n'existe pour l'instant.

```bash
# Clone the repository
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Utilisation

L'utilisation actuelle se concentre sur la maintenance de la documentation et la cohérence multilingue.

### Commandes courantes

```bash
ls -la
ls -la .auto-readme-work/20260301_070633
ls -la i18n
```

### Workflow typique de synchronisation du README

1. Consultez le contexte d'exécution dans `.auto-readme-work/20260301_070633/pipeline-context.md`.
2. Vérifiez les modèles de sélecteur de langue dans `.auto-readme-work/20260301_070633/language-nav-*.md`.
3. Modifiez `README.md` de manière incrémentielle ; ne supprimez pas les sections substantielles.
4. Gardez les blocs de bannière et de support uniques et placés aux positions requises.
5. Alignez les fichiers localisés sous `i18n/README.*.md` à la même structure si nécessaire.

## ⚙️ Configuration

Aucune configuration applicative n'existe encore. Le comportement documentaire du dépôt est défini par les artefacts de workflow dans `.auto-readme-work/` et les fichiers de locale dans `i18n/`.

- `pipeline-context.md` (contraintes et objectifs)
- `translation-plan.txt` (étendue et mappage des locales)
- `language-nav-root.md` et `language-nav-i18n.md` (cohérence de navigation)
- `README.md.auto-readme-support*` (assistants de scaffold)

## 🧪 Exemples

### Exemple 1 : Vérifier les lignes du sélecteur de langue

```bash
cat .auto-readme-work/20260301_070633/language-nav-root.md
cat .auto-readme-work/20260301_070633/language-nav-i18n.md
```

### Exemple 2 : Valider les locales prises en charge et les fichiers de traduction

```bash
cat .auto-readme-work/20260301_070633/translation-plan.txt
```

### Exemple 3 : Confirmer l'état du scaffold

```bash
find . -maxdepth 2 \
  \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

## 🛠️ Notes de développement

- Utilisez des modifications incrémentielles pour préserver le contexte technique existant.
- N'ajoutez pas d'étapes d'installation/build tant que des manifestes concrets ne sont pas présents.
- Assurez-vous que les sections banner et support n'apparaissent qu'une seule fois.
- Énoncez vos hypothèses quand le comportement du dépôt est inconnu.
- Conservez les exemples de commandes liés à des fichiers et répertoires existants.

## 🩺 Dépannage

### Je ne vois que des fichiers markdown

C'est normal dans cette phase de bootstrap.

### Le sélecteur de langue semble incohérent

Comparez chaque `README.*.md` avec la ligne de langues principale et les derniers fichiers de contexte de pipeline dans `.auto-readme-work/20260301_070633/`.

### Ma branche est en retard

```bash
git fetch origin
git pull --ff-only
```

### Je veux ajouter des instructions de code

Ajoutez uniquement des commandes de build/exécution après avoir ajouté des manifestes concrets (par exemple `package.json`, `pyproject.toml`, `Cargo.toml`, etc.) et confirmé la présence de ces actifs dans le dépôt.

## 🗺️ Feuille de route

- Introduire des composants concrets d'application/runtime.
- Étendre les guides d'installation, d'exécution et de déploiement une fois que le code et les outils existeront.
- Ajouter des contrôles CI pour la qualité Markdown et la parité des locales.
- Garder le processus de traduction reproductible via des pipelines versionnés explicites.
- Ajouter des recommandations de contribution pour la documentation et les futurs contributeurs au code.

## 🤝 Contribution

Les contributions sont les bienvenues.

1. Ouvrez un ticket décrivant le changement.
2. Créez une branche dédiée.
3. Gardez les changements minimaux et incrémentiels.
4. Préservez les sections existantes pertinentes.
5. Soumettez une pull request avec des notes de vérification concises.

### Flux suggéré

```bash
git checkout -b docs/your-update
# edit README.md et/ou i18n/
git add README.md
git commit -m "docs: refine README draft"
git push -u origin docs/your-update
```

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 📄 License

La licence n'est pas encore incluse dans l'instantané de ce dépôt.
