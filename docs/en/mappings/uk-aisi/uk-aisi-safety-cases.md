# UK AISI Safety Cases

This page is an explanatory crosswalk between Structural Assurability and
safety-case work published by the UK AI Security Institute.

It does not claim that AISI adopts Structural Assurability.

## Safety-Case Structure

AISI safety-case work uses structured, evidence-based arguments to support
safety claims.

Its published cyber inability template uses a
Claims-Arguments-Evidence structure and connects:

- top-level claims
- subclaims
- risk models
- proxy tasks
- evaluation settings
- evaluation results

Structural Assurability addresses a complementary question:

> Does the evaluated system and its evidence environment make the evidence
> required by such an argument obtainable under the evaluator's actual
> conditions?

## Structural Crosswalk

The relationship can be represented as:

```text
safety claim
     ↓
subclaims and required distinctions
     ↓
evaluation design
     ↓
required evidence
     ↓
structural obtainability of that evidence
     ↓
evaluation results
     ↓
safety-case argument
```

Structural Assurability concerns the structural obtainability and capability
portion of this sequence.

It does not establish the safety claim.

## Independent Evidence

The formal theory distinguishes structural properties such as:

- observability
- traceability
- reconstructability
- independence
- integrity
- evidence coverage

These properties can matter differently depending on the safety claim.

For example, detailed internal traces and independently generated external
evidence may enable different assurance-relevant capabilities.

Neither is automatically superior for every claim.

## Structural Assurability Source of Truth

```text
SE/StructuralAssurability/Layer30_Core/Capability.lean
SE/StructuralAssurability/Layer30_Core/Assurability.lean
SE/StructuralAssurability/Layer40_Order/Incomparability.lean
SE/StructuralAssurability/Layer50_Properties/Independence.lean
SE/StructuralAssurability/Layer50_Properties/Integrity.lean
SE/StructuralAssurability/Layer50_Properties/EvidenceCoverage.lean
SE/StructuralAssurability/Layer90_Examples/Case3_Incomparability.lean
```

## External Source of Truth

Relevant AISI sources include:

- Safety case template for frontier AI: A cyber inability argument
- AISI Safety Cases research collection

AISI publications remain authoritative for AISI safety-case methods.
