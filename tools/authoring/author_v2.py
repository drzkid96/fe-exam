"""Version families, part 2: geotechnical, fluid mechanics, surveying."""
from author_v import *
def F(base, stem, concept, sol, ans, wrong=None, dp=None, fig=None, sfig=None, **P): V(base, stem, P, ans, sol, wrong, dp, fig, sfig, concept)

# ---------------- Geotechnical ----------------
F('geotech-0001', "A moist soil sample has a mass of [M|2] kg and a volume of 0.001 m^{3}. Its water content is [wc]%. What is the dry density?",
  "Water content is the mass of water divided by the mass of dry solids, so the moist mass is the dry mass times (1 + w). Dividing the moist (bulk) density by (1 + w) therefore gives the dry density.",
  r"Bulk density = \frac{[M|2]}{0.001} = [M*1000|0] kg/m^{3}. || Dry density = \frac{[M*1000|0]}{1 + [wc/100|3]} = [ans|0] kg/m^{3}.",
  "M/0.001/(1+wc/100)", dp=0, M=[1.92, 2.05, 1.80, 1.98], wc=[20, 25, 12.5, 10])
F('geotech-0002', "A soil has a dry density of [rd] kg/m^{3}. The specific gravity of its solids is [Gs|2]. What is its void ratio?",
  "Dry density relates to void ratio through the phase diagram: dry density = G_{s} × (density of water) / (1 + e). Solving for e gives the volume of voids per unit volume of solids. Do not confuse it with porosity, n = e / (1 + e).",
  r"e = \frac{G_{s} × 1,000}{dry density} - 1 = \frac{[Gs|2](1,000)}{[rd]} - 1 = [Gs*1000/rd|3] - 1 = [ans|3].",
  "Gs*1000/rd-1", wrong=["1-rd/(Gs*1000)", "rd/(Gs*1000)", "Gs*1000/rd"], dp=3, rd=[1600, 1750, 1500, 1850], Gs=[2.70, 2.65, 2.70, 2.68])
F('geotech-0003', "A sand deposit has a unit weight of [g1] kN/m^{3} above the water table and a saturated unit weight of [g2] kN/m^{3} below it. The water table is [zw] m below the ground surface. What is the vertical effective stress at a depth of [z] m? Use 9.81 kN/m^{3} for water.",
  "Effective stress is total stress minus pore water pressure. Total stress is the weight of everything above the point; pore pressure is the unit weight of water times the depth below the water table. Effective stress, not total stress, controls strength and settlement.",
  "Total stress = [g1]([zw]) + [g2]([z] - [zw]) = [g1*zw+g2*(z-zw)|1] kPa. || Pore pressure = 9.81([z] - [zw]) = [9.81*(z-zw)|1] kPa. || Effective stress = [g1*zw+g2*(z-zw)|1] - [9.81*(z-zw)|1] = [ans|1] kPa.",
  "g1*zw+(g2-9.81)*(z-zw)", wrong=["9.81*(z-zw)", "g1*zw+g2*(z-zw)", "g1*zw+(g2+9.81)*(z-zw)"], dp=1, fig=lambda e: soil(e['g1'], e['g2'], e['zw'], e['z']), g1=[17, 18, 16, 17.5], g2=[19, 20, 19.5, 20.5], zw=[2, 1.5, 3, 1], z=[6, 5, 8, 4])
F('geotech-0004', "A retaining wall holds back dry sand with a friction angle of [phi]° and a level surface. What is the Rankine active earth pressure coefficient?",
  "The Rankine active coefficient is the ratio of horizontal to vertical effective stress when the soil has expanded enough to mobilise its full strength: K_{a} = tan^{2}(45° - friction angle / 2). A stronger soil pushes less on the wall. The passive coefficient is its reciprocal.",
  "K_{a} = tan^{2}(45° - [phi]° / 2) = tan^{2}([45-phi/2]°) = [ans|3].",
  "tan(rad(45-phi/2))**2", wrong=["1-sin(rad(phi))", "tan(rad(phi))", "tan(rad(45+phi/2))**2"], dp=3, phi=[30, 35, 25, 40])
F('geotech-0005', "A soil has an effective cohesion of [c] kPa and an effective friction angle of [phi]°. What is its shear strength on a plane where the effective normal stress is [sn] kPa?",
  "The Mohr-Coulomb criterion gives shear strength as a cohesion intercept plus a frictional part that grows with effective normal stress: strength = c' + (normal stress) tan(friction angle).",
  "Shear strength = [c] + [sn] tan [phi]° = [c] + [sn*tan(rad(phi))|1] = [ans|1] kPa.",
  "c+sn*tan(rad(phi))", dp=1, c=[10, 0, 25, 15], sn=[100, 150, 80, 200], phi=[30, 35, 20, 28])
F('geotech-0006', "A clay has a liquid limit of [LL] and a plastic limit of [PL]. What is its plasticity index?",
  "The plasticity index is the range of water content over which the soil behaves plastically: PI = LL - PL. With the liquid limit it places a fine-grained soil on the plasticity chart for classification.",
  "PI = LL - PL = [LL] - [PL] = [ans].", "LL-PL", wrong=["PL/LL", "(LL+PL)/2", "LL+PL"], LL=[45, 60, 38, 52], PL=[22, 25, 20, 30])
F('geotech-0009', "A grain size curve gives D_{60} = [D60] mm, D_{30} = [D30] mm and D_{10} = [D10] mm. What is the coefficient of uniformity?",
  "The coefficient of uniformity, C_{u} = D_{60} / D_{10}, measures the spread of particle sizes. The coefficient of curvature, C_{c} = D_{30}^{2} / (D_{60} × D_{10}), measures the shape of the curve. Both are needed to call a sand or gravel well graded.",
  r"C_{u} = \frac{D_{60}}{D_{10}} = \frac{[D60]}{[D10]} = [ans|2]. For reference, C_{c} = \frac{[D30]^{2}}{[D60] × [D10]} = [D30*D30/(D60*D10)|2].",
  "D60/D10", dp=2, D60=[0.84, 1.2, 0.6, 2.4], D30=[0.42, 0.5, 0.3, 0.9], D10=[0.12, 0.08, 0.15, 0.2])
F('geotech-0010', "A field density test gives a dry unit weight of [fd|1] kN/m^{3}. The maximum dry unit weight from the Proctor test is [mx|1] kN/m^{3}. What is the relative compaction?",
  "Relative compaction compares the dry unit weight achieved in the field with the laboratory maximum from the Proctor test. Specifications usually require a minimum percentage, often 90% to 95%.",
  r"Relative compaction = \frac{[fd|1]}{[mx|1]} × 100 = [ans|1]%.", "fd/mx*100", dp=1, fd=[17.1, 16.2, 18.4, 17.6], mx=[18.0, 17.5, 19.2, 18.9])
F('geotech-0011', "In a constant-head permeability test, [Q] cm^{3} of water passes through a sample in [t] s. The sample is [L] cm long with a cross-section of [A] cm^{2}, and the head difference is [h] cm. What is the coefficient of permeability?",
  "Darcy's law: flow rate = k i A, where the hydraulic gradient i is head loss divided by flow length. In a constant-head test the flow rate is the collected volume divided by time, so k = Q L / (A h t).",
  r"Hydraulic gradient i = [h] / [L] = [h/L|2]. || Flow rate = [Q] / [t] = [Q/t|2] cm^{3}/s. || k = \frac{[Q/t|2]}{[h/L|2] × [A]} = [ans] cm/s.",
  "Q*L/(A*h*t)", wrong=["Q*L/(A*h*t)/10", "Q*L/(A*h*t)*10", "Q*h/(A*L*t)"], Q=[600, 480, 900, 500], t=[300, 200, 300, 250], L=[15, 10, 20, 12], A=[40, 40, 50, 30], h=[30, 30, 40, 20])
F('geotech-0012', "A [H] m high wall retains dry sand with a unit weight of [gam] kN/m^{3}. The Rankine active coefficient is [Ka|3]. What is the total active force per metre of wall?",
  "Active pressure grows linearly with depth, from zero at the top to K_{a} × unit weight × H at the base. The resultant is the area of that triangle, (1/2) K_{a} (unit weight) H^{2}, and it acts at one third of the height above the base.",
  r"Pressure at the base = [Ka|3]([gam])([H]) = [Ka*gam*H|1] kPa. || P_{a} = \frac{1}{2}([Ka*gam*H|1])([H]) = [ans|1] kN per metre of wall, acting [H/3|2] m above the base.",
  "0.5*Ka*gam*H*H", dp=1, fig=lambda e: wall(e['H']), sfig=lambda e: wall(e['H'], e['ans']), H=[4, 5, 6, 3], gam=[18, 17, 19, 20], Ka=[0.333, 0.307, 0.271, 0.406])
F('geotech-0013', "An unconfined compression test on a clay gives a compressive strength of [qu] kPa. What is the undrained shear strength?",
  "In an unconfined test the minor principal stress is zero and the major principal stress at failure is q_{u}. The Mohr circle therefore has a radius of q_{u} / 2, which is the undrained shear strength of a saturated clay (friction angle taken as zero).",
  r"s_{u} = \frac{q_{u}}{2} = \frac{[qu]}{2} = [ans] kPa.", "qu/2", wrong=["qu/4", "qu", "2*qu"], qu=[120, 80, 200, 150])
F('geotech-0014', "A strip footing bears [D] m below the surface of a clay with a cohesion of [c] kPa and a unit weight of [gam] kN/m^{3}. Using bearing capacity factors N_{c} = 5.7, N_{q} = 1.0 and a zero third factor, what is the ultimate bearing capacity?",
  "Terzaghi's equation for a strip footing adds three resistances: cohesion (c N_{c}), surcharge from the soil beside the footing (unit weight × depth × N_{q}) and the weight of soil below (half × unit weight × B × N_{gamma}). For clay in undrained loading the third term is zero.",
  "q_{ult} = c N_{c} + (unit weight)(D) N_{q} = [c](5.7) + [gam]([D])(1.0) = [c*5.7|1] + [gam*D|1] = [ans|1] kPa.",
  "c*5.7+gam*D", dp=1, c=[50, 75, 40, 100], D=[1, 1.5, 2, 1.2], gam=[18, 17, 19, 18])
F('geotech-0015', "A square footing must carry a [P] kN column load. The ultimate bearing capacity is [qu] kPa and the factor of safety is [FS]. What footing width is required?",
  "Allowable bearing pressure is the ultimate capacity divided by the factor of safety. The required area is load divided by allowable pressure, and for a square footing the width is the square root of the area.",
  r"q_{allow} = [qu] / [FS] = [qu/FS|1] kPa. || Area = \frac{[P]}{[qu/FS|1]} = [P*FS/qu|2] m^{2}. || B = \sqrt{[P*FS/qu|2]} = [ans|2] m.",
  "sqrt(P*FS/qu)", dp=2, fig=lambda e: footing(None, e['P']), P=[600, 900, 1200, 450], qu=[450, 300, 600, 540], FS=[3, 3, 2.5, 3])
F('geotech-0016', "A [s] m square pile is [L] m long. The average skin friction is [fs] kPa and the end bearing resistance is [qp] kPa. What is the ultimate capacity of the pile?",
  "A pile carries load two ways: skin friction acting on the surface area of the shaft (perimeter × length) and end bearing acting on the tip area. The ultimate capacity is the sum.",
  "Shaft: [fs] × (4 × [s]) × [L] = [fs*4*s*L|0] kN. || Tip: [qp] × [s]^{2} = [qp*s*s|0] kN. || Q_{ult} = [fs*4*s*L|0] + [qp*s*s|0] = [ans|0] kN.",
  "fs*4*s*L+qp*s*s", dp=0, s=[0.3, 0.4, 0.35, 0.45], L=[10, 12, 15, 18], fs=[40, 50, 35, 60], qp=[2000, 1500, 2500, 3000])
F('geotech-0018', "A [H] m thick normally consolidated clay layer has a compression index of [Cc|2] and an initial void ratio of [e0|1]. The effective stress at mid-layer rises from [p1] kPa to [p2] kPa. What is the primary consolidation settlement?",
  "For normally consolidated clay, void ratio falls linearly with the logarithm of effective stress, at slope C_{c}. Settlement is the change in void ratio converted to a change in layer thickness: S = C_{c} H / (1 + e_{0}) × log_{10}(final stress / initial stress).",
  r"S = \frac{C_{c} H}{1 + e_{0}} log_{10}(\frac{p_{2}}{p_{1}}) = \frac{[Cc|2]([H])}{1 + [e0|1]} log_{10}(\frac{[p2]}{[p1]}) = [Cc*H/(1+e0)|3] × [log10(p2/p1)|3] = [ans/1000|3] m = [ans|0] mm.",
  "Cc*H/(1+e0)*log10(p2/p1)*1000", dp=0, H=[4, 3, 6, 5], Cc=[0.30, 0.25, 0.40, 0.36], e0=[1.0, 0.8, 1.2, 1.1], p1=[100, 80, 120, 150], p2=[200, 160, 180, 225])
F('geotech-0019', "A [H] m thick clay layer drains from both its top and bottom. Its coefficient of consolidation is [cv|1] m^{2}/year. Using a time factor of 0.197 for 50% consolidation, how long does 50% consolidation take?",
  "Consolidation time follows t = T_{v} H_{dr}^{2} / c_{v}, where H_{dr} is the longest path water must travel to drain. With drainage at both faces, H_{dr} is half the layer thickness, which makes consolidation four times faster than single drainage.",
  r"H_{dr} = [H] / 2 = [H/2] m. || t = \frac{T_{v} H_{dr}^{2}}{c_{v}} = \frac{0.197([H/2])^{2}}{[cv|1]} = [ans|3] years.",
  "0.197*(H/2)**2/cv", wrong=["0.197*(H/2)**2/cv/4", "0.197*(H/2)**2/cv*2", "0.197*H**2/cv"], dp=3, H=[4, 6, 3, 8], cv=[2.0, 1.5, 0.9, 4.0])
F('geotech-0020', "A long slope of dry sand stands at [b]° to the horizontal. The friction angle of the sand is [phi]°. What is the factor of safety against sliding?",
  "For an infinite slope in dry cohesionless soil, the resisting and driving forces on a plane parallel to the surface both scale with the weight, so FS = tan(friction angle) / tan(slope angle). The slope is at the point of failure when it stands at the friction angle.",
  r"FS = \frac{tan [phi]°}{tan [b]°} = \frac{[tan(rad(phi))|3]}{[tan(rad(b))|3]} = [ans|2].",
  "tan(rad(phi))/tan(rad(b))", wrong=["tan(rad(b))/tan(rad(phi))", "sin(rad(phi))/sin(rad(b))", "tan(rad(phi))/sin(rad(b))"], dp=3, fig=lambda e: incline(e['b']), b=[25, 20, 30, 18], phi=[35, 32, 38, 30])
F('geotech-0021', "A circular slip surface in clay has a radius of [R] m and an arc length of [La] m. The undrained shear strength is [su] kPa. The sliding mass weighs [W] kN per metre and its centroid is [x] m horizontally from the centre of the circle. What is the factor of safety?",
  "For a circular slip in clay under undrained conditions, take moments about the centre of the circle. The resisting moment is the shear strength acting along the arc at radius R; the driving moment is the weight times its horizontal lever arm.",
  r"Resisting moment = s_{u} × arc length × R = [su]([La])([R]) = [su*La*R] kN·m per metre. || Driving moment = W x = [W]([x]) = [W*x] kN·m per metre. || FS = \frac{[su*La*R]}{[W*x]} = [ans|2].",
  "su*La*R/(W*x)", dp=2, R=[15, 12, 20, 10], La=[20, 18, 28, 14], su=[30, 40, 25, 50], W=[1500, 1200, 2000, 800], x=[4, 3.6, 5, 3.5])
F('geotech-0023', "A clay subgrade is to be treated with [pct]% lime by dry mass. The soil has a dry density of [rd] kg/m^{3} and [Vol] m^{3} is to be treated. How much lime is needed?",
  "Stabiliser quantities are specified as a percentage of the dry mass of soil. Find the dry mass from dry density × volume, then take the percentage.",
  "Dry mass of soil = [rd] × [Vol] = [rd*Vol] kg. || Lime = [pct]% × [rd*Vol] = [ans|0] kg.",
  "pct/100*rd*Vol", dp=0, pct=[5, 4, 6, 3], rd=[1800, 1700, 1650, 1900], Vol=[300, 500, 250, 400])

# ---------------- Fluid mechanics ----------------
F('fluids-0001', "What is the gauge pressure [h] m below the surface of a freshwater reservoir? Use a specific weight of 9.81 kN/m^{3}.",
  "In a fluid at rest, pressure increases linearly with depth: p = (specific weight) × h. Gauge pressure is measured relative to the atmosphere, so it is zero at the free surface.",
  "p = (specific weight)(h) = 9.81 × [h] = [ans|1] kPa gauge.",
  "9.81*h", wrong=["h", "9.81*h/2", "9.81*h+101.3"], dp=1, h=[12, 8, 20, 5])
F('fluids-0002', "A liquid has a specific gravity of [SG|2]. What is its specific weight? Use 9.81 kN/m^{3} for water.",
  "Specific gravity is the ratio of a liquid's density (or specific weight) to that of water. Multiply by the specific weight of water to get the liquid's specific weight.",
  "Specific weight = SG × 9.81 = [SG|2] × 9.81 = [ans|2] kN/m^{3}.",
  "SG*9.81", wrong=["SG", "9.81", "9.81/SG"], dp=2, SG=[0.85, 0.80, 1.26, 0.92])
F('fluids-0003', "Water flows at [v] m/s in a [d1] mm diameter pipe. The pipe narrows to [d2] mm. What is the velocity in the narrow section?",
  "Continuity for an incompressible fluid: the flow rate A V is the same at every section. Area scales with diameter squared, so velocity scales with the inverse square of the diameter ratio.",
  r"A_{1} V_{1} = A_{2} V_{2}. || V_{2} = V_{1}(\frac{d_{1}}{d_{2}})^{2} = [v](\frac{[d1]}{[d2]})^{2} = [v] × [(d1/d2)**2|2] = [ans|2] m/s.",
  "v*(d1/d2)**2", dp=2, fig=lambda e: pipe(e['d1'], e['d2']), v=[2, 1.5, 3, 1.2], d1=[200, 300, 150, 400], d2=[100, 150, 100, 200])
F('fluids-0004', "A Pitot tube in a water stream shows a stagnation head [h|2] m higher than the static head. What is the flow velocity? Use g = 9.81 m/s^{2}.",
  "At the tip of a Pitot tube the flow is brought to rest and its velocity head, V^{2} / 2g, is converted to pressure head. The difference between stagnation and static head is therefore the velocity head.",
  r"\frac{V^{2}}{2g} = [h|2] m, so V = \sqrt{2(9.81)([h|2])} = [ans|2] m/s.",
  "sqrt(2*g*h)", wrong=["sqrt(2*h)", "sqrt(g*h)", "g*h"], dp=2, h=[0.45, 0.30, 0.80, 1.25])
F('fluids-0005', "A vertical rectangular gate is [b] m wide and [h] m tall. Its top edge is at the water surface. What is the total hydrostatic force on the gate? Use 9.81 kN/m^{3}.",
  "The resultant force on a submerged plane surface is the pressure at the centroid of the area times the area. For a gate that reaches the surface the pressure diagram is a triangle, and the force acts at two thirds of the depth.",
  "Depth to centroid = [h] / 2 = [h/2] m, so pressure there = 9.81 × [h/2] = [9.81*h/2|2] kPa. || Area = [b] × [h] = [b*h] m^{2}. || F = [9.81*h/2|2] × [b*h] = [ans|1] kN, acting [2*h/3|2] m below the surface.",
  "9.81*h/2*b*h", dp=1, fig=lambda e: gate(e['b'], e['h']), b=[2, 3, 1.5, 4], h=[3, 2, 4, 2.5])
F('fluids-0006', "Water discharges through a [d] mm diameter orifice under a head of [h] m. The discharge coefficient is [Cd|2]. What is the flow rate? Use g = 9.81 m/s^{2}.",
  "Torricelli's result gives the ideal jet velocity as the square root of 2 g h. Real flow is smaller because of jet contraction and friction, which the discharge coefficient accounts for: Q = C_{d} A × square root of (2 g h).",
  r"A = \frac{π([d/1000|3])^{2}}{4} = [pi*(d/1000)**2/4|5] m^{2}. || Ideal velocity = \sqrt{2(9.81)([h])} = [sqrt(2*g*h)|2] m/s. || Q = [Cd|2] × [pi*(d/1000)**2/4|5] × [sqrt(2*g*h)|2] = [ans/1000|5] m^{3}/s = [ans|2] L/s.",
  "Cd*pi*(d/1000)**2/4*sqrt(2*g*h)*1000", dp=2, fig=lambda e: orifice(e['h'], e['d']), d=[50, 75, 40, 100], h=[3, 2, 5, 1.5], Cd=[0.60, 0.62, 0.60, 0.61])
F('fluids-0007', "Water flows at [v] m/s in a [d] mm diameter pipe. Its kinematic viscosity is [nu|1] × 10^{-6} m^{2}/s. What is the Reynolds number?",
  "The Reynolds number is the ratio of inertial to viscous forces: Re = V D / (kinematic viscosity). In pipes, flow is laminar below about 2,100 and turbulent above about 4,000, which decides how the friction factor is found.",
  r"Re = \frac{V D}{kinematic viscosity} = \frac{[v]([d/1000|3])}{[nu|1] × 10^{-6}} = [ans|0], which is turbulent.",
  "v*d/1000/(nu*1e-6)", wrong=["v*d/1000/(nu*1e-6)/100", "v*d/1000/(nu*1e-6)/10", "v*d/1000/(nu*1e-6)*10"], dp=0, v=[1.5, 2, 0.8, 3], d=[100, 150, 250, 50], nu=[1.0, 1.0, 1.0, 1.2])
F('fluids-0008', "A liquid has a dynamic viscosity of [mu] Pa·s and a density of [rho] kg/m^{3}. What is its kinematic viscosity? Give the answer in units of 10^{-6} m^{2}/s.",
  "Kinematic viscosity is dynamic viscosity divided by density. It is the form that appears in the Reynolds number.",
  r"Kinematic viscosity = \frac{[mu]}{[rho]} = [ans|2] × 10^{-6} m^{2}/s.",
  "mu/rho*1e6", dp=2, mu=[0.0012, 0.003, 0.0009, 0.02], rho=[800, 1200, 900, 880])
F('fluids-0009', "A mercury manometer (specific gravity 13.6) connects two water pipes at the same elevation and shows a deflection of [h|2] m. What is the pressure difference between the pipes? Use 9.81 kN/m^{3} for water.",
  "Work around the manometer from one pipe to the other, adding pressure going down and subtracting going up. The water columns on the two sides cancel except over the deflection, leaving (SG of mercury - 1) × specific weight of water × deflection.",
  "Pressure difference = (13.6 - 1)(9.81)([h|2]) = 12.6 × 9.81 × [h|2] = [ans|2] kPa.",
  "(13.6-1)*9.81*h", wrong=["9.81*h", "(13.6-1)*h", "13.6*9.81*h"], dp=3, fig=lambda e: manometer(e['h']), h=[0.20, 0.15, 0.30, 0.08])
F('fluids-0010', "A [Vb] m^{3} block with a specific gravity of [SG|2] floats in water. What volume of the block is below the water surface?",
  "Archimedes' principle: a floating body displaces a weight of fluid equal to its own weight. In water, the submerged fraction of the volume equals the body's specific gravity.",
  "Weight of block = weight of displaced water, so submerged volume = SG × total volume = [SG|2] × [Vb] = [ans|3] m^{3}.",
  "SG*Vb", dp=3, Vb=[0.5, 2, 0.8, 1.2], SG=[0.60, 0.45, 0.75, 0.90])
F('fluids-0011', "Water flows in a horizontal pipe. At section 1 the velocity is [u1] m/s and the pressure is [p1] kPa. At section 2 the pipe is narrower and the velocity is [u2] m/s. Ignoring losses, what is the pressure at section 2?",
  "Bernoulli's equation says pressure head + velocity head + elevation head stays constant along a streamline when there are no losses. In a horizontal pipe, a gain in velocity is paid for by a drop in pressure.",
  r"p_{2} = p_{1} - \frac{density}{2}(V_{2}^{2} - V_{1}^{2}) = [p1] - \frac{1,000}{2}([u2]^{2} - [u1]^{2}) Pa = [p1] - [0.5*(u2*u2-u1*u1)|2] = [ans|1] kPa.",
  "p1-0.5*(u2*u2-u1*u1)", wrong=["p1-(u2*u2-u1*u1)", "p1", "p1+0.5*(u2*u2-u1*u1)"], u1=[2, 1.5, 3, 2], u2=[8, 6, 9, 10], p1=[200, 150, 300, 250])
F('fluids-0012', "A [d] mm diameter water jet moving at [v] m/s strikes a flat plate at right angles. What force does the jet exert on the plate?",
  "The impulse-momentum principle: force equals the rate of change of momentum. The plate destroys all of the jet's momentum in the original direction, so F = (density)(Q)(V) = (density)(A)(V^{2}).",
  r"A = \frac{π([d/1000|3])^{2}}{4} = [pi*(d/1000)**2/4|5] m^{2}. || F = (density) A V^{2} = 1,000([pi*(d/1000)**2/4|5])([v])^{2} = [ans|0] N.",
  "1000*pi*(d/1000)**2/4*v*v", dp=0, d=[50, 75, 40, 60], v=[20, 12, 25, 15])
F('fluids-0013', "Water flows at [v] m/s through [L] m of [d] mm diameter pipe with a friction factor of [f]. What is the head loss? Use g = 9.81 m/s^{2}.",
  "The Darcy-Weisbach equation gives friction head loss as the friction factor times the length-to-diameter ratio times the velocity head: h_{f} = f (L/D)(V^{2}/2g).",
  r"Velocity head = \frac{[v]^{2}}{2(9.81)} = [v*v/(2*g)|3] m. || h_{f} = [f] × \frac{[L]}{[d/1000|3]} × [v*v/(2*g)|3] = [ans|2] m.",
  "f*L/(d/1000)*v*v/(2*g)", wrong=["v*v/(2*g)", "f*L/(d/1000)*v*v/(2*g)/2", "f*L/(d/1000)*v*v/(2*g)*2"], dp=3, v=[2, 1.5, 3, 2.5], L=[100, 250, 60, 400], d=[200, 300, 150, 500], f=[0.02, 0.018, 0.025, 0.015])

# ---------------- Surveying ----------------
F('surveying-0001', "A level is set up between a benchmark at elevation [BM|2] m and a new point. The backsight reading on the benchmark is [bs|2] m and the foresight reading on the new point is [fs|2] m. What is the elevation of the new point?",
  "Differential leveling: the height of instrument is the benchmark elevation plus the backsight. The elevation of the new point is the height of instrument minus the foresight. A larger foresight means lower ground.",
  "Height of instrument = [BM|2] + [bs|2] = [BM+bs|2] m. || Elevation = [BM+bs|2] - [fs|2] = [ans|2] m.",
  "BM+bs-fs", wrong=["BM-bs-fs", "BM-bs+fs", "BM+bs+fs"], dp=2, fig=lambda e: level(e['bs'], e['fs']), BM=[100.00, 52.40, 31.25, 18.60], bs=[1.52, 2.84, 0.95, 3.10], fs=[2.31, 1.16, 2.67, 0.88])
F('surveying-0002', "A four-sided parcel has corners, in order, at (0, 0), ([bx], 0), ([cx], [cy]) and ([dx], [dy]), with coordinates in metres. What is its area?",
  "The area of a closed polygon from corner coordinates is half the absolute value of the sum of the cross products x_{i} y_{i+1} - x_{i+1} y_{i} taken around the boundary (the coordinate or shoelace method).",
  r"Cross products in order: 0(0) - [bx](0) = 0; [bx]([cy]) - [cx](0) = [bx*cy]; [cx]([dy]) - [dx]([cy]) = [cx*dy-dx*cy]; [dx](0) - 0([dy]) = 0. || Sum = [bx*cy+cx*dy-dx*cy]. || Area = \frac{[bx*cy+cx*dy-dx*cy]}{2} = [ans|0] m^{2}.",
  "abs(bx*cy+cx*dy-dx*cy)/2", dp=0, fig=lambda e: parcel([(0, 0), (e['bx'], 0), (e['cx'], e['cy']), (e['dx'], e['dy'])]), bx=[60, 50, 80, 40], cx=[80, 70, 90, 60], cy=[40, 30, 50, 40], dx=[20, 10, 30, 10], dy=[50, 40, 70, 60])
F('surveying-0003', "Two road cross-sections [L] m apart have cut areas of [A1] m^{2} and [A2] m^{2}. Using the average end area method, what is the volume of cut between them?",
  "The average end area method treats the earthwork between two cross-sections as a prism whose cross-section is the mean of the two end areas: V = L (A_{1} + A_{2}) / 2. It slightly overestimates when the areas differ a lot.",
  r"V = L × \frac{A_{1} + A_{2}}{2} = [L] × \frac{[A1] + [A2]}{2} = [L] × [(A1+A2)/2] = [ans|0] m^{3}.",
  "L*(A1+A2)/2", wrong=["L*A1", "L*A2", "L*(A1+A2)"], dp=0, L=[20, 25, 30, 15], A1=[24, 18, 40, 32], A2=[36, 30, 52, 20])
F('surveying-0005', "A road rises from elevation [e1|1] m to elevation [e2|1] m over a horizontal distance of [d] m. What is the grade?",
  "Grade is rise over horizontal run, expressed as a percentage. It is positive going uphill in the direction of stationing.",
  r"Rise = [e2|1] - [e1|1] = [e2-e1|1] m. || Grade = \frac{[e2-e1|1]}{[d]} × 100 = [ans|2]%.",
  "(e2-e1)/d*100", dp=2, e1=[102.4, 215.0, 88.6, 340.2], e2=[108.9, 221.3, 97.6, 343.8], d=[260, 420, 300, 450])
F('surveying-0006', "A slope distance of [S|2] m is measured at a vertical angle of [va]° above horizontal. What is the horizontal distance?",
  "A slope measurement is the hypotenuse of a right triangle. The horizontal distance is the slope distance times the cosine of the vertical angle, and the elevation difference is the slope distance times the sine.",
  "H = S cos(angle) = [S|2] × cos [va]° = [S|2] × [cos(rad(va))|4] = [ans|2] m. The rise is [S|2] × sin [va]° = [S*sin(rad(va))|2] m.",
  "S*cos(rad(va))", wrong=["S*sin(rad(va))", "S", "S/cos(rad(va))"], dp=2, S=[250, 180, 320.5, 145], va=[12, 14, 15, 20])
F('surveying-0007', "What should the interior angles of a closed [name]-sided traverse add up to?",
  "The interior angles of any closed polygon with n sides sum to (n - 2) × 180°. Comparing the measured sum with this value gives the angular misclosure of a traverse.",
  "Sum = (n - 2) × 180° = ([n] - 2) × 180° = [ans]°.",
  "(n-2)*180", wrong=["(n-3)*180", "(n-1)*180", "n*180"], n=[5, 6, 8, 4], name=['five', 'six', 'eight', 'four'])
F('surveying-0008', "Two sides of a triangular parcel are [sa] m and [sb] m long and meet at an angle of [C]°. What is the area of the parcel?",
  "When two sides and the included angle are known, area = (1/2) a b sin(C). The term b sin(C) is the height of the triangle measured from side a.",
  r"Area = \frac{1}{2} a b sin C = \frac{1}{2}([sa])([sb]) sin [C]° = [0.5*sa*sb] × [sin(rad(C))|4] = [ans|1] m^{2}.",
  "0.5*sa*sb*sin(rad(C))", dp=1, fig=lambda e: triangle(e['sa'], e['sb'], e['C']), sa=[80, 120, 65, 90], sb=[60, 75, 40, 110], C=[30, 50, 72, 38])
F('surveying-0009', "A borrow pit measures [pa] m by [pb] m in plan. Its average depth of cut is [dc] m. What volume is excavated?",
  "Borrow pit volume is plan area times average depth of cut. On a grid, the average depth is found by weighting each corner depth by the number of grid squares it touches.",
  "V = [pa] × [pb] × [dc] = [pa*pb] m^{2} × [dc] m = [ans|0] m^{3}.",
  "pa*pb*dc", wrong=["pa*pb", "pa*pb*dc/2", "2*pa*pb*dc"], dp=0, pa=[20, 25, 40, 15], pb=[30, 40, 50, 22], dc=[2.5, 1.8, 3.2, 4.0])
F('surveying-0010', "A traverse line is [L|2] m long with an azimuth of [az]°. What is its departure (east-west component)?",
  "Azimuth is measured clockwise from north. Latitude (the north-south component) is L cos(azimuth) and departure (the east-west component) is L sin(azimuth). East and north are positive.",
  "Departure = L sin(azimuth) = [L|2] × sin [az]° = [ans|1] m (east). || Latitude = [L|2] × cos [az]° = [L*cos(rad(az))|1] m (north).",
  "L*sin(rad(az))", wrong=["L*cos(rad(az))", "L", "2*L*sin(rad(az))"], dp=1, fig=lambda e: azimuth(e['az'], e['L']), L=[200, 150, 320, 85.5], az=[60, 35, 72, 25])
F('surveying-0011', "Point A has a northing of [N0|2] m and an easting of 500.00 m. Point B is [L|2] m from A on a bearing of S [br]° E. What is the northing of B?",
  "A bearing of S (angle) E points south and east, so the line's latitude is negative and its departure is positive. The new northing is the old northing plus the latitude, where latitude = -L cos(bearing angle).",
  "Latitude = -[L|2] × cos [br]° = -[L*cos(rad(br))|2] m. || Northing of B = [N0|2] - [L*cos(rad(br))|2] = [ans|2] m. || For reference, easting of B = 500.00 + [L|2] sin [br]° = [500+L*sin(rad(br))|2] m.",
  "N0-L*cos(rad(br))", dp=2, N0=[1000, 2500, 800, 1500], L=[100, 250, 60, 180], br=[30, 40, 55, 20])
if __name__ == '__main__': save()
