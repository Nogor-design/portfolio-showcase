# Week Two Runbook

Status: active  
Start date: 2026-06-16

## Week Two Goal

Turn the Week 1 draft into a public-ready portfolio package that can be shared confidently from GitHub/Netlify and used in interviews or outreach.

## Day 1: Deployment Hardening

Goals:

- Keep GitHub as the source of truth.
- Make Netlify publish the `site/` directory directly from the repo.
- Remove local-only instructions from the published package.
- Verify the live URL after each push.

Deliverables:

- `netlify.toml`
- Clean Git history with only public-safe tracked files
- Deployment notes in this runbook and `NEXT_ACTIONS.md`

## Day 2: Public Contact And Sharing

Goals:

- Add intentional contact links.
- Keep the resume as the detailed contact artifact.
- Make the homepage contact section useful without exposing unnecessary private details.

Deliverables:

- Email link
- GitHub profile link
- Resume link

## Day 3: Stronger Proof Assets

Goals:

- Confirm Job Application Factory generated packages use fictional data before adding package screenshots.
- Add one more TA Foundation artifact only if it can be sanitized safely.
- Decide whether a short Empire walkthrough video is worth the time.

Progress:

- JAF package proof completed from the app's demo generator using fictional Alex Builder/VibeTech data.
- Public visual added at `site/media/jaf-package-proof.png`.
- Remaining proof decision: TA Foundation sanitized report artifact vs. keeping the current system visual, plus optional Empire walkthrough video.

## Day 4: Sixth Case Study Decision

Goals:

- Choose Market Data Pipeline or NinjaAccountManager if the portfolio needs broader systems coverage.
- Avoid adding a sixth case study if it dilutes the five strongest stories.

Decision criteria:

- Public-safe demo surface exists.
- The project adds a genuinely new capability signal.
- It can be explained clearly in under 90 seconds.

## Day 5: Copy Tightening

Goals:

- Rewrite homepage and case-study copy for recruiter clarity.
- Keep trading-related language framed as software engineering and analytics infrastructure.
- Make business workflow value obvious to non-technical readers.

## Day 6: Public QA

Goals:

- Crawl the live site.
- Check images, alt text, resume link, contact links, mobile overflow, and obvious redaction terms.
- Confirm the live deployment is using the latest commit.

## Day 7: Outreach Package

Goals:

- Produce a short share message for recruiters/hiring managers.
- Produce a longer technical walkthrough script.
- Produce an interview demo order.
