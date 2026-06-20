# AGENTS.md - 프로젝트 가이드라인

## 참고 문서
작업 전 아래 문서를 반드시 확인하세요.

- 기술 결정: `docs/decisions/` — 왜 이 구조인지 이유가 담겨 있습니다
- 실패 기록: `docs/failures/` — 시도하면 안 되는 방법 목록입니다
- 용어 사전: `docs/domain/glossary.md` — 도메인 용어의 정확한 의미
- 코딩 규칙: `docs/conventions/` — 명명, 에러 처리, 테스트 규칙

## 프로젝트 개요
- **이름**: D:\code proj
- **언어**: Python 3.10+
- **목적**: TBD

## 프로젝트 구조
```
D:\code proj\
├── AGENTS.md              # 이 파일
├── opencode.json          # opencode 설정
├── pyproject.toml         # Python 도구 설정
├── progress.md            # 진행 상황 기록
├── src/                   # 소스 코드
├── tests/                 # 테스트 코드
├── scripts/               # 자동화 스크립트
└── docs/                  # 문서
    ├── decisions/         # 기술 결정 기록 (ADR)
    ├── conventions/       # 코딩 규칙 상세 설명
    ├── domain/            # 비즈니스 도메인 지식
    └── failures/          # 실패 기록
```

## 작업 분해 (Task Breakdown)

### Task 1: 프로젝트 초기 설정
- [x] git 저장소 초기화
- [x] .gitignore 생성
- [x] ruff 설치 및 설정
- [x] opencode 에이전트 설정
- **완료 기준**: `ruff check .` 정상 작동

### Task 2: 기본 구조 만들기
- [x] src/ 디렉토리 생성
- [x] tests/ 디렉토리 생성
- [x] __init__.py 파일 생성
- [x] 기본 모듈 작성 (src/core.py)
- [x] 테스트 코드 작성 (tests/test_core.py)
- [x] pytest 설치 및 테스트 통과
- **완료 기준**: `python -m pytest` 테스트 통과 ✅

### Task 3: 기능 구현
- [ ] TBD
- **완료 기준**: TBD

## 코딩 컨벤션

### 스타일 가이드
- PEP 8 준수
- 라인 길이: 88자
- 따옴표: 더블 쿼트 (")
- 들여쓰기: 4칸

### Import 규칙
```python
# 1. 표준 라이브러리
import os
import sys

# 2. 서드파티 라이브러리
import requests

# 3. 로컬 모듈
from . import my_module
```

### 명명 규칙
- 클래스: PascalCase (`MyClass`)
- 함수/변수: snake_case (`my_function`)
- 상수: UPPER_SNAKE_CASE (`MAX_VALUE`)
- 파일명: snake_case (`my_module.py`)

## 검증 시스템

### 린팅
```bash
ruff check .           # 린팅 검사
ruff check --fix .     # 자동 수정
ruff format .          # 포맷 적용
```

### 테스트
```bash
python -m pytest       # 전체 테스트 실행
python -m pytest -v    # 상세 결과
python -m pytest -x    # 첫 실패 시 중지
```

## 에이전트 역할

### python-linter
- **역할**: 코드 품질 검사
- **명령어**: `ruff check`, `ruff format`
- **동작**: 파일 변경 시 자동 실행

### general
- **역할**: 일반적인 작업 수행
- **사용 시점**: 복잡한 작업, 여러 파일 수정 필요 시

### explore
- **역할**: 코드베이스 탐색
- **사용 시점**: 파일 검색, 구조 파악

## 피드백 루프

1. **코드 작성** → python-linter가 린팅 검사
2. **테스트 실행** → pytest로 결과 확인
3. **문제 발견** → AGENTS.md에 규칙 추가
4. **반복 개선** → 컨벤션 업데이트

## 진행 상황 기록

작업 완료 시 progress.md에 기록:
- 날짜
- 완료한 작업
- 발생한 문제
- 다음 할 일

## 뻥뚜리 에이전트 (행정법 빈칸 문제 생성)

### 작업 규칙
1. **세션 시작 시**: `word proj/뻥뚜리_명세서.md` 반드시 읽기
2. **작업 중**: 명세서의 규칙 준수
3. **작업 완료 후**: 명세서와 progress.md 업데이트

### 핵심 파일
- `word proj/뻥뚜리_명세서.md` — 요구사항 명세서
- `word proj/law_terms_db.json` — 핵심 단어 DB
- `word proj/create_quiz_db.py` — 문제 생성 스크립트
- `progress.md` — 진행 상황 기록
