# Week Three Copy Review

Date: 2026-06-17  
Scope: static portfolio site and recruiter-facing project docs  
Posture: copy/documentation recommendations only; no media edits or new private project data

## Summary

The portfolio is already broadly recruiter-readable and redaction-aware. The strongest near-term polish is not adding more evidence; it is making the existing proof easier to scan, keeping internal planning paths out of outreach materials, and converting audit-style phrasing into hiring-manager value language where the public site currently sounds operational.

Tiny safe homepage edits made during this pass:

- `Demo candidates verified` -> `Runnable demos verified`
- `Services And Strengths` -> `Services and Strengths`
- `Public portfolio build / Week 2` -> `Public portfolio build / Week 3`

## Public Site Opportunities

| Area | Current Pattern | Recommendation | Rationale |
|---|---|---|---|
| Homepage proof panel | Strong evidence, but some labels are internal/audit-flavored | Keep proof labels outcome-oriented: runnable demos, tests observed, grounded workflows | Recruiters scan for credibility faster than implementation detail |
| Case-study bullets | Several bullets say what was verified during packaging | Keep one verification bullet, but lead each card with user/business/engineering value | Prevents the homepage from reading like an internal QA report |
| Trades Resource card | `contract-ready business workflow design` | Consider `business workflow design for real staffing operations` | Avoids implying production readiness beyond the current documented persistence/auth state |
| TA Foundation homepage copy | Accurate but dense | Keep the overview, but split future recruiter copy into 2-3 slices: reporting, optimizer orchestration, diagnostics | The project is large; smaller capability claims are easier to believe and discuss |
| Redaction notes | Strong and appropriate | Keep notes, but avoid expanding them with examples from private projects | They protect the public story without leaking paths, account data, or raw artifact names |

## Docs And Outreach Opportunities

| File | Recommendation | Notes |
|---|---|---|
| `OUTREACH_PACKAGE.md` | Refresh status from Week 2 wording when the next public deploy is current | Good recruiter message; no need for new evidence |
| `INTERVIEW_TALKING_POINTS.md` | Add one short "what I owned" line per project before interviews | Keep it high-level; do not add private repo paths or customer/trading specifics |
| `PORTFOLIO_INVENTORY.md` | Treat as internal only unless local paths are removed | It contains private/local project paths by design |
| `DEMO_RUNABILITY_AUDIT.md` | Treat as internal evidence log, not recruiter copy | It includes local paths, ports, and operational notes |
| `PUBLIC_REDACTION_REVIEW.md` | Keep as internal gate record | Useful for safety; not polished public copy |

## Suggested Recruiter-Safe Copy Patterns

- "Built a local-first AI workflow that drafts from approved evidence and flags unsupported claims."
- "Turned a repeated operations process into a daily dashboard with clear ownership and follow-up states."
- "Packaged a large analytics system into sanitized public slices that show architecture without exposing proprietary trading logic."
- "Verified public demos with tests, safe demo data, and redaction checks before sharing."

## Guardrails

- Do not add new screenshots, raw manifests, private report HTML, customer files, trading account details, strategy parameters, broker identifiers, local filesystem paths, secrets, or unpublished customer names.
- Keep public claims tied to already documented verification: tests observed, HTTP 200 launches, mock/demo modes, sanitized screenshots, and dependency checks.
- If a future copy pass adds stronger outcomes, use generic business value unless the underlying project has a public-safe metric.
