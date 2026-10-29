# Compulsory 2: demonstration and editorial review

This guide is for reviewing the hand-in with Kai and the group. A compulsory video is not requested by the new brief. The later exam has a mandatory live demonstration.

## 1. Understand what is being handed in

The checkpoint consists of an English report (3-4 main-text pages in the required LaTeX format, plus references and appendices) and a repository link to the running skeleton. The repository contains context, input, code, tests and recorded evidence. The final exam extends this same project.

Confirmed by Kai: Group 12, Kai Arne Hage and Mohammad Almojtaba Elhajj A Elhajj; Canvas deadline 7 November 2026, 23:59, file upload. Accepted file types and any Canvas-specific template have not been confirmed.

## 2. Look at the source and input

Open the source URL recorded in examples/ringgata.meta.json, then examples/ringgata.txt. Check that the three selected passages occur in the original and describe the proposal, stage and deadline correctly. Note that they are not contiguous and omit the response channel. Do not mark your review complete until you actually do it.

Question: if the full source provides a response address but our extract does not, should the model guess it? Expected reasoning: no; it must mark the route unknown and send the reader to the original.

## 3. Run the skeleton

From a terminal in the repository:

```text
python run.py --meta examples/ringgata.meta.json --input examples/ringgata.txt --backend ollama --model qwen2.5-coder:7b --checked-at 2026-10-28
```

This date reproduces the recorded check. For a current run substitute the actual Oslo date. Without Ollama use the fixture command in README. Open the newest folder under out and read the .md draft. Compare each field with its evidence and the input. Check the partial-source warning, unknown response route, check date and needs_human_review status.

## 4. Explain the code in plain language

- run.py/load: read a selected text and metadata file.
- run.py/extract: send the prompt and extract to the local model; preserve the raw response.
- checks.py/check: inspect the shape and evidence; reject malformed or unsupported exact passages.
- checks.py/deadline_status: use a date comparison rather than asking a model whether the date has passed.
- run.py/draft: render validated facts using a Norwegian template, with no second model call.
- run.py/run: orchestrate all stages, preserve separate runs, and save a draft or failure.

Question: does an exact quotation prove the generated claim is correct? Expected reasoning: no. The quotation can be genuine but irrelevant, or can contain a malicious instruction. A human still reviews meaning.

## 5. Inspect failures and measurements

Read RESULTS.md for early runs, then evidence/final-metrics.json and the final evaluation summary. There are five repeats of one short real input, not five sources. Model word checks are proxies. The rejected Llama run is preserved under evidence/real. The synthetic injection-followed case deliberately shows a vulnerability: it is not a passed security defense.

Run:

```text
python -m unittest discover -s tests -v
python evaluate.py --backend fixture
```

Question: what does a green fixture test prove? Expected reasoning: the code behaves as expected for supplied canned data. It does not show what a real model will do.

## 6. Edit and approve the report

Read the whole report. Check the problem, output contract, architecture, results and schedule against what you just saw. Rewrite any sentence you cannot explain or do not agree with. Confirm both members' actual contributions and whether the working-session records are accurate. Add real group meeting records when available. Compare the course-provided LaTeX template with the official style used here. Rebuild the PDF and recheck page count after edits.

The file is deliberately an editorial draft. This is necessary because the brief requires students to act as editors-in-chief and does not accept raw agent output as final prose. Do not remove pending-review statements without doing the corresponding review.

## 7. Connect it to the exam

Next work: broader non-personal test set, two fault-injection classes, repairs with regression evidence, explicit permission and token-budget controls, measurable halt rule, feedback from the live demo, and eight genuine meeting reports. The final white paper is 7-8 main-text pages and the public submission commit must be tagged exam.
