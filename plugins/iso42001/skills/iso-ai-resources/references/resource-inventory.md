# ISO/IEC 42001 AI resource inventory

Annex A.4 selectable controls: **A.4.2, A.4.3, A.4.4, A.4.5, A.4.6**. AIMS support: Clause **7.1**. A.4.1 is the objective, not a control.

If document type is omitted, fill the per-system pack, then 7.1.

---

## A.4.2 — Resource documentation header

| Field | Value |
|-------|-------|
| System ID | |
| System name | |
| Life-cycle stages covered | |
| Last reconstructed / reviewed | |
| Owner | |

After an incident, this pack plus logs (A.6.2.8) should be enough to say what the system depended on. If not, A.4.2 is 🔴.

---

## A.4.3 — Data resources

Pointer rows. Full A.7 fields live in the data-for-AI inventory.

| Dataset ID | Category | Purpose | Retention | Inventory complete (y/n) |
|------------|----------|---------|-----------|--------------------------|
| | train / validate / test / production | | | |

---

## A.4.4 — Tooling resources

| Name | Type (model / framework / library / eval / provisioning) | Version / hash | Source (internal / vendor / hub) | Owner |
|------|----------------------------------------------------------|----------------|----------------------------------|-------|
| | | | | |

Unmanaged hubs without a row fail A.4.4.

---

## A.4.5 — System and computing resources

| Resource | Provider / region | Capacity constraint | Environmental impact noted (y/n) | Owner |
|----------|-------------------|---------------------|----------------------------------|-------|
| Compute | | | | |
| Storage | | | | |
| Network | | | | |
| Hosting | | | | |

Cloud invoice without AI-specific capacity or energy is 🟡, not 🟢.

---

## A.4.6 — Human resources

| Name or role seat | Life-cycle stage | Technical competence | Oversight / domain role | Named individual (y/n) |
|-------------------|------------------|----------------------|-------------------------|------------------------|
| | develop / operate / test / oversee / retire | | | |

Competence **only** for developers fails A.4.6. Deeper 7.2 matrix is `iso42001`.

---

## Clause 7.1 — AIMS resources

| Need | Allocated (y/n) | Evidence | Gap |
|------|-----------------|----------|-----|
| AIMS operation (not only go-live project) | | | |
| External expertise (legal / ethical / domain) | | | |
| Monitoring / evaluation tooling | | | |
| Training budget for AI competence | | | |

---

## Completeness (🔴🟡🟢)

| Control | Status | Gap |
|---------|--------|-----|
| A.4.2 | | |
| A.4.3 | | |
| A.4.4 | | |
| A.4.5 | | |
| A.4.6 | | |
| 7.1 | | |
