# EU AI Act output templates

Copy-ready shells. Replace every `[bracket]` with facts from the user or from lookup in this skill's reference files. Do not invent article, annex, or control IDs.

Status values: 🔴 not started — no evidence of implementation. 🟡 partial — some implementation, gaps remain. 🟢 implemented — fully met with documented evidence.

## Gap-assessment row

Use one row per article (or article cluster). Repeat the row for every duty in scope for that role.

| Article | Requirement | Status 🔴🟡🟢 | Evidence | Gap |
|---------|-------------|---------------|----------|-----|
| [Art. X / Arts. X–Y] | [Short duty title] | [🔴 Not started / 🟡 Partial / 🟢 Implemented] | [Named document, control, or “none”] | [Missing control or “none — maintain”] |

Example filled row (illustrative, not a legal finding):

| Article | Requirement | Status 🔴🟡🟢 | Evidence | Gap |
|---------|-------------|---------------|----------|-----|
| Art. 9 | Risk management system | 🟡 Partial | [Risk register v0.3] | [No foreseeable-misuse testing; no residual-risk record] |

## FRIA — Article 27(1)(a)–(f) + MSA notification

Complete the **gate** first. If the gate is no, stop after the gate row; do not draft (a)–(f).

| Field | Fill-in |
|-------|---------|
| System | [Name / version / intended purpose] |
| Annex III point (if Art. 6(2)) | [Point number and short description, or “not Annex III”] |
| Gate — body governed by public law? | [Yes / No] — [entity name] |
| Gate — private entity providing public services? | [Yes / No] — [service] |
| Gate — Annex III 5(b) credit scoring deployer? | [Yes / No] |
| Gate — Annex III 5(c) life/health insurance deployer? | [Yes / No] |
| Gate — Annex III point 2 (critical infrastructure) exclusion? | [Yes → FRIA not triggered / No] |
| **FRIA required?** | **[Yes / FRIA not triggered]** — [cite the matching gate limb] |

If **FRIA required**, fill:

| Art. 27(1) | Required content | Fill-in |
|------------|------------------|---------|
| (a) | Deployer's processes in which the system will be used, in line with intended purpose | [Process names; how the system is used in those processes] |
| (b) | Period of time and **frequency** of intended use | [Start–end or ongoing; [n] times per [day/week/month/decision]] |
| (c) | Categories of natural persons and groups likely to be affected | [Categories / groups] |
| (d) | Specific risks of harm to fundamental rights of those persons or groups | [Rights at risk; harm scenarios; provider Art. 13 information used] |
| (e) | Implementation of human oversight measures, according to the instructions for use | [Oversight roles; intervene/override; training] |
| (f) | Measures if those risks materialise, including internal governance and complaint mechanisms | [Incident path; complaints channel; governance owner] |

| MSA notification (Art. 27(3)) | Fill-in |
|-------------------------------|---------|
| Market surveillance authority | [Member State MSA name] |
| What is notified | **Results** of this FRIA |
| Vehicle | Filled-out **Commission template** (Art. 27(5)) — not a generic filing, licence, or CE dossier |
| DPIA conjunction (Art. 27(4)) | [No DPIA / GDPR Art. 35 / LED Art. 27] — [elements reused / elements still unique to FRIA, including (b) period/frequency] |

## GPAI obligation row

Use one row per obligation. Include Art. 53(1)(a)–(d) for every GPAI model. Add Art. 55(1)(a)–(d) only if systemic risk (Art. 51/52). Record OSS drops only for 53(1)(a)–(b) when Art. 53(2) applies and the model is **not** systemic-risk.

| Obligation | Article | Status 🔴🟡🟢 | Evidence | Notes |
|------------|---------|---------------|----------|-------|
| [Duty title] | [Art. 53(1)(a) / (b) / (c) / (d) / Art. 55(1)(a) / (b) / (c) / (d) / Art. 52] | [🔴 Not started / 🟡 Partial / 🟢 Implemented / N/A — OSS drop / N/A — not systemic-risk] | [Named artefact or “none”] | [OSS drop? Union-level vs red-teaming? 2-week notification?] |

Seed rows to copy:

| Obligation | Article | Status 🔴🟡🟢 | Evidence | Notes |
|------------|---------|---------------|----------|-------|
| Technical documentation | Art. 53(1)(a) | [status] | [Annex XI docs or “none”] | [N/A — OSS drop only if Art. 53(2) and not systemic-risk] |
| Downstream-provider information | Art. 53(1)(b) | [status] | [Downstream pack or “none”] | [N/A — OSS drop only if Art. 53(2) and not systemic-risk] |
| Copyright policy | Art. 53(1)(c) | [status] | [Policy / TDM opt-out process] | Always applies, including OSS |
| Training-content summary | Art. 53(1)(d) | [status] | [Public summary per AI Office template] | Always applies, including OSS |
| Commission notification | Art. 52 | [status or N/A] | [Notification record] | Without delay and in any event within 2 weeks if Art. 51 met |
| Model evaluation including adversarial testing | Art. 55(1)(a) | [status or N/A] | [Eval / red-team reports] | Systemic-risk only |
| Assess and mitigate systemic risks at Union level | Art. 55(1)(b) | [status or N/A] | [Union-level assessment] | **Not** the same as red-teaming |
| Serious-incident tracking and reporting | Art. 55(1)(c) | [status or N/A] | [Incident log / reports] | Systemic-risk only |
| Cybersecurity | Art. 55(1)(d) | [status or N/A] | [Model + infrastructure protections] | Systemic-risk only |

## Classification result recipe

Output **is** these sections **in this order**. Complete every section. Article 50 is additive — fill section 5 even when section 1 or 2–4 already found a prohibition or EU high-risk duty. Emotion recognition and biometric categorisation are never an exclusive “limited risk” tier.

### (1) Art. 5

| Field | Fill-in |
|-------|---------|
| Prohibited practice examined | [Art. 5(1)(a)–(h) points checked] |
| Result | [Prohibited / Not prohibited] |
| Exception used (if any) | [None / medical or safety (Art. 5(1)(f)) / other cited exception] |
| Effect | [Must not be placed on the market, put into service, or used / continue to (2)] |

### (2) Art. 6(1)

| Field | Fill-in |
|-------|---------|
| Annex I Union harmonisation legislation | [Named act / none] |
| Safety component of a product, or itself a product? | [Yes — role / No] |
| Third-party conformity assessment already required under that legislation? | [Yes / No] |
| Result | [EU high-risk under Art. 6(1) / Not Art. 6(1)] |

### (3) Annex III / Art. 6(2)

| Field | Fill-in |
|-------|---------|
| Annex III point | [Point and sub-point, e.g. 1(c) / 4 / none] |
| Result | [EU high-risk under Art. 6(2) / Not Annex III] |

### (4) Art. 6(3)

| Field | Fill-in |
|-------|---------|
| Applies? | [Only if (3) is EU high-risk] |
| Limb 1 — no significant risk of harm, including by not materially influencing decision-making? | [Yes / No — facts] |
| Limb 2 — which of (a)–(d)? | [(a) narrow procedural / (b) improve prior human activity / (c) pattern-detection without replacing human assessment / (d) preparatory / none] |
| Profiles natural persons? | [Yes → remains EU high-risk / No] |
| Result | [Derogation applies — not high-risk for Chapter III Section 2; document under Art. 6(4) and Art. 49(2) / Derogation does not apply / N/A] |

### (5) Art. 50 independently

| Field | Fill-in |
|-------|---------|
| Art. 50(1) chatbot / direct interaction | [Applies / Does not apply] — [obviousness / LE exception] |
| Art. 50(2) machine-readable marking of synthetic audio/image/video/text | [Applies / Does not apply] — [assistive-edit / LE exception] |
| Art. 50(3) emotion recognition or biometric categorisation deployer notice | [Applies / Does not apply] — [LE exception] |
| Art. 50(4) deepfake and/or public-interest AI text | [Applies / Does not apply] — [art-satire / editorial / LE exception] |
| Additive statement | Art. 50 duties apply **in addition to** any Art. 5 or Art. 6 result above |

### (6) Residual

| Field | Fill-in |
|-------|---------|
| Residual? | [Yes — Art. 95 voluntary codes only, plus any Art. 50 duties in (5) / No — prohibited and/or EU high-risk duties apply] |
| Next artefact | [Gap table / Art. 43 path / FRIA gate / Annex IV / none] |
