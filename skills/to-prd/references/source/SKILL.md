---
name: to-prd
description: Turn the current conversation context into a PRD and submit it as a GitHub issue. Use when user wants to create a PRD from the current context.
---

This skill takes the current conversation context and codebase understanding and produces a PRD. Do NOT interview the user — just synthesize what you already know.

## Process

1. Explore the repo to understand the current state of the codebase, if you haven't already.
2. Sketch the modules to build or modify, look for deep modules, and check expectations and tests with the user.
3. Write a PRD with problem statement, solution, user stories, implementation decisions, testing decisions, out of scope, and further notes. Submit it as a GitHub issue.
