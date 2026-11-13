"""Authoring helpers for subtopic lessons. Each lesson: plain-words explanation, key formulas, a worked example whose number is recomputed, and common mistakes."""
from author_common import *
from author_dsl import TOPIC_HB, T
import json, os
SECS, CHECKS = {}, {}
def G(sub, title, body, F=(), ex=None, pit=()):
    topic = sub.rsplit('-', 1)[0]
    hbs = TOPIC_HB[topic][0]
    s = {'id': sub + '-lesson', 'subtopic': sub, 'title': title, 'body': T(body),
         'formulas': [{'name': n, 'expr': e, 'handbook': hbs + ', p. ' + HBP[hbs]} for n, e in F], 'pitfalls': list(pit), 'updated': '2026-11-13'}
    if ex:
        s['example'] = {'problem': ex[0], 'steps': T(ex[1])}
        if len(ex) > 2: CHECKS[s['id']] = {'expr': ex[3], 'value': ex[2]}
    SECS.setdefault(topic, []).append(s)
def save():
    for topic, lessons in SECS.items():
        path = os.path.join(ROOT, 'guide', topic + '.json')
        g = json.load(open(path))
        g['sections'] = [x for x in g['sections'] if not x.get('subtopic')] + lessons     # keep the topic overview
        json.dump(g, open(path, 'w'), indent=1, ensure_ascii=False); open(path, 'a').write('\n')
        print(topic, len(g['sections']))
    path = __import__('os').environ.get('FE_REPO', __import__('os').path.abspath(__import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))) + '/tools/guide_checks.json'
    allc = json.load(open(path)) if os.path.exists(path) else {}
    allc.update(CHECKS); json.dump(dict(sorted(allc.items())), open(path, 'w'), indent=1); open(path, 'a').write('\n')
    print('example checks:', len(allc))
