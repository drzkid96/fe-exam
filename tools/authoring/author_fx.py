"""Shared helpers for the later question-type scripts (author_f3.py onward).
NQ: one calculated question type in several numeric versions. `v1` is the hand-worked answer to the first version and the
formula must reproduce it. With `wrong` (three expressions for common mistakes) the type is multiple choice; without, numeric entry.
CQ: one rule-or-concept question type written out in two or more versions, each checked against a stated basis.
Each script runs twice: `base` (after author_f2.py base) creates first versions; `versions` (after the other version scripts) adds the rest."""
import sys, json, os, re
from author_v import *
from author_v import _load
import author_v
SPECS = []
def NQ(sub, find, unit, dp, v1, stem, concept, sol, ans, wrong=None, tol=0.01, units='SI', fig=None, **P):
    SPECS.append(dict(kind='n', sub=sub, find=find, unit=unit, dp=dp, v1=v1, stem=stem, concept=concept, sol=sol, ans=ans, wrong=wrong, tol=tol, units=units, fig=fig, P=P))
def CQ(sub, find, concept, basis, *vers):
    assert len(vers) >= 2 and all(len(v) == 4 and len(v[1]) == 4 for v in vers), vers[0][0]
    SPECS.append(dict(kind='c', sub=sub, find=find, concept=concept, basis=basis, vers=vers))
PICK = {'E', 'Fy', 'db', 'Fnv', 'Av', 'fy', 'Es'}          # catalogue values: taken from an existing version, never averaged
RX = re.compile(r'\[([^\[\]|]+)(?:\|\d)?\]')
def _dec(v): t = repr(float(v)); return 0 if float(v) == int(v) else len(t.split('.')[1])
def blend(P, a, b, pick):
    """A further parameter set: the average of versions a and b, which keeps any ordering that both of them satisfy."""
    out = {}
    for n, vals in P.items():
        if not all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in vals): return None
        if n in PICK or len(set(vals)) < len(vals): out[n] = vals[pick]; continue
        d = max(_dec(v) for v in vals); x = round((vals[a] + vals[b]) / 2, d); out[n] = int(x) if d == 0 and all(isinstance(v, int) for v in vals) else x
    return None if any(all(out[n] == vals[k] for n, vals in P.items()) for k in range(len(next(iter(P.values()))))) else out
def _vals(sp, e):
    e = dict(NAMES, **e); e['ans'] = eval(sp['ans'], {'__builtins__': {}}, e)
    return [float(eval(m.group(1), {'__builtins__': {}}, e)) for m in RX.finditer(sp['stem'] + ' ' + sp['sol']) if isinstance(eval(m.group(1), {'__builtins__': {}}, e), (int, float))] + [float(e['ans'])] + [float(eval(w, {'__builtins__': {}}, e)) for w in (sp['wrong'] or [])]
def plausible(sp, new):
    """True if every number the new set produces has the sign, and roughly the size, that the written versions produce."""
    if re.search(r'inside the loaded|which is less than|greater than 1|assumption holds|still below', sp['sol'] + sp['stem']): return False
    try:
        n = len(next(iter(sp['P'].values()))); old = [_vals(sp, {k: v[i] for k, v in sp['P'].items()}) for i in range(n)]; got = _vals(sp, new)
    except Exception: return False
    if any(len(o) != len(got) for o in old): return False
    for i, g in enumerate(got):
        col = [o[i] for o in old]
        if g != g or abs(g) == float('inf'): return False
        if all(c > 0 for c in col) and not (min(col) / 4 <= g <= max(col) * 4): return False
        if all(c < 0 for c in col) and not (max(col) / 4 >= g >= min(col) * 4): return False
    w = got[-(len(sp['wrong'] or []) + 1):]
    ac = [abs(o[len(got) - len(w)]) for o in old]
    if min(ac) > 0 and not (min(ac) / 4 <= abs(w[0]) <= max(ac) * 4): return False
    if abs(round(w[0], sp['dp']) - w[0]) > 0.004 * abs(w[0]) or any(abs(round(x, sp['dp']) - x) > 0.015 * abs(x) for x in w[1:]): return False     # the rounded answer must stay inside the marking tolerance
    return all(abs(w[i] - w[j]) > 0.02 * max(abs(w[i]), abs(w[j]), 1e-9) for i in range(len(w)) for j in range(i))
def fourth(sp):
    """Adds a fourth version to a three-version type when a plausible one can be derived."""
    if sp['kind'] != 'n' or len(next(iter(sp['P'].values()))) != 3: return
    for a, b, pk in ((0, 1, 2), (0, 2, 1), (1, 2, 0)):
        new = blend(sp['P'], a, b, pk)
        if new and plausible(sp, new):
            for k in sp['P']: sp['P'][k] = list(sp['P'][k]) + [new[k]]
            return
def example(sp):
    """A parameter set for a lesson example that no version uses."""
    n = len(next(iter(sp['P'].values())))
    for a, b, pk in ((1, 2, 0), (0, 2, 1), (2, 3, 0), (1, 3, 2)) if n == 4 else ((1, 2, 0), (0, 2, 1)):
        new = blend(sp['P'], a, b, pk)
        if new and plausible(sp, new): return new
def _env(sp, k=0):
    e = dict(NAMES); e.update({n: v[k] for n, v in sp['P'].items()}); e['ans'] = eval(sp['ans'], {'__builtins__': {}}, e); return e
def _fmt(v, dp, unit): return ('$' + nf(v, dp) + unit[1:]) if unit.startswith('$') else (nf(v, dp) + ' ' + unit).strip()
def _stem0(sp): return sp['vers'][0][0] if sp['kind'] == 'c' else render(sp['stem'], _env(sp))
def base_mode(tag):
    from author_dsl import N, M, save as dsave
    seen = set()
    for sp in SPECS:
        s0 = _stem0(sp); assert s0 not in seen, 'duplicate stem: ' + s0[:60]; seen.add(s0)
        if sp['kind'] == 'c':
            stem, options, ci, sol = sp['vers'][0]; M(sp['sub'], stem, options, ci, sp['concept'], sol, basis=sp['basis']); continue
        e = _env(sp); val = e['ans']
        assert abs(val - sp['v1']) <= 0.011 * max(abs(sp['v1']), 1e-9), ('hand value differs', sp['stem'][:50], val, sp['v1'])
        calc = "(lambda %s: %s)(%s)" % (', '.join(sp['P']), sp['ans'], ', '.join(repr(v[0]) for v in sp['P'].values()))
        if sp['wrong']:
            pos = len(sp['stem']) % 4; ws = [eval(w, {'__builtins__': {}}, e) for w in sp['wrong']]; allv = ws[:pos] + [val] + ws[pos:]
            for i in range(4):
                for j in range(i): assert abs(allv[i] - allv[j]) > 0.015 * max(abs(allv[i]), abs(allv[j]), 1e-9), ('options too close', sp['stem'][:50], allv)
            M(sp['sub'], render(sp['stem'], e), [_fmt(v, sp['dp'], sp['unit']) for v in allv], pos, render(sp['concept'], e), render(sp['sol'], e), calc=calc, units=sp['units'])
        else:
            N(sp['sub'], render(sp['stem'], e), round(val, sp['dp']), sp['unit'], render(sp['concept'], e), render(sp['sol'], e), calc, tol=sp['tol'], units=sp['units'])
    dsave(tag); print(tag, 'bases added:', len(SPECS))
def versions_mode(tag):
    find = {}
    for sp in SPECS:
        fourth(sp)
        topic = sp['sub'].rsplit('-', 1)[0]; bank = _load(topic); s0 = _stem0(sp).replace(' || ', '\n\n')
        i = next(k for k, x in enumerate(bank) if x['stem'] == s0); b = bank[i]; base = b['id']; find[base] = sp['find']
        if sp['kind'] == 'n':
            V(base, sp['stem'], sp['P'], sp['ans'], sp['sol'], sp['wrong'], sp['dp'], sp['fig'], None, sp['concept'])
            if author_v.ERRS and author_v.ERRS[-1].startswith(base + ':') and len(next(iter(sp['P'].values()))) == 4:      # the derived version did not pass: keep the three written ones
                author_v.ERRS.pop(); sp['P'] = {k: v[:3] for k, v in sp['P'].items()}; V(base, sp['stem'], sp['P'], sp['ans'], sp['sol'], sp['wrong'], sp['dp'], sp['fig'], None, sp['concept'])
            continue
        n = len(sp['vers']); b.update(family=base, version=1, versions=n); out = []
        for k, (stem, options, ci, sol) in enumerate(sp['vers'][1:], 1):
            q = json.loads(json.dumps(b)); q.update(id=base + '-' + 'bcdefgh'[k - 1], version=k + 1, stem=stem.replace(' || ', '\n\n'), options=[{'id': 'abcd'[j], 'text': t} for j, t in enumerate(options)], answer='abcd'[ci], solution=sol.replace(' || ', '\n\n'))
            out.append(q)
        bank[i + 1:i + 1] = out; author_v.STATS['families'] += 1; author_v.STATS['versions'] += n
    save(); json.dump(find, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'find_%s.json' % tag), 'w'), indent=1)
def run(tag):
    if sys.argv[1:] == ['base']: base_mode(tag)
    else: versions_mode(tag)
