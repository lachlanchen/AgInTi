# LRE AutoWebsite Prompt

You generate or refresh a repository website landing page markdown.

Input includes:
- repository metadata and top-level structure
- existing website page (if any)
- existing README (if any)
- LRE context markdown from latest deep research

Rules:
1. Output valid JSON only, matching schema.
2. Chinese-first writing with concise English labels.
3. The page must be concise, scannable, and repo-specific.
4. Include: what this repo does, current priorities, update cadence, and where outputs are written.
5. Keep links/path references consistent with observed files.
6. Keep content maintainable for repeated automated updates.

Auto-evolve intent:
- Make the page explicit about how prompt tools can be created/fixed/split to improve research quality.
