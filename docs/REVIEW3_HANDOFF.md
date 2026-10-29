# Third-review handoff

This local revision follows the supplied finishing checklist. It is not yet a final student-approved submission.

## What changed

- Report rewritten in plain English with short sentences and we/our for the project and plans. AI work and student work remain separate in the disclosure.
- No em dashes, en dashes or LaTeX dash shortcuts in the report prose. Exact source evidence and historical logs are not rewritten for style.
- Second source input: 61 words, checked against a fresh official HTTP response on 29 October. The current page label is 29 October; cached browsing still showed 26 October.
- Five new real Qwen attempts: five saved drafts, zero containing the required office day or populated route field. Submission details appear under participation. The missing content is reported as failure, not hidden.
- Original runs and extraction/checker code retained. Only evaluate.py and the result builder were extended for the new input and report table.
- Student placeholders, checklist, meeting template and a full raw evaluation summary added.

## Evidence

- Tests: evidence/tests-review3.txt (12 pass).
- Fixture output: evidence/fixture-review3-console.txt and evaluation-fixture-review3/.
- Fresh source check: evidence/source-check-20261029.json.
- New real runs: evidence/evaluation-extended/20261029T210826845602Z/.
- New metrics: evidence/extended-metrics.json (5,108 tokens; 51.176 seconds).
- Original final metrics: evidence/final-metrics.json (3,645 tokens; 37.971 seconds).
- The appendix evaluation-log.json is a byte-for-byte copy of the new summary.json.
- Fresh local clone of 787df5b: 12 tests pass; README fixture and evaluation commands run; both table totals reproduce. Full output: evidence/clean-clone-review3.txt. This does not verify the new revision on public GitHub.
- Compiled twice with MiKTeX. All eight pages rendered and visually inspected. Main text is pages 1 to 4, references start on page 5 and Appendix A occupies one page. Recheck after student edits.
- Automated text scan found no em/en/nonbreaking dashes in the PDF, no common secret-key patterns or absolute personal paths in project text. This is a scan, not a guarantee. Author names and institutional contact details are intentional.

## Local publication commands, not executed

After student review and explicit authorization to publish, run `git status`, commit any student edits, then `git push origin main`. Verify a fresh clone from the public URL and update the commit hash in the submission text file. None of those publication steps were run for this revision.

## Things to judge

Check whether the report is easy for second-year students to explain, every numerical claim matches saved evidence, passing checks is kept separate from content success, and the 3 to 4 main-page limit is respected. Do not request removal of pending-review statements before actual review. Verify the prompt quotes against the supplied conversations rather than assuming they are true.

## What is still open

Both students must read and edit the report, compare source and output, confirm actual contributions and add genuine meeting notes. Canvas's course-specific template and accepted file type are not confirmed. Source-reuse terms for broader use are unresolved. This revision is local only and must be published before the repository link can reproduce it. Review-only placeholders must be resolved before submission.

No assistant has sent this bundle to Claude or submitted to Canvas. The owner sends it for review.
