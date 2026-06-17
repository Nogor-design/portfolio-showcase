# Sixth Case Study Decision

Status: decided and re-checked for Week 3
Date: 2026-06-17

## Decision

Pick `NinjaAccountManager` if the portfolio adds a sixth case study.

Do not add it to the public site until a mocked WebSocket/account/order demo has been captured and redacted.

Week 3 re-check: a read-only worker found the sibling project at `D:\NinjaAccountManager`, but no existing public-safe mocked demo runner or screenshot package. The sixth case remains deferred until that harness exists.

## Why NinjaAccountManager Wins

`NinjaAccountManager` adds a capability signal the current five cases do not strongly show: desktop/runtime integration with a NinjaTrader-facing WebSocket bridge, account/order monitoring, a DearPyGUI dashboard, and a localhost strategy API.

`Market Data Pipeline` is useful, but it overlaps more heavily with the TA Foundation data/reporting story. It is better as supporting evidence for TA Foundation unless the portfolio needs a dedicated data-engineering case.

## Public-Safe Packaging Direction

Use only mocked data:

- fake account names
- fake order IDs
- simulated WebSocket events
- no real account state payloads
- no logs from live runs
- no strategy order-routing parameters

## Recommended Demo Surface

1. Launch the desktop app against a mocked WebSocket event stream.
2. Capture the DearPyGUI account monitor with fake balances, positions, and order state.
3. Add a short case page focused on runtime integration, not live trading.
4. Keep the case framed as software engineering: event bus, WebSocket protocol, desktop UI, API boundary, and safety gates.

## Week 3 Safe-Demo Gate

Before publishing this case, create a demo mode that:

- starts without a NinjaTrader connection
- seeds fake account, position, order, market-data, and strategy snapshot state
- avoids writing live bridge or order logs
- hides or renames account, instrument, strategy, signal, stop/target, and route controls
- produces at least two screenshots: Dashboard plus Strategy/runtime console

## Deferred Candidate

`Market Data Pipeline` remains a Tier 2 supporting case for:

- async ingestion
- Parquet/CSV storage
- DuckDB analytics
- FastAPI docs
- gap detection
- idempotent data quality checks

Use it later if the portfolio needs a stronger data-platform story.
