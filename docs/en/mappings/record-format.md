# Assurance Mapping Record Format

## Purpose

An assurance mapping record connects a specific external evaluation
question to applicable Structural Assurability concepts and results.

Records preserve the external source's terminology and distinguish
source statements from researcher interpretation.

The format is initially maintained in this pilot. Once it has
been exercised against different assurance approaches, its reusable
parts may be extracted into `se-assurance-mapping-kit`.

## Required Record Sections

### Identity

- Stable record identifier.
- Record status.
- External framework or method.

### Source

- Publisher and document title.
- Document version or publication date.
- Source URL.
- Exact source location, where established.
- Scope of source material actually reviewed.

### Source Structure

Describe the source's relevant concepts and relationships using
its own terminology.

Do not force different frameworks into an artificial common
structure.

### Evaluative Claim

Distinguish an explicit source claim from a claim formulated
by the researcher for investigation.

### Required Distinctions

Identify the alternatives that the evaluation would need
to distinguish to address the specified claim.

### Evidence

Identify the observations, measurements, records, or other
evidence relevant to those distinctions.

Distinguish evidence named by the source from additional
evidence proposed by the researcher.

### Evaluator Conditions

Record applicable access, knowledge, cooperation, trust,
and resource conditions.

Use `NOT ESTABLISHED` where the reviewed source does not
provide enough information.

### Assumptions

Record the conditions on which the proposed evidentiary
relationship depends.

Distinguish assumptions explicitly stated by the source
from assumptions introduced for the investigation.

### Structural Assurability Mapping

Identify relevant formal concepts, definitions, theorems,
or modeling limitations.

A conceptual correspondence does not establish that a
formal result applies to an operational system.

### Research Question

State one bounded question that can be investigated
against the source and the formal theory.

### Evidence and Analysis

Record source checks, constructed examples, experiments,
counterexamples, and relevant competing interpretations.

### Outcome

Classify the record as:

- `OPEN`: an investigation has been formulated but no
  substantiated conclusion has been reached.
- `SUPPORTED`: the stated finding is supported within
  its explicitly documented scope.
- `NOT SUPPORTED`: the investigated proposition was
  not supported by the evidence examined.
- `INDETERMINATE`: the available material cannot
  settle the investigated proposition.

Record limitations and outstanding work separately.

## Validation Boundary

Structural validation covers record structure, required fields,
identifiers, references, and controlled status values.

Structural validation does not infer that:

- A researcher interpretation is faithful to the source.
- A formal theorem applies to a real system.
- Available evidence resolves a claim.
- An assurance argument is justified.

Those are research and adjudication responsibilities,
not schema-validation outcomes.

## Initial Test

Exercise this format against two different sources:

1. NIST TEVV-Athlon, focusing on the relationship
   between evaluation design, measurements, and claims.
2. UK AISI's cyber-inability safety-case template,
   focusing on the relationship between risk models,
   proxy evaluations, and the resulting safety argument.

The format is ready for extraction after both
records can be completed without losing important
source-specific distinctions.
