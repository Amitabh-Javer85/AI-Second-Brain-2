---
project: example-project
type: decision
created: 2026-10-23
updated: 2026-10-23
tags: [example]
---

# Decision: Keep sample input local

## Context

This fictional project demonstrates a tiny note-processing workflow. The example input is a local text file.

## Decision

The sample workflow reads a local file supplied by the user.

## Alternatives considered

- Fetch input from an external service.

## Why this choice

A local file makes the example easy to understand without an account or key.

## Consequences and revisit trigger

The example does not demonstrate remote input. Revisit if the fictional project later needs to fetch it.
