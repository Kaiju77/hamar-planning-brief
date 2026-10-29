# Claude review 3 (KIUA-2003 Compulsory 2, Group 12)

Review only. I changed no implementation, report, evidence or checklist file. This file is the only thing I added.

## What I reviewed

- Commit: `a751662` ("Record local clone verification and third-review checks"), on `main`, working tree clean at the start. It is local only. The earlier reviewed commit `787df5b` differs from it by three docs/evidence files, so the report and code are the same.
- Read: `docs/REVIEW3_HANDOFF.md`, `docs/CLAUDE_REVIEW_PROMPT.md`, `STUDENT_CHECKLIST.md`, `README.md`, `report/main.tex`, `output/pdf/compulsory2_report.pdf`, the extraction prompt, the two example inputs, the raw run files for both batches, `evaluate.py` (reference checks), `report/results-*.tex`, and the original brief `../project_KIUA_2003.pdf`.

## Checks I ran

| Check | Result |
|---|---|
| `python -m unittest discover -s tests` | 12 tests pass (5 + 7 test functions in the two files). |
| `python evaluate.py --backend fixture` | Ran. 7 cases, all as expected, including the known-unsafe `syn_injection_followed` (deadline 2027-01-01 accepted). It wrote a new folder under `out/evaluation/`. `out/` is git-ignored, so the repo is still clean. |
| Word counts | `ringgata.txt` = 21, `ringgata_extended.txt` = 61. Matches the report. |
| Token and time totals, recomputed from all 10 `run.json` files | Batch A: 3,645 tokens, 37.971 s. Batch B: 5,108 tokens, 51.176 s. All ten table rows match the raw files exactly (A: 465 in / 264 out; B: 593 in / 431, 428, 428, 428, 428 out; times match). |
| The five Batch B drafts | All five have `participation` filled with the mailbox, case number and postal address, `response_route` = `unknown`, and no office day anywhere. Confirms your description. |
| PDF | 8 pages. Main text is pages 1 to 4, references start on page 5, Appendix A is on pages 5 to 6 at most (one page or less), so it is within two pages. The text has no em dash, en dash or non-breaking hyphen. |
| Privacy scan | No API keys or passwords in tracked project text. The only personal-looking data are the two author names and the institutional mailbox and address, which are intentional. |
| Output PDF vs `report/main.pdf` vs `SUBMISSION_FOLDER` copy | All three are byte-identical (same MD5). |

## What I could not verify

- The live Hamar page. I did not re-fetch it. I only checked that the quoted passages in the examples match what the saved files say. The "29 October fresh response" claim rests on `evidence/source-check-20261029.json`, which I did not re-check.
- A live Ollama run. I did not call the model, so I only checked saved runs. I cannot say a new run would give the same answer.
- The "fresh clone of 787df5b" claim. I read `evidence/clean-clone-review3.txt` but did not make my own clone.
- Canvas template, accepted file type, and whether the demo slot is 9 November. None of these can be checked from the folder.
- Whether the PDF was built from exactly the current `main.tex`. I did not recompile (no TeX run). The text and numbers in the PDF match the `.tex` and the result macros, which is good evidence but not proof.
- Git needed `-c safe.directory=*` on each command because the folder is owned by the Codex sandbox user. I did not change any git config.

## Must-fix (honesty or accuracy)

**M1. The report blames the model for something the prompt invited.**
`context/extract_prompt.md` says, under `participation`: "The official submission route (address or form) can be included." It then says `response_route` is only for a route "explicitly given". The Batch B model put the mailbox and address under `participation`, which the prompt allows. It never defines `participation` as events or ways to take part, and the word "office day" is not in the prompt. So the Batch B result is at least partly a prompt and spec problem, not only "the model missed it".
The report and the `ExtendedFindings` text say "The model put the submission details in participation ... and omitted the office day". That is true as a description, but it hides the likely cause. The report's own success rule for Input B (route in the response-route field) also conflicts with what the prompt asks for. A reader checking "success is applied consistently" will notice.
*Fix:* say plainly that the field definitions in our prompt overlap, and that this is a likely cause. Keep the failure. Either make the prompt clearer (a new run, kept separate and labeled) or just report the overlap as a known cause.

**M2. The saved Norwegian drafts contradict themselves, and the report does not say so.**
In every Batch B draft the line "Hva kan du gjøre" contains the mailbox and address, while the next line says "Offisiell innsendingsvei: ikke oppgitt" ("official route: not given"). A resident would read that the route is missing when it is right above. The office day (10 November, 14.00 to 18.00) never appears. This is a more concrete harm than "response_route unknown", and it is the strongest example for the failure section. One sentence is enough.

**M3. The results table can read as success for Batch B.**
The column is "Code checks" but every cell says "Saved", for both batches. The failure is only in the text below the table. Someone skimming the table sees ten identical rows. Add a column or a note such as "Office day and route: 0/5" for B, so the table and the text agree. This matters because the brief grades honest failure reporting.

**M4. The appendix log says `matches_fixture_behavior_expectation: true` for all five failed drafts.**
In `evaluation-log.json` (copied into Appendix C), each Batch B case has `"matches_fixture_behavior_expectation": true` next to `participation_office_day: false` and the other three route fields `false`. A reader will see "true" beside content that failed. The report text says the log keeps original values, which is fair, but add one sentence in the appendix explaining that this flag only means the code behaved as the fixture rules expect, not that the content was right. Do not edit the saved log.

## Optional improvements

1. **Batch B is not identical across runs, and the report does not say so.** Run 1 gives the location as "... Disenvegen, Hamar" and runs 2 to 5 omit ", Hamar". Run 1 also has 431 output tokens versus 428. ", Hamar" is not in the quoted evidence, so this is a small example of a value the quote does not support. The report says "extracted facts were identical" only for Batch A, which is correct. A short remark for B would be honest and easy.
2. **Consider "participation" in the success text.** For Input B the success definition could name both the office day (participation) and the route (response route), so the checker and the sentence match.
3. **The "known injection weakness" is reported well, but the 12 tests passing is easy to over-read.** The README and report already warn about this. No change needed beyond keeping that wording.
4. **The abstract says the longer runs "missed important information".** That is accurate. "Important" is a judgment. You could say "missed the office day and the route field" to be concrete.
5. **Local-only files.** `report/main.log` contains local Windows user-directory paths and `tmp/` and `SUBMISSION_FOLDER/` are untracked. They are git-ignored so they will not be pushed, but check they are not inside any ZIP you share. The handoff says the privacy scan covers "project text", which is true; the log is a build file.
6. **Dates in "Appendix B".** The working-session records use "Kai and Codex" and "two Claude reviews supplied by Kai". That is honest and does not invent group meetings. Keep it. The student markers for real meetings should stay open.

## Checked and fine

- All ten table rows and both totals match raw files.
- Two input lengths (21 and 61 words) are right.
- Four main pages, appendix A within two pages, English plain and short, no dashes, no inflated claims that I found.
- Failure for the longer input is stated in the abstract, in section 4 and in the README, and it says the code checks passed while the content failed.
- Known injection gap, fixture-vs-live distinction, source-check date, source-reuse limits and the "AI-assisted, students must review" disclosure are all present and honest.
- The eight `[[STUDENT: ...]]` markers and the checklist items are still open and must stay open. I did not remove or fill any.
- Nothing was pushed, published or submitted.

## Summary for the sit-down

(a) **Readiness for student review:** ready. The numbers are right and the failures are reported, so the students can start reading and checking.
(b) **Factual or technical errors:** I found no wrong numbers. The issues are about cause and presentation (M1 to M4), not arithmetic.
(c) **Edits worth making first:** M1, M2, M3, then M4. All are small wording or table changes, no rewrite. Any prompt change in M1 would need a new, separately labeled run and should not replace the saved Batch B.

I stopped here so you can decide which changes to make.
