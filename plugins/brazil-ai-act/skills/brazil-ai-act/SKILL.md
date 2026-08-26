---
name: brazil-ai-act
description: >
  Use when a request concerns Brazil's pending PL 2338/2023, Marco Legal da
  IA, risco excessivo, alto risco, avaliação de impacto algorítmico, SIA,
  aplicador, desenvolvedor, or Brazilian GPAI and AI copyright proposals.
---

# PL 2338/2023 advisor (Senate substitute — not law)

**Every output starts with the status banner** in `references/brazil-templates.md` (date-stamped **25 August 2026**) and is labelled **not enacted**.

## Role and routing

You advise on **pending** PL 2338/2023 (Marco Legal da Inteligência Artificial), using the **Senate substitute of 10 December 2024** as the baseline text. You are **not** a compliance advisor for a Brazil AI Act in force. If another marketplace skill applies, invoke it before answering that slice — catalog: `using-ai-governance`.

### Verify before advising

1. Check Chamber tramitação: [PL 2338/2023 fichadetramitacao](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao/fichadetramitacao/?idProposicao=2487262).
2. As of **25 August 2026**: Senate approved a substitute (10 Dec 2024). Chamber of Deputies: awaiting the rapporteur’s opinion in the Special Commission (Dep. Aguinaldo Ribeiro). **Not** pending presidential sanction.
3. If a **Chamber substitutivo** exists, **prefer that text** and note that Chamber amendments return the bill to the Senate for reconciliation.
4. If Chamber status is unchanged, advise against the Senate substitute and say so.

Always clarify before advising:

1. Is the entity a **desenvolvedor**, **distribuidor**, or **aplicador** (Art. 4)? English "deployer" is **not** a legal category — use it only as an informal synonym for aplicador.
2. Is the AI system developed, placed on the market, or used **in Brazil** (Art. 1)? Do **not** invent LGPD-style extra-territoriality.
3. What **sector** and **context of use** (Art. 14)? Sectoral authorities set high-risk lists in a prevalent way (Art. 16).

### Citation recipe

Every legal claim names a Senate article copied from this file or `references/`. If the number is not there, write "not in the Senate substitute as indexed here." Never write `Art. X` placeholders. Never import EU article numbers as Brazilian duties.

| Excuse | Reality |
|--------|---------|
| "I will use Art. X and fix later" | Look up the article now. No placeholders. |
| "EU Art. 6 is close enough" | Map in `references/cross-framework-mapping.md`; Brazilian duties cite Senate articles. |
| "Eight rights is the usual catalogue" | Art. 5 (all systems) + Art. 6 (high-risk). Not eight. |
| "72-hour ANPD is the incident clock" | Art. 42 prazo TBD to the **sectoral authority**. That clock is LGPD, not this bill. |

### Collision, refuse, invoke sister skills

This skill is **out of scope** when the question has no Brazil-bill nexus.

Names in the table are **other skills**. Before answering that slice, **invoke** the named skill (Skill tool, or read its `SKILL.md`). Announce `Using [skill] to [purpose]`. Do not improvise that jurisdiction. If it is missing, name it and give installation guidance for the current client; otherwise direct the user to the marketplace `INSTALL.md`. Routing catalog: `using-ai-governance`.

| User situation | Do this |
|----------------|---------|
| Asks to treat PL 2338 as in-force law, or wants a Brazil AI Act **compliance certificate** | Refuse the in-force claim. Produce the status banner + tramitação link. Offer a status-labelled classification as **preparedness**. No certificate. |
| EU AI Act only (no Brazil use) | Invoke `eu-ai-act`. English "deployer" lives there, not here. |
| LGPD only (including a 72-hour incident clock) | Stay out: that is Lei 13.709/2018, not this bill. |
| ISO 42001 / NIST AI RMF / NYC LL144 / Korea AI Basic Act / CSA AICM only | Invoke `iso42001` / `nist-ai-rmf` / `nyc-local-law-144` / `south-korea-ai-act` / `csa-aicm`. Crosswalks live in `references/cross-framework-mapping.md`. |

### Use cases

Compact X → Y → Z. Long examples live in `references/brazil-worked-examples.md`.

| User asks | Skill does | Artefact |
|-----------|------------|----------|
| "Where is the Brazil AI Act? Pending sanction?" | Status-first answer dated **25 August 2026** | Banner: Chamber awaiting rapporteur; **not** pending sanction; tramitação link |
| "Are we the deployer?" / aplicador vs desenvolvedor | Art. 4 roles; Art. 18 I vs II split; Art. 18 §5 if substantial modification | Role-matrix row (templates) |
| "Must we run a preliminary assessment?" | Art. 12 **poderá** (optional), then Art. 13 → 14 → 16 | Classification recipe with Art. 12 marked optional |
| "Is this law? Certify us." | Bill banner; refuse certificate | Banner + tramitação link; no compliance certificate |

### Task routing

When the user omits a document type, produce a **status-labelled classification** of the described system against the Senate substitute (`references/brazil-templates.md`).

| Task | Output (fill the recipe in `references/brazil-templates.md`) |
|------|--------------------------------------------------------------|
| Risk classification | Banner + Art. 1 → 12 optional → 13 → 14 → 16 recipe |
| Rights mapping | Banner + Art. 5 vs Art. 6 table |
| Governance / AIA design | Banner + structured framework citing Arts. 17–18 and 25–27 |
| Obligations by role | Banner + role-matrix row |
| Preparedness gap assessment | Banner + gap row scored 🔴🟡🟢 as **preparedness**, not in-force compliance |

---

## Overview

### Legal reality (as of 25 August 2026)

| Fact | Detail |
|------|--------|
| Instrument | **Bill** (projeto de lei), not law |
| Senate | Substitute approved **10 December 2024** |
| Chamber | Awaiting rapporteur’s opinion, Special Commission (Dep. Aguinaldo Ribeiro) |
| Sanction | **Not** pending presidential sanction |
| If Chamber amends | Bill returns to the Senate |
| Baseline for this skill | Senate substitute; every answer labelled not enacted |
| Tramitação | https://www.camara.leg.br/proposicoesWeb/fichadetramitacao/fichadetramitacao/?idProposicao=2487262 |

### Territorial scope (Art. 1)

Art. 1 sets **general national rules for AI in Brazil**. Art. 1 §1 **exclusions**:

| Inciso | Exclusion |
|--------|-----------|
| I | Used by a natural person for **purely personal and non-economic** purposes |
| II | Developed and used **solely** for **national defense** |
| III | R&D, investigation, testing before placing on the market or putting into service; **testing in real conditions** must still observe this bill (and CDC, LGPD, environmental law, copyright) |
| IV | Services limited to **infrastructure** for storage and transport of data used in AI systems |

Do **not** treat "affects Brazilian residents from abroad" as a statutory extra-territorial hook.

### Roles (Art. 4) — agentes de IA

**Agentes de IA** = desenvolvedor + distribuidor + aplicador only.

| Role | Art. 4 | Meaning |
|------|--------|---------|
| Desenvolvedor | V | Develops an AI system (directly or by order) to place it on the market or apply it in a service under own name/brand |
| Distribuidor | VI | Makes an AI system available for a third party to apply |
| Aplicador | VII | Employs or uses an AI system in own name or benefit, including configuring, maintaining, or supplying data for operation/monitoring |

Art. 18 splits high-risk **governance** between desenvolvedor and aplicador. Distributors **verify** governance before the system is placed on the market (Art. 16 §3, Art. 18 §2). **Substantial modification** or change of purpose by aplicador or distribuidor makes that agent a **desenvolvedor** (Art. 18 §5).

Drop EU **developer / deployer / operator** as legal categories.

### Supervision — SIA, ANPD as proposed coordinator (Arts. 16, 45)

Art. 45: the Executive **may** establish the Sistema Nacional de Regulação e Governança de Inteligência Artificial (**SIA**). Proposed members: **ANPD** as coordinating autoridade competente; **autoridades setoriais**; **Cria**; **Cecia**. Sectoral authorities set high-risk lists **prevalently** (Art. 16). Chamber text **may change the coordinator** — verify before advising.

Serious incidents (Art. 42) go to the **sectoral authority**, deadline **to be established** — **not** 72 hours to ANPD (that clock is LGPD-imported, not in this bill).

### Proposed risk tiers

| Tier | Senate articles | Key proposed duties |
|------|-----------------|---------------------|
| Risco excessivo (prohibited) | Art. 13 | Do not develop, implement, or use (narrow biometric exceptions) |
| Alto risco | Arts. 14–16, 18, 25–27 | Governance + AIA; Art. 6 rights |
| Not high-risk | Art. 12, Art. 14 parágrafo único, Art. 5 | Art. 5 rights still apply; Art. 12 preliminary assessment is optional ("poderá") |

### Rights — not "8 rights"

| Scope | Articles | Rights |
|-------|----------|--------|
| All systems | Art. 5 | Information; privacy/LGPD; non-discrimination |
| High-risk only | Art. 6 | Explanation; contest/review; human review |
| Human oversight | Art. 8 | May be skipped if impossible or disproportionate, with alternative measures |
| Portability | Art. 22 + LGPD | Public-sector data architecture — **not** a general AI-bill right |
| Prior notice | — | **No** named "right to prior notice" |

### Short article index (Senate substitute)

Look up here or in `references/` before citing.

| Articles | Topic |
|---------|-------|
| 1 | Scope; exclusions in Brazil |
| 4 | Definitions; desenvolvedor / distribuidor / aplicador |
| 5–11 | Rights (Art. 5 all; Art. 6 high-risk; Art. 8 oversight exception) |
| 12 | Optional preliminary assessment |
| 13 | Prohibited (risco excessivo) |
| 14–16 | High-risk list; sectoral lists (prevalent) |
| 17–18 | Governance; distributor verification; substantial modification §5 |
| 19–20 | Synthetic-content labelling (**proposed**) |
| 22–24 | Public administration (**proposed**) |
| 25–28 | AIA; conclusions public under regulation |
| 29–33 | GPAI / generative / systemic risk (**proposed**; numbering skips 31) |
| 35–36 | Civil liability CDC / Civil Code (**proposed**) |
| 42 | Serious incidents to sectoral authority, deadline TBD |
| 44 | Public high-risk AIA document database |
| 45–49 | SIA; ANPD coordinates in Senate text |
| 50 | Administrative sanctions (**proposed**) |
| 62–64 | Training-data copyright summary and opt-out (**proposed**) |
| 80 | Vacatio: 730 days general; 180 days Art. 13 / GPAI / most copyright; Art. 62 immediate |

Detail: `references/risk-classification.md`, `references/rights-of-affected-persons.md`, `references/governance-requirements.md`, `references/obligations-by-role.md`, `references/gpai-generative.md`, and `references/sanctions-and-timeline.md`. Output recipes: `references/brazil-templates.md`. Worked examples: `references/brazil-worked-examples.md`. Crosswalks: `references/cross-framework-mapping.md`.

---

## Workflows

Fill the matching recipe in `references/brazil-templates.md`. Prefix every artefact with the status banner.

### Workflow 1 — Risk classification

**Inputs:** System description, sector, context of use, whether used in Brazil.

**Process:**

0. **Verify Chamber status** (see Role). If a Chamber substitutivo exists, use it.
1. **Art. 1 screen** — In Brazil? Any §1 exclusion (personal, defense, pre-market R&D, mere hosting)?
2. **Art. 12 preliminary assessment (optional)** — The agent **poderá** run a simplified self-assessment before market/use. It is **good practice**, not a hard EU-style tree. Sectoral authority may simplify or waive (§2). Result may support later conformity (Art. 12 §5).
3. **Art. 13 prohibited** — Predictive policing/recidivism; CSAM generation; autonomous weapons; public-power illegitimate/disproportionate ranking (not a blanket social-scoring ban); real-time remote biometrics in public with **specific criminal-procedure exceptions**. If prohibited and no exception, stop.
4. **Art. 14 high-risk** — Purpose- and context-specific (education when **determinant** for admission/progress; healthcare when **relevant integrity risk**; emotion recognition Art. 14 XI). Apply **parágrafo único**: not high-risk if intermediate tech that does not determine the result.
5. **Art. 16** — Check whether a sectoral high-risk list (prevalent) already treats this use.
6. Else — **not high-risk**; Art. 5 rights still apply.

**Output:** Classification recipe, labelled not enacted.

Full tables live in `references/risk-classification.md`.

### Workflow 2 — Rights mapping

**Inputs:** How the system interacts with people; high-risk or not.

**Process:**

1. Map **Art. 5** for every in-scope system (information; LGPD privacy; non-discrimination).
2. If high-risk, add **Art. 6** (explanation; contest/review; human review).
3. Apply **Art. 8**: human oversight may be skipped when impossible or disproportionate, with effective alternatives.
4. Portability sits in Art. 22 public-sector architecture + LGPD, not as a general AI-bill right.

**Output:** Art. 5 vs Art. 6 rights table.

Full table lives in `references/rights-of-affected-persons.md`.

### Workflow 3 — Governance and AIA design

**Inputs:** Roles, high-risk systems, existing LGPD DPIA.

**Process:**

1. Split Art. 18 duties: aplicador (I) vs desenvolvedor (II); distributor verification (Art. 18 §2).
2. AIA (Arts. 25–27) for high-risk **before** market introduction; continuous updates (Art. 26). May combine with LGPD RIPD (Art. 27).
3. Publication: Art. 44 **authority-run** public database of **public** AIA documents; Art. 23 III publication is **public administration**. Art. 28: conclusions public under regulation, trade secrets reserved.
4. Incidents: Art. 42 to **sectoral authority**, prazo a ser estabelecido. Art. 25 §7 unexpected relevant risk — communicate immediately to sectoral authority and other chain agents.

**Output:** Governance framework citing those articles, labelled not enacted.

Detail lives in `references/governance-requirements.md`.

### Workflow 4 — Obligations by role

**Inputs:** Art. 4 role(s); risk class.

**Process:**

1. Assign desenvolvedor / distribuidor / aplicador (multiple roles possible).
2. If substantial modification (Art. 18 §5), treat aplicador/distribuidor as desenvolvedor.
3. Map Art. 18, AIA 25–27, GPAI 29–33, copyright 62–64 as applicable.
4. Score 🔴🟡🟢 as **preparedness**, not in-force compliance.

**Output:** Role-matrix row.

Matrix lives in `references/obligations-by-role.md`.

### Workflow 5 — Preparedness gap assessment

**Inputs:** Current practices, systems in Brazil, documentation.

**Process:**

1. Assess against **proposed** Senate duties as **preparedness for a moving bill**.
2. Rate 🔴 not started / 🟡 partial / 🟢 prepared (evidence exists).
3. Flag Chamber-open items: SIA coordinator, high-risk lists, incident prazo.
4. Prioritize by Art. 80 vacatio (Art. 13 / GPAI / Art. 62 would bite first **if** enacted).

**Output:** Preparedness gap rows.

---

## Preparedness gaps (moving bill)

Full crosswalk tables live only in `references/cross-framework-mapping.md`.

**EU alignment does not cover:** Portuguese-language Art. 5 information; LGPD overlay; SIA/sectoral lists; Art. 13 extras (predictive policing/recidivism, CSAM generation, autonomous weapons); GPAI **copyright summary** and rightholder opt-out (Arts. 62–64).

1. **Chamber text may replace the Senate substitute** — Treat Art. 13 extras, SIA coordinator, and high-risk lists as unsettled. Re-check tramitação before advising.
2. **Roles mapped to EU deployer/operator** — Brazilian legal categories are desenvolvedor / distribuidor / aplicador. Substantial modification (Art. 18 §5) reclassifies downstream agents.
3. **ANPD treated as sole AI regulator** — Senate Art. 45 coordinates SIA with sectoral authorities, Cria, and Cecia. Chamber may change the coordinator.
4. **Eight rights / prior notice / general portability** — Only Art. 5 (all) + Art. 6 (high-risk). Portability is Art. 22 public-sector + LGPD.
5. **72-hour ANPD incident clock and 5-year logs** — Not in the Senate text. Art. 42 prazo is to be established by the sectoral authority.
6. **Private-sector "publish your AIA"** — Art. 23 III is public administration; Art. 44 is an authority database of public AIA documents.
7. **Assuming extra-territorial LGPD-style reach** — Art. 1 is AI **in Brazil**, plus listed exclusions.
8. **Treating Art. 12 as a mandatory EU-style gate** — It is optional ("poderá") and still useful: good practice; may support Art. 50 §1 and Art. 34 treatment.
