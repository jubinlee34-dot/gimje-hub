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

### 서비스 · GitHub Pages (연결 예정)
- **배포 방식:** GitHub Pages — 별도 Vercel 연결 없음
- **배포 원본:** `main` 브랜치의 `/(root)` (정적 HTML 방식)
- **예상 수강생 URL:** `https://jubinlee34-dot.github.io/gimje-hub/` (**아직 배포·접속 검증 안 됨**)
- **자료 관리자:** [GitHub 저장소 관리](https://github.com/jubinlee34-dot/gimje-hub) — GitHub 로그인 및 저장소 쓰기 권한으로 관리
- **Pages 설정:** [Settings → Pages](https://github.com/jubinlee34-dot/gimje-hub/settings/pages)

> 현재 저장소는 **Private**임. GitHub Free에서는 Pages를 Public 저장소로 게시해야 하며, GitHub Pro 이상에서는 Private 저장소 Pages도 지원됨. Pages 결과 사이트는 일반적으로 공개 접근 가능하므로 민감 자료를 업로드하지 않음. 저장소 공개 범위는 소유자가 별도 결정.
>
> GitHub Pages는 정적 호스팅이므로 서버 측 관리자 비밀번호 로그인·파일 변경 API를 제공하지 않음. 숨겨진 관리자 URL이나 브라우저 JavaScript에 GitHub 토큰·비밀번호를 넣지 않음.

## 운영 기능 및 보안 원칙

- **수강생:** GitHub Pages에서 1회차 / 2회차 / 기타자료를 조회하고 새 탭으로 자료를 열기
- **관리자:** 별도 자체 로그인 페이지 대신 GitHub 저장소의 로그인·권한으로 파일 및 링크 데이터를 등록·교체·삭제
- **자동 배포:** GitHub Pages 활성화 후 소스 변경 시 Pages 빌드/게시
- **보안:** GitHub 토큰·비밀번호를 HTML/JS/JSON 또는 README에 저장하지 않음
- **자료 조회:** Private 저장소의 Contents API를 수강생 브라우저에서 직접 조회하면 인증 없이 실패할 수 있으므로, Pages에 함께 게시하는 정적 자료 목록(JSON 매니페스트)과 상대경로를 사용하도록 설계
- **검증:** 등록/교체/삭제, 파일 링크, 빈 목록, 잘못된 JSON, 경로 처리, 수강생 화면 회귀, Pages 배포 결과 확인
- **경로 주의:** 프로젝트 Pages는 `/gimje-hub/` 아래 게시되므로 루트 절대경로(`/session1`) 대신 상대경로를 사용

## 현재 상태

- GitHub 저장소 생성 완료
- README에 프로젝트·Notion·GitHub 링크 정리
- 배포 방식을 GitHub Pages로 확정, Vercel 미사용
- GitHub Pages 설정 및 실제 사이트 접속: **미확인/미완료**
- 정적 사이트 코드 및 수강생 자료 조회 QA: **미확인/미완료**

## GitHub Pages 배포 설정 안내

1. 저장소에 `index.html` 등 정적 진입 파일을 커밋한다.
2. `Settings → Pages → Build and deployment`에서 **Deploy from a branch**를 선택한다.
3. Branch는 `main`, Folder는 `/(root)` 선택 후 **Save**한다.
4. `Actions`의 Pages 배포 결과와 실제 URL 접속을 확인한다.
5. Private 저장소에서 Pages 설정이 불가능하면 저장소 공개 전환 필요 여부와 계정 요금제를 먼저 확인한다.

_최종 문서 정리: 2026-11-10 · GitHub Pages 배포 방식 반영_
