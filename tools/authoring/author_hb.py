"""Adds a handbook lookup to every question: the section and page range, plus the words to search for in the handbook PDF.
'-' marks a question that is not a handbook lookup (a rule to know, or plain arithmetic). 'Section::terms' overrides the section."""
import json, os, glob
from author_common import ROOT, HBP
HBP = dict(HBP); HBP.setdefault('Safety', '13–33'); HBP.setdefault('Chemical Engineering', '238–258'); HBP.setdefault('Units and Conversion Factors', '1–3'); HBP.setdefault('Chemistry and Biochemistry', '85–93'); HBP.setdefault('Industrial and Systems Engineering', '417–430'); HBP.setdefault('Mechanical Engineering', '431–460')
MM, CE, EN, MA, PS = 'Mechanics of Materials', 'Civil Engineering', 'Environmental Engineering', 'Mathematics', 'Engineering Probability and Statistics'
FIND = {
 'statics-0001': 'resultant; resolution of a force', 'statics-0002': 'equilibrium requirements; systems of forces', 'statics-0003': 'centroid', 'statics-0004': 'friction',
 'statics-0005': 'moment of inertia', 'statics-0006': 'couple; moments', 'statics-0007': 'couple; systems of forces', 'statics-0008': 'method of joints; truss', 'statics-0009': 'method of joints; method of sections',
 'statics-0010': 'moments; cross product', 'statics-0011': 'equilibrium requirements', 'statics-0012': 'centroid', 'statics-0013': 'parallel axis; moment of inertia', 'statics-0014': 'friction', 'statics-0015': 'concurrent forces; equilibrium requirements',
 'dynamics-0001': 'constant acceleration; particle kinematics', 'dynamics-0002': "Newton's second law; friction", 'dynamics-0003': 'conservation of energy; potential energy', 'dynamics-0004': 'mass moment of inertia; parallel axis',
 'dynamics-0005': 'projectile motion', 'dynamics-0006': 'normal and tangential components', 'dynamics-0007': 'mass moment of inertia', 'dynamics-0008': "Newton's second law", 'dynamics-0009': 'kinetics of a rigid body; mass moment of inertia',
 'dynamics-0010': 'power and efficiency; work', 'dynamics-0011': 'elastic potential energy; work and energy',
 'econ-0001': 'single payment compound amount', 'econ-0002': 'capital recovery', 'econ-0003': 'break-even analysis', 'econ-0004': PS + '::expected value', 'econ-0005': 'break-even analysis', 'econ-0006': '-',
 'econ-0007': 'single payment present worth', 'econ-0008': 'non-annual compounding; effective annual interest', 'econ-0009': 'benefit-cost analysis; uniform series present worth', 'econ-0010': 'capital recovery; sinking fund', 'econ-0011': PS + '::expected value',
 'ethics-0001': 'obligation to the public', 'ethics-0002': 'responsible charge; sign and seal', 'ethics-0003': 'conflicts of interest; obligation to employer', 'ethics-0004': 'licensure; model law', 'ethics-0005': '-', 'ethics-0006': '-',
 'ethics-0007': '-', 'ethics-0008': '-', 'ethics-0009': 'gratuities; obligation to employer',
 'fluids-0001': 'pressure field in a static liquid', 'fluids-0002': 'specific gravity; specific weight', 'fluids-0003': 'continuity equation', 'fluids-0004': 'Pitot tube', 'fluids-0005': 'forces on submerged surfaces; center of pressure',
 'fluids-0006': 'orifice', 'fluids-0007': 'Reynolds number', 'fluids-0008': 'kinematic viscosity', 'fluids-0009': 'manometer', 'fluids-0010': 'buoyancy; Archimedes', 'fluids-0011': 'Bernoulli equation; energy equation',
 'fluids-0012': 'impulse-momentum principle', 'fluids-0013': 'Darcy-Weisbach; head loss',
 'geotech-0001': 'water content; dry unit weight', 'geotech-0002': 'void ratio', 'geotech-0003': 'effective stress', 'geotech-0004': 'Rankine; active', 'geotech-0005': 'Mohr-Coulomb', 'geotech-0006': 'plasticity index',
 'geotech-0007': 'effective stress', 'geotech-0008': 'Unified Soil Classification', 'geotech-0009': 'coefficient of uniformity; coefficient of curvature', 'geotech-0010': 'relative compaction', 'geotech-0011': 'coefficient of permeability; constant head',
 'geotech-0012': 'Rankine; active force', 'geotech-0013': 'unconfined; undrained shear strength', 'geotech-0014': 'ultimate bearing capacity', 'geotech-0015': 'bearing capacity', 'geotech-0016': '-', 'geotech-0017': '-',
 'geotech-0018': 'compression index; normally consolidated', 'geotech-0019': 'time factor; coefficient of consolidation', 'geotech-0020': 'slope failure; factor of safety', 'geotech-0021': 'slope failure; factor of safety', 'geotech-0022': '-', 'geotech-0023': '-',
 'materials-0001': CE + '::water-cement ratio', 'materials-0002': CE + '::compressive strength', 'materials-0003': 'Materials Science/Structure of Matter::hardness; impact test', 'materials-0004': MM + "::Hooke's law; modulus of elasticity",
 'materials-0005': '-', 'materials-0006': '-', 'materials-0007': 'Materials Science/Structure of Matter::hardness', 'materials-0008': CE + '::reinforcement bar', 'materials-0009': CE + '::modulus of elasticity; ACI 318',
 'materials-0010': 'Materials Science/Structure of Matter::percent elongation; ductility', 'materials-0011': 'Materials Science/Structure of Matter::toughness; stress-strain',
 'math-0001': MA + '::straight line', 'math-0002': MA + '::integral calculus; indefinite integrals', 'math-0003': MA + '::dot product', 'math-0004': PS + '::standard deviation; dispersion', 'math-0005': PS + '::normal distribution',
 'math-0006': MA + '::conic sections; circle', 'math-0007': MA + '::distance between two points', 'math-0008': MA + '::law of cosines', 'math-0009': MA + '::differential calculus; derivative', 'math-0010': MA + '::test for a maximum',
 'math-0011': MA + '::integral calculus', 'math-0012': MA + '::cross product', 'math-0013': MA + '::vectors', 'math-0014': PS + '::probability', 'math-0015': PS + '::unit normal; normal distribution', 'math-0016': PS + '::least squares; linear regression', 'math-0017': PS + '::binomial distribution',
 'mechmat-0001': 'uniaxial loading; stress', 'mechmat-0002': 'uniaxial loading and deformation', 'mechmat-0003': 'shearing force and bending moment; simply supported beam', 'mechmat-0004': "Mohr's circle; principal stresses", 'mechmat-0005': 'stresses in beams; section modulus',
 'mechmat-0006': 'deflection of beams; beam slopes and deflections', 'mechmat-0007': 'shearing force and bending moment', 'mechmat-0008': 'shearing force and bending moment', 'mechmat-0009': 'torsion; polar moment of inertia', 'mechmat-0010': 'thermal deformations',
 'mechmat-0011': 'thermal deformations', 'mechmat-0012': "Mohr's circle; maximum in-plane shear", 'mechmat-0013': 'cylindrical pressure vessel',
 'structural-0001': CE + '::determinacy; classification of structures', 'structural-0002': MM + "::Euler's formula; columns", 'structural-0003': MM + '::simply supported beam slopes and deflections', 'structural-0004': CE + '::load combinations; LRFD',
 'structural-0005': CE + '::ACI 318; singly-reinforced', 'structural-0006': MM + '::shearing force and bending moment; cantilever', 'structural-0007': MM + '::shearing force and bending moment', 'structural-0008': MM + '::shearing force and bending moment',
 'structural-0009': MM + '::cantilevered beam slopes and deflections', 'structural-0010': MM + '::effective length; columns', 'structural-0011': CE + '::determinacy; classification of structures', 'structural-0012': MM + '::cantilevered beam slopes and deflections',
 'structural-0013': CE + '::fixed-end moment', 'structural-0014': '-', 'structural-0015': CE + '::tension members; yielding', 'structural-0016': CE + '::AISC; plastic section modulus', 'structural-0017': MM + '::slenderness; radius of gyration',
 'structural-0018': CE + '::ACI 318; stress block', 'structural-0019': CE + '::ACI 318; shear', 'structural-0020': CE + '::ACI 318; short columns',
 'surveying-0001': '-', 'surveying-0002': 'area by coordinates', 'surveying-0003': 'average end area; earthwork formulas', 'surveying-0004': '-', 'surveying-0005': '-', 'surveying-0006': MA + '::trigonometry', 'surveying-0007': MA + '::regular polygon',
 'surveying-0008': MA + '::trigonometry; law of sines', 'surveying-0009': 'earthwork formulas', 'surveying-0010': 'latitude; departure', 'surveying-0011': 'latitude; departure',
 'transport-0001': 'stopping sight distance', 'transport-0002': 'horizontal curves; superelevation', 'transport-0003': 'traffic flow relationships', 'transport-0004': 'peak hour factor', 'transport-0005': 'vertical curves', 'transport-0006': '-',
 'transport-0007': 'structural number', 'transport-0008': '-', 'transport-0009': 'ESAL; load equivalency', 'transport-0010': 'saturation flow; capacity', 'transport-0011': 'traffic flow relationships; Greenshields', 'transport-0012': 'vehicle signal change interval; yellow',
 'transport-0013': 'trip generation', 'transport-0014': 'crash rate; traffic safety equations', 'transport-0015': 'logit', 'transport-0016': 'horizontal curves', 'transport-0017': 'horizontal curves', 'transport-0018': 'vertical curves; sight distance',
 'water-0001': CE + '::rational formula', 'water-0002': CE + "::Manning's equation; hydraulic radius", 'water-0003': 'Fluid Mechanics::pump power equation', 'water-0004': EN + '::hydraulic residence time; sedimentation', 'water-0005': CE + "::Darcy's law", 'water-0006': '-',
 'water-0007': CE + '::NRCS; curve number', 'water-0008': CE + '::critical depth', 'water-0009': 'Fluid Mechanics::affinity laws; scaling laws', 'water-0010': '-', 'water-0011': 'Fluid Mechanics::pressure field in a static liquid', 'water-0012': '-', 'water-0013': '-',
 'water-0014': '-', 'water-0015': CE + '::rational formula', 'water-0016': CE + "::Manning's equation", 'water-0017': '-', 'water-0018': CE + "::Darcy's law; seepage velocity", 'water-0019': EN + '::BOD', 'water-0020': EN + '::hardness; equivalent weight',
 'water-0021': 'Safety::sound pressure level; noise', 'water-0022': '-', 'water-0023': EN + '::overflow rate; clarifier', 'water-0024': '-',
 'fluids-0014': 'impulse-momentum principle; deflectors and blades', 'surveying-0012': 'trapezoidal rule', 'surveying-0013': 'latitude; departure', 'water-0025': EN + '::BOD', 'water-0026': 'Fluid Mechanics::Froude number',
 'geotech-0024': 'water content', 'structural-0021': CE + '::fixed-end moment', 'dynamics-0012': 'mass moment of inertia; parallel axis', 'mechmat-0014': 'torsion; angle of twist',
 'construction-0001': 'CPM; float', 'construction-0002': 'earned-value analysis', 'construction-0003': '-', 'construction-0004': '-', 'construction-0005': '-', 'construction-0006': '-', 'construction-0007': '-', 'construction-0008': '-', 'construction-0009': '-',
 'construction-0010': '-', 'construction-0011': 'Safety::incidence rate', 'construction-0012': '-', 'construction-0013': 'earned-value analysis; schedule variance', 'construction-0014': '-', 'construction-0015': '-', 'construction-0016': '-',
}
for _f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'find*.json'))): FIND.update(json.load(open(_f)))
# Search words corrected against the handbook itself (edition 10.0.1): the handbook's own wording, or None where it has no entry.
FIX = {'ESAL': None, 'Mohr-Coulomb': 'major principal stress', 'angle of twist': 'twist', 'break-even analysis': 'breakeven analysis', 'coefficient of consolidation': 'time factor',
       'coefficient of curvature': 'coefficient of concavity', 'effective annual interest': 'effective interest rate', 'equivalent weight': None, 'maximum in-plane shear': "Mohr's Circle",
       'saturation flow': None, 'single payment compound amount': 'compound amount', 'single payment present worth': 'single payment', 'trip generation': None, 'undrained shear strength': None,
       'uniform series compound amount': 'uniform series', 'uniform series present worth': 'uniform series', 'vehicle signal change interval': 'yellow interval',
       'conditional probability': 'joint probability', 'conflict of interest': 'conflicts of interest', 'continuing': None, 'standard of care': None, 'shear and moment diagrams': 'shearing force and bending moment'}
def terms_of(v, default=None):
    """(section, [search words]) for one FIND entry, or (None, []) when the question is not a handbook lookup."""
    if v == '-': return None, []
    sec, ts = v.split('::') if '::' in v else (default, v)
    out = []
    for t in ts.split(';'):
        t = FIX.get(t.strip(), t.strip())
        if t and t not in out: out.append(t)
    return sec, out
EN_, MM_, MA_, MS_, CE_, EC_, ET_ = 'Environmental Engineering', 'Mechanics of Materials', 'Mathematics', 'Materials Science/Structure of Matter', 'Civil Engineering', 'Engineering Economics', 'Ethics and Professional Practice'
FIND.update({'econ-0023': EC_ + '::payback', 'ethics-0005': ET_ + '::negligence', 'ethics-0013': ET_ + '::negligence', 'ethics-0007': ET_ + '::contract', 'ethics-0008': ET_ + '::contract',
 'geotech-0042': CE_ + '::at rest', 'geotech-0046': CE_ + '::eccentric', 'geotech-0051': CE_ + '::overconsolidation', 'geotech-0054': CE_ + '::compaction',
 'materials-0005': MS_ + '::water-cement ratio', 'materials-0012': MS_ + '::water-cement ratio', 'materials-0014': MS_ + '::concrete', 'materials-0017': MS_ + '::tensile strength', 'materials-0024': MM_ + '::modular ratio',
 'math-0023': MA_ + '::circular sector', 'math-0027': EN_ + '::half-life', 'math-0030': MA_ + '::unit vector', 'structural-0033': CE_ + '::determinacy', 'structural-0034': CE_ + '::determinacy', 'structural-0035': CE_ + '::fixed-end',
 'transport-0031': CE_ + '::load equivalency', 'transport-0032': CE_ + '::load equivalency', 'transport-0039': CE_ + '::pedestrian', 'water-0024': EN_ + '::chlorine', 'water-0036': CE_ + '::infiltration', 'water-0053': CE_ + '::storativity',
 'construction-0027': 'Industrial and Systems Engineering::PERT', 'geotech-0039': CE_ + '::exit gradient', 'geotech-0030': CE_ + '::plasticity index', 'materials-0023': MM_ + '::elastic strain energy',
 'water-0058': 'Chemistry and Biochemistry::acids, bases, and ph', 'water-0065': EN_ + '::CT value', 'water-0017': CE_ + '::sewage flow', 'surveying-0022': 'Units and Conversion Factors::acre', 'surveying-0025': MA_ + '::right circular cone',
 'structural-0014': CE_ + '::tributary area', 'structural-0038': CE_ + '::tributary area', 'mechmat-0021': 'Mechanical Engineering::crushing',
 'water-0055': EN_ + '::mass balance', 'water-0056': EN_ + '::alkalinity', 'water-0057': EN_ + '::mass balance', 'water-0059': EN_ + '::suspended solids', 'water-0063': EN_ + '::filtration'})
def main():
  global n, miss, none
  n = miss = none = 0
  for f in sorted(glob.glob(os.path.join(ROOT, 'questions', '*.json'))):
      qs = json.load(open(f))
      for q in qs:
          v = FIND.get(q.get('family') or q['id'])
          if v is None: miss += 1; print('no entry:', q['id']); continue
          sec, terms = terms_of(v, q['handbook'][0]['section'])
          if not terms: q['handbook'] = [dict(h, find=[]) for h in q['handbook'][:1]]; q['lookup'] = False; none += 1; continue
          q['handbook'] = [{'section': sec, 'page': HBP[sec], 'find': terms}]; q['lookup'] = True; n += 1
      json.dump(qs, open(f, 'w'), indent=1, ensure_ascii=False); open(f, 'a').write('\n')
  print('handbook lookups:', n, 'not a lookup:', none, 'missing:', miss)

if __name__ == '__main__': main()
