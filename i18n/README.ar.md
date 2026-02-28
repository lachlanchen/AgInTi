[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Status](https://img.shields.io/badge/status-initializing-orange)](#aginti)
[![Docs](https://img.shields.io/badge/docs-readme_draft-blue)](#aginti)
[![Repository%20Stage](https://img.shields.io/badge/stage-bootstrap-yellow)](#aginti)
[![i18n](https://img.shields.io/badge/i18n-planned-0ea5e9)](#aginti)
[![License](https://img.shields.io/badge/license-TBD-lightgrey)](#aginti)

*مستودع تأسيسي قائم على التوثيق أولًا • سير عمل قائم على README أولًا • تخطيط متعدد اللغات قيد التفعيل.*

| Focus | Current state |
|---|---|
| Core maturity | Bootstrap scaffold (`README`-first) |
| Localization | 10 locales maintained in `i18n/` |
| Pipeline source | `.auto-readme-work/20260301_064213/` |

---

## 📌 Overview

AgInTi هي حالياً مستودعًا تأسيسيًا للتوثيق مع سير عمل Markdown أولاً (README-first) وتخطيط متعدد اللغات لتوثيق المشروع.

في وقت هذه المسودة، يركز محتوى المستودع بشكل أساسي على تنسيق التوثيق وتحضير اللغات، وليس على منتج تشغيلي فعلي:

- ✅ لم يتم اكتشاف شجرة مصدر على المستوى الأعلى بعد.
- ✅ يحتوي مجلد `i18n/` على نسخ README مترجمة.
- ✅ يضم `.auto-readme-work/20260301_064213/` سياق خط أنابيب التوليد النشط لهذه الدورة.
- ✅ يحتفظ `.auto-readme-work/20260228_184104/` كأثر تاريخي.

### Repository snapshot

| Item | Current state |
|---|---|
| 🧩 Source code | Not detected yet |
| ⚙️ Runtime manifests | Not detected yet |
| 🧪 CI workflows | Not detected yet |
| 🧭 Documentation workspace | `.auto-readme-work/20260301_064213/` |
| 🌐 Translated docs | 10 locales in `i18n/` |

---

## 🚦 Project status

هذا README هو مسودة إنجليزية كاملة أولى تعتمد على تحديثات تزايدية مطابقة لحالة المستودع.

- الحالة ما تزال موجهة نحو التأسيس والتوثيق.
- تم الحفاظ على الأقسام الموجودة وتوسيعها بدلًا من استبدال المحتوى الجوهري.
- يتم توضيح العناصر غير المؤكدة بوضوح لتجنب الإدعايات التخمينية.

إذا كان هناك نسخة README رسمية في فرع أو تاريخ آخر، يجب دمجها تدريجيًا في التحديثات اللاحقة.

---

## ✨ Features

- هيكل مستودع يعتمد على `README-first`.
- خط أنابيب README متعدد اللغات مركزي ضمن `.auto-readme-work/`.
- قوالب تبديل لغة واضحة وملفات خريطة ترجمة.
- مقاطع أوامر عملية لفحص المستودع والتحقق منه.
- عملية تحديث README مُراقبة بدقة مع إزالة التكرار في كتل الدعم/البانر.

---

## 🗂️ Project structure

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

### Key documentation inputs

| File | Purpose |
|---|---|
| `.auto-readme-work/20260301_064213/pipeline-context.md` | قيود التوليد وسياق التشغيل المستخدم في هذه الدورة. |
| `.auto-readme-work/20260301_064213/repo-structure-analysis.md` | لقطة من الهيكل المكتشف والفجوات الحالية. |
| `.auto-readme-work/20260301_064213/translation-plan.txt` | خريطة تحويل اللغات إلى الملفات المترجمة. |
| `.auto-readme-work/20260301_064213/language-nav-root.md` | سطر التبديل الموحد للغة في `README.md`. |
| `.auto-readme-work/20260301_064213/language-nav-i18n.md` | سطر التبديل الموحد للغة في ملفات `i18n/`. |

---

## 🧰 Prerequisites

لا توجد متطلبات تشغيل مطلوبة للحالة الحالية للمستودع.

لاستخدام التوثيق والصيانة، ستحتاج إلى:

- `git`
- shell متوافق مع POSIX (الأمثلة تستخدم `bash`)
- محرر نصوص لتحديث ملفات Markdown

---

## 📥 Installation

لا توجد عملية تثبيت أو بناء حتى الآن.

لفحص المستودع محليًا:

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Usage

الاستخدام الحالي يتمحور حول صيانة التوثيق ومراجعة التوافق وتزامن ملفات الترجمة.

### Common workflows

```bash
ls -la
ls -la .auto-readme-work/20260301_064213
ls -la i18n
```

### Typical README workflow

1. اقرأ ملفات السياق الحالية في `.auto-readme-work/20260301_064213/`.
2. راجع محتوى ملفات README المصدر والمترجمة.
3. طبق تعديلات تزايدية لتجنب حذف أي تفاصيل جوهرية موجودة.
4. احرص على اتساق سطر تبديل اللغة وكتل الدعم عبر جميع اللغات.

---

## ⚙️ Configuration

لا يوجد ملف إعداد تطبيق حاضر حتى الآن.

إعدادات التوثيق مُمثّلة حاليًا عبر:

- `.auto-readme-work/20260301_064213/translation-plan.txt` لاستهداف اللغات
- قوالب تبديل اللغة داخل `.auto-readme-work/20260301_064213/language-nav-root.md` و`.../language-nav-i18n.md`
- سياق هيكل المستودع في `.auto-readme-work/20260301_064213/repo-structure-analysis.md`

---

## 🧪 Examples

### Example 1: Verify language switcher lines

```bash
cat .auto-readme-work/20260301_064213/language-nav-root.md
cat .auto-readme-work/20260301_064213/language-nav-i18n.md
```

### Example 2: Confirm translation scope

```bash
cat .auto-readme-work/20260301_064213/translation-plan.txt
```

### Example 3: Confirm scaffold state (expected: no manifests)

```bash
find . -maxdepth 2 \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

---

## 🛠️ Development notes

- احتفظ بهذا الملف كمصدر التوثيق الإنجليزي المعتمد.
- حافظ على المكونات الجوهرية عند التحديث (سياسة التحرير التزايدي).
- أضف تعليمات runtime فقط عندما تتوفر ملفات manifests و toolchains وطبقات تشغيل فعلية.
- أبقِ كتل الدعم والبنر غير مكررة (بالضبط نسخة واحدة).
- حدّث خرائط الطريق واستكشاف المشكلات بمجرد توفر وظائف جديدة.

---

## 🩺 Troubleshooting

### I only see documentation files

هذا متوقع في حالة التهيئة الحالية؛ لم يتم اكتشاف manifests أو runtime أو شيفرة تشغيل.

### Locale documentation is inconsistent

استخدم أحدث خطة ترجمة ثم أعد تشغيل تدفق مزامنة README لتوحيد الهيكل والروابط.

### Local branch feels outdated

```bash
git fetch origin
git pull --ff-only
```

---

## 🗺️ Roadmap

- إضافة طبقة التطبيق/المنتج الفعلية عند إدخال الكود.
- توسيع تعليمات الإعداد والبناء والتشغيل من الملفات التنفيذية الحقيقية.
- إضافة سير عمل CI وفحوصات توثيقية.
- توسيع معايير المساهمة للشيفرة والترجمة.
- إبقاء ملفات README المترجمة متزامنة ومحدثة.

---

## 🤝 Contribution

المساهمات مرحّب بها.

1. افتح issue مع سياق ونطاق واضحين.
2. أنشئ فرعًا مخصصًا.
3. اجعل التعديلات مركّزة وتدرجية.
4. حافظ على التفاصيل الفنية الحالية وسياق الأقسام.
5. افتح PR مع ملاحظات تحقق واضحة.

### Suggested flow

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

لا يوجد ملف `LICENSE` بعد.

- Status: `TBD`
- Recommended next step: add a license file and set SPDX identifier here.

## 🧾 Assumptions and preservation notes

- تم تقييم محتوى المستودع من `/home/lachlan/ProjectsLFS/AgInTi` خلال هذه الدورة.
- الأهداف الزمنية والمعمارية للتشغيل غير ممثلة في الملفات الملتقطة بعد؛ هذه المسودة مركزة مقصودًا على الحقائق الموثقة.
- تم الحفاظ على الأقسام الجوهرية من المسودة السابقة وتوسعتها عند الحاجة.
- أُدرجت كتل البانر والدعم مرة واحدة فقط للالتزام بمتطلبات إزالة التكرار.
