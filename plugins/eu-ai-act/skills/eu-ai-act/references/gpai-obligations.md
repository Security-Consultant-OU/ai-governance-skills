# General-purpose AI model obligations (Chapter V)

## All GPAI models — Article 53 obligations

| Obligation | Article | What to implement | Evidence needed | Common gaps |
|------------|---------|-------------------|-----------------|-------------|
| Technical documentation | Art. 53(1)(a), Annex XI | Maintain and keep up to date technical documentation of the model including the training and testing process and the results of its evaluation, containing at minimum the information set out in Annex XI | Annex XI documentation: architecture, training methodology, data sources, compute used, evaluation results, known limitations | Documentation focuses on capabilities without disclosing limitations; training-data description insufficient; Annex XI sections incomplete |
| Information to downstream providers | Art. 53(1)(b) | Provide information and documentation to downstream AI system providers to enable their compliance with the AI Act | Downstream provider information package: capabilities, limitations, integration guidelines, known risks, appropriate use cases, instructions for compliance | Information is marketing-oriented rather than compliance-enabling; limitations and risks not adequately communicated |
| Copyright policy | Art. 53(1)(c) | Establish a policy to comply with Union copyright law, in particular to identify and comply with reservations of rights expressed pursuant to Article 4(3) of Directive (EU) 2019/790 (text and data mining opt-out) | Documented copyright compliance policy; opt-out mechanism; records of rights reservations identified and respected | No systematic process to identify opt-out signals; policy exists but is not operationalised |
| Training content summary | Art. 53(1)(d) | Draw up and make **publicly available** a sufficiently detailed summary of the content used for training the GPAI model, according to the template provided by the AI Office | Published training content summary per AI Office template | Summary too vague; does not follow the AI Office template; not publicly accessible; wrongly treated as OSS-exempt |

## Free and open-source GPAI models (Article 53(2))

| Aspect | Rule |
|--------|------|
| Definition | Released under a free and open-source licence that allows access, usage, modification, and distribution of the model, **and** whose parameters, including the weights, **the information on the model architecture**, and **the information on model usage**, are made publicly available |
| Art. 53(1)(a) technical documentation | **Dropped** by Art. 53(2) unless the model has systemic risk |
| Art. 53(1)(b) downstream provider information | **Dropped** by Art. 53(2) unless the model has systemic risk |
| Art. 53(1)(c) copyright policy | **Always applies** — not dropped |
| Art. 53(1)(d) training content summary | **Always applies** — not dropped |
| Art. 55 systemic-risk obligations | **Not exempt** — full compliance required; Art. 53(2) does not apply to GPAI models with systemic risk |

## Systemic risk determination and notification

| Criterion | Threshold | Detail |
|-----------|-----------|--------|
| Training compute | >10^25 FLOPs | GPAI models trained with a cumulative amount of computation greater than 10^25 floating point operations are presumed to have systemic risk (Art. 51) |
| Commission designation | Case-by-case | The Commission may designate a GPAI model as having systemic risk on the basis of the criteria in Annex XIII |
| Provider notification (Art. 52) | Mandatory | Providers shall notify the Commission **without delay and in any event within 2 weeks** after the requirement in Art. 51 is met or it becomes known that it will be met |

## Systemic risk GPAI models — Article 55 additional obligations

Article 55(1)(b) is **its own obligation**. It is not the same as adversarial testing / red-teaming under Art. 55(1)(a).

| Obligation | Article | What to implement | Evidence needed | Common gaps |
|------------|---------|-------------------|-----------------|-------------|
| Model evaluation, including adversarial testing | Art. 55(1)(a) | Perform model evaluation in accordance with standardised protocols and tools reflecting the state of the art, including conducting and documenting adversarial testing (red-teaming) to identify and mitigate systemic risks | Evaluation reports using standardised protocols; documented test methodologies; benchmark and safety-evaluation results; red-team reports | Evaluation limited to capability benchmarks; red-teaming superficial; systemic-risk scenarios (CBRN, cyber, loss of control) not tested |
| Assess and mitigate systemic risks at Union level | Art. 55(1)(b) | **Assess and mitigate possible systemic risks at Union level**, including their sources, that may stem from the development, placing on the market, or use of GPAI models with systemic risk | Union-level systemic-risk assessment; identified sources of risk; mitigation plan and residual-risk record | Collapsed into red-teaming; no Union-level (as opposed to model-lab) assessment; mitigations not documented |
| Serious incident tracking and reporting | Art. 55(1)(c) | Keep track of, document, and report, without undue delay, to the AI Office and, as appropriate, to national competent authorities, relevant information about serious incidents and possible corrective measures | Incident tracking system; incident reports; corrective-action documentation; reporting records | No formal incident tracking at model level; reporting threshold unclear |
| Cybersecurity protections | Art. 55(1)(d) | Ensure an adequate level of cybersecurity protection for the GPAI model with systemic risk and the physical infrastructure of the model | Cybersecurity assessment; protection-measures documentation; penetration testing; model-security measures (anti-extraction, anti-poisoning) | Cybersecurity focused on infrastructure only; model-specific threats not addressed |

## Codes of practice (Article 56)

| Aspect | Detail |
|--------|--------|
| Purpose | Enable GPAI model providers to demonstrate compliance with Chapter V obligations |
| Development | AI Office coordinates development; providers and other stakeholders participate |
| Compliance presumption | Adherence to a code of practice approved by the Commission creates a presumption of conformity with the corresponding obligations |
| Monitoring | AI Office and Board monitor and evaluate; codes must be updated based on new developments |
| Alternative | Providers may demonstrate compliance through alternative adequate means if they choose not to adhere to a code of practice |
