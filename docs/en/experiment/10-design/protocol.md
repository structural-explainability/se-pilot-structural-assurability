# Experimental Protocol

## Purpose

Investigate claim-resolution conditions arising from the query-violation
example in Section 3 of NIST AI 200-2 ipd.

This experiment supports pilot record TEVV-001. It examines the
applicability and limitations of Structural Assurability under
explicitly stated modeling assumptions.

## Method

1. Identify the source material and preserve its provenance.
2. Identify the source's evaluation question and distinguish it from
   claims introduced for experimental analysis.
3. Specify the admissible worlds, observation channels, and evaluator
   conditions.
4. State all assumptions introduced by the experimental model.
5. Identify applicable Structural Assurability definitions and results.
6. Keep source-stated content separate from researcher modeling choices.
7. Construct and test candidate indistinguishable, claim-disagreeing
   worlds where appropriate.
8. Record conditional results, limitations, unresolved obligations,
   and whether further analysis is justified.

## Initial Experiment

The initial finite-model experiment is implemented in:

`experiments/tevv-athlon/query_violation.py`

It examines two conditional questions:

- Whether observations from three tested scenarios resolve a
  researcher-defined claim covering an additional, untested scenario.
- Whether red-teaming observations alone resolve organic-use safety
  when organic and adversarial behavior may vary independently.

The experiment is illustrative.
It does not model all evidence collected by the NIST assessment
or establish that its constructed
worlds are realizable in operational AI systems.

## Interpretation

Experimental outputs establish results only for their specified
finite models and assumptions.

Further analysis must examine witness realizability, the actual
evidence-collection process, and relevant assumptions and limitations
documented by NIST.

## Research Record

The authoritative investigation record is:
`docs/en/mappings/tevv-athlon/TEVV-001.toml`.

Record status remains `OPEN`.
