# Research Question

## Primary Research Question

Under what conditions can evidence produced by a specified AI evaluation
distinguish the alternatives material to its evaluative claim?

The investigation examines whether claim-relative Structural Assurability
can identify the information available to an evaluator, the distinctions
that information supports, and the additional assumptions or evidence
needed when a claim remains unresolved.

## Initial Investigation: TEVV-001

The initial investigation examines the query-violation example in
Section 3 of NIST AI 200-2 ipd, *The TEVV-Athlon Framework for
Evaluating AI Systems*.

The example assesses chatbot performance across three low-impact
operational environments:

- TV Shows.
- Meal Planning.
- Travel Planning.

NIST describes two measurement Blocks:

- Helpfulness.
- Violation Frequency.

User Testing produces evidence for both Blocks.
Red Teaming produces additional evidence for Violation Frequency.

The assessment collects questionnaire responses and annotated chatbot
interactions,
then uses descriptive statistics to characterize the
observed results.

## Research Questions

The investigation considers four related questions.

1. Which claims about chatbot behavior can be resolved by the evidence
   available under a specified assessment and evaluator context?

2. Can two admissible worlds produce identical observations under
   the assessment while differing on a claim material to the evaluation?

3. What assumptions connect the observed samples to behavior across
   other queries, testing conditions, or operational environments?

4. What additional evidence or evaluator capabilities would be
   required to resolve a claim that the existing observations
   leave undetermined?

These questions concern the relationship between evaluative claims,
evidence, and admissible alternatives.

## Initial Finite-Model Experiment

The initial experiment is implemented in:
`experiments/tevv-athlon/query_violation.py`.

It examines two conditional questions:

- Whether observations covering three tested scenarios resolve a
  researcher-defined claim extending to a fourth, untested scenario.
- Whether Red Teaming alone resolves a claim about organic-use safety
  when organic and adversarial behavior may vary independently.

The experiment constructs indistinguishable, claim-disagreeing world
pairs under explicitly stated assumptions.

These constructions illustrate possible claim-resolution limitations.
They do not establish that the constructed worlds are realizable
in operational AI systems.

## Next Investigation

The next experiment will refine the observation model to distinguish
underlying system behavior from evidence actually collected through
an evaluation.

It will consider:

- Sampled prompts and their selection.
- Chatbot responses to those prompts.
- Human annotations of observed responses.
- Evidence collected through both User Testing and Red Teaming.
- Evaluator access and relevant measurement assumptions.

The investigation will determine whether indistinguishable,
claim-disagreeing alternatives remain under this more detailed model.

It will also examine the measurement-validation and generalization
considerations discussed in Sections 4.5 and 4.6 of the NIST draft.

## Research Boundary

NIST's example is a measurement exercise.
It does not assert the binary safety claims
introduced in the pilot's initial experiment.

The pilot must distinguish:

- The source's evaluation question.
- Claims introduced by the researcher.
- Results established within specified mathematical models.
- Evidence needed to justify applying those models to real systems.

## References

- NIST AI 200-2 ipd, *The TEVV-Athlon Framework for Evaluating AI Systems*:
  https://doi.org/10.6028/NIST.AI.200-2.ipd
- Pilot record: `docs/en/mappings/tevv-athlon/TEVV-001.toml`
