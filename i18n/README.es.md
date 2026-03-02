[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Repository](https://img.shields.io/badge/Repository-AgInTi-0f172a?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lachlanchen/AgInTi)
[![Docs](https://img.shields.io/badge/Docs-README%20Bootstrap-0ea5e9?style=for-the-badge&logo=mdbook&logoColor=white)](#aginti)
[![Localization](https://img.shields.io/badge/i18n-10%20locales-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)](#estructura-del-proyecto)
[![Status](https://img.shields.io/badge/Stage-Documentation%20Pipeline-f59e0b?style=for-the-badge&logo=githubactions&logoColor=white)](#alcance-y-estado-actual)
[![License](https://img.shields.io/badge/License-TBD-94a3b8?style=for-the-badge&logo=readme&logoColor=white)](#licencia)
[![Principle-Sear%20Creation-ef4444?style=flat-square&logo=firefox&logoColor=white)](#resumen-general)
[![Principle-Self--Healing-10b981?style=flat-square&logo=wrench&logoColor=white)](#caracteristicas)
[![Principle-Chain%20of%20Prompt%20Tools-3b82f6?style=flat-square&logo=chainlink&logoColor=white)](#arquitectura)

Repositorio base orientado a documentación para mantener un README completo en inglés y documentación multilingüe sincronizada, guiado por tres principios operativos: **sear creation tools**, **self-healing tools** y **chain of prompt tools**.

## 🧭 Navegación rápida

| Tipo | Destino |
| --- | --- |
| Resumen del proyecto | [Resumen general](#resumen-general) |
| Capacidades principales | [Características](#caracteristicas) |
| Diseño del pipeline | [Arquitectura](#arquitectura) |
| Base de filosofía | [Filosofía de un vistazo](#filosofia-de-un-vistazo) |
| Flujo para contribuidores | [Notas de desarrollo](#notas-de-desarrollo) |
| Dirección futura | [Roadmap](#roadmap) |
| Apoya este proyecto | [Support](#-support) |

---

## 📌 Alcance y estado actual

| Ítem | Estado actual |
| --- | --- |
| Fase del repositorio | Estructura base de documentación (bootstrap scaffold) |
| Código de ejecución | No detectado en la instantánea actual |
| Tests/CI pipelines | No detectados en la instantánea actual |
| Documentación localizada | 10 archivos de locale bajo `i18n/` |
| Artefactos del pipeline | Ejecuciones con marca temporal bajo `.auto-readme-work/` |
| Archivo de licencia | No presente como archivo independiente (badge en README: TBD) |
| Base filosófica | Sear creation + self-healing + chain of prompt tools |

## 🌍 Resumen general

Actualmente AgInTi funciona como un pipeline de ciclo de vida y localización de README, no como una aplicación en ejecución. El `README.md` raíz es la fuente canónica, y las variantes localizadas en `i18n/` se sincronizan desde esa estructura canónica.

La filosofía del proyecto es explícita y operativa, no decorativa. Cada actualización del README debe cumplir los tres principios:

1. **Sear creation tools**: flujos de creación intencionalmente precisos que producen documentación práctica y de alta señal a partir de evidencia restringida del repositorio.
2. **Self-healing tools**: mecanismos orientados a reparación que corrigen desalineaciones, eliminan duplicaciones y restauran consistencia estructural.
3. **Chain of prompt tools**: flujos de prompts por etapas y trazables que conservan la trazabilidad entre contexto y salida en cada ejecución del pipeline.

Este repositorio conserva contenido histórico sustantivo mediante actualizaciones incrementales, preservando enlaces, comandos y metadatos de soporte.

### Filosofía de un vistazo

| Principio | Intención | Resultado operativo |
| --- | --- | --- |
| **Sear creation tools** | Producir documentación de alta señal desde evidencia acotada. | Las secciones se mantienen prácticas, específicas y aterrizadas al repositorio. |
| **Self-healing tools** | Reparar desalineaciones, duplicaciones y estructura obsoleta. | Los README canónicos y localizados se mantienen alineados y limpios. |
| **Chain of prompt tools** | Mantener explícitas y trazables las etapas de generación. | Los artefactos del pipeline conservan contexto y handoffs reproducibles. |

## ✨ Características

- Estrategia de documentación README-first con un documento raíz canónico.
- Sincronización multilingüe entre 10 variantes README i18n.
- Autoría guiada por pipeline mediante artefactos en `.auto-readme-work/<run-id>/`.
- Invariantes de un solo banner y un solo panel de soporte para evitar bloques visuales duplicados.
- Disciplina de actualización incremental que preserva historial técnico relevante.

### Mapeo principio-característica

| Principio central | Cómo aparece en las características actuales |
| --- | --- |
| **Sear creation tools** | Redacción precisa del README a partir de evidencia del repositorio y plantillas de sección estables. |
| **Self-healing tools** | Verificaciones de deduplicación para bloques repetidos de banner/soporte, referencias obsoletas y deriva estructural. |
| **Chain of prompt tools** | Cadena de artefactos por ejecución (`pipeline-context`, plantillas de navegación, plan de traducción) para salida reproducible. |

## 🗂️ Estructura del proyecto

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

## 🏗️ Arquitectura

En esta etapa, arquitectura significa arquitectura del pipeline de documentación, no arquitectura de runtime de una aplicación.

### Flujo del pipeline

1. Se registra un contexto específico de ejecución en `.auto-readme-work/<run-id>/pipeline-context.md`.
2. Se generan plantillas de navegación de idioma (`language-nav-root.md` y `language-nav-i18n.md`).
3. El contenido canónico del README se actualiza incrementalmente en `README.md`.
4. Los README localizados en `i18n/` se alinean con la estructura canónica.
5. Verificaciones de calidad estructural aplican deduplicación, consistencia de enlaces y preservación de detalles técnicos.

### Principios centrales en la arquitectura

- **Sear creation tools**: se aplican durante la construcción de contenido para mantener secciones concretas, completas y fieles al repositorio.
- **Self-healing tools**: se aplican durante la validación para quitar bloques duplicados, reparar referencias obsoletas de ejecución y restaurar paridad estructural.
- **Chain of prompt tools**: se aplican en todos los artefactos para que cada etapa de generación permanezca explícita y auditable.

### Puntos de control por etapa del pipeline

| Etapa | Sear creation tools | Self-healing tools | Chain of prompt tools |
| --- | --- | --- | --- |
| Captura de contexto | Definir restricciones de generación precisas. | Detectar entradas faltantes/invalidas temprano. | Conservar prompt fuente y metadatos de ejecución. |
| Redacción canónica | Construir secciones completas del README desde evidencia del repositorio. | Prevenir regresiones y pérdida accidental de contenido. | Mantener salidas de etapa vinculadas a artefactos previos. |
| Alineación i18n | Mantener estructura y paridad técnica entre locales. | Corregir deriva entre archivos raíz e i18n. | Transportar la intención canónica a cada variante localizada. |
| Verificación final | Exigir legibilidad y preservación de detalles. | Quitar banners/paneles de soporte duplicados y referencias obsoletas. | Dejar una traza de artefactos auditable de la ejecución. |

## 🧾 Entradas de documentación y artefactos generados

| Archivo | Propósito |
| --- | --- |
| `.auto-readme-work/20260302_124338/pipeline-context.md` | Restricciones y objetivos fuente para esta pasada de generación. |
| `.auto-readme-work/20260302_124338/repo-structure-analysis.md` | Resumen del escaneo del repositorio y estado técnico inferido. |
| `.auto-readme-work/20260302_124338/language-nav-root.md` | Línea canónica de opciones de idioma para `README.md` raíz. |
| `.auto-readme-work/20260302_124338/language-nav-i18n.md` | Línea canónica de opciones de idioma para README i18n. |
| `.auto-readme-work/20260302_124338/translation-plan.txt` | Mapeo de locales y plan de archivos objetivo i18n. |
| `.auto-readme-work/<older-run-id>/...` | Contexto histórico de ejecuciones previas del pipeline README. |

## 🔧 Prerrequisitos

- `git`
- Shell POSIX (los ejemplos usan `bash`)
- Editor compatible con Markdown

### Supuestos

- En esta instantánea del repositorio no hay un servicio ejecutable ni manifiesto de aplicación.
- Por ello, las instrucciones de instalación/build/start están orientadas al flujo de documentación.

## 📥 Instalación

Aún no hay paquete binario ni paso de compilación runtime definido.

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Uso

El uso actual es el mantenimiento de documentación y la sincronización multilingüe.

### Comandos comunes de inspección

```bash
ls -la
ls -la .auto-readme-work/20260302_124338
ls -la i18n
```

### Flujo de sincronización del README canónico

1. Leer `.auto-readme-work/20260302_124338/pipeline-context.md`.
2. Verificar plantillas del selector de idioma en `language-nav-root.md` y `language-nav-i18n.md`.
3. Actualizar `README.md` incrementalmente como fuente de verdad.
4. Alinear archivos `i18n/README.*.md` con la misma estructura y detalles técnicos clave.
5. Confirmar que existe exactamente un banner y exactamente un panel de soporte.

## ⚙️ Configuración

Todavía no existe configuración de runtime. El comportamiento documental se guía por artefactos del repositorio.

- `pipeline-context.md`: objetivos y restricciones de ejecución.
- `repo-structure-analysis.md`: evidencia de la instantánea y brechas.
- `language-nav-root.md` y `language-nav-i18n.md`: consistencia de navegación.
- `translation-plan.txt`: objetivos de locale y mapeo.

## 🧪 Ejemplos

### Ejemplo 1: Verificar plantillas de navegación por idioma

```bash
cat .auto-readme-work/20260302_124338/language-nav-root.md
cat .auto-readme-work/20260302_124338/language-nav-i18n.md
```

### Ejemplo 2: Revisar plan de locales

```bash
cat .auto-readme-work/20260302_124338/translation-plan.txt
```

### Ejemplo 3: Confirmar ausencia de manifiestos de runtime (instantánea actual)

```bash
find . -maxdepth 2 \
  \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

## 🛠️ Notas de desarrollo

- Preservar secciones sustantivas y enlaces del historial del README canónico.
- Priorizar ediciones incrementales sobre reescrituras destructivas.
- Mantener solo un banner y un bloque de soporte.
- Mantener sincronizadas las estructuras del README raíz y los i18n.
- Declarar supuestos con claridad cuando no se conozcan detalles de runtime o infraestructura.
- Aplicar la tríada filosófica como guardarraíl activo:
  - **Sear creation tools** para redacción de alta señal.
  - **Self-healing tools** para reparar consistencia.
  - **Chain of prompt tools** para handoff reproducible entre etapas del pipeline.

## 🚑 Solución de problemas

### Solo veo archivos Markdown y artefactos del pipeline

Eso es lo esperado en la fase bootstrap actual.

### Las líneas del selector de idioma difieren entre archivos

Usa las plantillas canónicas en:

- `.auto-readme-work/20260302_124338/language-nav-root.md`
- `.auto-readme-work/20260302_124338/language-nav-i18n.md`

### Mi rama está detrás

```bash
git fetch origin
git pull --ff-only
```

### Quiero añadir instrucciones de runtime

Añade instrucciones de build/run solo después de introducir manifiestos concretos (por ejemplo: `package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`) y confirmar rutas en este repositorio.

## 🗺️ Roadmap

1. Fortalecer **sear creation tools** con plantillas estandarizadas de redacción README, compuertas de calidad por sección y verificaciones más claras de evidencia-a-salida.
2. Expandir **self-healing tools** con verificaciones automáticas para bloques duplicados, deriva de locales, anchors internos rotos y referencias de ejecución obsoletas.
3. Formalizar **chain of prompt tools** entre etapas de ejecución para trazas reproducibles de contexto, generación, traducción y verificación.
4. Añadir un flujo de mantenimiento de documentación en un solo comando cuando se introduzcan scripts en el repo.
5. Añadir comprobaciones CI para calidad Markdown, integridad de enlaces y paridad estructural i18n.
6. Introducir componentes de runtime concretos cuando se añadan manifiestos de código fuente y entrypoints.
7. Publicar una decisión de licencia estable y añadir un archivo de licencia independiente.

### Roadmap por foco de principio

| Área de enfoque | Objetivo cercano |
| --- | --- |
| **Sear creation tools** | Mejorar plantillas de redacción y prompts de sección respaldados por evidencia. |
| **Self-healing tools** | Automatizar detección de duplicados, revisión de anchors obsoletos y reparación de deriva de locales. |
| **Chain of prompt tools** | Estandarizar contratos de artefactos por etapa para salidas multilingües reproducibles. |

## 🤝 Contribución

Las contribuciones son bienvenidas.

1. Abre un issue describiendo el cambio propuesto.
2. Crea una rama enfocada.
3. Mantén ediciones de documentación incrementales y fieles al repositorio.
4. Preserva enlaces importantes, comandos y contexto histórico sustantivo.
5. Abre un pull request con notas concisas de verificación.

### Flujo sugerido

```bash
git checkout -b docs/your-update
# edit README.md and/or i18n/README.*.md
git add README.md i18n/README.*.md
git commit -m "docs: refine README content"
git push -u origin docs/your-update
```

## 📄 Licencia

TBD. Se planea un archivo de licencia independiente, pero aún no está presente en la instantánea actual.


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
