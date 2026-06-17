# Eric Irwin Portfolio Site

Static portfolio package.

## Open Locally

From this `site` directory:

```powershell
python -m http.server 8787 --bind 127.0.0.1
```

Then open:

```text
http://127.0.0.1:8787/
```

## Included Pages

| Page | Purpose |
|---|---|
| `index.html` | Portfolio homepage with featured case studies, proof points, services, and resume link |
| `case-empire-of-drawdown.html` | Trading strategy game / deterministic replay case study |
| `case-job-application-factory.html` | Local-first RAG and multi-agent application factory case study |
| `case-trades-resource.html` | Staffing operations dashboard case study |
| `case-agentic-engine.html` | Local idea validation ledger case study |
| `case-ta-foundation.html` | TA Foundation trading intelligence suite overview |
| `case-ninja-account-manager.html` | Desktop runtime bridge and strategy API integration case study |
| `case-trader-dan.html` | Client-facing Next.js education platform site case study |
| `case-ma-cross-workbench.html` | Moving-average research and cross-instrument proof workbench case study |
| `case-large-candle-studio.html` | Large candle event-study and strategy-construction workbench case study |
| `case-agent-trading-league.html` | Replay-scored trading agent league and bounded learning case study |

## Included Media

| File | Source / Safety |
|---|---|
| `media/empire-of-drawdown.png` | Captured from demo-mode local app |
| `media/empire-battle-replay.png` | Captured from seeded demo Battle Replay |
| `media/empire-debrief.png` | Captured from seeded demo Debrief Chamber |
| `media/job-application-factory.png` | Captured with temporary `JAF_DATA_DIR` and Mock Demo Mode active |
| `media/jaf-package-proof.png` | Generated from the fictional Alex Builder/VibeTech demo package |
| `media/trades-resource-dashboard.png` | Captured from sanitized runtime copy with demo data and no admin pages visible |
| `media/agentic-engine-dashboard.png` | Captured from seeded local dashboard |
| `media/ta-foundation-suite.png` | Generated sanitized TA Foundation architecture/coverage visual |
| `media/ta-weekly-report-suite.png` | Sanitized proof board derived from TA Foundation report-suite and weekly coverage artifacts |
| `media/ninja-account-manager-dashboard.png` | Synthetic NinjaAccountManager dashboard generated from fake account and market-data fixtures |
| `media/ninja-account-manager-strategy.png` | Synthetic NinjaAccountManager strategy console generated from fake runtime and event fixtures |
| `media/trader-dan-home.png` | Captured from local prelaunch TraderDan client site with no private admin/member data visible |
| `media/ma-cross-workbench.png` | Captured from local MA-Cross Workbench after an explorer run |
| `media/large-candle-studio.png` | Captured from local Large Candle Studio with local data-root label cropped out |
| `media/agent-trading-league.png` | Captured from the local League dashboard after cropping out the sidebar path and private runtime context |
| `media/portfolio-home-draft.png` | Full-page screenshot of the current homepage |
| `Eric_Irwin_AI_Software_Engineer_Lead_Resume.pdf` | Resume copied into site package so static server can serve it |

## Verification

Latest verification checked:

- Homepage returns HTTP 200.
- Resume PDF returns HTTP 200.
- Homepage and case-study pages render without horizontal overflow at desktop width.
- Homepage, Empire case study, Job Application Factory case study, and TA Foundation case study render without horizontal overflow at 390px mobile width.
- Images load with nonzero dimensions and alt text.
- Job Application Factory proof visual loads on the case-study page.
- TA Foundation report proof visual loads on the case-study page.
- NinjaAccountManager synthetic dashboard and strategy visuals load on the case-study page.
- TraderDan, MA-Cross, and Large Candle Studio visuals load on their case-study pages.
- Agent Trading League visual loads on the homepage and case-study page.

## Deployment

Supported static deploy paths:

- Netlify: publish directory `site`, configured from the repo root by `netlify.toml`.
- GitHub Pages: workflow at `../.github/workflows/pages.yml` publishes this directory to the `gh-pages` branch.

## Remaining Polish

- Optional: replace synthetic NinjaAccountManager visuals with captured app screenshots after a durable in-repo mock runner exists.
- Optional: add a more polished sanitized TA Foundation report screenshot later.
- Optional: publish the categorized ten-case build after final client/redaction review.
- Confirm live deployment target and custom domain.
