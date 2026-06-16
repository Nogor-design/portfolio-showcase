# Model Routing And Token Budget

## Available Worker Channels

Verified on 2026-06-16 from `D:\a1-program-manager`:

| Tool | Command Shape | Use |
|---|---|---|
| Codex | Current PM thread and subagents | PM, integration, code edits, verification |
| Claude Code | `claude -p "<prompt>"` | Strong synthesis, critique, copy, architecture review, repo-specific worker tasks |
| Gemini CLI | `gemini -p "<prompt>"` | Alternate critique, broad summarization, visual/copy review, checklist generation |
| Ollama | `ollama run <model> "<prompt>"` | Cheap local inventory, drafts, redaction sweeps, README summaries |

## Local Ollama Models Seen

Notable installed models:

- `qwen2.5:72b`
- `qwen3-coder:30b`
- `deepseek-coder:33b`
- `qwen2.5:32b`
- `deepseek-r1:32b`
- `phi4:14b`
- `gemma3:27b`
- `devstral-small-2`
- `nomic-embed-text`
- `mxbai-embed-large`

## Routing Rules

| Task Type | Preferred Worker |
|---|---|
| Repo inventory from README/docs | Ollama or Codex subagent |
| Final case-study copy | Claude or Gemini, then Codex edit |
| Technical architecture accuracy | Codex local inspection, optionally Claude second pass |
| Redaction risk review | Ollama first pass, Codex final pass |
| Portfolio site implementation | Codex primary, Claude/Gemini for review |
| Screenshot captioning and alt text | Ollama |
| Recruiter-facing positioning | Claude/Gemini, Codex final synthesis |
| App run/debug | Codex primary |

## Budget Rules

- Keep each delegated prompt bounded to one project or one deliverable.
- Ask workers for structured output, not open-ended exploration.
- Prefer summaries saved in workspace files over long chat history.
- Use local Ollama for first drafts when correctness risk is low.
- Use Claude/Gemini for high-leverage judgment after local evidence is gathered.
- Do not send raw customer data, account data, or private trading logic to external models.

## Token Ledger Template

| Date | Worker | Task | Input Size | Output Size | Status | Notes |
|---|---|---:|---:|---:|---|---|
| 2026-06-16 | Codex | Initial inventory and PM setup | Medium | Medium | In progress | Seeded PM docs |
| 2026-06-16 | Claude CLI | Empire of Drawdown packaging brief | Small | Medium | Complete | Read-only repo outline |
| 2026-06-16 | Gemini CLI | Job Application Factory packaging brief | Small | Medium | Complete | Read-only repo outline |
| 2026-06-16 | Ollama phi4:14b | Trades Resource dashboard local summary | Medium | Small | Complete | Local-only customer-adjacent summary |
