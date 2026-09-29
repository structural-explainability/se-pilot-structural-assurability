# NIST TEVV-Athlon

This page is a conceptual mapping between Structural Assurability and the
NIST TEVV-Athlon framework for evaluating AI systems.

It does not claim that TEVV-Athlon adopts Structural Assurability.

## Evaluation Question

A TEVV activity can produce meaningful results only for distinctions that its
evaluation design and available evidence can support.

Structural Assurability makes that dependency explicit.

A useful crosswalk is:

```text
intended evaluative claim
        ↓
distinctions required to evaluate the claim
        ↓
evidence required to make those distinctions
        ↓
evidence obtainable under actual evaluator conditions
        ↓
feasible TEVV activities
        ↓
conclusions bounded by the resulting evidence
```

## Evaluator Conditions

Structural Assurability represents evaluator conditions separately from the
system itself.

These conditions can include:

- knowledge
- access
- trust
- cooperation

Resource constraints are modeled separately.

This makes it possible to distinguish:

```text
evidence that could exist in principle
```

from:

```text
evidence this evaluator can practically obtain
```

That distinction can matter when evaluation requires privileged access,
instrumentation, logs, internal artifacts, controlled interventions, or
cooperation from a system provider.

## Claim Resolution

Structural Assurability also provides a bound on what an evaluation can
resolve.

If two admissible possibilities differ on the truth of the claim but produce
the same available observation, the observation cannot resolve the claim.

The implication for evaluation is straightforward:

```text
evaluation cannot distinguish
claim-relevant alternatives
→
evaluation cannot establish which alternative holds
```

This is a structural limitation on the available evidence, not a judgment
about the quality of the evaluator.

## Structural Assurability Source of Truth

```text
SE/StructuralAssurability/Layer10_Foundation/Evaluator.lean
SE/StructuralAssurability/Layer10_Foundation/Context.lean
SE/StructuralAssurability/Layer20_Semantics/Observation.lean
SE/StructuralAssurability/Layer20_Semantics/Accessibility.lean
SE/StructuralAssurability/Layer20_Semantics/Resources.lean
SE/StructuralAssurability/Layer20_Semantics/Indistinguishability.lean
SE/StructuralAssurability/Layer30_Core/Bounds.lean
SE/StructuralAssurability/Layer30_Core/Assurability.lean
```

## External Source of Truth

The authoritative external source is NIST AI 200-2,
The TEVV-Athlon Framework for Evaluating AI Systems.

NIST documentation remains authoritative for TEVV-Athlon.
