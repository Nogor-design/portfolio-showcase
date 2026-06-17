# Deployment Status

Status: GitHub Pages live and verified; old Netlify deploy is stale
Last checked: 2026-06-17

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

Live check result:

- HTTP status: 200
- Week 2 footer present: yes
- JAF case page references `jaf-package-proof.png`: yes
- TA case page references `ta-weekly-report-suite.png`: yes
- resume PDF returns HTTP 200: yes
- proof PNGs return HTTP 200: yes
- mojibake present: no

Browser QA result:

- Desktop render passed for homepage, JAF, TA Foundation, and Empire pages.
- Mobile render at 390px passed for homepage, JAF, TA Foundation, and Empire pages.
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

The `gh-pages` branch has also been pushed manually once from the current site package.

Verified Pages URL:

```text
https://nogor-design.github.io/portfolio-showcase/
```

The branch-publish workflow completed successfully for the verified deploy.

## Current Manual Redeploy Package

Latest static package was refreshed after the Week 3 polish pass at:

```text
D:\a1-program-manager\site.zip
```

This file is intentionally ignored by Git.

Manual Netlify path:

1. Open Netlify.
2. Drag `D:\a1-program-manager\site.zip` or the `D:\a1-program-manager\site` folder into a manual deploy.
3. Re-check the live URL for:
   - `Public portfolio build / Week 2`
   - `jaf-package-proof.png`
   - `ta-weekly-report-suite.png`
   - no mojibake marker

Preferred durable path:

1. Connect Netlify to `Nogor-design/portfolio-showcase`.
2. Use the existing `netlify.toml`.
3. Confirm publish directory is `site`.
4. Trigger a deploy from `master`.
