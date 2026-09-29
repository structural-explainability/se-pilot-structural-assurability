# NIST Assurance

This page maps Structural Assurability concepts to selected NIST assurance
terminology.

It does **not** claim that NIST adopts Structural Assurability or that the two
frameworks are equivalent.

## Claim-Relative Assurance

NIST assurance terminology describes assurance in terms of justified
confidence concerning specified claims.

NIST also describes assurance techniques and methods as generating credible
evidence used to substantiate claims.

This is compatible with the claim-relative starting point of Structural
Assurability:

```text
system S
claim C
evaluator conditions K
resource bounds B
```

Structural Assurability then asks what claim-material evidentiary capabilities
are available under those conditions.

## Assurance Evidence

NIST uses assurance evidence as information on which assurance,
trustworthiness, and risk decisions can be based.

Structural Assurability does not redefine that concept.

Instead, it separates several structural questions that precede use of
evidence in an assurance argument:

```text
Does the evidence exist?
        ↓
Can this evaluator access it?
        ↓
Can it be obtained within available resources?
        ↓
Is it material to this claim?
        ↓
What evidentiary capability does it enable?
```

## Assessment Context

NIST assessment guidance recognizes that evidence may come from different
sources and may be obtained through different assessment activities.

Structural Assurability provides a formal way to represent constraints on
that acquisition through evaluator conditions and resource bounds.

The mapping is conceptual rather than one-to-one.

## Structural Assurability Source of Truth

```text
SE/StructuralAssurability/Layer10_Foundation/Evaluator.lean
SE/StructuralAssurability/Layer10_Foundation/Context.lean
SE/StructuralAssurability/Layer20_Semantics/Accessibility.lean
SE/StructuralAssurability/Layer20_Semantics/Resources.lean
SE/StructuralAssurability/Layer20_Semantics/Materiality.lean
SE/StructuralAssurability/Layer30_Core/Assurability.lean
```

## External Source of Truth

Relevant NIST sources include:

- NIST CSRC Glossary: Assurance
- NIST CSRC Glossary: Assurance Case
- NIST CSRC Glossary: Assurance Evidence
- NIST SP 800-160 Volume 1 Revision 1
- NIST SP 800-171A Revision 3

NIST publications remain authoritative for NIST terminology and requirements.
