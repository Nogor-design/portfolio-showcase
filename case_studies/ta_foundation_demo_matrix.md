# TA Foundation Demo Matrix

Status: draft demo matrix  
Source: `D:\Backup\projects\PythonProject\ta_foundation` docs read on 2026-06-16  
Public posture: architecture and sanitized artifacts only

## Portfolio Story

TA Foundation is a large trading analytics and automation ecosystem. For the portfolio, it should not be presented as one giant project. It should be carved into focused demos that prove distinct engineering strengths:

- report generation from messy external exports
- strategy discovery and validation
- optimizer orchestration
- deterministic package review
- market-data quality analysis
- local research intake
- execution-adjacent integration boundaries

## Public Positioning

Use language like:

> A local trading research and analytics platform that ingests NinjaTrader exports, market data, and research artifacts, then produces auditable reports, optimizer decision packages, and validation workflows.

Avoid language that implies:

- live trading advice
- guaranteed profitability
- deployable public strategies
- account-specific execution
- proprietary template names or exact edge rules

## Demo Slices

| Slice | Public Story | Evidence Docs / Entry Points | Demo Artifact | Maturity | Redaction Rules | Portfolio Priority |
|---|---|---|---|---|---|---|
| Backtest Intelligence Reports | NinjaTrader backtest exports become executive HTML reports with KPIs, daily outcomes, drawdown, settings, and cards | `docs/CAPABILITY_CATALOG.md`; `python -m ta_foundation.cli.main`; `docs/GETTING_STARTED.md`; `CLAUDE.md` | Sanitized HTML report screenshots: KPI cards, daily leaderboard, drawdown, settings table | Shipped | Hide strategy names, parameter values, trade IDs, account data, and local export paths | High |
| Strategy Discovery Workbench | Backtests and market data are turned into ranked candidate strategies with validation and template evidence | `analysis/strategy_discovery/orchestrator.py`; `strategy_discovery:` YAML; `strategy_discovery_full` report preset | Ranked candidate table, MAE/MFE, OOS/holdout, entry/filter/exit evidence | Shipped | Hide exact rules, thresholds, parameter ranges, and generated template specs | High |
| Weekly Coverage Optimizer Package | A multi-stage optimizer builds a diversified weekly package and final review surface | Web `/optimizer/weekly-coverage`; `web/optimizer_weekly_coverage_package.py`; weekly runbooks | Lane-grid package, final review, package report, manifest overview | Shipped, operationally complex | Redact template names, fitness thresholds, package manifests, and naming logic | High, use canned artifacts |
| Deployment Matrix 252 | Fixed strategy-template pool organizes deployment candidates across sessions, tiers, and axes | Web `/optimizer/deployment-matrix`; `web/optimizer_deployment_matrix*.py`; `docs/designs/deployment_matrix_252_capability.md` | Matrix grid, manifest summary, fallback/coverage explanation | Engine + manifest + launcher done; live-smoked | Hide canonical template names and allocation logic | Medium-high |
| Exit Policy / Stop Engine Lab | Stop and trailing policies are compared using tick-path evidence and validated engine behavior | `analysis/exits/*`; `reports/html/sections/exit_policy_simulation.py`; `docs/runbooks/pantheon_stop_engine_and_test_harness.md` | Exit policy comparison table, trade debug view, stop engine validation note | Shipped; stop engine live-validated 2026-06-11 per catalog | Hide real trade times, prices, and strategy-specific stop heuristics | High |
| Market Data Diagnostics | Market data freshness and tick/minute quality are audited before analysis is trusted | `marketdata/*`; `market_data_dashboard.py`; `tick_data_diagnostics` section | File freshness dashboard, tick stream row counts, bad-minute diagnostics | Shipped | Hide local data roots, broker filenames, account metadata, and contract inventory if sensitive | Medium |
| Large Candle Excursion Study | Large candles are studied by timeframe, session, size bucket, continuation/reversal outcomes, and target curves | `analysis/large_candle_excursion/*`; `large_candle_excursion*` report sections | Target curves, event studies, continuation/reversal result tables | Implemented analysis surface | Hide validated thresholds and strategy blueprint exports | Medium |
| Research Intake To Hypothesis Ledger | Cited external research is converted into reviewable local hypotheses and guarded authoring artifacts | External `D:\local-deep-research`; `research_intake/ldr.py`; `import_ldr.py`; `author_from_intake.py` | Architecture diagram plus sanitized intake artifact | Wired, use canned demo | Remove prompt traces, ledger IDs, rejected hypotheses, proprietary citations | Medium |
| Prediction / Horizon Reports | Daily and horizon prediction artifacts summarize market context, scoring, and horizon behavior | `ta_foundation.prediction.*`; `horizon_overview`; `D:\DailyAnalysis` for context | Horizon overview screenshot, daily context report excerpt | Shipped prediction; DailyAnalysis functional | Hide live lineup, model scores, recent trade recommendations | Medium |
| Execution Bridge Boundary | Strategy signals and runtime messages are sent/monitored through a NinjaTrader-facing bridge | `strategies/TaFoundationExecutionBridge/*`; `cli/bridge_operator.py`; `D:\NinjaAccountManager` | Architecture diagram, signal contract excerpt, mocked state flow | Shipped bridge; live account manager working early | Never show live account, order, balance, position, or broker identifiers | Medium |

## Strongest First Public Set

For the first portfolio site, use these as public cards or sub-sections:

1. Backtest Intelligence Reports
2. Strategy Discovery Workbench
3. Weekly Coverage Optimizer Package
4. Exit Policy / Stop Engine Lab
5. Market Data Diagnostics

These show breadth without requiring live NinjaTrader or account connectivity in a public demo.

## Screenshot / Artifact Checklist

| Artifact | Source | Public Handling |
|---|---|---|
| Executive report KPI cards | Generated HTML report | Use sanitized historical/demo data |
| Daily or weekly leaderboard | Generated HTML report | Hide strategy names if proprietary |
| Strategy discovery table | Strategy discovery report | Blur rules and parameters |
| Weekly coverage final review | Canned weekly package | Show structure, not template identities |
| Exit-policy comparison | Report section | Use generic run labels |
| Market data diagnostics | Dashboard/report | Hide local roots and broker filenames |
| System pipeline diagram | `EXTERNAL_PROJECTS_MAP.md` | Replace local paths with repo/product names |

## Safety Copy For Public Page

Suggested note:

> Trading-related case studies are shown as software engineering and analytics systems. Public demos use sanitized or generated artifacts and omit proprietary strategy rules, account data, broker identifiers, and live trading recommendations.

## Next Verification Tasks

1. Find or generate one sanitized report artifact for Backtest Intelligence.
2. Find a safe strategy discovery report or build a small fixture-based one.
3. Reuse the latest weekly coverage package only after redaction review.
4. Capture a market-data diagnostics screenshot with local paths hidden.
5. Build one diagram that maps research -> discovery -> optimization -> package -> shadow/execution boundary.

