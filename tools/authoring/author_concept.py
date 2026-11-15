"""Adds concept figures to every lesson (the idea drawn, not a worked problem) and a connection map to every topic overview.
Run after author_fig.py and author_me.py (it reads the prerequisite map)."""
import json, os
import concept_figs as C
from author_common import ROOT
from author_me import NEEDS

SHORT = {
 'math-a': 'Lines and curves', 'math-b': 'Calculus', 'math-c': 'Vectors', 'math-d': 'Statistics',
 'statics-a': 'Resultants', 'statics-b': 'Moments, couples', 'statics-c': 'Equilibrium', 'statics-d': 'Trusses, frames', 'statics-e': 'Centroids', 'statics-f': 'Moment of inertia', 'statics-g': 'Friction',
 'dynamics-a': 'Kinematics', 'dynamics-b': 'Mass inertia', 'dynamics-c': 'F = m a', 'dynamics-d': 'Work and energy',
 'mechmat-a': 'Shear and moment', 'mechmat-b': 'Stress and strain', 'mechmat-c': 'Deformations', 'mechmat-d': "Mohr's circle",
 'materials-a': 'Mix design', 'materials-b': 'Test methods', 'materials-c': 'Material properties',
 'fluids-a': 'Flow measurement', 'fluids-b': 'Fluid properties', 'fluids-c': 'Fluid statics', 'fluids-d': 'Energy, momentum',
 'water-a': 'Hydrology', 'water-b': 'Hydraulics', 'water-c': 'Pumps', 'water-d': 'Distribution', 'water-e': 'Flood control', 'water-f': 'Stormwater', 'water-g': 'Collection', 'water-h': 'Groundwater', 'water-i': 'Water quality', 'water-j': 'Testing, standards', 'water-k': 'Treatment',
 'structural-a': 'Determinate analysis', 'structural-b': 'Deflection', 'structural-c': 'Columns', 'structural-d': 'Determinacy', 'structural-e': 'Indeterminate', 'structural-f': 'Loads, load paths', 'structural-g': 'Steel design', 'structural-h': 'Concrete design',
 'geotech-a': 'Classification', 'geotech-b': 'Phase relations', 'geotech-c': 'Lab, field tests', 'geotech-d': 'Effective stress', 'geotech-e': 'Retaining walls', 'geotech-f': 'Shear strength', 'geotech-g': 'Bearing capacity', 'geotech-h': 'Foundation types', 'geotech-i': 'Consolidation', 'geotech-j': 'Slope stability', 'geotech-k': 'Stabilization',
 'transport-a': 'Geometric design', 'transport-b': 'Pavements', 'transport-c': 'Traffic flow', 'transport-d': 'Signals, devices', 'transport-e': 'Planning',
 'surveying-a': 'Angles, distances', 'surveying-b': 'Areas', 'surveying-c': 'Earthwork volumes', 'surveying-d': 'Coordinates', 'surveying-e': 'Leveling',
 'construction-a': 'Administration', 'construction-b': 'Operations', 'construction-c': 'Project controls', 'construction-d': 'Estimating', 'construction-e': 'Drawings',
 'econ-a': 'Time value', 'econ-b': 'Cost', 'econ-c': 'Analyses', 'econ-d': 'Uncertainty',
 'ethics-a': 'Codes of ethics', 'ethics-b': 'Liability', 'ethics-c': 'Licensure', 'ethics-d': 'Contracts'}
C.TNAME.update(math='Math', statics='Statics', dynamics='Dynamics', mechmat='Mechanics', materials='Materials', fluids='Fluids', water='Water', structural='Structural', geotech='Geotech',
               transport='Transport', surveying='Surveying', construction='Construction', econ='Econ', ethics='Ethics')

FIGS = {s: [f] for s, f in {
 'math-a': C.math_a, 'math-b': C.math_b, 'math-c': C.math_c, 'math-d': C.math_d,
 'statics-a': C.statics_a, 'statics-b': C.statics_b, 'statics-c': C.statics_c, 'statics-d': C.statics_d, 'statics-e': C.statics_e, 'statics-f': C.statics_f, 'statics-g': C.statics_g,
 'dynamics-a': C.dynamics_a, 'dynamics-b': C.dynamics_b, 'dynamics-c': C.dynamics_c, 'dynamics-d': C.dynamics_d,
 'mechmat-a': C.mechmat_a, 'mechmat-c': C.mechmat_c, 'mechmat-d': C.mechmat_d,
 'structural-a': C.structural_a, 'structural-b': C.structural_b, 'structural-c': C.structural_c, 'structural-d': C.structural_d, 'structural-e': C.structural_e, 'structural-f': C.structural_f, 'structural-g': C.structural_g, 'structural-h': C.structural_h,
 'fluids-a': C.fluids_a, 'fluids-b': C.fluids_b, 'fluids-d': C.fluids_d,
 'water-a': C.water_a, 'water-b': C.water_b, 'water-c': C.water_c, 'water-d': C.water_d, 'water-e': C.water_e, 'water-f': C.water_f, 'water-g': C.water_g, 'water-h': C.water_h, 'water-i': C.water_i, 'water-j': C.water_j,
 'geotech-b': C.geotech_b, 'geotech-c': C.geotech_c, 'geotech-d': C.geotech_d, 'geotech-e': C.geotech_e, 'geotech-f': C.geotech_f, 'geotech-g': C.geotech_g, 'geotech-h': C.geotech_h, 'geotech-i': C.geotech_i, 'geotech-j': C.geotech_j, 'geotech-k': C.geotech_k,
 'materials-a': C.materials_a, 'materials-b': C.materials_b, 'materials-c': C.materials_c,
 'surveying-a': C.surveying_a, 'surveying-b': C.surveying_b, 'surveying-c': C.surveying_c, 'surveying-d': C.surveying_d, 'surveying-e': C.surveying_e,
 'transport-a': C.transport_a, 'transport-b': C.transport_b, 'transport-c': C.transport_c, 'transport-d': C.transport_d, 'transport-e': C.transport_e,
 'construction-a': C.construction_a, 'construction-b': C.construction_b, 'construction-c': C.construction_c, 'construction-d': C.construction_d, 'construction-e': C.construction_e,
 'econ-a': C.econ_a, 'econ-b': C.econ_b, 'econ-c': C.econ_c, 'econ-d': C.econ_d,
 'ethics-a': C.ethics_a, 'ethics-b': C.ethics_b, 'ethics-c': C.ethics_c, 'ethics-d': C.ethics_d}.items()}
FIGS['mechmat-b'] = [C.mechmat_b1, C.mechmat_b2]; FIGS['fluids-c'] = [C.fluids_c1, C.fluids_c2]; FIGS['geotech-a'] = [C.geotech_a1, C.geotech_a2]; FIGS['water-k'] = [C.water_k1, C.water_k2]

def order(ids):
    """Study order inside a topic: prerequisites first, otherwise the exam order."""
    out, left = [], list(ids)
    while left:
        for s in left:
            if all(p in out or p not in ids for p in NEEDS.get(s, [])): out.append(s); left.remove(s); break
        else: out += left; break
    return out

exam = json.load(open(os.path.join(ROOT, 'exam.json'))); n = m = 0
for t in exam['topics']:
    path = os.path.join(ROOT, 'guide', t['id'] + '.json'); g = json.load(open(path)); code = {u['id']: u['code'] for u in t['subtopics']}
    for s in g['sections']:
        sub = s.get('subtopic')
        if sub in FIGS:
            s['figures'] = []
            for fn in FIGS[sub]:
                f = fn(); s['figures'].append(dict(f, caption=f['alt'])); n += 1
        elif s['id'].endswith('-overview'):
            ids = order([u['id'] for u in t['subtopics']])
            f = C.topic_map(t['name'], [(i, code[i], SHORT[i]) for i in ids], NEEDS, SHORT, C.TNAME[t['id']])
            s['figures'] = [dict(f, caption='How this topic connects. The middle column is a suggested study order; the left column lists earlier lessons to refresh first; the right column shows where this topic is used again.')]; m += 1
    json.dump(g, open(path, 'w'), indent=1, ensure_ascii=False); open(path, 'a').write('\n')
missing = [u['id'] for t in exam['topics'] for u in t['subtopics'] if u['id'] not in FIGS]
print('concept figures:', n, '| topic maps:', m, '| lessons without one:', missing or 'none')
