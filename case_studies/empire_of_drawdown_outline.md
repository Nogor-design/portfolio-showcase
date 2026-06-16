# Empire Of Drawdown - Portfolio Packaging Brief

Source worker: Claude CLI  
Reviewed by: Codex PM  
Status: draft outline

## Portfolio Story

Empire of Drawdown is a browser-based strategy game that turns prop-firm and futures-trading mechanics into a commander campaign. Under the themed layer, it is a layered TypeScript monorepo with:

- deterministic historical replay
- reusable strategy execution logic
- game-domain progression rules
- Fastify API orchestration
- React/Vite/Tailwind web UI

The portfolio hook is that the playful surface demonstrates serious engineering discipline: boundaries, deterministic replay, seeded scenarios, and an explicit distinction between real simulation infrastructure and intentionally stubbed live-trading connectivity.

## What It Proves

- TypeScript monorepo architecture
- Clean separation of simulator, strategy engine, game domain, API, and UI
- Deterministic replay and testability
- Product thinking around demo scenarios
- UX storytelling for complex technical systems
- Honest scoping around what is real versus intentionally not connected

## Demo Surface

Primary browser flow:

1. Commander Hall
2. War Table
3. Battle Replay
4. Debrief Chamber
5. Session History / Session Detail

Recommended demo paths:

- Full create-to-debrief happy path
- Seeded Prop-vs-Standard scenario comparison

## Screenshots Needed

1. Commander Hall with seeded demo scenarios
2. War Table with faction, relics, and session selected
3. Battle Replay mid-playback with candle chart, trade markers, and event feed
4. Debrief Chamber with campaign result and battle outcomes
5. Session History or Session Detail showing analytics/persistence
6. Architecture diagram of monorepo layers
7. Optional short GIF of Play -> markers -> Debrief

## Risks And Redactions

- Do not publish `.env` or local runtime credentials.
- Genericize local database connection strings from docs before public posting.
- Add a visible note that this is a game/simulation, not financial advice or live brokerage software.
- Avoid implying a formal NinjaTrader partnership or live integration.
- Review design PDFs and scratch directories before using public screenshots or repo links.

## Case Study Outline

1. Hook: a trading-strategy game that reveals serious trading-infrastructure architecture.
2. Problem: complex strategy/replay systems are hard to inspect and explain.
3. Solution: use a game layer to make replay, risk, outcomes, and trade behavior understandable.
4. Architecture: simulator -> strategy engine -> game domain -> API -> web.
5. Deterministic replay: fixed backend snapshots, charted playback, reproducible debriefs.
6. Product demo: seeded Prop and Standard scenarios.
7. Engineering restraint: clear real-vs-stub boundaries.
8. Next steps: durable replay events, richer account modes, optional external execution seam.

## One-Week Packaging Tasks

1. Boot demo mode and verify happy path.
2. Capture five core screenshots and one short GIF/video.
3. Create a clean architecture diagram.
4. Add or polish a public disclaimer around simulation boundaries.
5. Draft final case study page.
6. Verify cold-start demo commands.

