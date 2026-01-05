# Nomad

Nomad is a planned, safe, and review-first system for migrating legacy codebases across frameworks and languages — without breaking trust, behavior, or teams.
Nomad does not aim for one-click rewrites.
It aims for controlled conversion at scale.

## What Nomad Is

- A migration assistant, not a code generator
- A Git-first system that works through diffs and pull requests
- A tool that understands what a system does, then re-expresses it elsewhere
- A phased platform for:
    - Framework migrations (e.g. Flask → FastAPI)
    - Cross-language migrations (e.g. Java → C#), incrementally

## What Nomad Is NOT

- Not a “rewrite everything automatically” tool
- Not a magic AI prompt wrapper
- Not a runtime transformer
- Not a replacement for human review

If something cannot be shown as a diff, Nomad doesn’t do it.

## Core Principles

- Safety first — read-only by default
- Dry-run mandatory — show what would change before changing anything
- Git is the contract — branches, commits, PRs
- Fail closed — ambiguous logic is skipped and flagged
- Intent over syntax — preserve behavior, not formatting

## Current Status

### 🚧 Phase 0 — Guardrails (In Progress)

Nomad is currently establishing foundational safety guarantees before any migration logic is introduced.

Phase 0 focuses on:
- Execution modes (analyze / plan / apply)
- Read-only repo access
- Dry-run outputs
- Audit logs
- PR-only changes

No framework or language migration happens yet.

## Current Status(Phase 0)

### Early development

Nomad is currently focused on establishing foundational safety guarantees before any migration logic is introduced.
No automatic migrations are performed at this stage.