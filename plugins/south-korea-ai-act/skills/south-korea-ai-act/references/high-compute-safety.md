# Art. 32 high-compute safety

Art. 32 is a **separate gate** from high-impact AI (Art. 2(4)). A system can be in-scope for Art. 32 without being high-impact, and high-impact without meeting Art. 32.

## In-scope test (all three limbs)

| Limb | Article / instrument | Threshold | Fail |
|------|----------------------|-----------|------|
| Compute | Art. 32 + Enforcement Decree No. 36053 | Training compute **≥ 10^26 FLOPs** | Below 10^26 FLOPs |
| SOTA | Art. 32 + decree | Model is **state of the art** | Not SOTA |
| Rights risk | Art. 32 + decree | **Broad fundamental-rights risk** | Narrow or no such risk at scale |

If any limb fails, Art. 32 safety submission does **not** apply. Do not treat 10^26 FLOPs alone as enough.

## Duties when in scope

| Duty | Article | What “done” looks like |
|------|---------|------------------------|
| Safety measures for the high-compute model | Art. 32 | Identified rights/safety risks, tests, mitigations, residual risk |
| Submit **results** to MSIT | Art. 32 | Results of the safety work are filed with MSIT |
| Keep compute and SOTA evidence | Art. 32 + decree | FLOPs methodology, training run record, SOTA rationale |
| Re-assess on a new training run that may cross the gate | Art. 32 + decree | New run ≥ 10^26 FLOPs re-opens the test |

## Mapping (do not copy EU Chapter V wholesale)

| Korea | Article | Closest analogue | Difference |
|-------|---------|------------------|------------|
| Compute + SOTA + broad rights-risk gate | Art. 32 | EU GPAI **compute gate** | Korea adds SOTA and broad rights-risk limbs; threshold is **10^26 FLOPs** |
| Results to MSIT | Art. 32 | EU GPAI documentation / systemic-risk duties to the AI Office | Different addressee, content, and extra Korea limbs |
| High-impact operator measures | Art. 34 | EU high-risk operator duties | Independent of Art. 32 |
| High-impact classification | Art. 2(4) | EU “high-risk” (mapping synonym only) | Independent of Art. 32 |

## Who is responsible

| Operator | Article | Art. 32 role |
|----------|---------|--------------|
| Development operator | Art. 2(7)(a), Art. 32 | Usually holds compute/SOTA facts and performs safety work |
| Use/service operator | Art. 2(7)(b), Art. 32 | In scope if it is the operator of the Art. 32 system |
| Foreign operator | Art. 32, Art. 36 | Same gate if Korea-facing; representative does not replace the MSIT results duty |
| Public institution | Art. 32, Art. 30(4) | Same gate if it is the operator |

## Checklist

| Item | Article | Status |
|------|---------|--------|
| FLOPs measured against ≥ 10^26 | Art. 32, decree | 🔴🟡🟢 |
| SOTA determination documented | Art. 32, decree | 🔴🟡🟢 |
| Broad fundamental-rights risk documented | Art. 32, decree | 🔴🟡🟢 |
| Safety measures implemented (if all limbs met) | Art. 32 | 🔴🟡🟢 |
| Results submitted to MSIT (if all limbs met) | Art. 32 | 🔴🟡🟢 |
| Out-of-scope rationale recorded (if any limb fails) | Art. 32 | 🔴🟡🟢 |
