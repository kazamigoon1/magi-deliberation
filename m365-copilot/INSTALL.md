# MAGI Deliberation — Per-User Installation Guide

> English

## Who this guide is for

Use this guide when each person should create and own a separate MAGI agent in
their **own tenant**. This is the supported external-distribution pattern for
the Agent Builder version: distribute the instructions, not access to the
creator's private agent.

## Before you start

1. Sign in with the Microsoft 365 work or school account that will own the
   agent. Confirm that **Agents** and **New agent** appear in Microsoft 365
   Copilot on desktop.
2. If they do not appear, Agent Builder is unavailable for that account, tenant
   policy, license, or rollout state. Do not share another person's account.
3. Open `agent-builder.md` in this folder. It is the canonical copy/paste
   source for the name, description, instructions, and starter prompts.

## Create a private MAGI agent

1. In Microsoft 365 Copilot desktop, open **Agents** → **New agent** →
   **Skip to configure**.
2. Copy the display name, description, instructions, and three starter prompts
   from `agent-builder.md`.
3. Leave knowledge sources, connectors, and external actions unconfigured.
   Keep web search off unless you explicitly want web-grounded answers.
4. Select **Create**. The new agent is private to its owner by default.

## Verify the installation

Run this prompt:

```text
MAGI Standard로 두 가지 계획을 비교해줘. 사실, 가정, 미확인 사항을 분리하고 P1 표기를 포함해줘.
```

A correct initial response visibly includes `Independence: P1 — perspective
review`, separates FACT / ASSUMPTION / UNKNOWN, and returns `PENDING-DATA`
instead of inventing missing plan details.

## Mobile check

On the Microsoft 365 Copilot mobile app, sign in with the same account and
look under **Agents** for `MAGI Deliberation`. Agent Builder authoring is a
desktop workflow; mobile availability must be verified on the owner's account.

## Other environments

- **Codex:** install this repository as a personal skill and use `SKILL.md`.
  See the repository's main README for the directory layout.
- **ChatGPT:** use a Project with `SKILL.md` as a reference and add the MAGI
  protocol as Project instructions. ChatGPT Projects can contain files and
  project-specific instructions, but they are not an automatic import of a
  Codex skill. [OpenAI Projects guide](https://help.openai.com/en/articles/10169521-projects-in-chatgpt)
- **ChatGPT managed workspaces:** a custom GPT may be an alternative when the
  workspace permits creation and sharing. Availability and publishing depend
  on the workspace and plan. [OpenAI GPTs guide](https://help.openai.com/en/articles/8554407-what-are-gpts)

---

# MAGI Deliberation — 사용자별 설치 가이드

> 한국어

## 대상

이 문서는 각 사용자가 자신의 **own tenant**에서 별도의 MAGI 에이전트를
생성하고 소유할 때 사용합니다. Agent Builder 버전은 만든 사람의 개인
에이전트 접근 권한을 외부에 넘기는 대신, 지침을 배포하고 각 사용자가 직접
설치하는 방식이 적합합니다.

## 시작 전 확인

1. 에이전트를 소유할 Microsoft 365 회사 또는 학교 계정으로 로그인합니다.
   데스크톱 Microsoft 365 Copilot에 **에이전트**와 **새 에이전트**가 보여야 합니다.
2. 메뉴가 보이지 않으면 해당 계정의 Agent Builder 사용 권한, 테넌트 정책,
   라이선스 또는 점진 배포 상태를 확인합니다. 다른 사람의 계정을 공유하지 않습니다.
3. 이 폴더의 `agent-builder.md`를 엽니다. 이름, 설명, 지침, 시작 프롬프트의
   표준 복사 원본입니다.

## 개인 MAGI 에이전트 생성

1. 데스크톱 Microsoft 365 Copilot에서 **에이전트** → **새 에이전트** →
   **구성으로 건너뛰기**를 선택합니다.
2. `agent-builder.md`의 표시 이름, 설명, 지침, 시작 프롬프트 세 개를 복사합니다.
3. 지식 원본, 커넥터, 외부 액션은 추가하지 않습니다. 웹 근거 답변이 필요할 때만
   웹 검색을 켭니다.
4. **만들기**를 선택합니다. 새 에이전트는 기본적으로 소유자 개인 전용입니다.

## 설치 검증

다음 프롬프트를 실행합니다.

```text
MAGI Standard로 두 가지 계획을 비교해줘. 사실, 가정, 미확인 사항을 분리하고 P1 표기를 포함해줘.
```

정상 응답에는 `Independence: P1 — perspective review`가 보이고,
FACT / ASSUMPTION / UNKNOWN이 분리되며, 계획 세부 정보가 없을 때
임의로 채우지 않고 `PENDING-DATA`를 반환해야 합니다.

## 모바일 확인

Microsoft 365 Copilot 모바일 앱에서 같은 계정으로 로그인한 뒤 **에이전트**에서
`MAGI Deliberation`을 찾습니다. 작성은 데스크톱 절차이며, 모바일 사용 가능 여부는
각 소유자 계정에서 직접 확인합니다.

## 다른 환경

- **Codex:** 이 저장소를 개인 스킬로 설치하고 `SKILL.md`를 사용합니다. 디렉터리
  구조는 저장소 최상단 README를 확인합니다.
- **ChatGPT:** `SKILL.md`를 참고 자료로 올리고 MAGI 규약을 Project instructions에
  넣은 프로젝트를 사용합니다. ChatGPT Projects는 파일과 프로젝트별 지침을 지원하지만,
  Codex 스킬을 자동으로 가져오지는 않습니다. [OpenAI Projects 안내](https://help.openai.com/en/articles/10169521-projects-in-chatgpt)
- **ChatGPT 관리형 워크스페이스:** 워크스페이스가 생성·공유를 허용하면 맞춤 GPT를
  대안으로 사용할 수 있습니다. 사용 가능 여부와 게시 권한은 워크스페이스·요금제에
  따라 다릅니다. [OpenAI GPTs 안내](https://help.openai.com/en/articles/8554407-what-are-gpts)

---

# MAGI Deliberation — ユーザーごとのインストールガイド

> 日本語

## 対象

各利用者が自分の **own tenant** で別々の MAGI エージェントを作成し、所有する
場合のガイドです。Agent Builder 版では作成者の個人エージェントへの外部アクセスを
配るのではなく、指示を配布して各利用者が自分で設定します。

## 事前確認

1. エージェントを所有する Microsoft 365 の職場または学校アカウントでサインインし、
   デスクトップ版 Microsoft 365 Copilot に **Agents** と **New agent** があることを確認します。
2. 表示されない場合は、Agent Builder の利用可否、テナント ポリシー、ライセンス、
   または段階的展開の状態を確認します。他者のアカウントは共有しません。
3. このフォルダーの `agent-builder.md` を開きます。名前、説明、指示、開始プロンプトの
   正式なコピー元です。

## 個人用 MAGI エージェントの作成

1. デスクトップの Microsoft 365 Copilot で **Agents** → **New agent** →
   **Skip to configure** を選びます。
2. `agent-builder.md` から表示名、説明、指示、三つの開始プロンプトをコピーします。
3. 知識ソース、コネクター、外部アクションは追加しません。Web 検索は Web 根拠の
   回答が必要な場合だけ有効にします。
4. **Create** を選びます。新しいエージェントは既定で所有者だけが利用できます。

## 検証

次のプロンプトを実行します。

```text
MAGI Standardで二つの計画を比較して。事実、仮定、未確認事項を分け、P1表記を含めて。
```

応答には `Independence: P1 — perspective review` が含まれ、FACT /
ASSUMPTION / UNKNOWN が分離され、詳細がない場合は推測せず `PENDING-DATA` を
返す必要があります。

## モバイル確認

Microsoft 365 Copilot モバイル アプリで同じアカウントにサインインし、**Agents**
から `MAGI Deliberation` を探します。作成はデスクトップで行い、モバイルでの利用可否は
各所有者のアカウントで確認します。

## 他の環境

- **Codex:** このリポジトリを個人スキルとしてインストールし、`SKILL.md` を使います。
- **ChatGPT:** `SKILL.md` を参考資料として追加し、MAGI 規約を Project instructions に
  入れたプロジェクトを使います。ChatGPT Projects は Codex スキルの自動インポートでは
  ありません。
