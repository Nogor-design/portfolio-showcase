# Week Three Runbook

Status: complete for public-site polish and sixth-case gate  
Start date: 2026-06-17

## Week Three Goal

Turn the verified Week 2 portfolio into a sharper recruiter-facing package, coordinate local AI workers, and decide whether the sixth case study is ready for public release.

## Worker Assignments

| ID | Owner | Scope | Output |
|---|---|---|---|
| WK3-001 | Codex PM | Integrate Week 3 public-site polish and final verification | Site edits, docs, QA results |
| WK3-002 | Claude CLI | Recruiter-facing copy critique | Recommended fast wins and sixth-case caution |
| WK3-003 | Gemini CLI | PM checklist and acceptance criteria | Week 3 checklist and risks |
| WK3-004 | Ollama phi4:14b | Local-only redaction categories | Sensitive classes to avoid |
| WK3-005 | Codex subagent Socrates | Read-only NinjaAccountManager discovery | Sixth-case gate: defer until mocked capture path exists |
| WK3-006 | Codex subagent Helmholtz | Static-site copy review | `WEEK_THREE_COPY_REVIEW.md` plus tiny homepage copy edits |

## Completed Work

- Updated homepage copy to say the portfolio is Week 3 current, not still being packaged.
- Added a clear availability line for senior AI/software engineering roles and contract internal-tool builds.
- Reworded proof-panel stats so they read as public credibility signals rather than internal audit shorthand.
- Standardized static CSS cache-busting across all case pages.
- Added a redaction note to the Agentic Idea Validation Engine case page.
- Refreshed outreach guidance with role-specific angles.
- Re-checked the sixth-case candidate and kept `NinjaAccountManager` gated until a public-safe mocked demo exists.

## Acceptance Criteria

- No public site references stale Week 2 copy.
- All static HTML pages load the same stylesheet version.
- Five existing case studies remain the public portfolio surface.
- Sixth case is not published until a mocked, redacted capture path exists.
- Redaction notes continue to avoid customer data, account data, secrets, trading IP, and local private paths.

## Deferred Work

- Build a mocked `NinjaAccountManager` demo mode with fake account/order/market/strategy state.
- Capture Dashboard and Strategy/runtime screenshots only after the mocked mode exists.
- Redeploy Netlify only after login or durable GitHub connection is available; GitHub Pages remains the verified public URL.
