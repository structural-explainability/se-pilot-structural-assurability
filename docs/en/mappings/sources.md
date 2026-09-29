# Source Register

| ID    | Source                                                                                                                                                                                                                                                                | Role in the original mapping                                                                  | Review status                                                          |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| S-001 | [NIST, TEVV-Athlon Framework for Evaluating AI Systems](https://www.nist.gov/artificial-intelligence/ai-research/tevv-athlon-framework-evaluating-ai-systems), initial public draft NIST AI 200-2 (Aug. 2026); [draft DOI](https://doi.org/10.6028/NIST.AI.200-2.ipd) | Initial external assessment-framework case; Events, Tools, Blocks and assessment construction | Overview verified; section-by-section review pending                   |
| S-002 | [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), AI RMF 1.0 (2023)                                                                                                                                                         | Risk-management context and TEVV terminology                                                  | Overview verified; compare relevant provisions                         |
| S-003 | [NIST, Building Evaluation Probes into Agentic AI](https://www.nist.gov/programs-projects/building-evaluation-probes-agentic-ai), project page (2026)                                                                                                                 | Evidence-grounding probes, structured audit trail and agentic evaluation instrumentation      | Project overview verified; inspect linked code and papers              |
| S-004 | [NIST AI 800-4, Challenges to the Monitoring of Deployed AI Systems](https://doi.org/10.6028/NIST.AI.800-4) (Mar. 2026)                                                                                                                                               | Post-deployment monitoring categories, barriers and open questions                            | Publication metadata verified; full report review pending              |
| S-005 | [PAgE 2026: Principles of Agentic Engineering, PLDI 2026](https://pldi26.sigplan.org/home/page-2026)                                                                                                                                                                  | Specifications, testing, verification, monitoring and repair for agents                       | Workshop overview verified; identify exact relevant paper(s)           |
| S-006 | [Apollo Research: Claude Sonnet 3.7 (often) knows when it is in alignment evaluations](https://apolloresearch.ai/science/claude-sonnet-37-often-knows-when-its-in-alignment-evaluations) (2025)                                                                       | Evaluation awareness as a possible validity threat to behavioral measurements                 | Research overview verified; methodology and limitations review pending |

## Source-level work needed

- Record stable citation and document version; retain local references to relevant passages with page or section numbers.
- For NIST AI 200-2, verify the exact wording of sections identified in the earlier comment outline against the initial public draft.
- Identify which PAgE papers, if any, are directly relevant.
- Distinguish the NIST probes project's stated scope (grounding and source-support checks) from broader claims about all agentic AI assurance.
- For evaluation-awareness work, distinguish observable expressions of awareness from actual awareness, as the latter may be underdetermined.

## Relevant formal research, not an external framework

- [Formal Theory: Structural Assurability](https://github.com/structural-explainability/se-theory-structural-assurability): definitions, claim resolution and proof obligations.
- [Paper 320: Structural Assurability](https://github.com/structural-explainability/paper-320-structural-assurability): manuscript development.

The external source register should stay independent of theory-derived interpretations; crosswalks belong in study-specific mapping records.
