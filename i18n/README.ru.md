[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Status](https://img.shields.io/badge/status-initializing-orange)](#aginti)
[![Docs](https://img.shields.io/badge/docs-readme_draft-blue)](#aginti)
[![Repository%20Stage](https://img.shields.io/badge/stage-bootstrap-yellow)](#aginti)
[![i18n](https://img.shields.io/badge/i18n-planned-0ea5e9)](#aginti)
[![License](https://img.shields.io/badge/license-TBD-lightgrey)](#aginti)

*Documentation-first bootstrap repository • README-first workflow • active multilingual planning.*

| Focus | Current state |
|---|---|
| Core maturity | Bootstrap scaffold (`README`-first) |
| Localization | 10 locales maintained in `i18n/` |
| Pipeline source | `.auto-readme-work/20260301_064213/` |

---

## 📌 Обзор

AgInTi на данный момент является репозиторием scaffolding с подходом documentation-first и управлением документацией через README.

На момент этого черновика содержимое репозитория сфокусировано на координации документации и подготовке переводов, а не на runtime-продукте:

- ✅ Верхнеуровневое дерево исходного кода пока не обнаружено.
- ✅ В `i18n/` содержатся переводимые варианты README.
- ✅ `.auto-readme-work/20260301_064213/` хранит активный контекст пайплайна для этого прохода.
- ✅ `.auto-readme-work/20260228_184104/` сохранён как исторический артефакт.

### Snapshot репозитория

| Элемент | Текущее состояние |
|---|---|
| 🧩 Исходный код | Не обнаружен |
| ⚙️ Runtime-манифесты | Не обнаружены |
| 🧪 CI workflows | Не обнаружены |
| 🧭 Рабочая область документации | `.auto-readme-work/20260301_064213/` |
| 🌐 Переводы | 10 локалей в `i18n/` |

---

## 🚦 Статус проекта

Этот README — инкрементальный, точный по текущему состоянию репозитория первый полноценный черновик на английском.

- Состояние по-прежнему ориентировано на bootstrap/documentation.
- Содержательные существующие разделы сохранены и расширены, а не заменены.
- Неопределённые моменты явно помечены и не содержат спекуляций.

Если канонический upstream-README существует в другой ветке или истории, будущие обновления должны выполняться инкрементально с его слиянием.

---

## ✨ Особенности

- Репозиторий с первым приоритетом на документацию.
- Централизованный multilingual README pipeline в `.auto-readme-work/`.
- Явные шаблоны переключения языка и файлы сопоставления переводов.
- Практические snippets команд для проверки и валидации структуры репозитория.
- Строго отслеживаемый процесс обновления README с дедупликацией блоков баннера/поддержки.

---

## 🗂️ Структура проекта

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

### Ключевые входные файлы документации

| Файл | Назначение |
|---|---|
| `.auto-readme-work/20260301_064213/pipeline-context.md` | Ограничения генерации и контекст промпта для этого прогона. |
| `.auto-readme-work/20260301_064213/repo-structure-analysis.md` | Снимок обнаруженной структуры и пробелов проекта. |
| `.auto-readme-work/20260301_064213/translation-plan.txt` | Сопоставление локалей и файлов для переведённых вариантов. |
| `.auto-readme-work/20260301_064213/language-nav-root.md` | Каноническая строка переключения языков для `README.md`. |
| `.auto-readme-work/20260301_064213/language-nav-i18n.md` | Каноническая строка переключения языков для файлов в `i18n/`. |

---

## 🧰 Требования

В текущем состоянии репозитория нет runtime-зависимостей.

Для использования и поддержки документации нужны:

- `git`
- POSIX shell (в примерах используется `bash`)
- Текстовый редактор для Markdown-изменений

---

## 📥 Установка

Пока не существует процесса сборки/установки.

Для локальной проверки репозитория:

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Использование

На данный момент использование — обслуживание документации, аудит и синхронизация локализаций.

### Типовые рабочие процессы

```bash
ls -la
ls -la .auto-readme-work/20260301_064213
ls -la i18n
```

### Типовой workflow README

1. Прочитать текущие артефакты контекста в `.auto-readme-work/20260301_064213/`.
2. Проверить исходный и переведённые варианты README.
3. Применять инкрементальные изменения, чтобы не удалять существующие содержательные детали.
4. Поддерживать строки переключения языков и support-блоки согласованными между локалями.

---

## ⚙️ Конфигурация

Файл конфигурации приложения пока отсутствует.

Текущая конфигурация на уровне документации описана в:

- `.auto-readme-work/20260301_064213/translation-plan.txt` — цели локализации
- Шаблоны языкового навигатора в `.auto-readme-work/20260301_064213/language-nav-root.md` и `.../language-nav-i18n.md`
- Контекст структуры репозитория в `.auto-readme-work/20260301_064213/repo-structure-analysis.md`

---

## 🧪 Примеры

### Пример 1: Проверка строк переключения языка

```bash
cat .auto-readme-work/20260301_064213/language-nav-root.md
cat .auto-readme-work/20260301_064213/language-nav-i18n.md
```

### Пример 2: Проверка объёма перевода

```bash
cat .auto-readme-work/20260301_064213/translation-plan.txt
```

### Пример 3: Проверка состояния scaffold (ожидается: нет манифестов)

```bash
find . -maxdepth 2 \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

---

## 🛠️ Заметки по разработке

- Вести этот файл как канонический исходный источник английской документации.
- Сохранять содержательные разделы при обновлении (политика инкрементальных правок).
- Добавлять инструкции по запуску только тогда, когда есть соответствующий код, манифесты и toolchain.
- Сохранять deduplicate-логику для блоков поддержки и баннера (ровно по одному каждому).
- Обновлять roadmap и troubleshooting сразу после появления функциональности.

---

## 🩺 Устранение неполадок

### Я вижу только файлы документации

Это ожидаемое состояние для bootstrap-фазы: в репозитории не обнаружены исходные runtime-манифесты.

### Локали документации непоследовательны

Используйте последний план переводов и повторите README-sync поток, чтобы нормализовать структуру и ссылки.

### Локальная ветка кажется устаревшей

```bash
git fetch origin
git pull --ff-only
```

---

## 🗺️ Дорожная карта

- Добавить реальный продуктовый/приложенческий слой при появлении кода.
- Расширить инструкции setup, build и run на основе реальных манифестов.
- Добавить CI workflows и проверки документации.
- Расширить стандарты контрибьюции для кода и переводов.
- Поддерживать синхронизацию и актуальность переведённых README.

---

## 🤝 Как внести вклад

Вклады приветствуются.

1. Откройте issue с контекстом и объёмом работы.
2. Создайте отдельную ветку.
3. Делайте правки точечно и инкрементально.
4. Сохраняйте существующие технические детали и контекст разделов.
5. Открывайте PR с понятными заметками о проверках.

### Предлагаемый flow

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

Файл `LICENSE` пока отсутствует.

- Status: `TBD`
- Рекомендуемый следующий шаг: добавить файл лицензии и указать SPDX-идентификатор здесь.

## 🧾 Допущения и заметки по сохранению

- Содержимое репозитория оценивалось из `/home/lachlan/ProjectsLFS/AgInTi` во время этого прогона.
- Runtime-цели и архитектура пока не представлены в закоммиченных файлах; этот черновик намеренно фокусируется на задокументированных фактах.
- Существующие содержательные разделы из предыдущего черновика сохранены и расширены, где это было полезно.
- Баннер и support-блоки были добавлены по одному разу для соблюдения требуемых позиций.
