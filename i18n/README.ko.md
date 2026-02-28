[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Status](https://img.shields.io/badge/status-initializing-orange)](#aginti)
[![Docs](https://img.shields.io/badge/docs-readme_draft-blue)](#aginti)
[![Repository%20Stage](https://img.shields.io/badge/stage-bootstrap-yellow)](#aginti)
[![i18n](https://img.shields.io/badge/i18n-planned-0ea5e9)](#aginti)
[![License](https://img.shields.io/badge/license-TBD-lightgrey)](#aginti)

*README 우선 부트스트랩 저장소 • 문서 우선 워크플로 • 다국어 문서화가 적극적으로 계획됨.*

| Focus | Current state |
|---|---|
| Core maturity | Bootstrap scaffold (`README`-first) |
| Localization | 10 locales maintained in `i18n/` |
| Pipeline source | `.auto-readme-work/20260301_064213/` |

---

## 📌 개요

AgInTi는 현재 README-first 워크플로와 다국어 문서화 계획을 갖춘 문서 스캐폴드 저장소입니다.

현재 초안 기준으로 저장소 내용은 문서 조정 및 언어 준비에 초점이 맞춰져 있으며, 아직 실행 가능한 런타임 제품 중심이 아닙니다.

- ✅ 최상위 소스 트리가 아직 탐지되지 않았습니다.
- ✅ `i18n/`에 번역된 README 변형이 존재합니다.
- ✅ `.auto-readme-work/20260301_064213/`은 이번 패스의 활성 파이프라인 컨텍스트를 저장합니다.
- ✅ `.auto-readme-work/20260228_184104/`은 참고용 이력 산출물로 남겨져 있습니다.

### 저장소 스냅샷

| 항목 | 현재 상태 |
|---|---|
| 🧩 소스 코드 | 아직 탐지되지 않음 |
| ⚙️ 런타임 매니페스트 | 아직 탐지되지 않음 |
| 🧪 CI 워크플로우 | 아직 탐지되지 않음 |
| 🧭 문서 작업 공간 | `.auto-readme-work/20260301_064213/` |
| 🌐 번역 문서 | `i18n/`에 10개 로케일 |

---

## 🚦 프로젝트 상태

이 README는 증분 업데이트 방식의, 저장소 기준 정확도를 갖춘 첫 번째 완성된 영어 초안입니다.

- 상태는 여전히 부트스트랩/문서 중심입니다.
- 기존 실질 섹션은 대체하지 않고 유지/보완했습니다.
- 미확인 항목은 추측 없이 명시적으로 표시했습니다.

실제 상위 브랜치/히스토리에 정식 README가 존재한다면, 이후 업데이트에서는 이를 증분 병합해야 합니다.

---

## ✨ 기능

- README-first 문서 중심 저장소 구조
- `.auto-readme-work/` 하위 중앙 집중 다국어 README 파이프라인
- 언어 전환 템플릿과 번역 매핑 파일
- 저장소 점검 및 검증용 실무형 명령 스니펫
- 배너/지원 블록 중복 제거가 반영된 엄격 추적 README 업데이트 프로세스

---

## 🗂️ 프로젝트 구조

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

### 주요 문서 입력

| 파일 | 용도 |
|---|---|
| `.auto-readme-work/20260301_064213/pipeline-context.md` | 이번 실행의 생성 제약사항 및 프롬프트 컨텍스트 |
| `.auto-readme-work/20260301_064213/repo-structure-analysis.md` | 감지된 구조와 프로젝트 공백(누락 항목)을 요약 |
| `.auto-readme-work/20260301_064213/translation-plan.txt` | 로케일별 번역 대상과 파일 매핑 |
| `.auto-readme-work/20260301_064213/language-nav-root.md` | `README.md`용 정식 언어 선택기 라인 |
| `.auto-readme-work/20260301_064213/language-nav-i18n.md` | `i18n/` 파일용 정식 언어 선택기 라인 |

---

## 🧰 사전 요구사항

현재 저장소 상태에서는 런타임 의존성이 필요하지 않습니다.

문서 사용 및 유지보수를 위해 필요한 항목은 다음과 같습니다.

- `git`
- POSIX 셸(예시: `bash`)
- Markdown 편집용 텍스트 에디터

---

## 📥 설치

아직 설치/빌드 프로세스는 없습니다.

로컬에서 저장소를 확인하려면:

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ 사용법

현재 사용은 문서 유지보수, 감사, 로컬라이제이션 동기화입니다.

### 공통 워크플로

```bash
ls -la
ls -la .auto-readme-work/20260301_064213
ls -la i18n
```

### 일반적인 README 워크플로

1. `.auto-readme-work/20260301_064213/`의 최신 컨텍스트 산출물을 읽습니다.
2. 소스 README 및 번역 README 내용을 검토합니다.
3. 기존 실질 내용을 제거하지 않도록 증분 편집을 적용합니다.
4. 언어 선택기와 지원 블록을 모든 로케일에서 일관되게 유지합니다.

---

## ⚙️ 구성

아직 애플리케이션 구성 파일은 존재하지 않습니다.

현재 문서 수준 구성은 아래에서 관리됩니다.

- `.auto-readme-work/20260301_064213/translation-plan.txt`(로케일 대상)
- `.auto-readme-work/20260301_064213/language-nav-root.md` 및 `.../language-nav-i18n.md`의 언어 전환 템플릿
- `.auto-readme-work/20260301_064213/repo-structure-analysis.md`의 저장소 구조 컨텍스트

---

## 🧪 예제

### 예제 1: 언어 선택기 라인 확인

```bash
cat .auto-readme-work/20260301_064213/language-nav-root.md
cat .auto-readme-work/20260301_064213/language-nav-i18n.md
```

### 예제 2: 번역 범위 확인

```bash
cat .auto-readme-work/20260301_064213/translation-plan.txt
```

### 예제 3: 스캐폴드 상태 확인 (기대값: 매니페스트 없음)

```bash
find . -maxdepth 2 \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

---

## 🛠️ 개발 노트

- 이 파일을 영어 문서의 정식 기준으로 유지합니다.
- 업데이트 시 기존 실질 섹션은 보존(증분 편집 정책).
- 대응되는 코드, 매니페스트, 툴체인이 존재할 때만 실행/설치 지침을 추가합니다.
- 지원/배너 블록은 정확히 하나씩만 유지합니다.
- 기능이 도입되면 로드맵과 트러블슈팅을 즉시 갱신합니다.

---

## 🩺 트러블슈팅

### 문서 파일만 보입니다

현재 부트스트랩 상태에서는 이것이 정상이며, 소스/런타임 매니페스트가 감지되지 않았습니다.

### 로케일 문서가 일치하지 않습니다

최신 번역 계획을 사용해 README 동기화 흐름을 다시 실행하고 구조와 링크를 정규화하세요.

### 로컬 브랜치가 오래된 것 같습니다

```bash
git fetch origin
git pull --ff-only
```

---

## 🗺️ 로드맵

- 코드가 도입될 때 구체적인 제품/애플리케이션 계층을 추가합니다.
- 실제 매니페스트가 생기면 설치, 빌드, 실행 지침을 확장합니다.
- CI 워크플로우와 문서 검증 절차를 추가합니다.
- 코드와 번역 기여를 위한 기여 규칙을 확장합니다.
- 번역 README 동기화를 계속 최신 상태로 유지합니다.

---

## 🤝 기여

기여를 환영합니다.

1. 맥락과 범위를 담은 이슈를 먼저 만듭니다.
2. 전용 브랜치를 생성합니다.
3. 변경 범위를 작게 두고 증분으로 진행합니다.
4. 기존 기술 상세와 섹션 맥락을 보존합니다.
5. 검증 내용이 포함된 PR을 제출합니다.

### 제안 워크플로

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

## 📄 라이선스

아직 `LICENSE` 파일이 존재하지 않습니다.

- 상태: `TBD`
- 권장 다음 단계: 라이선스 파일을 추가하고 SPDX 식별자를 이 섹션에 기재

## 🧾 가정 및 보존 노트

- 이 초안은 `/home/lachlan/ProjectsLFS/AgInTi`의 현재 상태를 바탕으로 작성했습니다.
- 런타임 목표와 아키텍처는 커밋된 파일에 아직 반영되지 않았으므로, 본 초안은 문서화된 사실에 집중합니다.
- 이전 초안의 실질 섹션은 유지하고 필요 시 보완했습니다.
- 배너/지원 블록은 각 위치에 각각 한 번씩만 배치했습니다.
