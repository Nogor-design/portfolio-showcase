# Next Actions

Status as of 2026-06-20 Workflow MRI flagship integration.

## Verified So Far

- Claude CLI, Gemini CLI, and Ollama all work headlessly from `D:\a1-program-manager`.
- PM docs exist and are seeded.
- First case-study outlines exist for:
  - `case_studies/empire_of_drawdown_outline.md`
  - `case_studies/job_application_factory_outline.md`
  - `case_studies/trades_resource_dashboard_outline.md`
- Agentic Engine:
  - 51 tests passed.
  - Local HTTP launch returned 200.
  - Screenshot captured at `site/media/agentic-engine-dashboard.png`.
- Trades Resource Dashboard:
  - Dependencies import.
  - Private runtime folders and local secrets are ignored by Git.
  - Sanitized runtime screenshot captured at `site/media/trades-resource-dashboard.png`.
- Empire of Drawdown:
  - 169 tests passed, 8 skipped.
  - API/web launch fixed; screenshot captured at `site/media/empire-of-drawdown.png`.
- Job Application Factory:
  - Key dependencies import successfully.
  - Temporary `JAF_DATA_DIR` used; Mock Demo Mode verified; screenshot captured at `site/media/job-application-factory.png`.
  - Demo package generation verified with fictional Alex Builder/VibeTech data and screenshot captured at `site/media/jaf-package-proof.png`.

## Immediate Next Work

1. Start outreach using `OUTREACH_PACKAGE.md` and the verified GitHub Pages URL after the Workflow MRI publish check passes.
2. Do a human copy pass on the five newest cases before broad client-facing sharing.
3. If Netlify remains desired, reconnect/redeploy it from GitHub or the current `site.zip`; do not share the old stale drag-drop URL.
4. Replace NinjaAccountManager synthetic visuals with captured app screenshots only after a durable mocked app runner exists in the sibling repo.
5. Reconsider an Empire walkthrough video only if reviewer conversations show that motion would materially help.
6. Reconsider a custom domain as optional future polish.

## Added Since Previous Status

- Static portfolio site scaffold created under `site/`.
- Draft screenshot saved at `site/media/portfolio-home-draft.png`.
- Desktop browser verification passed: title, case cards, proof cards, nav, no missing images, no horizontal overflow, no console warnings/errors.
- Mobile browser verification passed at 390px width: no horizontal overflow, buttons fit, topbar stacks correctly.
- `case_studies/ta_foundation_demo_matrix.md` created from current docs.
- Agentic Engine screenshot captured at `site/media/agentic-engine-dashboard.png`.
- Trades Resource screenshot captured from sanitized runtime at `site/media/trades-resource-dashboard.png`.
- Portfolio page now uses the Agentic and Trades screenshots and re-verifies with no missing images or overflow.
- Empire launch fixed; screenshot captured at `site/media/empire-of-drawdown.png`.
- Empire seeded demo loaded; Battle Replay and Debrief screenshots captured at `site/media/empire-battle-replay.png` and `site/media/empire-debrief.png`.
- JAF launched with temporary `JAF_DATA_DIR`; Mock Demo Mode verified; screenshot captured at `site/media/job-application-factory.png`.
- TA Foundation sanitized system visual generated at `site/media/ta-foundation-suite.png` and wired into homepage plus detail page.
- Individual case-study pages added for Empire, JAF, Trades, Agentic Engine, and TA Foundation.
- Resume PDF copied into the static site package and verified over HTTP 200.
- Static page crawl verified titles/H1s, images, alt text, and no desktop overflow across all site pages.
- Mobile checks passed for homepage, Empire case study, and TA Foundation case study.
- `site/README.md` and `WEEK_ONE_DELIVERY_SUMMARY.md` added.
- `INTERVIEW_TALKING_POINTS.md` and `PUBLIC_REDACTION_REVIEW.md` added.
- Trades screenshot cropped to remove the demo-login warning/sidebar and re-verified.
- Final static-site verification passed after crop: all pages render, all images have dimensions and alt text, no horizontal overflow, resume PDF served.
- Re-verified after adding TA Foundation visual:
  - Homepage image count is 5.
  - All six pages render.
  - No missing images or alt text.
  - No desktop horizontal overflow.
  - Mobile checks at 390px passed for homepage, TA Foundation, and Empire.
- Re-verified after adding Empire media strip and stylesheet cache-bust:
  - Empire case page image count is 3.
  - No missing images or alt text.
  - No desktop horizontal overflow.
  - Mobile checks at 390px passed for homepage, Empire, and TA Foundation.
- Week 2 kickoff:
  - Git history was purged to one clean public-safe commit.
  - `netlify.toml` added so Netlify can publish `site/` from GitHub.
  - Homepage contact buttons added for email, GitHub, and resume.
  - Local desktop/mobile verification passed after contact/deployment updates.
  - Live drag-drop Netlify URL still serves the older separator issue until redeployed or connected to GitHub.
- Week 2 proof pass:
  - JAF mock package generation verified from the app's demo generator.
  - Generated package scan found only fictional/demo identity markers and no personal/local/project-sensitive markers.
  - JAF proof visual added at `site/media/jaf-package-proof.png` and wired into the public case study.
  - Local browser verification passed for homepage and JAF case page at desktop width.
  - Mobile checks at 390px passed for homepage, JAF, Empire, and TA Foundation.
  - Static asset parser found no missing image files or missing alt text.
  - Outreach package drafted at `OUTREACH_PACKAGE.md`.
- TA Foundation report proof:
  - `site/media/ta-weekly-report-suite.png` generated from verified report-suite and weekly coverage summary artifacts.
  - Raw TA HTML reports and manifest rows were not copied into the public site.
  - TA case page now includes the sanitized report proof board.
- Sixth case decision:
  - `NinjaAccountManager` chosen if a sixth case study is added because it contributes desktop/runtime/WebSocket integration.
  - `Market Data Pipeline` deferred or folded into TA Foundation because it overlaps with the existing data/reporting story.
- Deployment status:
  - GitHub Pages is live and verified at `https://nogor-design.github.io/portfolio-showcase/`.
  - Latest GitHub commit is pushed, but the current Netlify drag-drop URL still serves the older build.
  - Netlify CLI is available through `npx` but not logged in.
  - Fresh manual redeploy package created at `D:\a1-program-manager\site.zip`.
  - Details recorded in `DEPLOYMENT_STATUS.md`.
  - GitHub Pages branch workflow added to publish `site/` from `master` into `gh-pages`.
  - `gh-pages` branch was pushed manually once from the current site package.
  - Branch-publish workflow completed successfully.
- Completion audit:
  - `WEEK_TWO_COMPLETION_AUDIT.md` records public GitHub Pages completion evidence.
  - Empire video and custom domain are deferred as optional future polish.
- Week 3 PM cycle:
  - Claude CLI, Gemini CLI, Ollama, and Codex subagents were assigned bounded review/discovery tasks.
  - Homepage copy now reflects Week 3 public polish, clearer availability, and public-friendly proof stats.
  - All case pages share the Week 3 stylesheet cache-bust token.
  - Agentic Engine now has a redaction note.
  - `NinjaAccountManager` was found and, at that time, deferred until a mocked demo capture path existed.
  - `WEEK_THREE_RUNBOOK.md`, `WEEK_THREE_COPY_REVIEW.md`, and `WEEK_THREE_COMPLETION_AUDIT.md` preserve the handoff.
- Week 4 sixth-case package:
  - `tools/generate_ninja_account_manager_mockups.py` generates two public-safe synthetic visuals from fake fixtures.
  - `site/media/ninja-account-manager-dashboard.png` and `site/media/ninja-account-manager-strategy.png` were generated.
  - `site/case-ninja-account-manager.html` was added.
  - Homepage now presents six case studies.
  - `WEEK_FOUR_RUNBOOK.md` and `WEEK_FOUR_COMPLETION_AUDIT.md` preserve the handoff.
  - Week 4 commit `4366477` was pushed to `master`.
  - Branch-publish workflow run `27712655651` completed successfully.
  - Live GitHub Pages verification passed for the six-card homepage and NinjaAccountManager case page.
- Week 5 candidate expansion first pass:
  - `D:\trader-dan` inspected as a client-facing Next.js futures education site.
  - `D:\strategy-analysis\ma-cross` inspected as a moving-average research workbench.
  - `D:\strategy-analysis\large-candle` inspected as a large candle event-study workbench.
  - Public-safe visuals captured at:
    - `site/media/trader-dan-home.png`
    - `site/media/ma-cross-workbench.png`
    - `site/media/large-candle-studio.png`
  - Case pages added for TraderDan, MA-Cross Workbench, and Large Candle Excursion Studio.
  - Homepage initially presented nine case studies before the later Agent Trading League/category pass.
  - Expanded commit `086de90` was pushed to `master`.
  - Branch-publish workflow run `27714428021` completed successfully.
  - Live GitHub Pages verification passed for the nine-card homepage and the three new case pages.
- Categorized ten-case expansion:
  - `D:\agent-trading-league` inspected as a replay-scored trading-agent operations dashboard.
  - Local League app health returned 200 and its test suite passed 12 tests.
  - App banner CSS was fixed locally so the hero image no longer dominates the dashboard.
  - Public-safe screenshot captured at `site/media/agent-trading-league.png`.
  - `site/case-agent-trading-league.html` added.
  - Homepage now groups the 10 cases into AI and agent workflows, client and operations platforms, trading research and runtime systems, and simulation systems.
- Creative-AI expansion:
  - `D:\scenario-builder\fate-scenario-weaver` inspected as a Next.js/Prisma/SQLite AI scenario workbench.
  - Source review found staged provider boundaries for mock, Ollama, and CLI-backed generation plus image/PDF export surfaces.
  - `npm run lint` and `npm run build` passed after a small JSX/import cleanup in the source project.
  - A temporary public-safe SQLite database was initialized and seeded at `D:\temp\fate-portfolio-demo.db` with `AI_PROVIDER=mock`.
  - Public-safe screenshot captured at `site/media/fate-scenario-weaver.png`.
  - `site/case-fate-scenario-weaver.html` added.
  - Homepage now presents 11 categorized case studies.
- Workflow MRI flagship integration:
  - `D:\workflow\workflow-mri` inspected and verified as a deterministic static React workbench over fictional Meridian Claims data.
  - Workflow MRI README and roadmap updated to reflect Phase 1 demo status.
  - Workflow MRI web test suite now includes Safe Mode redaction coverage; `npm test`, `npm run build`, and engine `python -m pytest` pass.
  - Public-safe screenshot captured at `site/media/workflow-mri-workbench.png`.
  - `site/case-workflow-mri.html` added.
  - Homepage now promotes Workflow MRI as the first flagship case, with an embedded portfolio-hosted demo and code links.

## Current Local Open Command

```powershell
cd D:\a1-program-manager\site
python -m http.server 8787 --bind 127.0.0.1
```

Open:

```text
http://127.0.0.1:8787/
```

## Important Safety Notes

- Do not use real customer data in screenshots.
- Do not print or publish `.env` or `.streamlit/secrets.toml`.
- For Trades screenshots, force:
  - `ENABLE_OWNER_ADMIN_TOOLS=false`
  - `TRADES_OWNER_ADMIN=false`
  - `ENABLE_LOCAL_CUSTOMER_FILES=false`
  - `BYPASS_DEMO_LOGIN=true`
  - `TRADES_BYPASS_DEMO_LOGIN=true`
- For Empire, use `TSG_RUNTIME_MODE=demo`.
