"""Checks site/content before publishing. Run: python3 tools/validate.py
Exits 1 on any error. No dependencies."""
import json, os, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")
FORMATS = {"mcq", "multi", "numeric", "hotspot", "match", "order"}
errors, warnings = [], []
err = lambda where, msg: errors.append(f"{where}: {msg}")


def load(rel):
    try:
        with open(os.path.join(ROOT, rel)) as f:
            return json.load(f)
    except Exception as e:  # missing file or bad JSON
        err(rel, str(e))
        return None


def check_question(q, where, topics, subs, seen):
    qid = q.get("id")
    if not qid or not isinstance(qid, str):
        return err(where, "missing id")
    w = f"{where} [{qid}]"
    if not all(c.isalnum() or c == "-" for c in qid):
        err(w, "id may use letters, digits and hyphens only")
    if qid in seen:
        err(w, f"duplicate id, also in {seen[qid]}")
    seen[qid] = where
    if q.get("topic") not in topics:
        err(w, f"unknown topic {q.get('topic')!r}")
    elif q.get("subtopic") not in subs.get(q["topic"], ()):
        err(w, f"subtopic {q.get('subtopic')!r} is not under topic {q['topic']!r}")
    fmt = q.get("format")
    if fmt not in FORMATS:
        return err(w, f"unknown format {fmt!r}")
    if q.get("status", "live") not in ("live", "draft"):
        err(w, "status must be live or draft")
    if not str(q.get("stem", "")).strip():
        err(w, "empty stem")
    if not q.get("sample"):
        if not str(q.get("solution", "")).strip():
            err(w, "missing solution")
        if not str(q.get("eli5", "")).strip():
            err(w, "missing plain-words explanation (eli5)")
        v = q.get("verify") or {}
        if v.get("method") not in ("computed", "reference"):
            err(w, "verify.method must be computed or reference")
        if v.get("method") == "reference" and not str(v.get("basis", "")).strip():
            err(w, "reference-verified question needs verify.basis")
        if not q.get("handbook"):
            err(w, "needs at least one handbook pointer")
    if not q.get("sample") and q.get("source", "original") != "original":
        warnings.append(f"{w}: source is {q.get('source')!r}; only original questions belong in the bank")
    a = q.get("answer")
    ids = lambda key: [o.get("id") for o in q.get(key, [])]
    if fmt in ("mcq", "multi"):
        opts = ids("options")
        if len(opts) < 2 or len(set(opts)) != len(opts):
            err(w, "needs at least two options with unique ids")
        if fmt == "mcq":
            if len(opts) != 4:
                warnings.append(f"{w}: exam multiple-choice items have four options, this has {len(opts)}")
            if a not in opts:
                err(w, "answer is not an option id")
        else:
            if not isinstance(a, list) or len(a) < 2 or any(x not in opts for x in a) or len(a) == len(opts):
                err(w, "answer must list two or more option ids, and not all of them")
            if q.get("selectCount") not in (None, len(a or [])):
                err(w, "selectCount does not match the number of answers")
    elif fmt == "numeric":
        if not isinstance(a, dict) or not (isinstance(a.get("value"), (int, float)) or ("min" in a and "max" in a)):
            err(w, "answer needs a numeric value, or min and max")
        elif a.get("toleranceType", "rel") not in ("rel", "abs"):
            err(w, "toleranceType must be rel or abs")
        elif a.get("toleranceType", "rel") == "rel" and a.get("value") == 0:
            err(w, "a zero answer needs an absolute tolerance")
    elif fmt == "hotspot":
        regs = ids("regions")
        fig = q.get("figure") or {}
        if not fig.get("svg") or not fig.get("viewBox") or not fig.get("alt"):
            err(w, "figure needs svg, viewBox and alt")
        if len(regs) < 2:
            err(w, "needs at least two regions so there is a wrong place to click")
        for r in q.get("regions", []):
            need = {"rect": ("x", "y", "w", "h"), "circle": ("cx", "cy", "r"), "poly": ("points",)}.get(r.get("shape"))
            if not need or any(k not in r for k in need):
                err(w, f"region {r.get('id')!r} has a bad shape")
        if any(x not in regs for x in (a if isinstance(a, list) else [a])):
            err(w, "answer is not a region id")
    elif fmt == "match":
        toks, tgts = ids("tokens"), ids("targets")
        if len(toks) < 2 or len(tgts) < 2:
            err(w, "needs at least two tokens and two targets")
        if not isinstance(a, dict) or set(a) - set(toks) or any(v is not None and v not in tgts for v in a.values()):
            err(w, "answer must map token ids to target ids or null")
        elif not any(a.values()):
            err(w, "no token has a target")
        else:
            single = [t["id"] for t in q["targets"] if not t.get("multi")]
            if any(sum(1 for v in a.values() if v == t) > 1 for t in single):
                err(w, "two tokens share a target that is not marked multi")
    elif fmt == "order":
        items = ids("items")
        if len(items) < 3:
            err(w, "needs at least three items")
        if not isinstance(a, list) or sorted(a) != sorted(items):
            err(w, "answer must be a permutation of the item ids")
        elif a == items:
            err(w, "items are listed in the answer order; scramble them")


def main():
    m = load("content/manifest.json")
    exam = load(m["exam"]) if m else None
    if not m or not exam:
        return
    topics = {t["id"] for t in exam["topics"]}
    subs = {t["id"]: {s["id"] for s in t["subtopics"]} for t in exam["topics"]}
    seen, counts, subcount = {}, {t: 0 for t in topics}, {}
    for rel in m["questions"]:
        data = load(rel)
        if not isinstance(data, list):
            if data is not None:
                err(rel, "must be a JSON array")
            continue
        for q in data:
            check_question(q, rel, topics, subs, seen)
            if not q.get("sample") and q.get("topic") in counts and q.get("status", "live") == "live":
                counts[q["topic"]] += 1
                subcount[q.get("subtopic")] = subcount.get(q.get("subtopic"), 0) + 1
    gseen = set()
    for rel in m["guide"]:
        g = load(rel)
        if not g:
            continue
        if g.get("topic") not in topics:
            err(rel, f"unknown topic {g.get('topic')!r}")
            continue
        for s in g.get("sections", []):
            w = f"{rel} [{s.get('id')}]"
            if not s.get("id") or s["id"] in gseen:
                err(w, "missing or duplicate section id")
            gseen.add(s.get("id"))
            if s.get("subtopic") is not None and s.get("subtopic") not in subs[g["topic"]]:
                err(w, f"subtopic {s.get('subtopic')!r} is not under this topic")
            if not s.get("title") or not str(s.get("body", "")).strip():
                err(w, "needs a title and a body")
    covered = set()
    for rel in m["guide"]:
        g = load(rel) or {}
        covered |= {x.get("subtopic") for x in g.get("sections", [])}
    for t in exam["topics"]:
        for sub in t["subtopics"]:
            if sub["id"] not in covered:
                warnings.append(f"no guide lesson for {sub['id']} ({sub['name'][:40]})")
            if not any(k == sub["id"] for k in subcount):
                warnings.append(f"no questions for {sub['id']}")
    ref = load(m["reference"])
    for s in (ref or {}).get("sections", []):
        if not s.get("id") or not s.get("title") or any(t not in topics for t in s.get("topics", [])):
            err(m["reference"], f"bad section {s.get('id')!r}")
    on_disk = {os.path.relpath(os.path.join(d, f), ROOT).replace(os.sep, "/") for d, _, fs in os.walk(os.path.join(ROOT, "content")) for f in fs}
    listed = set(m["questions"]) | set(m["guide"]) | {m["exam"], m["reference"], m.get("hbindex", ""), "content/manifest.json"}
    for f in sorted(on_disk - listed):
        if not f.startswith("content/figures/"):
            warnings.append(f"{f}: on disk but not in the manifest, so the site will not load it")
    total = sum(counts.values())
    print(f"{len(seen)} questions ({total} live in the bank), {len(gseen)} guide sections")
    for t in exam["topics"]:
        share = (t["min"] + t["max"]) / 2 / 126
        print(f"  {t['n']:>2}. {t['name']:<48} {counts[t['id']]:>4}   exam share {share:4.0%}" + (f", bank share {counts[t['id']] / total:4.0%}" if total else ""))


main()
for wmsg in warnings:
    print("warning:", wmsg)
for e in errors:
    print("ERROR:", e)
print("FAILED" if errors else "OK")
sys.exit(1 if errors else 0)
