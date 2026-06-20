# 실패 기록 001: 파일 복사 PermissionError

## 날짜
2026-06-20

## 상황
`shutil.copy2()`로 docx 파일을 복사할 때 `PermissionError: [WinError 32]` 발생

## 원인
- Word나 다른 프로세스가 파일을 사용 중
- 파일이 열려있는 상태에서 복사 시도

## 해결 방법
1. 파일을 닫은 후 재시도
2. `try/except`로 3회까지 재시도
3. 수동으로 파일 닫기

##教训
- Windows에서는 파일 사용 중 복사 불가
- 대용량 파일 처리 시 프로세스 확인 필요
