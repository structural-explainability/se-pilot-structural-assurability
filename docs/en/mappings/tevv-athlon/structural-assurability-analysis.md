# TEVV-Athlon: Structural Assurability Analysis

## Authority

The Lean repository is authoritative for formal definitions and theorems.
See: [Formal Theory: Structural Assurability](https://github.com/structural-explainability/se-theory-structural-assurability)

## Applied So Far

The resolution bound.
If two admissible worlds are indistinguishable under an observation model
and disagree on a claim, the model does not resolve the claim.

In Lean this is `not_claimResolvedBy_of_witness` in `Layer30_Core/Bounds.lean`.
The experiment script checks the same condition on finite models.

## Not Yet Applied

- Comparison of evaluator contexts by capability sets.
- Evaluator conditions and resource bounds.
- The candidate structural dimensions.

## More

See: [TEVV-001](TEVV-001.toml)
See: [Evaluator conditions](../../experiment/10-design/evaluator-contexts.md)
