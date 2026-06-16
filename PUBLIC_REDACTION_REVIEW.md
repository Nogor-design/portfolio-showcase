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
| `site/README.md` includes local `D:\a1-program-manager\site` and `127.0.0.1` instructions | Acceptable for local package docs | Do not publish this README as marketing copy without editing |
| `case-job-application-factory.html` mentions `.env` in a redaction note | Acceptable | It does not expose values |
| `case-trades-resource.html` mentions phone/email in a redaction note | Acceptable | It says those are excluded |
| CSS contains `@media` | Not sensitive | Search hit only |
| Trades screenshot initially showed login bypass warning | Fixed | Cropped to main dashboard content |
| Final scan after TA visual and Empire media | Acceptable | Hits are intentional redaction-note language plus local-only `site/README.md` open instructions |

## Public-Safe Screenshots

| Screenshot | Status |
|---|---|
| `media/empire-of-drawdown.png` | Safe for draft; shows demo product surface |
| `media/empire-battle-replay.png` | Safe for draft; seeded demo replay surface with simulator account label only |
| `media/empire-debrief.png` | Safe for draft; seeded demo debrief surface with simulator account label only |
| `media/job-application-factory.png` | Safe for draft; Mock Demo Mode active with fictional profile |
| `media/trades-resource-dashboard.png` | Safe for draft after crop; generated demo data only |
| `media/agentic-engine-dashboard.png` | Safe for draft; seeded demo dashboard |
| `media/ta-foundation-suite.png` | Safe for draft; generated sanitized system visual with no local paths, accounts, broker IDs, or proprietary strategy rules |

## Before Publishing

1. Review every screenshot at full size.
2. Remove or edit local-only instructions in `site/README.md` if that file is published.
3. Add final contact links intentionally.
4. Confirm resume PDF is the version intended for public distribution.
5. Re-run a redaction scan after any future TA Foundation report screenshots are added.
