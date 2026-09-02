# Microsoft Copilot용 MAGI Deliberation

이 폴더는 Microsoft Copilot 앱에서 만드는 MAGI Deliberation의 첫 번째
**개인 전용** 버전입니다. 의사결정을 검토하는 지침 기반 선언형 에이전트이며,
액션, API 플러그인, 커넥터, 추가 앱 권한은 사용하지 않습니다.

만든 사람의 조직 밖에 배포하려면 에이전트 접근 권한을 넘기지 말고
[INSTALL.md](INSTALL.md)와 `agent-builder.md`를 제공하여 각 사용자가 자신의
테넌트에 만들도록 안내합니다.

## 요구 사항

- Microsoft Copilot과 Agent Builder를 사용할 수 있는 회사 또는 학교 계정
- 작성에 쓸 **데스크톱** 브라우저 또는 Teams 데스크톱/웹 클라이언트

Agent Builder의 사용 가능 여부는 테넌트 정책, 라이선스, 점진 배포 상태에 따라
달라집니다. 모바일에서는 작성할 수 없습니다. Microsoft Copilot 앱에서
**Agents**와 **New agent** 메뉴가 보이는지 먼저 확인합니다.
[Microsoft 공식 Agent Builder 안내](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder)

## 개인 전용 에이전트 만들기

1. 데스크톱에서 [Microsoft Copilot 앱](https://m365.cloud.microsoft/chat)을 열고
   에이전트를 소유할 회사 또는 학교 계정으로 로그인합니다. 환경에 따라 Microsoft
   365 Copilot으로 표시될 수 있습니다.
2. **Agents**와 **New agent**가 보이는지 확인한 뒤 **New agent**를 선택합니다.
   둘 중 하나라도 없으면 해당 계정에서는 이 Agent Builder 경로를 사용할 수 없습니다.
3. **Configure**를 선택합니다.
4. [agent-builder.md](agent-builder.md)의 표시 이름, 설명, 지침, 시작 프롬프트 세 개를
   각각의 입력란에 복사합니다.
5. 첫 버전에는 지식 원본, 액션, 커넥터, 추가 기능을 넣지 않습니다.
6. **Create**를 선택합니다. 처음 만든 에이전트는 기본적으로 개인 전용입니다.

## 설치 확인

시작 프롬프트를 각각 실행합니다. 정상 응답은 다음을 만족해야 합니다.

- `Independence: P1 — perspective review`를 보이게 표시한다.
- 필요한 경우 FACT, ASSUMPTION, INFERENCE, UNKNOWN을 구분한다.
- 권고를 실행 승인으로 바꾸지 않고 하나의 최종 상태를 명시한다.
- 일정 생성, 메시지 전송, 구매, 외부 서비스 호출을 했다고 주장하지 않는다.

## 모바일 확인

같은 계정으로 Microsoft Copilot **모바일** 앱에 로그인합니다. **Agents**에서
`MAGI Deliberation`을 찾아 첫 번째 시작 프롬프트를 실행합니다. 에이전트가 보이는지와
P1 표기가 출력되는지를 기록합니다. 이는 계정 및 정책에 따라 달라지는 확인 절차이며,
이 문서는 모든 모바일 환경에서의 사용 가능을 보장하지 않습니다.

## 조직 내 정식 배포

현재 MAGI처럼 Agent Builder로 만든 선언형 에이전트는 **조직 카탈로그** 배포가
정식 경로입니다. 승인되면 같은 테넌트의 Agent Store에서 **Built by your org**로
표시됩니다. 단순 공유는 특정 사용자 또는 그룹에게 대화 권한을 주는 협업 방식이며,
조직 전체 배포를 대신하지 않습니다.

### 배포 전 준비

1. 개인 전용 상태에서 위 설치 확인을 마치고, 실제 대상 사용자와 소규모 파일럿을
   진행합니다.
2. 에이전트 설명과 시작 프롬프트를 조직용 문구로 점검합니다. 개인 계정이나 개인
   일정에 의존한다는 인상을 주지 않도록 합니다.
3. 지식 원본을 추가했다면 모든 대상 사용자가 해당 SharePoint, 파일 등 원본에 실제로
   접근할 수 있는지 확인합니다.
4. 배포 주체, 생성자 웹 사이트, 조직의 개인정보처리방침 URL, 이용약관 URL을 준비합니다.
   개인정보처리방침과 이용약관은 대상 사용자가 접근 가능한 유효한 HTTPS 주소여야 합니다.

### 제출 절차

1. Microsoft Copilot에서 **All agents**를 열고 MAGI를 선택한 뒤 **Edit**를 선택합니다.
2. 미게시 변경이 있으면 **Update**로 최신 버전을 게시합니다.
3. 작성 화면의 **…** 메뉴에서 **Submit to your org catalog**을 선택합니다.
4. 표시 이름, 짧은 설명, 개발자 이름, 생성자 웹 사이트, 개인정보처리방침, 이용약관을
   입력하고 제출합니다.
5. Microsoft 365 관리자가 관리 센터에서 요청을 검토·승인하도록 합니다.
6. 승인되면 Agent Store의 **Built by your org**에서 에이전트를 찾고 설치할 수 있습니다.

제출 후 상태는 같은 메뉴에서 확인합니다. Agent Builder에서 변경한 내용은 조직
카탈로그 버전에 자동 반영되지 않으므로, 변경마다 **Update → 재제출 → 관리자 승인**을
거쳐야 합니다.

[조직 카탈로그 제출 절차](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-submit-to-org-catalog)와
[개인정보처리방침·이용약관 요구 사항](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-publication-privacy-terms-of-use)을
따릅니다.

## 배포 방식 선택

| 목적 | 권장 방식 | 범위 |
|---|---|---|
| 소수 동료의 공동 검토 | Agent Builder의 Share | 같은 테넌트의 특정 사용자·그룹 |
| 조직 표준 도구로 배포 | Agent Builder의 조직 카탈로그 제출 | 같은 테넌트 전체 또는 관리자가 정한 대상 |
| 조직 외부, 웹·Teams 등 다중 채널, 상용 배포 | Copilot Studio로 별도 설계·배포 | 채널과 테넌트 정책에 따름 |

Agent Builder 에이전트는 Microsoft Commercial Marketplace에 직접 게시할 수
없습니다. 조직 밖 사용자에게 정식으로 제공하거나 여러 채널에 게시하려면 Copilot
Studio로 전환해 인증, 데이터, 비용, 지원 책임, 배포 채널을 별도로 설계해야 합니다.
[Microsoft의 게시 방식 비교](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/publish)

## 버전 관리 기준

`declarativeAgent.json`은 검토와 향후 Agents Toolkit 패키징을 위해 Agent Builder의
동작을 schema 1.8로 반영한 참조 파일입니다. 이것만으로는 바로 사이드로딩할 수 있는
완전한 Microsoft 365 앱 패키지가 아닙니다.

## 보안 경계

MAGI 요청에 암호, 액세스 토큰, 비밀값, 민감한 개인 기록을 넣지 않습니다. 일정, 날씨,
웹, Microsoft Graph 연동은 데이터 흐름, 권한 부여, 동의, 재검증 동작을 별도로 설계한
후에만 추가합니다.
