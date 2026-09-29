# Experimental Claims

## Purpose

Specify the claims examined by the TEVV-001 experiments and distinguish
them from the evaluation objectives stated in the NIST source.

A claim is resolved by an observation model when all admissible worlds
that produce identical observations agree on the claim's truth value.

This definition is applied relative to the specified admissible worlds,
observation channels, evaluator conditions, and modeling assumptions.

## Source-Stated Evaluation Objective

Section 3 of NIST AI 200-2 ipd presents an example assessment of
chatbots performing query-violation tasks.

Its evaluation question concerns the extent to which chatbots provide
useful responses while avoiding prohibited information.

The example assesses Helpfulness and Violation Frequency across
three selected, low-impact operational environments.

NIST describes a measurement exercise using User Testing,
Red Teaming, human annotation, and descriptive statistics.

It does not assert the binary claims introduced below.

## Candidate 1: Coverage

### Researcher-Defined Claim

A chatbot exhibits no organic-use violations across four modeled
scenarios:
the three scenarios tested in NIST's example and
one additional, hypothetical scenario.

The fourth scenario represents an untested part of a broader scenario
space.
Its inclusion and the extension of the claim beyond NIST's
three tested scenarios are researcher modeling choices.

### Admissible Worlds

Each world specifies binary organic-use behavior for all four
scenarios and binary red-teaming behavior for the three tested
scenarios.

The current model permits these values to vary independently.

### Observations

The experiment first considers organic-use behavior in the three
tested scenarios.

It then adds red-teaming behavior in those same scenarios.

Both observation models treat the modeled behavior as directly
observable.
They do not yet represent sampled prompts, responses,
or human annotation.

### Conditional Result

The experiment constructs two worlds with identical observations
across both User Testing and Red Teaming in the tested scenarios
but different organic-use behavior in the fourth scenario.

Consequently, the researcher-defined four-scenario claim is not
resolved by either observation model.

This result depends on admitting a fourth scenario whose behavior
is not constrained by the observations from the tested scenarios.

It does not establish that NIST intended its example to support
the broader claim.

## Candidate 2: Organic Versus Adversarial Behavior

Examining Red Teaming separately helps identify its evidentiary
contribution and the additional information provided by User Testing.

### Researcher-Defined Claim

A chatbot exhibits no organic-use violations in the three
tested scenarios.

Unlike Candidate 1, this claim does not extend to a fourth scenario.

### Admissible Worlds

The model permits organic-use behavior and red-teaming behavior
to vary independently within each scenario.

This independence is a researcher modeling assumption.
It is not a property of real chatbots established by the NIST source
or by this experiment.

### Observations

This candidate deliberately examines Red Teaming alone.

NIST's complete example also collects violation evidence through
User Testing.
The red-teaming-only observation model therefore
does not represent the complete NIST assessment.

### Conditional Result

The experiment constructs two worlds that produce identical
red-teaming observations in all three tested scenarios but
disagree on organic-use behavior.

Under the independence assumption, Red Teaming alone does not
resolve the researcher-defined organic-use claim.

In the current idealized model, adding complete observations
of organic-use behavior across the three tested scenarios
would resolve this particular claim.

That conclusion depends on treating underlying behavior as
directly observable and should not be transferred to an
assessment based on sampled interactions.

## Claims for Further Investigation

The existing finite model abstracts away the process through which
the assessment collects evidence.

The next investigation must define a claim and an observation model
that account for actual evidence collection.

In particular, it must specify:

- The population of queries or interactions to which the claim applies.
- The relationship between sampled prompts and that population.
- The responses and annotations available to the evaluator.
- The conditions under which observed results support the claim.
- Any assumptions needed to generalize beyond observed interactions.

The specific claim, its scope, and its resolution conditions must
be established before constructing further witness pairs.

The investigation should preserve NIST's distinction between
measurement results and conclusions about broader system behavior.

## Interpretation

The two initial candidates establish conditional results within
their explicitly defined finite models.

They do not establish:

- That the constructed alternatives are realizable in actual chatbots.
- That the modeled observation channels faithfully represent all
  evidence collected by NIST's example.
- That NIST asserts either researcher-defined claim.

These remain open research obligations.

## Supporting Material

- Experiment: `experiments/tevv-athlon/query_violation.py`
- Pilot record: `docs/en/mappings/tevv-athlon/TEVV-001.toml`
- Source: NIST AI 200-2 ipd, Sections 3 and 4.5–4.6:
  https://doi.org/10.6028/NIST.AI.200-2.ipd
