# Third-review findings: resolved and checked

Claude implemented M1 to M4 in local commit dba5c88. Codex then checked those changes rather than repeating them. The original review remains unchanged as a record of what was found.

| Finding | Resolution |
|---|---|
| M1: prompt definitions overlap | Section 3 and its generated findings now say our prompt permits submission details under participation and never explicitly asks for office days. This is a likely cause, not a proven cause. No prompt change or new model trial is claimed. |
| M2: Norwegian draft contradicts itself | The report now explains that the draft prints mailbox/address under what residents can do, then says the official route is not given. The office day is absent. |
| M3: table hides content failure | The table has a separate Content goal column: Met for the original input's narrow goal, Missed for all five longer-input attempts. The caption separates saving a draft from meeting that goal. These are limited reference checks, not independent human grading. |
| M4: misleading true flag in raw log | Appendix C explains that matches_fixture_behavior_expectation is not a completeness score. The original JSON is unchanged. |

## Codex verification after Claude's commit

- All 12 unit tests passed again.
- Running tools/build_results.py reproduced both result totals and made no working-tree changes.
- All eight PDF pages were rendered and inspected. Main text is pages 1 to 4; references and Appendix A start on page 5. The extra table column fits.
- All three existing PDF copies were byte-identical. PDF text contains no em dash, en dash or nonbreaking hyphen.
- Comparing a751662 with dba5c88 showed changes only to the review, report source, generated table, table builder and compiled PDF. run.py, checks.py, the extraction prompt and saved evidence did not change.
- Student checklist line references and the packaged commit reference were refreshed after verification.

No model rerun was needed for these reporting changes. No new public clone or independent student review is claimed. Eight student tasks remain open. The latest revision is local only; nothing was pushed or submitted.
