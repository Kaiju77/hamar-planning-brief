# First real-input runs, 28 October 2026

Input: three short non-contiguous excerpts from the official Ringgata notice, selected and checked by Codex. This is a partial source, not the whole notice. Student review remains pending. The original source URL and limitations are recorded in examples/ringgata.meta.json.

Temperature: 0. Output cap: 800 tokens. HTTP timeout: 120 seconds. Check date: 2026-10-28. No retries. All raw responses and extracted facts are preserved in evidence/real. Counts below come from run.json files.

| Run ID | Model | Wall seconds | Prompt tokens | Generated tokens | Outcome |
|---|---|---:|---:|---:|---|
| 20261028T185357839686 | llama3.2:3b | 13.263 | 353 | 212 | Rejected: in_scope false |
| 20261028T185424152034 | qwen2.5-coder:7b | 13.847 | 362 | 243 | Draft saved |
| 20261028T185444223832 | qwen2.5-coder:7b | 5.294 | 362 | 243 | Draft saved |
| 20261028T185449729140 | qwen2.5-coder:7b | 5.302 | 362 | 243 | Draft saved |
| 20261028T185455194927 | qwen2.5-coder:7b | 5.314 | 362 | 243 | Draft saved |
| 20261028T185500675545 | qwen2.5-coder:7b | 5.321 | 362 | 243 | Draft saved |

Initial model loading contributes to latency, so these runs are not a controlled speed comparison.

Assistant inspection of all five Qwen results found the proposal, location, stage and deadline consistent with the selected extract. Participation was unknown in 5/5, correctly reflecting its absence from this partial input. All five normalized deadlines were 2026-11-18. This is one small input repeated at temperature zero; consistency is not evidence of general accuracy or resistance to prompt injection.

The rejected Llama response contained invented quotations and a non-ISO deadline, as well as incorrect scope classification. The current checker exits early on out-of-scope output, so the recorded rejection reason is scope, not a successful detection of every invented quotation. No draft was saved. Do not describe this as a comprehensive security test.

The first six real runs predate input-snapshot logging and the improved display of partial-source status. Their original saved outputs are retained unchanged. Later runs record an input and prompt snapshot alongside the raw response. These implementation changes are not evidence of improved extraction accuracy.

Known failure retained from Claude: if an injected date appears in the source and the model adopts it, exact-evidence checking can pass it. A warning heuristic does not solve this. Human review is mandatory.
