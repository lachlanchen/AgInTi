[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Repository](https://img.shields.io/badge/Repository-AgInTi-0f172a?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lachlanchen/AgInTi)
[![Docs](https://img.shields.io/badge/Docs-README%20Bootstrap-0ea5e9?style=for-the-badge&logo=mdbook&logoColor=white)](#aginti)
[![Localization](https://img.shields.io/badge/i18n-10%20locales-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)](#documentation-inputs-and-generated-artifacts)
[![Status](https://img.shields.io/badge/Stage-Documentation%20Pipeline-f59e0b?style=for-the-badge&logo=githubactions&logoColor=white)](#scope-and-snapshot)
[![License](https://img.shields.io/badge/License-TBD-94a3b8?style=for-the-badge&logo=readme&logoColor=white)](#license)

Recurso de documentación con enfoque en README para mantener un README principal en inglés y documentación multilingüe sincronizada.

## 🧭 Navegación rápida

| Tipo | Destino |
|---|---|
| Flujo del repositorio | [Alcance y snapshot](#-scope-and-snapshot) |
| Casos de uso | [Uso](#-usage) |
| Guía de contribución | [Contribución](#-contribution) |
| Soporte del proyecto | [Support](#-support) |

---

[![Pipeline](https://img.shields.io/badge/Pipeline-.auto--readme--work-0f172a?style=flat-square&logo=githubactions&logoColor=white)](./.auto-readme-work)
[![Locales](https://img.shields.io/badge/Locales-10%20files-22c55e?style=flat-square&logo=googletranslate&logoColor=white)](./i18n)
[![Scope](https://img.shields.io/badge/Scope-Documentation-0ea5e9?style=flat-square&logo=mdbook&logoColor=white)](#documentation-inputs-and-generated-artifacts)

## 📌 A simple vista

| 🎯 Enfoque | 🧩 Valor actual |
| --- | --- |
| Objetivo del repositorio | Andamiaje para documentación de README sincronizado en múltiples idiomas |
| Invariante principal | Las ediciones incrementales preservan el historial sustantivo |
| Estado actual | No se detecta una aplicación o servicio en ejecución en la instantánea del repositorio |

| ✅ Snapshot | 📌 Estado actual |
| --- | --- |
| Fase del repositorio | Estructura bootstrap impulsada por `.auto-readme-work/` |
| Localizaciones | 10 variantes de README traducidas |
| Ejecución verificada | No se detectó una app o servicio ejecutable |

## 📌 Resumen general

AgInTi es un repositorio de **andamiaje de documentación**.

El repositorio se centra en documentación-first (README-first), la base de localización y los artefactos de flujo de trabajo iterativo utilizados para generar documentación multilingüe consistente.

- ✅ Aún no se detecta ningún árbol de código fuente de ejecución principal.
- ✅ `i18n/` contiene 10 variantes de README traducidas.
- ✅ `.auto-readme-work/` almacena artefactos de pipeline para actualizaciones iterativas de documentación.
- ✅ El contenido sustantivo existente se conserva mediante ediciones incrementales.

## ✅ Alcance y snapshot

| Ítem | Estado actual |
|---|---|
| 🧩 Código fuente | No detectado |
| 🧪 Pruebas/CI | No detectado |
| 📘 Flujo de documentación | Gestionado por `.auto-readme-work/` |
| 🌐 Documentación localizada | 10 locales mantenidas |
| 🔒 Archivo de licencia | No presente en esta instantánea |

## ✨ Características

- Estrategia de documentación centrada en README.
- Flujo con conciencia de idioma y enlaces canónicos para páginas raíz y localizadas.
- Bloques de banner y de soporte deduplicados en posiciones definidas.
- Actualizaciones incrementales que preservan secciones sustantivas.
- Snippets prácticos de inspección y verificación para quienes aportan documentación.

## 🗂️ Estructura del proyecto

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

## 🧱 Modelo de arquitectura y flujo de trabajo

En esta etapa, la “arquitectura” es el pipeline de documentación del repositorio:

1. Por cada ejecución se generan contexto y restricciones en `.auto-readme-work/<run-id>/pipeline-context.md`.
2. Se producen plantillas de selector de idioma en `language-nav-root.md` / `language-nav-i18n.md`.
3. Se aplican ediciones incrementales al README para mantener intacta la historia sustantiva.
4. Los archivos localizados se sincronizan desde la misma plantilla estructural.

## 📚 Entradas de documentación y artefactos generados

| Archivo | Propósito |
|---|---|
| `.auto-readme-work/20260301_070633/pipeline-context.md` | Restricciones e instrucciones para esta ejecución. |
| `.auto-readme-work/20260301_070633/translation-plan.txt` | Mapeo de locales para la sincronización multilingüe. |
| `.auto-readme-work/20260301_070633/language-nav-root.md` | Línea canónica de navegación de idiomas para `README.md`. |
| `.auto-readme-work/20260301_070633/language-nav-i18n.md` | Línea canónica de navegación de idiomas para READMEs traducidos. |
| `.auto-readme-work/20260301_070633/repo-structure-analysis.md` | Snapshot del repositorio usado en este ciclo de generación. |
| `README.md.auto-readme-support*` | Manifiestos auxiliares de soporte usados durante pases previos de bootstrap. |

## 🧭 Objetivos del flujo del repositorio

Este repositorio es intencionalmente ligero. El objetivo a largo plazo es mantener el README raíz y las variantes traducidas sincronizados sin perder contexto técnico, enlaces y estructura.

## 🧰 Prerrequisitos

- `git` para acceso al repositorio.
- Un shell POSIX (los ejemplos usan `bash`).
- Un editor compatible con Markdown.

### Suposiciones de ejecución

No hay requisitos de compilación o ejecución definidos todavía porque aún no se detectaron manifiestos de producto ejecutable en este repositorio.

## 📥 Instalación

No existe aún un proceso de instalación binaria o de compilación.

```bash
# Clonar el repositorio
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Uso

El uso actual se centra en mantenimiento de documentación y consistencia multilingüe.

### Comandos comunes

```bash
ls -la
ls -la .auto-readme-work/20260301_070633
ls -la i18n
```

### Flujo típico de sincronización de README

1. Revisar el contexto de ejecución en `.auto-readme-work/20260301_070633/pipeline-context.md`.
2. Verificar plantillas del selector de idioma en `.auto-readme-work/20260301_070633/language-nav-*.md`.
3. Editar `README.md` de manera incremental; no eliminar secciones sustantivas.
4. Mantener banner y soporte únicos y en las posiciones requeridas.
5. Alinear los archivos traducidos en `i18n/README.*.md` a la misma estructura cuando sea necesario.

## ⚙️ Configuración

Aún no existe configuración de aplicación. El comportamiento documental del repositorio se define por los artefactos de workflow en `.auto-readme-work/` y los archivos de localización en `i18n/`.

- `pipeline-context.md` (restricciones y objetivos)
- `translation-plan.txt` (alcance y mapeo de locales)
- `language-nav-root.md` y `language-nav-i18n.md` (consistencia de navegación)
- `README.md.auto-readme-support*` (helpers de scaffold)

## 🧪 Ejemplos

### Ejemplo 1: Verificar las líneas del selector de idioma

```bash
cat .auto-readme-work/20260301_070633/language-nav-root.md
cat .auto-readme-work/20260301_070633/language-nav-i18n.md
```

### Ejemplo 2: Validar locales compatibles y archivos de traducción

```bash
cat .auto-readme-work/20260301_070633/translation-plan.txt
```

### Ejemplo 3: Confirmar estado del scaffold

```bash
find . -maxdepth 2 \
  \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

## 🛠️ Notas de desarrollo

- Usa ediciones incrementales para preservar el contexto técnico previo.
- No agregues pasos de compilación/ejecución sin manifiestos concretos presentes.
- Asegura que banner y soporte aparezcan solo una vez.
- Expresa supuestos cuando el comportamiento del repositorio sea desconocido.
- Mantén los ejemplos de comandos vinculados a archivos y directorios existentes.

## 🩺 Solución de problemas

### Solo veo archivos Markdown

Esto es esperable en esta fase de bootstrap.

### El selector de idioma parece inconsistente

Compara cada `README.*.md` con la línea de idiomas principal y con los archivos más recientes de contexto de pipeline en `.auto-readme-work/20260301_070633/`.

### Mi rama está desactualizada

```bash
git fetch origin
git pull --ff-only
```

### Quiero agregar instrucciones de código

Solo agrega comandos de compilación/ejecución después de incluir manifiestos concretos (por ejemplo `package.json`, `pyproject.toml`, `Cargo.toml`, etc.) y confirmar que esos activos existen en el repositorio.

## 🗺️ Hoja de ruta

- Introducir componentes concretos de aplicación/ejecución.
- Expandir guías de instalación, ejecución y despliegue cuando haya código y herramientas.
- Añadir validaciones de CI para calidad de Markdown y paridad de locales.
- Mantener reproducible el proceso de traducción mediante pipelines versionados explícitos.
- Añadir orientación de contribución tanto para documentación como para futuros colaboradores de código.

## 🤝 Contribución

Las contribuciones son bienvenidas.

1. Abre un issue describiendo el cambio.
2. Crea una rama dedicada.
3. Mantén los cambios mínimos e incrementales.
4. Conserva las secciones significativas existentes.
5. Envía un pull request con notas de verificación concisas.

### Flujo sugerido

```bash
git checkout -b docs/your-update
# editar README.md y/o i18n/
git add README.md
git commit -m "docs: refine README draft"
git push -u origin docs/your-update
```

## 📄 Licencia

La licencia aún no está incluida en la instantánea de este repositorio.


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
