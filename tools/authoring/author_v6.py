"""Version families for the problem types added in author_n0.py."""
from author_v import *
def F(base, stem, concept, sol, ans, wrong=None, dp=None, fig=None, sfig=None, **P): V(base, stem, P, ans, sol, wrong, dp, fig, sfig, concept)
F('fluids-0014', "A [d] mm diameter water jet moving at [v] m/s is turned through [th]° by a fixed, smooth vane without changing speed. What is the horizontal force the jet exerts on the vane?",
  "The momentum equation gives the force on the fluid as mass flow rate times the change in velocity. In the jet's original direction the velocity changes from V to V cos(angle), so the vane feels (density)(Q)(V)(1 - cos(angle)). A flat plate is the 90° case, and a full reversal at 180° doubles it.",
  r"Q = A V = [pi*(d/1000)**2/4|5] × [v] = [pi*(d/1000)**2/4*v|4] m^{3}/s. || F_{x} = (density) Q V (1 - cos [th]°) = 1,000([pi*(d/1000)**2/4*v|4])([v])(1 - ([cos(rad(th))|3])) = [ans|0] N.",
  "1000*pi*(d/1000)**2/4*v*v*(1-cos(rad(th)))", dp=0, d=[50, 40, 75, 60], v=[20, 25, 12, 18], th=[60, 90, 45, 120])
F('surveying-0012', "Offsets from a straight baseline to a curved boundary, measured every [dx] m, are [o0|1], [o1|1], [o2|1], [o3|1] and [o4|1] m. Using the trapezoidal rule, what is the area between the baseline and the boundary?",
  "The trapezoidal rule treats each strip between adjacent offsets as a trapezoid. Summed, the area is the common interval times (half the first and last offsets plus all the offsets in between). Simpson's 1/3 rule fits parabolas instead and needs an even number of intervals.",
  "A = d × ((first + last) / 2 + the others) = [dx] × (([o0|1] + [o4|1]) / 2 + [o1|1] + [o2|1] + [o3|1]) = [dx] × [(o0+o4)/2+o1+o2+o3|2] = [ans|1] m^{2}.",
  "dx*((o0+o4)/2+o1+o2+o3)", dp=1, dx=[10, 15, 20, 5], o0=[3.2, 4.0, 6.5, 1.8], o1=[4.5, 5.5, 8.0, 2.6], o2=[5.1, 6.2, 9.5, 3.1], o3=[4.0, 5.0, 7.0, 2.4], o4=[2.6, 3.0, 5.5, 1.2])
F('surveying-0013', "Point A has coordinates N [NA|2], E [EA|2] and point B has coordinates N [NB|2], E [EB|2], in metres. What is the azimuth of the line from A to B?",
  "The direction between two coordinated points comes from the differences in easting and northing: tan(azimuth) = change in easting / change in northing. The signs of the two differences fix the quadrant, so add 180° or 360° to the calculator result when the line does not run north-east.",
  r"Change in northing = [NB|2] - [NA|2] = [NB-NA|2] m. Change in easting = [EB|2] - [EA|2] = [EB-EA|2] m. Both are positive, so the line runs north-east. || Azimuth = arctan(\frac{[EB-EA|2]}{[NB-NA|2]}) = [ans|2]°. || Length = \sqrt{[NB-NA|2]^{2} + [EB-EA|2]^{2}} = [hypot(NB-NA,EB-EA)|2] m.",
  "atan((EB-EA)/(NB-NA))*180/pi", dp=2, fig=lambda e: azimuth(round(e['ans'], 1)), NA=[1000, 500, 2500, 120], EA=[2000, 800, 1200, 340], NB=[1400, 620, 2750, 300], EB=[2300, 1250, 1900, 460])
F('water-0025', "A wastewater has a 5-day BOD of [B5] mg/L and a BOD rate constant of [k|2] per day (base e). What is its ultimate BOD?",
  "BOD is exerted as a first-order reaction: the oxygen used by time t is the ultimate BOD times (1 - e^{-k t}). A five-day test captures only part of the total, so the ultimate value is the five-day value divided by that fraction. Check whether k is given to base e or base 10.",
  r"BOD_{t} = L_{0}(1 - e^{-k t}), so L_{0} = \frac{[B5]}{1 - e^{-[k|2](5)}} = \frac{[B5]}{1 - [exp(-k*5)|4]} = \frac{[B5]}{[1-exp(-k*5)|4]} = [ans|0] mg/L.",
  "B5/(1-exp(-k*5))", dp=0, B5=[180, 220, 150, 300], k=[0.23, 0.30, 0.20, 0.35])
F('water-0026', "Water flows at [v|1] m/s and [y|2] m deep in a wide rectangular channel. What is the Froude number? Use g = 9.81 m/s^{2}.",
  "The Froude number compares the flow velocity with the speed of a small surface wave, the square root of g times the depth. Below 1 the flow is subcritical: deep, slow and controlled from downstream. Above 1 it is supercritical: shallow, fast and controlled from upstream. At exactly 1 it is critical.",
  r"Fr = \frac{V}{\sqrt{g y}} = \frac{[v|1]}{\sqrt{9.81([y|2])}} = \frac{[v|1]}{[sqrt(g*y)|3]} = [ans|3]. || [reg]",
  "v/sqrt(g*y)", dp=3, fig=lambda e: channel(3, e['y']), v=[2.5, 1.2, 4.0, 3.6], y=[0.80, 1.50, 0.40, 0.60],
  reg=['This is less than 1, so the flow is subcritical.', 'This is less than 1, so the flow is subcritical.', 'This is greater than 1, so the flow is supercritical.', 'This is greater than 1, so the flow is supercritical.'])
F('geotech-0024', "A soil sample has a mass of [mw|1] g when moist and [md|1] g after oven drying. What is its water content?",
  "Water content is the mass of water divided by the mass of dry solids, not by the moist mass. That is why it can exceed 100% in very soft clays and organic soils.",
  r"Mass of water = [mw|1] - [md|1] = [mw-md|1] g. || w = \frac{[mw-md|1]}{[md|1]} × 100 = [ans|2]%.",
  "(mw-md)/md*100", dp=2, mw=[245, 318.5, 182, 96.4], md=[210, 260, 160, 80])
F('structural-0021', "A beam fixed at both ends spans [L] m and carries a [P] kN point load [a] m from the left support. What is the fixed-end moment at the left support?",
  "Fixed-end moments are the support moments of a beam held against rotation at both ends. For a point load they are P a b^{2} / L^{2} at the end a distance a from the load and P a^{2} b / L^{2} at the other end. The end nearer the load takes the larger moment, and for a central load both equal P L / 8.",
  r"b = [L] - [a] = [L-a] m. || M_{left} = \frac{P a b^{2}}{L^{2}} = \frac{[P]([a])([L-a])^{2}}{[L]^{2}} = [ans|2] kN·m. || For reference, M_{right} = \frac{P a^{2} b}{L^{2}} = [P*a*a*(L-a)/L**2|2] kN·m.",
  "P*a*(L-a)**2/L**2", dp=2, L=[6, 8, 5, 9], P=[60, 40, 90, 54], a=[2, 3, 2, 6])
F('dynamics-0012', "A slender rod of mass [m] kg and length [L] m is pivoted at one end. A small [M] kg mass is fixed to its free end. What is the mass moment of inertia of the assembly about the pivot?",
  "Moments of inertia about the same axis add. Take each part about the pivot: use the tabulated value where the axis matches, and the parallel axis theorem, or m d^{2} for a small mass, where it does not. The distance d runs from the axis to that part's own centre of mass.",
  r"Rod about its end: \frac{[m]([L])^{2}}{3} = [m*L*L/3|2] kg·m^{2}. || Tip mass, treated as a particle [L] m from the pivot: [M]([L])^{2} = [M*L*L|2] kg·m^{2}. || Total = [m*L*L/3|2] + [M*L*L|2] = [ans|2] kg·m^{2}.",
  "m*L**2/3+M*L**2", dp=2, m=[6, 3, 12, 4.5], L=[2, 1.5, 1, 2], M=[4, 2, 5, 1.5])
F('mechmat-0014', "A solid steel shaft [d] mm in diameter and [L] m long carries a torque of [Tq] kN·m. The shear modulus is 80 GPa. What is the angle of twist, in degrees?",
  "A shaft in torsion twists by T L / (G J), the rotational counterpart of P L / (A E). G is the shear modulus and J the polar moment of inertia, π d^{4} / 32 for a solid round shaft. The result is in radians; multiply by 180/π for degrees.",
  r"J = \frac{π d^{4}}{32} = \frac{π([d])^{4}}{32} = [pi*d**4/32|0] mm^{4}. || Angle = \frac{T L}{G J} = \frac{([Tq] × 10^{6})([L*1000])}{(80,000)([pi*d**4/32|0])} = [Tq*1e6*L*1000/(80000*pi*d**4/32)|4] rad = [ans|2]°.",
  "Tq*1e6*L*1000/(80000*pi*d**4/32)*180/pi", dp=2, d=[50, 60, 40, 75], L=[2, 1.5, 1.2, 3], Tq=[1.5, 3, 0.8, 6])
if __name__ == '__main__': save()
