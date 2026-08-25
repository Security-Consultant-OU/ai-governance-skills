# Output templates — Senate-approved PL 2338/2023 (not enacted)

**Label (25 August 2026):** based on Senate-approved PL 2338/2023; not enacted.

## Contents

- Status banner (required on every output)
- Default artefact
- Classification recipe
- Rights table (Art. 5 vs Art. 6)
- Role matrix row
- Preparedness gap row
- Citation recipe
- Refused-certificate recipe

---

## Status banner (required on every output)

Copy this block as the **first** paragraph of every answer:

```
**Status (25 August 2026):** Based on Senate-approved PL 2338/2023 (substitute of 10 December 2024); **not enacted**. Chamber of Deputies: awaiting the rapporteur’s opinion in the Special Commission (Dep. Aguinaldo Ribeiro). **Not** pending presidential sanction. This is preparedness against a moving bill, not in-force compliance.

Tramitação: https://www.camara.leg.br/proposicoesWeb/fichadetramitacao/fichadetramitacao/?idProposicao=2487262
```

If a Chamber substitutivo now exists, keep the **not enacted** label and state that the Chamber text is preferred.

---

## Default artefact

When the user does not name a document type, produce:

1. Status banner (above)
2. Classification recipe (below) filled for the described system against the Senate substitute

---

## Classification recipe

Fill **every** row in this order. Art. 12 is optional ("poderá") — record whether it was run; it is not a mandatory gate.

```
**Status (25 August 2026):** Based on Senate-approved PL 2338/2023 (substitute of 10 December 2024); **not enacted**. Chamber of Deputies: awaiting the rapporteur’s opinion in the Special Commission (Dep. Aguinaldo Ribeiro). **Not** pending presidential sanction. This is preparedness against a moving bill, not in-force compliance.

Tramitação: https://www.camara.leg.br/proposicoesWeb/fichadetramitacao/fichadetramitacao/?idProposicao=2487262

SYSTEM: [name / short description]
ROLES (Art. 4): desenvolvedor / distribuidor / aplicador — [who]

| Step | Senate hook | Finding |
|------|-------------|---------|
| 1. Territorial screen | Art. 1 + §1 exclusions | In Brazil: yes/no. Exclusion I–IV: [none / which] |
| 2. Optional prelim | Art. 12 ("poderá") | Run: yes/no/recommended. Not a mandatory tree. Sectoral waiver (Art. 12 §2): [if any] |
| 3. Prohibited | Art. 13 | Risco excessivo: yes/no. Exception (Art. 13 IV): [if any]. If yes and no exception, stop |
| 4. High-risk context | Art. 14 + parágrafo único | Inciso: [I–XII or none]. Intermediate/non-determinant: [yes/no] |
| 5. Sectoral list | Art. 16 | Prevalent sectoral list: [none known / which] |

RESULT: risco excessivo / alto risco / not high-risk (Art. 5 still applies)
NEXT PREPAREDNESS: [Art. 18 / AIA Arts. 25–27 / Art. 5 only]
```

---

## Rights table (Art. 5 vs Art. 6)

```
**Status (25 August 2026):** Based on Senate-approved PL 2338/2023 (substitute of 10 December 2024); **not enacted**. Chamber of Deputies: awaiting the rapporteur’s opinion in the Special Commission (Dep. Aguinaldo Ribeiro). **Not** pending presidential sanction. This is preparedness against a moving bill, not in-force compliance.

RIGHT (Senate)                 | SCOPE        | HOW TO PREPARE                         | EVIDENCE              | STATUS
Information (Art. 5 I)         | All systems  | Portuguese (or audience) disclosure    | Notices, logs         | 🔴/🟡/🟢
Privacy / LGPD (Art. 5 II)     | Personal data| Run LGPD programme in parallel         | RIPD, DPO records     | 🔴/🟡/🟢
Non-discrimination (Art. 5 III)| All systems  | Bias testing and remediation           | Test reports          | 🔴/🟡/🟢
Explanation (Art. 6 I)         | High-risk    | Intelligible rationale (Arts. 6–7)     | Templates             | 🔴/🟡/🟢 / n/a
Contest and review (Art. 6 II) | High-risk    | Accessible contest channel              | Process + outcomes    | 🔴/🟡/🟢 / n/a
Human review (Art. 6 III)      | High-risk    | Reviewer with authority, or Art. 8 alt. | Roster / Art. 8 memo  | 🔴/🟡/🟢 / n/a
```

Scores are **preparedness**, not in-force compliance. Art. 6 rows are `n/a` when the system is not high-risk.

---

## Role matrix row

```
**Status (25 August 2026):** Based on Senate-approved PL 2338/2023 (substitute of 10 December 2024); **not enacted**. Chamber of Deputies: awaiting the rapporteur’s opinion in the Special Commission (Dep. Aguinaldo Ribeiro). **Not** pending presidential sanction. This is preparedness against a moving bill, not in-force compliance.

ENTITY: [name]    ASSIGNED ROLE(S): [desenvolvedor / distribuidor / aplicador]
Art. 18 §5 substantial modification / purpose change: yes/no — [if yes, treat as desenvolvedor]

OBLIGATION                      | DESENVOLVEDOR | DISTRIBUIDOR      | APLICADOR | ARTICLE      | STATUS
Art. 12 optional prelim         | May perform   | May perform       | May perform | Art. 12    | 🔴/🟡/🟢
Art. 13 prohibited screen       | Must not develop/use; prevent caput uses | Must not distribute | Must not implement/use | Art. 13 | 🔴/🟡/🟢
Art. 18 high-risk governance    | II            | Verify before market (Art. 18 §2) | I | Art. 18 | 🔴/🟡/🟢
AIA before market               | Yes if high-risk | Support          | Yes if high-risk | Arts. 25–26 | 🔴/🟡/🟢
Art. 5 rights                   | Design to enable | Do not strip disclosures | Provide at interaction | Art. 5 | 🔴/🟡/🟢
Art. 6 rights                   | Enable technically | —               | Primary interface if high-risk | Arts. 6–9 | 🔴/🟡/🟢 / n/a
Incident notice                 | Sectoral authority, prazo TBD | Same | Same | Art. 42 | 🔴/🟡/🟢
```

English "deployer" does not appear as a column. Informal synonym for aplicador only.

---

## Preparedness gap row

Score 🔴 not started / 🟡 partial / 🟢 prepared. These scores are **preparedness** for a moving bill, not in-force compliance. Do not write "non-compliant with the Brazil AI Act."

```
**Status (25 August 2026):** Based on Senate-approved PL 2338/2023 (substitute of 10 December 2024); **not enacted**. Chamber of Deputies: awaiting the rapporteur’s opinion in the Special Commission (Dep. Aguinaldo Ribeiro). **Not** pending presidential sanction. This is preparedness against a moving bill, not in-force compliance.

PROPOSED REQUIREMENT            | STATUS      | EVIDENCE            | GAP NOTES                              | PRIORITY
Art. 13 prohibited screen       | 🟢 Prepared | Review memo         | Brazil-specific extras checked          | —
Art. 12 optional prelim         | 🟡 Partial  | Informal notes      | Optional ("poderá"); still good practice | Medium
AIA Arts. 25–27                 | 🔴 Not started | —                | Prepare if high-risk; bill may move    | High
Art. 42 incident channel        | 🟡 Partial  | LGPD process only   | Sectoral authority TBD; no 72h ANPD     | Medium
Art. 62 copyright summary       | 🔴 Not started | —                | Immediate vacatio if enacted (Art. 80) | High if GPAI
```

---

## Citation recipe

Every legal sentence includes a Senate article number found in this skill’s `references/` or SKILL.md article index.

If the number is not indexed: write "not in the Senate substitute as indexed here."

Never write `Art. X`. Never paste an EU article as a Brazilian duty.

---

## Refused-certificate recipe

When the user asks whether this is law, or asks for a Brazil AI Act compliance certificate:

```
**Status (25 August 2026):** Based on Senate-approved PL 2338/2023 (substitute of 10 December 2024); **not enacted**. Chamber of Deputies: awaiting the rapporteur’s opinion in the Special Commission (Dep. Aguinaldo Ribeiro). **Not** pending presidential sanction. This is preparedness against a moving bill, not in-force compliance.

Tramitação: https://www.camara.leg.br/proposicoesWeb/fichadetramitacao/fichadetramitacao/?idProposicao=2487262

This skill cannot issue a compliance certificate. PL 2338/2023 is a bill. Chamber text may still replace the Senate substitute.

Offered instead: a status-labelled classification of the described system against the Senate substitute (classification recipe above).
```
