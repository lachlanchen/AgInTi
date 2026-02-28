[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Status](https://img.shields.io/badge/status-initializing-orange)](#aginti)
[![Docs](https://img.shields.io/badge/docs-readme_draft-blue)](#aginti)
[![Repository%20Stage](https://img.shields.io/badge/stage-bootstrap-yellow)](#aginti)
[![i18n](https://img.shields.io/badge/i18n-planned-0ea5e9)](#aginti)
[![License](https://img.shields.io/badge/license-TBD-lightgrey)](#aginti)

*README-first-Workflow • Dokumentationszentriertes Bootstrap-Repository • aktive mehrsprachige Planung.*

| Fokus | Aktueller Status |
|---|---|
| Reifegrad des Kerns | Bootstrap-Scaffold (`README`-first) |
| Lokalisierung | 10 Sprachen werden in `i18n/` gepflegt |
| Pipeline-Quelle | `.auto-readme-work/20260301_064213/` |

---

## 📌 Überblick

AgInTi ist derzeit ein Dokumentations-Scaffold-Repository mit einem `README`-first-Workflow und geplanter Mehrsprachigkeit.

Zum Zeitpunkt dieses Entwurfs konzentriert sich der Repository-Inhalt auf Dokumentationskoordination und Sprachvorbereitung, noch nicht auf ein Laufzeitprodukt:

- ✅ Es ist noch kein oberstes Source-Tree erkannt.
- ✅ `i18n/` enthält übersetzte README-Varianten.
- ✅ `.auto-readme-work/20260301_064213/` enthält den aktiven Pipeline-Kontext für diesen Lauf.
- ✅ `.auto-readme-work/20260228_184104/` wird als historisches Artefakt aufbewahrt.

### Repository-Snapshot

| Element | Aktueller Status |
|---|---|
| 🧩 Quellcode | Noch nicht erkannt |
| ⚙️ Laufzeit-Manifest-Dateien | Noch nicht erkannt |
| 🧪 CI-Workflows | Noch nicht erkannt |
| 🧭 Dokumentations-Arbeitsbereich | `.auto-readme-work/20260301_064213/` |
| 🌐 Übersetzte Dokumentation | 10 Sprachen in `i18n/` |

---

## 🚦 Projektstatus

Diese README ist ein inkrementeller, repository-genauer erster vollständiger englischer Entwurf.

- Der Zustand bleibt bootstrap-/Dokumentationsorientiert.
- Bestehende substantielle Abschnitte wurden erhalten und erweitert, statt ersetzt.
- Unbekanntes ist explizit markiert, ohne spekulative Behauptungen.

Falls in einem anderen Branch oder in der Historie eine kanonische upstream README existiert, sollten künftige Aktualisierungen diese inkrementell übernehmen.

---

## ✨ Funktionen

- Dokumentationszentrierte Repository-Struktur
- Zentrale mehrsprachige README-Pipeline unter `.auto-readme-work/`
- Klare Sprachumschalter-Vorlagen und Übersetzungs-Mappings
- Praktische Befehlsschnipsel zur Repository-Inspektion und Validierung
- Streng nachverfolgbare README-Aktualisierung mit Deduplizierung von Support-/Bannerblöcken

---

## 🗂️ Projektstruktur

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

### Wichtige Dokumentationseingänge

| Datei | Zweck |
|---|---|
| `.auto-readme-work/20260301_064213/pipeline-context.md` | Generierungsgrenzen und Prompt-Kontext für diesen Lauf. |
| `.auto-readme-work/20260301_064213/repo-structure-analysis.md` | Snapshot der erkannten Struktur und Projektlücken. |
| `.auto-readme-work/20260301_064213/translation-plan.txt` | Gebietsschema-zu-Datei-Zuordnung für übersetzte Varianten. |
| `.auto-readme-work/20260301_064213/language-nav-root.md` | Korrekte Sprachumschalterzeile für `README.md`. |
| `.auto-readme-work/20260301_064213/language-nav-i18n.md` | Korrekte Sprachumschalterzeile für Dateien in `i18n/`. |

---

## 🧰 Voraussetzungen

Für den aktuellen Zustand des Repositories sind keine Laufzeit-Abhängigkeiten erforderlich.

Für die Dokumentationsnutzung und -Pflege benötigen Sie:

- `git`
- Eine POSIX-Shell (Beispiele nutzen `bash`)
- Einen Texteditor für Markdown-Aktualisierungen

---

## 📥 Installation

Es gibt noch keinen Install-/Build-Prozess.

So prüfen Sie das Repository lokal:

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Nutzung

Aktuelle Nutzung ist Dokumentationswartung, Prüfung und Lokalisierungs-Synchronisation.

### Gemeinsame Workflows

```bash
ls -la
ls -la .auto-readme-work/20260301_064213
ls -la i18n
```

### Typischer README-Workflow

1. Lesen Sie die aktuellen Kontexte in `.auto-readme-work/20260301_064213/`.
2. Überprüfen Sie den Quell- und übersetzten README-Inhalt.
3. Nehmen Sie inkrementelle Änderungen vor, ohne bestehende substanzielle Details zu entfernen.
4. Halten Sie Sprachumschalter und Support-Blöcke konsistent über alle Locales.

---

## ⚙️ Konfiguration

Noch keine Anwendungs-Konfigurationsdatei vorhanden.

Aktuelle dokumentationsbezogene Konfiguration wird repräsentiert durch:

- `.auto-readme-work/20260301_064213/translation-plan.txt` für Ziel-Locales
- Sprachumschalter-Vorlagen in `.auto-readme-work/20260301_064213/language-nav-root.md` und `.../language-nav-i18n.md`
- Strukturkontext in `.auto-readme-work/20260301_064213/repo-structure-analysis.md`

---

## 🧪 Beispiele

### Beispiel 1: Sprachumschalterzeilen prüfen

```bash
cat .auto-readme-work/20260301_064213/language-nav-root.md
cat .auto-readme-work/20260301_064213/language-nav-i18n.md
```

### Beispiel 2: Übersetzungsumfang bestätigen

```bash
cat .auto-readme-work/20260301_064213/translation-plan.txt
```

### Beispiel 3: Scaffold-Status prüfen (erwartet: keine Manifeste)

```bash
find . -maxdepth 2 \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

---

## 🛠️ Entwicklungsnotizen

- Führen Sie diese Datei als kanonische englische Dokumentationsquelle.
- Erhalten Sie substanzielle Abschnitte bei Aktualisierungen (Inkrement-Politik).
- Fügen Sie Laufzeitanweisungen nur hinzu, wenn entsprechende Code-Basis, Manifeste und Toolchains vorhanden sind.
- Halten Sie Support- und Bannerblöcke dedupliziert (genau je eines).
- Aktualisieren Sie Roadmap und Fehlersuche, sobald Funktionalität verfügbar ist.

---

## 🩺 Fehlerbehebung

### Ich sehe nur Dokumentationsdateien

Das ist in diesem Bootstrap-Zustand zu erwarten; es wurden keine Quell-/Laufzeit-Manifeste erkannt.

### Lokalisierte Dokumentation ist inkonsistent

Nutzen Sie den neuesten Übersetzungsplan und starten Sie den README-Abgleich erneut, um Struktur und Links zu normalisieren.

### Lokaler Branch wirkt veraltet

```bash
git fetch origin
git pull --ff-only
```

---

## 🗺️ Roadmap

- Die konkrete Produkt-/Anwendungsebene ergänzen, sobald Code eingeführt wird.
- Setup-, Build- und Run-Anweisungen mit echten Manifesten ergänzen.
- CI-Workflows und Dokumentationsprüfungen hinzufügen.
- Kontributionsstandards für Code und Übersetzungen erweitern.
- Übersetzte READMEs synchronisiert und aktuell halten.

---

## 🤝 Mitwirken

Beiträge sind willkommen.

1. Eröffnen Sie ein Issue mit Kontext und Scope.
2. Erstellen Sie einen dedizierten Branch.
3. Halten Sie Änderungen fokussiert und inkrementell.
4. Bewahren Sie bestehende technische Details und den Abschnittskontext.
5. Öffnen Sie eine PR mit klaren Verifikationshinweisen.

### Empfohlener Ablauf

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

## 📄 Lizenz

Es ist keine `LICENSE`-Datei vorhanden.
