# Public Redaction Review

Date: 2026-06-16  
Scope: `D:\a1-program-manager\site`

## Current Public-Site Review

The static site was scanned for obvious private-path, secret, and sensitive-data leakage.

Search terms included:

- Windows paths: `D:\`, `C:\`
- secret indicators: `.env`, `secrets.toml`, `API_KEY`, `PASSWORD`, `TOKEN`
- local runtime indicators: `localhost`, `127.0.0.1`
- admin-mode indicators: `Owner/admin tools are enabled`, `ENABLE_OWNER_ADMIN_TOOLS`, `BYPASS_DEMO_LOGIN`
- basic contact markers: `phone`, `email`, `@`

## Findings

| Finding | Status | Notes |
|---|---|---|
| `site/README.md` includes local-open instructions | Acceptable | Local machine path removed; loopback URL remains as local instructions |
| `case-job-application-factory.html` mentions `.env` in a redaction note | Acceptable | It does not expose values |
| `case-trades-resource.html` mentions phone/email in a redaction note | Acceptable | It says those are excluded |
| CSS contains `@media` | Not sensitive | Search hit only |
| Trades screenshot initially showed login bypass warning | Fixed | Cropped to main dashboard content |
| Final scan after TA visual and Empire media | Acceptable | Hits are intentional redaction-note language plus local-open instructions |
| Public contact links | Acceptable | Email and GitHub are already present in the public resume and are now intentionally linked |
| Local path scan after Week 2 kickoff | Acceptable | No `D:\a1-program-manager` path remains in the published `site/` files |
| JAF package proof scan | Acceptable | Generated proof uses fictional Alex Builder/VibeTech package data and no checked private markers |

## Public-Safe Screenshots

| Screenshot | Status |
|---|---|
| `media/empire-of-drawdown.png` | Safe for draft; shows demo product surface |
| `media/empire-battle-replay.png` | Safe for draft; seeded demo replay surface with simulator account label only |
| `media/empire-debrief.png` | Safe for draft; seeded demo debrief surface with simulator account label only |
| `media/job-application-factory.png` | Safe for draft; Mock Demo Mode active with fictional profile |
| `media/jaf-package-proof.png` | Safe for draft; generated from fictional Alex Builder/VibeTech demo package |
| `media/trades-resource-dashboard.png` | Safe for draft after crop; generated demo data only |
| `media/agentic-engine-dashboard.png` | Safe for draft; seeded demo dashboard |
| `media/ta-foundation-suite.png` | Safe for draft; generated sanitized system visual with no local paths, accounts, broker IDs, or proprietary strategy rules |
| `media/ta-weekly-report-suite.png` | Safe for draft; sanitized proof board derived from report artifacts, with raw manifest rows withheld |

## Before Publishing

1. Review every screenshot at full size.
2. Keep `site/README.md` local-open instructions generic if it remains published.
3. Confirm final contact links intentionally before broad sharing.
4. Confirm resume PDF is the version intended for public distribution.
5. Re-run a redaction scan after any future TA Foundation raw-report screenshots are added.
6. Re-check live Netlify after connecting the repo or manually redeploying from the latest GitHub state.
