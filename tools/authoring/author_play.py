"""Puts an exam playbook at the top of every lesson: the hand-written fast moves (playbook.py) and, from the question bank,
every question type in the lesson with its exact ask, the handbook page to open, a target time (from the number of calculation steps in its solution) and a link to try it.
Topic overviews get the topic's share of the exam. Run last among the lesson scripts."""
import json, os, re, glob
from author_common import ROOT
from playbook import PLAY

exam = json.load(open(os.path.join(ROOT, 'exam.json'))); per = exam['examMinutes'] / exam['questionCount']
qs = [q for f in sorted(glob.glob(os.path.join(ROOT, 'questions', '*.json'))) for q in json.load(open(f))]
first = {}
for q in qs:
    fam = q.get('family') or q['id']
    if fam not in first or q.get('version', 1) < first[fam].get('version', 1): first[fam] = q

def ask(stem):
    t = re.sub(r'\s+', ' ', stem.replace('**', '')).strip()
    parts = re.split(r'(?<=[.?])\s+(?=[A-Z])', t); qn = [p for p in parts if p.endswith('?')]
    do = [p for p in parts if re.match(r'(Click|Select|Choose|Find|Determine|Calculate|Compute|Match|Drag|Put|Order|Arrange|Estimate|Identify|Classify|Rank)\b', p)]
    a = (qn or do or parts)[-1]
    return a if len(a) <= 140 else a[:137].rsplit(' ', 1)[0] + '...'

n_rows = n_types = 0; missing = []
for t in exam['topics']:
    path = os.path.join(ROOT, 'guide', t['id'] + '.json'); g = json.load(open(path))
    lo, hi = t['min'], t['max']; share = f"{lo} to {hi} of the {exam['questionCount']} exam questions"
    for s in g['sections']:
        sub = s.get('subtopic')
        if s['id'].endswith('-overview'):
            br = s.get('bridge') or {}
            s['play'] = {'intro': f"{t['name']}: {share}. At about {per:.1f} minutes a question, that is roughly {lo * per:.0f} to {hi * per:.0f} minutes of the exam." +
                         (' ' + br['exam'] if br.get('exam') else '') + ' Work the lessons below in the order of the map; open each lesson\'s playbook first.', 'rows': [], 'types': []}
            continue
        if not sub: continue
        rows = PLAY.get(sub)
        if not rows: missing.append(sub); continue
        types = []
        for fam, q in sorted(first.items()):
            if q.get('subtopic') != sub: continue
            hb = (q.get('handbook') or [{}])[0] if q.get('lookup') is not False else {}
            calc = (q.get('verify') or {}).get('method') == 'computed'
            steps = sum(1 for ln in re.split(r'\n+|(?<=\.)\s+(?=[A-Z])', q.get('solution', '')) if '=' in ln)
            tmin = 1 if not calc else 1.5 if steps <= 1 else 2 if steps == 2 else 3 if steps <= 4 else 4
            types.append({'id': q['id'], 'ask': ask(q['stem']), 'section': hb.get('section', ''), 'page': hb.get('page', ''), 'find': (hb.get('find') or [])[:1],
                          'time': f"about {tmin:g} min", 'n': q.get('versions', 1)})
        s['play'] = {'intro': f"{t['name']} is {share}. This lesson's questions: recognise the type in the left column, make the move on the right, and stay near {per:.0f} minutes each.",
                     'rows': [list(r) for r in rows], 'types': types}
        n_rows += len(rows); n_types += len(types)
    json.dump(g, open(path, 'w'), indent=1, ensure_ascii=False); open(path, 'a').write('\n')
print('playbook rows:', n_rows, '| question types listed:', n_types, '| lessons without a playbook:', missing or 'none')
