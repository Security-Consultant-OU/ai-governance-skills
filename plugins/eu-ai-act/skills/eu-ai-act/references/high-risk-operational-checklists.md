# EU high-risk operational checklists (Chapter III)

Article-keyed autoeval shells for **high-risk AI systems** after Art. 6 classification. Status: 🔴 not started · 🟡 partial · 🟢 implemented. Do not invent article numbers.

These tables follow the shape of operational workbooks (article text → guidance measures → additional measures → autoeval). If the user has Spanish `.xlsx` checklists with sheets `Artículo RIA`, `Medidas guías (MG)`, `Autoeval MG`, `Medidas Adicionales (MA)`, `Autoeval MA`, fill those sheets using the article in this file — **do not copy third-party measure wording into the repo**.

Provider-default unless the user is a deployer (then add Art. 26 rows). Art. 12(3) extra logging is **only** Annex III point 1(a).

If the user omits which checklist: produce **Art. 9** first, then the rest in article order.

---

## Workbook → article

| Workbook theme | Article | Output |
|----------------|---------|--------|
| Risk management | Art. 9 | Lifecycle RMS; foreseeable misuse; residual risk; testing |
| Data governance | Art. 10 | Train/val/test governance; bias exam; representativeness |
| Technical documentation | Art. 11 + Annex IV | Annex IV pack (default generated document for this skill) |
| Logging / records | Art. 12 | Event logs for Art. 79(1) risk, substantial modification, Art. 72, Art. 26(5) |
| Transparency | Art. 13 | Instructions for use to deployers |
| Human oversight | Art. 14 | Effective oversight; Art. 14(5) dual control only for remote biometric ID |
| Accuracy | Art. 15 (accuracy) | Documented metrics in IFU |
| Robustness | Art. 15 (robustness) | Errors, faults, fail-safe |
| Cybersecurity | Art. 15 (cybersecurity) | Unauthorised manipulation; adversarial inputs |
| Quality management | Art. 17 | QMS covering design, test, RMS, PMS, incidents |
| Incidents / corrective action | Arts. 20, 73 | Corrective action; serious-incident report ≤ 15 days after awareness |
| Post-market monitoring | Art. 72 | Proportionate PMS |

---

## Autoeval row (copy)

| ID | Article | Measure (short duty) | Status 🔴🟡🟢 | Evidence | Gap |
|----|---------|----------------------|---------------|----------|-----|
| | | | | | |

---

## Seed duties (provider)

| ID | Article | Measure (short duty) | Status 🔴🟡🟢 | Evidence | Gap |
|----|---------|----------------------|---------------|----------|-----|
| RMS-1 | Art. 9 | Iterative RMS across the lifecycle | | | |
| RMS-2 | Art. 9 | Known and reasonably foreseeable risks, including misuse | | | |
| RMS-3 | Art. 9 | Residual-risk record after measures | | | |
| RMS-4 | Art. 9 | Testing before placing on the market and during the lifecycle | | | |
| DAT-1 | Art. 10 | Governance for training, validation, and test data | | | |
| DAT-2 | Art. 10 | Bias examination including proxies | | | |
| DAT-3 | Art. 10 | Statistical properties fit the deployment setting | | | |
| DOC-1 | Art. 11 | Annex IV technical documentation drawn up **before** placing on the market | | | |
| LOG-1 | Art. 12(1)–(2) | Automatic event recording over the system lifetime | | | |
| LOG-2 | Art. 12(3) | Extra biometric logs — **N/A unless Annex III 1(a)** | | | |
| TRN-1 | Art. 13 | Instructions for use: capabilities, limits, metrics, oversight, resources | | | |
| HO-1 | Art. 14 | Human can understand, monitor, disregard, interrupt, override | | | |
| HO-2 | Art. 14(5) | Two-person verification — **N/A unless remote biometric ID** | | | |
| ACC-1 | Art. 15 | Accuracy levels documented in the IFU | | | |
| ROB-1 | Art. 15 | Resilience to errors/faults; fail-safe | | | |
| CYB-1 | Art. 15 | Cybersecurity against third-party manipulation and adversarial inputs | | | |
| QMS-1 | Art. 17 | Documented QMS covering compliance strategy, design, test, RMS, PMS | | | |
| NCR-1 | Art. 20 | Corrective action, withdrawal, or recall if the system presents a risk | | | |
| PMS-1 | Art. 72 | Proportionate post-market monitoring | | | |
| INC-1 | Art. 73 | Serious-incident report to MSA without delay, ≤ 15 days after awareness | | | |
| CE-1 | Arts. 43, 47, 48, 49 | Conformity path, DoC, CE, EU database registration | | | |

---

## Seed duties (deployer of high-risk)

| ID | Article | Measure (short duty) | Status 🔴🟡🟢 | Evidence | Gap |
|----|---------|----------------------|---------------|----------|-----|
| DEP-1 | Art. 26(1) | Use according to instructions for use | | | |
| DEP-2 | Art. 26(2) | Oversight persons have competence, training, and authority | | | |
| DEP-3 | Art. 26(4) | Input data relevant and representative | | | |
| DEP-4 | Art. 26(5) | Monitor operation; inform provider of risks | | | |
| DEP-5 | Art. 26(6) | Keep logs at least 6 months unless other Union/national law | | | |
| DEP-6 | Art. 26(7) | Inform workers’ representatives before workplace use | | | |
| DEP-7 | Art. 26(11) | Inform natural persons subject to Annex III decisioning systems | | | |
| DEP-8 | Art. 27 | FRIA only if the Art. 27 gate is met — do not auto-require | | | |
