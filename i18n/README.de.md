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

Dokumentationsorientiertes Repository-Scaffold zur Pflege einer vollständigen englischen README und synchronisierter mehrsprachiger Dokumentation, geführt von drei Leitprinzipien: **sear creation tools**, **self-healing tools** und **chain of prompt tools**.

## 🧭 Schnellnavigation

| Typ | Ziel |
| --- | --- |
| Projektzusammenfassung | [Überblick](#overview) |
| Kernfähigkeiten | [Features](#features) |
| Pipeline-Design | [Architektur](#architecture) |
| Philosophische Basis | [Philosophie auf einen Blick](#philosophy-at-a-glance) |
| Workflow für Mitwirkende | [Entwicklungsnotizen](#development-notes) |
| Zukünftige Ausrichtung | [Roadmap](#roadmap) |
| Projekt unterstützen | [Support](#-support) |

---

<a id="scope-and-snapshot"></a>
## 📌 Umfang und Snapshot

| Element | Aktueller Stand |
| --- | --- |
| Repository-Phase | Bootstrap-Scaffold für Dokumentation |
| Laufzeitcode | Im aktuellen Snapshot nicht erkannt |
| Tests/CI-Pipelines | Im aktuellen Snapshot nicht erkannt |
| Lokalisierte Doku | 10 Locale-Dateien unter `i18n/` |
| Pipeline-Artefakte | Zeitgestempelte Läufe unter `.auto-readme-work/` |
| Lizenzdatei | Nicht als eigenständige Datei vorhanden (README-Badge: TBD) |
| Philosophische Basis | Sear creation + self-healing + chain of prompt tools |

<a id="overview"></a>
## 🌍 Überblick

AgInTi fungiert derzeit als README-Lifecycle- und Lokalisierungs-Pipeline statt als Laufzeitanwendung. Die `README.md` im Root ist die kanonische Quelle, und lokalisierte Varianten in `i18n/` werden an dieser Struktur ausgerichtet.

Die Projektphilosophie ist explizit und operativ, nicht dekorativ. Jedes README-Update sollte alle drei Prinzipien erfüllen:

1. **Sear creation tools**: gezielt scharfe Erstellungs-Workflows, die aus eingeschränkter Repository-Evidenz praxisnahe Dokumentation mit hoher Signalstärke erzeugen.
2. **Self-healing tools**: reparaturorientierte Mechanismen, die Drift korrigieren, Duplikate entfernen und strukturelle Konsistenz wiederherstellen.
3. **Chain of prompt tools**: gestufte, nachvollziehbare Prompt-Flows, die die Herkunft von Kontext zu Ausgabe über Pipeline-Läufe hinweg erhalten.

Dieses Repository bewahrt substanzielle historische Inhalte durch inkrementelle Updates und erhält dabei Links, Befehle und Support-Metadaten.

<a id="philosophy-at-a-glance"></a>
### Philosophie auf einen Blick

| Prinzip | Zweck | Operatives Ergebnis |
| --- | --- | --- |
| **Sear creation tools** | Hochwertige Dokumentation aus begrenzter Evidenz erzeugen. | Abschnitte bleiben praxisnah, konkret und repository-basiert. |
| **Self-healing tools** | Drift, Duplikate und veraltete Strukturen reparieren. | Kanonische und lokalisierte READMEs bleiben sauber und ausgerichtet. |
| **Chain of prompt tools** | Generierungsstufen explizit und nachvollziehbar halten. | Pipeline-Artefakte bewahren reproduzierbaren Kontext und Übergaben. |

<a id="features"></a>
## ✨ Features

- README-first-Dokumentationsstrategie mit einem kanonischen Root-Dokument.
- Mehrsprachige Synchronisierung über 10 i18n-README-Varianten.
- Pipeline-gesteuerte Erstellung über Artefakte in `.auto-readme-work/<run-id>/`.
- Invarianten für genau ein Banner und genau ein Support-Panel, um doppelte visuelle Blöcke zu vermeiden.
- Disziplinierte inkrementelle Updates, die bedeutende technische Historie erhalten.

### Abbildung von Prinzipien auf Features

| Kernprinzip | Erscheinungsform in den aktuellen Features |
| --- | --- |
| **Sear creation tools** | Präzises README-Drafting aus repository-basierter Evidenz und stabilen Abschnitts-Scaffolds. |
| **Self-healing tools** | Deduplizierungs-Checks für wiederholte Banner-/Support-Blöcke, veraltete Referenzen und Strukturdrift. |
| **Chain of prompt tools** | Lauf-spezifische Artefaktkette (`pipeline-context`, Nav-Templates, Übersetzungsplan) für reproduzierbare Ausgabe. |

<a id="project-structure"></a>
## 🗂️ Projektstruktur

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

<a id="architecture"></a>
## 🏗️ Architektur

In diesem Stadium bedeutet Architektur Pipeline-Architektur für Dokumentation, nicht Laufzeitarchitektur einer Anwendung.

### Pipeline-Ablauf

1. Ein lauf-spezifischer Kontext wird in `.auto-readme-work/<run-id>/pipeline-context.md` festgehalten.
2. Vorlagen für Sprach-Navigation werden erzeugt (`language-nav-root.md` und `language-nav-i18n.md`).
3. Kanonischer README-Inhalt wird inkrementell in `README.md` aktualisiert.
4. Lokalisierte README-Dateien in `i18n/` werden an die kanonische Struktur angeglichen.
5. Struktur-Qualitätsprüfungen erzwingen Deduplizierung, Link-Konsistenz und Erhalt technischer Details.

### Kernprinzipien in der Architektur

- **Sear creation tools**: angewendet bei der Inhaltserstellung, damit Abschnitte konkret, vollständig und repository-genau bleiben.
- **Self-healing tools**: angewendet bei der Validierung, um doppelte Blöcke zu entfernen, veraltete Laufreferenzen zu reparieren und strukturelle Parität wiederherzustellen.
- **Chain of prompt tools**: angewendet über Artefakte hinweg, damit jede Generierungsstufe explizit und auditierbar bleibt.

### Prinzip-Checkpoints je Pipeline-Phase

| Phase | Sear creation tools | Self-healing tools | Chain of prompt tools |
| --- | --- | --- | --- |
| Kontexterfassung | Scharfe Generierungsgrenzen definieren. | Fehlende/ungültige Inputs früh markieren. | Quell-Prompt und Lauf-Metadaten erhalten. |
| Kanonisches Drafting | Vollständige README-Abschnitte aus Repository-Evidenz erstellen. | Regressionen und versehentlichen Inhaltsverlust verhindern. | Phasenausgaben mit vorherigen Artefakten verknüpfen. |
| i18n-Angleichung | Struktur und technische Parität über Locales halten. | Drift zwischen Root- und i18n-Dateien korrigieren. | Kanonische Intention in jede lokalisierte Variante übertragen. |
| Finale Verifikation | Lesbarkeit und Detailerhalt erzwingen. | Doppelte Banner-/Support-Blöcke und veraltete Referenzen entfernen. | Auditierbare Artefaktspur für den Lauf hinterlassen. |

## 🧾 Dokumentations-Inputs und generierte Artefakte

| Datei | Zweck |
| --- | --- |
| `.auto-readme-work/20260302_124338/pipeline-context.md` | Quellvorgaben und Ziele für diesen Generierungsdurchlauf. |
| `.auto-readme-work/20260302_124338/repo-structure-analysis.md` | Zusammenfassung des Repository-Scans und abgeleiteter technischer Stand. |
| `.auto-readme-work/20260302_124338/language-nav-root.md` | Kanonische Sprachoptionszeile für die Root-`README.md`. |
| `.auto-readme-work/20260302_124338/language-nav-i18n.md` | Kanonische Sprachoptionszeile für i18n-README-Dateien. |
| `.auto-readme-work/20260302_124338/translation-plan.txt` | Locale-Mapping und i18n-Zieldateiplan. |
| `.auto-readme-work/<older-run-id>/...` | Historischer Laufkontext aus früheren README-Pipeline-Durchläufen. |

## 🔧 Voraussetzungen

- `git`
- POSIX-Shell (Beispiele nutzen `bash`)
- Markdown-fähiger Editor

### Annahmen

- In diesem Repository-Snapshot ist kein ausführbarer Service und kein Anwendungsmanifest vorhanden.
- Installations-/Build-/Start-Anleitungen sind deshalb auf Dokumentations-Workflows ausgerichtet.

## 📥 Installation

Es ist noch kein Binärpaket oder Laufzeit-Build-Schritt definiert.

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Nutzung

Die aktuelle Nutzung ist Dokumentationspflege und mehrsprachige Synchronisierung.

### Häufige Inspektionsbefehle

```bash
ls -la
ls -la .auto-readme-work/20260302_124338
ls -la i18n
```

### Workflow zur Synchronisierung der kanonischen README

1. Lies `.auto-readme-work/20260302_124338/pipeline-context.md`.
2. Prüfe Sprachselektor-Vorlagen aus `language-nav-root.md` und `language-nav-i18n.md`.
3. Aktualisiere `README.md` inkrementell als Source of Truth.
4. Gleiche `i18n/README.*.md`-Dateien an dieselbe Struktur und dieselben wichtigen technischen Details an.
5. Bestätige, dass es genau ein Banner und genau ein Support-Panel gibt.

## ⚙️ Konfiguration

Es gibt noch keine Laufzeitkonfiguration. Das Dokumentationsverhalten wird durch Repository-Artefakte gesteuert.

- `pipeline-context.md`: Laufziele und Randbedingungen.
- `repo-structure-analysis.md`: Snapshot-Evidenz und Lücken.
- `language-nav-root.md` und `language-nav-i18n.md`: Navigationskonsistenz.
- `translation-plan.txt`: Locale-Ziele und Mapping.

## 🧪 Beispiele

### Beispiel 1: Vorlagen für Sprach-Navigation prüfen

```bash
cat .auto-readme-work/20260302_124338/language-nav-root.md
cat .auto-readme-work/20260302_124338/language-nav-i18n.md
```

### Beispiel 2: Locale-Plan prüfen

```bash
cat .auto-readme-work/20260302_124338/translation-plan.txt
```

### Beispiel 3: Fehlen von Runtime-Manifests bestätigen (aktueller Snapshot)

```bash
find . -maxdepth 2 \
  \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

<a id="development-notes"></a>
## 🛠️ Entwicklungsnotizen

- Erhalte substanzielle Abschnitte und Links aus der Historie der kanonischen README.
- Bevorzuge inkrementelle Edits statt destruktiver Neuschreibungen.
- Halte genau ein Banner und genau einen Support-Block.
- Halte Root- und i18n-README-Strukturen synchron.
- Nenne Annahmen klar, wenn Laufzeit- oder Infrastrukturdetails unbekannt sind.
- Nutze die Triade der Philosophie als aktive Leitplanken:
  - **Sear creation tools** für Drafting mit hoher Signalstärke.
  - **Self-healing tools** für Konsistenzreparatur.
  - **Chain of prompt tools** für reproduzierbare Übergaben zwischen Pipeline-Phasen.

## 🚑 Fehlerbehebung

### Ich sehe nur Markdown-Dateien und Pipeline-Artefakte

Das ist in der aktuellen Bootstrap-Phase erwartbar.

### Sprachselektor-Zeilen unterscheiden sich zwischen Dateien

Nutze die kanonischen Vorlagen in:

- `.auto-readme-work/20260302_124338/language-nav-root.md`
- `.auto-readme-work/20260302_124338/language-nav-i18n.md`

### Mein Branch ist nicht aktuell

```bash
git fetch origin
git pull --ff-only
```

### Ich möchte Laufzeitanleitungen ergänzen

Füge Build-/Run-Anleitungen erst hinzu, nachdem konkrete Manifeste (zum Beispiel `package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`) eingeführt wurden und die Pfade in diesem Repository bestätigt sind.

## 🗺️ Roadmap

1. **Sear creation tools** mit standardisierten README-Drafting-Templates, Abschnitts-Qualitäts-Gates und klareren Evidenz-zu-Ausgabe-Checks stärken.
2. **Self-healing tools** mit automatisierten Checks für doppelte Blöcke, Locale-Drift, defekte interne Anker und veraltete Laufreferenzen ausbauen.
3. **Chain of prompt tools** über Laufphasen hinweg formalisieren, um reproduzierbare Spuren für Kontext, Generierung, Übersetzung und Verifikation zu schaffen.
4. Einen Single-Command-Flow für Dokumentationspflege hinzufügen, sobald Repository-Skripte eingeführt sind.
5. CI-Checks für Markdown-Qualität, Link-Integrität und i18n-Strukturparität ergänzen.
6. Konkrete Laufzeitkomponenten einführen, wenn Source-Manifeste und Entry-Points hinzugefügt werden.
7. Eine stabile Lizenzentscheidung veröffentlichen und eine eigenständige Lizenzdatei ergänzen.

### Roadmap nach Prinzipfokus

| Fokusbereich | Kurzfristiges Ziel |
| --- | --- |
| **Sear creation tools** | Drafting-Templates und evidenzbasierte Abschnitts-Prompts verbessern. |
| **Self-healing tools** | Duplikaterkennung, Prüfungen auf veraltete Anker und Locale-Drift-Reparatur automatisieren. |
| **Chain of prompt tools** | Artefaktverträge pro Laufphase für reproduzierbare mehrsprachige Ausgaben standardisieren. |

## 🤝 Beitrag

Beiträge sind willkommen.

1. Öffne ein Issue, das die geplante Änderung beschreibt.
2. Erstelle einen fokussierten Branch.
3. Halte Doku-Edits inkrementell und repository-genau.
4. Erhalte wichtige Links, Befehle und substanzielle historische Kontexte.
5. Öffne einen Pull Request mit knappen Verifikationsnotizen.

### Empfohlener Ablauf

```bash
git checkout -b docs/your-update
# edit README.md and/or i18n/README.*.md
git add README.md i18n/README.*.md
git commit -m "docs: refine README content"
git push -u origin docs/your-update
```

## 📄 Lizenz

TBD. Eine eigenständige Lizenzdatei ist geplant, im aktuellen Snapshot aber noch nicht vorhanden.


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
