# Governance requirements — Senate-approved PL 2338/2023 (not enacted)

**Label:** based on Senate-approved PL 2338/2023; not enacted.

Senate text does **not** fix a 5-year log-retention period or a 72-hour incident clock.

---

## Art. 17 — All agentes de IA

Guarantee system security and rights of affected persons, **nos termos de regulamento**.

---

## Art. 18 — High-risk governance (split by role)

Applies to desenvolvedor and aplicador when introducing or placing a **high-risk** system on the market, according to state of the art and **reasonable efforts**.

| Agent | Inciso | Proposed measures |
|-------|--------|-------------------|
| Aplicador | I(a)–(f) | Lifecycle documentation; tools/processes to assess accuracy, robustness, illicit/abusive discrimination and mitigations; reliability/safety tests; document degree of **human supervision** that contributed to results; bias mitigation when risk arises from **application**; information enabling interpretation of results (trade secrets reserved) |
| Desenvolvedor | II(a)–(f) | Record of governance measures to inform the aplicador (Art. 18 I); operational logging for accuracy/robustness; safety tests; technical measures so results are applicable and interpretable; bias mitigation when risk arises from application; transparency on social/sustainable governance policies |

| Paragraph | Rule |
|-----------|------|
| §1 | Sectoral authorities may **flex or waive** regulated obligations by value-chain context |
| §2 | **Distribuidores** support and **verify** that governance measures are met **before** the system is placed on the market |
| §3 | Value-chain agents cooperate: necessary information, technical access, reasonably expected assistance (trade secrets reserved) |
| §4 | Measures match the **lifecycle phase** the agent actually owns |
| §5 | If aplicador or distribuidor makes a **substantial modification** or changes **purpose**, that agent is treated as **desenvolvedor** |

Art. 16 §3 repeats distributor pre-market verification.

Art. 21: high-risk agents must keep systems aligned with all Chapter IV governance measures and sectoral law.

---

## Arts. 25–28 — Avaliação de impacto algorítmico (AIA)

| Article | Proposed rule |
|---------|----------------|
| Art. 25 caput | Obligation of the **desenvolvedor or aplicador** who introduces or places the system on the market, whenever the system **or its use** is high-risk, considering the agent’s role in the chain |
| Art. 25 §1 | High-risk desenvolvedor shares preliminary assessments and AIA with the **sectoral authority**; methodology records risks/benefits to fundamental rights, mitigations, and effectiveness |
| Art. 25 §3 | Performed **before** the specific context of market introduction |
| Art. 25 §4 | Sectoral authority may **flex** AIA by role; general norms from autoridade competente |
| Art. 25 §5–§6 | Competent authority (Cria guidelines) sets general AIA elements and update cadence; sectoral authority regulates criteria and periodicity |
| Art. 25 §7 | After market/use, unexpected **relevant** risk to natural persons’ rights → communicate **immediately** to sectoral authority and other chain agents; notify affected persons when necessary |
| Art. 25 §8 | Public participation hypotheses set by competent + sectoral authorities |
| Art. 26 | AIA **before** market introduction **and** continuous/iterative over the high-risk lifecycle; update at least on **significant changes** |
| Art. 27 | May be performed **together with** an LGPD RIPD/DPIA |
| Art. 28 | **Conclusions** of the AIA are public, trade secrets reserved, **nos termos de regulamento** |

### Publication — who publishes what

| Article | Who | What | Not |
|--------|-----|------|-----|
| Art. 44 | Autoridade competente + sectoral authorities | Public **database** of high-risk AI containing **public** AIA documents (LGPD + LAI; trade secrets) | Not a duty on private agents to post the full AIA on their own site |
| Art. 23 III | **Public administration** (and Art. 23 §3 public-service contractors) | Publish **preliminary assessments** of high-risk AI they develop, implement, or use | Not a general private-sector publish-your-AIA duty |
| Art. 28 | Via regulation / Art. 44 database | Public **conclusions** | Not an open-ended self-publication mandate |

---

## Arts. 22–24 — Public administration (proposed)

| Article | Proposed duty |
|---------|----------------|
| Art. 22 I–II | When developing, contracting, or adopting high-risk AI: access to databases and **portability** of citizens’ and public-management data under **LGPD**; minimum data-architecture/metadata standards for interoperability |
| Art. 23 I | Access/use protocols logging who used the system, for which case, and for what purpose |
| Art. 23 II | Facilitated explanation and human review of decisions with relevant legal effects |
| Art. 23 III | Publication of preliminary assessments (see above) |
| Art. 23 §1 | Public biometric identification: AIA first |
| Art. 23 §2 | If AIA risks cannot be eliminated or substantially mitigated → **discontinue** use |
| Art. 24 | Federal Executive sets minimum transparency standards for federal public-sector AI |

---

## Art. 42 — Serious incidents (not 72 hours to ANPD)

| Aspect | Senate text |
|--------|-------------|
| Who reports | Agente de IA |
| To whom | **Autoridade setorial** (not ANPD as default clock) |
| Deadline | **Prazo a ser estabelecido** (Art. 42 caput and §1). Communication is due **after** the sectoral authority defines prazo and gravity criteria |
| What | Grave security incident, including risk to life/physical integrity; interruption of critical infrastructure operations; serious property or environmental damage; serious violations of fundamental rights, information integrity, freedom of expression, or the democratic process |
| Follow-up | Sectoral authority may order measures to reverse or mitigate (Art. 42 §2) |
| Other law | Art. 43: cybersecurity, critical-infrastructure, and related legislation remain applicable |
| Distinct duty | Art. 25 §7 unexpected relevant rights impact → **immediate** notice to sectoral authority and chain (not a 72-hour ANPD rule) |

Do **not** import LGPD’s 72-hour personal-data breach clock as an AI-bill deadline.

---

## Record-keeping — no 5-year default

| What | Senate hook | Retention |
|------|-------------|-----------|
| Art. 18 logging / tests / human-supervision documentation | Art. 18 I–II | **Not specified.** Await regulation; do not invent 5 years |
| AIA versions | Arts. 25–26 | Lifecycle + significant-change updates; no fixed statutory years |
| Incident files | Art. 42 | Per forthcoming sectoral rules |
| Rights-exercise records | Arts. 9–10; LGPD if personal data | LGPD rules where personal data apply |

---

## Sandbox (proposed)

| Article | Note |
|---------|------|
| Art. 4 XVIII | Definition of ambiente regulatório experimental |
| Art. 46 parágrafo único | Sectoral sandboxes: autoridade competente is notified and may opine |
| Art. 50 IV | Sanction: ban from sandbox for up to 5 years |

---

## Design checklist (preparedness)

- [ ] Roles mapped as desenvolvedor / distribuidor / aplicador (Art. 4)
- [ ] Art. 18 split implemented or planned for high-risk
- [ ] Distributor pre-market verification (Art. 18 §2 / Art. 16 §3)
- [ ] Substantial-modification trigger (Art. 18 §5)
- [ ] AIA process for high-risk (Arts. 25–27); LGPD RIPD combined where needed
- [ ] Sectoral-authority incident path (Art. 42) — prazo TBD
- [ ] No reliance on invented 72-hour / 5-year figures
