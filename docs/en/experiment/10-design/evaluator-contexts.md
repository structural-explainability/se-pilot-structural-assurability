# Evaluator Conditions

## Source-Stated Content (Section 3.1)

The source gives some evaluator-condition detail specific to this example,
in the course of answering the Heilmeier-style Question 3 and 4 prompts
from Section 2.1:

- **Resources**: "computational environments, expertise needed to design
  materials, the materials themselves, and a group of users to interact
  with chatbots."
- **Cooperation**: recruitment of human testers and red-teamers is
  required; time and cost are described as sensitive to "the ability to
  recruit individuals to interact with chatbots."
- **Method grounding**: the approach "will build on current approaches to
  user studies in human-computer interaction."

The source does not state, for this example specifically:

- Whether the evaluator has direct API or interface access to the systems
  under test, or works through some intermediary.
- Any trust or provenance assumption about the human testers, red-teamers,
  or annotators themselves.
  It makes no statement of annotator training,
  inter-rater reliability, or independence between the group producing
  Events and the group applying the Annotation Schema.
- Budget or time bounds beyond the general acknowledgment that cost and
  timeline depend on recruitment.

## What the Experiment Models

`experiments/tevv-athlon/query_violation.py` does not model evaluator
conditions in the Access/Resource/Trust/Cooperation/Budget sense that
`AssurabilityModel` uses.
It treats the stated observation channels (User Testing results, Red Teaming results)
as simply available to the evaluator,
with no explicit access or trust model attached to how they
were obtained.

This is a limitation of the current experiment.
It cannot yet establish how evaluator access, resources, trust,
or cooperation affect the resolution of either candidate claim.
Its results concern only the distinguishing power of the
specified observation channels under the current modeling assumptions.

A version of either candidate that models evaluator access explicitly (for
example, an evaluator with API access to run additional queries directly,
versus one limited to the two collected Event types) is future work.

## Relationship to TEVV-001

TEVV-001's own Evaluator Conditions field lists these as still to be
established for a concrete assessment.
