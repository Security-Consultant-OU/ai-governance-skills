# What these skills do

This marketplace is a set of **specialized advisors**, not a single “AI governance” chatbot. Each skill loads when the question matches a specific law or framework. It then classifies the system, scores gaps (🔴 not started / 🟡 partial / 🟢 implemented), and fills a copy-ready artefact. It does **not** invent article, control, or Playbook IDs: it looks them up in that skill’s `references/` files.

Add the marketplace, then install the dispatcher first. Client-specific steps (Claude Code, Claude.ai, Cursor, Codex, Copilot, others): [INSTALL.md](INSTALL.md). Versions as of **25 August 2026**: `ai-governance` **1.0.0**, `eu-ai-act` **1.3.0**, `iso42001` **1.4.0**, `csa-aicm` **1.0.0**; others **1.2.0**.

| Skill | In force? | Default artefact if you omit the document type |
|---|---|---|
| `using-ai-governance` | n/a (router) | Invokes the matching specialist; does not produce a compliance artefact |
| `eu-ai-act` | Yes (phased; most product duties in force 2 Aug 2026) | Annex IV technical documentation |
| `nist-ai-rmf` | Voluntary framework | Current vs Target Profile |
| `iso42001` | Certifiable standard | Gap assessment + Statement of Applicability |
| `nyc-local-law-144` | Yes (enforced since 5 Jul 2023) | AEDT determination, then bias-audit table shells if it is an AEDT |
| `south-korea-ai-act` | Yes (22 Jan 2026; Decree 36053 in force) | Art. 2(4) high-impact classification, then the operator matrix |
| `brazil-ai-act` | **No** — pending bill | Status-labelled classification against the Senate substitute |
| `csa-aicm` | Voluntary CSA programme | CAIQ answer table from the user's AICM workbook |

Use **one skill per jurisdiction or standard**. If several apply, **invoke each** (do not blend article numbers). The dispatcher `using-ai-governance` is the catalog. Crosswalks exist so you can map, not so one skill can stand in for another. Official ISO, EU OJ, and CSA PDFs are cited, not copied into the repo.

---

## `using-ai-governance` — marketplace dispatcher

**What it does.** Superpowers-style router. At session start (plugin `ai-governance`) it is injected so the agent checks the catalog **before** answering. If another skill might apply, it must **invoke** that skill, announce `Using [skill] to [purpose]`, and follow it. Collision terms (high-risk, GPAI, FRIA, AISIA, deployer) are disambiguated here.

**When to use it.** Any AI-system / AI-compliance / AI-regulation question; “which skill?”; mixed-jurisdiction prompts.

**What it will not do.** Produce a SoA, FRIA, or CAIQ itself.

---

## `eu-ai-act` — EU AI Act (Regulation 2024/1689)

**What it does.** Treats Claude as an EU AI Act compliance advisor. It classifies a system under **Art. 5** (prohibited), **Art. 6** (EU high-risk, including the Annex I product path and Annex III), and **Art. 50** (transparency) **independently** — Art. 50 is additive, not a “limited risk” bucket. It then runs role-specific gap tables (provider vs deployer vs importer/distributor), **high-risk operational checklists** (Arts. 9–15, 17, 20, 72–73), the **Art. 27 FRIA** gate, Chapter V **GPAI** duties, **Art. 43** conformity/CE, and Annex IV documentation. Installing `eu-ai-act` also loads **`eu-gpai-cop`** for the Art. 56 Code of Practice (not mandatory; alternative means still satisfy Arts. 53/55).

**When to use it.** EU AI Act, Regulation 2024/1689, Annex III, Art. 27 FRIA, EU GPAI, CE marking for AI, Art. 50, prohibited practices, EU sandboxes.

**Typical jobs**

- Classify a chatbot (Art. 50 disclosure, and Art. 6 if it is also Annex III).
- Classify workplace emotion recognition (usually Art. 5(1)(f), with medical/safety exceptions).
- Medical-device AI on the Annex I path (Art. 6(1) + sectoral conformity under Art. 43(3)).
- Decide whether a **deployer** must do a FRIA (public body / public services / certain biometric uses — not every high-risk system).
- Separate ordinary GPAI (Art. 53) from systemic-risk GPAI (Arts. 51/55).
- Fill an Art. 9–15 operational autoeval (Spanish workbook *shape* only — do not copy third-party measure text).
- Assess GPAI CoP chapter coverage vs alternative means (`eu-gpai-cop`).

**What it will not do.** NIST Profiles, ISO 42001 Statements of Applicability, NYC bias-audit math, Korea 고영향 AI, or Brazil’s pending bill (including Brazil GPAI).

---

## `nist-ai-rmf` — NIST AI Risk Management Framework 1.0

**What it does.** Builds a **Current vs Target Profile** for a named system against the **72 official subcategory outcomes** in NIST AI 100-1 (GOVERN, MAP, MEASURE, MANAGE). For generative systems it overlays **NIST AI 600-1** (12 generative-AI risk families mapped back to Core IDs). Scoring is 🔴🟡🟢, not a 1–5 “NIST maturity” scale (that scale is not in the RMF).

**When to use it.** NIST AI RMF, AI 100-1, Current vs Target Profile, GOVERN/MAP/MEASURE/MANAGE, AI RMF Playbook, NIST AI 600-1.

**Typical jobs**

- Profile one production system and list gaps.
- Apply the 600-1 overlay instead of treating generative AI as a generic MAP exercise.
- Run MEASURE 2 for fairness and safety (ME-2.6, ME-2.11), not accuracy-only (ME-2.5).

**What it will not do.** CE marking, ISO certification, NYC audit statistics, or statutory high-risk classification. Playbook Action IDs are used only when they are in context or fetched from [airc.nist.gov](https://airc.nist.gov/airmf-resources/playbook/); it will not invent them.

---

## `iso42001` — ISO/IEC 42001:2023 AIMS

**What it does.** Treats Claude as an ISO/IEC 42001 lead-auditor / implementation consultant. It scopes the AI management system, splits **AI risk** (Clauses 6.1.2 / 8.2) from **AISIA** (Clauses 6.1.4 / 8.4), fills a **Statement of Applicability** for the **38 real Annex A controls**, and checks Stage 1 / Stage 2 certification readiness. Role matters: provider vs user vs both changes which controls apply.

**When to use it.** ISO 42001, ISO/IEC 42001, AIMS certification, Statement of Applicability, AIMS gap. Standalone AISIA / inventories / policy pack → companion skills below.

**Typical jobs**

- User-only SoA (exclude development controls such as A.6.1.2 with a written justification).
- Keep AISIA and risk as two records, not one merged memo.
- Produce the Stage 1 documented-information list.
- Supplier due diligence under **A.10.3** (A.10 is suppliers/customers, not decommission).

**What it will not do.** NYC scoring-rate math, EU CE marking, or NIST Playbook actions. It will not invent Annex A IDs (there is no A.5.8; A.x.1 is an objective, not a selectable control).

Installing `iso42001` also loads **companion skills** that produce a single AIMS artefact instead of a full gap/SoA pack:

| Companion | Artefact | ISO hook |
|-----------|----------|----------|
| `iso-aisia` | AISIA record | 6.1.4 / 8.4, A.5.2–A.5.5 |
| `iso-ai-system-inventory` | AI system register | Clause 4.3 |
| `iso-ai-data-inventory` | Data-for-AI inventory | A.7.2–A.7.6, A.4.3 |
| `iso-ai-resources` | Resource pack | A.4.2–A.4.6, Clause 7.1 |
| `iso-aims-policy-kit` | Policies, SOPs, document master list | 7.5, A.2, Stage 1 documented information |

They refuse EU FRIA, Korea Art. 35, GDPR RoPA-only, CSA CAIQ as SoA, and generic FinOps unless the user is in an ISO 42001 context. Document numbers such as AIMS-DOC / SOP are an example organisation scheme, not ISO IDs.

---

## `nyc-local-law-144` — NYC Local Law 144

**What it does.** Decides whether a hiring or promotion tool is an **AEDT**, then produces **DCWP bias-audit table shells** (scoring rate = share **above the sample median**; 7 EEO-1 race/ethnicity categories plus sex and intersectional tables) and **candidate/employee notices**. Geography is split: **job/agency location** drives the audit; **NYC residence** drives notice.

**When to use it.** NYC Local Law 144, LL144, AEDT, DCWP bias audit, NYC hiring AI.

**Typical jobs**

- Equal-weight score among several criteria → usually **not** an AEDT (prong 2).
- Fully remote role tied to an NYC office → audit yes; notice only if the person lives in NYC.
- First use of a vendor tool → other-employer historical data may be allowed; the **employer** remains liable.
- Draft notice vs plan the audit as separate artefacts.

**What it will not do.** ISO SoA, EU high-risk class, or a NIST Profile. It will not treat the 4/5ths rule as LL144 pass/fail, invent “Section 20-a,” or use mean scoring rate.

---

## `south-korea-ai-act` — Korea AI Basic Act (인공지능 기본법)

**What it does.** Advises on the **in-force** Framework Act (22 January 2026) and Enforcement Decree **No. 36053**. The statutory class is **high-impact AI (고영향 AI, Art. 2(4))**, not EU “high-risk.” It maps operator duties under **Arts. 31–36**, treats **Art. 35** impact assessment as an **endeavor** (not a licence), and checks **Art. 36** domestic-representative thresholds for foreign operators. MSIT grace on most investigations/fines runs through at least January 2027; duties still apply now.

**When to use it.** Korea AI Basic Act, AI Framework Act, 인공지능 기본법, 고영향 AI, MSIT, Korea Art. 36 / domestic representative.

**Typical jobs**

- Human-in-the-loop exclusion (human makes the final, controllable decision → not high-impact).
- Generative labelling only (Art. 31 still applies because the system is generative).
- Foreign operator: whether a Korean representative is required.
- Selling to a public body: Art. 35(2) is **preference**, not a pre-market approval.

**What it will not do.** EU Annex III classification, mandatory ISO AISIA inside a certified AIMS, or treat the Act as “decrees still pending.”

---

## `brazil-ai-act` — PL 2338/2023 (Marco Legal da IA)

**What it does.** Advises on a **pending bill**, using the **Senate substitute of 10 December 2024**. As of 25 August 2026 the Chamber is still awaiting the rapporteur’s opinion; it is **not** pending presidential sanction and is **not law**. Every answer is labelled **not enacted**. Roles are **desenvolvedor / distribuidor / aplicador** (English “deployer” is not a legal category). It classifies risco excessivo / alto risco, maps rights (Art. 5 all systems; Art. 6 high-risk only — not an “8 rights” list), and prepares AIA / SIA-ANPD / GPAI-copyright work as **preparedness**, not compliance certification.

**When to use it.** Brazil AI bill, Marco Legal da IA, PL 2338/2023, aplicador, desenvolvedor, avaliação de impacto algorítmico, risco excessivo.

**Typical jobs**

- “Is this law? Are we pending sanction?” → status banner + tramitação link; refuse a compliance certificate.
- Aplicador vs desenvolvedor (including substantial modification).
- Whether a preliminary assessment is required (Art. 12 is **optional** — *poderá*).

**What it will not do.** Treat the bill as in-force law, import LGPD’s 72-hour incident clock, or substitute EU article numbers for Senate articles.

---

## `csa-aicm` — CSA AICM / AI-CAIQ / STAR for AI

**What it does.** Fills **AI-CAIQ** answers and **AICM** gap rows from the **user’s workbook**. Control and question IDs are copied from the sheets (`AICM`, `AI-CAIQ`, mappings), never invented. Supports STAR for AI Level 1 as a CAIQ submission, not as ISO certification. Maps to ISO 42001 or NIST AI 600-1 only when those mapping sheets exist.

**When to use it.** CSA AICM, AI-CAIQ, STAR for AI, CSA AI Controls Matrix, CAIQ for AI.

**Typical jobs**

- Fill a buyer vs provider CAIQ (do not merge the two roles).
- List STAR Level 1 evidence gaps.
- Map AICM IDs to ISO 42001 or NIST 600-1 from the user’s mapping sheet.

**What it will not do.** Complete an ISO SoA of 38 Annex A controls, run EU CE marking, or produce a NIST Current vs Target Profile against the 72 Core outcomes. CBRA is optional CSA method — not a substitute for ISO 6.1.2 or EU Art. 9.

---

## Which skill should load?

| You are asking about… | Use |
|---|---|
| Which skill / mixed jurisdictions / “AI governance” generally | `using-ai-governance` first, then the specialists it names |
| CE marking, Annex III, Art. 50, EU FRIA, EU GPAI Chapter V, high-risk operational checklists | `eu-ai-act` |
| GPAI Code of Practice, Art. 56 model documentation form | `eu-gpai-cop` (installs with `eu-ai-act`) |
| Current vs Target Profile, Playbook, NIST AI 600-1 | `nist-ai-rmf` |
| AIMS certification, SoA | `iso42001` |
| ISO AISIA / system or data or resource inventory / AIMS policy pack | companions on `iso42001` |
| NYC hiring/promotion tools, DCWP audit, candidate notice | `nyc-local-law-144` |
| 고영향 AI, MSIT, Korean representative | `south-korea-ai-act` |
| PL 2338, aplicador, whether Brazil has an AI Act yet | `brazil-ai-act` |
| CSA AICM, AI-CAIQ, STAR for AI | `csa-aicm` |
| Generic “responsible AI” / “AI governance framework” | None of these by themselves — name the law or standard |

If two jurisdictions apply, install both skills and ask each question against the relevant one. Mapping tables live in each skill’s `references/cross-framework-mapping.md`; they are lookup aids, not a substitute for the source skill.
