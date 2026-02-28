[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Repository](https://img.shields.io/badge/Repository-AgInTi-0f172a?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lachlanchen/AgInTi)
[![Docs](https://img.shields.io/badge/Docs-README%20Bootstrap-0ea5e9?style=for-the-badge&logo=mdbook&logoColor=white)](#aginti)
[![Localization](https://img.shields.io/badge/i18n-10%20locales-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)](#documentation-inputs-and-generated-artifacts)
[![Status](https://img.shields.io/badge/Stage-Documentation%20Pipeline-f59e0b?style=for-the-badge&logo=githubactions&logoColor=white)](#scope-and-snapshot)
[![License](https://img.shields.io/badge/License-TBD-94a3b8?style=for-the-badge&logo=readme&logoColor=white)](#license)

مستودع توثيق يُعتمد فيه README الأساسي للحفاظ على نسخة إنجليزية كاملة من README وتوثيق متعدد اللغات متزامن.

## 🧭 التنقل السريع

| النوع | الوجهة |
|---|---|
| سير عمل المستودع | [النطاق واللقطة](#-scope-and-snapshot) |
| أمثلة الاستخدام | [الاستخدام](#-usage) |
| دليل المساهمة | [المساهمة](#-contribution) |
| دعم هذا المشروع | [الدعم](#-support) |

---

[![Pipeline](https://img.shields.io/badge/Pipeline-.auto--readme--work-0f172a?style=flat-square&logo=githubactions&logoColor=white)](./.auto-readme-work)
[![Locales](https://img.shields.io/badge/Locales-10%20files-22c55e?style=flat-square&logo=googletranslate&logoColor=white)](./i18n)
[![Scope](https://img.shields.io/badge/Scope-Documentation-0ea5e9?style=flat-square&logo=mdbook&logoColor=white)](#documentation-inputs-and-generated-artifacts)

## 📌 في جملة واحدة

| 🎯 التركيز | 🧩 القيمة الحالية |
| --- | --- |
| هدف المستودع | هيكل توثيق لمرجعية README متعددة اللغات المتزامنة |
| الخاصية الأساسية | التعديلات المتزايدة تحافظ على التاريخ الجوهري |
| الحالة الحالية | لم يتم الكشف عن أي تطبيق/خدمة تشغيلية في لقطة المستودع |

---

| ✅ لقطة | 📌 الحالة الحالية |
| --- | --- |
| مرحلة المستودع | هيكل توجيهي (bootstrap) تديره `.auto-readme-work/` |
| الترجمات المحلية | 10 نسخ README مترجمة |
| التشغيل المتحقق منه | لا يوجد تطبيق أو خدمة تشغيلية مكتشفة |

## 📌 نظرة عامة

`AgInTi` هو مستودع **documentation-bootstrap**.

يركز المستودع حاليًا على توثيق README أولًا، وبنية الترجمات، وسير عمل متدرج يُستخدم لإنشاء توثيق متعدد اللغات متناسق.

- ✅ لا يوجد حتى الآن شجرة مصادر تشغيلية على المستوى الأعلى.
- ✅ يحتوي `i18n/` على 10 نسخ README مترجمة.
- ✅ يخزن `.auto-readme-work/` لقطات خط الأنابيب للتحديثات التوثيقية المتدرجة.
- ✅ يتم الحفاظ على المحتوى القائم عبر تعديلات متزايدة.

## ✅ النطاق واللقطة

| البند | الحالة الحالية |
|---|---|
| 🧩 كود المصدر | غير مكتشف |
| 🧪 الاختبارات/CI | غير مكتشفة |
| 📘 سير عمل التوثيق | يعتمد على `.auto-readme-work/` |
| 🌐 المستندات المحلية | 10 لغات مُدارة |
| 🔒 ملف الترخيص | غير موجود في هذه اللقطة |

## ✨ الميزات

- استراتيجية توثيق تبدأ بـ README.
- سير عمل واعٍ باللغة مع روابط مرجعية موحدة للصفحة الجذرية والصفحات المحلية.
- كتل البانر والدعم غير مكررة وتتموضع في مواقع محددة.
- تحديثات متزايدة تحافظ على الأقسام ذات المضمون.
- مقاطع تحقق وفحص عملية لمساهمة موجهة للمساهمين في التوثيق.

## 🗂️ بنية المشروع

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

## 🧱 نموذج الهندسة وسير العمل

في هذه المرحلة، "الهندسة" هي خط أنابيب التوثيق الخاص بالمستودع:

1. يتم إنتاج السياق والقيود في كل تنفيذ داخل `.auto-readme-work/<run-id>/pipeline-context.md`.
2. تُنشأ قوالب مبدل اللغة في `language-nav-root.md` و`language-nav-i18n.md`.
3. تُطبّق تعديلات README بشكل متزايد للحفاظ على التاريخ الجوهري.
4. يتم مزامنة الملفات المترجمة من نفس القالب البنيوي.

## 📚 مدخلات التوثيق والمخرجات المولدة

| الملف | الغرض |
|---|---|
| `.auto-readme-work/20260301_070633/pipeline-context.md` | قيود وتعليمات هذا المسار. |
| `.auto-readme-work/20260301_070633/translation-plan.txt` | خريطة إعدادات اللغات للتزامن متعدد اللغات. |
| `.auto-readme-work/20260301_070633/language-nav-root.md` | سطر تنقل اللغة القياسي الخاص بـ `README.md`. |
| `.auto-readme-work/20260301_070633/language-nav-i18n.md` | سطر تنقل اللغة القياسي لملفات README المترجمة. |
| `.auto-readme-work/20260301_070633/repo-structure-analysis.md` | لقطة بنية المستودع المستخدمة في هذه الدورة. |
| `README.md.auto-readme-support*` | ملفات دعم مساعدة استُخدمت خلال جولات التهيئة السابقة. |

## 🧭 أهداف سير عمل المستودع

هذا المستودع رقيق بشكل مقصود. الهدف طويل المدى هو إبقاء README الجذر والنسخ المترجمة متزامنة دون تراجع في السياق التقني أو الروابط أو البنية.

## 🧰 المتطلبات المسبقة

- `git` للوصول إلى المستودع.
- shell من نوع POSIX (تعتمد الأمثلة على `bash`).
- محرر يدعم Markdown.

### افتراضات التشغيل

لا توجد متطلبات بناء/تشغيل محددة بعد لأنّ أي مكونات تشغيلية قابلة للتنفيذ لم تُكشف في لقطة هذا المستودع.

## 📥 التثبيت

لا توجد حتى الآن عملية تثبيت ثنائي أو بناء.

```bash
# Clone the repository
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ الاستخدام

التركيز الحالي هو صيانة التوثيق والتناسق متعدد اللغات.

### الأوامر الشائعة

```bash
ls -la
ls -la .auto-readme-work/20260301_070633
ls -la i18n
```

### سير العمل المعتاد لتزامن README

1. مراجعة سياق التشغيل في `.auto-readme-work/20260301_070633/pipeline-context.md`.
2. مراجعة قوالب مبدل اللغة في `.auto-readme-work/20260301_070633/language-nav-*.md`.
3. تعديل `README.md` تدريجيًا؛ دون حذف الأقسام التاريخية الجوهرية.
4. الإبقاء على كتل البانر والدعم فريدة وفي المواقع المطلوبة.
5. مواءمة الملفات المترجمة ضمن `i18n/README.*.md` إلى نفس البنية عند الحاجة.

## ⚙️ الإعداد

لا يوجد إعداد تطبيقي بعد. سلوك التوثيق على مستوى المستودع مُعرَّف عبر artefacts في `.auto-readme-work/` وملفات locale داخل `i18n/`.

- `pipeline-context.md` (القيود والأهداف)
- `translation-plan.txt` (نطاق الترجمات والتعيين)
- `language-nav-root.md` و`language-nav-i18n.md` (اتساق التنقل)
- `README.md.auto-readme-support*` (أدوات scaffold)

## 🧪 الأمثلة

### المثال 1: التحقق من سطور مبدل اللغة

```bash
cat .auto-readme-work/20260301_070633/language-nav-root.md
cat .auto-readme-work/20260301_070633/language-nav-i18n.md
```

### المثال 2: التحقق من المناطق المدعومة وملفات الترجمة

```bash
cat .auto-readme-work/20260301_070633/translation-plan.txt
```

### المثال 3: التأكد من حالة scaffold

```bash
find . -maxdepth 2 \
  \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

## 🛠️ ملاحظات التطوير

- استخدم تعديلات متزايدة للحفاظ على سياق التقنية السابق.
- لا تضف خطوات بناء/تشغيل إلا بعد وجود ملفات manifest فعلية.
- تأكد من أن أقسام البانر والدعم تظهر مرة واحدة فقط.
- صِغ الفرضيات عندما يكون سلوك المستودع غير واضح.
- احرص أن تكون أمثلة الأوامر مرتبطة بالملفات والأدلة الموجودة فعليًا.

## 🩺 استكشاف الأخطاء وإصلاحها

### أرى ملفات Markdown فقط

هذا متوقع في مرحلة bootstrap الحالية.

### مبدل اللغة يبدو غير متناسق

قارن كل `README.*.md` مع سطر اللغات في الجذر ومع أحدث ملفات سياق pipeline داخل `.auto-readme-work/20260301_070633/`.

### فرعي متأخر

```bash
git fetch origin
git pull --ff-only
```

### أريد إضافة تعليمات للكود

أضف أوامر البناء/التشغيل فقط بعد إضافة manifest واضح (مثل `package.json`، `pyproject.toml`، `Cargo.toml`) والتأكد من وجود هذه العناصر فعلًا في المستودع.

## 🗺️ خارطة الطريق

- إدخال مكونات تطبيق/تشغيل فعلية.
- توسيع دليل التثبيت والتشغيل والنشر بعد توفر الكود والأدوات.
- إضافة فحوصات CI لجودة Markdown وتوافق اللغات.
- الحفاظ على قابلية إعادة إنتاج عملية الترجمة عبر pipelines صريحة ومتدرجة.
- إضافة إرشادات مساهمة لكل من مساهمي التوثيق ومهندسي الكود مستقبلاً.

## 🤝 المساهمة

المساهمات مرحب بها.

1. أنشئ issue يصف التغيير.
2. افتح فرعًا مخصصًا.
3. اجعل التغييرات بسيطة وتدريجية.
4. احتفظ بالأقسام المهمة الموجودة بالفعل.
5. قدّم pull request بملاحظات تحقق موجزة.

### المسار المقترح

```bash
git checkout -b docs/your-update
# edit README.md and/or i18n/
git add README.md
git commit -m "docs: refine README draft"
git push -u origin docs/your-update
```

## 📄 الترخيص

ليست هناك رخصة مضافة حتى الآن في لقطة هذا المستودع.


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
