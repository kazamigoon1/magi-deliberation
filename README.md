# MAGI Deliberation

MAGI Deliberation은 결론을 대신 내리는 역할극이 아니라, 중요한 선택에서
잘못된 결론이 나오기 어렵게 만드는 구조화된 의사결정 지원 스킬입니다.
사실·제약·불확실성·가역성·실행 현실을 분리해 검토하고, 세 관점의 검토와
RITSUKO의 적대적 감사를 거쳐 최종 상태를 제시합니다.

## Overview

MAGI 2.1은 다음 원칙을 우선합니다.

1. 사실을 판단보다 먼저 둡니다.
2. 선호보다 하드 제약을 먼저 적용합니다.
3. 합의 전에 독립적인 관점 검토를 수행합니다.
4. 정밀해 보이는 추정 대신 불확실성을 드러냅니다.
5. 결과가 비슷하면 더 가역적인 선택을 우선합니다.

MAGI는 다수결 엔진이 아닙니다. 하드 제약, 안전 위험, 근거 충족도,
가역성, 실행 가능성을 순서대로 처리하며, 결론에는 실행·보류·재검토의
조건을 함께 남깁니다.

## Components

| Component | Focus |
|---|---|
| MELCHIOR | 사실성, 기술적 가능성, 성능 |
| BALTHASAR | 위험, 복구, 회복력, 가역성 |
| CASPER | 시간, 피로, 일정, 실제 실행 가능성 |
| RITSUKO | 잠재된 전제 오류·누락 선택지·근거 과대평가 감사 |

RITSUKO는 투표하지 않습니다. 잠정 결론의 구체적인 주장 하나를 대상으로
반박하고, 반박이 성립하려면 대상 주장·결함 유형·오류 메커니즘·반증 조건·검증
방법·영향을 모두 제시해야 합니다.

## Modes

| Mode | Suitable for | Scope |
|---|---|---|
| Quick | 저위험·가역적인 일상 선택 | C0 한 건, 핵심 가정 한 건, 세 관점, RITSUKO 반박 한 건 |
| Standard | 비용·불확실성·운영 영향이 있는 선택 | 근거 원장, 두 가지 민감도 점검, RITSUKO 반박 최대 두 건 |
| Full | 고비용·안전 민감·되돌리기 어려운 선택 | 전체 옵션 확장, 프리모텀, 강건성 배터리 |

## Independence grades

모든 결과에는 실제 검토 방식에 따라 독립성 등급을 표시합니다.

| Grade | Meaning |
|---|---|
| P3 | 서로의 초기 결론을 보지 않은 별도 병렬 에이전트 검토 |
| P2 | 이전 결론을 노출하지 않은 격리 순차 검토 |
| P1 | 하나의 모델이 수행한 관점 검토 |

P1은 독립 에이전트 심의가 아닙니다. 실제 병렬 작업이 없으면 P3라고
표기하지 않습니다.

## MAGI-MAINT

`MAGI-MAINT`는 차량·가전 유지보수의 일정과 실행 여부를 판단할 때 쓰는
프로파일입니다. 선택한 작업일과 실제 작업 승인을 분리합니다.

```text
Schedule selection
  → PENDING-CONDITION
  → Pre-execution recheck
  → Day-of go/no-go
  → APPROVED 또는 fallback / delay
```

필요한 경우 다음 C0 검사를 등록합니다.

- 정확한 모델, 부품·어댑터 호환성, 소모품 준비
- 작업 장소의 접근성·운영 시간·조명·세척·기능 시험 여건
- 손상 또는 실패 시 안전하게 중단·복구하는 방법
- 보호된 작업 시간과 작업자의 컨디션

날짜를 선택할 때는 선호 창, 다음 가능 창, 연기, 부분 준비를 비교합니다.
실행 직전에는 일정 충돌, 날씨, 장소, 호환성, 공구와 소모품을 다시 확인합니다.
당일 C0가 모두 통과할 때만 `PENDING-CONDITION → APPROVED`로 전환합니다.

## Install in Codex

Codex 개인 스킬 디렉터리 아래에 이 저장소를 `magi-deliberation` 이름으로
둡니다.

```text
<CODEX_HOME>/skills/magi-deliberation/
├── SKILL.md
├── agents/openai.yaml
└── tests/
```

이미 설치된 스킬을 갱신하는 경우에는 저장소 루트에서 최신 변경을 가져온 뒤,
Codex가 해당 스킬 디렉터리를 다시 읽는 환경에서 사용합니다.

## Example

```text
Use MAGI Standard with the MAGI-MAINT profile to choose the best weekend
for replacing my vehicle wipers. Compare my calendar, the local forecast,
part compatibility, and the work site's availability. Keep the result as
PENDING-CONDITION until the day-before recheck passes.
```

## Validate

```powershell
$env:PYTHONUTF8='1'
python tests/skill_contract_test.py
python tests/readme_contract_test.py
python <path-to-skill-creator>/scripts/quick_validate.py .
```

The first test checks the MAGI-MAINT contract. The second checks the public
README contract. The validator checks the skill package structure.

## Scope and limits

- MAGI is decision support; it does not replace the user's approval or perform
  an external action without authorization.
- Current facts, including calendars, forecasts, prices, or service state,
  must be retrieved for the relevant decision instead of inferred from old data.
- ChatGPT and Codex can differ in their available tools and agent execution
  model. Report the actual P1, P2, or P3 provenance rather than assuming a
  capability from the skill text.
