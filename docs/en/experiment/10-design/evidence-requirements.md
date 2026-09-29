# Evidence Requirements

## What the Source Describes as Collected

Section 3.3 and Table 2 describe, for this example: User Testing chats
across all three tested scenarios, annotated for Helpfulness via a
Post-Task Questionnaire; and, for Violation Frequency, chats from both
User Testing and Red Teaming, labeled by human annotators against an
Annotation Schema.
Section 3.4 states the annotation is applied "across
User Testing and Red Teaming sessions," not restricted to one Event type.

A precision worth recording here rather than in `protocol.md`:
Section 3 is presented as an illustrative worked example,
adapted from the NIST ARIA 0.1 Pilot Evaluation
(footnote 1, citing NIST AI 700-2) "to simplify the
description of the TEVV-Athlon approach."
It is not a report of completed, real evidence.
If real evidence exists to examine for this problem class,
it would be in the ARIA report, a separate source not yet reviewed for
this record.

## What Claim A Would Need

Claim A (all four scenarios) is not resolved by evidence restricted to the
three tested scenarios, under any combination of User Testing and Red
Teaming, because the untested scenario is unobserved by construction.
See `query_violation.py`'s Candidate 1.
Resolving it would need either:

- direct evidence on the untested scenario (extend testing to it), or
- an explicit, source-independent representativeness assumption
  connecting the untested scenario's behavior to one of the three tested
  ones, which the source does not supply, and which the "low-impact"
  framing of the tested scenarios (Section 3.1) argues against assuming
  without separate justification.

## What Claim B Would Need

Claim B (organic-use safety on the three tested scenarios) is not
resolved by Red Teaming evidence alone.
See `query_violation.py`'s Candidate 2.
This is the narrower, source-permitted evidence set
described in `claims.md`, not the full set the source's own example
actually collects.

In the current idealized model, adding complete observations of
organic-use behavior across the three tested scenarios resolves Claim B
directly, because the observations contain the behavior the claim concerns.

However, NIST's example collects sampled interactions and human
annotations, not complete knowledge of organic-use behavior.
Consequently, collecting evidence through both User Testing and
Red Teaming does not, by itself, establish that Claim B is resolved
under a realistic sampling model.

The current experiment establishes only that Red Teaming alone
does not resolve Claim B under the specified independence assumption.
Whether the combined evidence resolves Claim B depends on the sampling,
measurement, and generalization assumptions that remain to be modeled.

## Consequences for the Two Candidates

Candidate 1 and Candidate 2 are not the same kind of gap.

Candidate 1 concerns a scenario the source's own
described evidence-collection process never reaches, tested or untested.

Candidate 2 concerns the relationship between evidence collected
through Red Teaming and behavior under organic use.
The current experiment isolates Red Teaming, although NIST's example
also collects organic-use evidence through User Testing.

The distinction matters for what "further analysis"
(per `protocol.md`) would need to check:
Candidate 1 needs a realizability argument about the
untested scenario;
Candidate 2 needs to establish whether real evaluators,
following the source's guidance, would actually be expected to make the
narrower choice, or whether the permissive wording is not meant to be read
as license to skip organic annotation in practice.
