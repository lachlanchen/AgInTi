[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Repository](https://img.shields.io/badge/Repository-AgInTi-0f172a?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lachlanchen/AgInTi)
[![Docs](https://img.shields.io/badge/Docs-README%20Bootstrap-0ea5e9?style=for-the-badge&logo=mdbook&logoColor=white)](#aginti)
[![Localization](https://img.shields.io/badge/i18n-10%20locales-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)](#documentation-inputs-and-generated-artifacts)
[![Status](https://img.shields.io/badge/Stage-Documentation%20Pipeline-f59e0b?style=for-the-badge&logo=githubactions&logoColor=white)](#scope-and-snapshot)
[![License](https://img.shields.io/badge/License-TBD-94a3b8?style=for-the-badge&logo=readme&logoColor=white)](#license)

Документационный репозиторий-скелет с подходом `README-first`, созданный для поддержания полного английского README и синхронизированной многоязычной документации.

## 🧭 Быстрая навигация

| Тип | Назначение |
|---|---|
| Рабочий процесс репозитория | [Область и снимок](#-scope-and-snapshot) |
| Примеры использования | [Использование](#-usage) |
| Руководство по внесению вклада | [Вклад](#-contribution) |
| Поддержка проекта | [Support](#-support) |

---

[![Pipeline](https://img.shields.io/badge/Pipeline-.auto--readme--work-0f172a?style=flat-square&logo=githubactions&logoColor=white)](./.auto-readme-work)
[![Locales](https://img.shields.io/badge/Locales-10%20files-22c55e?style=flat-square&logo=googletranslate&logoColor=white)](./i18n)
[![Scope](https://img.shields.io/badge/Scope-Documentation-0ea5e9?style=flat-square&logo=mdbook&logoColor=white)](#documentation-inputs-and-generated-artifacts)

## 📌 Краткий обзор

| 🎯 Фокус | 🧩 Текущее значение |
| --- | --- |
| Цель репозитория | Документационный шаблон для синхронизированного многоязычного README |
| Основной инвариант | Инкрементальные изменения сохраняют содержательную историю |
| Текущее состояние | В текущем снимке репозитория не обнаружено приложение или сервис с runtime |

| ✅ Снимок | 📌 Текущее состояние |
| --- | --- |
| Фаза репозитория | bootstrap-структура, управляемая `.auto-readme-work/` |
| Локализации | 10 переведённых вариантов README |
| Проверенный runtime | Исполняемое приложение или сервис не обнаружены |

## 📌 Обзор

AgInTi — это репозиторий **документационного bootstrap**.

Репозиторий ориентирован на документацию в стиле `README-first`, подготовку локализационной инфраструктуры и итеративные артефакты workflow, которые используются для генерации согласованной многоязычной документации.

- ✅ На верхнем уровне исходный код, содержащий runtime, пока не обнаружен.
- ✅ В `i18n/` есть 10 локализованных вариантов README.
- ✅ `.auto-readme-work/` хранит артефакты конвейера для последовательных обновлений документации.
- ✅ Существующее содержимое сохраняется с помощью инкрементальных обновлений.

## ✅ Область и snapshot

| Элемент | Текущее состояние |
|---|---|
| 🧩 Исходный код | Не обнаружен |
| 🧪 Тесты/CI | Не обнаружены |
| 📘 Документационный workflow | Управляется `.auto-readme-work/` |
| 🌐 Локализованная документация | Поддерживается 10 языков |
| 🔒 Файл лицензии | В этом снимке отсутствует |

## ✨ Возможности

- Стратегия документации, ориентированная на README.
- Языково-осознанный workflow с каноническими ссылками для корневой и локализованных страниц.
- Дедуплицированные блоки баннера и поддержки на согласованных позициях.
- Инкрементальные обновления, которые сохраняют содержательно важные разделы.
- Практичные сниппеты проверки и валидации для участников документации.

## 🗂️ Структура проекта

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

## 🧱 Модель архитектуры и workflow

На этом этапе «архитектура» — это конвейер документации репозитория:

1. Контекст и ограничения создаются в каждом запуске в `.auto-readme-work/<run-id>/pipeline-context.md`.
2. Шаблоны языка формируются в `language-nav-root.md` / `language-nav-i18n.md`.
3. Изменения в README применяются инкрементно, чтобы сохранить содержательный контекст.
4. Локализованные файлы синхронизируются из одного и того же структурного шаблона.

## 📚 Входные данные документации и сгенерированные артефакты

| Файл | Назначение |
|---|---|
| `.auto-readme-work/20260301_070633/pipeline-context.md` | Ограничения и инструкции для этого прохода. |
| `.auto-readme-work/20260301_070633/translation-plan.txt` | Соответствие локалей для многоязычной синхронизации. |
| `.auto-readme-work/20260301_070633/language-nav-root.md` | Каноническая строка переключателя языков для `README.md`. |
| `.auto-readme-work/20260301_070633/language-nav-i18n.md` | Каноническая строка переключателя языков для локализованных README. |
| `.auto-readme-work/20260301_070633/repo-structure-analysis.md` | Срез структуры репозитория, использованный для этой генерации. |
| `README.md.auto-readme-support*` | Вспомогательные манифесты поддержки, применявшиеся в предыдущих bootstrap-проходах. |

## 🧭 Цели workflow репозитория

Этот репозиторий по сути тонкий и намеренно минимальный. Долгосрочная цель — поддерживать корневой README и локализованные варианты синхронизированными без регресса технического контекста, ссылок и структуры.

## 🧰 Предварительные требования

- `git` для доступа к репозиторию.
- POSIX-совместимая оболочка (в примерах используется `bash`).
- Редактор с поддержкой Markdown.

### Предположения о runtime

Определений требований к сборке/запуску пока нет, потому что в этом снимке репозитория не обнаружено артефактов исполняемого продукта.

## 📥 Установка

Пока не существует бинарной установки или процесса сборки.

```bash
# Клонировать репозиторий
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Использование

Текущее использование сосредоточено на поддержке документации и многоязыковой согласованности.

### Общие команды

```bash
ls -la
ls -la .auto-readme-work/20260301_070633
ls -la i18n
```

### Типичный workflow синхронизации README

1. Просмотреть контекст запуска в `.auto-readme-work/20260301_070633/pipeline-context.md`.
2. Проверить шаблоны переключателя языка в `.auto-readme-work/20260301_070633/language-nav-*.md`.
3. Изменять `README.md` инкрементно; не удалять содержательные исторические разделы.
4. Держать блоки баннера и поддержки уникальными и размещать их только в заданных позициях.
5. По мере необходимости выравнивать локализованные файлы `i18n/README.*.md` к одной и той же структуре.

## ⚙️ Конфигурация

Конфигурация приложения пока отсутствует. Поведение документации репозитория определяется артефактами workflow в `.auto-readme-work/` и файлами локализации в `i18n/`.

- `pipeline-context.md` (ограничения и цели)
- `translation-plan.txt` (область действия и маппинг локалей)
- `language-nav-root.md` и `language-nav-i18n.md` (согласованность навигации)
- `README.md.auto-readme-support*` (вспомогательные инструменты scaffolding)

## 🧪 Примеры

### Пример 1: Проверка строк селектора языка

```bash
cat .auto-readme-work/20260301_070633/language-nav-root.md
cat .auto-readme-work/20260301_070633/language-nav-i18n.md
```

### Пример 2: Проверка поддерживаемых локалей и файлов переводов

```bash
cat .auto-readme-work/20260301_070633/translation-plan.txt
```

### Пример 3: Подтверждение статуса scaffold

```bash
find . -maxdepth 2 \
  \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

## 🛠️ Заметки по разработке

- Используйте инкрементальные изменения, чтобы сохранить существующий технический контекст.
- Не добавляйте шаги сборки/установки, пока не появятся конкретные манифесты.
- Обеспечьте единственный экземпляр баннера и секции поддержки.
- Формулируйте допущения, когда поведение репозитория неясно.
- Привязывайте примеры команд к существующим файлам и директориям.

## 🩺 Устранение неполадок

### Я вижу только markdown-файлы

Это ожидаемо на стадии bootstrap.

### Переключатель языка выглядит неконсистентно

Сверьте каждый `README.*.md` с корневой строкой языков и последними файлами контекста пайплайна в `.auto-readme-work/20260301_070633/`.

### Моя ветка отстаёт

```bash
git fetch origin
git pull --ff-only
```

### Я хочу добавить инструкции по коду

Добавляйте команды сборки/запуска только после добавления конкретных манифестов (например, `package.json`, `pyproject.toml`, `Cargo.toml` и т. п.) и подтверждения их наличия в репозитории.

## 🗺️ Дорожная карта

- Добавить конкретные компоненты приложения/runtime.
- Расширить инструкции по установке, запуску и деплою после появления кода и инструментов.
- Добавить проверки CI для качества Markdown и паритета локалей.
- Поддерживать воспроизводимый процесс перевода через явно версионируемые пайплайны.
- Добавить рекомендации по участию как для документации, так и для будущих контрибьютеров кода.

## 🤝 Вклад

Вклад приветствуется.

1. Создайте issue с описанием изменений.
2. Откройте отдельную ветку.
3. Держите изменения минимальными и инкрементальными.
4. Сохраняйте существующие содержательные разделы.
5. Отправьте pull request с краткими заметками верификации.

### Рекомендуемый поток

```bash
git checkout -b docs/your-update
# отредактируйте README.md и/или i18n/
git add README.md
git commit -m "docs: refine README draft"
git push -u origin docs/your-update
```

## 📄 Лицензия

Лицензия пока не включена в текущий снимок репозитория.


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
