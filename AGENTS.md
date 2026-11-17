# Agent instructions for this vault

This vault keeps a short memory for work in a separate code repository. It is a template: replace `example-project` with a local project name in your own vault. Keep personal notes and generated graphs out of the public repository.

## Start of a session

1. Read `projects/<project>/sessions/latest.md` for the last handover.
2. Read `projects/<project>/decisions.md` for decisions and their reasons.
3. List titles in `projects/<project>/wiki/` and open only pages relevant to the task.
4. If a Graphify graph exists for the code repository, query it for the specific module or symbol being changed. Do not load the entire graph into context.
5. Read `areas/` and `resources/` only for relevant cross-project context.

Use the notes and graph as starting context. Check current source when the answer is missing or may be stale; say what is uncertain rather than guessing.

## End of a session

1. Update `projects/<project>/sessions/latest.md` with work done, decisions made, and unresolved items.
2. Add a dated entry to `decisions.md` when an architectural decision was made. Record alternatives and the reason.
3. Add or update a short `wiki/` page for a reusable pattern or important behavior learned from source. Link related pages with Obsidian `[[wikilinks]]`.
4. Put cross-project patterns in `resources/` or `areas/` when they apply beyond one project.

## Wiki frontmatter

```yaml
---
project: <project-name>
type: decision | pattern | gotcha | reference
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
---
```

## Graph boundary

Graphify runs against a code repository and writes generated output there. Do not copy `graphify-out/` or a junction to it into this public vault. If no graph exists, continue from the notes and source.
