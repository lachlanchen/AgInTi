[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Status](https://img.shields.io/badge/status-initializing-orange)](#aginti)
[![Docs](https://img.shields.io/badge/docs-readme_draft-blue)](#aginti)
[![Repository%20Stage](https://img.shields.io/badge/stage-bootstrap-yellow)](#aginti)
[![i18n](https://img.shields.io/badge/i18n-planned-0ea5e9)](#aginti)
[![License](https://img.shields.io/badge/license-TBD-lightgrey)](#aginti)

*Repositorio base centrado en documentación • Flujo de trabajo README-first • planificación multilingüe activa.*

| Enfoque | Estado actual |
|---|---|
| Madurez del núcleo | Andamiaje bootstrap (`README`-first) |
| Localización | 10 locales mantenidos en `i18n/` |
| Origen del pipeline | `.auto-readme-work/20260301_064213/` |

---

## 📌 Descripción general

AgInTi es actualmente un repositorio de andamiaje de documentación con un flujo de trabajo README-first y planificación de documentación multilingüe.

En el momento de este borrador, el contenido del repositorio se centra en la coordinación de documentación y preparación de idiomas, y aún no en un producto en ejecución:

- ✅ Aún no se detecta árbol fuente de nivel superior.
- ✅ `i18n/` contiene variantes de README traducidas.
- ✅ `.auto-readme-work/20260301_064213/` almacena el contexto de pipeline activo para esta pasada.
- ✅ `.auto-readme-work/20260228_184104/` se conserva como artefacto histórico.

### Instantánea del repositorio

| Elemento | Estado actual |
|---|---|
| 🧩 Código fuente | No detectado aún |
| ⚙️ Manifiestos de ejecución | No detectados aún |
| 🧪 Flujos de trabajo CI | No detectados aún |
| 🧭 Espacio de trabajo de documentación | `.auto-readme-work/20260301_064213/` |
| 🌐 Documentos traducidos | 10 idiomas en `i18n/` |

---

## 🚦 Estado del proyecto

Este README es un primer borrador completo en inglés, increment-only y preciso al repositorio.

- El estado permanece orientado a bootstrap/documentación.
- Se han preservado y ampliado las secciones sustantivas existentes en lugar de reemplazarlas.
- Las incógnitas se marcan explícitamente y se evitan afirmaciones especulativas.

Si existe un README canónico ascendente en una rama diferente o en el historial, las futuras actualizaciones deberían fusionarlo de forma incremental.

---

## ✨ Características

- Diseño de repositorio centrado en documentación-first
- Pipeline multilingüe README centralizado en `.auto-readme-work/`
- Plantillas explícitas de selector de idioma y archivos de mapeo de traducción
- Fragmentos de comandos prácticos para inspección y validación del repositorio
- Proceso de actualización de README estrictamente rastreado con deduplicación de bloques de soporte/banner

---

## 🗂️ Estructura del proyecto

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

### Documentación clave de entrada

| Archivo | Propósito |
|---|---|
| `.auto-readme-work/20260301_064213/pipeline-context.md` | Restricciones y contexto del prompt de generación para esta ejecución. |
| `.auto-readme-work/20260301_064213/repo-structure-analysis.md` | Resumen de la estructura detectada y brechas del proyecto. |
| `.auto-readme-work/20260301_064213/translation-plan.txt` | Mapeo de locale a archivo para variantes traducidas. |
| `.auto-readme-work/20260301_064213/language-nav-root.md` | Línea canónica del selector de idioma para `README.md`. |
| `.auto-readme-work/20260301_064213/language-nav-i18n.md` | Línea canónica del selector de idioma para archivos en `i18n/`. |

---

## 🧰 Requisitos previos

No se requieren dependencias de ejecución para el estado actual del repositorio.

Para uso y mantenimiento de documentación necesitas:

- `git`
- Una shell compatible con POSIX (los ejemplos usan `bash`)
- Un editor de texto para Markdown

---

## 📥 Instalación

Aún no hay proceso de instalación/construcción.

Para inspeccionar el repositorio localmente:

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Uso

El uso actual es mantenimiento de documentación, auditoría y sincronización de localización.

### Flujos comunes

```bash
ls -la
ls -la .auto-readme-work/20260301_064213
ls -la i18n
```

### Flujo típico de README

1. Leer los artefactos de contexto actuales en `.auto-readme-work/20260301_064213/`.
2. Revisar contenido del README fuente y traducido.
3. Aplicar ediciones incrementales para evitar quitar detalles sustantivos existentes.
4. Mantener selector de idioma y bloques de soporte coherentes entre locales.

---

## ⚙️ Configuración

Aún no existe un archivo de configuración de aplicación.

La configuración a nivel documentación actual está representada por:

- `.auto-readme-work/20260301_064213/translation-plan.txt` para objetivos de locale
- Plantillas de selector de idioma en `.auto-readme-work/20260301_064213/language-nav-root.md` y `.../language-nav-i18n.md`
- Contexto de estructura del repositorio en `.auto-readme-work/20260301_064213/repo-structure-analysis.md`

---

## 🧪 Ejemplos

### Ejemplo 1: Verificar líneas de selector de idioma

```bash
cat .auto-readme-work/20260301_064213/language-nav-root.md
cat .auto-readme-work/20260301_064213/language-nav-i18n.md
```

### Ejemplo 2: Confirmar alcance de traducción

```bash
cat .auto-readme-work/20260301_064213/translation-plan.txt
```

### Ejemplo 3: Confirmar estado de andamiaje (esperado: sin manifiestos)

```bash
find . -maxdepth 2 \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

---

## 🛠️ Notas de desarrollo

- Mantener este archivo como fuente de documentación canónica en inglés.
- Preservar secciones sustantivas al actualizar (política de edición increment-only).
- Añadir instrucciones de tiempo de ejecución solo cuando existan código, manifiestos y cadenas de herramientas correspondientes.
- Mantener bloque de soporte y banner deduplicados (exactamente uno cada uno).
- Actualizar roadmap y solución de problemas tan pronto como aterricen funcionalidades.

---

## 🩺 Solución de problemas

### Solo veo archivos de documentación

Esto es esperable en este estado de bootstrap; no se detectaron manifiestos de fuente/runtime.

### La documentación por locale es inconsistente

Usa el plan de traducción más reciente y vuelve a ejecutar tu flujo de sincronización README para normalizar estructura y enlaces.

### La rama local parece desactualizada

```bash
git fetch origin
git pull --ff-only
```

---

## 🗺️ Hoja de ruta

- Añadir la capa concreta de producto/aplicación cuando se introduzca código.
- Ampliar instrucciones de setup, build y ejecución a partir de manifiestos reales.
- Añadir flujos CI y chequeos de documentación.
- Extender estándares de contribución para código y traducciones.
- Mantener sincronizados y actualizados los READMEs traducidos.

---

## 🤝 Contribución

Las contribuciones son bienvenidas.

1. Abre un issue con contexto y alcance.
2. Crea una rama dedicada.
3. Mantén los cambios enfocados e incrementales.
4. Preserva detalles técnicos y contexto de sección existentes.
5. Abre un PR con notas de verificación claras.

### Flujo sugerido

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

## 📄 Licencia

No hay archivo `LICENSE` presente aún.

- Estado: `TBD`
- Siguiente paso recomendado: añadir un archivo de licencia y establecer el identificador SPDX aquí.

## 🧾 Suposiciones y notas de preservación

- El contenido del repositorio fue evaluado desde `/home/lachlan/ProjectsLFS/AgInTi` durante esta ejecución.
- Los objetivos de runtime y arquitectura aún no se representan en los archivos confirmados; este borrador se centra intencionalmente en hechos documentados.
- Las secciones sustantivas existentes del borrador previo fueron preservadas y ampliadas cuando fue útil.
- Los bloques de banner y soporte se insertaron una única vez para cumplir con las posiciones solicitadas.
