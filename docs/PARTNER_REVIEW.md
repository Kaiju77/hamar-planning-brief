# Mohammad: quick review before submission

Latest handoff and final technical checks: [FINAL_HANDOFF.md](FINAL_HANDOFF.md). No further AI-review round is planned.

Group 12: Kai Arne Hage and Mohammad Almojtaba Elhajj A Elhajj.

This draft presents a working planning-notice workflow, its test results and its limitations. Kai led the initial preparation with substantial AI assistance. The next step is to agree the shared direction and review the draft together.

## Decision before submission

Compare this candidate with your bus-delay reporting work. Please share what already runs, the input data, one sample output and who would use the report. Decide together whether to continue one candidate or build a genuinely connected workflow. A shared reporting pipeline alone does not establish that two unrelated topics are the same project.

Your message reports that the compulsory project must substantially continue into the exam (about 50 percent, as explained by the lecturer). Confirm what must carry over before committing to a direction. This planning-notice draft is not a claim that the joint decision has been made.

## Open these

- [Report PDF](../output/pdf/compulsory2_report.pdf). Main text is the first four pages. References and appendices do not count towards the 3 to 4-page main-text limit.
- [Editable LaTeX ZIP for Overleaf](../output/latex/Compulsory2_Group12_Overleaf.zip). Includes the current report source, NeurIPS style, result tables and raw-log appendix.
- [Official Hamar notice](https://www.hamar.kommune.no/lokaldemokrati/oppstart-reguleringsplan-fv-187-ringgata-i-hamar).
- [Selected longer input](../examples/ringgata_extended.txt).
- [One preserved real draft](../evidence/evaluation-extended/20261029T210826845602Z/runs/20261029T220826846511/ringgata_extended.md).

## What to do

### Editing the report

Download the LaTeX ZIP and upload it to Overleaf as a project. Open main.tex, edit the text and compile using pdfLaTeX. Keep all six supplied files together. The NeurIPS 2025 preprint setup is already included; no template needs to be built from scratch. If Canvas provides a course-specific template, compare it with this setup before submission.

The results paragraph and tables are defined in results-rows.tex and results-macros.tex. Do not change measured numbers unless correcting them from saved evidence. To make durable changes to generated text, update tools/build_results.py in the repository too, or tell Kai what changed so the source stays synchronized. Check that main text remains 3 to 4 pages after editing, download the PDF and return the edited source ZIP as well. Overleaf edits do not automatically update GitHub.

### Review and decisions

1. Read the four main pages. Tell Kai which sentences are unclear, inaccurate or different from how you would explain the project. Finding no problem is a valid result.
2. Compare the source and selected input with the draft: proposal, endpoints, deadline, submission mailbox/address and office day.
3. Check the reported failure: the draft includes the address under participation, then says the official route is not given. It also omits the office day. Passing our code checks does not mean a complete draft.
4. Discuss your findings with Kai. Record the actual date, who took part, decisions, edits and next actions. No invented meeting history is needed.

Send back a brief note: what you read, what you checked, any corrections, and what you can now explain. Do not say you reviewed code you have not read.

Deadline in the supplied announcement: 30 October, retake 6 November. Kai confirmed PDF upload is accepted. Confirm the precise cutoff in Canvas. This is a review copy, not final student approval.
