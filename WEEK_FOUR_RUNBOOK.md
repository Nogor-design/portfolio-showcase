# Week Four Runbook

Status: complete for sixth-case public-safe package  
Start date: 2026-06-17

## Week Four Goal

Open the sixth-case gate by packaging `NinjaAccountManager` as a public-safe
desktop/runtime integration case without exposing live account data, order
history, strategy parameters, logs, or local private paths.

## Work Completed

- Re-inspected the sibling `D:\NinjaAccountManager` source for portfolio-safe
  evidence: WebSocket entry point, AppState store, dashboard panel, strategy
  console, direct strategy API tests, and live-smoke tooling.
- Added `tools/generate_ninja_account_manager_mockups.py` to create reproducible
  public-safe mock captures.
- Generated:
  - `site/media/ninja-account-manager-dashboard.png`
  - `site/media/ninja-account-manager-strategy.png`
- Added `site/case-ninja-account-manager.html`.
- Updated the homepage to show six case studies and a NinjaAccountManager proof
  card.
- Updated the site README, task ledger, next actions, and sixth-case decision.

## Acceptance Criteria

- Sixth case is visible on the homepage and has a linked detail page.
- Public visuals are explicitly synthetic and use fake accounts, fake orders,
  fake market data, and simulated runtime events.
- Site copy frames the case as software engineering/runtime integration, not as
  trading recommendations.
- Static pages use the Week 4 stylesheet token.
- Verification confirms all pages load, images have dimensions and alt text,
  no horizontal overflow appears, and redaction scans do not find sensitive
  local/runtime markers.

## Deferred Work

- Add a real in-repo mocked app runner to `D:\NinjaAccountManager`.
- Capture true DearPyGUI screenshots from that mocked runner.
- Publish the refreshed Week 4 package to GitHub Pages and optional Netlify.
