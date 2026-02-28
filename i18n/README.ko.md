[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Repository](https://img.shields.io/badge/Repository-AgInTi-0f172a?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lachlanchen/AgInTi)
[![Docs](https://img.shields.io/badge/Docs-README%20Bootstrap-0ea5e9?style=for-the-badge&logo=mdbook&logoColor=white)](#aginti)
[![Localization](https://img.shields.io/badge/i18n-10%20locales-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)](#documentation-inputs-and-generated-artifacts)
[![Status](https://img.shields.io/badge/Stage-Documentation%20Pipeline-f59e0b?style=for-the-badge&logo=githubactions&logoColor=white)](#scope-and-snapshot)
[![License](https://img.shields.io/badge/License-TBD-94a3b8?style=for-the-badge&logo=readme&logoColor=white)](#license)

영문 기준 전체 README와 동기화된 다국어 README를 유지 관리하기 위한 문서 우선(Documentation-first) 저장소 스캐폴드입니다.

## 🧭 빠른 탐색

| 유형 | 이동 대상 |
|---|---|
| 저장소 워크플로우 | [범위 및 스냅샷](#-scope-and-snapshot) |
| 사용 예시 | [사용법](#-usage) |
| 기여 가이드 | [기여하기](#-contribution) |
| 프로젝트 지원 | [지원하기](#-support) |

---

[![Pipeline](https://img.shields.io/badge/Pipeline-.auto--readme--work-0f172a?style=flat-square&logo=githubactions&logoColor=white)](./.auto-readme-work)
[![Locales](https://img.shields.io/badge/Locales-10%20files-22c55e?style=flat-square&logo=googletranslate&logoColor=white)](./i18n)
[![Scope](https://img.shields.io/badge/Scope-Documentation-0ea5e9?style=flat-square&logo=mdbook&logoColor=white)](#documentation-inputs-and-generated-artifacts)

## 📌 한눈에 보기

| 🎯 핵심 초점 | 🧩 현재 값 |
| --- | --- |
| 저장소 목적 | 영문 README와 동기화된 다국어 문서 스캐폴드 |
| 핵심 불변 조건 | 증분 편집으로 기존 실질적 이력 보존 |
| 현재 상태 | 저장소 스냅샷에서 런타임 앱/서비스 미탐지 |

---

| ✅ 스냅샷 | 📌 현재 상태 |
| --- | --- |
| 저장소 단계 | `.auto-readme-work/` 기반 부트스트랩 스캐폴드 |
| 지역화 | 번역된 README 10개 파일 |
| 런타임 검증 | 실행 가능한 앱 또는 서비스 미탐지 |

## 📌 개요

AgInTi는 **문서 부트스트랩** 저장소입니다.

이 저장소는 README 우선 문서화, 지역화 스캐폴드, 그리고 일관된 다국어 문서를 생성하기 위한 반복형 워크플로우 산출물을 중심으로 구성됩니다.

- ✅ 최상위 런타임 소스 트리는 아직 탐지되지 않았습니다.
- ✅ `i18n/`에는 번역된 README가 10개 있습니다.
- ✅ `.auto-readme-work/`는 반복형 문서 업데이트를 위한 파이프라인 산출물을 저장합니다.
- ✅ 기존 내용은 증분 업데이트 방식으로 보존됩니다.

## ✅ 범위 및 스냅샷

| 항목 | 현재 상태 |
|---|---|
| 🧩 소스 코드 | 탐지되지 않음 |
| 🧪 테스트/CI | 탐지되지 않음 |
| 📘 문서 워크플로우 | `.auto-readme-work/` 기반 |
| 🌐 로컬라이즈 문서 | 유지되는 로케일 10개 |
| 🔒 라이선스 파일 | 이번 스냅샷에서 존재하지 않음 |

## ✨ 기능

- README 우선 저장소 문서 전략.
- 루트와 지역화 페이지를 위한 정식 링크가 포함된 언어 인식형 워크플로우.
- 지정된 위치에서 배너와 지원 블록의 중복 제거.
- 기존 의미 있는 섹션을 보존하는 증분 업데이트.
- 문서 기여자를 위한 실용적인 검증 스니펫 제공.

## 🗂️ 프로젝트 구조

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

## 🧱 아키텍처 및 워크플로우 모델

현재 단계에서는 “아키텍처”가 바로 저장소의 문서 파이프라인을 의미합니다.

1. 실행마다 `.auto-readme-work/<run-id>/pipeline-context.md`에서 컨텍스트와 제약 조건이 생성됩니다.
2. 언어 선택기 템플릿이 `language-nav-root.md` / `language-nav-i18n.md`에 생성됩니다.
3. 기존 실질적 이력을 유지하면서 README 편집이 증분 적용됩니다.
4. 지역화 파일은 동일한 구조 템플릿으로 동기화됩니다.

## 📚 문서 입력과 생성 산출물

| 파일 | 용도 |
|---|---|
| `.auto-readme-work/20260301_070633/pipeline-context.md` | 이번 패스의 제약 조건 및 지침 소스 |
| `.auto-readme-work/20260301_070633/translation-plan.txt` | 다국어 동기화를 위한 로케일 매핑 |
| `.auto-readme-work/20260301_070633/language-nav-root.md` | `README.md`용 표준 언어 네비게이션 라인 |
| `.auto-readme-work/20260301_070633/language-nav-i18n.md` | 번역본 README용 표준 언어 네비게이션 라인 |
| `.auto-readme-work/20260301_070633/repo-structure-analysis.md` | 이번 생성 패스에 사용된 저장소 스냅샷 |
| `README.md.auto-readme-support*` | 이전 부트스트랩 단계에서 사용된 보조 지원 파일 |

## 🧭 저장소 워크플로우 목표

이 저장소는 의도적으로 경량으로 구성되어 있습니다. 장기 목표는 루트 README와 번역본을 기술적 맥락, 링크, 구조를 손상하지 않고 동기화 상태로 유지하는 것입니다.

## 🧰 필수 조건

- 저장소 접근을 위한 `git`.
- POSIX 셸(예시에서는 `bash` 사용).
- 마크다운 인식 편집기.

### 런타임 가정

현재 저장소 스냅샷에서 실행 가능한 제품 매니페스트가 감지되지 않았으므로 빌드/런타임 요구사항은 아직 정의되지 않았습니다.

## 📥 설치

아직 바이너리 설치 또는 빌드 절차가 없습니다.

```bash
# Clone the repository
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ 사용법

현재 사용법은 문서 유지보수와 다국어 일관성 관리에 중점을 둡니다.

### 공통 명령

```bash
ls -la
ls -la .auto-readme-work/20260301_070633
ls -la i18n
```

### 전형적인 README 동기화 워크플로우

1. `.auto-readme-work/20260301_070633/pipeline-context.md`의 실행 컨텍스트를 검토합니다.
2. `.auto-readme-work/20260301_070633/language-nav-*.md`의 언어 전환 템플릿을 확인합니다.
3. `README.md`를 증분으로 편집하며 기존의 의미 있는 섹션을 삭제하지 않습니다.
4. 배너와 지원 섹션이 각각 한 번씩만 남도록 유지합니다.
5. 필요 시 `i18n/README.*.md`를 동일한 구조로 정렬합니다.

## ⚙️ 설정

아직 애플리케이션 구성은 존재하지 않습니다. 저장소 수준 문서 동작은 `.auto-readme-work/`의 워크플로 산출물과 `i18n/`의 로케일 파일로 정의됩니다.

- `pipeline-context.md` (제약 조건 및 목표)
- `translation-plan.txt` (로케일 범위 및 매핑)
- `language-nav-root.md` 및 `language-nav-i18n.md` (네비게이션 일관성)
- `README.md.auto-readme-support*` (스캐폴딩 도우미)

## 🧪 예시

### 예시 1: 언어 선택기 라인 확인

```bash
cat .auto-readme-work/20260301_070633/language-nav-root.md
cat .auto-readme-work/20260301_070633/language-nav-i18n.md
```

### 예시 2: 지원 로케일 및 번역 파일 검증

```bash
cat .auto-readme-work/20260301_070633/translation-plan.txt
```

### 예시 3: 스캐폴드 상태 확인

```bash
find . -maxdepth 2 \
  \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

## 🛠️ 개발 노트

- 기존의 기술 맥락을 보존하려면 증분 편집만 사용하세요.
- 구체적인 매니페스트 파일이 존재할 때까지 실행/빌드 단계는 추가하지 마세요.
- 배너와 지원 섹션은 한 번만 표시되도록 유지하세요.
- 저장소 동작이 불분명할 때는 가정 사항을 명시하세요.
- 명령 예시는 기존 파일과 디렉터리로 연결해야 합니다.

## 🩺 문제 해결

### 마크다운 파일만 보입니다

이 부트스트랩 단계에서는 이것이 정상입니다.

### 언어 전환기가 일관되지 않아 보입니다

각 `README.*.md`를 루트의 언어 네비게이터 줄과 `.auto-readme-work/20260301_070633/`의 최신 파이프라인 컨텍스트에 맞춰 비교하세요.

### 내 브랜치가 뒤쳐졌습니다

```bash
git fetch origin
git pull --ff-only
```

### 코드 지침을 추가하고 싶습니다

구체적인 매니페스트(예: `package.json`, `pyproject.toml`, `Cargo.toml` 등)가 추가되고 저장소에 해당 자산이 존재함이 확인된 뒤에만 빌드/실행 명령을 추가합니다.

## 🗺️ 로드맵

- 구체적인 애플리케이션/런타임 구성요소를 도입합니다.
- 코드와 툴링이 준비되면 설치, 런타임, 배포 가이드를 확장합니다.
- Markdown 품질 및 로케일 동등성 검증 CI를 추가합니다.
- 버전 관리된 파이프라인으로 번역 절차의 재현성을 유지합니다.
- 문서 및 향후 코드 기여자 모두를 위한 기여 안내를 추가합니다.

## 🤝 기여

기여를 환영합니다.

1. 변경 내용을 설명하는 이슈를 생성합니다.
2. 전용 브랜치를 만듭니다.
3. 변경은 최소화하고 증분으로 유지합니다.
4. 기존의 의미 있는 섹션을 보존합니다.
5. 간결한 검증 노트를 포함해 PR을 제출합니다.

### 제안 워크플로

```bash
git checkout -b docs/your-update
# edit README.md and/or i18n/
git add README.md
git commit -m "docs: refine README draft"
git push -u origin docs/your-update
```

## 📄 라이선스

이 저장소 스냅샷에는 라이선스가 아직 포함되어 있지 않습니다.


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
