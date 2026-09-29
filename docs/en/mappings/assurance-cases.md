# Assurance Cases

This page is an explanatory crosswalk between Structural Assurability and
assurance-case reasoning.
Assurance cases are not part of the formal theory.

## Assurance-Case View

An assurance case organizes:

- claims
- supporting arguments
- evidence
- relevant assumptions

The argument explains why the available evidence supports the stated claim.

## Structural Assurability View

Structural Assurability asks an earlier structural question:

> Can the specified evaluator obtain evidence capable of making the
> distinctions required to evaluate this claim under the stated conditions?

The relationship can be summarized as:

```text
assurance claim
      ↓
required evidentiary distinctions
      ↓
evidence structurally obtainable?
      ↓
claim-material evidentiary capabilities
      ↓
assurance argument using that evidence
```

Structural Assurability addresses the middle portion of this sequence.
It does **not** determine whether an assurance argument succeeds.

## The Distinction

An assurance argument can identify evidence that would support a claim without
establishing that a particular evaluator can actually obtain that evidence.

Access restrictions, resource constraints, missing instrumentation,
insufficient coverage, weak provenance, or lack of independent evidence may
limit what can practically be established.

Structural Assurability makes those conditions explicit.

## Structural Assurability Source of Truth

Formal definitions and results are authoritative in:

```text
SE/StructuralAssurability/Layer10_Foundation/Context.lean
SE/StructuralAssurability/Layer20_Semantics/Accessibility.lean
SE/StructuralAssurability/Layer20_Semantics/Resources.lean
SE/StructuralAssurability/Layer20_Semantics/Materiality.lean
SE/StructuralAssurability/Layer30_Core/Capability.lean
SE/StructuralAssurability/Layer30_Core/Assurability.lean
```

## External Source of Truth

For assurance-case terminology, consult the applicable assurance framework.

The NIST CSRC Glossary and NIST publications define assurance cases using
claims, structured argumentation, evidence, and explicit assumptions.

Those external sources remain authoritative for NIST terminology.
