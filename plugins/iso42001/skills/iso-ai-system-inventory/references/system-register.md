# ISO/IEC 42001 AI system register (Clause 4.3)

Self-contained register for AIMS scope. Clause **4.3**. Context **4.1**. Interested parties **4.2**. This is not a SoA and not Annex A.

If document type is omitted, produce the scope sentence, then this table, then the exclusion log.

---

## Scope sentence (fill)

AIMS scope: [organisation / units]. Role: [provider / user / both]. Included AI: [types]. Locations: [sites / cloud regions]. Valid from: [date]. Approved by: [role].

---

## Register table

| ID | Name | Intended purpose | Provider or user | Owner | Life-cycle stage | Personal data (y/n) | In scope (y/n) | Notes |
|----|------|------------------|------------------|-------|------------------|---------------------|----------------|-------|
| SYS-001 | | | | | [idea / design / deploy / operate / retire] | | | |
| SYS-002 | | | | | | | | |

Copy a blank row:

| ID | Name | Intended purpose | Provider or user | Owner | Life-cycle stage | Personal data (y/n) | In scope (y/n) | Notes |
|----|------|------------------|------------------|-------|------------------|---------------------|----------------|-------|
| | | | | | | | | |

Life-cycle stage values: idea, design/development, verification, deployment, operation, retirement. Do not invent Annex A IDs as stage names.

---

## Exclusion log

Every **In scope = n** row needs a line here. “Not important” is not a rationale.

| System ID | Exclusion rationale | Review date |
|-----------|---------------------|-------------|
| | | |

---

## Completeness check (🔴🟡🟢)

| Check | Status | Gap |
|-------|--------|-----|
| Embedded SaaS AI listed | | |
| Pilots and proofs of concept listed | | |
| Internal automation / copilots listed | | |
| Every in-scope row has an owner | | |
| Register reviewed after last new system | | |
| Interested parties include people subject to AI decisions (4.2) | | |

---

## Discovery questions (if the inventory is empty)

| Ask | Looking for |
|-----|-------------|
| Which products or processes use a model, ranking, or generative output? | Named systems |
| Which SaaS tools score, recommend, generate, or classify? | Embedded AI |
| Any pilots, sandboxes, or shadow model-hub use? | Out-of-band systems |
| Who can approve a new AI tool? | Owner / 5.3 |
| Which systems affect customers, staff, or the public? | 4.2 subjects |
