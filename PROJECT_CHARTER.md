# Project Charter

## Mission

Build a polished software portfolio in one week that helps Eric Irwin win software engineering jobs and contract work.

The portfolio should prove the ability to build practical AI, automation, analytics, and internal business platforms that replace messy manual workflows.

## Primary Audience

- Hiring managers for AI software engineer, senior software engineer, automation engineer, and platform engineer roles
- Small and midsize businesses considering contract application development
- Technical reviewers who want evidence of real systems, not toy apps

## Positioning

Eric builds local-first AI systems, workflow automation, business dashboards, trading analytics, and evidence-grounded software that turns fragmented processes into reliable tools.

## One-Week Definition Of Done

- Portfolio website exists and can be opened locally or deployed.
- 5-7 case studies are written and visually supported.
- At least 3 case studies include screenshots or short demo media.
- Private data, trading IP, account details, and customer information are redacted.
- Resume is linked or available for download.
- Each project has a clear "what this proves" section.
- A reviewer can understand the portfolio in under 5 minutes and choose deeper case studies.

## Recommended Case Study Set

1. Empire of Drawdown: trading strategy game and deterministic replay
2. Job Application Factory: local-first RAG and multi-agent application generation
3. Trades Resource Command Center: staffing operations dashboard and customer review workflow
4. Agentic Idea Validation Engine: evidence ledger for ideas, tests, results, and decisions
5. TA Foundation Trading Intelligence Suite: multiple carved-out trading analytics demos
6. Market Data Pipeline or NinjaAccountManager: backend/data or runtime integration proof

## Scope Boundaries

In scope:

- Inspecting local repos and docs
- Running apps locally when feasible
- Capturing screenshots and demo artifacts
- Writing and editing public-facing case studies
- Building a portfolio site
- Using Claude, Gemini, Codex subagents, and Ollama/local LLMs for bounded tasks

Out of scope for week one:

- Building entirely new production apps unless a critical portfolio gap remains
- Publishing private customer data
- Publishing live trading strategy parameters, account data, broker data, or proprietary edge logic
- Large refactors inside existing project repos unless needed to make a demo run

## PM Role

Codex acts as the program manager:

- Maintains the task ledger
- Assigns work to Claude, Gemini, Codex subagents, and local Ollama models
- Tracks risk, progress, model usage, and deliverables
- Consolidates outputs into the portfolio
- Verifies artifacts before declaring work complete

## Risk Register

| Risk | Mitigation |
|---|---|
| Private customer data leaks into screenshots or text | Use generated/sanitized data only; run redaction pass before public use |
| Trading IP exposed | Use architecture, workflow, and synthetic/canned artifacts; hide exact edge rules and parameter values |
| Too many projects make the portfolio feel scattered | Lead with 5-7 case studies under one coherent positioning |
| Live demos are fragile | Prefer recorded/screenshot demos plus reproducible local commands |
| Agents duplicate work or drift | Use `AGENT_TASK_LEDGER.md` and bounded prompts with expected outputs |
| Token/context exhaustion | Use local models for inventory/drafting; keep summaries in workspace docs |

