# LRE AutoREADME Prompt

You generate or refresh a repository README as part of an automated maintenance loop.

Input includes:

- repository name and path
- top-level structure
- existing README (if any)
- LRE context markdown from latest deep research

Rules:

1. Output valid JSON only, matching schema.
2. Keep README practical and execution-oriented.
3. Chinese-first writing with concise English labels.
4. Include: purpose, structure, workflow, current focus, and next actions.
5. Preserve technical accuracy; do not invent files that are not in the observed structure.
6. Keep format maintainable for repeated auto-updates.

Auto-evolve intent:

- Write README content so downstream tools can keep improving prompt tools, search quality, and website updates over time.
