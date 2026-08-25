# Korea AI Basic Act — worked examples

Facts below are illustrations. Classification still follows Art. 2(4), Decree No. 36053, and optional Art. 33. Statutory class is **high-impact (고영향 AI)**.

## 1 — HITL exclusion (human final decision + controllable → not high-impact)

**User asks:** Clinical diagnostic AI proposes findings; a licensed clinician must accept or reject before any treatment change. Is this high-impact AI?

**Skill does:** Domain → significance → HITL exclusion.

| Step | Finding |
|------|---------|
| Domain (Art. 2(4)) | Healthcare / medical devices — used in diagnosis affecting care |
| Significance (Art. 2(4)) | Yes — life and physical safety |
| Human final decision (Decree No. 36053) | Yes — named clinician, documented authority |
| Controllable | Yes — reject/override is used in practice, not a courtesy click |
| Art. 33 | Optional if the hospital wants MSIT confirmation; not a licence |
| Art. 31 generative? | No (unless the product is also generative) |
| Art. 32? | No, unless the three Art. 32 limbs are met |

**Artefact Z — classification**

```
CLASSIFICATION (Art. 2(4) + Decree No. 36053)
System: clinical diagnostic support, version …
Operator type (Art. 2(7)): development and/or use-service (hospital)
Domain: healthcare / medical devices
Significance: Yes — life/safety
HITL exclusion: Applies — clinician final decision, deemed controllable
RESULT: Not high-impact
Art. 33: Not needed (or Seek if status is contested)
Also check: Art. 31 generative? No. Art. 32 high-compute? No.
Evidence to keep: role mandate; reject/override log; why residual risk is controllable
```

If the same model auto-writes orders that staff cannot reject, HITL exclusion fails and the result is **high-impact**.

## 2 — Generative labelling only (not high-impact; Art. 31 still applies)

**User asks:** Marketing image generator for Korea-facing ads. Not used in a listed domain. What notices and labels are required?

**Skill does:** Confirm not 고영향 AI. Apply Art. 31 because the system is **generative**, not because it is high-impact. Skip Art. 34.

| Topic | Article | Applies? |
|-------|---------|----------|
| Listed domain + significance | Art. 2(4) | No — marketing images, no listed-domain use |
| HITL | Decree No. 36053 | n/a |
| Result | Art. 2(4) | **Not high-impact** |
| Prior notice that the service uses AI | Art. 31(1) | **Yes — generative** |
| Label generative outputs | Art. 31(2) | **Yes** |
| Extra notice for hard-to-distinguish audio/image/video | Art. 31(3) | **Yes** if photorealistic ads could be taken as real; artistic/creative exception if that use is documented |
| High-impact operator measures | Art. 34 | **No** |
| Art. 35 endeavor AISIA | Art. 35 | Endeavor remains available; not a launch condition |
| Fine for missing Art. 31 notice | Art. 43 | Up to KRW 30 million |

**Artefact Z — Art. 31 checklist**

```
Art. 31(1) prior notice (generative): 🔴🟡🟢 — shown before first use, Korean for Korea-facing users
Art. 31(2) generative output labels: 🔴🟡🟢
Art. 31(3) hard-to-distinguish image notice / artistic exception file: 🔴🟡🟢
Art. 34: not applicable (not high-impact)
```

## 3 — Art. 36 foreign operator (revenue / 1 million daily users / corrective-order fine)

**User asks:** A US AI use/service operator provides a chatbot to persons in Korea. Average daily Korean users = 1.2 million. AI-related revenue = KRW 8 billion. Total revenue below KRW 1 trillion. No corrective-order fine. Need a domestic representative?

**Skill does:** Nexus, then **any** Art. 36 + Decree No. 36053 limb.

| Limb | Figure | Threshold | Met? |
|------|--------|-----------|------|
| Korean nexus | Yes — provided in/into Korea | Required | Yes |
| Total revenue | Below KRW 1 trillion | ≥ KRW 1 trillion | No |
| AI-related revenue | KRW 8 billion | ≥ KRW 10 billion | No |
| Average daily Korean users | 1.2 million | ≥ **1 million** | **Yes** |
| Corrective-order fine | None | Any such fine | No |

**Artefact Z — Art. 36**

```
ART. 36 DOMESTIC REPRESENTATIVE
Korean nexus: Yes
Limbs met: 1M daily users
IN SCOPE: Yes
Action: designate representative (name, Korean address, contact, mandate)
Art. 31 notices remain with the operator
Art. 43 if missing: up to KRW 30 million
```

Other in-scope paths with the same recipe: total revenue ≥ KRW 1 trillion; AI-related revenue ≥ KRW 10 billion; **or** the operator was fined for violating a corrective order — each alone is enough.

## 4 — Art. 35 endeavor for public sales (Art. 35(2) preference, not a licence)

**User asks:** We sell a hiring ranker to a Korean public institution. Must we obtain MSIT impact-assessment approval before the sale?

**Skill does:** Classify (hiring + significance, then HITL). Produce an **Art. 35 endeavor AISIA**. Treat Art. 35(2) as procurement **preference**, not a licence.

| Topic | Article | Reading |
|-------|---------|---------|
| Hiring ranker that determines hire / no-hire | Art. 2(4) | High-impact unless HITL exclusion applies |
| Art. 34 measures | Art. 34, Art. 34(1)2 | Binding if high-impact |
| Impact assessment | Art. 35 | Operator **shall endeavor** — not a statutory launch condition |
| Public buyer | Art. 35(2) | Public institution **prefers** products that have undergone assessment |
| MSIT approval of every AIA | — | **None** |
| Optional status confirmation | Art. 33 | Separate from Art. 35; optional |

**Artefact Z — labelled endeavor assessment (excerpt)**

```
ART. 35 ENDEAVOR AISIA (Art. 35 endeavor impact assessment)
Not a pre-market gate. MSIT does not approve this document. Art. 35(2) is preference, not a licence.

High-impact (Art. 2(4)): Yes (unless HITL exclusion documented)
Public-institution use (Art. 35(2)): Yes — preference only
Measures: Art. 34 risk management, Art. 34(1)2 explainability, user protection, human oversight, documentation
Conclusion: completed endeavor file supports Art. 35(2) preference; not an MSIT licence
```

Do not block the sale pending an invented MSIT AIA certificate. If the buyer is public, a completed endeavor file is the Art. 35(2) differentiator.
