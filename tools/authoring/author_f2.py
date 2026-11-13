"""Question families for problem types worked in the recorded review sessions that the bank did not yet have.
Each spec is one numeric-entry family with four versions. `v1` is the hand-worked answer for the first version; the
formula must reproduce it. Usage: `python3 author_f2.py base` (after author_n0.py) creates the base questions;
`python3 author_f2.py versions` (after the other version scripts) turns them into families."""
import sys, json, os
from author_v import *
from author_v import _load
SPECS = []
def NF(sub, find, unit, dp, v1, stem, concept, sol, ans, ex, tol=0.01, units='SI', fig=None, **P):
    SPECS.append(dict(sub=sub, find=find, unit=unit, dp=dp, v1=v1, stem=stem, concept=concept, sol=sol, ans=ans, ex=ex, tol=tol, units=units, fig=fig, P=P))
CE, MM_, EN, FM = 'Civil Engineering', 'Mechanics of Materials', 'Environmental Engineering', 'Fluid Mechanics'
# ---------------- Statics ----------------
NF('statics-c', 'equilibrium requirements; centroid', 'kN', 2, 24, "A simply supported beam spans [L] m. It carries a triangular distributed load that is zero at A and rises to [w0] kN/m at B. What is the reaction at B?",
   "A triangular load acts as a single force equal to half its peak intensity times its length, placed one third of the length from the tall end. With the resultant known, take moments about A.",
   r"Resultant = \frac{1}{2}([w0])([L]) = [w0*L/2] kN, acting [2*L/3|2] m from A. || Moments about A: B_{y}([L]) = [w0*L/2]([2*L/3|2]), so B_{y} = [ans|2] kN. A carries the other [w0*L/6|2] kN.",
   "w0*L/3", dict(L=7.5, w0=16), L=[6, 9, 4.5, 12], w0=[12, 14, 20, 5])
NF('statics-g', 'friction', 'N', 1, 260, "A [W1] N block rests on a [W2] N block on a floor, and a cable holds the upper block in place. The coefficient of static friction is [m1|2] between the blocks and [m2|2] between the lower block and the floor. What horizontal force starts the lower block moving?",
   "Each sliding surface has its own normal force. The top face of the lower block carries the upper block's weight; its bottom face carries both. Friction on both faces opposes the pull.",
   "Friction on the top face = [m1|2] × [W1] = [m1*W1|1] N. || Friction on the bottom face = [m2|2] × ([W1] + [W2]) = [m2*(W1+W2)|1] N. || P = [m1*W1|1] + [m2*(W1+W2)|1] = [ans|1] N.",
   "m1*W1+m2*(W1+W2)", dict(W1=250, W2=500, m1=0.35, m2=0.25), W1=[200, 150, 400, 80], W2=[300, 450, 600, 120], m1=[0.30, 0.25, 0.20, 0.40], m2=[0.40, 0.30, 0.35, 0.50])
NF('statics-a', 'resolution of a force', 'N', 1, 400, "A [Fm] N force acts along a line that rises [r] units for every [s] units of horizontal run. What is its horizontal component?",
   "When a direction is given as a slope, the components are the force times the side ratios of the slope triangle. The hypotenuse is the square root of rise squared plus run squared.",
   r"Hypotenuse = \sqrt{[r]^{2} + [s]^{2}} = [hypot(r,s)]. || F_{x} = [Fm] × \frac{[s]}{[hypot(r,s)]} = [ans|1] N. The vertical component is [Fm] × \frac{[r]}{[hypot(r,s)]} = [Fm*r/hypot(r,s)|1] N.",
   "Fm*s/hypot(r,s)", dict(Fm=850, r=8, s=15), Fm=[500, 650, 340, 200], r=[3, 5, 8, 7], s=[4, 12, 15, 24])
# ---------------- Structural ----------------
NF('structural-c', MM_ + "::Euler's formula; columns", 'kN', 0, 1755, "A steel column [L] m long has pinned ends and is braced at mid-height against buckling about its weak axis only. E = 200 GPa, I_{x} = [Ix] × 10^{6} mm^{4} and I_{y} = [Iy] × 10^{6} mm^{4}. What is the governing Euler buckling load?",
   "One axial load can buckle the column about either axis. Each axis has its own unbraced length and moment of inertia, and the smaller critical load governs. Bracing the weak axis at mid-height halves its length and quadruples its critical load.",
   r"Strong axis, full length: P = \frac{π^{2}(200,000)([Ix] × 10^{6})}{([L*1000])^{2}} = [pi**2*200000*Ix*1e6/(L*1000)**2/1000|0] kN. || Weak axis, half length: P = \frac{π^{2}(200,000)([Iy] × 10^{6})}{([L*500])^{2}} = [pi**2*200000*Iy*1e6/(L*500)**2/1000|0] kN. || The smaller governs: [ans|0] kN.",
   "min(pi**2*200000*Ix*1e6/(L*1000)**2, pi**2*200000*Iy*1e6/(L*500)**2)/1000", dict(L=7, Ix=60, Iy=12), L=[6, 8, 5, 10], Ix=[40, 90, 30, 200], Iy=[8, 30, 5, 60])
NF('water-e', 'Fluid Mechanics::forces on submerged surfaces', '', 2, 1.92, "A concrete gravity dam with a rectangular section is [b] m wide at the base and [h] m high. Water stands level with its top on one side. Concrete weighs 23.5 kN/m^{3}, the coefficient of friction on the base is [mu|2] and uplift is ignored. What is the factor of safety against sliding?",
   "Check a one-metre length of dam as a rigid block. The water thrust is the area of the triangular pressure diagram, half the unit weight of water times the depth squared. Friction can supply up to the coefficient times the dam's weight.",
   r"Weight = 23.5([b])([h]) = [23.5*b*h|1] kN/m. || Water thrust = \frac{1}{2}(9.81)([h])^{2} = [0.5*9.81*h*h|1] kN/m. || FS = \frac{[mu|2]([23.5*b*h|1])}{[0.5*9.81*h*h|1]} = [ans|2].",
   "mu*23.5*b*h/(0.5*9.81*h*h)", dict(b=5, h=7, mu=0.6), b=[4, 6, 3, 8], h=[6, 9, 5, 10], mu=[0.60, 0.65, 0.55, 0.70])
NF('structural-e', CE + '::indeterminate; fixed-end moment', 'kN', 1, 75, "A continuous beam has two equal spans of [L] m and carries a uniform load of [w] kN/m over its whole length. What is the reaction at the middle support?",
   "A two-span continuous beam is indeterminate to the first degree. Removing the middle support and restoring zero deflection there gives a middle reaction of 1.25 w L, more than the w L that tributary length would suggest; each end support carries 0.375 w L.",
   "R_{middle} = 1.25 w L = 1.25([w])([L]) = [ans|1] kN. || Each end support carries 0.375([w])([L]) = [0.375*w*L|2] kN. Check: [ans|1] + 2([0.375*w*L|2]) = [2*w*L|1] kN, the total load.",
   "1.25*w*L", dict(L=7, w=16), L=[6, 8, 5, 10], w=[10, 12, 24, 7.5])
NF('structural-f', CE + '::load combinations; LRFD', 'kN·m', 1, 230.4, "Floor beams span [L] m and are spaced [s] m apart. The floor carries a dead load of [D|1] kPa and a live load of [Lv|1] kPa. Using 1.2D + 1.6L, what is the factored bending moment in an interior beam?",
   "Follow the load path. Factor the area loads, multiply by the tributary width (the beam spacing for an interior beam) to get a line load, then use the simple-span moment w L^{2} / 8.",
   r"Factored area load = 1.2([D|1]) + 1.6([Lv|1]) = [1.2*D+1.6*Lv|2] kPa. || Line load = [1.2*D+1.6*Lv|2] × [s] = [(1.2*D+1.6*Lv)*s|2] kN/m. || M_{u} = \frac{[(1.2*D+1.6*Lv)*s|2]([L])^{2}}{8} = [ans|1] kN·m.",
   "(1.2*D+1.6*Lv)*s*L*L/8", dict(L=9, s=3.5, D=4.2, Lv=3.6), L=[8, 6, 10, 7.5], s=[3, 2.5, 4, 3], D=[4.0, 3.5, 5.0, 4.5], Lv=[3.0, 4.8, 2.4, 4.0])
NF('structural-g', CE + '::tension members; net area', 'kips', 1, 135.9, "A steel plate tension member is [wd] in wide and [t] in thick. One cross-section has [n] holes for [db] in diameter bolts in standard holes. F_{u} = 58 ksi and U = 1. With a resistance factor of 0.75, what is the design strength for net-section rupture?",
   "Rupture is checked on the net area through the holes. Each hole removes a width equal to the bolt diameter plus 1/8 in: 1/16 in for the standard hole and 1/16 in for damage. Design strength is 0.75 F_{u} A_{e}, with A_{e} = U A_{n}.",
   "Net width = [wd] - [n]([db] + 0.125) = [wd-n*(db+0.125)|3] in. || A_{n} = [wd-n*(db+0.125)|3] × [t] = [(wd-n*(db+0.125))*t|3] in^{2}. || Design strength = 0.75(58)([(wd-n*(db+0.125))*t|3]) = [ans|1] kips.",
   "0.75*58*(wd-n*(db+0.125))*t", dict(wd=9, t=0.625, n=2, db=0.875), units='USCS', wd=[8, 10, 6, 12], t=[0.5, 0.75, 0.375, 1.0], n=[2, 3, 1, 3], db=[0.75, 0.875, 0.75, 0.875])
NF('structural-h', CE + '::ACI 318; shear', 'kN', 1, 149.1, "A reinforced concrete beam has an effective depth of [d] mm and stirrups with a total leg area of [Av] mm^{2} at [s] mm spacing. The stirrup yield strength is 420 MPa. What shear do the stirrups carry, V_{s}?",
   "A diagonal shear crack crosses about d / s stirrups, each carrying A_{v} f_{y}, so V_{s} = A_{v} f_{y} d / s. A_{v} counts every leg that crosses the crack, two for a U-stirrup.",
   r"V_{s} = \frac{A_{v} f_{y} d}{s} = \frac{[Av](420)([d])}{[s]} = [ans*1000|0] N = [ans|1] kN.",
   "Av*420*d/s/1000", dict(d=520, Av=142, s=175), d=[500, 450, 600, 550], Av=[142, 142, 200, 157], s=[200, 150, 250, 125])
# ---------------- Mathematics ----------------
NF('math-b', 'Mathematics::integral calculus', 'square units', 2, 4.5, "What is the area enclosed between the line y = [k]x and the parabola y = x^{2}?",
   "Set the functions equal to find where they cross; those x values are the limits. Integrate the upper function minus the lower one between them.",
   r"[k]x = x^{2} at x = 0 and x = [k]. Between them the line is on top. || Area = integral from 0 to [k] of ([k]x - x^{2}) dx = \frac{[k]([k])^{2}}{2} - \frac{([k])^{3}}{3} = [k**3/2|2] - [k**3/3|2] = [ans|2] square units.",
   "k**3/6", dict(k=5), k=[3, 6, 2, 4.5])
NF('math-d', 'Engineering Probability and Statistics::binomial distribution', '', 4, 0.7373, "Each trial of a process succeeds with probability [p|2], independently of the others. In [n] trials, what is the probability of at least [n-1] successes?",
   "Independent trials with two outcomes and a fixed probability are binomial. 'At least n - 1' means exactly n - 1 or exactly n, so add those two terms.",
   "P(exactly [n-1]) = [n] × ([p|2])^{[n-1]} × ([1-p|2]) = [n*p**(n-1)*(1-p)|4]. || P(exactly [n]) = ([p|2])^{[n]} = [p**n|4]. || Sum = [ans|4].",
   "n*p**(n-1)*(1-p)+p**n", dict(p=0.75, n=4), p=[0.80, 0.90, 0.60, 0.70], n=[5, 4, 5, 6])
# ---------------- Construction ----------------
NF('construction-d', '-', 'yd^{3}', 2, 33.33, "A slab is [L] ft long, [W] ft wide and [t] in thick. How many cubic yards of concrete does it contain?",
   "Work in feet, then convert. A thickness in inches is divided by 12, and cubic feet are divided by 27 to give cubic yards.",
   r"Volume = [L] × [W] × \frac{[t]}{12} = [L*W*t/12|1] ft^{3}. || \frac{[L*W*t/12|1]}{27} = [ans|2] yd^{3}.",
   "L*W*t/12/27", dict(L=80, W=36, t=7), units='USCS', L=[60, 40, 100, 24], W=[30, 25, 50, 18], t=[6, 8, 5, 4])
NF('construction-d', '-', 'tons', 2, 9.0, "A floor has [n] steel beams, each [L] ft long, of a shape that weighs [wt] lb per foot. What is the total weight of the beams in tons?",
   "Steel is taken off by weight: weight per foot times length times the number of pieces. Divide pounds by 2,000 for short tons.",
   r"[n] × [L] ft × [wt] lb/ft = [n*L*wt] lb. || \frac{[n*L*wt]}{2,000} = [ans|2] tons.",
   "n*L*wt/2000", dict(n=18, L=32, wt=44), units='USCS', n=[12, 8, 20, 15], L=[30, 25, 40, 28], wt=[50, 84, 26, 35])
NF('construction-e', '-', 'ft^{2}', 1, 96, "On a drawing at a scale of 3/4 in = 1 ft, a room measures [a|2] in by [b|2] in. What is the actual floor area?",
   "Convert each drawing dimension to its real length before multiplying. At 3/4 in to the foot, real feet = drawing inches / 0.75.",
   r"Length = \frac{[a|2]}{0.75} = [a/0.75|2] ft. Width = \frac{[b|2]}{0.75} = [b/0.75|2] ft. || Area = [a/0.75|2] × [b/0.75|2] = [ans|1] ft^{2}.",
   "(a/0.75)*(b/0.75)", dict(a=13.5, b=8.25), units='USCS', a=[9, 12, 7.5, 15], b=[6, 9, 6, 10.5])
NF('construction-d', '-', '$', 0, 20412, "Erecting steel takes [hr|1] labour-hours per ton. A job has [tons] tons, the average wage is $[wage] per hour and the labour burden is [bd]%. What is the labour cost?",
   "Labour-hours are productivity times quantity. Cost is hours times wage, increased by the labour burden that covers payroll taxes, insurance and benefits.",
   "Labour-hours = [hr|1] × [tons] = [hr*tons|0]. || Base wages = [hr*tons|0] × [wage] = $[hr*tons*wage|0]. || With burden: [hr*tons*wage|0] × [1+bd/100|2] = $[ans|0].",
   "hr*tons*wage*(1+bd/100)", dict(hr=9, tons=60, wage=44, bd=32), hr=[8, 6, 10, 7.5], tons=[45, 120, 30, 80], wage=[42, 38, 45, 40], bd=[35, 40, 30, 25])
# ---------------- Transportation ----------------
NF('transport-a', 'horizontal curves', 'ft', 2, 2158.82, "A horizontal curve has a radius of [R] ft and a deflection angle of [I]°. The PI is at station [sta]. What is the station of the PC? Enter it in feet, so that station 12+50 is entered as 1,250.",
   "The PC lies one tangent length back from the PI, and T = R tan(I / 2). Stations are 100 ft units, so work in feet and convert at the end.",
   "T = R tan(I / 2) = [R] × tan([I/2]°) = [R*tan(rad(I/2))|2] ft. || Station [sta] is [PIft] ft. PC = PI - T = [PIft] - [R*tan(rad(I/2))|2] = [ans|2] ft.",
   "PIft-R*tan(rad(I/2))", dict(R=1000, I=44, PIft=3675, sta='36+75'), tol=0.001, units='USCS', fig=lambda e: hcurve(e['R'], e['I']), R=[800, 1200, 600, 1500], I=[40, 28, 52, 36], PIft=[2450, 5180, 1325, 8640], sta=['24+50', '51+80', '13+25', '86+40'])
NF('transport-a', 'vertical curves', 'ft', 2, 447.0, "A vertical curve [L] ft long joins a [g1|1]% grade to a [g2|1]% grade. The PVC elevation is [e0|2] ft. What is the PVT elevation?",
   "The PVI sits at half the curve length. From the PVC, follow the first grade for L / 2 to the PVI, then the second grade for L / 2 to the PVT. The curve itself is not needed for the end points.",
   r"PVI elevation = [e0|2] + \frac{[g1|1]}{100}([L/2]) = [e0+g1/100*L/2|2] ft. || PVT elevation = [e0+g1/100*L/2|2] + \frac{[g2|1]}{100}([L/2]) = [ans|2] ft.",
   "e0+g1/100*L/2+g2/100*L/2", dict(L=700, g1=3, g2=-2, e0=215.5), tol=0.001, units='USCS', L=[600, 400, 800, 500], g1=[2, -3, 1.5, 4], g2=[-3, 1, -2.5, -1], e0=[450, 612.5, 300, 128.4])
NF('transport-a', 'vertical curves; sight distance', 'ft', 0, 864, "A crest vertical curve joins a +[g1|1]% grade to a -[g2|1]% grade. The required stopping sight distance is [S] ft. Assuming the sight distance is shorter than the curve, what minimum curve length is needed? Use L = A S^{2} / 2,158.",
   "On a crest, the hill itself blocks the driver's view. For a 3.5 ft eye height and a 2 ft object, with the sight distance shorter than the curve, L = A S^{2} / 2,158, where A is the algebraic difference in grades in percent. Check afterwards that S is less than L.",
   r"A = [g1|1] + [g2|1] = [g1+g2|1]%. || L = \frac{[g1+g2|1]([S])^{2}}{2,158} = [ans|0] ft. This is longer than [S] ft, so the assumption holds.",
   "(g1+g2)*S*S/2158", dict(g1=2.5, g2=2, S=700), units='USCS', fig=lambda e: vcurve(e['g1'], -e['g2'], 'L = ?'), g1=[2, 3, 1.5, 2.5], g2=[1.5, 2, 2.5, 3.5], S=[730, 645, 570, 820])
NF('transport-a', 'horizontal curves', 'ft', 1, 1432.4, "A horizontal curve has a degree of curve of [Dc|1]° by the arc definition. What is its radius?",
   "By the arc definition, the degree of curve is the central angle subtended by 100 ft of arc. A full circle of 360° has a circumference of 2πR, which gives R = 5,729.58 / D.",
   r"R = \frac{5,729.58}{[Dc|1]} = [ans|1] ft.",
   "5729.58/Dc", dict(Dc=3.5), units='USCS', Dc=[4, 2.5, 6, 8])
NF('transport-c', 'traffic flow relationships; level of service', 'pc/mi/ln', 1, 22.6, "A freeway carries [Vh] veh/h in one direction on [N] lanes, with a peak hour factor of [PHF|2] and [PT]% trucks (passenger car equivalent 2.0). The average speed is [S] mph. What is the density?",
   "Convert the volume to an equivalent passenger car flow rate per lane: divide by the peak hour factor, the number of lanes in that direction and the heavy vehicle factor, f_{HV} = 1 / (1 + P_{T}(E_{T} - 1)). Density is flow rate over speed.",
   r"f_{HV} = \frac{1}{1 + [PT/100|2](2.0 - 1)} = [1/(1+PT/100)|4]. || v_{p} = \frac{[Vh]}{[PHF|2]([N])([1/(1+PT/100)|4])} = [Vh/(PHF*N)*(1+PT/100)|0] pc/h/ln. || Density = \frac{[Vh/(PHF*N)*(1+PT/100)|0]}{[S]} = [ans|1] pc/mi/ln.",
   "Vh/(PHF*N)*(1+PT/100)/S", dict(Vh=4800, N=4, PHF=0.94, PT=6, S=64), units='USCS', Vh=[3600, 4200, 2400, 5400], N=[3, 3, 2, 4], PHF=[0.90, 0.92, 0.88, 0.95], PT=[10, 5, 8, 12], S=[65, 60, 62, 58])
NF('transport-e', 'Engineering Economics::single payment compound amount', 'veh/day', 0, 17831, "A road carries [V0] vehicles per day. Traffic grows at [r|1]% per year. What daily volume is expected in [n] years?",
   "Traffic growth compounds like interest: future volume = present volume × (1 + rate)^{years}. The factor is the single payment compound amount factor from engineering economics.",
   "V = [V0] × (1 + [r/100|3])^{[n]} = [V0] × [(1+r/100)**n|4] = [ans|0] vehicles per day.",
   "V0*(1+r/100)**n", dict(V0=15500, r=2.5, n=20), V0=[12000, 8500, 24000, 5200], r=[2, 3, 1.5, 4], n=[20, 15, 25, 10])
NF('transport-e', 'gravity model', 'trips', 0, 333, "A zone produces [Pz] trips. Three destination zones have attractions of [A1], [A2] and [A3] and friction factors of [F1], [F2] and [F3]. Using the gravity model with K = 1, how many trips go to the first destination?",
   "The gravity model splits a zone's trip productions among destinations in proportion to each destination's attractions times its friction factor. The shares sum to 1.",
   r"A × F for each zone: [A1*F1], [A2*F2] and [A3*F3]; sum = [A1*F1+A2*F2+A3*F3]. || Trips to the first = [Pz] × \frac{[A1*F1]}{[A1*F1+A2*F2+A3*F3]} = [ans|0].",
   "Pz*A1*F1/(A1*F1+A2*F2+A3*F3)", dict(Pz=1800, A1=350, A2=450, A3=200, F1=6, F2=3, F3=8), Pz=[1000, 2400, 600, 1500], A1=[300, 500, 200, 400], A2=[500, 800, 400, 600], A3=[200, 300, 100, 250], F1=[5, 2, 10, 4], F2=[2, 6, 5, 8], F3=[10, 4, 2, 3])
# ---------------- Water ----------------
NF('water-a', CE + '::NRCS; curve number', '', 1, 80, "A catchment is [a1|1] ha of pavement (curve number 98) and [a2|1] ha of lawn (curve number [cn2]). What is the composite curve number?",
   "For mixed land cover, use the area-weighted average curve number. Pavement is assigned 98 because surface pits hold a little water.",
   r"CN = \frac{[a1|1](98) + [a2|1]([cn2])}{[a1|1] + [a2|1]} = \frac{[a1*98+a2*cn2|1]}{[a1+a2|1]} = [ans|1].",
   "(a1*98+a2*cn2)/(a1+a2)", dict(a1=3, a2=9, cn2=70), a1=[2, 5, 1.5, 8], a2=[6, 5, 8.5, 4], cn2=[74, 61, 69, 80])
NF('water-b', CE + '::hydraulic jump', 'm', 2, 1.34, "Water flows [y1|2] m deep at [u|1] m/s in a rectangular channel just before a hydraulic jump. What is the depth after the jump? Use g = 9.81 m/s^{2}.",
   "A hydraulic jump takes supercritical flow to subcritical. The depths on either side are conjugate: y_{2} = (y_{1} / 2)(square root of (1 + 8 Fr_{1}^{2}) - 1), with the Froude number taken upstream. It must exceed 1 for a jump to occur.",
   r"Fr_{1} = \frac{[u|1]}{\sqrt{9.81([y1|2])}} = [u/sqrt(g*y1)|2], greater than 1. || y_{2} = \frac{[y1|2]}{2}(\sqrt{1 + 8([u/sqrt(g*y1)|2])^{2}} - 1) = [ans|2] m.",
   "y1/2*(sqrt(1+8*u*u/(g*y1))-1)", dict(y1=0.35, u=6.5), y1=[0.30, 0.50, 0.25, 0.40], u=[6.0, 7.0, 5.0, 8.0])
NF('water-b', CE + '::weir', 'm^{3}/s', 3, 0.605, "A suppressed rectangular weir is [Lw|1] m long, and the head over its crest is [H|2] m. Using Q = 1.84 L H^{3/2} in SI units, what is the discharge?",
   "Flow over a sharp-crested rectangular weir varies with the head to the 3/2 power, so a small error in head matters. A suppressed weir spans the full channel width and has no end contractions.",
   "Q = 1.84([Lw|1])([H|2])^{3/2} = 1.84 × [Lw|1] × [H**1.5|4] = [ans|3] m^{3}/s.",
   "1.84*Lw*H**1.5", dict(Lw=2.5, H=0.35), Lw=[2, 3.5, 1.2, 5], H=[0.30, 0.45, 0.20, 0.60])
NF('water-g', CE + "::Manning's equation", '%', 3, 0.330, "A [D] mm sewer flowing full must keep a velocity of at least 0.6 m/s. With Manning's n = 0.013, what minimum slope is needed, as a percentage?",
   "Set Manning's velocity equal to the self-cleansing minimum and solve for slope: S = (V n / R^{2/3})^{2}, with R = D / 4 for a full circular pipe. Larger pipes need flatter minimum slopes.",
   r"R = [D/1000|3] / 4 = [D/4000|4] m, and R^{2/3} = [(D/4000)**(2/3)|4]. || S = (\frac{0.6(0.013)}{[(D/4000)**(2/3)|4]})^{2} = [(0.6*0.013/(D/4000)**(2/3))**2|5] = [ans|3]%.",
   "(0.6*0.013/(D/4000)**(2/3))**2*100", dict(D=375), D=[200, 300, 450, 600])
NF('water-h', CE + "::Dupuit; unconfined aquifer", 'm/day', 2, 4.55, "A well in an unconfined aquifer is pumped at [Q] m^{3}/day. At steady state the saturated thickness is [h1|1] m at [r1] m from the well and [h2|1] m at [r2] m. What is the hydraulic conductivity?",
   "For steady flow to a well in an unconfined aquifer, Q = π K (h_{2}^{2} - h_{1}^{2}) / ln(r_{2} / r_{1}), where each h is the saturated thickness at that radius. Rearrange for K.",
   r"K = \frac{Q ln(r_{2} / r_{1})}{π(h_{2}^{2} - h_{1}^{2})} = \frac{[Q] ln([r2] / [r1])}{π([h2|1]^{2} - [h1|1]^{2})} = \frac{[Q]([log(r2/r1)|4])}{π([h2*h2-h1*h1|2])} = [ans|2] m/day.",
   "Q*log(r2/r1)/(pi*(h2*h2-h1*h1))", dict(Q=800, h1=20, r1=12, h2=21.4, r2=60), Q=[500, 1200, 300, 2000], h1=[18, 24.5, 11, 28], r1=[10, 15, 8, 20], h2=[19.5, 26, 12, 29.6], r2=[50, 90, 40, 120])
# ---------------- Geotechnical ----------------
NF('geotech-c', 'relative density', '%', 1, 62.3, "A sand has a field dry unit weight of [gd|1] kN/m^{3}. Its maximum and minimum dry unit weights are [gmax|1] and [gmin|1] kN/m^{3}. What is its relative density?",
   "Relative density places a granular soil between its loosest and densest states. In terms of dry unit weights, D_{r} = ((field - minimum) / (maximum - minimum)) × (maximum / field). It is not the same as relative compaction, which is simply field over maximum.",
   r"D_{r} = \frac{[gd|1] - [gmin|1]}{[gmax|1] - [gmin|1]} × \frac{[gmax|1]}{[gd|1]} × 100 = [(gd-gmin)/(gmax-gmin)|4] × [gmax/gd|4] × 100 = [ans|1]%. || For comparison, relative compaction = [gd|1] / [gmax|1] = [gd/gmax*100|1]%.",
   "(gd-gmin)/(gmax-gmin)*gmax/gd*100", dict(gd=16.8, gmax=18.4, gmin=14.8), gd=[16.5, 17.2, 15.4, 18.0], gmax=[18.0, 18.5, 17.0, 19.2], gmin=[14.5, 15.0, 14.0, 15.6])
NF('geotech-f', 'Mohr-Coulomb', '°', 1, 30, "A drained triaxial test on clean sand fails at a cell pressure of [s3] kPa and a major principal stress of [s1] kPa. What is the friction angle?",
   "For a soil with no cohesion the failure envelope passes through the origin and is tangent to the Mohr circle at failure. The geometry gives sin(friction angle) = radius / centre = (major - minor) / (major + minor).",
   r"sin(friction angle) = \frac{[s1] - [s3]}{[s1] + [s3]} = \frac{[s1-s3]}{[s1+s3]} = [(s1-s3)/(s1+s3)|4]. || Friction angle = [ans|1]°.",
   "asin((s1-s3)/(s1+s3))*180/pi", dict(s3=120, s1=400), s3=[100, 150, 80, 200], s1=[300, 520, 270, 680])
NF('geotech-g', 'bearing capacity; eccentricity', 'kPa', 1, 240, "A [B|1] m wide strip footing carries a vertical load of [P] kN per metre and a moment of [M] kN·m per metre. What is the maximum bearing pressure?",
   "A moment shifts the resultant by e = M / P. While e is within B / 6, the pressure under the footing is trapezoidal, with edge values (P / B)(1 ± 6e / B). The larger value is at the toe.",
   r"e = \frac{[M]}{[P]} = [M/P|3] m, which is less than B / 6 = [B/6|3] m. || q_{max} = \frac{[P]}{[B|1]}(1 + \frac{6([M/P|3])}{[B|1]}) = [P/B|1] × [1+6*M/P/B|3] = [ans|1] kPa.",
   "P/B*(1+6*(M/P)/B)", dict(B=2.4, P=420, M=84), B=[2, 2.5, 1.5, 3], P=[300, 450, 180, 600], M=[60, 90, 20, 150])
NF('geotech-i', 'compression index', '', 3, 0.315, "Using the correlation C_{c} = 0.009(LL - 10), what is the compression index of a clay with a liquid limit of [LL]?",
   "The compression index is the slope of the virgin compression line. For undisturbed clays of low to medium sensitivity it is often estimated from the liquid limit. The recompression index is commonly taken as about one sixth of it.",
   "C_{c} = 0.009([LL] - 10) = [ans|3]. The recompression index would be about [0.009*(LL-10)/6|3].",
   "0.009*(LL-10)", dict(LL=52), LL=[45, 60, 38, 72])
NF('geotech-j', 'slope failure; factor of safety', '', 2, 1.11, "A wedge of soil weighing [W] kN per metre can slide on a plane [Lp|1] m long inclined at [al]°. The soil has a cohesion of [c] kPa and a friction angle of [phi]°. What is the factor of safety against sliding?",
   "A planar slide is a block on an incline. The weight component down the plane drives it. Friction from the normal component, plus cohesion acting over the length of the plane, resists it.",
   r"Driving = [W] sin [al]° = [W*sin(rad(al))|1] kN/m. || Resisting = [c]([Lp|1]) + [W] cos [al]° tan [phi]° = [c*Lp|1] + [W*cos(rad(al))*tan(rad(phi))|1] = [c*Lp+W*cos(rad(al))*tan(rad(phi))|1] kN/m. || FS = \frac{[c*Lp+W*cos(rad(al))*tan(rad(phi))|1]}{[W*sin(rad(al))|1]} = [ans|2].",
   "(c*Lp+W*cos(rad(al))*tan(rad(phi)))/(W*sin(rad(al)))", dict(W=1000, al=28, Lp=14, c=12, phi=26), fig=lambda e: incline(e['al']), W=[800, 1200, 500, 1500], al=[30, 25, 28, 20], Lp=[12, 15, 8, 20], c=[10, 15, 8, 12], phi=[25, 28, 22, 30])
# ---------------- Materials ----------------
NF('materials-a', '-', 'kg', 1, 30.0, "A concrete batch calls for [Ws] kg of sand in the saturated surface-dry condition. The stockpiled sand has a total moisture content of [mc|1]% and an absorption of [ab|1]%. How much free water does that sand bring into the batch?",
   "Mix designs assume saturated surface-dry aggregate. Moisture beyond the absorption is free water that would raise the water-cement ratio, so it is found and taken off the batch water.",
   r"Oven-dry mass = \frac{[Ws]}{1 + [ab/100|3]} = [Ws/(1+ab/100)|1] kg. || Stockpile mass = [Ws/(1+ab/100)|1] × (1 + [mc/100|3]) = [Ws/(1+ab/100)*(1+mc/100)|1] kg. || Free water = [Ws/(1+ab/100)*(1+mc/100)|1] - [Ws] = [ans|1] kg.",
   "Ws/(1+ab/100)*(1+mc/100)-Ws", dict(Ws=760, mc=4.6, ab=1.1), Ws=[800, 650, 900, 720], mc=[5.0, 4.2, 6.5, 3.8], ab=[1.2, 0.8, 1.5, 1.0])
NF('materials-a', CE + '::water-cement ratio', 'kg', 1, 60, "A truck carries [vol|1] m^{3} of concrete with [cem] kg of cement per cubic metre. The maximum water-cement ratio is [wc|2], and [wb] kg of water has been batched. How much more water may be added on site?",
   "The water-cement ratio is by mass. The most water the load may hold is the maximum ratio times the total cement in the truck; anything already batched counts against it.",
   "Cement in the truck = [cem] × [vol|1] = [cem*vol|0] kg. || Allowable water = [wc|2] × [cem*vol|0] = [wc*cem*vol|1] kg. || May still be added: [wc*cem*vol|1] - [wb] = [ans|1] kg.",
   "wc*cem*vol-wb", dict(vol=7, cem=360, wc=0.44, wb=1050), vol=[8, 6, 7.5, 9], cem=[350, 400, 320, 380], wc=[0.45, 0.40, 0.50, 0.42], wb=[1200, 885, 1150, 1400])
# ---------------- Economics ----------------
NF('econ-b', 'Engineering Economics::depreciation; straight line', '$', 0, 32000, "Equipment costs $[C], has a salvage value of $[Sv] and a life of [n] years. Using straight-line depreciation, what is its book value after [yr] years?",
   "Straight-line depreciation writes off the same amount every year: (cost - salvage) / life. Book value is the cost minus the depreciation taken so far.",
   r"Annual depreciation = \frac{[C] - [Sv]}{[n]} = $[(C-Sv)/n|0]. || Book value = [C] - [yr]([(C-Sv)/n|0]) = $[ans|0].",
   "C-(C-Sv)/n*yr", dict(C=64000, Sv=4000, n=8, yr=3), C=[50000, 120000, 36000, 80000], Sv=[5000, 20000, 6000, 8000], n=[10, 8, 5, 12], yr=[4, 3, 2, 5])
NF('econ-a', 'Engineering Economics::uniform series compound amount', '$', 0, 822470, "$[A] is deposited at the end of each year into an account paying [i]% per year. What is the balance after [n] years?",
   "A uniform series of end-of-period deposits grows to F = A × ((1 + i)^{n} - 1) / i, the uniform series compound amount factor (F/A, i, n). The last deposit earns no interest.",
   r"(F/A, [i]%, [n]) = \frac{(1 + [i/100|2])^{[n]} - 1}{[i/100|2]} = [((1+i/100)**n-1)/(i/100)|3]. || F = [A] × [((1+i/100)**n-1)/(i/100)|3] = $[ans|0].",
   "A*((1+i/100)**n-1)/(i/100)", dict(A=4000, i=7, n=20), fig=lambda e: cashflow(min(e['n'], 30), A='$' + nf(e['A']), F='F = ?'), A=[5000, 2000, 10000, 3600], i=[10, 6, 8, 5], n=[30, 20, 15, 25])
NF('econ-c', 'Engineering Economics::break-even analysis; capital recovery', 'units per year', 0, 3698, "A machine costs $[Pm] and $[fx] per year to run, plus $[uc|2] for each unit it makes. It lasts [n] years with no salvage value. Buying the part instead costs $[pr|2] per unit. At [i]% interest, how many units per year make owning the machine break even?",
   "Put owning on an annual basis: the first cost times the capital recovery factor (A/P), plus the fixed annual cost, plus the unit cost times the quantity. Set that equal to the purchase price times the quantity and solve.",
   r"(A/P, [i]%, [n]) = [i/100*(1+i/100)**n/((1+i/100)**n-1)|5], so the annual cost of owning before any units = [Pm]([i/100*(1+i/100)**n/((1+i/100)**n-1)|5]) + [fx] = $[Pm*(i/100*(1+i/100)**n/((1+i/100)**n-1))+fx|0]. || Each unit made saves [pr|2] - [uc|2] = $[pr-uc|2]. || Break-even = \frac{[Pm*(i/100*(1+i/100)**n/((1+i/100)**n-1))+fx|0]}{[pr-uc|2]} = [ans|0] units per year.",
   "(Pm*(i/100*(1+i/100)**n/((1+i/100)**n-1))+fx)/(pr-uc)", dict(Pm=75000, fx=5000, uc=2.8, pr=6.5, n=10, i=9), Pm=[60000, 150000, 25000, 90000], fx=[4000, 10000, 1500, 6000], uc=[2.50, 4.00, 1.20, 3.00], pr=[6.00, 9.50, 3.00, 7.50], n=[10, 8, 5, 12], i=[8, 10, 6, 7])
# ---------------- Fluids ----------------
NF('fluids-c', 'pressure field in a static liquid', 'kPa', 2, 32.13, "A tank holds [h1|1] m of oil (specific gravity [sg|2]) floating on [h2|1] m of water. What is the gauge pressure on the floor of the tank? Use 9.81 kN/m^{3} for water.",
   "Pressure at depth is the sum of specific weight times thickness for each layer above. The lower layer starts from the pressure at the interface, not from zero.",
   "Pressure at the interface = [sg|2](9.81)([h1|1]) = [sg*9.81*h1|2] kPa. || Add the water: [sg*9.81*h1|2] + 9.81([h2|1]) = [ans|2] kPa.",
   "9.81*(sg*h1+h2)", dict(h1=1.2, sg=0.82, h2=1.8), h1=[1.5, 2.0, 0.8, 3.0], sg=[0.85, 0.90, 0.80, 0.88], h2=[2.0, 1.0, 2.5, 1.5])
NF('fluids-d', 'pipe bends; impulse-momentum principle', 'kN', 2, 14.64, "A horizontal [d] mm pipe bend turns the flow through [th|1]°. The pressure is [p] kPa and velocities are low enough to ignore the momentum change. What is the resultant thrust on the bend?",
   "The pressure force p A acts along the pipe axis at each end of the bend. The two are equal in size but differ in direction, leaving a resultant of 2 p A sin(angle / 2) that a thrust block must resist.",
   r"A = \frac{π([d/1000|3])^{2}}{4} = [pi*(d/1000)**2/4|5] m^{2}, so p A = [p*pi*(d/1000)**2/4|2] kN. || Thrust = 2([p*pi*(d/1000)**2/4|2]) sin([th/2|2]°) = [ans|2] kN.",
   "2*p*pi*(d/1000)**2/4*sin(rad(th/2))", dict(d=250, th=60, p=450), d=[300, 200, 450, 600], th=[30, 45, 90, 22.5], p=[400, 600, 350, 500])
NF('fluids-c', 'buoyancy; Archimedes', 'kN', 2, 7.85, "A timber raft has a volume of [Vr|1] m^{3} and a specific gravity of [sg|2]. What is the largest cargo weight it can carry in fresh water before it is fully submerged?",
   "At the limit the raft is fully submerged and displaces its whole volume of water. The buoyant force then equals the raft's weight plus the cargo, so the cargo is the weight of displaced water minus the weight of the raft.",
   "Buoyant force when submerged = 9.81([Vr|1]) = [9.81*Vr|2] kN. || Raft weight = [sg|2](9.81)([Vr|1]) = [sg*9.81*Vr|2] kN. || Cargo = [9.81*Vr|2] - [sg*9.81*Vr|2] = [ans|2] kN.",
   "9.81*Vr*(1-sg)", dict(Vr=2.8, sg=0.62), Vr=[2.0, 3.5, 1.2, 5.0], sg=[0.60, 0.55, 0.70, 0.65])
# ---------------- Surveying ----------------
NF('surveying-a', 'Mathematics::trigonometry', '°', 4, 38.46, "Convert [dd]° [mi]' [ss]\" to decimal degrees.",
   "A degree has 60 minutes and a minute has 60 seconds, so decimal degrees = degrees + minutes / 60 + seconds / 3,600.",
   r"[dd] + \frac{[mi]}{60} + \frac{[ss]}{3,600} = [dd] + [mi/60|4] + [ss/3600|4] = [ans|4]°.",
   "dd+mi/60+ss/3600", dict(dd=74, mi=12, ss=45), tol=0.0005, dd=[38, 112, 7, 256], mi=[27, 45, 8, 30], ss=[36, 18, 24, 54])
NF('surveying-c', 'prismoidal formula; earthwork formulas', 'm^{3}', 0, 1700, "Two end sections of a cut are [L] m apart, with areas of [A1] m^{2} and [A2] m^{2}. The section midway between them has an area of [Am] m^{2}. Using the prismoidal formula, what is the volume?",
   "The prismoidal formula is a weighted average of three sections: each end once and the middle four times, divided by six. It is exact for a prismoid, and the average end area method gives a slightly larger volume.",
   r"V = \frac{L(A_{1} + 4A_{m} + A_{2})}{6} = \frac{[L]([A1] + 4([Am]) + [A2])}{6} = [ans|0] m^{3}. || Average end area would give [L*(A1+A2)/2|0] m^{3}.",
   "L*(A1+4*Am+A2)/6", dict(L=50, A1=16, Am=22, A2=30), L=[60, 40, 100, 30], A1=[20, 12, 35, 8], Am=[28, 17, 44, 13], A2=[38, 24, 56, 20])
NF('surveying-a', 'latitude; departure', 'm', 3, -0.06, "A closed traverse has a perimeter of [per] m and a misclosure in latitude of [ml|2] m. Using the compass rule, what correction is applied to the latitude of a [leg|1] m leg?",
   "The compass rule shares the misclosure among the legs in proportion to their lengths, with the opposite sign so that the corrected latitudes sum to zero.",
   r"Correction = -(misclosure) × \frac{leg length}{perimeter} = -([ml|2]) × \frac{[leg|1]}{[per]} = [ans|3] m.",
   "-ml*leg/per", dict(per=960, ml=0.16, leg=240), tol=0.02, per=[1200, 850, 2400, 640], ml=[0.24, -0.18, 0.36, 0.08], leg=[300, 212.5, 600, 160])
# ---------------- Dynamics ----------------
NF('dynamics-a', 'constant acceleration; particle kinematics', 's', 2, 5.69, "A car travelling at [v] m/s brakes on a [G]% upgrade. Its brakes alone give a deceleration of [a|1] m/s^{2}. How long does it take to stop? Use g = 9.81 m/s^{2}.",
   "On a grade, gravity adds g times the grade to the deceleration when climbing, and takes it away when descending. With a constant total deceleration, stopping time is the speed divided by it.",
   r"Deceleration from the grade = 9.81 × [G/100|2] = [g*G/100|3] m/s^{2}. || Total = [a|1] + [g*G/100|3] = [a+g*G/100|3] m/s^{2}. || t = \frac{[v]}{[a+g*G/100|3]} = [ans|2] s.",
   "v/(a+g*G/100)", dict(v=22, G=5, a=4.5), v=[25, 30, 20, 15], G=[4, 6, 3, 5], a=[4.0, 3.5, 5.0, 3.0])
NF('dynamics-c', "Newton's second law; normal and tangential components", 'm', 1, 81.5, "A car travels at [v] m/s around a flat curve. The coefficient of friction between the tyres and the road is [mu|2]. What is the smallest radius it can follow without sliding? Use g = 9.81 m/s^{2}.",
   "On a flat curve friction alone supplies the inward force m v^{2} / R, and friction cannot exceed the coefficient times the weight. Setting the two equal gives the smallest radius, and the mass cancels.",
   r"\frac{m v^{2}}{R} = (coefficient) m g, so R = \frac{v^{2}}{(coefficient) g} = \frac{[v]^{2}}{[mu|2](9.81)} = [ans|1] m.",
   "v*v/(mu*g)", dict(v=18, mu=0.45), v=[20, 25, 15, 30], mu=[0.50, 0.35, 0.60, 0.40])
NF('dynamics-c', "Newton's second law", 'm/s^{2}', 2, 3.92, "A [m1] kg block on a frictionless table is tied by a cord over a light, frictionless pulley to a hanging [m2] kg block. What is the acceleration of the blocks? Use g = 9.81 m/s^{2}.",
   "Bodies joined by a taut cord share one acceleration. Treat them as a single system along the cord: the only driving force is the weight of the hanging block, and it must accelerate the total mass. The tension is internal and cancels.",
   r"Driving force = [m2](9.81) = [m2*g|2] N. Total mass = [m1] + [m2] = [m1+m2] kg. || a = \frac{[m2*g|2]}{[m1+m2]} = [ans|2] m/s^{2}, which is less than g as it must be.",
   "m2*g/(m1+m2)", dict(m1=9, m2=3), m1=[6, 10, 4, 15], m2=[4, 5, 6, 5])
NF('dynamics-d', 'work and energy; mass moment of inertia', 'rad/s', 2, 4.95, "A uniform slender rod [L|1] m long is released from rest in a horizontal position and swings about a frictionless pin at one end. What is its angular speed as it passes through the vertical? Use g = 9.81 m/s^{2}.",
   "Energy is conserved. The rod's centre of mass falls by L / 2, and that potential energy becomes rotational kinetic energy about the pin, where the rod's moment of inertia is m L^{2} / 3.",
   r"m g \frac{L}{2} = \frac{1}{2}(\frac{m L^{2}}{3})(angular speed)^{2}, so angular speed = \sqrt{\frac{3 g}{L}} = \sqrt{\frac{3(9.81)}{[L|1]}} = [ans|2] rad/s.",
   "sqrt(3*g/L)", dict(L=1.8), L=[1.2, 2.0, 0.8, 1.5])

def _env(sp, k=0):
    e = dict(NAMES); e.update({n: v[k] for n, v in sp['P'].items()}); e['ans'] = eval(sp['ans'], {'__builtins__': {}}, e); return e
def base_mode():
    from author_dsl import N, save as dsave
    for sp in SPECS:
        e = _env(sp); val = e['ans']
        assert abs(val - sp['v1']) <= 0.011 * max(abs(sp['v1']), 1e-9), (sp['stem'][:50], val, sp['v1'])
        calc = "(lambda %s: %s)(%s)" % (', '.join(sp['P']), sp['ans'], ', '.join(repr(v[0]) for v in sp['P'].values()))
        N(sp['sub'], render(sp['stem'], e), round(val, sp['dp']), sp['unit'], render(sp['concept'], e), render(sp['sol'], e), calc, tol=sp['tol'], units=sp['units'])
    dsave('f2'); print('bases added:', len(SPECS))
def _register():
    for sp in SPECS:
        topic = sp['sub'].rsplit('-', 1)[0]; stem0 = render(sp['stem'], _env(sp))
        sp['base'] = next(x['id'] for x in _load(topic) if x['stem'] == stem0)
        V(sp['base'], sp['stem'], sp['P'], sp['ans'], sp['sol'], None, sp['dp'], sp['fig'], None, sp['concept'])
if sys.argv[1:] != ['base']: _register()
if __name__ == '__main__':
    if sys.argv[1:] == ['base']: base_mode()
    else:
        save(); json.dump({sp['base']: sp['find'] for sp in SPECS}, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'find2.json'), 'w'), indent=1)
