# AI Assurance Research Mapping

## Research Documents

- [Source register](sources.md): reference list,
  links, and items for source-level review.

## Conceptual Crosswalks

These documents map selected external assurance
concepts to Structural Assurability.
They are conceptual crosswalks.

- [NIST Assurance](nist-assurance.md): claim-relative assurance,
  assurance evidence, assessment context, evaluator access,
  and resource constraints.
- [NIST TEVV-Athlon](nist-tevv-athlon.md): evaluation claims,
  required evidentiary distinctions, evaluator conditions,
  obtainable evidence, and claim-resolution limits.
- [EU AI Act](eu-ai-act.md): technical documentation, evaluator
  access, conformity-assessment evidence, and the separation
  between structural evidence conditions and legal compliance.
- [UK AISI Safety Cases](uk-aisi-safety-cases.md): structured
  safety-case arguments, evidence obtainability, independent
  evidence, and candidate structural properties.
- [Assurance Cases](assurance-cases.md): relationships among
  claims, arguments, evidence, assumptions, and the structural
  conditions under which evidence can be obtained.

Each crosswalk identifies relevant Lean source files and
distinguishes Structural Assurability's formal concepts from
the terminology and authority of external sources.

## Initial External-Framework Study

- [TEVV-Athlon study](tevv-athlon/index.md): the NIST-specific
  research application, incorporating the recovered conceptual
  crosswalk, source review, and candidate questions.

[NIST TEVV-Athlon crosswalk](nist-tevv-athlon.md)
is an input to this study,
not a substitute for reviewing the
external source documents.

flowchart TB
    subgraph NIST["NIST TEVV-Athlon"]
        direction TB
        N1["Measurement concepts (Blocks)"]
        N2["Assessment activities (Events and Tools)"]
        N3["Measurements and observations"]
        N4{"Do the observations distinguish<br/>claim-relevant alternatives?"}
        N5["Evaluative claim"]
        N1 --> N2 --> N3 --> N4 --> N5
    end

    subgraph AISI["UK AISI cyber-inability safety case"]
        direction TB
        A1["Safety claim and subclaims"]
        A2["Risk models"]
        A3["Proxy tasks and evaluation settings"]
        A4["Evaluation results"]
        A5{"Are the evidence and inferential<br/>assumptions adequate for the claim?"}
        A1 --> A2 --> A3 --> A4 --> A5
    end

    N4 -. "Structural Assurability analysis" .-> S["Observations, evaluator conditions,<br/>trust assumptions and claim-resolution limits"]
    A5 -. "Structural Assurability analysis" .-> S

## Research Discipline

The mapping starts with an assurance claim, identifies what could
be observed or measured, records the necessary access and trust
assumptions, and distinguishes the observation from the inference
made from it.

It does not infer from a sensor's existence that a claim is
resolvable.

The recovered conceptual crosswalks provide starting points for
source-grounded investigation.

The [pilot specification](SPECIFICATION.md) governs future
mapping records.

Formal definitions and proofs are owned by
[Formal Theory: Structural Assurability](https://github.com/structural-explainability/se-theory-structural-assurability).
