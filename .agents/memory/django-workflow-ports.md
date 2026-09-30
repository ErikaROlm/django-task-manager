---
name: Django workflow ports
description: Environment-specific guidance for running a Django app through a Replit workflow.
---

Use an explicit `0.0.0.0:<port>` in a Django workflow command when the workflow is configured with `waitForPort`; do not rely on `$PORT` expansion inside the command.

**Why:** The workflow shell passed `$PORT` through literally in this environment, so Django rejected `0.0.0.0:` as an invalid address.

**How to apply:** Keep the explicit port synchronized with the workflow's `waitForPort` value.