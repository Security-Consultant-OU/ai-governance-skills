# Worked examples — Senate-approved PL 2338/2023 (not enacted)

**Label (25 August 2026):** based on Senate-approved PL 2338/2023; not enacted.

## Contents

- Example 1 — Status-first answer
- Example 2 — Aplicador vs desenvolvedor
- Example 3 — Art. 12 optional preliminary assessment
- Example 4 — "Is this law?" / no compliance certificate

Every example output starts with the status banner and is labelled not enacted.

---

## Example 1 — Status-first answer

**User asks:** "What is the status of the Brazil AI Act? Are we pending presidential sanction?"

**Skill does:** Date-stamped tramitação check. States Chamber awaiting rapporteur as of 25 August 2026; **not** pending sanction. Does not treat the bill as law.

**Artefact:**

```
**Status (25 August 2026):** Based on Senate-approved PL 2338/2023 (substitute of 10 December 2024); **not enacted**. Chamber of Deputies: awaiting the rapporteur’s opinion in the Special Commission (Dep. Aguinaldo Ribeiro). **Not** pending presidential sanction. This is preparedness against a moving bill, not in-force compliance.

Tramitação: https://www.camara.leg.br/proposicoesWeb/fichadetramitacao/fichadetramitacao/?idProposicao=2487262

PL 2338/2023 is a bill. The Senate approved a substitute on 10 December 2024. As of 25 August 2026 the Chamber of Deputies has not finished its Special Commission work; the file is awaiting the rapporteur’s opinion. It is not on the President's desk.

If the Chamber amends the text, the bill returns to the Senate for reconciliation. Advise against the Senate substitute only until a Chamber substitutivo exists; then prefer the Chamber text and relabel.

This skill can prepare risco excessivo / alto risco classification, rights mapping, AIA design, and GPAI/copyright readiness against the Senate text. It cannot certify in-force compliance.
```

---

## Example 2 — Aplicador vs desenvolvedor

**User asks:** "We license a third-party CV-ranking model, fine-tune it on our Brazilian applicant data, and use it to screen candidates in São Paulo. Are we the deployer?"

**Skill does:** Map Art. 4 roles. Apply Art. 18 I vs II. Test Art. 18 §5 substantial modification. Classify the use under Art. 14 III. Fill a role-matrix row. English "deployer" is not a legal category.

**Artefact:**

```
**Status (25 August 2026):** Based on Senate-approved PL 2338/2023 (substitute of 10 December 2024); **not enacted**. Chamber of Deputies: awaiting the rapporteur’s opinion in the Special Commission (Dep. Aguinaldo Ribeiro). **Not** pending presidential sanction. This is preparedness against a moving bill, not in-force compliance.

Tramitação: https://www.camara.leg.br/proposicoesWeb/fichadetramitacao/fichadetramitacao/?idProposicao=2487262

English "deployer" is not a Brazilian legal category. Informal synonym for aplicador only.

ENTITY: hiring company in Brazil
ASSIGNED ROLE(S): aplicador (Art. 4 VII) and, after fine-tuning, desenvolvedor (Art. 18 §5)
Art. 18 §5 substantial modification / purpose change: yes — fine-tune on own applicant data for screening is a substantial modification / change of purpose. That agent is treated as desenvolvedor.

Vendor that built the base model remains a desenvolvedor of the unmodified system. The hiring company is not a distribuidor unless it makes the system available for a third party to apply (Art. 4 VI).

Risk (preview): employment screening is Art. 14 III alto risco (purpose-specific). Art. 13 does not apply on these facts. Art. 16 sectoral list: none known; re-check if enacted.

OBLIGATION                      | DESENVOLVEDOR | DISTRIBUIDOR | APLICADOR | ARTICLE | STATUS
Art. 12 optional prelim         | May perform   | n/a          | May perform | Art. 12 | 🟡 Partial
Art. 13 prohibited screen       | Must not develop/use | n/a   | Must not implement/use | Art. 13 | 🟢 Prepared
Art. 18 high-risk governance    | II (because §5) | n/a | I | Art. 18 | 🔴 Not started
AIA before market               | Yes (alto risco) | n/a      | Yes | Arts. 25–26 | 🔴 Not started
Art. 5 rights                   | Design to enable | n/a      | Provide at interaction | Art. 5 | 🟡 Partial
Art. 6 rights                   | Enable technically | n/a    | Primary interface | Arts. 6–9 | 🔴 Not started
Incident notice                 | Sectoral authority, prazo TBD | n/a | Same | Art. 42 | 🟡 Partial
```

---

## Example 3 — Art. 12 optional preliminary assessment

**User asks:** "Must we complete a preliminary risk assessment before launching a Portuguese customer-support chatbot for users in Brazil?"

**Skill does:** Answer Art. 12 as optional ("poderá"), then still walk Art. 1 → 12 optional → 13 → 14 → 16. Does not import an EU-style mandatory tree.

**Artefact:**

```
**Status (25 August 2026):** Based on Senate-approved PL 2338/2023 (substitute of 10 December 2024); **not enacted**. Chamber of Deputies: awaiting the rapporteur’s opinion in the Special Commission (Dep. Aguinaldo Ribeiro). **Not** pending presidential sanction. This is preparedness against a moving bill, not in-force compliance.

Tramitação: https://www.camara.leg.br/proposicoesWeb/fichadetramitacao/fichadetramitacao/?idProposicao=2487262

SYSTEM: Portuguese customer-support chatbot used in Brazil
ROLES (Art. 4): confirm whether the entity develops it (desenvolvedor) or only employs it (aplicador)

| Step | Senate hook | Finding |
|------|-------------|---------|
| 1. Territorial screen | Art. 1 + §1 exclusions | Used in Brazil: yes. Not personal (I), not defense (II), not pre-market R&D (III), not mere hosting (IV). In scope. |
| 2. Optional prelim | Art. 12 ("poderá") | **Not mandatory.** The agente de IA "poderá" run a simplified self-assessment before market/use. Recommended as good practice; may support Art. 50 §1 and Art. 34 treatment. Sectoral authority may simplify or waive (Art. 12 §2). |
| 3. Prohibited | Art. 13 | No match on these facts (not predictive policing/recidivism, CSAM generation, autonomous weapons, public-power ranking, or real-time remote biometrics in public). |
| 4. High-risk context | Art. 14 + parágrafo único | No listed finalidade on these facts (not education determinant, not employment screening, not essential-services gatekeeping, not healthcare with relevant integrity risk). Customer support is not alto risco solely because it is a chatbot. Re-screen if it becomes determinant for Art. 14 IV essential services. |
| 5. Sectoral list | Art. 16 | None known. Lists would be set prevalently by autoridades setoriais if the bill is enacted. |

RESULT: not high-risk under the Senate substitute, on these facts. Art. 5 still applies (information, LGPD, non-discrimination). Art. 6 does not. If the system generates conteúdo sintético, Art. 19 identifier is a proposed duty for that output.

Art. 12 is optional. Skipping it does not by itself make the system prohibited or high-risk. Running it remains useful preparedness.
```

---

## Example 4 — "Is this law?" / no compliance certificate

**User asks:** "Issue a Brazil AI Act compliance certificate for our HR screening tool."

**Skill does:** Refuse the in-force claim. Produce the bill banner and tramitação link. Offer a status-labelled classification as preparedness. No certificate.

**Artefact:**

```
**Status (25 August 2026):** Based on Senate-approved PL 2338/2023 (substitute of 10 December 2024); **not enacted**. Chamber of Deputies: awaiting the rapporteur’s opinion in the Special Commission (Dep. Aguinaldo Ribeiro). **Not** pending presidential sanction. This is preparedness against a moving bill, not in-force compliance.

Tramitação: https://www.camara.leg.br/proposicoesWeb/fichadetramitacao/fichadetramitacao/?idProposicao=2487262

This skill cannot issue a compliance certificate. PL 2338/2023 is a bill. There is no in-force Brazil AI Act to certify against. Chamber text may still replace the Senate substitute.

Offered instead: a status-labelled classification of the HR screening tool against the Senate substitute.

SYSTEM: HR screening tool used in Brazil
ROLES (Art. 4): confirm desenvolvedor / distribuidor / aplicador (English "deployer" is not a legal category)

| Step | Senate hook | Finding |
|------|-------------|---------|
| 1. Territorial screen | Art. 1 | Used in Brazil: yes, if deployed there. |
| 2. Optional prelim | Art. 12 ("poderá") | Optional. Recommended before market/use. |
| 3. Prohibited | Art. 13 | Employment screening is not an Art. 13 prohibition on these facts. |
| 4. High-risk context | Art. 14 III | Recruitment, screening, filtering, or evaluation of candidates is alto risco. |
| 5. Sectoral list | Art. 16 | None known; sectoral lists would prevail if enacted. |

RESULT: alto risco (Art. 14 III) under the Senate substitute, on these facts — **preparedness**, not a legal finding of in-force non-compliance. Next: Art. 18 split, AIA Arts. 25–27, Art. 5 and Art. 6 rights. Scores below would be preparedness only.
```
