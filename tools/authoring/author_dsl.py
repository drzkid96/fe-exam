"""Compact authoring helpers for batch 2. Run after author_a.py and author_b.py; appends to the topic files."""
from author_common import *
import json, os, re
TOPIC_HB = {'math': ['Mathematics', 'Engineering Probability and Statistics'], 'ethics': ['Ethics and Professional Practice'], 'econ': ['Engineering Economics'],
            'statics': ['Statics'], 'dynamics': ['Dynamics'], 'mechmat': ['Mechanics of Materials'], 'materials': ['Materials Science/Structure of Matter', 'Civil Engineering'],
            'fluids': ['Fluid Mechanics'], 'surveying': ['Civil Engineering'], 'water': ['Civil Engineering', 'Environmental Engineering'],
            'structural': ['Civil Engineering', 'Mechanics of Materials'], 'geotech': ['Civil Engineering'], 'transport': ['Civil Engineering'], 'construction': ['Civil Engineering']}
BANK, EXPR = {}, {}
def T(s): return s.replace(' || ', '\n\n')
def _load(topic):
    if topic not in BANK: BANK[topic] = json.load(open(os.path.join(ROOT, 'questions', topic + '.json')))
    return BANK[topic]
def _add(sub, fmt, stem, answer, eli5, sol, calc, basis, units, **extra):
    topic = sub.rsplit('-', 1)[0]; bank = _load(topic)
    qid = '%s-%04d' % (topic, max(int(x['id'].rsplit('-', 1)[1]) for x in bank) + 1)
    bank.append(q(qid, sub, fmt, T(stem), answer, T(eli5), T(sol), hb(*TOPIC_HB[topic]), verify='computed' if calc else 'reference', basis=basis, units=units, **extra))
    if calc: EXPR[qid] = calc
def M(sub, stem, options, ans, eli5, sol, calc=None, basis=None, units='SI'):
    assert calc or basis, stem
    _add(sub, 'mcq', stem, 'abcd'[ans], eli5, sol, calc, basis, units, options=opts(*options))
def N(sub, stem, value, unit, eli5, sol, calc, tol=0.01, units='SI'):
    _add(sub, 'numeric', stem, num(value, unit, tol), eli5, sol, calc, None, units)
def save(expr_file):
    for topic, items in BANK.items(): dump(topic, items)
    path = __import__('os').environ.get('FE_REPO', __import__('os').path.abspath(__import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))) + '/tools/calc_expr.json'
    allx = json.load(open(path)) if os.path.exists(path) else {}
    allx.update(EXPR)
    json.dump(dict(sorted(allx.items())), open(path, 'w'), indent=1); open(path, 'a').write('\n')
    print('expressions:', len(allx))
