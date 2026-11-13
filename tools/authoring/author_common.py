import json, os
ROOT = __import__('os').environ.get('FE_REPO', __import__('os').path.abspath(__import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))) + '/site/content'
HBP = {'Ethics and Professional Practice': '4–12', 'Mathematics': '34–62', 'Engineering Probability and Statistics': '63–84',
       'Materials Science/Structure of Matter': '94–106', 'Statics': '107–113', 'Dynamics': '114–129', 'Mechanics of Materials': '130–142',
       'Fluid Mechanics': '177–203', 'Engineering Economics': '230–237', 'Civil Engineering': '259–309', 'Environmental Engineering': '310–354'}
def hb(*sections): return [{'section': s, 'page': HBP[s]} for s in sections]
def opts(*texts): return [{'id': chr(97 + i), 'text': t} for i, t in enumerate(texts)]
def ids(prefix_pairs): return [{'id': a, 'text': b} for a, b in prefix_pairs]
def q(id, sub, fmt, stem, answer, eli5, solution, handbook, verify='computed', basis=None, diff=2, units='SI', tags=(), **extra):
    d = {'id': id, 'topic': sub.rsplit('-', 1)[0], 'subtopic': sub, 'format': fmt, 'status': 'live', 'difficulty': diff, 'units': units, 'stem': stem}
    d.update(extra)
    d.update({'answer': answer, 'eli5': eli5, 'solution': solution, 'handbook': handbook, 'tags': list(tags), 'source': 'original'})
    d['verify'] = {'method': verify, **({'basis': basis} if basis else {})}
    return d
def num(value, unit, tol=0.01): return {'value': value, 'tolerance': tol, 'toleranceType': 'rel', 'unit': unit}
def dump(topic, items):
    assert all(x['topic'] == topic for x in items), topic
    with open(os.path.join(ROOT, 'questions', topic + '.json'), 'w') as f:
        json.dump(items, f, indent=1, ensure_ascii=False); f.write('\n')
    print(topic, len(items))
