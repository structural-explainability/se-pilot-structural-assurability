# EU AI Act

This page identifies structural concepts in the EU AI Act that can be examined
using Structural Assurability.

It is **not** legal advice.
It does **not** interpret compliance requirements or claim that Structural
Assurability is required by the EU AI Act.

## Evidence and Evaluator Access

The EU AI Act includes conformity-assessment mechanisms involving technical
documentation, evidence, testing, and access by notified bodies.

Annex VII provides examples including:

- examination of technical documentation
- access to relevant training, validation, and testing data
- technical means for access where appropriate
- requests for additional evidence
- requests for additional testing
- direct testing by the notified body where appropriate
- access to trained models and relevant parameters under specified conditions

These provisions illustrate why evaluator access is structurally relevant to
assurance.

## Structural Assurability View

Structural Assurability separates:

```text
system
claim
evaluator conditions
resource bounds
```

Evaluator conditions include access and cooperation.
The theory can represent a difference between:

```text
evidence present within the provider environment
```

and:

```text
evidence obtainable by the evaluating body
under the applicable access conditions
```

Those may be different evidence sets.

## No Compliance Inference

Structural Assurability does **not** determine whether:

- an AI system falls within a particular legal category
- a conformity-assessment procedure applies
- documentation satisfies a legal requirement
- access provided to an evaluator is legally sufficient
- a provider complies with the EU AI Act

Those are legal and regulatory questions **outside** the formal theory.

The theory can help describe the structural **evidence conditions** under
which particular evaluative distinctions are or are not possible.

## Structural Assurability Source of Truth

```text
SE/StructuralAssurability/Layer10_Foundation/Evaluator.lean
SE/StructuralAssurability/Layer10_Foundation/Context.lean
SE/StructuralAssurability/Layer20_Semantics/Accessibility.lean
SE/StructuralAssurability/Layer20_Semantics/Resources.lean
SE/StructuralAssurability/Layer60_Theorems/AccessExpansion.lean
SE/StructuralAssurability/Layer60_Theorems/ResourceExpansion.lean
```

## External Source of Truth

The authoritative legal source is Regulation (EU) 2024/1689,
including Annex VII and the applicable Articles.

The official text of the Regulation remains authoritative.
