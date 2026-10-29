# Agent assistance and decision record

## 29 October: independent review supplied by Kai

Claude inspected the review bundle, reproduced the original eleven tests, recomputed the 3,645-token/37.971-second table and manually checked an unavailable-model failure. Codex verified the reported 21-word count, corrected the earlier erroneous 25-word description, added an unavailable-service unit test, clarified evaluation labels and report limitations, introduced an itemized risk table, moved baseline preparation before the demonstration window, and replaced paraphrased appendix content with short actual dialogue excerpts. Original experiment files are unchanged. Human editorial approval, partner contributions and Canvas template confirmation remain pending; software changes cannot complete those activities.

## 27-28 October 2026: problem and output design

The student asked for a feasible local project under the 30 October deadline and agreed to investigate a Hamar planning-notice brief. Codex researched official notices and proposed a specification. The student brought a Claude review that challenged the response route, date status, scope rule, field-level evidence and failure reporting. Codex incorporated those points and corrected one proposal: deadline status should use a recorded check date rather than retrieval date.

## Claude handoff

Claude supplied a standard-library skeleton, extraction prompt, seven canned fixture cases, tests and planning notes. The handoff explicitly stated that real data and the Ollama backend were untested. It documented the injection/evidence gap and deterministic rendering. The archive is retained outside this public repository. Do not attribute human review or real test runs to that stage.

## 28 October: Codex audit and implementation

Codex reproduced seven passing tests, then found a TypeError for a numeric deadline. Codex added four robustness tests, validated provenance fields, used an explicit check date, handled input failures, preserved unique run directories, and recorded raw model responses. Later work added a separate response_route field and input/prompt snapshots. Fixture expectations were extended with unknown response routes; existing assertions were retained.

One Llama attempt was rejected and its raw response retained. Five Qwen runs with the earlier prompt saved mechanically valid drafts. A final five-run batch was then recorded with the response_route field and input snapshots. These are two separate batches, not ten independent inputs. Evaluation code records narrow word-level reference checks, whose limitations must be reported.

Codex obtained the official NeurIPS 2025 style, created the public repository under the student's authorization, and drafted the report, schedule, risk table and review guide. The report is an AI-assisted editorial draft pending the student's actual review. Meetings with a partner, partner identity and private Canvas details have not been invented.
