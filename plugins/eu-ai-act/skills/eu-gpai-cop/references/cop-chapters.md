# GPAI Code of Practice (Article 56) — chapters and model documentation

Art. 56 codes of practice help GPAI **model** providers demonstrate Chapter V compliance. Adherence to a Commission-approved code creates a **presumption of conformity** with the corresponding obligations. Providers may use **alternative adequate means** instead. This is not Brazil GPAI and not ISO AISIA.

Do not invent CoP paragraph numbers. If the user has the official chapter PDFs or the Model Documentation Form, quote **their** clause IDs; otherwise use the chapter titles below.

Status: 🔴 not started · 🟡 partial · 🟢 implemented / ⚪ N/A — alternative means.

---

## Chapter coverage

| Chapter | Typical Chapter V link | What the artefact must show |
|---------|------------------------|-----------------------------|
| Transparency (GPAI models) | Art. 53(1)(a)–(b), Annex XI downstream information | Documentation and downstream-provider information sufficient for system providers |
| Copyright | Art. 53(1)(c) | Union copyright / TDM opt-out (Directive (EU) 2019/790 Art. 4(3)) operationalised |
| Safety and security | Art. 55 when systemic-risk; otherwise state N/A | Evaluation, Union-level systemic-risk assessment, incidents, model+infra cyber — do not collapse 55(1)(b) into red-teaming |
| Transparency of AI-generated content | Art. 50 (systems), not a substitute for model Art. 53 | Marking/detectability duties of the **system** provider or deployer — hand off to `eu-ai-act` classification if the question is Art. 50 only |

---

## Adherence vs alternative means

| Path | When | Output |
|------|------|--------|
| Adhere to CoP | User will sign / has signed the GPAI CoP | Chapter autoeval + model documentation form |
| Alternative means | User will not adhere | Map each Art. 53/55 duty to a named alternative artefact; no CoP presumption |

---

## Model documentation form (fill-in)

Public CoP model-documentation fields. Replace brackets. Do not invent Annex XI section letters.

```
GPAI MODEL DOCUMENTATION — Art. 56 CoP / Art. 53(1)(a)

Model name / version: [ ]
Provider: [ ]
Licence / OSS (Art. 53(2) test): [weights, architecture, and usage info public? Y/N]
Systemic-risk (Art. 51 / 10^25 FLOPs / Annex XIII): [Yes / No / under assessment]
Art. 52 notification (if 51 met): [date or N/A]

1. Intended and prohibited uses: [ ]
2. Architecture and training process (high level): [ ]
3. Training data description / public summary pointer (Art. 53(1)(d)): [ ]
4. Compute (training): [ ]
5. Evaluation and known limitations: [ ]
6. Downstream-provider information pack location (Art. 53(1)(b)): [ ]
7. Copyright / TDM opt-out process (Art. 53(1)(c)): [ ]
8. If systemic-risk: Art. 55(1)(a)–(d) artefact pointers: [ ]
```

---

## Chapter autoeval row

| Chapter | CoP clause (from user PDF or “not in context”) | Mapped article | Status 🔴🟡🟢 | Evidence | Gap |
|---------|-----------------------------------------------|----------------|---------------|----------|-----|
| | | | | | |
