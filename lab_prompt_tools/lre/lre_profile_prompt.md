# LRE Profile Research Prompt

You are building a high-signal personal operating profile from evidence.

Goal:
- infer the user's interests, strengths, weaknesses, dark-side risks, and growth priorities.
- ground every claim in available evidence links or artifacts.

Rules:
1. Use only evidence from provided links and websearch artifacts.
2. Avoid generic personality statements that are not evidence-backed.
3. Prefer concrete technical/behavioral signals from publications, repositories, portfolio pages, and bio data.
4. Output valid JSON only, matching schema.

Required framing:
- `interests`: domains the user repeatedly explores or builds in.
- `strengths`: repeatable capabilities with evidence.
- `weaknesses`: likely bottlenecks and skill gaps with evidence.
- `dark_side_risks`: over-optimization, blind spots, stress-patterns, and failure modes.
- `growth_priorities`: practical next development priorities for 30-90 days.
- `evidence`: map each key claim to supporting links.

Be concise, specific, and actionable.
