# Clean-clone verification, 29 October 2026

Source: fresh clone from https://github.com/Kaiju77/hamar-planning-brief.git at commit 5fd0379. The clone was placed in a new ignored temporary directory, without copying a virtual environment or caches. Verification used the desktop's existing Python and local Ollama service; this is not a different-machine or independent-student review.

Observed outcomes:

1. `python -m unittest discover -s tests -v`: 11 tests passed.
2. README fixture command with check date 2026-10-28: draft saved with expected synthetic fields and human-review status.
3. `python tools/build_results.py`: reconstructed 3,645 tokens and 37.971 seconds for the fixed five-run batch.
4. README real Qwen command with the same recorded check date: draft saved with the proposal, street endpoints, planning stage and normalized deadline. Participation and response route were unknown. This is a separate reproduction run, not added to the final five-run table.

The fixture and real reproduction artifacts are preserved under evidence/clean-clone. The service version and installed model digests were queried separately on 29 October and are under evidence; these observations do not retroactively prove the exact runtime state of all earlier experiments.

GitHub CLI returned isPrivate=false and main as the default branch. No Canvas submission or external message was sent.

## Review revision verification

A second fresh GitHub clone at commit 73da416 was checked on 29 October 2026. All 12 tests passed, the seven-case fixture evaluation reproduced its expected behaviors (including the explicitly labeled known unsafe acceptance), and the results builder reconstructed the same 3,645 tokens and 37.971 seconds. The model extraction logic was unchanged; the earlier real-model reproduction remains the real-backend check. This was again the same desktop, not an independent machine or student review.
