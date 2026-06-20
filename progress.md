# Progress - 진행 상황 기록

## 2026-06-20

### 완료한 작업
1. ✅ git 저장소 초기화
2. ✅ .gitignore 생성
3. ✅ ruff 0.15.18 설치 및 설정
4. ✅ opencode python-linter 에이전트 생성
5. ✅ AGENTS.md 구조화
6. ✅ src/, tests/ 디렉토리 생성
7. ✅ 기본 모듈 작성 (src/core.py)
8. ✅ 테스트 코드 작성 (tests/test_core.py)
9. ✅ pytest 9.1.1 설치
10. ✅ ruff 린팅 검사 통과
11. ✅ pytest 테스트 2개 통과

### 발생한 문제
- ruff가 사전 설치되어 있지 않음 → pip install ruff로 해결
- pytest가 사전 설치되어 있지 않음 → pip install pytest로 해결
- ruff 린팅 오류 (줄 끝 개행문자 누락) → ruff check --fix로 자동 해결

### 다음 할 일
1. AGENTS.md에서 Task 2 완료 처리
2. Task 3 (기능 구현) 시작
3. CI/CD 설정 (GitHub Actions 등)

### 메모
- 하네스 엔지니어링 구조 적용 시작
- AGENTS.md에 작업 분해, 완료 기준, 코딩 컨벤션 정리 완료
- warm start 전략 적용: 기본 프로젝트 구조 미리 만들어둠