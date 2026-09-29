# AISI-001: From Proxy Evaluation to Safety Claim

## Identity

- Record ID: `AISI-001`
- Status: `OPEN`
- Framework: UK AI Security Institute safety-case research
- Focus: Cyber-inability arguments and proxy evaluations

## Source

- Publisher: UK AI Security Institute
- Document: Safety case template for frontier AI:
  A cyber inability argument
- Published: December 2024
- Source: https://www.aisi.gov.uk/research/safety-case-template-for-frontier-ai-a-cyber-inability-argument-2

Companion explanation:

https://www.aisi.gov.uk/blog/safety-case-template-for-inability-arguments

Reviewed material:

- Published abstract.
- Companion explanation of the argument structure.
- Previously developed Structural Assurability crosswalk.

Pending:

- Detailed examination of the complete research paper.
- Identification of exact passages governing each
  proposed evidentiary relationship.

## Source Structure

The template develops a structured inability argument
using Claims, Arguments, Evidence.

Its described elements include:

- An overall safety claim.
- More specific subclaims.
- Risk models.
- Proxy tasks derived from those risk models.
- Evaluation settings.
- Evaluation results.
- Arguments concerning evaluation sufficiency.

The accompanying explanation identifies concerns
including inadequate capability elicitation.

These are source-described components of the
safety-case approach.

## Evaluative Claim

The template considers an argument that an AI system
lacks capabilities sufficient to pose unacceptable
offensive cyber risk.

The pilot does not adopt that claim for any particular
AI system.

## Required Distinctions

The investigation must identify which alternatives
the relevant evidence is intended to distinguish.

For example, a constructed model might distinguish
between systems that produce the same proxy-task
results but differ in their capabilities in a
specified risk context.

Whether those alternatives are admissible under
the template's assumptions must be established
before treating them as a counterexample.

## Evidence

Source-described evidence includes:

- Risk models.
- Proxy-task selection and justification.
- Evaluation settings.
- Results from capability evaluations.
- Evidence supporting the adequacy of evaluation.

To be established for a concrete application:

- Which observations are available.
- Which observations are material to each subclaim.
- Which relevant capabilities may remain unobserved.
- What additional evidence supports the argument
  connecting proxy tasks to risk models.

## Evaluator Conditions

The investigation must establish:

- Who conducts the evaluation.
- Who constructs and reviews the safety case.
- Access to the evaluated system.
- Control over evaluation settings.
- Resources needed to conduct the evaluation.
- Relevant cooperation and trust assumptions.

These conditions must not be inferred merely from
the presence of evaluation results.

## Assumptions

The source describes the need to justify proxy-task
selection and evaluation sufficiency.

The investigation must distinguish:

- Assumptions governing observation and access.
- Assumptions about elicitation and measurement.
- Assumptions connecting proxy-task performance
  to risk-relevant capabilities.
- Assumptions connecting capability evidence
  to the overall safety argument.

Not all these relationships are formalized by
Structural Assurability.

## Structural Assurability Mapping

Potentially applicable concepts include:

- Claim-relative evidence.
- Evaluator conditions.
- Evidentiary capabilities.
- Observational indistinguishability.
- Claim-resolution bounds.
- Evidence independence and integrity.

Structural Assurability can investigate whether
specified observations distinguish alternatives
material to an evaluative claim.

It does not independently establish that a proxy
task is an adequate measure of a real-world
capability or that the resulting safety argument
is justified.

Those inferential relationships require separate
argumentation and supporting evidence.

## Research Question

Which parts of a cyber-inability safety-case argument
concern the structural availability of claim-material
evidence, and which require additional assumptions
connecting proxy evaluations to broader claims
about capabilities and risk?

## Evidence and Analysis

Completed:

- Initial conceptual crosswalk.
- Identification of the source's argument structure.
- Identification of potentially relevant formal concepts.

Pending:

- Select a specific risk model and associated proxy task.
- Identify the applicable subclaim.
- Establish the evaluation setting and observations.
- Examine the source's justification for the
  proxy-task and evaluation relationships.
- Specify relevant alternative worlds and assumptions.
- Determine which limitations can be expressed
  by the current Structural Assurability theory.
- Record which obligations remain outside that theory.

A possible indistinguishability example must not
ignore assumptions or supporting evidence already
provided by the source.

## Outcome

Status: `OPEN`

The investigation may identify an applicable structural
limitation, clarify the theory's boundary with assurance
argumentation, or produce no additional finding.

## Related Material

- [Recovered AISI crosswalk](../uk-aisi-safety-cases.md)
- [Pilot specification](../SPECIFICATION.md)
