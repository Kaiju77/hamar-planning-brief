# Hamar Planning Brief

Compulsory 2, KIUA-2003, Group 12: Kai Arne Hage and Mohammad Almojtaba Elhajj A Elhajj.

A small Python workflow turns selected planning-notice text into a Norwegian draft with field-level evidence, deadline status and an explicit human-review gate. It runs in four stages: load input, extract facts with a local model, format a draft, then check and save. It uses Python's standard library, files and Ollama's local HTTP API. One command performs all stages automatically. There is no automatic external publication.

Status: a working program and student-review draft, updated 29 October 2026. The course announcement gives **30 October 2026** as the first deadline and **6 November** as the retake deadline. Kai confirmed PDF is accepted; exact cutoff times remain to be checked. Both students joined Group 12 and agreed to work together. Kai led the preparation with substantial AI help; Mohammad joined late and his review is planned. Kai compared source text with a draft; full student report review remains unfinished.

## Open on a phone or share for review

- [Current report PDF](output/pdf/compulsory2_report.pdf): read the first four pages for the main report. References and appendices follow.
- [Mohammad's review guide](docs/PARTNER_REVIEW.md): a short list of what to check and send back.
- [Student checklist](STUDENT_CHECKLIST.md): remaining factual checks and approval tasks.

The repository is public, so these links can be opened on a phone without a local Python installation. The app itself runs on a computer; this does not install or host it on the phone. The PDF is still for student review, not a claim of final approval.

Public repository: https://github.com/Kaiju77/hamar-planning-brief

## Run without a model

Install Python 3.10 or later. There are no Python dependencies to install. Open a terminal in this repository root. On Linux use `python3` in place of `python` if needed.

```text
python run.py --meta fixtures/syn_ok.meta.json --input fixtures/syn_ok.txt --backend fixture --checked-at 2026-10-28
```

Fixture mode reads a canned `.model.json` file. It demonstrates the pipeline and validators; it does not measure model reasoning or attack resistance. Output directories are printed indirectly through the saved files under `out/`, with one timestamped directory per run.

## Run with the local model

Install Ollama, start its local service and download the exact model tag:

```text
ollama pull qwen2.5-coder:7b
python run.py --meta examples/ringgata.meta.json --input examples/ringgata.txt --backend ollama --model qwen2.5-coder:7b --checked-at 2026-10-28
```

The service uses `http://localhost:11434/api/generate`. The fixed date reproduces the recorded check. For a current check pass the actual Europe/Oslo date. When IANA timezone data is unavailable on Windows, `--checked-at` is required. An expired date is not proof that the original notice has not been extended; always review the source.

Each run saves an input/prompt snapshot, code hashes, raw model response and measurements. A valid draft adds JSON and Markdown; a failed run adds `.failure.json` and exits nonzero. Earlier exploratory runs have less snapshot information and are labeled separately in RESULTS.md. Input and output folders must be writable and sufficient disk space must be available; filesystem failure can prevent logging.

## Verify and evaluate

```text
python -m unittest discover -s tests -v
python evaluate.py --backend fixture
python evaluate.py --backend ollama --count 5
python evaluate.py --backend ollama --example ringgata_extended --count 5 --checked-at 2026-10-29
python tools/build_results.py
```

Twelve unit tests cover the seven original fixture cases and five added robustness cases, including an unavailable Ollama service. The fixture evaluation also deliberately records a known unsafe outcome: a quoted injected date may pass the evidence checker. Passing this expected-behavior test is not a security success. New evaluation output explicitly labels this as `known_unsafe_acceptance`; the original saved summaries retain their historical field names.

`evaluate.py` preserves every attempt and limits a real batch to five runs. Its reference checks look for selected words and addresses, not full meaning. `tools/build_results.py` regenerates the report table from the two fixed saved batches. It does not replace them with newly run results.

## Evidence and project files

- `run.py`: CLI, local model call, template and output persistence.
- `checks.py`: provenance, field structure, evidence and date checks.
- `context/extract_prompt.md`: all extraction instructions supplied to the model.
- `examples/`: minimal real Ringgata extract and source metadata.
- `fixtures/`: synthetic notices and canned model outputs.
- `evidence/real/`: early exploratory runs, including a rejected Llama response.
- `evidence/evaluation-final/`: final five-run Qwen batch with response-route extraction.
- `evidence/evaluation-extended/`: five runs on the 61-word extract, including their missing participation/route content.
- `evidence/evaluation-fixture/`: saved pipeline evaluation, including the known gap.
- `evidence/final-metrics.json`: computed report measurements.
- `report/`: report source and official unmodified NeurIPS 2025 style.
- `output/pdf/compulsory2_report.pdf`: compiled editorial draft for student review.
- `docs/`: source review, assistance record, working-session records and review guidance.

The first five Qwen repetitions saved drafts on the same 21-word input. Five new repetitions used a 61-word extract from the same notice. All five new drafts passed the code checks, but missed the office day and left response_route unknown. Submission details appeared under participation instead. They failed the content goal despite passing code checks. This is two inputs from one notice, not ten independent notices. Earlier attempts are kept separately.

## Operation limits and known gaps

There is one model call per run, temperature 0, an 800-token generation cap, a 12,000-character input cap, no automatic retry and a 120-second HTTP timeout. These limits do not yet implement a measured total token budget. Ctrl+C stops the client. Server inference may require `ollama stop qwen2.5-coder:7b`; a client timeout alone is not a guaranteed server kill switch. More explicit budget enforcement and a halt policy are exam work.

The model cannot itself execute shell commands or publish output. Python still has the filesystem permissions of its operating-system user; application-level path sandboxing is not implemented. Use selected non-personal data and local output folders. No credentials are required or stored. All drafts require human review.

Evidence matching ignores whitespace and case. It confirms that a passage occurs in the input, not that the passage supports the claim. Instruction-like text triggers a heuristic warning only. A model that adopts an injected date may produce a draft that passes; this is a documented open failure. Multiple-deadline ambiguity is addressed in instructions but not systematically evaluated. Precise cutoff times and source freshness need further work.

The first real extract omits response details; the full page contains them. The second includes an institutional mailbox, postal address, case number and office day. Both were source-checked with AI assistance and still need student review. They are selected passages, not a full notice. No broad source-reuse or crawling permission has been established. No raw HTML or full source document is redistributed. See [source review](docs/source-review.md).

## Report and assistance

The report uses `\usepackage[preprint]{neurips_2025}` and removes the conference checklist. The style file came from the official archive at https://media.neurips.cc/Conferences/NeurIPS2025/Styles.zip . The Canvas-specific template still needs comparison if it contains course changes. Compile in `report/` with `pdflatex main.tex` twice; copy the resulting PDF to `output/pdf/compulsory2_report.pdf`. The main text must remain 3-4 pages; references and appendices are separate.

Claude supplied the initial skeleton, fixtures and tests. Codex audited and extended it, checked source passages, ran experiments, drafted documentation and prepared the report. Kai selected the direction, supplied critique and authorized the work. Student editorial review and partner contributions are recorded only when actually confirmed. See [assistance log](docs/assistance-log.md) and [working-session records](docs/working-sessions.md). The report is an editorial draft, not a claim that an assistant can fulfill the students' review obligations.
