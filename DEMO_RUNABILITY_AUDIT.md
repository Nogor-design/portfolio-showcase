# Demo Runability Audit

Status: initial read-only audit  
Date: 2026-06-16

## Portfolio Site Verification

- Static site created under `D:\a1-program-manager\site`.
- Temporary local server on `http://127.0.0.1:8787/` returned HTTP 200.
- Browser desktop check passed:
  - Title: `Eric Irwin | AI Software Engineer Portfolio`
  - Five case-study cards rendered.
  - Four proof cards rendered.
  - No missing images.
  - No horizontal overflow.
  - No console warnings/errors.
- Browser mobile check at 390px width passed:
  - No horizontal overflow.
  - Buttons fit parent containers.
  - Topbar stacks vertically.
- Full-page draft screenshot saved at `site/media/portfolio-home-draft.png`.
- Portfolio page now includes real local screenshots for:
  - Empire of Drawdown: `site/media/empire-of-drawdown.png`
  - Job Application Factory: `site/media/job-application-factory.png`
  - Agentic Engine: `site/media/agentic-engine-dashboard.png`
  - Trades Resource Dashboard: `site/media/trades-resource-dashboard.png`
  - TA Foundation sanitized system visual: `site/media/ta-foundation-suite.png`
- Re-verification after adding images passed:
  - Four images loaded with nonzero dimensions.
  - No missing images.
  - No horizontal overflow.
  - No console warnings/errors.
- Final headless render verification:
  - `cards=5`
  - `proofCards=4`
  - `imageCount=4`
  - `missingImages=0`
  - `overflow=False`
  - Updated full-page screenshot saved at `site/media/portfolio-home-draft.png`.
- Browser re-verification after adding TA Foundation visual:
  - Homepage image count: 5.
  - All six public pages rendered with expected title/H1.
  - No missing images or alt text.
  - No desktop horizontal overflow.
  - Mobile checks at 390px passed for homepage, TA Foundation, and Empire.
  - Updated full-page screenshot saved at `site/media/portfolio-home-draft.png`.
- Browser re-verification after adding Empire media strip and stylesheet cache-bust:
  - Empire case page image count: 3.
  - No missing images or alt text.
  - No desktop horizontal overflow.
  - Mobile checks at 390px passed for homepage, Empire, and TA Foundation.
  - Updated full-page screenshot saved at `site/media/portfolio-home-draft.png`.
- Week 2 local verification after deployment/contact updates:
  - Homepage contact links present: email, GitHub, and resume.
  - Homepage image count: 5.
  - Empire case page image count: 3.
  - TA Foundation case page image count: 1.
  - No missing images or alt text on checked pages.
  - No desktop horizontal overflow.
  - Mobile checks at 390px passed for homepage, Empire, and TA Foundation.
  - Browser console warning/error check returned empty.
  - Full-page screenshot refresh timed out in the browser tool; layout/media checks still passed.
- Week 2 JAF package proof verification:
  - The app's demo generator produced a package under an ignored temporary `JAF_DATA_DIR`.
  - Generated package identity markers were fictional/demo only: Alex Builder, VibeTech, example.com contact data, and Demo Mode labels.
  - Scan found no personal identity markers, local paths, known private project names, or secret-like values from the checked terms.
  - Public proof visual saved at `site/media/jaf-package-proof.png` and added to the Job Application Factory case page.
  - Local browser verification after wiring:
    - Homepage image count: 5.
    - JAF case page image count: 2.
    - JAF proof image loaded at desktop width with nonzero dimensions.
    - No missing images or alt text on checked pages.
    - No desktop horizontal overflow.
    - Mobile checks at 390px passed for homepage, JAF, Empire, and TA Foundation.
    - Browser console warning/error check returned empty.
    - Static asset parser found no missing image files or missing alt text.
- Individual case-study page verification:
  - Pages added for Empire of Drawdown, Job Application Factory, Trades Resource, Agentic Engine, and TA Foundation.
  - All six static pages returned expected title/H1 content in headless browser checks.
  - All images on detail pages loaded with nonzero dimensions and alt text.
  - No desktop horizontal overflow detected on any static page.
  - Mobile checks at 390px width passed for homepage, Empire, and TA Foundation.
  - Resume PDF copied into `site/` and served with HTTP 200.
  - Re-verified after cropping Trades screenshot:
    - All six pages rendered.
    - All image dimensions nonzero.
    - All images have alt text.
    - No horizontal overflow.
    - Resume PDF served with HTTP 200.
  - Public redaction scan found only documentation-local paths/instructions and explicit redaction-note terms; no exposed secret values.

## Summary

The first four lead case studies all have plausible local demo paths. The next step is to run them one at a time, capture setup friction, and decide whether each should be live-demo, recorded-demo, or screenshot-only for the portfolio.

## Lead Demo Candidates

| Project | Path | Runtime Shape | First Run Command | Demo Risk | Current Recommendation |
|---|---|---|---|---|---|
| Empire of Drawdown | `D:\Projects\EmpireOfDrawdown` | Node monorepo: Fastify API + React/Vite web | `npm.cmd run dev:api` and `npm.cmd run dev:web` | Medium: Node/Postgres/Prisma complexity, but demo mode should reduce DB need | Launch first as visual flagship |
| Job Application Factory | `D:\JobApplicationFactory` | Python 3.12+ Streamlit app | `python -m streamlit run app/main.py` | Medium: dependencies and local data/privacy boundaries | Use mock demo mode only |
| Trades Resource Dashboard | `D:\trades-resource-dashboard` | Python Streamlit app | `python -m streamlit run app.py` | Low-medium: dependencies simple; customer data must stay hidden | Use generated demo data |
| Agentic Idea Validation Engine | `D:\agentic-engine` | Python stdlib HTTP + SQLite | `python -m app.backend.main` | Low: no external Python dependencies | Easy live demo candidate |

## Dependency Notes

### Empire of Drawdown

- Root `package.json` includes:
  - `dev:api`
  - `dev:web`
  - `build`
  - `typecheck`
  - `lint`
  - `test`
  - Prisma helpers
- Readme says seeded demo scenarios exist.
- 2026-06-16 verification:
  - Node `v24.14.0` and npm `11.12.0` are available.
  - `node_modules` exists.
  - `.env` and `.env.example` both exist; do not print `.env`.
  - `npm.cmd test` passed: 41 test files passed, 169 tests passed, 8 skipped.
  - First API/web launch attempt was inconclusive. Vite was left running by the timed-out job and was stopped.
  - Corrected launch using default repo scripts succeeded:
    - API `/api/demo/content` returned HTTP 200.
    - Vite web root returned HTTP 200.
    - Logs showed API listening on `127.0.0.1:3001` and Vite on `localhost:5173`.
  - Screenshot saved at `site/media/empire-of-drawdown.png`.
  - Seeded demo loaded successfully into Battle Replay.
  - Battle Replay screenshot saved at `site/media/empire-battle-replay.png`.
  - Debrief Chamber screenshot saved at `site/media/empire-debrief.png`.
  - Empire case page now includes both deeper demo screenshots.
- Audit needed:
  - Optional: capture a short video walkthrough if the portfolio needs motion.

### Job Application Factory

- `pyproject.toml` requires Python >= 3.12.
- Streamlit entry exists at `app/main.py`.
- Dependencies include Streamlit, LanceDB, sentence-transformers, Playwright, Ollama, Anthropic, SQLAlchemy, and document tooling.
- 2026-06-16 verification:
  - Key imports succeeded in the current environment: Streamlit, Pydantic, SQLAlchemy, LanceDB, sentence-transformers, Ollama, Anthropic, Playwright, pypdf, and python-docx.
  - Launched with temporary `JAF_DATA_DIR` under `demo_runtimes/jaf-data`.
  - Mock Demo Mode was toggled on in the browser.
  - Verified safe demo indicators:
    - `Demo Mode Active=True`
    - `Alex Builder=True`
    - `Live Mode Active=False`
    - `personal profile=False`
  - Screenshot saved at `site/media/job-application-factory.png`.
- Audit needed:
  - Decide whether to keep the proof screenshot as the final JAF artifact or add a short recorded flow later.

### Trades Resource Dashboard

- `requirements.txt` is small:
  - Streamlit
  - pandas
  - plotly
  - numpy
  - openpyxl
  - pypdf
- Entry exists at `app.py`.
- 2026-06-16 verification:
  - Required Python imports are available in the current environment.
  - `.streamlit/secrets.toml`, `runtime_uploads/`, `runtime_sessions/`, and `runtime_exports/` are ignored by Git.
  - Local secrets contain an owner/admin-related flag, so screenshot sessions must force safe demo settings through environment variables.
  - Temporary Streamlit launch on port `8503` returned health HTTP 200 and home HTTP 200.
  - Server process was stopped after smoke test.
  - Initial screenshot attempt against the original repo was rejected as public unsafe because local secrets surfaced owner/admin mode.
  - A sanitized temporary runtime was created under `demo_runtimes/trades-resource-dashboard-safe` with only `app.py`, `src`, `data`, and `requirements.txt`.
  - Sanitized runtime on port `8505` confirmed:
    - `Owner/admin tools are enabled=False`
    - `Demo Data=True`
    - `Client Demo Mode=True`
    - `Full Prototype Mode=False`
    - `Data / Admin=False`
  - Public-safe screenshot saved at `site/media/trades-resource-dashboard.png`.
- Audit needed:
  - Confirm owner/admin secrets do not reveal private controls in screenshots.
  - Confirm runtime/customer upload folders remain ignored.

### Agentic Idea Validation Engine

- `pyproject.toml` declares no runtime dependencies.
- Entry exists at `app/backend/main.py`.
- Readme claims `python -m unittest discover tests` should pass.
- 2026-06-16 verification:
  - `python -m unittest discover tests` passed: 51 tests.
  - Temporary launch on `http://127.0.0.1:8765` returned HTTP 200.
  - Server process was stopped after smoke test.
  - Seeded dashboard screenshot saved at `site/media/agentic-engine-dashboard.png`.
- Audit needed:
  - Seed portfolio-relevant demo ideas if needed.

### TA Foundation

- 2026-06-16 verification:
  - Existing runbook screenshots were reviewed and not reused directly because they exposed local artifact paths and strategy/template labels.
  - A sanitized dashboard-style visual was generated instead at `site/media/ta-foundation-suite.png`.
  - The visual shows pipeline, capability signals, and weekly coverage matrix structure without account data, broker identifiers, local paths, or proprietary strategy rules.
  - The visual is wired into the homepage and TA Foundation detail page.
- 2026-06-17 verification:
  - Generated report-suite index inspected at `ExampleWeeklyReport/index.html`.
  - Weekly coverage package summary inspected at `operationally_diverse_weekly_coverage_package_report.html`.
  - Raw weekly manifest rows were rejected for public use because they include template names, parameters, PnL rows, and local paths.
  - Sanitized report proof board generated at `site/media/ta-weekly-report-suite.png`.
  - TA Foundation detail page now includes the report proof board.
  - Local browser verification after wiring:
    - Homepage footer now shows Week 2 status.
    - TA Foundation case page image count: 2.
    - TA report proof image loaded with nonzero dimensions.
    - No missing images or alt text on checked pages.
    - No desktop horizontal overflow.
    - Mobile checks at 390px passed for homepage, TA Foundation, JAF, and Empire.
    - Browser console warning/error check returned empty.
- Audit needed:
  - Optional: capture a more polished cropped screenshot later from a sanitized report copy, but do not publish raw report HTML.

## Next Launch Order

1. Empire of Drawdown: tests verified; repeat launch smoke test with corrected command.
2. Job Application Factory: AI/RAG demo after dependency/privacy audit.
3. Agentic Engine: verified runnable; next step is screenshots.
4. Trades Resource Dashboard: verified runnable; next step is screenshots under forced demo settings.

## Decision Criteria

| Demo Type | Criteria |
|---|---|
| Live demo | Starts reliably in under 5 minutes with no private data |
| Recorded demo | Visually strong but setup is fragile or multi-process |
| Screenshot-only | Valuable system, but live run depends on private data, credentials, or heavy setup |
