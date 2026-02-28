[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# AgInTi

[![Status](https://img.shields.io/badge/status-initializing-orange)](#aginti)
[![Docs](https://img.shields.io/badge/docs-readme_draft-blue)](#aginti)
[![Repository Stage](https://img.shields.io/badge/stage-bootstrap-yellow)](#aginti)
[![i18n](https://img.shields.io/badge/i18n-planned-0ea5e9)](#aginti)
[![License](https://img.shields.io/badge/license-TBD-lightgrey)](#aginti)

## 📌 Überblick

AgInTi befindet sich derzeit in einer Initialisierungs-/Scaffold-Phase. Zum Zeitpunkt dieses README-Entwurfs enthält das Repository hauptsächlich:

- Git-Metadaten (`.git/`)
- Ein `i18n/`-Verzeichnis, vorbereitet für mehrsprachige README-Dateien
- Einen `.auto-readme-work/`-Workspace mit Pipeline-Kontext zur README-Generierung und Artefakten zur Sprachplanung

Im aktuellen Working Tree wurden kein Anwendungsquellcode, keine Paket-Manifeste, keine Runtime-Entrypoints und keine CI-Workflows erkannt.

### Repository-Snapshot

| Element | Aktueller Status |
| --- | --- |
| Quellcode | Noch nicht erkannt |
| Runtime-Manifeste | Noch nicht erkannt |
| CI-Workflows | Noch nicht erkannt |
| Dokumentations-Workspace | `.auto-readme-work/20260228_184104/` |
| i18n-Verzeichnis | Vorhanden (`i18n/`) |

## 🚦 Projektstatus

Dies ist der **erste vollständige README-Entwurf** für dieses Repository.

- Beobachteter Repository-Status: **noch kein Top-Level-Quellbaum**
- Vorhandene kanonische README-Basis: **während dieses Laufs im lokalen Workspace nicht vorhanden**
- Hier verwendeter Dokumentationsansatz: alle erkannten repository-genauen Details beibehalten und Unbekanntes klar kennzeichnen, statt Inhalte zu entfernen oder zu erfinden

Falls eine kanonische historische README in einem Remote-Branch oder der Historie existiert, sollte dieser Entwurf schrittweise mit diesem Inhalt zusammengeführt werden, statt substanzielle Abschnitte zu ersetzen.

## ✨ Features (Aktuell)

Die aktuellen Repository-Fähigkeiten sind dokumentations-/pipeline-orientiert:

- README-Generierungs-Workspace unter `.auto-readme-work/`
- Planung mehrsprachiger README-Ziele (11 Sprachen inklusive Englisch)
- Sprach-Navigationsvorlagen für Root und `i18n/`

Geplante Produkt-/Runtime-Features sind in diesem Stadium unbekannt.

## 🗂️ Projektstruktur

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

### Wichtige Dokumentationsquellen

| Datei | Zweck |
| --- | --- |
| `.auto-readme-work/20260228_184104/pipeline-context.md` | Definiert README-Einschränkungen und den Workflow-Kontext der Generierung für diesen Lauf. |
| `.auto-readme-work/20260228_184104/repo-structure-analysis.md` | Fasst die erkannte Repository-Struktur und bekannte Lücken zusammen. |
| `.auto-readme-work/20260228_184104/language-nav-root.md` | Kanonische Sprachumschalter-Zeile für die Root-`README.md`. |
| `.auto-readme-work/20260228_184104/language-nav-i18n.md` | Kanonische Sprachumschalter-Zeile für übersetzte Dateien unter `i18n/`. |
| `.auto-readme-work/20260228_184104/translation-plan.txt` | Zuordnung von Locale zu Datei für Übersetzungen. |

## 🧰 Voraussetzungen

Derzeit sind keine Runtime-Voraussetzungen nötig, um den Repository-Inhalt in seinem aktuellen Zustand zu verwenden.

Für Dokumentations-Workflows und Repository-Operationen benötigen Sie wahrscheinlich:

- `git`
- Eine POSIX-kompatible Shell (Beispiele verwenden `bash`)
- Einen Texteditor

## 📥 Installation

Da aktuell kein Anwendungs-/Paket-Manifest vorhanden ist, gibt es noch keinen Installations-/Build-Schritt.

Repository klonen:

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Nutzung

Die praktische Nutzung besteht derzeit aus Repository-Inspektion und README-/i18n-Dokumentationsarbeit.

Beispiele:

```bash
# Show top-level files
ls -la

# Inspect auto-generated README context files
ls -la .auto-readme-work/20260228_184104

# Inspect i18n directory
ls -la i18n
```

## ⚙️ Konfiguration

Aktuell wurden keine Anwendungs-Konfigurationsdateien erkannt.

Bekannte Konfigurationssignale im Repository:

- Git-Remote ist als `origin git@github.com:lachlanchen/AgInTi.git` konfiguriert
- Mehrsprachige README-Navigation und Ziel-Locale-Zuordnungen in `.auto-readme-work/20260228_184104/`

## 🧪 Beispiele

### Beispiel 1: Konsistenz der README-Sprachnavigation validieren

```bash
# Compare language switcher templates used by the pipeline
cat .auto-readme-work/20260228_184104/language-nav-root.md
cat .auto-readme-work/20260228_184104/language-nav-i18n.md
```

### Beispiel 2: Menge der Übersetzungsziele bestätigen

```bash
cat .auto-readme-work/20260228_184104/translation-plan.txt
```

### Beispiel 3: Verifizieren, dass noch keine Runtime-Manifeste vorhanden sind

```bash
# Typical manifest check (expected: none in current state)
find . -maxdepth 2 \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml \)
```

## 🛠️ Hinweise zur Entwicklung

- Das Repository scheint sich in einer frühen Bootstrap-Phase zu befinden.
- Ein README-First-Setup ist in Arbeit, die mehrsprachige Struktur ist vorbereitet.
- Während der Strukturanalyse wurde keine lokale Commit-Historie erkannt (`No commits yet on main` wurde im Analysekontext notiert).
- Beim Hinzufügen von Quellcode sollte diese README mit konkreten Anweisungen zu Setup, Nutzung und Konfiguration aktualisiert werden.

## 🩺 Fehlerbehebung

### `README.md` fehlt in älteren/lokalen Kopien

Wenn Ihr lokaler Klon zuvor keine `README.md` enthielt, synchronisieren Sie mit dem neuesten Branch-Stand:

```bash
git fetch origin
git pull --ff-only
```

### `i18n/` existiert, aber übersetzte Dateien fehlen

Das ist in einer frühen Entwurfsphase erwartbar. Übersetzungsziele sind definiert in:

- `.auto-readme-work/20260228_184104/translation-plan.txt`

### Unklarer Projekt-Runtime-Stack

Wenn Sie kein `src/`, keine Manifeste oder keine Entrypoints sehen, entspricht das dem aktuell beobachteten Zustand. Ergänzen Sie Stack-Details, sobald Implementierungsdateien eingeführt werden.

## 🗺️ Roadmap

Kurzfristige Ziele für Dokumentation und Projekt-Bootstrap:

- Baseline der englischen README mit realem Projektzweck und Architektur finalisieren
- Übersetzte README-Dateien unter `i18n/` gemäß Übersetzungsplan hinzufügen
- Anwendungs-Quellstruktur und Runtime-Manifest(e) einführen
- Reproduzierbare Setup- und Ausführungsbefehle hinzufügen
- CI-Prüfungen (Lint/Test/Dokumentationsvalidierung) hinzufügen, sobald die Codebasis existiert

## 🤝 Mitwirken

Beiträge sind willkommen. Da sich das Repository in einer frühen Setup-Phase befindet:

1. Öffnen Sie ein Issue, das die vorgeschlagene Änderung beschreibt (Dokumentation, Struktur oder initiales Code-Layout).
2. Erstellen Sie einen Feature-Branch.
3. Halten Sie Änderungen fokussiert und dokumentiert.
4. Aktualisieren Sie README-/i18n-Dokumentation, wenn sich Verhalten oder Struktur ändern.
5. Erstellen Sie einen Pull Request mit klarem Kontext und Verifizierungsschritten.

Empfohlener lokaler Workflow:

```bash
git checkout -b feat/your-change
# make edits

git add .
git commit -m "Describe your change"
git push -u origin feat/your-change
```

## 💬 Support

Aktuell sind in den Repository-Dateien keine dedizierten Support-, Sponsoring- oder Spendenkanäle deklariert.

Falls später Support-Links ergänzt werden, sollten sie hier aufgenommen und über README-Revisionen hinweg beibehalten werden.

## 📄 Lizenz

Lizenzinformationen sind im aktuellen Repository-Inhalt nicht deklariert.

- Status: `TBD`
- Empfohlener nächster Schritt: Eine `LICENSE`-Datei hinzufügen und diesen Abschnitt mit der exakten SPDX-Kennung aktualisieren.

## 🧾 Annahmen und Hinweise zur Inhaltsbewahrung

- Dieser Entwurf wurde aus den aktuell vorhandenen Repository-Dateien in `/home/lachlan/ProjectsLFS/AgInTi` erstellt.
- Eine kanonische, bereits vorhandene README war zum Generierungszeitpunkt lokal nicht verfügbar; daher konnte kein substantieller Inhalt daraus übernommen werden.
- Gemäß Inhaltsbewahrungsrichtlinie werden unbekannte oder fehlende Details explizit markiert, statt sie zu raten oder wegzulassen.
