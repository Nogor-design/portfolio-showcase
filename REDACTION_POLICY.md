# Redaction Policy

Before any screenshot, case study, code excerpt, or generated report becomes public, check it against this policy.

## Never Publish

- Customer names, phone numbers, emails, addresses, contracts, resumes, or private staffing files
- Trading account IDs, broker names tied to accounts, balances, orders, positions, or live PnL
- Exact proprietary trading strategy rules, thresholds, template names, or allocation logic
- API keys, tokens, local secrets, license keys, machine IDs, or `.env` values
- Local filesystem paths that reveal private structure beyond project names
- Raw prompt traces that include private instructions, credentials, or unpublished IP

## Usually Sanitize

- Strategy parameters and optimizer fitness thresholds
- Exact market dates if tied to live decision-making
- Internal project codenames
- Proprietary template naming conventions
- Customer workflow files and uploaded data manifests
- Git remotes if private

## Safe To Show

- High-level architecture diagrams
- Synthetic demo data
- Generated sample rows with fake names and fake accounts
- Public README snippets after attribution/ownership check
- Screenshots with blurred/redacted sensitive cells
- Test results and validation summaries without private paths

## Redaction Workflow

1. Capture screenshot or artifact into a private staging folder.
2. Review manually for sensitive text.
3. Run an LLM redaction pass on the visible text or screenshot notes.
4. Produce a sanitized public copy.
5. Add the artifact path and redaction status to `AGENT_TASK_LEDGER.md`.

## External Model Rule

Do not send raw customer files, raw trading exports, live account data, private resumes, or proprietary strategy parameters to Claude, Gemini, or other external services. Use Codex/local inspection or Ollama for sensitive local-only work.

