# Deployment Status

Status: Workflow MRI twelve-case flagship package is live and verified on GitHub Pages
Last checked: 2026-06-20

## Current GitHub State

Repository:

```text
https://github.com/Nogor-design/portfolio-showcase
```

See `git log -1 --oneline` for the current pushed commit.

## Current Live Netlify URL

```text
https://6a31cd1325555e77d846b28f--heroic-gumdrop-ee0c3d.netlify.app/#top
```

Live check result:

- HTTP status: 200
- Week 2 footer present: no
- JAF proof image present: no
- TA report proof image present: no
- Mojibake still present: yes

Conclusion: this URL is still serving the older manual drag-drop deploy, not the latest GitHub state.

## Verified Live GitHub Pages URL

```text
https://nogor-design.github.io/portfolio-showcase/
```

Live check result after Workflow MRI flagship publish:

- HTTP status: 200
- Categorized homepage rendered: yes
- Homepage case-card count: 12
- Homepage category count: 4
- `case-workflow-mri.html` linked from homepage: yes
- Workflow MRI portfolio-hosted live demo linked from homepage: yes
- Workflow MRI case page returns the expected title/H1 and image loads: yes
- Workflow MRI embedded demo returns HTTP 200 and React content loads: yes
- `case-fate-scenario-weaver.html` linked from homepage: yes
- `case-agent-trading-league.html` linked from homepage: yes
- `case-ninja-account-manager.html` linked from homepage: yes
- `case-trader-dan.html` linked from homepage: yes
- `case-ma-cross-workbench.html` linked from homepage: yes
- `case-large-candle-studio.html` linked from homepage: yes
- Fate Scenario Weaver case page returns the expected title/H1 and image loads: yes
- Agent Trading League case page returns the expected title/H1 and image loads: yes
- NinjaAccountManager case page returns the expected title/H1: yes
- NinjaAccountManager page images loaded: yes, 3 images
- TraderDan case page returns the expected title/H1 and images load: yes
- MA-Cross Workbench case page returns the expected title/H1 and images load: yes
- Large Candle Studio case page returns the expected title/H1 and images load: yes
- JAF case page references `jaf-package-proof.png`: yes
- TA case page references `ta-weekly-report-suite.png`: yes
- resume PDF returns HTTP 200: yes
- proof PNGs return HTTP 200: yes
- mojibake present: no

Browser QA result:

- Local desktop and mobile render passed across all 13 site pages before publish.
- Live homepage, Workflow MRI case page, and embedded Workflow MRI demo rendered after publish.
- Live mobile homepage rendered after publish.
- No missing images.
- No missing alt text.
- No horizontal overflow.
- No console warnings/errors.

## Deployment Blocker

Netlify CLI is not globally installed. Running through `npx netlify-cli` works, but Netlify reports:

```text
Not logged in. Please log in to see project status.
```

No `NETLIFY_*` auth token is present in the environment.

GitHub CLI is not installed in this shell, so GitHub Pages cannot be enabled from here through `gh`.

## GitHub Pages Fallback

A GitHub Pages branch-publish workflow now exists at:

```text
.github/workflows/pages.yml
```

It publishes the `site/` directory to the `gh-pages` branch on pushes to `master` and through manual `workflow_dispatch`.

The `gh-pages` branch is updated by the branch-publish workflow. Categorized eleven-case source commit:

```text
4c4adec Add Fate Scenario Weaver portfolio case
```

Verified Pages URL:

```text
https://nogor-design.github.io/portfolio-showcase/
```

The branch-publish workflow completed successfully for the verified eleven-case deploy:

```text
https://github.com/Nogor-design/portfolio-showcase/actions/runs/27716028824
```

The branch-publish workflow completed successfully for the Workflow MRI flagship deploy:

```text
https://github.com/Nogor-design/portfolio-showcase/actions/runs/27885300496
```

## Current Manual Redeploy Package

Latest static package was refreshed after the categorized eleven-case local verification pass at:

```text
D:\a1-program-manager\site.zip
```

This file is intentionally ignored by Git.

Manual Netlify path:

1. Open Netlify.
2. Drag `D:\a1-program-manager\site.zip` or the `D:\a1-program-manager\site` folder into a manual deploy.
3. Re-check the live URL for:
   - `Public portfolio build / Week 5 creative-AI expansion`
   - `case-fate-scenario-weaver.html`
   - `case-agent-trading-league.html`
   - `case-ninja-account-manager.html`
   - `case-trader-dan.html`
   - `case-ma-cross-workbench.html`
   - `case-large-candle-studio.html`
   - `fate-scenario-weaver.png`
   - `agent-trading-league.png`
   - `ninja-account-manager-dashboard.png`
   - `ninja-account-manager-strategy.png`
   - `trader-dan-home.png`
   - `ma-cross-workbench.png`
   - `large-candle-studio.png`
   - `jaf-package-proof.png`
   - `ta-weekly-report-suite.png`
   - no mojibake marker

Preferred durable path:

1. Connect Netlify to `Nogor-design/portfolio-showcase`.
2. Use the existing `netlify.toml`.
3. Confirm publish directory is `site`.
4. Trigger a deploy from `master`.
