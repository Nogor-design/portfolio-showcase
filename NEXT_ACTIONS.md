# Next Actions

Status as of 2026-06-16 Week 2 kickoff.

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

## Immediate Next Work

1. Confirm generated JAF packages use fictional data before showing package screenshots.
2. Generate or locate true sanitized `ta_foundation` report artifacts beyond the current system visual.
3. Decide whether Market Data Pipeline or NinjaAccountManager becomes the sixth public case study.
4. Add final contact links and deployment target.
5. Consider a short Empire walkthrough video if motion would strengthen the flagship case.

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
