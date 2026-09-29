# 10-Design

Design stage for the query-violation experiment supporting pilot record
[TEVV-001](../../mappings/tevv-athlon/TEVV-001.toml).

This stage specifies what the experiment claims, tests, and assumes,
before any execution.
It does not run anything.
See `20-fixtures` and `30-execution`.

## Contents

- [`protocol.md`](./protocol.md) - purpose, method, and the constraints on
  how results may be interpreted.
- [`research-question.md`](./research-question.md) - the question this
  experiment narrows TEVV-001's own research question to, and the two
  candidate questions it asks.
- [`claims.md`](./claims.md) - the source's own evaluation question,
  distinguished from the two claims constructed for experimental analysis,
  and why each construction is or isn't source-motivated.
- [`evaluator-contexts.md`](./evaluator-contexts.md) - what the source
  states about evaluator conditions for this example, what it leaves
  unstated, and what the experiment itself does and does not model.
- [`evidence-requirements.md`](./evidence-requirements.md) - what evidence
  the source describes as collected, and what each candidate claim would
  need beyond that to be resolved.

## Reading Order

`protocol.md` first, for the constraints everything else operates under.
`research-question.md` and `claims.md` can be read in either order;
`evaluator-contexts.md` and `evidence-requirements.md` both depend on the
claims `claims.md` defines.

## Status

The initial design and finite-model experiment are documented.

Both candidate constructions produce reproducible, conditional
non-resolution results under their stated modeling assumptions.

Further work will refine the observation model to represent sampled
prompts, responses, human annotations, and evidence collected through
both User Testing and Red Teaming.

The TEVV-001 research record remains `OPEN`.
