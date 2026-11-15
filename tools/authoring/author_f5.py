"""Further question types: structural, geotechnical and materials. See author_fx.py for the format."""
from author_fx import *
CE, MM, MS = 'Civil Engineering', 'Mechanics of Materials', 'Materials Science/Structure of Matter'
# ================= Structural =================
NQ('structural-a', 'Statics::moments; couple', 'kN', 2, 15, "A simply supported beam spans [L] m. A clockwise couple of [M0] kN·m is applied to it at midspan and there are no other loads. What is the magnitude of each support reaction?",
   "A couple has no net force, so the two reactions must form an equal and opposite couple: one up, one down, each equal to the applied moment divided by the span. Where the couple is applied does not change the reactions.",
   r"R = \frac{M_{0}}{L} = \frac{[M0]}{[L]} = [ans|2] kN, upward at one support and downward at the other.",
   "M0/L", wrong=["M0/(2*L)", "2*M0/L", "1.5*M0/L"], M0=[120, 75, 250], L=[8, 6, 10])
NQ('structural-a', 'shear and moment diagrams', 'kN·m', 2, 27.71, "A simply supported beam spans [L|1] m and carries a triangular load that is zero at one end and [w0] kN/m at the other. What is the maximum bending moment?",
   "For a triangular load on a simple span the shear is zero, and the moment greatest, at L / square root of 3 from the zero-load end (0.577 L), not at midspan. The maximum moment is w_{0} L^{2} / (9 × square root of 3), or 0.0642 w_{0} L^{2}.",
   r"M_{max} = \frac{w_{0} L^{2}}{9\sqrt{3}} = \frac{[w0]([L|1])^{2}}{15.59} = [ans|2] kN·m, at [L/sqrt(3)|2] m from the zero-load end.",
   "w0*L*L/(9*sqrt(3))", w0=[12, 20, 8], L=[6, 4.5, 9])
NQ('structural-b', MM + '::deflection of beams', 'mm', 2, 2.53, "A cantilever [L|1] m long carries a uniform load of [w] kN/m over its whole length. Its flexural rigidity EI is [EI] kN·m^{2}. What is the deflection at the free end?",
   "For a cantilever under uniform load the tip deflection is w L^{4} / (8 EI). The same load on a simple span of the same length would deflect about one tenth as much.",
   r"Deflection = \frac{[w]([L|1])^{4}}{8([EI])} = [w*L**4/(8*EI)|6] m = [ans|2] mm.",
   "w*L**4/(8*EI)*1000", w=[5, 12, 2], L=[3, 2, 4.5], EI=[20000, 15000, 45000])
NQ('structural-b', MM + '::deflection of beams', '× 10^{6} mm^{4}', 1, 50.6, "A simply supported steel beam (E = 200 GPa) spans [L] m and carries a uniform service load of [w] kN/m. Deflection is limited to span/360. What moment of inertia is required?",
   "Set the midspan deflection, 5 w L^{4} / (384 E I), equal to the limit L / 360 and solve for I. Work in N and mm so that E in MPa is consistent.",
   r"I = \frac{5(360) w L^{3}}{384 E} = \frac{5(360)([w])([L*1000|0])^{3}}{384(200,000)} = [ans|1] × 10^{6} mm^{4}.",
   "5*360*w*(L*1000)**3/(384*200000)/1e6", w=[10, 15, 6], L=[6, 8, 5])
NQ('structural-c', MM + "::Euler's formula", 'MPa', 1, 137.1, "A column has a slenderness ratio (effective length over radius of gyration) of [sl] and a modulus of elasticity of [E] GPa. What is its Euler critical stress?",
   "Dividing the Euler load by the area gives a critical stress of π^{2} E / (KL/r)^{2}. It depends only on stiffness and slenderness, not on the material's strength, and it applies only while it is below the proportional limit.",
   r"Critical stress = \frac{π^{2}([E*1000|0])}{[sl]^{2}} = [ans|1] MPa.",
   "pi**2*E*1000/sl**2", E=[200, 200, 70], sl=[120, 150, 90])
NQ('structural-c', MM + "::Euler's formula", 'kN', 0, 2527, "A steel column (E = 200 GPa) [L] m long is [ends], so its effective length factor is [K|1]. Its least moment of inertia is [I|1] × 10^{6} mm^{4}. What is its Euler buckling load?",
   "End restraint changes the length of the buckled half-wave. The effective length K L replaces L in Euler's formula, so the load varies with 1 / K^{2}: fixing both ends quadruples it, and a flagpole column has one quarter of it.",
   r"P_{cr} = \frac{π^{2} E I}{(K L)^{2}} = \frac{π^{2}(200,000)([I|1] × 10^{6})}{([K|1] × [L*1000|0])^{2}} = [pi**2*200000*I*1e6/(K*L*1000)**2|0] N = [ans|0] kN.",
   "pi**2*200000*I*1e6/(K*L*1000)**2/1000", L=[5, 6, 4], K=[0.5, 0.7, 2.0], I=[8, 20, 3.5], ends=['fixed at both ends', 'fixed at one end and pinned at the other', 'fixed at the base and free at the top'])
NQ('structural-d', '-', '', 0, 3, "A rigid plane frame has [m] members, [j] joints and [r] support reaction components, with no internal hinges. What is its degree of static indeterminacy?",
   "For a rigid plane frame each member carries three unknown internal forces and each joint supplies three equilibrium equations: degree = 3m + r - 3j. Zero means determinate; a positive value is the number of extra unknowns.",
   "Degree = 3([m]) + [r] - 3([j]) = [3*m+r] - [3*j] = [ans|0].",
   "3*m+r-3*j", wrong=["3*m+r-2*j", "r", "3*m+r-3*j+1"], m=[3, 3, 5], r=[6, 4, 9], j=[4, 4, 6])
NQ('structural-d', '-', '', 0, 2, "A continuous beam under vertical and horizontal loads has [r] support reaction components and [hw]. What is its degree of static indeterminacy?",
   "A beam has three equilibrium equations, and each internal hinge adds one more because the moment there is zero. Degree = reactions - 3 - hinges.",
   "Degree = [r] - 3 - [hg] = [ans|0].",
   "r-3-hg", wrong=["r-2-hg", "r-hg", "r-3+hg"], r=[6, 6, 8], hg=[1, 2, 1], hw=['one internal hinge', 'two internal hinges', 'one internal hinge'])
NQ('structural-e', '-', 'kN·m', 2, 54, "A beam [L|1] m long is fixed at one end and simply supported at the other. It carries a uniform load of [w] kN/m. What is the magnitude of the moment at the fixed end?",
   "A propped cantilever under uniform load has a fixed-end moment of w L^{2} / 8, the same number as the midspan moment of a simple span, but negative (tension on top) and at the support.",
   r"M = \frac{w L^{2}}{8} = \frac{[w]([L|1])^{2}}{8} = [ans|2] kN·m.",
   "w*L*L/8", w=[12, 20, 8], L=[6, 4, 7.5])
NQ('structural-e', '-', '', 3, 0.6, "Two members with the same EI are rigidly joined at a joint and both are fixed at their far ends. Their lengths are [L1] m and [L2] m. In moment distribution, what distribution factor does the [L1] m member have at the joint?",
   "An unbalanced moment at a joint is shared among the members in proportion to their stiffness, 4EI / L for a member fixed at its far end. Stiffer, shorter members take more.",
   r"Stiffnesses are proportional to \frac{1}{[L1]} = [1/L1|4] and \frac{1}{[L2]} = [1/L2|4]. || DF = \frac{[1/L1|4]}{[1/L1|4] + [1/L2|4]} = [ans|3].",
   "(1/L1)/(1/L1+1/L2)", L1=[4, 5, 3], L2=[6, 8, 9])
NQ('structural-e', MM + '::uniaxial loading and deformation', 'kN', 1, 262.3, "A short composite column has a steel core of [As] mm^{2} (E = 200 GPa) cast in [Ac] mm^{2} of concrete (E = 25 GPa). A rigid cap applies [P] kN. How much of the load does the steel carry?",
   "Under a rigid cap both materials shorten equally, so each carries load in proportion to its axial stiffness, A E. This is the simplest statically indeterminate problem: equilibrium plus compatibility.",
   r"A E: steel [As*200|0] kN, concrete [Ac*25|0] kN. || P_{steel} = [P] × \frac{[As*200|0]}{[As*200|0] + [Ac*25|0]} = [ans|1] kN.",
   "P*As*200/(As*200+Ac*25)", P=[1000, 2500, 600], As=[4000, 8000, 2000], Ac=[90000, 160000, 60000])
NQ('structural-f', '-', 'kN', 1, 864, "An interior column supports [n] floors. Each floor carries a total factored load of [q|1] kPa and the column grid is [a|1] m by [b] m. What factored axial load reaches the base of the column?",
   "An interior column's tributary area extends half-way to each neighbouring column, which is one full bay. Load per floor is the area load times that area, and the floors add down the column.",
   "Tributary area = [a|1] × [b] = [a*b|1] m^{2}. || Load = [n] × [q|1] × [a*b|1] = [ans|1] kN.",
   "n*q*a*b", n=[3, 5, 2], q=[6, 7.5, 4.8], a=[6, 7.5, 5], b=[8, 9, 6])
NQ('structural-f', 'load combinations', 'kN', 1, 121, "A member carries a dead load of [D] kN, a live load of [Lv] kN and a snow load of [Sn] kN. Among the LRFD combinations 1.4D, 1.2D + 1.6L + 0.5S and 1.2D + 1.6S + L, what factored load governs?",
   "LRFD checks several combinations, each taking one variable load at its full factor with the others reduced, because the extremes are unlikely to coincide. The largest result governs design.",
   "1.4D = [1.4*D|1] kN. || 1.2D + 1.6L + 0.5S = [1.2*D+1.6*Lv+0.5*Sn|1] kN. || 1.2D + 1.6S + L = [1.2*D+1.6*Sn+Lv|1] kN. || The largest is [ans|1] kN.",
   "max(1.4*D, 1.2*D+1.6*Lv+0.5*Sn, 1.2*D+1.6*Sn+Lv)", D=[40, 60, 25], Lv=[25, 80, 10], Sn=[30, 10, 5])
NQ('structural-f', 'influence lines', 'kN·m', 2, 240, "A single concentrated load of [P] kN can be anywhere on a simply supported span of [L|1] m. What is the largest bending moment it can cause?",
   "The influence line for moment at a section of a simple span is a triangle, tallest when the section is at midspan. One moving load therefore does most when it sits at midspan: M = P L / 4.",
   r"M_{max} = \frac{P L}{4} = \frac{[P]([L|1])}{4} = [ans|2] kN·m.",
   "P*L/4", wrong=["P*L/8", "P*L/2", "P*L/3"], P=[80, 145, 50], L=[12, 20, 7.5])
NQ('structural-g', 'bolt', 'kips', 1, 71.6, "A connection has [n] bolts of [db|3] in diameter in single shear. The nominal shear strength of the bolt material is [Fnv] ksi. With a resistance factor of 0.75, what is the design shear strength of the bolt group?",
   "Each bolt's nominal shear strength is its nominal shear stress times its gross cross-sectional area, per shear plane. Design strength multiplies by 0.75 and by the number of bolts.",
   r"A_{b} = \frac{π([db|3])^{2}}{4} = [pi*db*db/4|4] in^{2}. || Design strength = 0.75([Fnv])([pi*db*db/4|4])([n]) = [ans|1] kips.",
   "0.75*Fnv*pi*db*db/4*n", units='USCS', n=[4, 6, 3], db=[0.75, 0.875, 1.0], Fnv=[54, 54, 68])
NQ('structural-g', 'weld', 'kips', 1, 44.5, "A fillet weld with a leg size of [w|4] in is [L] in long and made with E70 electrodes (70 ksi). Using 0.75 × 0.60 F_{EXX} on the effective throat, what is its design strength?",
   "A fillet weld fails in shear through its throat, which is 0.707 times the leg size for equal legs. Design strength is 0.75 × 0.60 × electrode strength × throat × length.",
   "Throat = 0.707([w|4]) = [0.707*w|4] in. || Design strength = 0.75(0.60)(70)([0.707*w|4])([L]) = [ans|1] kips.",
   "0.75*0.6*70*0.707*w*L", units='USCS', w=[0.25, 0.3125, 0.375], L=[8, 12, 6])
NQ('structural-g', 'plastic', '× 10^{3} mm^{3}', 0, 966, "A compact, laterally braced steel beam with F_{y} = [Fy] MPa must resist a factored moment of [Mu] kN·m. With a resistance factor of 0.90, what plastic section modulus is required?",
   "A compact, fully braced beam can reach its plastic moment, F_{y} Z. Design strength is 0.90 F_{y} Z, so the required Z is the factored moment divided by 0.90 F_{y}.",
   r"Z = \frac{[Mu] × 10^{6}}{0.90([Fy])} = [Mu*1e6/(0.9*Fy)|0] mm^{3} = [ans|0] × 10^{3} mm^{3}.",
   "Mu*1e6/(0.9*Fy)/1000", Mu=[300, 520, 150], Fy=[345, 345, 250])
NQ('structural-g', 'shear', 'kN', 1, 828, "A rolled steel beam is [d] mm deep with a web [tw|1] mm thick, and F_{y} = [Fy] MPa. Taking the nominal shear strength as 0.6 F_{y} A_{w} with a resistance factor of 1.0, what is its design shear strength?",
   "Shear in a rolled beam is carried by the web. The web area is the full depth times the web thickness, and shear yielding occurs at about 0.6 F_{y}.",
   "A_{w} = [d] × [tw|1] = [d*tw|0] mm^{2}. || Design strength = 1.0(0.6)([Fy])([d*tw|0]) = [0.6*Fy*d*tw|0] N = [ans|1] kN.",
   "0.6*Fy*d*tw/1000", d=[400, 530, 310], tw=[10, 11, 6.5], Fy=[345, 345, 250])
NQ('structural-h', 'ACI 318', '', 4, 0.0115, "A singly reinforced beam is [b] mm wide with an effective depth of [d] mm and [As] mm^{2} of steel (f_{y} = 420 MPa). The concrete strength is [fc] MPa, for which the stress block factor is [b1|2]. What is the strain in the tension steel when the concrete reaches 0.003?",
   "Find the stress block depth a from force equilibrium, then the neutral axis depth c = a / (stress block factor). Strains vary linearly from 0.003 at the compression face, so the steel strain is 0.003 (d - c) / c. A value of 0.005 or more means the section is tension-controlled.",
   r"a = \frac{[As](420)}{0.85([fc])([b])} = [As*420/(0.85*fc*b)|2] mm, so c = \frac{[As*420/(0.85*fc*b)|2]}{[b1|2]} = [As*420/(0.85*fc*b)/b1|2] mm. || Steel strain = 0.003 × \frac{[d] - [As*420/(0.85*fc*b)/b1|2]}{[As*420/(0.85*fc*b)/b1|2]} = [ans|4].",
   "0.003*(d-As*420/(0.85*fc*b)/b1)/(As*420/(0.85*fc*b)/b1)", As=[1500, 2400, 1000], b=[300, 350, 250], d=[500, 600, 400], fc=[28, 35, 21], b1=[0.85, 0.80, 0.85])
NQ('structural-h', '-', 'kN·m', 1, 41.0, "A rectangular concrete beam is [b] mm wide and [h] mm deep overall, with f'_{c} = [fc] MPa. Using a modulus of rupture of 0.62 × the square root of f'_{c} (MPa) and the gross section, what is the cracking moment?",
   "Concrete cracks when the extreme tension stress reaches the modulus of rupture. Until then the gross section resists bending, so the cracking moment is f_{r} I_{g} / y_{t}.",
   r"f_{r} = 0.62\sqrt{[fc]} = [0.62*sqrt(fc)|3] MPa. I_{g} = \frac{[b]([h])^{3}}{12} = [b*h**3/12/1e9|4] × 10^{9} mm^{4}, y_{t} = [h/2|0] mm. || M_{cr} = \frac{[0.62*sqrt(fc)|3]([b*h**3/12/1e9|4] × 10^{9})}{[h/2|0]} = [ans|1] kN·m.",
   "0.62*sqrt(fc)*b*h**3/12/(h/2)/1e6", fc=[28, 35, 21], b=[300, 400, 250], h=[500, 700, 450])
NQ('structural-h', 'stirrup', 'mm', 1, 248.5, "Stirrups with a total leg area of [Av] mm^{2} and f_{y} = 420 MPa must provide a shear strength V_{s} of [Vs] kN in a beam with an effective depth of [d] mm. What stirrup spacing is required?",
   "Rearranging V_{s} = A_{v} f_{y} d / s gives the spacing. Closer stirrups carry more shear; the code also caps the spacing, typically at d / 2.",
   r"s = \frac{A_{v} f_{y} d}{V_{s}} = \frac{[Av](420)([d])}{[Vs*1000|0]} = [ans|1] mm.",
   "Av*420*d/(Vs*1000)", Av=[142, 142, 200], d=[500, 450, 600], Vs=[120, 200, 150])
# ================= Geotechnical =================
NQ('geotech-a', '-', '', 3, 0.385, "A clay has a natural water content of [w]%, a liquid limit of [LL] and a plastic limit of [PL]. What is its liquidity index?",
   "The liquidity index places the natural water content between the plastic limit (index 0) and the liquid limit (index 1). Values near 1 indicate a soft, sensitive soil; values near 0 or below indicate a stiff one.",
   r"LI = \frac{w - PL}{LL - PL} = \frac{[w] - [PL]}{[LL] - [PL]} = [ans|3].",
   "(w-PL)/(LL-PL)", w=[32, 45, 18], LL=[48, 60, 35], PL=[22, 25, 15])
NQ('geotech-a', 'group index', '', 0, 10, "A soil has [F]% passing the No. 200 sieve, a liquid limit of [LL] and a plasticity index of [PI]. Using GI = (F - 35)(0.2 + 0.005(LL - 40)) + 0.01(F - 15)(PI - 10), what is its AASHTO group index, rounded to the nearest whole number?",
   "The AASHTO group index rates a subgrade soil within its group: the higher the number, the poorer the soil as a pavement subgrade. It is reported as a whole number in parentheses after the group symbol.",
   "GI = ([F] - 35)(0.2 + 0.005([LL] - 40)) + 0.01([F] - 15)([PI] - 10) = [(F-35)*(0.2+0.005*(LL-40))|2] + [0.01*(F-15)*(PI-10)|2] = [(F-35)*(0.2+0.005*(LL-40))+0.01*(F-15)*(PI-10)|2], reported as [ans|0].",
   "int((F-35)*(0.2+0.005*(LL-40))+0.01*(F-15)*(PI-10)+0.5)", F=[60, 75, 48], LL=[45, 58, 38], PI=[20, 30, 14])
NQ('geotech-b', 'phase relationships', '%', 1, 74.8, "A soil has a water content of [w]%, a specific gravity of solids of [Gs|2] and a void ratio of [vr|2]. What is its degree of saturation?",
   "The phase relationships link four quantities: S e = w G_{s}. The degree of saturation is the share of the void space that is filled with water.",
   r"S = \frac{w G_{s}}{e} = \frac{[w/100|2]([Gs|2])}{[vr|2]} × 100 = [ans|1]%.",
   "w*Gs/vr", w=[18, 25, 12], Gs=[2.70, 2.65, 2.72], vr=[0.65, 0.80, 0.55])
NQ('geotech-b', 'phase relationships', '', 3, 0.394, "A soil has a void ratio of [vr|2]. What is its porosity?",
   "Void ratio compares the volume of voids with the volume of solids; porosity compares it with the total volume. They are linked by n = e / (1 + e), so porosity is always less than 1.",
   r"n = \frac{[vr|2]}{1 + [vr|2]} = [ans|3].",
   "vr/(1+vr)", wrong=["1/(1+vr)", "vr/(1-vr)", "vr/(1+vr)**2"], vr=[0.65, 0.90, 0.45])
NQ('geotech-b', 'phase relationships', 'kN/m^{3}', 2, 19.62, "A fully saturated soil has a specific gravity of solids of [Gs|2] and a void ratio of [vr|2]. What is its saturated unit weight? Use 9.81 kN/m^{3} for water.",
   "Take a volume of solids of 1: the solids weigh G_{s} times the unit weight of water, the water filling the voids weighs e times it, and the total volume is 1 + e.",
   r"Saturated unit weight = \frac{([Gs|2] + [vr|2])(9.81)}{1 + [vr|2]} = [ans|2] kN/m^{3}.",
   "(Gs+vr)*9.81/(1+vr)", Gs=[2.70, 2.65, 2.75], vr=[0.70, 0.55, 1.10])
NQ('geotech-c', 'coefficient of permeability', '× 10^{-4} cm/s', 3, 1.596, "In a falling-head test, a soil sample [L] cm long with a cross-section of [A] cm^{2} is fed from a standpipe of [a|1] cm^{2}. The head falls from [h1] cm to [h2] cm in [t] s. What is the coefficient of permeability?",
   "In a falling-head test the flow comes from a narrow standpipe, so the head drops as water passes: k = (a L / (A t)) ln(h_{1} / h_{2}). It suits fine soils, where a constant-head test would pass too little water to measure.",
   r"k = \frac{[a|1]([L])}{[A]([t])} ln(\frac{[h1]}{[h2]}) = [a*L/(A*t)*1e4|4] × 10^{-4} × [log(h1/h2)|4] = [ans|3] × 10^{-4} cm/s.",
   "a*L/(A*t)*log(h1/h2)*1e4", a=[1.0, 0.5, 2.0], A=[80, 50, 100], L=[15, 10, 12], t=[600, 900, 300], h1=[100, 80, 120], h2=[60, 50, 90])
NQ('geotech-c', '-', 'blows', 1, 22.5, "A standard penetration test records [N] blows per 300 mm with a hammer that delivers [ER]% of the theoretical free-fall energy. What is the blow count corrected to 60% energy, N_{60}?",
   "Different hammers deliver different fractions of the theoretical energy, so blow counts are normalised to a standard 60%. A more efficient hammer drives the sampler with fewer blows, and its count is scaled up.",
   r"N_{60} = N × \frac{ER}{60} = [N] × \frac{[ER]}{60} = [ans|1].",
   "N*ER/60", N=[18, 32, 9], ER=[75, 45, 80])
NQ('geotech-c', 'major principal stress', '°', 1, 32.3, "A direct shear test on dry sand fails at a shear stress of [ta] kPa under a normal stress of [sn] kPa. Taking cohesion as zero, what is the friction angle?",
   "For a cohesionless soil the failure envelope is a straight line through the origin, shear strength = normal stress × tan(friction angle). One test gives the angle directly.",
   r"Friction angle = tan^{-1}(\frac{[ta]}{[sn]}) = tan^{-1}([ta/sn|4]) = [ans|1]°.",
   "atan(ta/sn)*180/pi", sn=[150, 200, 80], ta=[95, 115, 58])
NQ('geotech-d', 'effective stress', 'kPa', 1, 58.1, "A saturated soil with a unit weight of [gs|1] kN/m^{3} lies beneath a lake. What is the vertical effective stress [z|1] m below the lake bed? Use 9.81 kN/m^{3} for water.",
   "Below standing water, the weight of the water above the bed adds equally to total stress and to pore pressure, so it cancels. Effective stress is the buoyant unit weight times the depth below the bed, whatever the depth of the lake.",
   "Effective stress = ([gs|1] - 9.81)([z|1]) = [gs-9.81|2] × [z|1] = [ans|1] kPa.",
   "(gs-9.81)*z", wrong=["gs*z", "gs*z-9.81", "(gs+9.81)*z"], gs=[19.5, 18.2, 20.4], z=[6, 10, 3.5])
NQ('geotech-d', '-', '', 3, 1.031, "A sand has a specific gravity of solids of [Gs|2] and a void ratio of [vr|2]. What upward hydraulic gradient would cause a quick (boiling) condition?",
   "Upward seepage reduces effective stress. When the seepage force equals the buoyant weight of the soil the effective stress is zero and the sand boils. That critical gradient is (G_{s} - 1) / (1 + e), usually close to 1.",
   r"i_{c} = \frac{[Gs|2] - 1}{1 + [vr|2]} = [ans|3].",
   "(Gs-1)/(1+vr)", Gs=[2.65, 2.70, 2.68], vr=[0.60, 0.85, 0.45])
NQ('geotech-d', '-', 'kPa', 2, 45, "A footing [B|1] m by [Lf|1] m carries a load of [Q] kN. Using the 2:1 method, what is the increase in vertical stress [z|1] m below the footing?",
   "The 2:1 method spreads the load outward at 2 vertical to 1 horizontal, so at depth z the loaded area has grown by z in each plan dimension. Stress increase is the load divided by that enlarged area.",
   r"Stress increase = \frac{[Q]}{([B|1] + [z|1])([Lf|1] + [z|1])} = \frac{[Q]}{[(B+z)*(Lf+z)|2]} = [ans|2] kPa.",
   "Q/((B+z)*(Lf+z))", Q=[900, 1500, 400], B=[2, 2.5, 1.5], Lf=[3, 2.5, 1.5], z=[2, 3, 1])
NQ('geotech-e', 'Rankine', 'kN/m', 2, 60.75, "The toe of a retaining wall is embedded [H|1] m in sand with a friction angle of [phi]° and a unit weight of [gam|1] kN/m^{3}. Using Rankine theory, what passive resistance is available per metre of wall?",
   "Passive pressure develops when a wall pushes into the soil. The coefficient is K_{p} = tan^{2}(45° + friction angle / 2), the reciprocal of the active coefficient, and the force is (1/2) K_{p} (unit weight) H^{2}.",
   r"K_{p} = tan^{2}(45° + \frac{[phi]°}{2}) = [tan(rad(45+phi/2))**2|3]. || P_{p} = \frac{1}{2}([tan(rad(45+phi/2))**2|3])([gam|1])([H|1])^{2} = [ans|2] kN/m.",
   "0.5*tan(rad(45+phi/2))**2*gam*H*H", phi=[30, 34, 28], gam=[18, 19, 17.5], H=[1.5, 2, 1.2])
NQ('geotech-e', '-', 'kPa', 2, 45, "A rigid basement wall that cannot move retains sand with a friction angle of [phi]° and a unit weight of [gam|1] kN/m^{3}. Using K_{0} = 1 - sin(friction angle), what is the horizontal earth pressure [z] m below the surface?",
   "A wall that cannot move does not let the soil relax to the active state, so it feels at-rest pressure, which is higher. For normally consolidated sand the at-rest coefficient is about 1 - sin(friction angle).",
   "K_{0} = 1 - sin [phi]° = [1-sin(rad(phi))|4]. || Pressure = [1-sin(rad(phi))|4] × [gam|1] × [z] = [ans|2] kPa.",
   "(1-sin(rad(phi)))*gam*z", phi=[30, 36, 25], gam=[18, 19.5, 17], z=[5, 4, 8])
NQ('geotech-e', 'Rankine', 'kN/m', 2, 20, "A uniform surcharge of [q] kPa, such as traffic, acts on the ground behind a [H|1] m retaining wall. The backfill has a friction angle of [phi]°. Using the Rankine active coefficient, what extra horizontal force does the surcharge put on each metre of wall?",
   "A uniform surcharge adds a constant horizontal pressure of K_{a} q over the full height of the wall. Its resultant, K_{a} q H, acts at mid-height, unlike the triangular soil pressure, which acts at one third.",
   r"K_{a} = tan^{2}(45° - \frac{[phi]°}{2}) = [tan(rad(45-phi/2))**2|4]. || Force = [tan(rad(45-phi/2))**2|4] × [q] × [H|1] = [ans|2] kN/m, acting [H/2|2] m above the base.",
   "tan(rad(45-phi/2))**2*q*H", phi=[30, 35, 26], q=[15, 20, 10], H=[4, 6, 3.5])
NQ('geotech-f', 'major principal stress', 'kPa', 1, 369.3, "A soil has a cohesion of [c] kPa and a friction angle of [phi]°. In a triaxial test with a cell pressure of [s3] kPa, what major principal stress causes failure?",
   "At failure Mohr's circle touches the Mohr-Coulomb envelope. That gives the major principal stress as the minor one times tan^{2}(45° + friction angle / 2), plus 2c tan(45° + friction angle / 2).",
   r"tan(45° + \frac{[phi]°}{2}) = [tan(rad(45+phi/2))|4]. || Major principal stress = [s3]([tan(rad(45+phi/2))|4])^{2} + 2([c])([tan(rad(45+phi/2))|4]) = [s3*tan(rad(45+phi/2))**2|1] + [2*c*tan(rad(45+phi/2))|1] = [ans|1] kPa.",
   "s3*tan(rad(45+phi/2))**2+2*c*tan(rad(45+phi/2))", s3=[100, 150, 60], phi=[30, 24, 35], c=[20, 35, 0])
NQ('geotech-g', 'ultimate bearing capacity', 'kPa', 1, 759.6, "A strip footing [B|1] m wide is founded [D|1] m deep in sand with a unit weight of [gam] kN/m^{3} and no cohesion. The bearing capacity factors are N_{q} = [Nq|1] and N_{γ} = [Ng|1]. What is the ultimate bearing capacity?",
   "The bearing capacity equation has three terms: cohesion, surcharge from the soil beside the footing, and the weight of soil below it. With no cohesion only the last two remain: (unit weight)(depth) N_{q} + (1/2)(unit weight) B N_{γ}.",
   r"q_{ult} = [gam]([D|1])([Nq|1]) + \frac{1}{2}([gam])([B|1])([Ng|1]) = [gam*D*Nq|1] + [0.5*gam*B*Ng|1] = [ans|1] kPa.",
   "gam*D*Nq+0.5*gam*B*Ng", gam=[18, 19, 17], D=[1, 1.5, 0.8], B=[2, 1.2, 3], Nq=[22.5, 41.4, 12.7], Ng=[19.7, 42.4, 9.7])
NQ('geotech-g', '-', 'kPa', 1, 210.5, "A strip footing [B|1] m wide carries [P] kN per metre and a moment of [M] kN·m per metre. Using the effective width B' = B - 2e, what uniform bearing pressure acts on the effective width?",
   "The effective-area method replaces an eccentrically loaded footing by a narrower one loaded centrally. The resultant sits at the centre of the reduced width B - 2e, and bearing capacity is checked on that width.",
   r"e = \frac{[M]}{[P]} = [M/P|3] m, so B' = [B|1] - 2([M/P|3]) = [B-2*M/P|3] m. || Pressure = \frac{[P]}{[B-2*M/P|3]} = [ans|1] kPa.",
   "P/(B-2*M/P)", B=[2.5, 3, 1.8], M=[120, 90, 40], P=[400, 600, 250])
NQ('geotech-h', '-', 'kN', 1, 659.7, "A round pile [d|1] m in diameter is driven [L] m into clay with an undrained shear strength of [cu] kPa. The adhesion factor is [al|1] and the tip capacity is 9 c_{u} on the tip area. What is the ultimate capacity?",
   "A pile in clay carries load by adhesion along its shaft, a fraction of the undrained strength acting on the shaft surface, and by end bearing of about nine times the undrained strength on the tip.",
   r"Shaft: [al|1]([cu]) × π([d|1])([L]) = [al*cu*pi*d*L|1] kN. || Tip: 9([cu]) × \frac{π([d|1])^{2}}{4} = [9*cu*pi*d*d/4|1] kN. || Total = [ans|1] kN.",
   "al*cu*pi*d*L+9*cu*pi*d*d/4", al=[0.8, 0.6, 1.0], cu=[50, 90, 25], d=[0.4, 0.5, 0.3], L=[12, 15, 10])
NQ('geotech-h', '-', 'm', 2, 6.8, "Two columns [s] m apart carry [P1] kN and [P2] kN and share one rectangular footing. The footing starts [a|1] m beyond the centre of the [P1] kN column. How long must it be for the soil pressure to be uniform?",
   "Soil pressure under a rigid footing is uniform only if the footing's centroid lies under the resultant of the column loads. Locate the resultant, then make the footing twice the distance from its end to the resultant.",
   r"Resultant from the first column = \frac{[P2]([s])}{[P1] + [P2]} = [P2*s/(P1+P2)|3] m. || Length = 2([a|1] + [P2*s/(P1+P2)|3]) = [ans|2] m.",
   "2*(a+P2*s/(P1+P2))", P1=[600, 800, 450], P2=[900, 1000, 750], s=[5, 6, 4], a=[0.4, 0.5, 0.3])
NQ('geotech-i', 'time factor', 'mm^{2}/min', 3, 4.925, "A consolidation test specimen [H] mm thick drains from both faces. It reaches 50% consolidation in [t50|1] min. With a time factor of 0.197 at 50%, what is the coefficient of consolidation?",
   "The time factor links time and drainage path: T_{v} = c_{v} t / H_{dr}^{2}. With drainage from both faces the drainage path is half the thickness.",
   r"H_{dr} = \frac{[H]}{2} = [H/2|2] mm. || c_{v} = \frac{0.197([H/2|2])^{2}}{[t50|1]} = [ans|3] mm^{2}/min.",
   "0.197*(H/2)**2/t50", H=[20, 25, 19], t50=[4, 6.5, 2.5])
NQ('geotech-i', 'compression index', 'mm', 1, 33.6, "An overconsolidated clay layer [H] m thick has a recompression index of [Cr|2] and an initial void ratio of [e0|2]. The effective stress at mid-layer rises from [s0] kPa to [sf] kPa, which is still below the preconsolidation pressure. What is the consolidation settlement?",
   "While the stress stays below the preconsolidation pressure the clay is being reloaded, so the flatter recompression index applies in place of the compression index: S = C_{r} H / (1 + e_{0}) × log(final / initial).",
   r"S = \frac{[Cr|2]([H])}{1 + [e0|2]} log(\frac{[sf]}{[s0]}) = [Cr*H/(1+e0)|5] × [log10(sf/s0)|4] = [Cr*H/(1+e0)*log10(sf/s0)|5] m = [ans|1] mm.",
   "Cr*H/(1+e0)*log10(sf/s0)*1000", Cr=[0.05, 0.04, 0.06], H=[5, 8, 3], e0=[0.9, 1.1, 0.75], s0=[100, 80, 150], sf=[180, 120, 240])
NQ('geotech-i', '-', '', 2, 2.67, "A clay [z] m below the surface has a preconsolidation pressure of [sp] kPa. The soil above has a unit weight of [gam|1] kN/m^{3} and the water table is deep. What is the overconsolidation ratio?",
   "The overconsolidation ratio is the largest effective stress the soil has ever carried divided by what it carries now. A ratio of 1 is normally consolidated; above 1 the soil has been unloaded and settles less under new load.",
   r"Present effective stress = [gam|1] × [z] = [gam*z|1] kPa. || OCR = \frac{[sp]}{[gam*z|1]} = [ans|2].",
   "sp/(gam*z)", sp=[240, 150, 400], gam=[18, 17, 19.5], z=[5, 6, 8])
NQ('geotech-j', 'slope failure', '', 2, 1.72, "A dry soil layer [H] m thick (measured vertically) lies on a planar interface sloping at [bt]°. The soil has a cohesion of [c] kPa, a friction angle of [phi]° and a unit weight of [gam] kN/m^{3}. For an infinite slope, what is the factor of safety against sliding on the interface?",
   "For an infinite slope with cohesion, FS = c / (unit weight × H × sin(slope) × cos(slope)) + tan(friction angle) / tan(slope). The cohesion term shrinks as the layer gets thicker; the friction term does not depend on thickness.",
   r"Cohesion term = \frac{[c]}{[gam]([H])(sin [bt]°)(cos [bt]°)} = [c/(gam*H*sin(rad(bt))*cos(rad(bt)))|3]. || Friction term = \frac{tan [phi]°}{tan [bt]°} = [tan(rad(phi))/tan(rad(bt))|3]. || FS = [ans|2].",
   "c/(gam*H*sin(rad(bt))*cos(rad(bt)))+tan(rad(phi))/tan(rad(bt))", c=[10, 5, 15], gam=[18, 19, 17], H=[3, 2, 5], bt=[25, 30, 20], phi=[30, 28, 22])
NQ('geotech-j', 'slope failure', '', 2, 1.19, "A long slope of cohesionless soil stands at [bt]° with seepage parallel to the slope and the water table at the surface. The saturated unit weight is [gs] kN/m^{3} and the friction angle is [phi]°. What is the factor of safety? Use 9.81 kN/m^{3} for water.",
   "Seepage parallel to the slope lowers the effective normal stress without lowering the driving weight. The dry-slope factor of safety, tan(friction angle) / tan(slope), is multiplied by the ratio of buoyant to saturated unit weight, roughly one half.",
   r"FS = \frac{[gs] - 9.81}{[gs]} × \frac{tan [phi]°}{tan [bt]°} = [(gs-9.81)/gs|4] × [tan(rad(phi))/tan(rad(bt))|4] = [ans|2].",
   "(gs-9.81)/gs*tan(rad(phi))/tan(rad(bt))", gs=[20, 19, 21], phi=[32, 35, 30], bt=[15, 18, 12])
NQ('geotech-k', '-', 'L', 1, 87.5, "Fill is to be compacted to a dry density of [rd] kg/m^{3}. The borrow soil arrives at a water content of [w1|1]% and the optimum is [w2|1]%. How much water must be added per cubic metre of compacted fill?",
   "Water content is the mass of water divided by the mass of dry solids. The water to add is the dry mass times the increase in water content, and 1 kg of water is 1 L.",
   r"Water = [rd] × \frac{[w2|1] - [w1|1]}{100} = [ans|1] kg, or [ans|1] L per cubic metre.",
   "rd*(w2-w1)/100", rd=[1750, 1680, 1900], w1=[8, 10.5, 4], w2=[13, 16, 9.5])
# ================= Materials =================
NQ('materials-a', '-', 'm^{3}', 3, 0.958, "A concrete batch contains [c] kg of cement (specific gravity 3.15), [w] kg of water, [s] kg of sand (2.65) and [gr] kg of coarse aggregate (2.70). Ignoring air, what volume of concrete does it make?",
   "The absolute volume method adds the solid volume of each ingredient: mass divided by (specific gravity × 1,000 kg/m^{3}). The bulk volumes of the piles do not add, because the fines fill the gaps between the coarse particles.",
   r"\frac{[c]}{3,150} + \frac{[w]}{1,000} + \frac{[s]}{2,650} + \frac{[gr]}{2,700} = [c/3150|4] + [w/1000|4] + [s/2650|4] + [gr/2700|4] = [ans|3] m^{3}.",
   "c/3150+w/1000+s/2650+gr/2700", c=[350, 400, 300], w=[175, 180, 165], s=[700, 650, 780], gr=[1100, 1050, 1150])
NQ('materials-a', '-', '%', 2, 4.08, "A compacted asphalt mix has a bulk specific gravity of [Gmb|2] and a theoretical maximum specific gravity of [Gmm|2]. What is its air void content?",
   "The theoretical maximum specific gravity is the mix with no air at all. Air voids are the shortfall of the compacted bulk specific gravity from it, as a percentage; about 4% is the usual design target.",
   r"Air voids = (1 - \frac{[Gmb|2]}{[Gmm|2]}) × 100 = [ans|2]%.",
   "(1-Gmb/Gmm)*100", Gmb=[2.35, 2.40, 2.28], Gmm=[2.45, 2.52, 2.42])
NQ('materials-a', '-', '%', 2, 15.75, "A compacted asphalt mix has a bulk specific gravity of [Gmb|2] and contains [Ps|1]% aggregate by mass of mix. The aggregate's bulk specific gravity is [Gsb|2]. What are the voids in the mineral aggregate (VMA)?",
   "VMA is the space between the aggregate particles in the compacted mix, which holds both the air voids and the effective asphalt. VMA = 100 - G_{mb} P_{s} / G_{sb}.",
   r"VMA = 100 - \frac{[Gmb|2]([Ps|1])}{[Gsb|2]} = 100 - [Gmb*Ps/Gsb|2] = [ans|2]%.",
   "100-Gmb*Ps/Gsb", Gmb=[2.35, 2.40, 2.30], Ps=[95, 94.5, 95.5], Gsb=[2.65, 2.70, 2.60])
NQ('materials-b', '-', 'MPa', 2, 2.83, "In a splitting tensile test, a concrete cylinder [D] mm in diameter and [L] mm long fails at a load of [P] kN applied along its length. What is its splitting tensile strength?",
   "Loading a cylinder along two opposite lines sets up nearly uniform tension across the loaded diameter. The splitting tensile strength is 2P / (π L D).",
   r"Strength = \frac{2([P*1000|0])}{π([L])([D])} = [ans|2] MPa.",
   "2*P*1000/(pi*L*D)", P=[200, 250, 160], L=[300, 300, 200], D=[150, 150, 100])
NQ('materials-b', '-', 'MPa', 2, 4.0, "A [b] mm square concrete beam is tested in third-point loading on a span of [L] mm and breaks in the middle third at a total load of [P|1] kN. What is its modulus of rupture?",
   "Third-point loading puts a constant moment of P L / 6 across the middle third. Dividing by the section modulus, b d^{2} / 6, gives the modulus of rupture R = P L / (b d^{2}).",
   r"R = \frac{[P*1000|0]([L])}{[b]([b])^{2}} = [ans|2] MPa.",
   "P*1000*L/b**3", P=[30, 36, 25], L=[450, 450, 600], b=[150, 150, 150])
NQ('materials-b', '-', '', 2, 2.9, "A sieve analysis of sand gives cumulative percentages retained on the six standard sieves from No. 4 to No. 100 of [c1], [c2], [c3], [c4], [c5] and [c6]. What is the fineness modulus?",
   "The fineness modulus is the sum of the cumulative percentages retained on the standard sieves, divided by 100. A larger value means a coarser sand; concrete sands usually fall between 2.3 and 3.1.",
   r"FM = \frac{[c1] + [c2] + [c3] + [c4] + [c5] + [c6]}{100} = \frac{[c1+c2+c3+c4+c5+c6]}{100} = [ans|2].",
   "(c1+c2+c3+c4+c5+c6)/100", c1=[4, 2, 6], c2=[15, 12, 20], c3=[35, 30, 42], c4=[58, 52, 65], c5=[82, 78, 86], c6=[96, 95, 98])
NQ('materials-b', '-', '%', 2, 1.52, "An aggregate sample has a mass of [ssd|1] g in the saturated surface-dry condition and [od|1] g after oven drying. What is its absorption?",
   "Absorption is the water an aggregate holds inside its pores when saturated surface-dry, as a percentage of its oven-dry mass.",
   r"Absorption = \frac{[ssd|1] - [od|1]}{[od|1]} × 100 = [ans|2]%.",
   "(ssd-od)/od*100", ssd=[502.5, 1012.0, 755.4], od=[495.0, 1000.0, 741.2])
NQ('materials-b', '-', '', 3, 2.667, "A coarse aggregate sample has a mass of [ssd] g saturated surface-dry in air and an apparent mass of [wsub] g when submerged in water. What is its bulk specific gravity (SSD)?",
   "By Archimedes' principle the loss of mass in water equals the mass of water displaced, which gives the sample's bulk volume. Specific gravity is the SSD mass divided by that loss.",
   r"Bulk specific gravity (SSD) = \frac{[ssd]}{[ssd] - [wsub]} = [ans|3].",
   "ssd/(ssd-wsub)", ssd=[1000, 2450, 1520], wsub=[625, 1540, 940])
NQ('materials-c', MS + '::reduction in area', '%', 2, 43.75, "A tension specimen has an original diameter of [d0|1] mm. After fracture the diameter at the neck is [df|1] mm. What is the percent reduction in area?",
   "Reduction in area measures ductility: the loss of cross-section at the fracture as a percentage of the original. Areas go with diameter squared.",
   r"Reduction = (1 - (\frac{[df|1]}{[d0|1]})^{2}) × 100 = [ans|2]%.",
   "(1-(df/d0)**2)*100", d0=[12.8, 10, 12.5], df=[9.6, 7.2, 10.5])
NQ('materials-c', '-', 'kJ/m^{3}', 1, 156.3, "A metal has a yield strength of [sy] MPa and a modulus of elasticity of [E] GPa. What is its modulus of resilience?",
   "The modulus of resilience is the energy per unit volume a material can absorb without permanent deformation: the area under the straight part of the stress-strain curve, (yield strength)^{2} / (2E).",
   r"u_{r} = \frac{[sy]^{2}}{2([E*1000|0])} = [sy*sy/(2*E*1000)|5] MPa = [ans|1] kJ/m^{3}.",
   "sy*sy/(2*E*1000)*1000", sy=[250, 345, 275], E=[200, 200, 70])
NQ('materials-c', '-', '', 2, 8.04, "Concrete has f'_{c} = [fc] MPa. Using E_{c} = 4,700 × the square root of f'_{c} (MPa) and E_{s} = 200 GPa, what is the modular ratio of steel to concrete?",
   "The modular ratio n = E_{s} / E_{c} converts steel area into an equivalent area of concrete in transformed-section analysis. Stronger concrete is stiffer, so n falls as strength rises.",
   r"E_{c} = 4,700\sqrt{[fc]} = [4700*sqrt(fc)|0] MPa. || n = \frac{200,000}{[4700*sqrt(fc)|0]} = [ans|2].",
   "200000/(4700*sqrt(fc))", fc=[28, 35, 21])
NQ('materials-c', MS + '::true stress', 'MPa', 1, 432, "At a point in a tension test before necking begins, the engineering stress is [s] MPa and the engineering strain is [es|2]. What is the true stress?",
   "Engineering stress uses the original area; true stress uses the current, smaller area. While deformation is uniform and volume is constant, true stress = engineering stress × (1 + engineering strain).",
   "True stress = [s](1 + [es|2]) = [ans|1] MPa.",
   "s*(1+es)", s=[400, 520, 310], es=[0.08, 0.12, 0.05])
if __name__ == '__main__': run('f5')
