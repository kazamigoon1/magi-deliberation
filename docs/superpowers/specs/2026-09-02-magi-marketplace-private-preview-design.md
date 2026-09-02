# MAGI Microsoft 365 앱 제품화 설계

## 목적

MAGI Deliberation을 서로 다른 회사 테넌트의 소수 테스트 사용자가 Microsoft
Teams와 Microsoft 365 Copilot에서 설치·사용할 수 있는 비공개 앱 패키지로 만든다.
테스트 결과가 충분하면 같은 제품을 Microsoft Commercial Marketplace 및 Teams Store
제출 대상으로 확장한다.

첫 버전은 판단 지원만 제공하는 선언형 에이전트다. 외부 시스템을 호출하거나 고객
데이터를 저장하지 않는다.

## 범위

### 포함

- Microsoft 365 Agents Toolkit 호환 선언형 에이전트 앱 패키지
- Teams와 Microsoft 365 Copilot에서 동작하는 비공개 테스트용 ZIP 산출물
- 앱 브랜딩, 배포 메타데이터, 개인정보처리방침, 이용약관, 지원 안내
- 테스터·테넌트 관리자용 설치 및 검증 안내
- 패키지와 MAGI 행동 경계를 검증하는 CI
- 테스트 결과를 Marketplace 제출 조건으로 판단하는 기준

### 제외

- 액션, 커넥터, Microsoft Graph, 외부 API
- 서버, 데이터베이스, 사용자 데이터 저장, 사용량 과금
- 개인 Microsoft 계정 지원
- Marketplace 실제 제출과 상용 과금 설계

## 배포 모델

### 비공개 프리뷰

각 테스터는 Teams와 Microsoft 365 Copilot을 쓸 수 있는 회사 또는 학교 계정을
사용한다. 릴리스 담당자는 버전별 앱 ZIP과 SHA-256 체크섬을 GitHub Release로
제공한다. 테스터의 테넌트 관리자는 Custom App Upload 정책을 허용하고 앱을
업로드한 뒤 지정된 테스트 사용자 또는 그룹에 할당한다.

테스트용 ZIP은 단일 테넌트의 조직 카탈로그 등록을 전제하지 않는다. 테스터가 속한
각 테넌트가 자체 승인과 설치를 수행한다. 사용자 개인 계정이나 개인용 Agent Builder
화면은 테스트 대상이 아니다.

### 공개 전환

공개 시에는 Microsoft 365 Agents Toolkit 앱 패키지를 Microsoft Partner Center의
Microsoft 365 and Copilot 프로그램 제출 대상으로 사용한다. 이 단계는 Marketplace
심사에 필요한 공개 메타데이터, 지원 체계, 법적 고지, 아이콘·스크린샷을 별도로
완성한 뒤에만 시작한다.

## 아키텍처

```text
MAGI package
 ├─ appPackage/
 │   ├─ manifest.json                 Teams / Microsoft 365 app identity
 │   ├─ color.png, outline.png        app icons
 │   └─ declarative agent definition  MAGI P1 behavior
 ├─ m365-copilot/                     human-readable protocol and installer docs
 ├─ docs/legal/                       privacy, terms, support policy
 ├─ docs/preview/                     tenant-admin and tester runbooks
 └─ tests/                            contract and package validation
```

`m365-copilot/declarativeAgent.json`은 기존 Agent Builder용 참조 정의로 유지한다.
제품 패키지의 선언 정의는 앱 매니페스트에서 참조되는 별도 파일로 둔다. 두 정의는
표시 이름, 설명, P1 등급, MAGI 역할과 무액션 경계가 일치해야 한다.

첫 버전은 백엔드가 없다. 에이전트는 대화 입력을 처리하지만 이를 저장·전송하는
자체 서비스가 없다. 따라서 제품은 사용자 비밀값을 요구하거나 전달하지 않는다.

## 패키지와 브랜딩

- 앱 ID는 개발 단계에서 고정하고 릴리스마다 바꾸지 않는다.
- 앱 이름은 `MAGI Deliberation`으로 유지한다.
- 컬러 및 윤곽 아이콘은 Teams 앱 요구 사항에 맞는 PNG로 제공한다.
- 매니페스트에는 개발자 이름, 지원 URL, 개인정보처리방침 URL, 이용약관 URL을
  넣는다. 모든 공개 URL은 유효한 HTTPS 주소여야 한다.
- 릴리스 ZIP에는 빌드 산출물만 포함한다. 원본 문서와 테스트 코드는 저장소에 남긴다.

## 비공개 테스트 절차

1. 릴리스 담당자가 태그된 버전에서 ZIP과 SHA-256 파일을 만든다.
2. 테스터는 ZIP의 체크섬을 확인한 뒤 자기 테넌트 관리자에게 전달한다.
3. 관리자는 Custom App Upload 허용 여부를 확인하고, 테스트 대상에게만 앱을
   설치·할당한다.
4. 테스터는 Teams와 Microsoft 365 Copilot에서 각각 앱을 열어 시작 프롬프트를
   실행한다.
5. 테스터는 P1 표기, 사실·가정·미확인 사항 구분, 외부 작업 미수행을 확인한다.
6. 피드백은 Issue 템플릿으로 수집한다. 프롬프트, 화면, 로그에 포함된 회사 기밀과
   개인정보는 제거한다.

관리자가 앱 업로드를 허용하지 않거나 사용자가 필요한 Microsoft 365 Copilot 권한을
갖지 못한 경우에는 `ENVIRONMENT-BLOCKED`로 기록한다. 설치 후 패키지 로드 실패,
P1 표기 누락, 허가되지 않은 외부 작업 주장은 제품 결함으로 분류한다.

## 품질 게이트

CI는 다음을 검사한다.

- 앱 매니페스트 및 선언형 에이전트 파일의 형식과 참조 무결성
- 아이콘과 필수 메타데이터의 존재
- 지원·개인정보처리방침·이용약관 URL의 HTTPS 형식
- MAGI의 P1 표기와 MELCHIOR, BALTHASAR, CASPER, RITSUKO 역할
- 액션, 커넥터, 외부 API, 사용자 데이터 저장 설정의 부재
- ZIP에 허용되지 않은 파일과 비밀값이 포함되지 않았는지 여부

출시 후보는 최소 두 개의 별도 테스트 테넌트에서 Teams와 Microsoft 365 Copilot
양쪽의 설치·실행을 통과해야 한다. `ENVIRONMENT-BLOCKED` 결과는 통과로 세지 않으며,
대체 테넌트를 추가하거나 차단 원인을 해소해야 한다.

## Marketplace 전환 기준

다음 조건을 모두 만족할 때만 공개 제출을 시작한다.

- 두 개 이상 테스트 테넌트에서 수용 테스트 통과
- 심각도 높은 미해결 결함 없음
- 개인정보처리방침, 이용약관, 지원 연락처, 개발자 정보 확정
- Marketplace용 공개 설명, 아이콘, 스크린샷 준비 완료
- 릴리스 절차, 취약점 신고·지원·업데이트 책임자 지정
- Partner Center의 현재 심사 및 프로그램 요구 사항 재확인

Marketplace 심사 중 발견된 요구 사항은 제품 범위를 확장하기 전에 별도 설계 검토를
거친다.

## 보안 및 운영 경계

- 테스트 안내는 암호, 액세스 토큰, 고객 데이터, 민감한 대화 로그 공유를 금지한다.
- 제품은 외부 액션을 제공하지 않으며, 일정 생성·메시지 전송·구매·API 호출을
  수행했다고 주장하지 않는다.
- 지식 원본이나 액션 추가는 별도의 설계, 권한 검토, 개인정보처리방침 개정, 새 수용
  테스트를 요구한다.
- 공개 버전의 앱 ID와 신뢰 경계를 유지한다. 기능 확장이 필요하면 새 기능 플래그나
  다음 주 버전으로 구분한다.

## 근거

- [Microsoft 365 Agents Toolkit 앱 게시](https://learn.microsoft.com/en-us/microsoftteams/platform/toolkit/publish)
- [에이전트 사이드로드 정책](https://learn.microsoft.com/en-us/microsoft-365/copilot/agent-essentials/agent-policies/agent-sideload)
- [Microsoft 365 Copilot 에이전트 게시 경로](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/publish)
