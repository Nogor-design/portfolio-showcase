# Eric Irwin Portfolio Site

Static portfolio draft for Week 1.

## Open Locally

From `D:\a1-program-manager\site`:

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

## Included Media

| File | Source / Safety |
|---|---|
| `media/empire-of-drawdown.png` | Captured from demo-mode local app |
| `media/job-application-factory.png` | Captured with temporary `JAF_DATA_DIR` and Mock Demo Mode active |
| `media/trades-resource-dashboard.png` | Captured from sanitized runtime copy with demo data and no admin pages visible |
| `media/agentic-engine-dashboard.png` | Captured from seeded local dashboard |
| `media/portfolio-home-draft.png` | Full-page screenshot of the current homepage |
| `Eric_Irwin_AI_Software_Engineer_Lead_Resume.pdf` | Resume copied into site package so static server can serve it |

## Verification

Latest verification checked:

- Homepage returns HTTP 200.
- Resume PDF returns HTTP 200.
- Homepage and case-study pages render without horizontal overflow at desktop width.
- Homepage, Empire case study, and TA Foundation case study render without horizontal overflow at 390px mobile width.
- Images load with nonzero dimensions and alt text.

## Remaining Polish

- Capture deeper Empire Battle Replay and Debrief screenshots.
- Add sanitized TA Foundation report screenshots.
- Add one more systems/backend case study if desired: Market Data Pipeline or NinjaAccountManager.
- Decide final deployment target.
- Add real contact links when ready.

