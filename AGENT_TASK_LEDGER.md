# Agent Task Ledger

This is the active work queue. Every delegated task should have a bounded owner, expected output, and status.

## Status Key

- `todo`
- `assigned`
- `blocked`
- `review`
- `done`

## Active Tasks

| ID | Status | Owner | Project | Task | Expected Output | Notes |
|---|---|---|---|---|---|---|
| PM-001 | done | Codex | Program | Verify Claude/Gemini/Ollama CLI availability | Version/command notes in routing file | Claude Code 2.1.178, Gemini 0.45.0 |
| PM-002 | done | Codex | Program | Create PM control docs | Markdown files in `D:\a1-program-manager` | Initial seed complete |
| INV-001 | done | Claude | Empire of Drawdown | Inspect README/demo docs and draft case study outline | `case_studies/empire_of_drawdown_outline.md` | Produced packaging brief; Codex cleaned into case-study workspace |
| INV-002 | done | Gemini | Job Application Factory | Inspect README/user flow and draft case study outline | `case_studies/job_application_factory_outline.md` | Produced packaging brief; Codex cleaned into case-study workspace |
| INV-003 | done | Ollama | Trades Resource Dashboard | Summarize public-safe business value and screenshot checklist | `case_studies/trades_resource_dashboard_outline.md` | Used local model for customer-adjacent material |
| INV-004 | done | Codex | TA Foundation | Build TA demo slice matrix with evidence links | `case_studies/ta_foundation_demo_matrix.md` | Built from current capability catalog, analysis guide, and external project map |
| SITE-001 | done | Codex | Portfolio Site | Choose site stack and scaffold first version | Website files | Static site exists under `site/`; four runtime screenshots plus TA visual wired; final render check passed |
| SITE-002 | done | Codex | Portfolio Site | Add individual case-study pages | Five linked case-study pages | Pages added for Empire, JAF, Trades, Agentic Engine, and TA Foundation |
| SITE-003 | done | Codex | Portfolio Site | Package resume inside static site | Resume PDF served from site root | Static server returns HTTP 200 for resume PDF |
| QA-001 | done | Codex | Portfolio Site | Run public redaction and render review | `PUBLIC_REDACTION_REVIEW.md` and verification notes | Trades screenshot cropped; no secret values found in static site scan |
| RUN-001 | done | Codex | Agentic Engine | Run tests and launch local server | Runability notes and screenshots plan | 51 tests passed; local server returned HTTP 200; screenshot captured |
| RUN-002 | done | Codex | Trades Resource Dashboard | Launch demo data mode and inspect privacy controls | Runability notes and screenshot list | Sanitized runtime screenshot captured; demo data/client demo mode verified; admin screens absent |
| RUN-003 | done | Codex | Empire of Drawdown | Launch API/web demo mode | Runability notes and screenshot list | API/web launch fixed; overview, Battle Replay, and Debrief screenshots captured |
| RUN-004 | done | Codex | Job Application Factory | Verify mock demo mode without personal data | Runability notes and screenshot list | Temporary data dir used; Mock Demo Mode verified; screenshot captured |
| RUN-005 | done | Codex | TA Foundation | Create public-safe visual without strategy/account leakage | Sanitized visual and verification notes | `site/media/ta-foundation-suite.png` generated; homepage/detail page wired; browser verification passed |
| DEPLOY-001 | done | Codex | Portfolio Site | Purge unsafe Git history | Single clean root commit | `master` rewritten to one public-safe commit |
| DEPLOY-002 | done | Codex | Portfolio Site | Add Netlify repo config | `netlify.toml` | Netlify should publish `site/` when connected to GitHub |
| SITE-004 | done | Codex | Portfolio Site | Add intentional contact links | Homepage contact buttons | Email, GitHub, and resume links added |
| RUN-006 | done | Codex | Job Application Factory | Verify and publish mock package proof | `site/media/jaf-package-proof.png` plus case-page media strip | Generated with ignored temporary `JAF_DATA_DIR`; fictional Alex Builder/VibeTech data only |
| OUT-001 | done | Codex | Portfolio Site | Draft outreach/share package | `OUTREACH_PACKAGE.md` | Includes recruiter message, hiring-manager message, talk track, and demo order |
| RUN-007 | done | Codex + Banach | TA Foundation | Add sanitized report proof board | `site/media/ta-weekly-report-suite.png` plus TA case-page media strip | Derived from report-suite index and weekly coverage package summary; raw manifests withheld |
| INV-005 | done | Codex + Aquinas | Portfolio Site | Decide sixth case candidate | `SIXTH_CASE_DECISION.md` | NinjaAccountManager wins; Market Data Pipeline deferred or folded into TA |
| PM-003 | done | Codex | Program | Audit Week 2 completion and remaining gate | `WEEK_TWO_COMPLETION_AUDIT.md` | Week 2 complete and publicly verified on GitHub Pages |
| QA-002 | done | Codex | Portfolio Site | Verify live public deploy | Live URL QA notes | GitHub Pages passed; old Netlify drag-drop URL remains stale and should not be shared |
| WK3-001 | done | Codex PM | Program | Coordinate Week 3 worker split and integrate outputs | `WEEK_THREE_RUNBOOK.md`, `WEEK_THREE_COMPLETION_AUDIT.md` | Claude, Gemini, Ollama, and Codex subagents assigned bounded work |
| WK3-002 | done | Claude CLI | Portfolio Site | Review recruiter-facing copy and proof gaps | Week 3 recommendations in PM transcript | Recommended staleness cleanup, role signal, Agentic redaction note, and sixth-case deferral |
| WK3-003 | done | Gemini CLI | Program | Produce Week 3 checklist and risk frame | Week 3 checklist in PM transcript | Emphasized NinjaAccountManager acceptance criteria and deployment stability |
| WK3-004 | done | Ollama phi4:14b | Redaction | Summarize sensitive information classes to avoid | Local-only redaction categories | Customer data, account data, trading IP, secrets, and local paths |
| WK3-005 | done | Socrates | NinjaAccountManager | Read-only sixth-case readiness check | `SIXTH_CASE_DECISION.md` update | Found sibling project, but no public-safe mocked capture path yet |
| WK3-006 | done | Helmholtz | Portfolio Site | Static copy polish pass | `WEEK_THREE_COPY_REVIEW.md` | Added focused copy-review notes and tiny homepage copy edits |
| WK4-001 | done | Codex | NinjaAccountManager | Create public-safe sixth-case package | `case-ninja-account-manager.html` plus two synthetic visuals | Source-inspected sibling repo and generated fake dashboard/strategy captures |
| WK4-002 | done | Codex | Portfolio Site | Wire sixth case into public site | Homepage card, proof card, site README, cache-bust token | Six-case portfolio surface now exists locally |
| WK4-003 | done | Codex | Program | Audit Week 4 completion | `WEEK_FOUR_RUNBOOK.md` and `WEEK_FOUR_COMPLETION_AUDIT.md` | Verification and redaction gates recorded |
| WK5-001 | done | Codex | TraderDan | Add client-site case candidate | `case-trader-dan.html` plus homepage card and screenshot | Local Next.js site inspected and public prelaunch hero captured |
| WK5-002 | done | Codex | Strategy Analysis | Add MA-Cross and Large Candle workbench cases | Two case pages plus homepage cards and screenshots | Local Flask apps inspected and public-safe workbench visuals captured |

## Completed Discovery

| Date | Owner | Summary |
|---|---|---|
| 2026-06-16 | Codex + subagents | Initial D: markdown scan found lead candidates: Empire of Drawdown, Job Application Factory, Trades Resource Command Center, Agentic Idea Validation Engine, TA Foundation, Market Data Pipeline, NinjaAccountManager |
| 2026-06-16 | Claude CLI | Drafted Empire of Drawdown packaging brief from README/demo docs |
| 2026-06-16 | Gemini CLI | Drafted Job Application Factory packaging brief from README/user-flow docs |
| 2026-06-16 | Ollama phi4:14b | Drafted local-only Trades Resource Command Center summary from README/plan docs |
| 2026-06-16 | Codex | Verified Agentic Engine tests and local HTTP launch |
| 2026-06-16 | Codex | Verified Trades Resource Dashboard imports, ignored private paths, and safe Streamlit launch |
| 2026-06-16 | Codex | Verified Empire of Drawdown test suite; launch smoke needs follow-up |
| 2026-06-16 | Codex | Verified Job Application Factory key dependency imports |
| 2026-06-16 | Codex | Created static portfolio draft and verified desktop/mobile rendering |
| 2026-06-16 | Codex | Created TA Foundation public demo-slice matrix |
| 2026-06-16 | Codex | Captured Agentic Engine and sanitized Trades Resource screenshots and wired them into the portfolio |
| 2026-06-16 | Codex | Fixed Empire dev launch and captured screenshot |
| 2026-06-16 | Codex | Captured JAF screenshot in safe Mock Demo Mode with temporary data directory |
| 2026-06-16 | Codex | Re-verified portfolio render with four screenshots: no missing images or overflow |
| 2026-06-16 | Codex | Added five individual case-study pages and verified desktop/mobile rendering plus resume PDF link |
| 2026-06-16 | Codex | Added site README and Week One Delivery Summary |
| 2026-06-16 | Codex | Added interview talking points and public redaction review; re-verified site after cropping Trades screenshot |
| 2026-06-16 | Codex | Generated sanitized TA Foundation visual, wired it into the site, and re-verified desktop/mobile rendering |
| 2026-06-16 | Codex | Captured Empire Battle Replay and Debrief screenshots, added them to the case page, and re-verified desktop/mobile rendering |
| 2026-06-16 | Codex | Rewrote Git history to a single clean commit and added Week 2 deployment/contact work |
| 2026-06-17 | Codex | Verified JAF generated packages use fictional demo data and added the proof visual to the case page |
| 2026-06-17 | Codex | Drafted outreach package for recruiter/hiring-manager sharing and updated homepage Week 2 footer |
| 2026-06-17 | Codex + Banach | Added TA Foundation sanitized report proof board from generated report artifacts |
| 2026-06-17 | Codex + Aquinas | Chose NinjaAccountManager as the sixth-case candidate, pending mocked demo capture |
| 2026-06-17 | Codex | Added Week 2 completion audit and deferred Empire video/custom domain until live deploy is current |
| 2026-06-17 | Codex | Published and verified GitHub Pages live portfolio at `https://nogor-design.github.io/portfolio-showcase/` |
| 2026-06-17 | Codex + Claude + Gemini + Ollama + Socrates + Helmholtz | Completed Week 3 PM cycle: public-site polish, outreach angles, redaction gate, and sixth-case deferral decision |
| 2026-06-17 | Codex | Completed Week 4 sixth-case package: NinjaAccountManager public page, synthetic dashboard/strategy visuals, PM runbook, and verification audit |
| 2026-06-17 | Codex | Added Week 5 candidate expansion: TraderDan client site, MA-Cross Workbench, and Large Candle Excursion Studio |

## Delegation Prompt Pattern

Use this shape for external workers:

```text
You are contributing to Eric Irwin's one-week portfolio build. Work only on the named project and produce the requested artifact. Do not expose private customer data, trading account data, secrets, or proprietary strategy parameters. Use concise Markdown with sections: Portfolio Story, What It Proves, Demo Surface, Screenshots Needed, Risks/Redactions, Case Study Outline.
```
