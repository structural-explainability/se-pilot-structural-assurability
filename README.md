# SE Pilot: Structural Assurability

[![Docs Site](https://img.shields.io/badge/docs-site-blue?logo=github)](https://structural-explainability.github.io/se-pilot-structural-assurability/)
[![Repo](https://img.shields.io/badge/repo-GitHub-black?logo=github)](https://github.com/structural-explainability/se-pilot-structural-assurability)
[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](./LICENSE)

[![CI](https://github.com/structural-explainability/se-pilot-structural-assurability/actions/workflows/ci-python-zensical.yml/badge.svg?branch=main)](https://github.com/structural-explainability/se-pilot-structural-assurability/actions/workflows/ci-python-zensical.yml)
[![Docs Deploy](https://github.com/structural-explainability/se-pilot-structural-assurability/actions/workflows/deploy-zensical.yml/badge.svg?branch=main)](https://github.com/structural-explainability/se-pilot-structural-assurability/actions/workflows/deploy-zensical.yml)

> IN PROGRESS: Applied research investigating the applicability and
> limitations of claim-relative Structural Assurability.

## Purpose

This pilot investigates whether Structural Assurability can identify
useful distinctions among available observations, evidentiary
capabilities, evaluator constraints, trust assumptions, and claim
resolution when examining concrete assurance claims and external
evaluation frameworks.

The research uses source-grounded mappings, explicit assumptions,
and reproducible experiments where needed.

Possible outcomes include constructive examples, counterexamples
within specified models, research findings, proposed formal
extensions, or contributions to external evaluation frameworks.

No particular outcome is presumed.

## Initial Study

The initial study draws on
[NIST's TEVV-Athlon Framework for Evaluating AI Systems](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.200-2.ipd.pdf).

NIST's framework provides a concrete evaluation methodology through
which to investigate the applicability and limitations of Structural
Assurability.

The study begins with NIST's illustrative query-violation assessment,
examining relationships among evaluative questions, observations,
evidence, evaluator conditions, and modeling assumptions.

Source-stated material is distinguished from researcher-defined
claims and experimental assumptions.
The investigation seeks to clarify what
claim-relative Structural Assurability can contribute,
where additional justification is required, and where the theory
itself may need further development.

NIST has opened the framework for
[public comment](https://www.nist.gov/artificial-intelligence/ai-research/tevv-athlon-framework-evaluating-ai-systems)
until 2026-10-06.

See the [study specification](docs/en/mappings/SPECIFICATION.md)
and [mappings](docs/en/mappings/index.md).

## Experiments

```shell
uv run python experiments/tevv-athlon/query_violation.py
```

The initial experiment produces two illustrative, conditional results:

- Candidate 1: Under the researcher's four-scenario model,
  observations from User Testing and Red Teaming in the three
  tested scenarios do not resolve a researcher-defined claim
  that also covers an untested fourth scenario.

- Candidate 2: Under an explicit assumption that organic and
  adversarial behavior can vary independently, Red Teaming
  alone does not resolve the researcher-defined organic-use claim.
  NIST's example also collects organic-use evidence through
  User Testing. In the idealized model, complete observations
  of organic-use behavior resolve the claim directly.
  Section 3.3 states that both User Testing and Red Teaming
  can be used to measure Violation Frequency.
  Whether an evaluator would collect both, and what conclusions sampled
  interactions and human annotations can support,
  remain open research questions.

Both constructions produce reproducible witness pairs within
their specified finite models.
These results concern the researcher-defined claims and modeling
assumptions.
They do not establish claims about the behavior of operational AI systems.

## Related Research

- [Formal Theory: Structural Assurability](https://github.com/structural-explainability/se-theory-structural-assurability)
- [Formal Theory Documentation](https://structural-explainability.github.io/se-theory-structural-assurability/)
- [Paper 320: Structural Assurability](https://github.com/structural-explainability/paper-320-structural-assurability)

The Lean repository is authoritative for formal definitions and
theorems. The paper develops the research argument. This pilot
investigates applicability to external assurance problems.

## Research Boundaries

A difference in available observations or structural properties does
not independently establish improved evidentiary capabilities or
claim resolution.

The pilot separates external source statements, researcher
interpretation, formal results, experimental observations, and
substantiated findings.

It does not establish the safety, trustworthiness, or adequacy
of an evaluated system.

See
[SPECIFICATION.md](docs/en/mappings/SPECIFICATION.md)
for the research method, mapping requirements, boundaries,
and expected outputs.

## Development

This repository uses `uv`.

```shell
uv self update
uv python install
uv lock --upgrade
uv sync
uv audit

# Update GitHub Actions and pin all action references to immutable SHAs
uvx gha-tools autoupdate --pin=all --write .github/workflows

# Then audit the resulting GitHub configuration for security findings
uvx zizmor@latest .github/

uv run prek install -f
uv run prek update --freeze --cooldown-days 7

git add -A
uv run prek run --all-files
# repeat if changes were made
uv run prek run --all-files

uvx se-mapping-assurance validate-mapping --path docs/en/mappings/tevv-athlon/TEVV-001.toml --strict

uvx se-mapping-assurance validate-mapping --path docs/en/mappings/uk-aisi/AISI-001.toml --strict
```

## Annotations

[.annotations/annotations.md](./.annotations/annotations.md)

## Citation

See [CITATION.cff](CITATION.cff).

## Documentation

[Docs Site](https://structural-explainability.github.io/se-pilot-structural-assurability/)

## License

[MIT](./LICENSE)

## Repository Manifest

[SE_MANIFEST.toml](SE_MANIFEST.toml)

## Specification

[SPECIFICATION.md](docs/en/mappings/SPECIFICATION.md)
