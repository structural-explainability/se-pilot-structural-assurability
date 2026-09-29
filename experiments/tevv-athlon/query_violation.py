"""experiments/tevv-athlon/query_violation.py - Finite-model sketch for query-violation TEVV-Athlon example.

Pilot record: TEVV-001

Status: Exploratory finite-model constructions.

Run with:

uv run python experiments/tevv-athlon/query_violation.py

Finite-model sketch:

Using NIST's query-violation example (NIST AI 200-2 ipd, Section 3),
investigate which researcher-defined claims can be resolved by
specified observation channels under an idealized finite model.

SOURCE-STATED (Section 3, Table 1, Table 2):

- Three tested Operational Environments:

    TV Shows, Meal Planning, Travel Planning.
    Explicitly "low-impact" per the source text.

- Events:

    User Testing (evidence for Helpfulness + Violation Frequency),
    Red Teaming (evidence for Violation Frequency only).

- Tool for Violation Frequency: human annotation via an Annotation Schema.

- Stated evaluation goal:

    To what extent do chatbots successfully answer
    queries without giving away violations?

RESEARCHER MODELING CHOICES
(not source-stated, flagged per the pilot's method, step 6):

- The source's measurement-style goal is converted here into a
  resolution-style claim ("no violations across the intended scenario
  space") so it fits claimResolvedBy's shape.
  The source itself never commits to a binary pass/fail claim.
  It asks for descriptive statistics.
  The conversion to a binary claim is a researcher modeling choice,
  not something stated by the source.

- A fourth, UNTESTED scenario is added to represent "the rest of the
  intended-use scenario space" the claim is actually about.
  NIST's example never specifies what that space is,
  only that three low-impact scenarios were chosen from it.

- Worlds encode binary, scenario-level violation-free behavior
  for organic use across four scenarios and Red Teaming across
  the three tested scenarios.
  Organic and adversarial behavior may vary independently.
  This is a researcher modeling assumption motivated by the
  different purposes of the two Events.
  The model treats scenario-level behavior as directly observable.
  It does not represent sampled prompts, individual responses,
  or human annotations.
"""

from collections import defaultdict
from itertools import product


def resolved(worlds, channels, claim):
    """Check if the claim is resolved given the observed channels across all worlds."""
    groups = defaultdict(set)
    for w in worlds:
        groups[tuple(ch(w) for ch in channels)].add(claim(w))
    return all(len(v) == 1 for v in groups.values())


def witnesses(worlds, channels, claim):
    """Return a list of witness tuples where the claim is contradicted within the same observed channels."""
    groups = defaultdict(list)
    for w in worlds:
        groups[tuple(ch(w) for ch in channels)].append(w)
    out = []
    for obs, ws in groups.items():
        vals = {claim(w) for w in ws}
        if len(vals) > 1:
            a = next(w for w in ws if claim(w))
            b = next(w for w in ws if not claim(w))
            out.append((obs, a, b))
    return out


# World: (tv, meal, travel, untested) violation-free? for organic queries;
# (rt_tv, rt_meal, rt_travel) violation-free? under adversarial red-teaming;
# these are INDEPENDENT per scenario -- nothing in the source claims a
# fixed relationship between organic and adversarial behavior.
Scenario = ["tv", "meal", "travel", "untested"]
World = list(product([True, False], repeat=4))  # organic, 4 scenarios
RTWorld = list(product([True, False], repeat=3))  # red-team, 3 tested scenarios only
Worlds = [(o, r) for o in World for r in RTWorld]


def organic(w, i):
    """Return the organic behavior for the i-th scenario in the world tuple."""
    return w[0][i]


def redteam(w, i):
    """Return the red-team behavior for the i-th scenario in the world tuple."""
    return w[1][i]


"""
CANDIDATE 1: coverage / representativeness of the untested scenario ----

Conditional coverage result.
The fourth scenario and universal claim are researcher modeling choices,
not NIST's assessment commitments.
"""
claim_all = lambda w: all(w[0])  # "no violations across ALL FOUR scenarios"

user_testing_only = lambda w: tuple(organic(w, i) for i in (0, 1, 2))  # 3 tested
print("== Candidate 1: coverage ==")
print(
    "User Testing on 3 tested scenarios resolves claim over all 4:",
    resolved(Worlds, [user_testing_only], claim_all),
)
w = witnesses(Worlds, [user_testing_only], claim_all)[0]
print("  witness: same evidence on tested scenarios, untested scenario differs")
print(
    "  ",
    w[1][0],
    "vs",
    w[2][0],
    " (untested slot differs:",
    w[1][0][3],
    "vs",
    w[2][0][3],
    ")",
)

with_redteam = lambda w: (user_testing_only(w), tuple(redteam(w, i) for i in (0, 1, 2)))
print(
    "Adding Red Teaming on the 3 tested scenarios still resolves claim over all 4:",
    resolved(Worlds, [with_redteam], claim_all),
)

"""
CANDIDATE 2: does organic behavior track adversarial behavior?
Claim restricted to the TESTED scenarios only, but under ORGANIC use,
i.e. does passing red-teaming say anything about organic-query safety?
"""
claim_tested_organic = lambda w: all(organic(w, i) for i in (0, 1, 2))
redteam_only = lambda w: tuple(redteam(w, i) for i in (0, 1, 2))

print()
print("== Candidate 2: adversarial vs organic ==")
print(
    "Red Teaming alone resolves organic-use safety on the 3 tested scenarios:",
    resolved(Worlds, [redteam_only], claim_tested_organic),
)
w2 = witnesses(Worlds, [redteam_only], claim_tested_organic)[0]
print("  witness: same red-team result, organic behavior differs")
print("  organic:", w2[1][0][:3], "vs", w2[2][0][:3])
