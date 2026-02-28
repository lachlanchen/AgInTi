[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Status](https://img.shields.io/badge/status-initializing-orange)](#aginti)
[![Docs](https://img.shields.io/badge/docs-readme_draft-blue)](#aginti)
[![Repository%20Stage](https://img.shields.io/badge/stage-bootstrap-yellow)](#aginti)
[![i18n](https://img.shields.io/badge/i18n-planned-0ea5e9)](#aginti)
[![License](https://img.shields.io/badge/license-TBD-lightgrey)](#aginti)

*Dépôt bootstrap orienté documentation • Workflow « README-first » • planification multilingue active.*

| Focus | Current state |
|---|---|
| Maturité du cœur | Échafaudage bootstrap (`README`-first) |
| Localisation | 10 locales maintenues dans `i18n/` |
| Contexte du pipeline | `.auto-readme-work/20260301_064213/` |

---

## 📌 Vue d'ensemble

AgInTi est actuellement un dépôt « bootstrap » de documentation avec un workflow centré sur le README et une planification de documentation multilingue.

Au moment de cette ébauche, le contenu du dépôt est centré sur la coordination documentaire et la préparation linguistique, pas encore sur un produit exécutable :

- ✅ Aucun arbre source de haut niveau n'est encore détecté.
- ✅ `i18n/` contient des variantes de README traduites.
- ✅ `.auto-readme-work/20260301_064213/` stocke le contexte de pipeline actif pour cette passe.
- ✅ `.auto-readme-work/20260228_184104/` est conservé comme artefact historique.

### Instantané du dépôt

| Élément | État actuel |
|---|---|
| 🧩 Code source | Non détecté pour l’instant |
| ⚙️ Manifeste d’exécution | Non détecté pour l’instant |
| 🧪 Workflows CI | Non détectés pour l’instant |
| 🧭 Espace de travail documentation | `.auto-readme-work/20260301_064213/` |
| 🌐 Documents traduits | 10 locales dans `i18n/` |

---

## 🚦 État du projet

Ce README est une ébauche anglaise complète incrémentale et fidèle à l’état réel du dépôt.

- L’état reste orienté bootstrap/documentation.
- Les sections existantes substantielles ont été conservées et enrichies plutôt que remplacées.
- Les zones inconnues sont explicitement signalées et les affirmations spéculatives évitées.

Si un README de référence existe dans une autre branche ou dans l’historique, les mises à jour futures doivent le fusionner incrémentalement.

---

## ✨ Fonctionnalités

- Répertoire orienté documentation « README-first »
- Pipeline centralisé de gestion des README multilingues dans `.auto-readme-work/`
- Modèles de switcher linguistique explicites et fichiers de mappage de traduction
- Extraits de commandes pratiques pour l’inspection et la validation du dépôt
- Processus de mise à jour README strictement tracé avec dédoublonnage des blocs de support et de bannière

---

## 🗂️ Structure du projet

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

### Références de documentation clés

| Fichier | Objectif |
|---|---|
| `.auto-readme-work/20260301_064213/pipeline-context.md` | Contraintes de génération et contexte de prompt pour cette exécution. |
| `.auto-readme-work/20260301_064213/repo-structure-analysis.md` | Instantané de la structure détectée et des lacunes projet. |
| `.auto-readme-work/20260301_064213/translation-plan.txt` | Mapping locale → fichier pour les variantes traduites. |
| `.auto-readme-work/20260301_064213/language-nav-root.md` | Ligne canonique de sélection linguistique pour `README.md`. |
| `.auto-readme-work/20260301_064213/language-nav-i18n.md` | Ligne canonique de sélection linguistique pour les fichiers de `i18n/`. |

---

## 🧰 Prérequis

Aucune dépendance d’exécution n’est requise pour l’état actuel du dépôt.

Pour l’usage et la maintenance de la documentation, vous avez besoin de :

- `git`
- Un shell POSIX (les exemples utilisent `bash`)
- Un éditeur de texte pour les mises à jour Markdown

---

## 📥 Installation

Il n’existe pas encore de processus d’installation/compilation.

Pour inspecter le dépôt localement :

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Utilisation

L’usage actuel est la maintenance documentaire, l’audit et la synchronisation de la localisation.

### Workflow courant

```bash
ls -la
ls -la .auto-readme-work/20260301_064213
ls -la i18n
```

### Workflow README typique

1. Lire les artefacts de contexte actuels dans `.auto-readme-work/20260301_064213/`.
2. Consulter le README source et les versions traduites.
3. Appliquer des modifications incrémentales pour éviter la suppression de détails substantiels existants.
4. Conserver la cohérence du switcher linguistique et des blocs support/bannière entre les locales.

---

## ⚙️ Configuration

Aucun fichier de configuration applicative n’est encore présent.

La configuration au niveau documentation est représentée par :

- `.auto-readme-work/20260301_064213/translation-plan.txt` pour les cibles locales
- Les modèles de switcher linguistique dans `.auto-readme-work/20260301_064213/language-nav-root.md` et `.../language-nav-i18n.md`
- Le contexte de structure du dépôt dans `.auto-readme-work/20260301_064213/repo-structure-analysis.md`

---

## 🧪 Exemples

### Exemple 1 : Vérifier les lignes de switcher linguistique

```bash
cat .auto-readme-work/20260301_064213/language-nav-root.md
cat .auto-readme-work/20260301_064213/language-nav-i18n.md
```

### Exemple 2 : Confirmer la portée de traduction

```bash
cat .auto-readme-work/20260301_064213/translation-plan.txt
```

### Exemple 3 : Vérifier l’état du scaffold (résultat attendu : aucun manifeste)

```bash
find . -maxdepth 2 \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

---

## 🛠️ Notes de développement

- Maintenir ce fichier comme source de documentation canonique en anglais.
- Préserver les sections substantielles lors des mises à jour (politique de modification incrémentale).
- Ajouter des instructions runtime uniquement quand les fichiers de code, manifestes et chaînes de compilation correspondantes existent.
- Garder un seul bloc support et un seul bloc bannière (strictement dédoublonnés).
- Mettre à jour la feuille de route et le dépannage dès que la fonctionnalité devient disponible.

---

## 🩺 Dépannage

### Je ne vois que des fichiers de documentation

C’est attendu dans cet état bootstrap ; aucun manifeste source/runtime n’a été détecté.

### La documentation locale est incohérente

Utilisez le plan de traduction le plus récent et relancez votre flux de synchronisation README pour normaliser la structure et les liens.

### La branche locale semble périmée

```bash
git fetch origin
git pull --ff-only
```

---

## 🗺️ Feuille de route

- Ajouter la couche produit/application concrète lorsque le code sera introduit.
- Étendre les instructions d’installation, build et run depuis de vrais manifestes.
- Ajouter des workflows CI et des contrôles de docs.
- Étendre les standards de contribution pour le code et les traductions.
- Maintenir les README traduits synchronisés et à jour.

---

## 🤝 Contribution

Les contributions sont les bienvenues.

1. Ouvrir une issue avec le contexte et la portée.
2. Créer une branche dédiée.
3. Garder les modifications ciblées et incrémentales.
4. Préserver les détails techniques existants et le contexte des sections.
5. Ouvrir une PR avec des notes de vérification claires.

### Flux suggéré

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
