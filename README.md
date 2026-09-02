# MAGI Deliberation

> English

MAGI Deliberation is a structured decision-support skill. It does not perform
role-play to manufacture a conclusion; it separates facts, constraints,
uncertainty, reversibility, and execution reality so that incorrect decisions
are harder to make.

## Overview

MAGI 2.1 prioritizes facts before judgment, constraints before preferences,
independent review before consensus, uncertainty before false precision, and
reversibility before optimization. It is not a majority-vote engine: hard
constraints, safety, evidence sufficiency, reversibility, and operational
feasibility take priority in that order.

## Components

| Component | Focus |
|---|---|
| MELCHIOR | Facts, technical feasibility, and performance |
| BALTHASAR | Risk, recovery, resilience, and reversibility |
| CASPER | Time, fatigue, schedule, and real-world execution |
| RITSUKO | Adversarial audit for premise errors, hidden options, and evidence inflation |

RITSUKO has no vote. A valid finding identifies its target claim, defect class,
mechanism, falsification condition, verification method, and effect.

## Modes

| Mode | Suitable for | Scope |
|---|---|---|
| Quick | Low-risk, reversible everyday choices | One C0 check, one material assumption, three views, one RITSUKO attack |
| Standard | Decisions with cost, uncertainty, or operational impact | Evidence ledger, two targeted robustness checks, up to two RITSUKO attacks |
| Full | High-cost, safety-sensitive, or difficult-to-reverse decisions | Full option expansion, pre-mortem, and robustness battery |

## Independence grades

| Grade | Meaning |
|---|---|
| P3 | Separate parallel agents reviewed a common packet without seeing each other's initial conclusion |
| P2 | Isolated sequential reviews were produced without exposing an earlier conclusion |
| P1 | One model performed a perspective review |

P1 is not independent-agent deliberation. Never report P3 unless parallel work
actually occurred.

## MAGI-MAINT

`MAGI-MAINT` is the profile for vehicle and appliance maintenance. It keeps a
chosen work date separate from permission to execute.

```text
Schedule selection
  → PENDING-CONDITION
  → Pre-execution recheck
  → Day-of go/no-go
  → APPROVED or fallback / delay
```

When material, register C0 checks for exact model and part compatibility,
required consumables, work-site readiness, safety and recovery, protected work
time, and operator condition. Recheck calendar conflicts, weather, site access,
compatibility, tools, and consumables shortly before work. Transition to
`APPROVED` only when day-of C0 checks pass.

## Install in Codex

Place this repository as `magi-deliberation` under the Codex personal skills
directory:

```text
<CODEX_HOME>/skills/magi-deliberation/
├── SKILL.md
├── agents/openai.yaml
└── tests/
```

After updating an existing installation, use it in an environment where Codex
reloads that skills directory.

## Personal Microsoft Copilot agent

Use [m365-copilot/README.md](m365-copilot/README.md) to create the private,
instruction-only MAGI agent in the Microsoft Copilot app, including Microsoft
365 Copilot where it is branded that way. On desktop, verify that **Agents**
and **New agent** are visible before starting; availability depends on the
account, license, tenant policy, and rollout state. It is authored on desktop
and then verified in the mobile app with the owner's account. The first release
uses P1 perspective review only and has no actions, connectors, or extra
permissions.

For users outside the creator's organization, use the
[per-user installation guide](m365-copilot/INSTALL.md) instead of sharing the
creator's private agent.

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
python tests/license_contract_test.py
python tests/protocol_behavior_contract_test.py
python tests/m365_personal_agent_contract_test.py
python <path-to-skill-creator>/scripts/quick_validate.py .
```

## Automated validation

GitHub Actions runs the four repository-local contract scripts on every push
and pull request. It does not evaluate generated LLM output.

## Scope and limits

- MAGI provides decision support; it does not replace the user's approval or
  perform external actions without authorization.
- Retrieve current calendars, forecasts, prices, and service states for the
  decision at hand instead of inferring them from old data.
- ChatGPT and Codex can expose different tools and agent execution models;
  report the actual P1, P2, or P3 provenance.

## License

This project is licensed under the [MIT License](LICENSE).

---

# MAGI Deliberation — 한국어

> 한국어

MAGI Deliberation은 중요한 선택에서 잘못된 결론이 나오기 어렵게 만드는
구조화된 의사결정 지원 스킬입니다. 결론을 만들기 위한 역할극이 아니라 사실,
제약, 불확실성, 가역성, 실제 실행 여건을 분리하여 검토합니다.

## 개요

MAGI 2.1은 판단보다 사실을, 선호보다 제약을, 합의보다 독립 검토를,
가짜 정밀도보다 불확실성 공개를, 최적화보다 가역성을 우선합니다. 다수결로
결정하지 않으며 하드 제약, 안전, 근거 충족도, 가역성, 운영 가능성을 그 순서로
평가합니다.

## 구성 요소

| 구성 요소 | 중점 |
|---|---|
| MELCHIOR | 사실성, 기술적 가능성, 성능 |
| BALTHASAR | 위험, 복구, 회복력, 가역성 |
| CASPER | 시간, 피로, 일정, 실제 실행 가능성 |
| RITSUKO | 전제 오류, 숨은 선택지, 근거 과대평가를 찾는 적대적 감사 |

RITSUKO는 투표하지 않습니다. 유효한 지적에는 대상 주장, 결함 유형, 오류
메커니즘, 반증 조건, 검증 방법, 영향을 모두 적어야 합니다.

## 모드

| 모드 | 적합한 경우 | 범위 |
|---|---|---|
| Quick | 저위험·가역적 일상 선택 | C0 한 건, 핵심 가정 한 건, 세 관점, RITSUKO 반박 한 건 |
| Standard | 비용·불확실성·운영 영향이 있는 선택 | 근거 원장, 목표 강건성 점검 두 건, RITSUKO 반박 최대 두 건 |
| Full | 고비용·안전 민감·되돌리기 어려운 선택 | 전체 옵션 확장, 프리모텀, 강건성 배터리 |

## 독립성 등급

| 등급 | 의미 |
|---|---|
| P3 | 서로의 초기 결론을 보지 않은 별도 병렬 에이전트 검토 |
| P2 | 이전 결론을 노출하지 않은 격리 순차 검토 |
| P1 | 하나의 모델이 수행한 관점 검토 |

P1은 독립 에이전트 심의가 아닙니다. 실제 병렬 작업이 없었다면 P3로 표기하지
않습니다.

## MAGI-MAINT

`MAGI-MAINT`는 차량·가전 유지보수용 프로파일입니다. 선택한 작업일과 실제
작업 승인을 분리합니다.

```text
일정 선정
  → PENDING-CONDITION
  → 작업 전 재검증
  → 당일 Go/No-Go
  → APPROVED 또는 예비일 / 연기
```

필요한 경우 정확한 모델·부품 호환성, 소모품, 작업 장소, 안전·복구 방법,
보호된 작업 시간, 작업자 컨디션을 C0로 등록합니다. 실행 직전에는 일정 충돌,
날씨, 장소 접근성, 호환성, 공구와 소모품을 다시 확인하고, 당일 C0가 모두
통과할 때만 `APPROVED`로 전환합니다.

## Codex 설치

이 저장소를 Codex 개인 스킬 디렉터리 아래 `magi-deliberation`으로 둡니다.

```text
<CODEX_HOME>/skills/magi-deliberation/
├── SKILL.md
├── agents/openai.yaml
└── tests/
```

기존 설치본을 갱신했다면 Codex가 해당 스킬 디렉터리를 다시 읽는 환경에서
사용합니다.

## 개인용 Microsoft Copilot 에이전트

[m365-copilot/README.md](m365-copilot/README.md)의 절차에 따라 Microsoft
Copilot 앱(Microsoft 365 Copilot으로 표시되는 환경 포함)에서 개인 전용·지침 기반
MAGI 에이전트를 만듭니다. 시작 전에 데스크톱에서 **에이전트**와 **새 에이전트**
메뉴가 보이는지 확인합니다. 사용 가능 여부는 계정, 라이선스, 테넌트 정책, 점진 배포
상태에 따라 달라집니다. 작성 후 같은 계정으로 모바일 앱에서 확인합니다. 1차 버전은
P1 관점 검토만 사용하며, 액션·커넥터·추가 권한을 사용하지 않습니다.

만든 사람의 조직 밖 사용자에게는 개인 에이전트를 공유하지 말고,
[사용자별 설치 가이드](m365-copilot/INSTALL.md)를 제공하여 각자 자신의 테넌트에서
생성하도록 안내합니다.

## 예시

```text
Use MAGI Standard with the MAGI-MAINT profile to choose the best weekend
for replacing my vehicle wipers. Compare my calendar, the local forecast,
part compatibility, and the work site's availability. Keep the result as
PENDING-CONDITION until the day-before recheck passes.
```

## 검증

```powershell
$env:PYTHONUTF8='1'
python tests/skill_contract_test.py
python tests/readme_contract_test.py
python tests/license_contract_test.py
python tests/protocol_behavior_contract_test.py
python tests/m365_personal_agent_contract_test.py
python <path-to-skill-creator>/scripts/quick_validate.py .
```

## 자동 검증

GitHub Actions는 모든 push와 pull request에서 저장소 내부의 네 가지 계약
스크립트를 실행합니다. 생성된 LLM 출력은 평가하지 않습니다.

## 범위와 한계

- MAGI는 의사결정을 지원하며, 사용자의 승인이나 별도 권한 없이 외부 작업을
  수행하지 않습니다.
- 일정, 예보, 가격, 서비스 상태처럼 변하는 사실은 과거 데이터로 추정하지 말고
  해당 판단 시점에 조회해야 합니다.
- ChatGPT와 Codex는 사용 가능한 도구와 에이전트 실행 방식이 다를 수 있으므로,
  실제 P1, P2, P3 출처를 표시합니다.

## 라이선스

이 프로젝트는 [MIT License](LICENSE)로 배포됩니다.

---

# MAGI Deliberation — 日本語

> 日本語

MAGI Deliberation は、重要な選択で誤った結論に至りにくくするための構造化された
意思決定支援スキルです。結論を作るためのロールプレイではなく、事実、制約、
不確実性、可逆性、実行上の現実を分けて検討します。

## 概要

MAGI 2.1 は、判断より事実、好みより制約、合意より独立したレビュー、見せかけの
精密さより不確実性の開示、最適化より可逆性を優先します。多数決で決めるのでは
なく、ハード制約、安全性、根拠の十分性、可逆性、運用可能性の順で評価します。

## 構成要素

| 構成要素 | 主な観点 |
|---|---|
| MELCHIOR | 事実性、技術的実現可能性、性能 |
| BALTHASAR | リスク、復旧、レジリエンス、可逆性 |
| CASPER | 時間、疲労、予定、実際の実行可能性 |
| RITSUKO | 前提の誤り、隠れた選択肢、根拠の過大評価を探す敵対的監査 |

RITSUKO は投票しません。有効な指摘には、対象の主張、欠陥の種類、誤りの
仕組み、反証条件、検証方法、影響をすべて記載します。

## モード

| モード | 適するケース | 範囲 |
|---|---|---|
| Quick | 低リスクで可逆的な日常の選択 | C0 一件、重要な仮定一件、三つの観点、RITSUKO の反論一件 |
| Standard | コスト、不確実性、運用への影響がある選択 | 根拠台帳、対象を絞った堅牢性確認二件、RITSUKO の反論は最大二件 |
| Full | 高コスト、安全性に敏感、または戻しにくい選択 | 選択肢の完全な展開、プレモーテム、堅牢性バッテリー |

## 独立性の等級

| 等級 | 意味 |
|---|---|
| P3 | 初期結論を見せずに別々の並列エージェントが共通パケットを確認 |
| P2 | 先行する結論を公開せずに行った隔離された順次レビュー |
| P1 | 一つのモデルによる観点レビュー |

P1 は独立エージェントによる審議ではありません。実際の並列作業がなければ
P3 と表記しません。

## MAGI-MAINT

`MAGI-MAINT` は車両・家電のメンテナンス用プロファイルです。作業日を選ぶことと
実行を承認することを分けます。

```text
日程の選択
  → PENDING-CONDITION
  → 実行前の再確認
  → 当日の Go/No-Go
  → APPROVED または予備日 / 延期
```

必要に応じて、正確なモデルと部品の適合性、消耗品、作業場所、安全な中断・復旧
方法、保護された作業時間、作業者の状態を C0 として登録します。実行直前には
予定の競合、天気、場所へのアクセス、適合性、工具、消耗品を再確認し、当日の
C0 がすべて通過した場合にのみ `APPROVED` に移行します。

## Codex へのインストール

このリポジトリを Codex の個人スキルディレクトリ配下に
`magi-deliberation` として配置します。

```text
<CODEX_HOME>/skills/magi-deliberation/
├── SKILL.md
├── agents/openai.yaml
└── tests/
```

既存のインストールを更新した場合は、Codex がそのスキルディレクトリを再読み込み
する環境で利用します。

## 個人用 Microsoft Copilot エージェント

[m365-copilot/README.md](m365-copilot/README.md) の手順に従い、Microsoft
Copilot アプリ（Microsoft 365 Copilot と表示される環境を含む）で個人専用・指示
ベースの MAGI エージェントを作成します。開始前にデスクトップで **Agents** と
**New agent** が見えることを確認します。利用可否はアカウント、ライセンス、
テナント ポリシー、段階的展開の状態に依存します。作成後、同じアカウントで
モバイルアプリから確認します。第1版は P1 の観点レビューのみを使用し、
アクション、コネクタ、追加権限は使用しません。

作成者の組織外の利用者には個人エージェントを共有せず、
[ユーザーごとのインストールガイド](m365-copilot/INSTALL.md)を配布して各自の
テナントで作成するよう案内します。

## 例

```text
Use MAGI Standard with the MAGI-MAINT profile to choose the best weekend
for replacing my vehicle wipers. Compare my calendar, the local forecast,
part compatibility, and the work site's availability. Keep the result as
PENDING-CONDITION until the day-before recheck passes.
```

## 検証

```powershell
$env:PYTHONUTF8='1'
python tests/skill_contract_test.py
python tests/readme_contract_test.py
python tests/license_contract_test.py
python tests/protocol_behavior_contract_test.py
python tests/m365_personal_agent_contract_test.py
python <path-to-skill-creator>/scripts/quick_validate.py .
```

## 自動検証

GitHub Actions は、push と pull request のたびにリポジトリ内の 4 つの契約
スクリプトを実行します。生成された LLM 出力は評価しません。

## 範囲と制限

- MAGI は意思決定を支援するものであり、利用者の承認または個別の権限なしに
  外部アクションを実行しません。
- カレンダー、予報、価格、サービス状態のように変化する事実は、過去のデータから
  推測せず、その判断時点で取得します。
- ChatGPT と Codex では利用できるツールやエージェント実行モデルが異なる場合が
  あるため、実際の P1、P2、P3 の来歴を表示します。

## ライセンス

このプロジェクトは [MIT License](LICENSE) の下で公開されています。
