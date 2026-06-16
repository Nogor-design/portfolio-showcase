# Job Application Factory - Portfolio Packaging Brief

Source worker: Gemini CLI  
Reviewed by: Codex PM  
Status: draft outline

## Portfolio Story

Job Application Factory is a local-first AI career copilot. It uses RAG, local LLMs, and a multi-agent generation pipeline to create personalized job-application packages from approved evidence instead of inventing generic resume claims.

The strongest public story is not "AI writes a resume." It is "AI drafts only from verified evidence, then a critic loop checks for unsupported claims before anything is exported."

## What It Proves

- Local-first AI application design
- RAG-grounded evidence library
- Multi-agent orchestration and critic loops
- Streamlit product UI
- Job discovery and semantic scoring
- Document generation and package export
- Practical automation for a real personal/business workflow

## Demo Surface

Primary demo mode:

- Streamlit mock demo mode
- Job discovery inbox
- Approve-and-generate package flow
- Evidence selection
- Critic/self-correction loop
- Typeset resume or cover-letter preview
- Application tracker or job landing strategy flow

## Screenshots Needed

1. Onboarding or persona setup
2. Job discovery inbox with match scores
3. Package-generation workflow
4. Critic loop / validation output
5. Evidence library or approved bullet selector
6. Rendered PDF/resume/cover-letter preview
7. Optional GitHub portfolio auditor
8. Optional mock interview / strategy copilot

## Risks And Redactions

- Use mock demo mode only for public screenshots.
- Do not publish real resume, contact info, application history, job targets, or personal databases.
- Confirm `.env`, API keys, data folders, generated packages, and personal files are ignored.
- If using generated PDFs, ensure every identity/company/person is fictional or intentionally public.
- Avoid overstating ATS guarantees; frame as strategic positioning and evidence-grounded generation.

## Case Study Outline

1. Problem: generic AI application tools create shallow, risky, unsupported claims.
2. Solution: a local-first application factory grounded in approved evidence.
3. Architecture: job inbox, evidence store, vector retrieval, generation agents, critic loop, export.
4. Workflow: onboard -> score job -> approve package -> validate claims -> export.
5. Safety: local data, mock mode, banned-claim checks, self-correction.
6. Outcome: faster tailored applications without losing truthfulness.

## One-Week Packaging Tasks

1. Verify mock demo mode runs end-to-end.
2. Capture screenshots for the generation and critic loop.
3. Generate 1-2 fully fictional sample packages.
4. Audit data/privacy boundaries.
5. Draft final case study.
6. Decide whether repo should be public, private, or shown through screenshots only.

