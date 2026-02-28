[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# AgInTi

[![Status](https://img.shields.io/badge/status-initializing-orange)](#aginti)
[![Docs](https://img.shields.io/badge/docs-readme_draft-blue)](#aginti)
[![Repository Stage](https://img.shields.io/badge/stage-bootstrap-yellow)](#aginti)
[![i18n](https://img.shields.io/badge/i18n-planned-0ea5e9)](#aginti)
[![License](https://img.shields.io/badge/license-TBD-lightgrey)](#aginti)

## 📌 Vue d'ensemble

AgInTi est actuellement dans une phase d'initialisation/de structuration. Au moment de cette version brouillon du README, le dépôt contient principalement :

- Des métadonnées Git (`.git/`)
- Un répertoire `i18n/` préparé pour les fichiers README multilingues
- Un espace de travail `.auto-readme-work/` contenant le contexte du pipeline de génération du README et des artefacts de planification linguistique

Aucun code source applicatif, manifeste de package, point d'entrée d'exécution ou workflow CI n'a été détecté dans l'arborescence actuelle.

### Instantané du dépôt

| Élément | État actuel |
| --- | --- |
| Code source | Non détecté pour le moment |
| Manifestes d'exécution | Non détectés pour le moment |
| Workflows CI | Non détectés pour le moment |
| Espace de travail de documentation | `.auto-readme-work/20260228_184104/` |
| Répertoire i18n | Présent (`i18n/`) |

## 🚦 État du projet

Il s'agit du **premier brouillon README complet** pour ce dépôt.

- État du dépôt observé : **pas encore d'arborescence source au niveau racine**
- Base README canonique existante : **non présente dans l'espace de travail local pendant cette exécution**
- Approche documentaire utilisée ici : conserver tous les détails exacts détectés dans le dépôt et signaler clairement les inconnues plutôt que supprimer ou inventer du contenu

Si un README canonique historique existe dans une branche/historique distant, ce brouillon doit être fusionné progressivement avec ce contenu plutôt que de remplacer des sections substantielles.

## ✨ Fonctionnalités (actuelles)

Les capacités actuelles du dépôt sont orientées documentation/pipeline :

- Espace de travail du pipeline de génération de README sous `.auto-readme-work/`
- Planification des README multilingues (11 langues, anglais inclus)
- Modèles de navigation linguistique à la racine et dans `i18n/`

Les fonctionnalités produit/exécution prévues sont inconnues à ce stade.

## 🗂️ Structure du projet

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

### Entrées de documentation clés

| Fichier | Rôle |
| --- | --- |
| `.auto-readme-work/20260228_184104/pipeline-context.md` | Définit les contraintes README et le contexte du workflow de génération pour cette exécution. |
| `.auto-readme-work/20260228_184104/repo-structure-analysis.md` | Résume la structure du dépôt détectée et les lacunes connues. |
| `.auto-readme-work/20260228_184104/language-nav-root.md` | Ligne canonique de sélecteur de langue pour le `README.md` racine. |
| `.auto-readme-work/20260228_184104/language-nav-i18n.md` | Ligne canonique de sélecteur de langue pour les fichiers traduits sous `i18n/`. |
| `.auto-readme-work/20260228_184104/translation-plan.txt` | Correspondance locale-vers-fichier pour les traductions. |

## 🧰 Prérequis

Aucun prérequis d'exécution n'est actuellement nécessaire pour utiliser le contenu du dépôt en l'état.

Pour le workflow de documentation et les opérations sur le dépôt, vous aurez probablement besoin de :

- `git`
- Un shell compatible POSIX (les exemples utilisent `bash`)
- Un éditeur de texte

## 📥 Installation

Comme aucun manifeste d'application/package n'est encore présent, il n'y a pas d'étape d'installation/de build.

Clonez le dépôt :

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Utilisation

L'utilisation pratique actuelle consiste à inspecter le dépôt et à travailler sur la documentation README/i18n.

Exemples :

```bash
# Show top-level files
ls -la

# Inspect auto-generated README context files
ls -la .auto-readme-work/20260228_184104

# Inspect i18n directory
ls -la i18n
```

## ⚙️ Configuration

Aucun fichier de configuration applicative n'est actuellement détecté.

Signaux de configuration connus du dépôt :

- Remote Git configuré comme `origin git@github.com:lachlanchen/AgInTi.git`
- Navigation README multilingue et correspondances des locales cibles dans `.auto-readme-work/20260228_184104/`

## 🧪 Exemples

### Exemple 1 : valider la cohérence de navigation linguistique du README

```bash
# Compare language switcher templates used by the pipeline
cat .auto-readme-work/20260228_184104/language-nav-root.md
cat .auto-readme-work/20260228_184104/language-nav-i18n.md
```

### Exemple 2 : confirmer l'ensemble des cibles de traduction

```bash
cat .auto-readme-work/20260228_184104/translation-plan.txt
```

### Exemple 3 : vérifier que le dépôt n'a pas encore de manifestes d'exécution

```bash
# Typical manifest check (expected: none in current state)
find . -maxdepth 2 \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml \)
```

## 🛠️ Notes de développement

- Le dépôt semble être à un stade bootstrap précoce.
- Une configuration README-first est en cours, avec une structure multilingue préparée.
- Aucun historique de commits local n'a été détecté pendant l'analyse de structure (`No commits yet on main` a été noté dans le contexte d'analyse).
- Lors de l'ajout de code source, maintenez ce README à jour avec des instructions concrètes de configuration, d'utilisation et de paramétrage.

## 🩺 Dépannage

### `README.md` manquant dans des copies locales/anciennes

Si votre clone local n'incluait pas auparavant `README.md`, synchronisez avec l'état le plus récent de la branche :

```bash
git fetch origin
git pull --ff-only
```

### `i18n/` existe mais les fichiers traduits sont absents

C'est attendu à un stade de brouillon précoce. Les cibles de traduction sont définies dans :

- `.auto-readme-work/20260228_184104/translation-plan.txt`

### Stack d'exécution du projet non claire

Si vous ne voyez pas `src/`, de manifestes ou de points d'entrée, cela correspond à l'état actuellement observé. Ajoutez les détails de la stack une fois les fichiers d'implémentation introduits.

## 🗺️ Feuille de route

Objectifs à court terme pour la documentation et le bootstrap du projet :

- Finaliser le README anglais de base avec le véritable objectif du projet et son architecture
- Ajouter les fichiers README traduits sous `i18n/` selon le plan de traduction
- Introduire une arborescence de code applicatif et un/des manifeste(s) d'exécution
- Ajouter des commandes reproductibles de configuration et d'exécution
- Ajouter des vérifications CI (lint/test/validation docs) une fois la base de code en place

## 🤝 Contribution

Les contributions sont les bienvenues. Comme le dépôt est en phase de mise en place précoce :

1. Ouvrez une issue décrivant le changement proposé (docs, structure, ou mise en place initiale du code).
2. Créez une branche de fonctionnalité.
3. Gardez des changements ciblés et documentés.
4. Mettez à jour la documentation README/i18n chaque fois que le comportement ou la structure change.
5. Soumettez une pull request avec un contexte clair et des étapes de vérification.

Workflow local suggéré :

```bash
git checkout -b feat/your-change
# make edits

git add .
git commit -m "Describe your change"
git push -u origin feat/your-change
```

## 💬 Support

Aucun canal dédié de support, de sponsoring ou de donation n'est actuellement déclaré dans les fichiers du dépôt.

Si des liens de support sont ajoutés ultérieurement, incluez-les ici et conservez-les lors des révisions du README.

## 📄 Licence

Les informations de licence ne sont pas déclarées dans le contenu actuel du dépôt.

- Statut : `TBD`
- Étape suivante recommandée : ajouter un fichier `LICENSE` et mettre à jour cette section avec l'identifiant SPDX exact.

## 🧾 Hypothèses et notes de préservation

- Ce brouillon est construit à partir des fichiers actuellement présents dans `/home/lachlan/ProjectsLFS/AgInTi`.
- Un README canonique préexistant n'était pas disponible localement au moment de la génération ; par conséquent, aucun contenu substantiel n'a pu en être importé.
- Conformément à la politique de préservation, les détails inconnus ou manquants sont explicitement signalés au lieu d'être devinés ou omis.
