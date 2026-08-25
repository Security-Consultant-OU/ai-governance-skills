# ISO/IEC 42001 data-for-AI inventory

Annex A.7 selectable controls: **A.7.2, A.7.3, A.7.4, A.7.5, A.7.6**. Data resources: **A.4.3**. A.7.1 and A.4.1 are objectives, not controls. There is no A.5.8.

If document type is omitted, fill the dataset table, then the coverage scores.

---

## Dataset register

| Dataset ID | Linked system ID | Name | Category (A.4.3) | Source and rights (A.7.3) | Known bias / limits | Quality criteria (A.7.4) | Provenance recoverable (A.7.5 y/n) | Preparation methods (A.7.6) | Retention | Owner |
|------------|------------------|------|------------------|---------------------------|---------------------|--------------------------|------------------------------------|-----------------------------|-----------|-------|
| DAT-001 | SYS-001 | | train / validate / test / production | | | | | | | |

Copy a blank row:

| Dataset ID | Linked system ID | Name | Category (A.4.3) | Source and rights (A.7.3) | Known bias / limits | Quality criteria (A.7.4) | Provenance recoverable (A.7.5 y/n) | Preparation methods (A.7.6) | Retention | Owner |
|------------|------------------|------|------------------|---------------------------|---------------------|--------------------------|------------------------------------|-----------------------------|-----------|-------|
| | | | | | | | | | | |

Category must be one of: train, validate, test, production. Do not invent categories.

---

## Coverage (🔴🟡🟢)

Score per dataset, then overall.

| Control | What “🟢” looks like | DAT-001 | DAT-002 |
|---------|----------------------|---------|---------|
| A.7.2 | Development-data rules exist (privacy, representativeness, integrity) | | |
| A.7.3 | Source, rationale, rights, metadata recorded | | |
| A.7.4 | Named quality tests run before use | | |
| A.7.5 | Lineage can rebuild the set | | |
| A.7.6 | Cleaning/labelling/augmentation method recorded | | |
| A.4.3 | Dataset listed as a resource of the AI system | | |

---

## Provenance test (A.7.5)

If any answer is no, status is 🔴 or 🟡.

| Question | Y/N | Evidence |
|----------|-----|----------|
| Who created or licensed this dataset? | | |
| What transformations were applied, in order? | | |
| Who validated it, against which criteria? | | |
| Where does it live; who can transfer it? | | |
| Can we reproduce the snapshot used for the current model version? | | |
