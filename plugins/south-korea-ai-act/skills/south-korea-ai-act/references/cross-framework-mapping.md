# Cross-framework mapping — in-force Korea AI Basic Act

Korea **high-impact AI (고영향 AI)** is not EU **high-risk AI**. Use “high-risk” only as a mapping synonym.

## Requirement-level mapping

| Korea requirement | Article | EU AI Act | ISO/IEC 42001 | NIST AI RMF | Brazil AI Act | NYC LL144 |
|-------------------|---------|-----------|---------------|-------------|---------------|-----------|
| High-impact classification (listed domain **and** significant effect on life/safety/rights; HITL exclusion) | Art. 2(4), decree, Art. 33 optional | Art. 6 + Annex III **high-risk** (synonym only — tests differ) | A.5 impact informs design; does not classify 고영향 | MAP 1, MAP 2 | High-risk / excessive-risk tiers | AEDT definition (hiring overlap only) |
| High-impact operator measures (risk management, explainability, user protection, human oversight, documentation) | Art. 34, Art. 34(1)2 | Arts. 9–15 high-risk duties (different list; **no** general Korea MSIT incident-reporting duty for all high-impact systems) | **A.6** life cycle | MAP / MEASURE / MANAGE | Governance duties for high-risk | Bias-audit methodology ≠ Art. 34 |
| Transparency — prior AI-use notice | Art. 31(1) | Art. 50 (limited-risk transparency) — Korea applies **only** to high-impact **or** generative | A.6.2.7 / transparency documentation | GOVERN 1.2 | Information rights | 10-business-day AEDT notice (hiring only) |
| Generative labels / hard-to-distinguish synthetic A/V/I | Art. 31(2)–(3) | Art. 50(2) and 50(4) (deep fake / AI interaction) | Transparency documentation | GOVERN 1.2 | Generative transparency | No equivalent |
| Explanation principle vs measures | Art. 3(2) principle; Art. 34(1)2 measures | Art. 86 explanation (high-risk individual decisions) | A.5 / A.6 documentation | GOVERN 1.2 | Right to explanation | No individual explanation right |
| Endeavor impact assessment | Art. 35; public **prefer** Art. 35(2) | Art. 27 FRIA (deployer; mandatory where triggered) | **A.5** AISIA (mandatory **inside** an AIMS) | MAP 5 | Algorithmic impact assessment | Annual bias audit ≠ AISIA |
| High-compute safety; results to MSIT | Art. 32 (≥ 10^26 FLOPs **and** SOTA **and** broad rights risk) | GPAI **compute gate** / systemic-risk duties (different threshold and limbs) | A.6 life-cycle evidence for frontier models | GOVERN / MAP at organisational scale | Foundation-model rules if any | No equivalent |
| Domestic representative | Art. 36 | Authorised representative | **A.10** suppliers/customers | GOVERN 6 | Local representative if any | No equivalent |
| Ethics promotion | Art. 27 | Art. 5 prohibitions (different legal tool) | Policy / A.8 | GOVERN values | Principles | Fairness via audit only |
| Administrative fines | Art. 43 (≤ KRW 30 million) | Up to 7% global turnover or EUR 35 million | Loss of certification | None (voluntary) | Pending / statute-specific | Up to $1,500 per violation per day |
| Public-institution extra duties | Art. 30(4), Art. 35(2) | Public-sector high-risk + FRIA | A.5 + A.10 if procuring | GOVERN | Public-sector duties | NYC agencies as employers only |

## Structural differences

| Dimension | Korea AI Basic Act | EU AI Act | ISO/IEC 42001 | NIST AI RMF | Brazil AI Act | NYC LL144 |
|-----------|-------------------|-----------|---------------|-------------|---------------|-----------|
| Force | Binding; in force 22 Jan 2026 (Act No. 20676 / 21311; Decree No. 36053) | Binding EU regulation; **phased application** | Certifiable standard | Voluntary | National statute (jurisdiction-specific) | Binding NYC law |
| Key class | **High-impact (고영향 AI)** | High-risk (+ prohibited / GPAI / limited) | Organisation-defined impact (A.5) | Contextual profile | Tiered risk | AEDT only |
| Roles | Development operator / use-service operator (Art. 2(7)); user is rights-holder (Art. 2(8)); foreign + representative (Art. 36); public (Art. 30(4)) | Provider / deployer / importer / distributor / authorised representative | Provider and user (AIMS roles) | Any organisation | Statute-specific | Employer / vendor |
| Compute gate | Art. 32: 10^26 FLOPs + SOTA + broad rights risk; results to MSIT | GPAI compute / systemic-risk gate | No statutory FLOPs gate | No statutory FLOPs gate | If any, different | None |
| Impact assessment | Art. 35 **endeavor**; Art. 35(2) public **preference** | FRIA where triggered | A.5 mandatory in AIMS | MAP 5 | Often mandatory for high-risk | Bias audit |
| Enforcement posture | MSIT grace through at least Jan 2027 for most investigations/fines **except serious harm** | Dated phase-in | Certification bodies | None | Authority-specific | NYC DCWP |
| Fine scale | Art. 43 ≤ KRW 30 million | 7% / EUR 35 million | N/A | N/A | Statute-specific | Per-day civil penalty |

## Gaps when mapping from another framework

| Gap | Detail | Articles |
|-----|--------|----------|
| High-impact ≠ high-risk | Annex III systems are not automatically 고영향 AI; Korea needs domain **and** significance, then the HITL exclusion | Art. 2(4), decree |
| Art. 31 is narrower than Art. 50 folklore | Prior notice is **high-impact or generative**, not all AI | Art. 31(1) |
| Art. 35 is weaker than FRIA / ISO AISIA | Endeavor + public preference — not a launch licence | Art. 35, Art. 35(2) |
| No general high-impact incident report to MSIT | Do not import EU Art. 73-style reporting as an Art. 34 duty | Art. 34 |
| Art. 32 is not full GPAI Chapter V | Extra SOTA and rights-risk limbs; 10^26 FLOPs; results to MSIT | Art. 32 |
| Art. 36 thresholds are Korea-specific | KRW 1T total **or** KRW 10B AI **or** 1M daily Korean users **or** corrective-order fine | Art. 36, decree |
| Fine scale | KRW 30 million vs EU turnover percentages | Art. 43 |
| Grace ≠ delayed applicability | Duties apply from 22 Jan 2026; most fines restrained until at least Jan 2027 except serious harm | Act + MSIT grace |
| User is not a deployer | Art. 2(8) user is the person provided with the product | Art. 2(7), Art. 2(8) |
| Art. 27 is not a private hook | Government promotion of ethics | Art. 27 |
| Art. 3(2) is not Art. 86 | Principle vs high-impact explanation **measures** | Art. 3(2), Art. 34(1)2 |
| ISO IDs | Map impact → **A.5**, life cycle → **A.6**, representative/suppliers → **A.10** — do not invent A.5.8 or A.10 decommission | A.5, A.6, A.10 |
