---
name: using-ai-governance
description: >
  Use at the start of any AI-system, AI-compliance, AI-risk, or AI-regulation
  question — routes to the correct marketplace skill and requires invoking
  that skill before answering, including clarifying questions. Also use when
  the user mentions EU AI Act, NIST AI RMF, ISO 42001, NYC LL144, Korea AI
  Basic Act, Brazil PL 2338, CSA AICM, GPAI, FRIA, AIMS, AEDT, or CAIQ.
version: 1.0.0
triggers:
  - AI governance
  - AI compliance
  - AI regulation
  - AI Act
  - which AI skill
---

# Using the AI governance marketplace

If you were dispatched as a subagent to execute **one named skill**, skip this file and follow that skill.

## The rule

If another skill in this marketplace might apply, **invoke it before you answer** — including before clarifying questions, file reads, or drafting a table. Announce `Using [skill] to [purpose]`, then follow that skill exactly.

Do not improvise another jurisdiction from memory. Do not mix EU article numbers into a Korea or Brazil answer. Do not treat a mapping table as a substitute for the source skill.

If the Skill tool cannot find the skill, tell the user to install it:

`/plugin install <plugin>@ai-governance-skills`

Then continue with whatever skills **are** loaded.

User instructions (CLAUDE.md, AGENTS.md, direct requests) override skills. Skip a skill workflow only when the user explicitly says to.

## Catalog

| User is asking about | Invoke | Plugin (if missing) |
|----------------------|--------|---------------------|
| EU AI Act, Annex III, Art. 50, FRIA, CE marking, high-risk operational checklists | `eu-ai-act` | `eu-ai-act` |
| GPAI Code of Practice, Art. 56 model documentation form | `eu-gpai-cop` | `eu-ai-act` |
| NIST AI RMF, Current vs Target, Playbook, NIST AI 600-1 | `nist-ai-rmf` | `nist-ai-rmf` |
| ISO 42001 gap, SoA, certification | `iso42001` | `iso42001` |
| ISO AISIA record (6.1.4 / 8.4) | `iso-aisia` | `iso42001` |
| AI system register / Clause 4.3 | `iso-ai-system-inventory` | `iso42001` |
| Data-for-AI inventory (A.7) | `iso-ai-data-inventory` | `iso42001` |
| AI resource inventory (A.4 / 7.1) | `iso-ai-resources` | `iso42001` |
| AIMS policies, SOPs, document master list | `iso-aims-policy-kit` | `iso42001` |
| NYC hiring/promotion AEDT, DCWP bias audit, candidate notice | `nyc-local-law-144` | `nyc-local-law-144` |
| Korea AI Basic Act, 고영향 AI, Art. 36 representative | `south-korea-ai-act` | `south-korea-ai-act` |
| Brazil PL 2338, Marco Legal da IA, aplicador (not enacted) | `brazil-ai-act` | `brazil-ai-act` |
| CSA AICM, AI-CAIQ, STAR for AI | `csa-aicm` | `csa-aicm` |
| Generic “responsible AI” with no law or standard named | Ask which instrument; do not pick one | — |

Companions install with their parent plugin (`eu-gpai-cop` with `eu-ai-act`; ISO artefact skills with `iso42001`).

## When several apply

Invoke **each** matching skill for its own slice. Never blend outputs.

| Order | Why |
|-------|-----|
| 1. `brazil-ai-act` if Brazil is in scope | Status banner first — the bill is not law |
| 2. Classification skills (`eu-ai-act`, `south-korea-ai-act`, `nyc-local-law-144`) | Class before gap tables |
| 3. Management-system / profile skills (`iso42001`, `nist-ai-rmf`, `csa-aicm`) | After you know what the system is |
| 4. Companion artefact skills | One artefact each; do not let `iso42001` fake an AISIA if `iso-aisia` is available |

Examples:

- “NYC hiring tool plus EU high-risk” → `nyc-local-law-144` then `eu-ai-act`. Two artefacts.
- “ISO SoA and EU CE” → `iso42001` then `eu-ai-act`. Two artefacts.
- “GPAI CoP vs Chapter V” → `eu-gpai-cop` for the CoP; `eu-ai-act` for Art. 5/6/50/CE.
- “AISIA” with no ISO/EU/Korea cue → ask; default ISO `iso-aisia` only if they have an AIMS context.

## Collision terms

| Word | Do not guess | Invoke |
|------|--------------|--------|
| high-risk | EU Annex III vs Korea 고영향 vs Brazil alto risco | Ask, then the matching skill |
| GPAI | EU Chapter V vs Brazil bill GPAI | `eu-ai-act` / `eu-gpai-cop` vs `brazil-ai-act` |
| FRIA | EU Art. 27 only | `eu-ai-act` |
| AISIA | ISO 6.1.4 vs Korea Art. 35 endeavor | `iso-aisia` vs `south-korea-ai-act` |
| deployer | EU role vs Brazil aplicador | `eu-ai-act` vs `brazil-ai-act` |

## Rationalizations to ignore

| Thought | Do this instead |
|---------|-----------------|
| “I know the EU AI Act well enough” | Invoke `eu-ai-act`. Skills and references change. |
| “A mapping row is enough” | Mapping tables are lookup aids. Invoke the source skill. |
| “This is just a quick question” | Quick questions still pick a jurisdiction. |
| “I’ll answer ISO and mention EU in passing” | Invoke both; two labelled artefacts. |
| “The skill isn’t installed, I’ll approximate” | Say it is missing and give the install line. |

## After routing

Follow the invoked skill’s default artefact if the user omitted a document type. Score gaps 🔴 not started / 🟡 partial / 🟢 implemented. Do not invent article, Annex A, NIST subcategory, AICM, or Playbook IDs.
