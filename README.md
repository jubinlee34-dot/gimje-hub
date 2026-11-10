# 김제 AI 실습허브 (gimje-hub)

김제 사회복지 종사자를 위한 **AI·Canva 교육자료실** 프로젝트입니다.

## 교육 구성

| 회차 | 일자 | 내용 |
|---|---|---|
| 1회차 | 2026-11-11 | 김제 사회복지업무와 AI 활용 (ChatGPT·문서 업무·홍보 포스터) |
| 2회차 | 2026-11-13 | 김제 사회복지업무와 Canva (홍보 포스터·AI 영상 제작/편집) |

## 연결 링크

### GitHub · 개발
- [프로젝트 저장소](https://github.com/jubinlee34-dot/gimje-hub)
- [README](https://github.com/jubinlee34-dot/gimje-hub/blob/main/README.md)
- [Issues · 오류 및 작업 관리](https://github.com/jubinlee34-dot/gimje-hub/issues)
- [Pull requests · 코드 검토](https://github.com/jubinlee34-dot/gimje-hub/pulls)
- [Actions · 자동 검증](https://github.com/jubinlee34-dot/gimje-hub/actions)

### Notion · 교육 기획 정본
- [김제 사회복지협의회 2회기 전체 기획](https://app.notion.com/p/40bbaa25b968808c909bc64c901f8f56)
- [1회차 · 11/11 AI 활용 교육안](https://app.notion.com/p/40cbaa25b96881fdb2c1e3dd84909e1b)
- [2회차 · 11/13 Canva 교육안](https://app.notion.com/p/40cbaa25b96881509cd0d274b0f92545)

### 서비스 · 배포 (연결 예정)
- **수강생 자료실:** 배포 URL 미확정
- **관리자 로그인:** 배포 URL 확정 후 연결 예정 (예정 경로: `/admin/login`)
- **Vercel 프로젝트:** 연결 전 · 주소 미확정

> 아직 서비스가 배포되지 않았으므로 가상의 사이트 주소를 기재하지 않습니다. 배포와 실접속 QA가 완료되면 위 항목을 실제 링크로 업데이트합니다.

## 예정 기능 및 보안 원칙

- 수강생 화면: **1회차 / 2회차 / 기타자료** 조회 및 자료 열기
- 관리자 화면: 교육자료·외부 링크의 등록·교체·삭제
- 관리자 URL을 숨기는 방식만으로 보호하지 않고 **서버 인증·권한 검사** 적용
- 비밀번호와 GitHub 토큰은 저장소나 클라이언트 코드에 기록하지 않음
- 변경사항은 QA 시나리오(정상·오류·권한·회귀) 검증 후 배포

## 현재 상태

- GitHub 저장소 생성 완료
- README에 프로젝트·연결 링크 정리
- 서비스 코드, 실제 배포, 관리자 E2E 테스트: **아직 미확인/미완료**

_최종 문서 정리: 2026-11-10_
