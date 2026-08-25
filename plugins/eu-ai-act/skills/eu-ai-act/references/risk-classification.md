# EU AI Act risk classification

Classification is **non-exclusive**. Complete Article 5, then Article 6(1), then Annex III / Article 6(2), then the Article 6(3) derogation, then **independently** Article 50. Article 50 is **additive**. Emotion recognition and biometric categorisation are **never** an exclusive “limited risk” tier.

## Prohibited AI practices (Article 5)

| Category | Description | Exceptions |
|----------|-------------|------------|
| Subliminal, manipulative or deceptive techniques (Art. 5(1)(a)) | Placing on the market, putting into service or use of an AI system that deploys subliminal techniques beyond a person's consciousness **or purposefully manipulative or deceptive techniques**, with the objective or the effect of materially distorting behaviour, causing or reasonably likely to cause significant harm | None |
| Exploitation of vulnerabilities (Art. 5(1)(b)) | AI systems that exploit vulnerabilities of persons due to age, disability, or a specific social or economic situation to materially distort behaviour, causing or reasonably likely to cause significant harm | None |
| Social scoring (Art. 5(1)(c)) | AI systems that evaluate or classify persons based on social behaviour or personal or personality characteristics, leading to detrimental or unfavourable treatment unrelated to the context in which the data was generated or that is unjustified or disproportionate | None |
| Predictive policing (individual) (Art. 5(1)(d)) | AI systems that assess or predict the risk of a natural person committing a criminal offence, based solely on profiling or on personality traits and characteristics | Permitted when used to support the human assessment of the involvement of a person in a criminal activity, based on objective and verifiable facts directly linked to a criminal activity |
| Untargeted facial recognition scraping (Art. 5(1)(e)) | AI systems that create or expand facial recognition databases through untargeted scraping of facial images from the internet or CCTV footage | None |
| Emotion recognition in workplace/education (Art. 5(1)(f)) | AI systems that infer emotions of a natural person in the areas of workplace and education institutions | Permitted where the use is intended to be put in place or into the market for medical or safety reasons |
| Biometric categorisation of sensitive attributes (Art. 5(1)(g)) | AI systems that categorise individually natural persons based on their biometric data to deduce or infer race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation | Labelling or filtering of lawfully acquired biometric datasets, and law enforcement |
| Real-time remote biometric identification in publicly accessible spaces for law enforcement (Art. 5(1)(h)) | Real-time remote biometric identification of natural persons in publicly accessible spaces for the purposes of law enforcement | Permitted only for: (a) targeted search for specific victims of abduction, trafficking or sexual exploitation, or missing persons; (b) prevention of a specific, substantial and imminent threat to life or of a terrorist attack; (c) localisation or identification of a person suspected of a serious criminal offence. Requires prior authorisation except in duly justified urgency |

Emotion recognition **outside** workplace and education is **not** an Article 5 prohibition. It is Annex III point 1(c) high-risk **and** Article 50(3) deployer notice (additive). Do not classify it as limited-risk only.

## High-risk — Article 6(1) Annex I product-law path

An AI system is high-risk where **both** of the following are fulfilled:

| Condition | Rule |
|-----------|------|
| (a) | The AI system is intended to be used as a **safety component** of a product, or the AI system is itself a product, covered by Union harmonisation legislation listed in **Annex I** |
| (b) | The product whose safety component is the AI system, or the AI system itself as a product, is required to undergo a **third-party conformity assessment** for the purpose of placing it on the market or putting it into service pursuant to that Annex I legislation |

## High-risk AI systems (Annex III) — Article 6(2)

Article 6(2): AI systems referred to in Annex III **shall be considered to be high-risk**. Point 1 includes identification **and** categorisation **and** emotion recognition.

| Area | Category | Specific use cases |
|------|----------|-------------------|
| 1 | Biometrics | (a) Remote biometric identification (where permitted); (b) biometric categorisation according to sensitive or protected attributes or characteristics based on the inference of those attributes or characteristics; (c) emotion recognition systems |
| 2 | Critical infrastructure | AI used as safety components in the management and operation of critical digital infrastructure, road traffic, or the supply of water, gas, heating or electricity |
| 3 | Education and vocational training | AI determining access to or admission to educational and vocational training institutions; evaluating learning outcomes; assessing the appropriate level of education; monitoring and detecting prohibited behaviour during tests |
| 4 | Employment and worker management | AI for recruitment or selection (advertising, analysing/filtering applications, evaluating candidates); decisions affecting terms of work, promotion or termination; task allocation based on behaviour or personal traits; monitoring and evaluating performance and behaviour of workers |
| 5 | Access to essential private and public services | (a) Eligibility for essential public assistance benefits and services; **(b) creditworthiness of natural persons or credit score, with the exception of AI systems used for the purpose of detecting financial fraud**; (c) risk assessment and pricing in life and health insurance; (d) evaluation and classification of emergency calls; dispatching or prioritisation of emergency first-response services |
| 6 | Law enforcement | Polygraphs and similar tools; risk assessment of a natural person as regards offending or re-offending (where not prohibited); evaluation of the reliability of evidence; profiling in the course of detection, investigation or prosecution; crime analytics of large datasets |
| 7 | Migration, asylum, and border control | Polygraphs and similar tools; risk assessment of irregular migration; examination of asylum, visa or residence-permit applications and related complaints; detection, recognition or identification of natural persons (except travel-document authenticity checks) |
| 8 | Administration of justice and democratic processes | AI assisting judicial authorities in researching and interpreting facts and the law and in applying the law to a concrete set of facts; AI intended to influence the outcome of an election or referendum or the voting behaviour of natural persons (excluding systems used to organise, optimise or structure political campaigns that are not directly targeting voters) |

## Article 6 numbering and Art. 6(3) derogation (verbatim)

**Art. 6(2)** means Annex III systems **are** high-risk. **Art. 6(3)** is the derogation. Do not treat Art. 6(2) as the exception clause.

An Annex III AI system is not high-risk only if **both** are met: (1) it does not pose a significant risk of harm to the health, safety or fundamental rights of natural persons, including by not materially influencing the outcome of decision making; **and** (2) at least one of (a)–(d) is fulfilled.

| Point | Condition |
|-------|-----------|
| (a) | Intended to perform a narrow procedural task |
| (b) | Intended to improve the result of a previously completed human activity |
| (c) | Intended to detect decision-making patterns or deviations from prior decision-making patterns and is not meant to replace or influence the previously completed human assessment, without proper human review |
| (d) | Intended to perform a preparatory task to an assessment relevant for the purposes of the use cases listed in Annex III |

Profiling of natural persons: the system always remains high-risk (Art. 6(3) last subparagraph). There is no standalone exception for “not the sole or primary decision basis.”

Art. 6(4): the provider shall document the not-high-risk assessment before placing on the market or putting into service, is subject to registration under Art. 49(2), and shall submit the documentation to national competent authorities upon request.

## Article 50 — Transparency obligations (additive)

Article 50 has applied since **2 August 2026** and is **in force**. It is **not** an exclusive residual tier. Apply it independently after Articles 5 and 6.

| Provision | Who | Obligation | Exceptions |
|-----------|-----|------------|------------|
| Art. 50(1) | Providers | AI systems intended to interact directly with natural persons: inform those persons that they are interacting with an AI system, unless this is obvious from the point of view of a reasonably well-informed, observant and circumspect person | Systems authorised by law to detect, prevent, investigate or prosecute criminal offences (unless made available for the public to report a criminal offence) |
| Art. 50(2) | Providers, including GPAI systems | Synthetic **audio, image, video or text** outputs marked in a **machine-readable** format and detectable as artificially generated or manipulated; technical solutions effective, interoperable, robust and reliable as far as technically feasible | Assistive function for standard editing that does not substantially alter the input data provided by the deployer; functionality limited to detecting, preventing, investigating or prosecuting criminal offences |
| Art. 50(3) | Deployers | **Emotion recognition** or **biometric categorisation**: inform natural persons exposed of the operation of the system; process personal data in accordance with GDPR, Regulation (EU) 2018/1725 or the Law Enforcement Directive, as applicable | Systems used for biometric categorisation and emotion recognition which are permitted by law to detect, prevent or investigate criminal offences |
| Art. 50(4) first subparagraph | Deployers | Image, audio or video content constituting a deep fake: disclose that the content has been artificially generated or manipulated | Use authorised by law to detect, prevent, investigate or prosecute a criminal offence; where the content forms part of an evidently artistic, creative, satirical or fictional analogous work or programme, disclosure in an appropriate manner that does not hamper the display or enjoyment of the work |
| Art. 50(4) second subparagraph | Deployers | AI-generated or manipulated **text** published with the purpose of informing the public on **matters of public interest**: disclose that the text has been artificially generated or manipulated | Use authorised by law to detect, prevent, investigate or prosecute criminal offences; **or** the AI-generated content has undergone a process of **human review or editorial control** and a natural or legal person holds **editorial responsibility** for the publication |

Emotion recognition that is not prohibited under Art. 5(1)(f) is **Annex III point 1(c) high-risk and Art. 50(3)**. Biometric categorisation that is not prohibited under Art. 5(1)(g) is **Annex III point 1(b) high-risk and Art. 50(3)**. Neither is limited-risk only.

## Residual systems

| Aspect | Detail |
|--------|--------|
| Obligations | No specific mandatory product requirements under the EU AI Act beyond any applicable Art. 50 duties |
| Encouraged measures | Voluntary codes of conduct (Art. 95) covering transparency, human oversight, sustainability, accessibility, stakeholder participation, diversity of development teams |
| Examples (only if Arts. 5, 6 and 50 do not apply) | AI-enabled video games, spam filters, inventory management systems |
