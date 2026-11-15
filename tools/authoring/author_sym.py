"""Adds a list of symbol definitions to every question and lesson, so that each explanation says what its variables stand for.
Symbols are found in the concept note, the solution and the lesson text; their meanings come from the glossary in sym_glossary.py.
Run after author_rev.py. Prints any symbol that has no definition yet."""
import json, os, re, glob, collections
from author_common import ROOT
from sym_glossary import G
import fig2
SUB = re.compile(r"(?<![A-Za-z])([A-Za-zαβγδεθλμνρστφω]'?_\{[^{}]+\})")
SEG = re.compile(r"([^.\n|]*?)=([^\n|]*?)(?=\. |\.$|\n|\|\||$)", re.M)
ONE = re.compile(r"(?<![A-Za-z_{}'^\\0-9])([A-Za-z])(?![A-Za-z_'{])")
def symbols(text):
    out = []
    for m in SUB.finditer(text):
        if m.group(1) not in out: out.append(m.group(1))
    for seg in SEG.finditer(text):
        s = seg.group(0)
        for m in ONE.finditer(s):
            c, i = m.group(1), m.start()
            if re.search(r"\d[,\d.]*\)? ?$", s[max(0, i - 8):i]): continue                    # a unit after a number
            if c in 'aAI' and re.match(r" [a-z]{2,}", s[i + 1:i + 5]) and not s[i + 1:].lstrip().startswith('='): continue   # a word
            if s[i - 1:i] in '/·' and re.search(r"[A-Za-z]$", s[:i - 1]): continue             # part of a compound unit
            if c not in out: out.append(c)
    return out
def pick(d, text, whole):
    """A meaning may be a list of (pattern, meaning): the first pattern found in the text decides. Lessons list every meaning."""
    if isinstance(d, str): return d
    if whole: return '; in other questions, '.join(dict.fromkeys(m for _, m in d))
    return next(m for p, m in d if not p or re.search(p, text, re.I))
def define(topic, sub, syms, text='', whole=False):
    got, miss = [], []
    for s in syms:
        d = G.get(sub, {}).get(s) or G.get(topic, {}).get(s) or G['*'].get(s)
        (got if d else miss).append([s, pick(d, text, whole)] if d else s)
    return got, miss
def main():
    missing = collections.defaultdict(collections.Counter); n = 0
    for f in sorted(glob.glob(os.path.join(ROOT, 'questions', '*.json'))):
        qs = json.load(open(f))
        for q in qs:
            fig2.post(q)
            _t = (q.get('stem') or '') + '\n' + (q.get('eli5') or '') + '\n' + (q.get('solution') or '')
            got, miss = define(q['topic'], q['subtopic'], symbols((q.get('eli5') or '') + '\n' + (q.get('solution') or '')), _t)
            for m in miss: missing[q['topic']][m] += 1
            if got: q['symbols'] = got; n += 1
            else: q.pop('symbols', None)
        json.dump(qs, open(f, 'w'), indent=1, ensure_ascii=False); open(f, 'a').write('\n')
    for f in sorted(glob.glob(os.path.join(ROOT, 'guide', '*.json'))):
        g = json.load(open(f))
        for s in g['sections']:
            txt = '\n'.join([s.get('body') or '', s.get('deep') or ''] + [x.get('expr', '') for x in s.get('formulas', [])] + [x['text'] for x in s.get('ideas', [])] + [x.get('steps', '') for x in s.get('examples', [])])
            got, miss = define(g['topic'], s.get('subtopic') or '', symbols(txt), txt, True)
            for m in miss: missing[g['topic']][m] += 1
            if got: s['symbols'] = got
            else: s.pop('symbols', None)
        json.dump(g, open(f, 'w'), indent=1, ensure_ascii=False); open(f, 'a').write('\n')
    print('questions with symbol definitions:', n, '| undefined symbols:', sum(len(v) for v in missing.values()))
    for t, c in missing.items(): print(' ', t, ' '.join(c))
if __name__ == '__main__': main()
