#!/usr/bin/env python3
"""Planning notice brief: load -> extract -> draft -> check and save."""
import argparse, json, pathlib, re, sys, urllib.request
import checks
from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
import time
import hashlib

HERE = pathlib.Path(__file__).parent
WARN = ("Dette er et utkast som må kontrolleres av et menneske. Den offisielle "
        "kunngjøringen er gjeldende, og utkastet kan være ufullstendig eller utdatert.")
LABEL = {"unknown": "ikke oppgitt", "ambiguous": "uklar i kilden", "open": "åpen", "closed": "utløpt"}


def load(meta_path, input_path):
    meta = json.loads(pathlib.Path(meta_path).read_text(encoding="utf-8"))
    return meta, pathlib.Path(input_path).read_text(encoding="utf-8")


def extract(extract_text, backend, input_path, model, audit=None):
    if backend == "fixture":  # canned model output, tests the pipeline and checks only
        return json.loads(input_path.with_suffix(".model.json").read_text(encoding="utf-8"))
    prompt = (HERE / "context/extract_prompt.md").read_text(encoding="utf-8")
    body = {"model": model, "stream": False, "format": "json",
            "options": {"temperature": 0, "num_predict": 800},
            "prompt": f"{prompt}\n<KILDE>\n{extract_text}\n</KILDE>"}
    req = urllib.request.Request("http://localhost:11434/api/generate",
                                 json.dumps(body).encode(), {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        response = json.loads(r.read())
    if audit is not None:
        audit.update(response)
    return json.loads(response["response"])


def draft(facts, meta, status):
    g = lambda f: LABEL.get(facts[f]["value"], facts[f]["value"])
    dl = facts["deadline"]["value"]
    lines = [f"# Utkast: {meta.get('title', 'plankunngjøring')}", "",
             f"> {WARN}", "",
             f"**Hva foreslås:** {g('proposal')}",
             f"**Hvor:** {g('location')}",
             f"**Frist for innspill:** {LABEL.get(dl, dl)} ({LABEL.get(status, status)})",
             f"**Hva kan du gjøre:** {g('participation')}",
             f"**Offisiell innsendingsvei:** {g('response_route')}",
             f"**Fase:** {g('planning_stage')}", "", "## Belegg fra kilden"]
    for f in checks.FIELDS:
        if facts[f]["evidence"]:
            lines.append(f"- {f}: «{facts[f]['evidence']}»")
    lines += ["", f"Kilde: {meta['source_url']} (hentet {meta['retrieved_at']})",
              "Status: needs_human_review"]
    return "\n".join(lines) + "\n"


def run(meta_path, input_path, backend="fixture", model="qwen2.5-coder:7b", out="out", checked_at=None):
    input_path = pathlib.Path(input_path)
    run_id = datetime.now().strftime("%Y%m%dT%H%M%S%f")
    out = pathlib.Path(out) / run_id
    out.mkdir(parents=True, exist_ok=False)
    stem = input_path.stem
    meta, text, audit = {}, "", {}
    started = time.monotonic()
    try:
        today = datetime.now(ZoneInfo("Europe/Oslo")).date().isoformat()
    except ZoneInfoNotFoundError:
        # Windows may lack IANA timezone data. Require an explicit date instead.
        today = None
    checked_at = checked_at or today
    try:
        if checked_at is None:
            raise ValueError("provide --checked-at YYYY-MM-DD (Europe/Oslo)")
        from datetime import date
        if not isinstance(checked_at, str) or not checks.ISO.fullmatch(checked_at):
            raise ValueError("checked_at must be YYYY-MM-DD")
        date.fromisoformat(checked_at)
        meta, text = load(meta_path, input_path)
        if not isinstance(meta, dict):
            raise ValueError("metadata must be an object")
        if len(text) > 12000:
            raise ValueError("source exceeds 12000 character input cap")
        facts = extract(text, backend, input_path, model, audit)
        err, warn = checks.check(facts, text, meta)
    except Exception as e:  # model down, bad JSON, ...
        facts, err, warn = None, [f"input or extraction failed: {type(e).__name__}"], []
    measurement = {"run_id": run_id, "backend": backend, "model": model if backend == "ollama" else None,
                   "temperature": 0, "num_predict": 800, "timeout_seconds": 120,
                   "checked_at": checked_at, "elapsed_seconds": round(time.monotonic()-started, 3),
                   "raw_model_response": audit, "extracted_facts": facts}
    (out / "run.json").write_text(json.dumps(measurement, ensure_ascii=False, indent=2), encoding="utf-8")
    prompt_file = HERE / 'context/extract_prompt.md'
    snapshot = {"source_metadata": meta, "input_text": text,
                "input_sha256": hashlib.sha256(text.encode('utf-8')).hexdigest(),
                "extraction_prompt": prompt_file.read_text(encoding='utf-8') if prompt_file.exists() else None,
                "code_sha256": {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                                for name in ('run.py','checks.py')}}
    (out / 'input-snapshot.json').write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding='utf-8')
    if facts is not None and not err and not facts["in_scope"]:
        err = ["out of scope: not a planning notice open for input"]
    if err:
        rep = {"status": "failed", "failed_checks": err, "message": "Run requires attention; no draft saved.", "source_url": meta.get("source_url") if isinstance(meta, dict) else None}
        (out / f"{stem}.failure.json").write_text(json.dumps(rep, ensure_ascii=False, indent=1), encoding="utf-8")
        return rep
    status = checks.deadline_status(facts["deadline"]["value"], checked_at)
    result = {"source_url": meta["source_url"], "retrieved_at": meta["retrieved_at"],
              **{f: facts[f] for f in checks.FIELDS}, "deadline_status": status,
              "checked_at": checked_at, "warnings": warn, "review_status": "needs_human_review"}
    (out / f"{stem}.json").write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    rendered = draft(facts, meta, status)
    rendered += f"\nKontrolldato: {checked_at}. Kilden kan ha blitt endret siden den ble hentet.\n"
    if meta.get('partial'):
        rendered += "Grunnlag: utvalgte utdrag, ikke hele kunngjøringen. Se originalen for full informasjon og innsendingsvei.\n"
    (out / f"{stem}.md").write_text(rendered, encoding="utf-8")
    return result


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--meta", required=True); ap.add_argument("--input", required=True)
    ap.add_argument("--backend", choices=["fixture", "ollama"], default="fixture")
    ap.add_argument("--model", default="qwen2.5-coder:7b"); ap.add_argument("--out", default="out")
    ap.add_argument("--checked-at", help="Check date in Europe/Oslo, YYYY-MM-DD")
    a = ap.parse_args()
    r = run(a.meta, a.input, a.backend, a.model, a.out, a.checked_at)
    print(json.dumps(r, ensure_ascii=False, indent=1)[:1500])
    sys.exit(1 if r.get("status") == "failed" else 0)
