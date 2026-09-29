# Changelog

<!-- markdownlint-disable MD024 -->

All notable changes to this project will be documented in this file.

The format is based on **[Keep a Changelog](https://keepachangelog.com/en/1.1.0/)**
and this project adheres to **[Semantic Versioning](https://semver.org/spec/v2.0.0.html)**.

## [Unreleased]

---

## [0.1.0] - 2026-09-29

### Added

- Initial Structural Assurability applied-research pilot.
- Research specification defining the pilot's scope, methodology,
  evidentiary requirements, and boundaries of interpretation.
- Source-grounded assurance-mapping records for two investigations:
  - TEVV-001: NIST TEVV-Athlon framework.
  - AISI-001: UK AI Security Institute cyber-inability safety-case research.
- Assurance records distinguishing source-stated material, researcher
  interpretations, completed analysis, pending analysis, and unresolved questions.
- Strict structural validation of both records using `se-mapping-assurance`.
- Reproducible finite-model experiment for NIST's query-violation example,
  examining two conditional claim-resolution questions:
  - Coverage of a researcher-defined claim extending beyond tested scenarios.
  - The relationship between red-teaming observations and organic-use behavior
    under an explicit independence assumption.
- Illustrative indistinguishable, claim-disagreeing witness pairs for both
  constructions.
- Initial research documentation, source references, repository metadata,
  and experiment execution instructions.

Both investigations remain open.
Finite-model constructions establish conditional results
under their stated assumptions, not operational validity.

---

## Notes on versioning and releases

We use **SemVer**:

- **MAJOR** - Breaking changes to artifact structure or validation semantics.
- **MINOR** - Backward-compatible additions to schema or validation rules.
- **PATCH** - Fixes, documentation, and tooling.

Package versions are derived from Git tags. Tag `vX.Y.Z` to release.

## Release Procedure (Required)

Follow these steps exactly when creating a new release.

### Task 1. Update release metadata (manual edits)

1.1. CHANGELOG.md: add section, move unreleased entries, update links
1.2. `CITATION.cff` - update `version` and `date-released`
1.3. `pyproject.toml` - update build system `fallback-version`

### Task 2. Validate

Run from the repository root in PowerShell.

```powershell
# Run repository checks.
.\sit.ps1

# Update GitHub Actions and pin all action references to immutable SHAs
uvx gha-tools autoupdate --pin=all --write .github/workflows

# Update hooks
uvx prek update
git add -A
uvx prek run --all-files

# Audit the resulting GitHub configuration for security findings
uvx zizmor@latest .github/

# Validate citation metadata
uvx cffconvert --validate

# Format markdown
npx markdownlint-cli2 --fix

# Validate examples.
uvx se-mapping-assurance validate-mapping --path docs/en/mappings/tevv-athlon/TEVV-001.toml --strict
uvx se-mapping-assurance validate-mapping --path docs/en/mappings/uk-aisi/AISI-001.toml --strict

# Run experiments
uv run python experiments/tevv-athlon/query_violation.py
```

### Task 4. Commit, push, tag

```shell
git add -A
git commit -m "Prepare X.Y.Z"
git push -u origin main
```

Verify actions run on GitHub. After success:

```shell
git tag vX.Y.Z -m "X.Y.Z"
git push origin vX.Y.Z
```

## Only As Needed (delete a tag)

```shell
git tag -d vX.Z.Y
git push origin :refs/tags/vX.Z.Y
```

## Links

[Unreleased]: https://github.com/structural-explainability/se-pilot-structural-assurability/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/structural-explainability/se-pilot-structural-assurability/releases/tag/v0.1.0

<!-- markdownlint-enable MD024 -->
