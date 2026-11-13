"""Adds a drawn figure to the lessons where a picture carries the idea. Run after the lesson scripts."""
import json, os
from author_v import *
from author_common import ROOT
FIGS = {
 'statics-a': (forces(100, 80, 60), 'Two concurrent forces. Resolve each into x and y components, add, then recombine.'),
 'statics-b': (lever(2, 150, 30), 'Only the component of the force perpendicular to the arm produces moment about the pivot.'),
 'statics-c': (beam(6, [(2, 30)], R=(20, 10)), 'Free-body diagram of a simply supported beam. Moments about A give the reaction at B; vertical equilibrium gives A.'),
 'statics-d': (truss(8, 3, 24), 'A simple truss. Find the reactions first, then work joint by joint or cut a section.'),
 'statics-e': (tsec(100, 20, 20, 80), 'A composite section split into two rectangles for the centroid calculation.'),
 'statics-f': (rect(100, 200), 'The centroidal axis of a rectangle. I about this axis is b h^{3} / 12.'),
 'statics-g': (incline(0, 'Sliding starts when tan(angle) equals the coefficient of static friction'), 'A block on an incline at the point of sliding.'),
 'dynamics-a': (projectile(20, 30), 'Projectile motion: constant horizontal velocity and constant downward acceleration.'),
 'dynamics-c': (incline(30), 'On a frictionless incline only the weight component along the slope, m g sin(angle), accelerates the block.'),
 'mechmat-a': (beam(8, w=10, R=(40, 40)), 'A uniformly loaded simple beam. Shear is largest at the supports; moment is largest at midspan, where shear is zero.'),
 'mechmat-b': (bar(20, None, 50), 'Axial stress is force over the cross-sectional area perpendicular to the force.'),
 'mechmat-c': (bar(20, 2, 50), 'Axial deformation of a prismatic bar: P L / (A E).'),
 'mechmat-d': (mohr(80, 20, 40), "Mohr's circle. The centre is the average normal stress, the radius is the maximum in-plane shear stress, and the circle crosses the horizontal axis at the principal stresses."),
 'structural-a': (beam(6, [(3, 40)], R=(20, 20)), 'A central point load on a simple span: reactions of P / 2 and a maximum moment of P L / 4 under the load.'),
 'structural-b': (beam(3, [(3, 12)], kind='cantilever'), 'A cantilever with a tip load deflects P L^{3} / (3 EI) at the free end.'),
 'structural-c': (column(4, 1), 'A pinned-pinned column buckles in a single half-wave, so K = 1.'),
 'structural-h': (rcbeam(300, 500, 1500, 88.2), 'A singly reinforced section. The shaded block is the equivalent rectangular stress block of depth a.'),
 'geotech-d': (soil(17, 19, 2, 6), 'A soil profile with a water table. Effective stress is total stress minus pore water pressure.'),
 'geotech-e': (wall(4, 48), 'Rankine active pressure on a wall: a triangular diagram whose resultant acts at one third of the height.'),
 'geotech-g': (footing(2, 600, 1), 'A shallow footing. Bearing capacity depends on cohesion, the surcharge of soil beside the footing and the footing width.'),
 'geotech-j': (incline(25, 'Factor of safety = tan(friction angle) / tan(slope angle) for dry sand'), 'An infinite slope in cohesionless soil.'),
 'fluids-a': (orifice(3, 50), 'Orifice flow: the ideal jet velocity is the square root of 2 g h, reduced by the discharge coefficient.'),
 'fluids-c': (gate(2, 3), 'Hydrostatic pressure on a vertical gate grows linearly with depth. The resultant acts at two thirds of the depth.'),
 'fluids-d': (pipe(200, 100), 'Continuity: the flow rate A V is the same at both sections, so the narrower section has the higher velocity and the lower pressure.'),
 'surveying-a': (azimuth(60, 200), 'Latitude is L cos(azimuth) and departure is L sin(azimuth).'),
 'surveying-b': (parcel([(0, 0), (60, 0), (80, 40), (20, 50)]), 'Area by coordinates: list the corners in order and apply the cross-product sum.'),
 'surveying-e': (level(1.52, 2.31), 'Differential leveling: height of instrument = benchmark + backsight; new elevation = height of instrument - foresight.'),
 'transport-a': (hcurve(1000, 30), 'A simple horizontal curve. T = R tan(Δ / 2) and L = R Δ π / 180.'),
 'transport-c': (greenshields(60, 120), 'The Greenshields speed-density line. Capacity occurs at half the jam density and half the free-flow speed.'),
 'water-b': (channel(3, 1), 'A rectangular channel. Hydraulic radius = flow area / wetted perimeter.'),
 'water-d': (tank(40), 'With no flow, pressure anywhere in the system is the specific weight of water times the height of the tank surface above that point.'),
 'econ-a': (cashflow(5, P='$20,000', A='A'), 'A cash flow diagram: a loan received at time 0 and five equal end-of-year payments.'),
 'construction-c': (network(3, 4, 6, 2), 'An activity-on-node network. The longest path, A-C-D, is critical; B has float.'),
}
n = 0
for sub, (fig, cap) in FIGS.items():
    path = os.path.join(ROOT, 'guide', sub.rsplit('-', 1)[0] + '.json'); g = json.load(open(path))
    for s in g['sections']:
        if s.get('subtopic') == sub: s['figure'] = dict(fig, caption=cap); n += 1
    json.dump(g, open(path, 'w'), indent=1, ensure_ascii=False); open(path, 'a').write('\n')
print('lesson figures:', n)
