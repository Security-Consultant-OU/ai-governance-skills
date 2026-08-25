# Generative AI Profile — NIST AI 600-1 (July 2024)

Cross-sector profile of AI RMF 1.0 for generative AI (GAI). Voluntary. **Do not invent new Core IDs.** Map GAI risks to existing GOVERN/MAP/MEASURE/MANAGE subcategories, then apply 600-1 suggested actions (Action IDs such as GV-1.1-001) from the Profile — quote the Profile or say the action is not stored here.

Use this file when MAP-2.1 identifies generative tasks (foundation models, chat, image/audio/video generation, code generation, RAG).

---

## 12 GAI risk categories (NIST AI 600-1 §2)

| Risk | What NIST describes | Typical Core anchors |
|------|---------------------|----------------------|
| CBRN information or capabilities | Eased access to or synthesis of nefarious information or design capabilities related to chemical, biological, radiological, or nuclear weapons or other dangerous materials | MAP-5, ME-2.6, ME-2.7, MG-1 |
| Confabulation | Confidently stated but erroneous or false content (“hallucinations” / “fabrications”) that can mislead | ME-2.5, ME-2.9, MG-2.4 |
| Dangerous, violent, or hateful content | Eased production of violent, inciting, radicalizing, or threatening content; self-harm or illegal-activity recommendations; hateful/stereotyping exposure | ME-2.6, ME-2.8, MG-4.3 |
| Data privacy | Leakage, unauthorized use, disclosure, or de-anonymization of personal or sensitive data | ME-2.10, GV-6, MAP-4 |
| Environmental impacts | Energy, water, and related impacts of training and operating GAI | ME-2.12, MAP-3.2 |
| Harmful bias or homogenization | Amplified bias, performance disparities, and output homogeneity that can harm decisions or culture | ME-2.11, MAP-5, GV-3 |
| Human-AI configuration | Automation bias, over-reliance, anthropomorphism, algorithmic aversion, emotional entanglement | MAP-2.2, MAP-3.5, GV-3.2 |
| Information integrity | Lowered barriers to mis/disinformation and content that hides uncertainty or origin | ME-2.8, MAP-5, MG-4.3 |
| Information security | Offensive cyber capability; attacks on data, code, systems, or weights | ME-2.7, GV-6, MG-3 |
| Intellectual property | Unauthorized reproduction, trade-secret exposure, plagiarism, and related rights issues | GV-6.1, MAP-4.1 |
| Obscene, degrading, and/or abusive content | Abusive imagery, synthetic CSAM, non-consensual intimate imagery | ME-2.6, MG-1.1, MG-2.4 |
| Value chain and component integration | Opaque third-party components, weak supplier vetting, untraceable upstream data or software | GV-6, MAP-4, MG-3.1, MG-3.2 |

---

## Workflow add-on (generative systems)

1. Confirm GAI (MAP-2.1).
2. Score which of the 12 risks are plausible in this context (MAP-5.1).
3. Measure with the matching MEASURE 2 rows (especially ME-2.5–2.12).
4. Treat via MANAGE; for third-party models use MG-3.2.
5. If the user asks for Playbook or 600-1 Action IDs, retrieve them from NIST documents rather than fabricating `GV-1.1-001` style rows.
