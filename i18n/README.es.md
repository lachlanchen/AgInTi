[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# AgInTi

[![Status](https://img.shields.io/badge/status-initializing-orange)](#aginti)
[![Docs](https://img.shields.io/badge/docs-readme_draft-blue)](#aginti)
[![Repository Stage](https://img.shields.io/badge/stage-bootstrap-yellow)](#aginti)
[![i18n](https://img.shields.io/badge/i18n-planned-0ea5e9)](#aginti)
[![License](https://img.shields.io/badge/license-TBD-lightgrey)](#aginti)

## 📌 Resumen

AgInTi se encuentra actualmente en una fase de inicialización/estructura base. En el momento de este borrador del README, el repositorio contiene principalmente:

- Metadatos de Git (`.git/`)
- Un directorio `i18n/` preparado para archivos README multilingües
- Un espacio de trabajo `.auto-readme-work/` que contiene el contexto del pipeline de generación de README y artefactos de planificación de idiomas

No se detectaron código fuente de aplicación, manifiestos de paquetes, puntos de entrada de ejecución ni flujos de trabajo de CI en el árbol de trabajo actual.

### Instantánea del repositorio

| Elemento | Estado actual |
| --- | --- |
| Código fuente | Aún no detectado |
| Manifiestos de ejecución | Aún no detectados |
| Flujos de trabajo de CI | Aún no detectados |
| Espacio de trabajo de documentación | `.auto-readme-work/20260228_184104/` |
| Directorio i18n | Presente (`i18n/`) |

## 🚦 Estado del proyecto

Este es el **primer borrador completo del README** para el repositorio.

- Estado del repositorio observado: **todavía no hay un árbol de código fuente de nivel superior**
- Línea base del README canónico existente: **no presente en el espacio de trabajo local durante esta ejecución**
- Enfoque de documentación usado aquí: preservar todos los detalles detectados y fieles al repositorio, y etiquetar claramente las incógnitas en lugar de eliminar o inventar contenido

Si existe un README canónico histórico en una rama remota o en el historial, este borrador debería integrarse de forma incremental con ese contenido en lugar de reemplazar secciones sustantivas.

## ✨ Funcionalidades (actuales)

Las capacidades actuales del repositorio están orientadas a documentación/pipeline:

- Espacio de trabajo del pipeline de generación de README en `.auto-readme-work/`
- Planificación de objetivos README multilingües (11 idiomas, incluido inglés)
- Plantillas de navegación por idioma para la raíz y `i18n/`

Las funcionalidades de producto/ejecución previstas son desconocidas en esta etapa.

## 🗂️ Estructura del proyecto

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

### Entradas clave de documentación

| Archivo | Propósito |
| --- | --- |
| `.auto-readme-work/20260228_184104/pipeline-context.md` | Define las restricciones del README y el contexto del flujo de generación para esta ejecución. |
| `.auto-readme-work/20260228_184104/repo-structure-analysis.md` | Resume la estructura detectada del repositorio y las brechas conocidas. |
| `.auto-readme-work/20260228_184104/language-nav-root.md` | Línea canónica del selector de idioma para el `README.md` raíz. |
| `.auto-readme-work/20260228_184104/language-nav-i18n.md` | Línea canónica del selector de idioma para los archivos traducidos bajo `i18n/`. |
| `.auto-readme-work/20260228_184104/translation-plan.txt` | Mapeo de configuración regional a archivo para traducciones. |

## 🧰 Requisitos previos

Actualmente no se requieren requisitos de ejecución para usar el contenido del repositorio tal como está.

Para el flujo de documentación y operaciones de repositorio, probablemente necesitarás:

- `git`
- Un shell compatible con POSIX (los ejemplos usan `bash`)
- Un editor de texto

## 📥 Instalación

Como todavía no hay manifiesto de aplicación/paquete, no existe paso de instalación/compilación.

Clona el repositorio:

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ Uso

El uso práctico actual es la inspección del repositorio y el trabajo de documentación README/i18n.

Ejemplos:

```bash
# Show top-level files
ls -la

# Inspect auto-generated README context files
ls -la .auto-readme-work/20260228_184104

# Inspect i18n directory
ls -la i18n
```

## ⚙️ Configuración

Actualmente no se detectaron archivos de configuración de la aplicación.

Señales de configuración conocidas del repositorio:

- Remoto de Git configurado como `origin git@github.com:lachlanchen/AgInTi.git`
- Navegación README multilingüe y mapeos de idiomas objetivo en `.auto-readme-work/20260228_184104/`

## 🧪 Ejemplos

### Ejemplo 1: Validar consistencia de la navegación de idioma del README

```bash
# Compare language switcher templates used by the pipeline
cat .auto-readme-work/20260228_184104/language-nav-root.md
cat .auto-readme-work/20260228_184104/language-nav-i18n.md
```

### Ejemplo 2: Confirmar conjunto de objetivos de traducción

```bash
cat .auto-readme-work/20260228_184104/translation-plan.txt
```

### Ejemplo 3: Verificar que el repositorio aún no tiene manifiestos de ejecución

```bash
# Typical manifest check (expected: none in current state)
find . -maxdepth 2 \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml \)
```

## 🛠️ Notas de desarrollo

- El repositorio parece estar en una etapa temprana de arranque.
- La configuración README-first está en progreso, con estructura multilingüe preparada.
- No se detectó historial local de commits durante el análisis de estructura (en el contexto de análisis se indicó `No commits yet on main`).
- Al añadir código fuente, mantén este README actualizado con instrucciones concretas de configuración, uso y configuración.

## 🩺 Solución de problemas

### Falta `README.md` en copias locales/antiguas

Si tu clon local no incluía previamente `README.md`, sincroniza desde el estado más reciente de la rama:

```bash
git fetch origin
git pull --ff-only
```

### Existe `i18n/` pero faltan archivos traducidos

Esto es esperable en una etapa temprana de borrador. Los objetivos de traducción están definidos en:

- `.auto-readme-work/20260228_184104/translation-plan.txt`

### Stack de ejecución del proyecto no claro

Si no ves `src/`, manifiestos o puntos de entrada, esto coincide con el estado observado actual. Añade detalles del stack cuando se incorporen archivos de implementación.

## 🗺️ Hoja de ruta

Objetivos de corto plazo para documentación y arranque del proyecto:

- Finalizar el README base en inglés con el propósito real del proyecto y su arquitectura
- Añadir archivos README traducidos bajo `i18n/` según el plan de traducción
- Introducir el diseño del código fuente de la aplicación y manifiesto(s) de ejecución
- Añadir comandos reproducibles de configuración y ejecución
- Añadir verificaciones de CI (lint/test/validación de docs) cuando exista la base de código

## 🤝 Contribuir

Las contribuciones son bienvenidas. Dado que el repositorio está en configuración inicial:

1. Abre un issue describiendo el cambio propuesto (docs, estructura o diseño inicial del código).
2. Crea una rama de funcionalidad.
3. Mantén cambios enfocados y documentados.
4. Actualiza la documentación README/i18n cuando cambie el comportamiento o la estructura.
5. Envía un pull request con contexto claro y pasos de verificación.

Flujo de trabajo local sugerido:

```bash
git checkout -b feat/your-change
# make edits

git add .
git commit -m "Describe your change"
git push -u origin feat/your-change
```

## 💬 Soporte

Actualmente no hay canales dedicados de soporte, patrocinio o donaciones declarados en los archivos del repositorio.

Si se añaden enlaces de soporte más adelante, inclúyelos aquí y consérvalos en futuras revisiones del README.

## 📄 Licencia

La información de licencia no está declarada en el contenido actual del repositorio.

- Estado: `TBD`
- Siguiente paso recomendado: añadir un archivo `LICENSE` y actualizar esta sección con el identificador SPDX exacto.

## 🧾 Suposiciones y notas de preservación

- Este borrador está construido a partir de los archivos del repositorio actualmente presentes en `/home/lachlan/ProjectsLFS/AgInTi`.
- Un README canónico preexistente no estaba disponible localmente en el momento de la generación; por lo tanto, no se pudo importar contenido sustantivo desde él.
- Según la política de preservación, los detalles desconocidos o faltantes se marcan explícitamente en lugar de adivinarse u omitirse.
