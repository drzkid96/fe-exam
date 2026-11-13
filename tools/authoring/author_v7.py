"""Second versions for the ordering, hotspot, matching and multi-select question types."""
import json
from author_v import BANK, _load, EXPR, STATS, save, beam
def X(base, concept, sol, calc=None, basis=None, **over):
    bank = _load(base.rsplit('-', 1)[0]); i = next(k for k, x in enumerate(bank) if x['id'] == base); b = bank[i]
    b.update(family=base, version=1, versions=2)
    q = json.loads(json.dumps(b)); q.update(id=base + '-b', version=2, eli5=concept, solution=sol.replace(' || ', '\n\n')); q.update(over)
    if calc: EXPR[q['id']] = calc; q['verify'] = {'method': 'computed'}
    else: q['verify'] = {'method': 'reference', 'basis': basis}
    bank.insert(i + 1, q); STATS['families'] += 1; STATS['versions'] += 2
ids = lambda pairs: [{'id': a, 'text': b} for a, b in pairs]
X('construction-0005', "Closeout follows a fixed sequence because each step triggers a contractual consequence: substantial completion starts warranties and ends liquidated damages, the punch list defines what is left, and final payment releases the retainage.",
  "The work is first inspected for substantial completion. Remaining items go on a punch list, the contractor completes them, a final inspection confirms it, and only then is final payment made and retainage released.",
  basis='Standard construction contract closeout sequence',
  stem="Put these project closeout steps in order, from first (top) to last (bottom).",
  items=ids([('final', 'Final payment and release of retainage'), ('punch', 'Punch list issued'), ('insp', 'Inspection for substantial completion'), ('fix', 'Punch list work completed'), ('finsp', 'Final inspection')]),
  answer=['insp', 'punch', 'fix', 'finsp', 'final'])
X('water-0006', "Wastewater treatment removes contaminants from coarsest to finest: large objects and grit first to protect equipment, then settleable solids, then dissolved and fine organic matter by biological treatment, then the biological solids, and finally pathogens.",
  "Screening and grit removal are preliminary treatment. Primary clarification settles solids. The aeration basin provides biological (secondary) treatment, the secondary clarifier settles the biological solids, and disinfection comes last so that solids do not shield organisms.",
  basis='Conventional activated sludge wastewater treatment sequence',
  stem="Put the steps of conventional activated sludge wastewater treatment in order, from first (top) to last (bottom).",
  items=ids([('aer', 'Aeration basin'), ('screen', 'Screening'), ('dis', 'Disinfection'), ('prim', 'Primary clarifier'), ('grit', 'Grit removal'), ('sec', 'Secondary clarifier')]),
  answer=['screen', 'grit', 'prim', 'aer', 'sec', 'dis'])
X('geotech-0007', "Hydrostatic pore water pressure is zero at the water table and increases linearly with depth below it, at 9.81 kPa per metre. Above the water table, ignoring capillary rise, it is zero.",
  "Pore pressure depends only on depth below the water table. The clay is the deepest layer, so it has the greatest pore pressure. The sand above the water table has none.",
  basis='Hydrostatic pore pressure increases with depth below the water table',
  stem="Click the layer in which the pore water pressure is greatest. Ignore capillary rise.", answer='clay')
_cant = beam(3, [(3, 12)], kind='cantilever')
X('mechmat-0007', "In a cantilever with a load at its free end, the bending moment at any section is the load times the distance from the load to that section. It is zero under the load and grows linearly to its maximum, P L, at the fixed support.",
  "M(x) = P × (distance from the free end). That distance is largest at the fixed support, so the moment peaks there: 12 kN × 3 m = 36 kN·m. At the free end the moment is zero.",
  calc="max({'fixed': 12*3, 'mid': 12*1.5, 'free': 12*0}.items(), key=lambda kv: kv[1])[0]",
  stem="A cantilever beam carries one point load at its free end. Click the place on the beam where the bending moment is largest.", figure=_cant,
  regions=[{'id': 'fixed', 'label': 'At the fixed support', 'shape': 'rect', 'x': 30, 'y': 46, 'w': 50, 'h': 78}, {'id': 'mid', 'label': 'At mid-length', 'shape': 'rect', 'x': 175, 'y': 60, 'w': 50, 'h': 50}, {'id': 'free', 'label': 'At the free end', 'shape': 'rect', 'x': 322, 'y': 46, 'w': 50, 'h': 78}], answer='fixed')
X('materials-0003', "Each standard test targets one property. Soil and aggregate tests describe grading, plasticity and compaction behaviour; concrete tests describe strength in a particular mode of loading.",
  "A sieve analysis gives the particle size distribution. The Proctor test gives maximum dry density and optimum water content. Atterberg limits give the plasticity of fine-grained soil. The split-cylinder test gives the tensile strength of concrete.",
  basis='Standard test methods: ASTM C136 / D6913 (sieve analysis), ASTM D698 (standard Proctor), ASTM D4318 (Atterberg limits), ASTM C496 (splitting tensile strength)',
  tokens=ids([('proctor', 'Proctor test'), ('split', 'Split-cylinder test'), ('sieve', 'Sieve analysis'), ('atter', 'Atterberg limits')]),
  targets=[{'id': 'grad', 'label': 'Particle size distribution'}, {'id': 'tens', 'label': 'Tensile strength of concrete'}, {'id': 'comp', 'label': 'Maximum dry density and optimum water content'}, {'id': 'plast', 'label': 'Plasticity of fine-grained soil'}],
  answer={'proctor': 'comp', 'split': 'tens', 'sieve': 'grad', 'atter': 'plast'})
X('surveying-0004', "An azimuth runs clockwise from north through 360°. A bearing is the acute angle from the north or south line toward east or west. Quadrant by quadrant: 0° to 90° is N (azimuth) E; 90° to 180° is S (180° - azimuth) E; 180° to 270° is S (azimuth - 180°) W; 270° to 360° is N (360° - azimuth) W.",
  "30° is in the north-east quadrant: N 30° E. || 160° is in the south-east quadrant: 180° - 160° = 20°, so S 20° E. || 200° is in the south-west quadrant: 200° - 180° = 20°, so S 20° W. || 290° is in the north-west quadrant: 360° - 290° = 70°, so N 70° W.",
  calc="{'az%d' % a: ('ne' if a < 90 else 'se' if a < 180 else 'sw' if a < 270 else 'nw') for a in (30, 160, 200, 290)}",
  tokens=ids([('az200', '200°'), ('az30', '30°'), ('az290', '290°'), ('az160', '160°')]),
  targets=[{'id': 'ne', 'label': 'N 30° E'}, {'id': 'se', 'label': 'S 20° E'}, {'id': 'sw', 'label': 'S 20° W'}, {'id': 'nw', 'label': 'N 70° W'}],
  answer={'az30': 'ne', 'az160': 'se', 'az200': 'sw', 'az290': 'nw'})
X('math-0005', "The sample standard deviation is the square root of the sample variance, which divides the sum of squared deviations from the mean by n - 1. It has the same units as the data, is never negative, and is pulled upward by extreme values because deviations are squared.",
  "Dividing by n - 1 and sharing the data's units are both true. || It cannot be negative, because it is a square root. It is the square root of the variance, not its square. Outliers increase it strongly.",
  basis='FE Reference Handbook 10.0.1, Engineering Probability and Statistics, dispersion: sample standard deviation',
  stem="Which statements about the sample standard deviation are true? Select the two that apply.",
  options=ids([('a', 'It divides the sum of squared deviations by n - 1'), ('b', 'It has the same units as the data'), ('c', 'It can be negative'), ('d', 'It equals the variance squared'), ('e', 'It is unaffected by outliers')]), answer=['a', 'b'])
X('mechmat-0006', "The tip deflection of a cantilever with an end load is P L^{3} / (3 E I). Anything in the numerator increases deflection and anything in the denominator reduces it, and length counts three times over because it is cubed.",
  "Doubling the load doubles the deflection. Doubling the length multiplies it by 8. Halving the moment of inertia doubles it. || Doubling E or doubling I halves the deflection.",
  calc="sorted(k for k, r in {'a': 2/(1*1), 'b': 2**3/(1*1), 'c': 1/(2*1), 'd': 1/(1*2), 'e': 1/(1*0.5)}.items() if r > 1)",
  stem="A cantilever beam carries a point load at its free end. Which changes increase its tip deflection? Select all that apply.",
  options=ids([('a', 'Double the load'), ('b', 'Double the length'), ('c', 'Use a material with twice the modulus of elasticity'), ('d', 'Use a section with twice the moment of inertia'), ('e', 'Use a section with half the moment of inertia')]), answer=['a', 'b', 'e'])
X('transport-0006', "The MUTCD sorts signs by function. Warning signs alert drivers to conditions ahead and are mostly yellow diamonds with black legends; pedestrian and school warnings may be fluorescent yellow-green. Regulatory signs state laws and are mostly white rectangles. Guide signs give directions.",
  "The Curve sign, the Signal Ahead sign and the Pedestrian Crossing sign are all warning signs. || Speed Limit and Do Not Enter are regulatory signs.",
  basis='MUTCD Part 2, Chapter 2C warning signs (Curve W1-2, Signal Ahead W3-3, Pedestrian Crossing W11-2); Chapter 2B regulatory signs (Speed Limit R2-1, Do Not Enter R5-1)',
  stem="Which of these are warning signs under the MUTCD? Select the three that apply.",
  options=ids([('a', 'Curve sign'), ('b', 'Signal Ahead sign'), ('c', 'Speed Limit sign'), ('d', 'Pedestrian Crossing sign'), ('e', 'Do Not Enter sign')]), answer=['a', 'b', 'd'])
if __name__ == '__main__': save()
