[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# AgInTi

[![Status](https://img.shields.io/badge/status-initializing-orange)](#aginti)
[![Docs](https://img.shields.io/badge/docs-readme_draft-blue)](#aginti)
[![Repository Stage](https://img.shields.io/badge/stage-bootstrap-yellow)](#aginti)
[![i18n](https://img.shields.io/badge/i18n-planned-0ea5e9)](#aginti)
[![License](https://img.shields.io/badge/license-TBD-lightgrey)](#aginti)

## 📌 개요

AgInTi는 현재 초기화/스캐폴딩 단계에 있습니다. 이 README 초안 작성 시점에 저장소에는 주로 다음이 포함되어 있습니다.

- Git 메타데이터 (`.git/`)
- 다국어 README 파일을 위해 준비된 `i18n/` 디렉터리
- README 생성 파이프라인 컨텍스트와 언어 계획 산출물을 담은 `.auto-readme-work/` 작업 공간

현재 워킹 트리에서는 애플리케이션 소스 코드, 패키지 매니페스트, 런타임 엔트리포인트, CI 워크플로가 감지되지 않았습니다.

### 저장소 스냅샷

| 항목 | 현재 상태 |
| --- | --- |
| Source code | 아직 감지되지 않음 |
| Runtime manifests | 아직 감지되지 않음 |
| CI workflows | 아직 감지되지 않음 |
| Documentation workspace | `.auto-readme-work/20260228_184104/` |
| i18n directory | 존재함 (`i18n/`) |

## 🚦 프로젝트 상태

이 문서는 저장소의 **첫 번째 완성형 README 초안**입니다.

- 관찰된 저장소 상태: **최상위 소스 트리가 아직 없음**
- 기존의 정본 README 기준선: **이번 실행 중 로컬 워크스페이스에서 확인되지 않음**
- 본 문서의 작성 원칙: 저장소에서 확인된 정확한 정보를 보존하고, 알 수 없는 내용은 삭제나 추측 없이 명확히 표시

원격 브랜치/히스토리에 정본 성격의 기존 README가 있다면, 이 초안으로 대체하기보다 해당 내용과 점진적으로 병합해야 합니다.

## ✨ 기능 (현재)

현재 저장소의 기능은 문서화/파이프라인 중심입니다.

- `.auto-readme-work/` 하위의 README 생성 파이프라인 작업 공간
- 다국어 README 대상 계획(영어 포함 11개 언어)
- 루트 및 `i18n/`용 언어 전환 템플릿

제품/런타임 기능 계획은 이 단계에서 아직 알려져 있지 않습니다.

## 🗂️ 프로젝트 구조

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

### 주요 문서 입력

| 파일 | 용도 |
| --- | --- |
| `.auto-readme-work/20260228_184104/pipeline-context.md` | 이번 실행의 README 제약사항과 생성 워크플로 컨텍스트를 정의합니다. |
| `.auto-readme-work/20260228_184104/repo-structure-analysis.md` | 감지된 저장소 구조와 확인된 공백(미구현 영역)을 요약합니다. |
| `.auto-readme-work/20260228_184104/language-nav-root.md` | 루트 `README.md`용 표준 언어 전환 한 줄을 제공합니다. |
| `.auto-readme-work/20260228_184104/language-nav-i18n.md` | `i18n/` 하위 번역 파일용 표준 언어 전환 한 줄을 제공합니다. |
| `.auto-readme-work/20260228_184104/translation-plan.txt` | 번역 대상 로케일과 파일 매핑을 정의합니다. |

## 🧰 사전 요구사항

현재 상태 그대로 저장소 내용을 사용하는 데 필요한 런타임 사전 요구사항은 없습니다.

문서화 워크플로와 저장소 작업을 위해 일반적으로 다음이 필요합니다.

- `git`
- POSIX 호환 셸(예시는 `bash` 사용)
- 텍스트 에디터

## 📥 설치

아직 애플리케이션/패키지 매니페스트가 없으므로 설치/빌드 단계는 없습니다.

저장소를 클론하세요.

```bash
git clone git@github.com:lachlanchen/AgInTi.git
cd AgInTi
```

## ▶️ 사용법

현재 실질적인 사용 방식은 저장소 점검과 README/i18n 문서 작업입니다.

예시:

```bash
# Show top-level files
ls -la

# Inspect auto-generated README context files
ls -la .auto-readme-work/20260228_184104

# Inspect i18n directory
ls -la i18n
```

## ⚙️ 설정

현재 애플리케이션 설정 파일은 감지되지 않았습니다.

확인된 저장소 설정 신호:

- Git 원격이 `origin git@github.com:lachlanchen/AgInTi.git`로 구성됨
- 다국어 README 내비게이션 및 대상 로케일 매핑이 `.auto-readme-work/20260228_184104/`에 존재

## 🧪 예제

### Example 1: README 언어 내비게이션 일관성 검증

```bash
# Compare language switcher templates used by the pipeline
cat .auto-readme-work/20260228_184104/language-nav-root.md
cat .auto-readme-work/20260228_184104/language-nav-i18n.md
```

### Example 2: 번역 대상 집합 확인

```bash
cat .auto-readme-work/20260228_184104/translation-plan.txt
```

### Example 3: 저장소에 아직 런타임 매니페스트가 없는지 확인

```bash
# Typical manifest check (expected: none in current state)
find . -maxdepth 2 \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml \)
```

## 🛠️ 개발 노트

- 저장소는 초기 부트스트랩 단계로 보입니다.
- 다국어 구조를 준비한 README 우선 구성 작업이 진행 중입니다.
- 구조 분석 시점 기준 로컬 커밋 히스토리는 감지되지 않았습니다(분석 컨텍스트에 `No commits yet on main` 기록).
- 소스 코드를 추가할 때는 이 README를 실제 설정, 사용법, 설정 지침으로 최신화하세요.

## 🩺 문제 해결

### 이전/로컬 복사본에서 `README.md`가 없는 경우

로컬 클론에 `README.md`가 포함되어 있지 않았다면 최신 브랜치 상태로 동기화하세요.

```bash
git fetch origin
git pull --ff-only
```

### `i18n/`은 있지만 번역 파일이 없는 경우

초기 초안 단계에서는 정상입니다. 번역 대상은 다음에 정의되어 있습니다.

- `.auto-readme-work/20260228_184104/translation-plan.txt`

### 프로젝트 런타임 스택이 불명확한 경우

`src/`, 매니페스트, 엔트리포인트가 보이지 않는다면 현재 관찰 상태와 일치합니다. 구현 파일이 추가되면 스택 정보를 함께 기록하세요.

## 🗺️ 로드맵

가까운 시일 내 문서화 및 프로젝트 부트스트랩 목표:

- 실제 프로젝트 목적과 아키텍처를 반영한 기준 영어 README 확정
- 번역 계획에 따라 `i18n/` 하위에 번역 README 파일 추가
- 애플리케이션 소스 레이아웃과 런타임 매니페스트 도입
- 재현 가능한 설정 및 실행 명령 추가
- 코드베이스가 생기면 CI 점검(lint/test/docs validation) 추가

## 🤝 기여

기여를 환영합니다. 저장소가 초기 설정 단계이므로:

1. 제안 변경사항(문서, 구조, 초기 코드 레이아웃)을 설명하는 이슈를 먼저 열어 주세요.
2. 기능 브랜치를 생성하세요.
3. 변경 범위를 작게 유지하고 문서화하세요.
4. 동작이나 구조가 바뀌면 README/i18n 문서를 함께 업데이트하세요.
5. 맥락과 검증 절차를 명확히 포함해 풀 리퀘스트를 제출하세요.

권장 로컬 워크플로:

```bash
git checkout -b feat/your-change
# make edits

git add .
git commit -m "Describe your change"
git push -u origin feat/your-change
```

## 💬 지원

현재 저장소 파일에는 전용 지원, 스폰서, 후원 채널이 선언되어 있지 않습니다.

향후 지원 링크가 추가되면 이 섹션에 반영하고, README 개정 시에도 유지하세요.

## 📄 라이선스

현재 저장소 내용에는 라이선스 정보가 선언되어 있지 않습니다.

- 상태: `TBD`
- 권장 다음 단계: `LICENSE` 파일을 추가하고 이 섹션에 정확한 SPDX 식별자를 기재

## 🧾 가정 및 보존 노트

- 이 초안은 `/home/lachlan/ProjectsLFS/AgInTi`에 현재 존재하는 저장소 파일을 바탕으로 작성되었습니다.
- 생성 시점에 정본 성격의 기존 README를 로컬에서 확인할 수 없어, 그로부터 실질 내용을 가져올 수 없었습니다.
- 보존 정책에 따라 알 수 없거나 누락된 정보는 추측하거나 생략하지 않고 명시적으로 표시했습니다.
