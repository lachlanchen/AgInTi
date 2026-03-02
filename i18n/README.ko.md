[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AgInTi

[![Repository](https://img.shields.io/badge/Repository-AgInTi-0f172a?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lachlanchen/AgInTi)
[![Docs](https://img.shields.io/badge/Docs-README%20Bootstrap-0ea5e9?style=for-the-badge&logo=mdbook&logoColor=white)](#aginti)
[![Localization](https://img.shields.io/badge/i18n-10%20locales-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)](#프로젝트-구조)
[![Status](https://img.shields.io/badge/Stage-Documentation%20Pipeline-f59e0b?style=for-the-badge&logo=githubactions&logoColor=white)](#범위-및-스냅샷)
[![License](https://img.shields.io/badge/License-TBD-94a3b8?style=for-the-badge&logo=readme&logoColor=white)](#라이선스)
[![Principle-Sear%20Creation-ef4444?style=flat-square&logo=firefox&logoColor=white)](#개요)
[![Principle-Self--Healing-10b981?style=flat-square&logo=wrench&logoColor=white)](#기능)
[![Principle-Chain%20of%20Prompt%20Tools-3b82f6?style=flat-square&logo=chainlink&logoColor=white)](#아키텍처)

완전한 영어 README와 동기화된 다국어 문서를 유지하기 위한 문서 중심 저장소 스캐폴드입니다. 운영 원칙은 **sear creation tools**, **self-healing tools**, **chain of prompt tools**의 세 축으로 구성됩니다.

## 🧭 빠른 이동

| 유형 | 이동 |
| --- | --- |
| 프로젝트 요약 | [개요](#개요) |
| 핵심 기능 | [기능](#기능) |
| 파이프라인 설계 | [아키텍처](#아키텍처) |
| 철학 요약 | [철학 한눈에 보기](#철학-한눈에-보기) |
| 기여 워크플로 | [개발 노트](#개발-노트) |
| 향후 방향 | [로드맵](#로드맵) |
| 프로젝트 지원 | [Support](#-support) |

---

## 📌 범위 및 스냅샷

| 항목 | 현재 상태 |
| --- | --- |
| 저장소 단계 | 문서 부트스트랩 스캐폴드 |
| 런타임 코드 | 현재 스냅샷에서 미확인 |
| 테스트/CI 파이프라인 | 현재 스냅샷에서 미확인 |
| 로컬라이즈 문서 | `i18n/` 아래 10개 로케일 파일 |
| 파이프라인 산출물 | `.auto-readme-work/` 아래 타임스탬프 실행 기록 |
| 라이선스 파일 | 독립 파일 없음 (README 배지: TBD) |
| 철학 기준선 | Sear creation + self-healing + chain of prompt tools |

## 🌍 개요

AgInTi는 현재 런타임 애플리케이션이 아니라 README 수명주기 및 로컬라이제이션 파이프라인으로 동작합니다. 루트 `README.md`가 정본(canonical)이며, `i18n/`의 각 언어 버전은 이 정본 구조를 기준으로 동기화됩니다.

프로젝트 철학은 장식이 아니라 실제 운영 기준입니다. 모든 README 업데이트는 아래 세 원칙을 동시에 충족해야 합니다.

1. **Sear creation tools**: 제약된 저장소 근거에서 신호 밀도가 높은 실용 문서를 의도적으로 날카로운 작성 흐름으로 생성합니다.
2. **Self-healing tools**: 드리프트를 교정하고, 중복을 제거하며, 구조 일관성을 복원하는 복구 지향 메커니즘입니다.
3. **Chain of prompt tools**: 파이프라인 실행 전 구간에서 컨텍스트-출력 계보를 보존하는 단계형·추적형 프롬프트 흐름입니다.

이 저장소는 링크, 명령어, 지원 메타데이터를 유지하면서 점진적 업데이트로 의미 있는 과거 내용을 보존합니다.

### 철학 한눈에 보기

| 원칙 | 의도 | 운영 결과 |
| --- | --- | --- |
| **Sear creation tools** | 제약된 근거에서 신호 밀도가 높은 문서 생성 | 섹션이 실용적이고 구체적이며 저장소 근거에 기반함 |
| **Self-healing tools** | 드리프트, 중복, 오래된 구조 복구 | 정본 README와 다국어 README를 정렬된 상태로 유지 |
| **Chain of prompt tools** | 생성 단계를 명시적이고 추적 가능하게 유지 | 파이프라인 산출물에 재현 가능한 컨텍스트/인수인계 보존 |

## ✨ 기능

- 루트 문서를 정본으로 두는 README 중심 문서 전략
- 10개 i18n README 변형 간 다국어 동기화
- `.auto-readme-work/<run-id>/` 산출물 기반 파이프라인 작성
- 배너 1개, 지원 패널 1개 불변식으로 시각 블록 중복 방지
- 의미 있는 기술 이력을 보존하는 점진 업데이트 규율

### 원칙-기능 매핑

| 핵심 원칙 | 현재 기능에서의 반영 방식 |
| --- | --- |
| **Sear creation tools** | 저장소 근거 기반의 정밀 README 초안 작성과 안정적인 섹션 스캐폴드 |
| **Self-healing tools** | 중복 배너/지원 블록, 오래된 참조, 구조 드리프트에 대한 중복 제거 점검 |
| **Chain of prompt tools** | 재현 가능한 출력을 위한 실행별 산출물 체인(`pipeline-context`, 내비 템플릿, 번역 계획) |

## 🗂️ 프로젝트 구조

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

## 🏗️ 아키텍처

현 단계에서의 아키텍처는 애플리케이션 런타임 아키텍처가 아니라 문서 파이프라인 아키텍처를 의미합니다.

### 파이프라인 흐름

1. 실행별 컨텍스트를 `.auto-readme-work/<run-id>/pipeline-context.md`에 기록합니다.
2. 언어 내비게이션 템플릿(`language-nav-root.md`, `language-nav-i18n.md`)을 생성합니다.
3. 정본 README 콘텐츠를 `README.md`에서 점진적으로 갱신합니다.
4. `i18n/`의 각 언어 README를 정본 구조에 맞춰 정렬합니다.
5. 구조 품질 점검으로 중복 제거, 링크 일관성, 기술 세부 보존을 강제합니다.

### 아키텍처 속 핵심 원칙

- **Sear creation tools**: 섹션을 구체적이고 완전하며 저장소 사실에 맞게 구성하는 콘텐츠 작성 단계에 적용됩니다.
- **Self-healing tools**: 중복 블록 제거, 오래된 실행 참조 복구, 구조적 동등성 회복을 위한 검증 단계에 적용됩니다.
- **Chain of prompt tools**: 생성 전 단계 산출물 전반에 적용되어 각 단계가 명시 가능하고 감사 가능하도록 유지합니다.

### 파이프라인 단계별 원칙 체크포인트

| 단계 | Sear creation tools | Self-healing tools | Chain of prompt tools |
| --- | --- | --- | --- |
| 컨텍스트 수집 | 날카로운 생성 제약 정의 | 누락/잘못된 입력 조기 탐지 | 원본 프롬프트와 실행 메타데이터 보존 |
| 정본 초안 작성 | 저장소 근거로 완전한 README 섹션 구성 | 회귀 및 우발적 콘텐츠 손실 방지 | 단계 산출물을 이전 산출물과 연결 유지 |
| i18n 정렬 | 로케일 전반 구조/기술 동등성 유지 | 루트와 i18n 파일 간 드리프트 교정 | 정본 의도를 각 로컬라이즈 버전에 전달 |
| 최종 검증 | 가독성과 세부 보존 강제 | 중복 배너/지원 블록, 오래된 참조 제거 | 실행별 감사 가능한 산출물 이력 유지 |

## 🧾 문서 입력과 생성 산출물

| 파일 | 목적 |
| --- | --- |
| `.auto-readme-work/20260302_124338/pipeline-context.md` | 이번 생성 패스의 원본 제약과 목표 |
| `.auto-readme-work/20260302_124338/repo-structure-analysis.md` | 저장소 스캔 요약 및 추론된 기술 상태 |
| `.auto-readme-work/20260302_124338/language-nav-root.md` | 루트 `README.md`용 정본 언어 옵션 라인 |
| `.auto-readme-work/20260302_124338/language-nav-i18n.md` | i18n README용 정본 언어 옵션 라인 |
| `.auto-readme-work/20260302_124338/translation-plan.txt` | 로케일 매핑 및 i18n 대상 파일 계획 |
| `.auto-readme-work/<older-run-id>/...` | 이전 README 파이프라인 실행의 이력 컨텍스트 |

## 🔧 사전 요구사항

- `git`
- POSIX shell (examples use `bash`)
- Markdown-capable editor

### 가정

- 현재 저장소 스냅샷에는 실행 가능한 서비스 또는 애플리케이션 매니페스트가 없습니다.
- 따라서 설치/빌드/시작 안내는 문서 워크플로 중심으로 작성됩니다.

## 📥 설치

아직 바이너리 패키지나 런타임 빌드 단계는 정의되어 있지 않습니다.

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ 사용법

현재 사용 시나리오는 문서 유지보수와 다국어 동기화입니다.

### 자주 쓰는 점검 명령어

```bash
ls -la
ls -la .auto-readme-work/20260302_124338
ls -la i18n
```

### 정본 README 동기화 워크플로

1. `.auto-readme-work/20260302_124338/pipeline-context.md`를 읽습니다.
2. `language-nav-root.md`, `language-nav-i18n.md`의 언어 선택 템플릿을 검증합니다.
3. 소스 오브 트루스로서 `README.md`를 점진적으로 갱신합니다.
4. `i18n/README.*.md` 파일을 동일한 구조와 핵심 기술 세부로 정렬합니다.
5. 배너가 정확히 1개이고 지원 패널도 정확히 1개인지 확인합니다.

## ⚙️ 설정

아직 런타임 설정은 없습니다. 문서 동작은 저장소 산출물에 의해 구동됩니다.

- `pipeline-context.md`: 실행 목표와 제약
- `repo-structure-analysis.md`: 스냅샷 근거와 공백
- `language-nav-root.md` and `language-nav-i18n.md`: 내비게이션 일관성
- `translation-plan.txt`: 로케일 대상과 매핑

## 🧪 예시

### 예시 1: 언어 내비게이션 템플릿 확인

```bash
cat .auto-readme-work/20260302_124338/language-nav-root.md
cat .auto-readme-work/20260302_124338/language-nav-i18n.md
```

### 예시 2: 로케일 계획 점검

```bash
cat .auto-readme-work/20260302_124338/translation-plan.txt
```

### 예시 3: 런타임 매니페스트 부재 확인 (현재 스냅샷)

```bash
find . -maxdepth 2 \
  \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name pom.xml \)
```

## 🛠️ 개발 노트

- 정본 README 이력의 실질적 섹션과 링크를 보존합니다.
- 파괴적 재작성보다 점진 편집을 우선합니다.
- 배너와 지원 블록은 각각 하나만 유지합니다.
- 루트와 i18n README 구조를 동기화 상태로 유지합니다.
- 런타임/인프라 세부가 불명확할 때는 가정을 명확히 표기합니다.
- 철학 3요소를 능동적 가드레일로 적용합니다.
  - 고신호 초안을 위한 **Sear creation tools**
  - 일관성 복구를 위한 **Self-healing tools**
  - 파이프라인 단계 간 재현 가능한 인수인계를 위한 **Chain of prompt tools**

## 🚑 문제 해결

### Markdown 파일과 파이프라인 산출물만 보입니다

현재 부트스트랩 단계에서는 정상입니다.

### 파일마다 언어 선택 줄이 다릅니다

아래 정본 템플릿을 사용하세요.

- `.auto-readme-work/20260302_124338/language-nav-root.md`
- `.auto-readme-work/20260302_124338/language-nav-i18n.md`

### 내 브랜치가 뒤처졌습니다

```bash
git fetch origin
git pull --ff-only
```

### 런타임 지침을 추가하고 싶습니다

구체적인 매니페스트(예: `package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`)를 추가하고 이 저장소 내 경로를 확인한 뒤에만 빌드/실행 지침을 추가하세요.

## 🗺️ 로드맵

1. 표준 README 초안 템플릿, 섹션 품질 게이트, 더 명확한 근거-출력 점검으로 **sear creation tools**를 강화합니다.
2. 중복 블록, 로케일 드리프트, 깨진 내부 앵커, 오래된 실행 참조를 자동 점검해 **self-healing tools**를 확장합니다.
3. 재현 가능한 컨텍스트/생성/번역/검증 추적을 위해 실행 단계 전반에 **chain of prompt tools**를 공식화합니다.
4. 저장소 스크립트가 도입되면 단일 명령 문서 유지보수 흐름을 추가합니다.
5. 마크다운 품질, 링크 무결성, i18n 구조 동등성에 대한 CI 점검을 추가합니다.
6. 소스 매니페스트와 엔트리포인트가 추가되면 구체적인 런타임 컴포넌트를 도입합니다.
7. 안정적인 라이선스 결정을 공개하고 독립 라이선스 파일을 추가합니다.

### 원칙 초점별 로드맵

| 초점 영역 | 단기 목표 |
| --- | --- |
| **Sear creation tools** | 초안 템플릿과 근거 기반 섹션 프롬프트 개선 |
| **Self-healing tools** | 중복 탐지, 오래된 앵커 점검, 로케일 드리프트 복구 자동화 |
| **Chain of prompt tools** | 재현 가능한 다국어 출력을 위해 실행 단계 산출물 계약 표준화 |

## 🤝 기여

기여를 환영합니다.

1. 의도한 변경 내용을 설명하는 이슈를 엽니다.
2. 범위를 좁힌 브랜치를 생성합니다.
3. 문서 수정은 점진적이고 저장소 사실에 맞게 유지합니다.
4. 중요한 링크, 명령어, 실질적 이력 맥락을 보존합니다.
5. 간결한 검증 메모와 함께 풀 리퀘스트를 엽니다.

### 권장 흐름

```bash
git checkout -b docs/your-update
# edit README.md and/or i18n/README.*.md
git add README.md i18n/README.*.md
git commit -m "docs: refine README content"
git push -u origin docs/your-update
```

## 📄 라이선스

TBD. 독립 라이선스 파일을 추가할 예정이지만 현재 스냅샷에는 아직 없습니다.


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
