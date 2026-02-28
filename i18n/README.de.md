[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Repository](https://img.shields.io/badge/Repository-AgInTi-0f172a?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lachlanchen/AgInTi)
[![Docs](https://img.shields.io/badge/Docs-README%20Bootstrap-0ea5e9?style=for-the-badge&logo=mdbook&logoColor=white)](#aginti)
[![Localization](https://img.shields.io/badge/i18n-10%20locales-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)](#documentation-inputs-and-generated-artifacts)
[![Status](https://img.shields.io/badge/Stage-Documentation%20Pipeline-f59e0b?style=for-the-badge&logo=githubactions&logoColor=white)](#scope-and-snapshot)
[![License](https://img.shields.io/badge/License-TBD-94a3b8?style=for-the-badge&logo=readme&logoColor=white)](#license)

Dokumentationsorientiertes Repository-Scaffolding für ein vollständiges englisches README und eine synchronisierte mehrsprachige Dokumentation.

## 🧭 Schnellnavigation

| Typ | Ziel |
|---|---|
| Repository-Workflow | [Scope and snapshot](#-scope-and-snapshot) |
| Verwendungsbeispiele | [Verwendung](#-usage) |
| Beitragsleitfaden | [Mitwirkung](#-contribution) |
| Projekt unterstützen | [Support](#-support) |

---

[![Pipeline](https://img.shields.io/badge/Pipeline-.auto--readme--work-0f172a?style=flat-square&logo=githubactions&logoColor=white)](./.auto-readme-work)
[![Locales](https://img.shields.io/badge/Locales-10%20files-22c55e?style=flat-square&logo=googletranslate&logoColor=white)](./i18n)
[![Scope](https://img.shields.io/badge/Scope-Documentation-0ea5e9?style=flat-square&logo=mdbook&logoColor=white)](#documentation-inputs-and-generated-artifacts)

## 📌 Auf einen Blick

| 🎯 Fokus | 🧩 Aktueller Wert |
| --- | --- |
| Repository-Zweck | Dokumentations-Scaffold für die Synchronisierung mehrsprachiger READMEs |
| Zentrale Invariante | Inkrementelle Änderungen bewahren die fachliche Historie |
| Aktueller Zustand | In diesem Repository-Snapshot wurde noch keine Laufzeit-App/ein Dienst erkannt |

| ✅ Snapshot | 📌 Aktueller Stand |
| --- | --- |
| Repository-Phase | Bootstrap-Scaffold gesteuert durch `.auto-readme-work/` |
| Lokalisierungen | 10 übersetzte README-Varianten |
| Verifizierte Runtime | Keine ausführbare App oder kein Service erkannt |

## 📌 Übersicht

AgInTi ist ein **Dokumentations-Bootstrap-Repository**.

Das Repository fokussiert auf README-first-Dokumentation, Lokalisierungs-Scaffolding und iterative Workflow-Artefakte, die für konsistente mehrsprachige Dokumentation sorgen.

- ✅ Kein Top-Level-Runtime-Quellbaum wurde bisher erkannt.
- ✅ `i18n/` enthält 10 übersetzte README-Varianten.
- ✅ `.auto-readme-work/` speichert Pipeline-Artefakte für inkrementelle Dokumentationsupdates.
- ✅ Bestehende Inhalte bleiben durch inkrementelle Updates erhalten.

## ✅ Scope and snapshot

| Element | Aktueller Stand |
|---|---|
| 🧩 Quellcode | Nicht erkannt |
| 🧪 Tests/CI | Nicht erkannt |
| 📘 Dokumentations-Workflow | Getrieben durch `.auto-readme-work/` |
| 🌐 Lokalisierte Dokumentation | 10 gepflegte Sprachen |
| 🔒 Lizenzdatei | In diesem Snapshot nicht vorhanden |

## ✨ Funktionen

- README-first-Strategie für Repository-Dokumentation.
- Sprachbewusster Workflow mit kanonischen Links für Root- und Lokalisierungsseiten.
- Deduplizierte Banner- und Support-Blöcke an festgelegten Positionen.
- Inkrementelle Updates, die substanzielle Abschnitte bewahren.
- Praktische Prüf- und Validierungsschnipsel für Dokumentationsbeiträge.

## 🗂️ Projektstruktur

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

## 🧱 Architektur- und Workflow-Modell

In diesem Stadium ist „Architektur“ die Dokumentations-Pipeline des Repos:

1. Kontext und Beschränkungen werden pro Lauf in `.auto-readme-work/<run-id>/pipeline-context.md` erzeugt.
2. Sprachnavigations-Templates werden in `language-nav-root.md` / `language-nav-i18n.md` erzeugt.
3. README-Änderungen werden inkrementell angewendet, um fachlichen Kontext zu bewahren.
4. Lokalisierte Dateien werden aus derselben Strukturvorlage synchronisiert.

## 📚 Dokumentationseingaben und generierte Artefakte

| Datei | Zweck |
|---|---|
| `.auto-readme-work/20260301_070633/pipeline-context.md` | Quellbeschränkungen und Anweisungen für diesen Durchlauf. |
| `.auto-readme-work/20260301_070633/translation-plan.txt` | Lokalisierungs-Mapping für die mehrsprachige Synchronisation. |
| `.auto-readme-work/20260301_070633/language-nav-root.md` | Kanonische Sprach-Navigationszeile für `README.md`. |
| `.auto-readme-work/20260301_070633/language-nav-i18n.md` | Kanonische Sprach-Navigationszeile für lokalisierte READMEs. |
| `.auto-readme-work/20260301_070633/repo-structure-analysis.md` | Repository-Snapshot, das für diese Generierung genutzt wurde. |
| `README.md.auto-readme-support*` | Hilfsmanifestdateien für frühere Bootstrap-Durchläufe. |

## 🧭 Ziele des Repository-Workflows

Dieses Repository ist absichtlich schlank gehalten. Langfristiges Ziel ist es, die Root-README und lokalisierten Varianten zu synchronisieren, ohne technischen Kontext, Links und Struktur zu regressieren.

## 🧰 Voraussetzungen

- `git` für Repository-Zugriff.
- Eine POSIX-Shell (Beispiele verwenden `bash`).
- Ein Markdown-fähiger Editor.

### Laufzeit-Annahmen

Es sind noch keine Build-/Runtime-Anforderungen definiert, da in diesem Repository-Snapshot keine ausführbare Produkt-Implementierung erkannt wurde.

## 📥 Installation

Es gibt noch keinen Installations- oder Build-Prozess für Binärartefakte.

```bash
# Clone the repository
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Verwendung

Der aktuelle Verwendungsfokus liegt auf Dokumentationspflege und mehrsprachiger Konsistenz.

### Häufige Befehle

```bash
ls -la
ls -la .auto-readme-work/20260301_070633
ls -la i18n
```

### Typischer README-Sync-Workflow

1. Review-run-Kontext in `.auto-readme-work/20260301_070633/pipeline-context.md` prüfen.
2. Sprachumschalter-Vorlagen in `.auto-readme-work/20260301_070633/language-nav-*.md` prüfen.
3. `README.md` inkrementell bearbeiten; keine substantielle historisch relevante Sektion entfernen.
4. Banner- und Support-Blöcke eindeutig halten und an den vorgegebenen Positionen platzieren.
5. Lokalisierte Dateien in `i18n/README.*.md` bei Bedarf auf dieselbe Struktur anpassen.

## ⚙️ Konfiguration

Es existiert noch keine Anwendungskonfiguration. Das repositoryweite Dokumentationsverhalten ist durch Workflow-Artefakte in `.auto-readme-work/` und Locale-Dateien in `i18n/` definiert.

- `pipeline-context.md` (Randbedingungen und Ziele)
- `translation-plan.txt` (Umfang und Zuordnung der Sprachen)
- `language-nav-root.md` und `language-nav-i18n.md` (Navigationskonsistenz)
- `README.md.auto-readme-support*` (Scaffolding-Helfer)

## 🧪 Beispiele

### Beispiel 1: Sprachumschalter-Zeilen prüfen

```bash
cat .auto-readme-work/20260301_070633/language-nav-root.md
cat .auto-readme-work/20260301_070633/language-nav-i18n.md
```

### Beispiel 2: Unterstützte Locales und Übersetzungsdateien prüfen

```bash
cat .auto-readme-work/20260301_070633/translation-plan.txt
```

### Beispiel 3: Scaffold-Status bestätigen

```bash
find . -maxdepth 2 \
  \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

## 🛠️ Entwicklungsnotizen

- Nutze inkrementelle Edits, um vorhandenen technischen Kontext zu bewahren.
- Keine Build-/Installationsschritte hinzufügen, solange keine konkreten Manifestdateien vorhanden sind.
- Sicherstellen, dass Banner- und Support-Abschnitte nur einmal vorkommen.
- Annahmen explizit aussprechen, wenn Repository-Verhalten unbekannt ist.
- Halte Command-Beispiele an bestehende Dateien und Verzeichnisse gebunden.

## 🩺 Fehlerbehebung

### Ich sehe nur Markdown-Dateien

Das ist in dieser Bootstrap-Phase zu erwarten.

### Sprachumschalter wirkt inkonsistent

Vergleiche jedes `README.*.md` mit der Root-Sprachzeile und den neuesten Pipeline-Kontext-Dateien in `.auto-readme-work/20260301_070633/`.

### Mein Branch ist hinterher

```bash
git fetch origin
git pull --ff-only
```

### Ich möchte Codeanweisungen hinzufügen

Füge Build-/Ausführungsbefehle erst hinzu, nachdem konkrete Manifeste (z. B. `package.json`, `pyproject.toml`, `Cargo.toml` usw.) hinzugefügt und deren Vorhandensein im Repository bestätigt wurden.

## 🗺️ Roadmap

- Konkrete Anwendungs- oder Laufzeitkomponenten einführen.
- Installations-, Laufzeit- und Deployment-Hinweise erweitern, sobald Code und Tooling vorhanden sind.
- CI-Prüfungen für Markdown-Qualität und Locale-Konsistenz ergänzen.
- Den Übersetzungsprozess über explizit versionierte Pipelines reproduzierbar halten.
- Beitragsrichtlinien sowohl für Dokumentations- als auch für zukünftige Code-Beitragende hinzufügen.

## 🤝 Mitwirkung

Beiträge sind willkommen.

1. Erstelle ein Issue, das die Änderung beschreibt.
2. Öffne einen dedizierten Branch.
3. Halte Änderungen minimal und inkrementell.
4. Bewahre bestehende sinnstiftende Abschnitte.
5. Reiche eine Pull Request mit prägnanten Verifizierungsnotizen ein.

### Vorgeschlagener Ablauf

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

Die Lizenz ist in diesem Repository-Snapshot noch nicht enthalten.
