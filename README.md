# 김제 AI 실습허브 (gimje-hub)

김제 사회복지 종사자를 위한 AI·Canva 강의안 및 실습자료실. **Vercel 없이 GitHub Pages로 운영**합니다.

## 연결 링크

| 항목 | 링크 |
|---|---|
| GitHub 저장소 | https://github.com/jubinlee34-dot/gimje-hub |
| GitHub Actions · QA 및 배포 | https://github.com/jubinlee34-dot/gimje-hub/actions |
| Pages 설정 | https://github.com/jubinlee34-dot/gimje-hub/settings/pages |
| 예상 배포 주소 (아직 미검증) | https://jubinlee34-dot.github.io/gimje-hub/ |
| 김제 사회복지협의회 2회기 Notion | https://app.notion.com/p/40bbaa25b968808c909bc64c901f8f56 |
| 1회차 11월 11일 AI 교육안 | https://app.notion.com/p/40cbaa25b96881fdb2c1e3dd84909e1b |
| 2회차 11월 13일 Canva 교육안 | https://app.notion.com/p/40cbaa25b96881509cd0d274b0f92545 |

## 교육 구성 및 관리자 자료 등록

- **1회차 (11/11):** ChatGPT·사회복지 문서 업무·홍보 포스터
- **2회차 (11/13):** Canva 홍보 포스터·AI 영상 제작 및 편집
- **기타 자료:** 공통 파일, 외부 참고 링크

**관리자 인증은 GitHub가 담당**합니다. 수강생 사이트에서 별도 아이디/비밀번호를 입력하지 않습니다.

1. [저장소](https://github.com/jubinlee34-dot/gimje-hub)에 GitHub 계정으로 로그인합니다.
2. 해당 폴더의 Add file → Upload files 메뉴로 자료를 등록하고 main 브랜치에 커밋합니다.
   - **session1/**: 1회차 AI
   - **session2/**: 2회차 Canva
   - **etc/**: 기타 자료
3. 자료 교체/삭제도 같은 폴더에서 GitHub의 파일 변경 기능을 이용합니다.
4. 커밋 후 [Actions](https://github.com/jubinlee34-dot/gimje-hub/actions)에서 자동 QA 및 Pages 배포 결과를 확인합니다.
5. 성공 후 수강생 페이지의 자료 링크를 실제로 열어 검증합니다.

외부 링크는 etc 폴더에 JSON 파일을 만들고 아래처럼 입력합니다.

    {"name":"참고 사이트","url":"https://example.com"}

링크 JSON은 URL만 목록에 반영되며, 원본 JSON 파일은 공개 사이트로 복사되지 않습니다.

## GitHub Pages 설정 (필수)

GitHub 저장소 **Settings → Pages → Build and deployment → Source → GitHub Actions**를 선택합니다. main에 커밋하면 워크플로가 Python QA → JavaScript 문법 검사 → 정적 목록 자동 생성 → Pages 게시를 수행합니다.

**주의:** 예전에 안내한 Deploy from a branch/(root)는 현재 자동 목록 생성 방식과 다릅니다. **GitHub Actions**를 사용해야 최신 자료가 자동 표시됩니다.

현재 저장소는 Private이며 GitHub Free에서는 Private 저장소 GitHub Pages 배포가 제한될 수 있습니다. Private Pages 이용 가능 요금제이거나 Public 저장소로 전환되어야 합니다. 저장소 공개 범위 변경은 소유자 판단으로 남깁니다. Pages에 게시된 콘텐츠는 일반인이 접근할 수 있으므로 민감정보를 업로드하지 마세요.

## 주요 소스 파일

- index.html : 수강생 1·2회차 및 기타 자료 목록
- admin.html : 강사용 GitHub 파일 관리 안내 (별도 로그인 페이지가 아님)
- assets/style.css : 베이지 반응형 UI
- assets/app.js : 안전한 DOM 기반 목록 조회 및 XSS 방어
- session1/ · session2/ · etc/ : 강의안 및 기타자료 등록 장소
- scripts/build_site.py : 저장소 자료 → 공개 배포용 정적 목록/파일 생성
- tests/test_build_site.py : 자동 QA 12개 시나리오
- .github/workflows/pages.yml : GitHub Pages 자동 QA·배포

## 보안 및 운영 원칙

- 브라우저에 GitHub 토큰·비밀번호 저장 금지. 관리자 전용 업로드 API를 가장하지 않음.
- Private 저장소 GitHub Contents API를 수강생 브라우저에서 호출하지 않음. 빌드에서 정적 JSON을 만들어 제공.
- 파일명·표시 이름은 textContent로 렌더링. 외부 URL은 HTTP(S)만 허용.
- 최대 파일 크기 **10,000,000바이트**. 허용 확장자: HTML, HTM, PDF, PPT, PPTX, DOC, DOCX, XLS, XLSX, TXT, CSV, ZIP, PNG, JPG, JPEG, GIF, WebP.
- HTML 파일은 스크립트를 실행할 수 있으므로 강사가 신뢰하는 파일만 등록.
- 수강생 개인 작성 데이터는 이 허브 서버에서 수집하지 않음. 개별 HTML 자체의 데이터 저장·복원은 별도 QA.
- 자동 QA 성공은 실제 배포 접속·교안 동작 확인의 대체가 아님.

_2026-11-10 기준_
