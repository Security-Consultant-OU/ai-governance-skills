# Operator obligations — Arts. 2(7), 30(4), 31–36, 43

Roles are **AI development business operator** and **AI use/service business operator** (Art. 2(7)). The **user** (Art. 2(8)) is the person provided with the product — a rights-holder, not a third obligated column.

Legend: **Yes** = duty applies to that operator type when the trigger is met. **If HI** = only if the system is high-impact (고영향 AI, Art. 2(4)). **If gen** = generative. **If foreign+threshold** = Art. 36. **Endeavor** = Art. 35 (not a pre-market gate). **Prefer** = Art. 35(2). **—** = not that operator’s statutory column.

## Core obligations by operator type

| Obligation | Development operator (Art. 2(7)(a)) | Use/service operator (Art. 2(7)(b)) | Foreign operator | Public institution | Article | Trigger |
|------------|-------------------------------------|-------------------------------------|------------------|--------------------|---------|---------|
| High-impact classification record | Yes | Yes | Yes (if Korean nexus) | Yes | Art. 2(4), Art. 33 optional | Any in-scope system |
| Prior notice that the product/service uses AI | Yes (enable/issue in the product) | Yes (issue to persons provided with the service) | Yes (if Korean nexus) | Yes | Art. 31(1), Art. 43 | High-impact **or** generative only — not all AI |
| Label generative outputs | Yes | Yes | Yes | Yes | Art. 31(2) | Generative outputs |
| Extra notice for synthetic audio/image/video hard to distinguish from real | Yes | Yes | Yes | Yes | Art. 31(3) | Hard-to-distinguish synthetic A/V/I; artistic/creative exception |
| High-impact risk management | If HI | If HI | If HI | If HI | Art. 34 | High-impact |
| Explainability measures (results, main criteria, training-data overview) | If HI | If HI | If HI | If HI | Art. 34(1)2 | High-impact — operator measures, not a GDPR appeal clock |
| User protection | If HI | If HI | If HI | If HI | Art. 34 | High-impact |
| Human oversight | If HI | If HI | If HI | If HI | Art. 34 | High-impact |
| Documentation of Art. 34 measures | If HI | If HI | If HI | If HI | Art. 34 | High-impact |
| Impact assessment | Endeavor | Endeavor | Endeavor | **Prefer** products that have undergone assessment | Art. 35, Art. 35(2) | Not a mandatory pre-market gate; no MSIT approval of every AIA |
| Extra public-institution duties | — | — | — | Yes | Art. 30(4) | Public institutions |
| Domestic representative | — | — | If foreign+threshold | — | Art. 36, Art. 43 | Decree thresholds or corrective-order fine |
| High-compute safety measures and results to MSIT | If Art. 32 in-scope | If Art. 32 in-scope | If Art. 32 in-scope | If Art. 32 in-scope | Art. 32 | ≥ 10^26 FLOPs **and** SOTA **and** broad fundamental-rights risk |
| General MSIT incident reporting for all high-impact systems | — | — | — | — | — | **Not** an Art. 34 duty |
| AI ethics as a catch-all private mandate | — | — | — | — | Art. 27 | Government **promotion**, not a private-enforcement clause |
| Explanation as an individual timed right | — | — | — | — | Art. 3(2) | **Principle** (technically/reasonably possible), not an appeal SLA |

## Art. 34 high-impact measures (detail)

| Measure | Article | What “implemented” looks like | Common miss |
|---------|---------|-------------------------------|-------------|
| Risk management | Art. 34 | Identified life/safety/rights risks, treatments, residual risk, owner | EU Art. 9 template copied without Korea domain facts |
| Explainability | Art. 34(1)2 | Can explain **results**, **main criteria**, and **training-data overview** | Promising a 30-day individual GDPR-style appeal |
| User protection | Art. 34 | Protections for persons provided with the product (Art. 2(8) users) | Treating “user” as a third obligated operator |
| Human oversight | Art. 34 | Humans can monitor, intervene, and own the decision where required | HITL theatre (click-through accept) |
| Documentation | Art. 34 | Written measures, versions, and who is accountable | Wiki notes with no operator attribution |

Development operators typically design these measures into the system. Use/service operators operate them in the service. An entity that both develops and provides the service must satisfy **both** Art. 2(7) columns.

## Art. 31 vs Art. 34 vs Art. 35 (do not merge)

| Topic | Article | Legal character |
|-------|---------|-----------------|
| Prior AI-use notice | Art. 31(1) | Binding when high-impact **or** generative; Art. 43 fine |
| Generative output labels / synthetic-media notice | Art. 31(2)–(3) | Binding for generative / hard-to-distinguish synthetic A/V/I |
| High-impact operator measures | Art. 34 | Binding for high-impact operators |
| Impact assessment | Art. 35 | **Shall endeavor**; public bodies **prefer** assessed products (Art. 35(2)) |

## Status template

| Obligation | Article | Applies? | Status | Evidence | Gap notes | Priority |
|-----------|---------|----------|--------|----------|-----------|----------|
| Classification record | Art. 2(4) | Yes/No | 🔴🟡🟢 | | | Critical |
| Art. 31(1) prior notice | Art. 31(1) | HI or gen? | 🔴🟡🟢 | | | Critical |
| Art. 31(2) generative labels | Art. 31(2) | Gen? | 🔴🟡🟢 | | | High |
| Art. 31(3) synthetic A/V/I notice | Art. 31(3) | Hard-to-distinguish? | 🔴🟡🟢 | | | High |
| Art. 34 risk management | Art. 34 | HI? | 🔴🟡🟢 | | | Critical |
| Art. 34(1)2 explainability | Art. 34(1)2 | HI? | 🔴🟡🟢 | | | Critical |
| Art. 34 user protection | Art. 34 | HI? | 🔴🟡🟢 | | | High |
| Art. 34 human oversight | Art. 34 | HI? | 🔴🟡🟢 | | | High |
| Art. 34 documentation | Art. 34 | HI? | 🔴🟡🟢 | | | High |
| Art. 35 endeavor AISIA | Art. 35 | Endeavor | 🔴🟡🟢 | | | Medium |
| Art. 35(2) public preference | Art. 35(2) | Public buyer? | 🔴🟡🟢 | | | Medium |
| Art. 30(4) public duties | Art. 30(4) | Public institution? | 🔴🟡🟢 | | | High |
| Art. 36 representative | Art. 36 | Foreign+threshold? | 🔴🟡🟢 | | | Critical |
| Art. 32 safety + MSIT results | Art. 32 | Compute gate? | 🔴🟡🟢 | | | High |
