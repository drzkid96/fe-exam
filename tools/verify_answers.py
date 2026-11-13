"""Recomputes every answer key from the numbers in the question, independently of the JSON.
Run: python3 tools/verify_answers.py      Exits 1 if any key disagrees or any live question is unverified.

Each entry in CALC returns what the answer should be:
  number  -> must match the numeric answer, or the one multiple-choice option whose first number is within 1%
  string  -> must appear in the text of the correct option and in no other (or equal the hotspot region id)
  list    -> must equal the multi-select set or the ranking
  dict    -> must equal the drag-and-drop mapping
Questions whose answer is a matter of definition or code text use verify.method "reference" and must state their basis."""
import json, math, os, re, statistics, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")
g, gw, pi = 9.81, 9.81, math.pi
deg = math.radians


def simpson(f, a, b, n=200):
    h = (b - a) / n
    return h / 3 * (f(a) + f(b) + 4 * sum(f(a + h * i) for i in range(1, n, 2)) + 2 * sum(f(a + h * i) for i in range(2, n, 2)))


def shoelace(pts):
    return abs(sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]))) / 2


def bearing(az):
    ns, ew = ("n" if az < 90 or az > 270 else "s"), ("e" if az < 180 else "w")
    return ns + ew


def cpm_float(dur, preds, act):
    es, order = {}, list(dur)
    for a in order:
        es[a] = max((es[p] + dur[p] for p in preds[a]), default=0)
    end = max(es[a] + dur[a] for a in order)
    lf = {}
    for a in reversed(order):
        succ = [s for s in order if a in preds[s]]
        lf[a] = min((lf[s] - dur[s] for s in succ), default=end)
    return lf[act] - dur[act] - es[act]


def defl(E=1.0, I=1.0, L=1.0, w=1.0):
    return 5 * w * L ** 4 / (384 * E * I)


def moment_peak_region():
    L, a = 1.0, 1 / 3                      # unit load at L/3 on a simple span
    M = lambda x: (1 - a / L) * x if x <= a else a / L * (L - x)
    x = max((i / 3000 for i in range(3001)), key=M)
    return "load" if abs(x - a) < 1e-3 else "mid" if abs(x - 0.5) < 1e-3 else "a" if x < 1e-3 else "b"


def zero_pore_pressure_layer():
    layers = {"dry": 1.0, "satsand": 3.5, "clay": 5.5}   # mid-depths (m); water table at 2 m
    return [k for k, z in layers.items() if max(0.0, z - 2.0) * gw == 0]


CALC = {
    "math-0001": lambda: 3 - (11 - 3) / (6 - 2) * 2,
    "math-0002": lambda: simpson(lambda x: 3 * x * x, 0, 2),
    "math-0003": lambda: math.degrees(math.acos((3 * 4 + 4 * -3) / (math.hypot(3, 4) * math.hypot(4, -3)))),
    "math-0004": lambda: statistics.stdev([2, 4, 4, 6, 9]),
    "econ-0001": lambda: 5000 * 1.06 ** 10,
    "econ-0002": lambda: 20000 * 0.08 * 1.08 ** 5 / (1.08 ** 5 - 1),
    "econ-0003": lambda: 120000 / (30 - 18),
    "econ-0004": lambda: 0.2 * -50000 + 0.5 * 40000 + 0.3 * 100000,
    "statics-0001": lambda: math.hypot(100 + 80 * math.cos(deg(60)), 80 * math.sin(deg(60))),
    "statics-0002": lambda: 30 - 30 * 2 / 6,
    "statics-0003": lambda: (20 * 80 * 40 + 100 * 20 * 90) / (20 * 80 + 100 * 20),
    "statics-0004": lambda: math.degrees(math.atan(0.50)),
    "statics-0005": lambda: 100 * 200 ** 3 / 12 / 1e6,
    "dynamics-0001": lambda: 0.5 * (27 / 9) * 9 ** 2,
    "dynamics-0002": lambda: (300 - 0.30 * 50 * g) / 50,
    "dynamics-0003": lambda: math.sqrt(2 * g * 10),
    "dynamics-0004": lambda: 6 * 2 ** 2 / 3,
    "mechmat-0001": lambda: 50e3 / (pi * 20 ** 2 / 4),
    "mechmat-0002": lambda: 50e3 * 2000 / (pi * 20 ** 2 / 4 * 200e3),
    "mechmat-0003": lambda: 10 * 8 ** 2 / 8,
    "mechmat-0004": lambda: (80 + 20) / 2 + math.hypot((80 - 20) / 2, 40),
    "mechmat-0005": lambda: 20e6 * (200 / 2) / (100 * 200 ** 3 / 12),
    "mechmat-0006": lambda: sorted(k for k, d in {"a": defl(E=2), "b": defl(I=2), "c": defl(L=0.8), "d": defl(w=2), "e": defl(I=0.25)}.items() if d < defl()),
    "mechmat-0007": moment_peak_region,
    "materials-0001": lambda: 180 / 400,
    "materials-0002": lambda: 530e3 / (pi * 150 ** 2 / 4),
    "materials-0004": lambda: 140 / 0.0007 / 1000,
    "fluids-0001": lambda: gw * 12,
    "fluids-0002": lambda: 0.85 * gw,
    "fluids-0003": lambda: 2 * (200 / 100) ** 2,
    "fluids-0004": lambda: math.sqrt(2 * g * 0.45),
    "fluids-0005": lambda: gw * (3 / 2) * (2 * 3),
    "surveying-0001": lambda: 100.00 + 1.52 - 2.31,
    "surveying-0002": lambda: shoelace([(0, 0), (60, 0), (80, 40), (20, 50)]),
    "surveying-0003": lambda: 20 * (24 + 36) / 2,
    "surveying-0004": lambda: {"az%d" % a: bearing(a) for a in (45, 135, 225, 315)},
    "surveying-0005": lambda: (108.9 - 102.4) / 260 * 100,
    "water-0001": lambda: 0.60 * 2.5 * 12,
    "water-0002": lambda: (1 / 0.015) * ((3 * 1) / (3 + 2 * 1)) ** (2 / 3) * 0.001 ** 0.5 * (3 * 1),
    "water-0003": lambda: gw * 0.05 * 30 / 0.75,
    "water-0004": lambda: 1800 / 7200 * 24,
    "water-0005": lambda: 15 * 0.004 * 2000,
    "structural-0001": lambda: {0: "Statically determinate", 1: "first degree", 2: "second degree", 3: "third degree"}[14 + 3 - 2 * 8],
    "structural-0002": lambda: pi ** 2 * 200e3 * 8.0e6 / 4000 ** 2 / 1e3,
    "structural-0003": lambda: 20 * 6 ** 3 / (48 * 30000) * 1000,
    "structural-0004": lambda: max(1.4 * 20, 1.2 * 20 + 1.6 * 30),
    "structural-0005": lambda: 1500 * 420 * (500 - 1500 * 420 / (0.85 * 28 * 300) / 2) / 1e6,
    "structural-0006": lambda: 12 * 3,
    "geotech-0001": lambda: 1.92 / 0.001 / (1 + 0.20),
    "geotech-0002": lambda: 2.70 * 1000 / 1600 - 1,
    "geotech-0003": lambda: 17 * 2 + 19 * 4 - gw * 4,
    "geotech-0004": lambda: math.tan(deg(45 - 30 / 2)) ** 2,
    "geotech-0005": lambda: 10 + 100 * math.tan(deg(30)),
    "geotech-0006": lambda: 45 - 22,
    "geotech-0007": lambda: zero_pore_pressure_layer()[0],
    "transport-0001": lambda: 1.47 * 60 * 2.5 + 60 ** 2 / (30 * (11.2 / 32.2)),
    "transport-0002": lambda: 50 ** 2 / (15 * (0.06 + 0.14)),
    "transport-0003": lambda: 40 * 45,
    "transport-0004": lambda: 1200 / (4 * 375),
    "transport-0005": lambda: 3 * 500 / (3 - (-2)),
    "construction-0001": lambda: cpm_float({"A": 3, "B": 4, "C": 6, "D": 2}, {"A": [], "B": ["A"], "C": ["A"], "D": ["B", "C"]}, "B"),
    "construction-0002": lambda: 90000 / 95000,
    "construction-0003": lambda: 30 * 20 * 0.150 * 1.05,
    "construction-0004": lambda: 1.5 * (50 * 60 / 30),
}
# Further calculations are kept as plain expressions in tools/calc_expr.json, one per question id.
NAMES = {k: getattr(math, k) for k in ("sqrt", "pi", "sin", "cos", "tan", "atan", "log10", "log", "exp", "erf", "hypot", "comb")}
NAMES.update(rad=math.radians, g=g, gw=gw, simpson=simpson, abs=abs, max=max, min=min, sum=sum, range=range, format=format, int=int)
_expr_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "calc_expr.json")
if os.path.exists(_expr_path):
    for _id, _expr in json.load(open(_expr_path)).items():
        assert _id not in CALC, _id
        CALC[_id] = (lambda e: lambda: eval(e, {"__builtins__": {}}, dict(NAMES)))(_expr)
# Spot checks that back up reference-verified items where a number is involved.
assert abs(math.erf(1 / math.sqrt(2)) - 0.6827) < 1e-4          # math-0005: share within one standard deviation


def first_number(text):
    m = re.search(r"-?\d+(?:\.\d+)?", str(text).replace(",", "").replace("$", ""))
    return float(m.group()) if m else None


def close(a, b, rel=0.01):
    return abs(a - b) <= rel * max(abs(b), 1e-9)


def check(q, want):
    fmt, ans = q["format"], q["answer"]
    if fmt == "numeric":
        tol = ans.get("tolerance", 0.01)
        lo, hi = (ans["min"], ans["max"]) if "min" in ans else ((ans["value"] - tol, ans["value"] + tol) if ans.get("toleranceType") == "abs" else sorted((ans["value"] * (1 - tol), ans["value"] * (1 + tol))))
        if not lo <= want <= hi:
            return f"computed {want:.6g} is outside the accepted range {lo:.6g} to {hi:.6g}"
        if "value" in ans and not close(want, ans["value"], 0.005):
            return f"computed {want:.6g} but the key says {ans['value']}"
    elif fmt == "mcq":
        if isinstance(want, str):
            hits = [o["id"] for o in q["options"] if want.lower() in o["text"].lower()]
        else:
            hits = [o["id"] for o in q["options"] if first_number(o["text"]) is not None and close(first_number(o["text"]), want)]
        if hits != [ans]:
            return f"computed {want!r} matches option(s) {hits}, key says {ans!r}"
    elif fmt == "hotspot":
        if want not in (ans if isinstance(ans, list) else [ans]):
            return f"computed region {want!r}, key says {ans!r}"
    elif fmt in ("multi",):
        if sorted(want) != sorted(ans):
            return f"computed {sorted(want)}, key says {sorted(ans)}"
    elif fmt == "order":
        if list(want) != list(ans):
            return f"computed {want}, key says {ans}"
    elif fmt == "match":
        if {k: v for k, v in want.items() if v} != {k: v for k, v in ans.items() if v}:
            return f"computed {want}, key says {ans}"
    return None


def main():
    m = json.load(open(os.path.join(ROOT, "content", "manifest.json")))
    errors, computed, reference = [], 0, 0
    seen = set()
    for rel in m["questions"]:
        for q in json.load(open(os.path.join(ROOT, rel))):
            if q.get("sample") or q.get("status") == "draft":
                continue
            qid, v = q["id"], q.get("verify") or {}
            seen.add(qid)
            if v.get("method") == "computed":
                if qid not in CALC:
                    errors.append(f"{qid}: marked computed but has no calculation in CALC")
                    continue
                try:
                    msg = check(q, CALC[qid]())
                except Exception as e:  # a broken calculation is a failure, not a pass
                    msg = f"calculation raised {e!r}"
                if msg:
                    errors.append(f"{qid}: {msg}")
                computed += 1
            elif v.get("method") == "reference":
                if not str(v.get("basis", "")).strip():
                    errors.append(f"{qid}: reference-verified but states no basis")
                reference += 1
            else:
                errors.append(f"{qid}: live question with no verification")
    for extra in sorted(set(CALC) - seen):
        errors.append(f"{extra}: calculation exists but the question is missing or not live")
    # worked examples in the guide: the final number of each is recomputed too
    gpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "guide_checks.json")
    checks = json.load(open(gpath)) if os.path.exists(gpath) else {}
    lessons = {s_["id"]: s_ for rel in m["guide"] for s_ in json.load(open(os.path.join(ROOT, rel)))["sections"]}
    for sid, c in checks.items():
        if sid not in lessons or "example" not in lessons[sid]:
            errors.append(f"{sid}: example check exists but the lesson or its example is missing")
            continue
        got = eval(c["expr"], {"__builtins__": {}}, dict(NAMES))
        if abs(got - c["value"]) > 0.01 * max(abs(c["value"]), 1e-9):
            errors.append(f"{sid}: example computes to {got:.6g}, lesson says {c['value']}")
    print(f"{len(checks)} guide examples recomputed")
    print(f"{computed} answers recomputed, {reference} checked against a stated reference")
    for e in errors:
        print("ERROR:", e)
    print("FAILED" if errors else "OK")
    sys.exit(1 if errors else 0)


main()
