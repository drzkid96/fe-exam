"""Version families, part 3: transportation, water resources and environmental."""
from author_v import *
def F(base, stem, concept, sol, ans, wrong=None, dp=None, fig=None, sfig=None, **P): V(base, stem, P, ans, sol, wrong, dp, fig, sfig, concept)

# ---------------- Transportation ----------------
F('transport-0001', "A vehicle travels at [V] mph on a level road. Using a perception-reaction time of 2.5 s and a deceleration rate of 11.2 ft/s^{2}, what is the stopping sight distance?",
  "Stopping sight distance has two parts: the distance covered at full speed during perception and reaction, 1.47 V t, and the braking distance, V^{2} / (30 (a/32.2 ± G)). With V in mph the constants give feet. On a level road the grade term G is zero.",
  r"Reaction distance = 1.47([V])(2.5) = [1.47*V*2.5|1] ft. || Braking distance = \frac{[V]^{2}}{30(11.2 / 32.2)} = \frac{[V*V]}{[30*11.2/32.2|2]} = [V*V/(30*11.2/32.2)|1] ft. || SSD = [1.47*V*2.5|1] + [V*V/(30*11.2/32.2)|1] = [ans|0] ft.",
  "1.47*V*2.5+V*V/(30*11.2/32.2)", wrong=["1.47*V*2.5", "V*V/(30*11.2/32.2)", "1.2*(1.47*V*2.5+V*V/(30*11.2/32.2))"], dp=0, V=[60, 45, 70, 35])
F('transport-0002', "What is the minimum radius of a horizontal curve for a design speed of [V] mph, with a superelevation of [e]% and a side friction factor of [f|2]?",
  "On a horizontal curve the centripetal force is supplied by superelevation and side friction together. Balancing them gives the minimum radius R = V^{2} / (15 (e + f)), with V in mph, R in feet and e as a decimal.",
  r"R_{min} = \frac{V^{2}}{15(e + f)} = \frac{[V]^{2}}{15([e/100|2] + [f|2])} = \frac{[V*V]}{[15*(e/100+f)|2]} = [ans|0] ft.",
  "V*V/(15*(e/100+f))", dp=0, V=[50, 60, 40, 70], e=[6, 8, 4, 6], f=[0.14, 0.12, 0.16, 0.10])
F('transport-0003', "Traffic in a freeway lane has a density of [k] veh/mi and a space mean speed of [u] mph. What is the flow rate?",
  "The fundamental relation of traffic flow: flow = density × space mean speed (q = k u). The units confirm it: veh/mi × mi/h = veh/h.",
  "q = k u = [k] × [u] = [ans|0] veh/h.", "k*u", wrong=["u/k", "k+u", "k*u/2"], k=[40, 25, 60, 32], u=[45, 58, 30, 50])
F('transport-0004', "An intersection approach carries [Vh] vehicles in the peak hour. The busiest 15 minutes of that hour carries [V15] vehicles. What is the peak hour factor?",
  "The peak hour factor compares the hourly volume with the flow rate of the busiest 15 minutes: PHF = V / (4 × V_{15}). A value of 1.0 means perfectly even flow; lower values mean sharper peaking. Dividing a volume by the PHF gives the design flow rate.",
  r"PHF = \frac{V}{4 × V_{15}} = \frac{[Vh]}{4([V15])} = \frac{[Vh]}{[4*V15]} = [ans|2].",
  "Vh/(4*V15)", dp=2, Vh=[1200, 1840, 960, 2250], V15=[375, 500, 300, 625])
F('transport-0005', "A crest vertical curve connects a +[g1]% grade to a -[g2]% grade and is [L] ft long. How far from the start of the curve (PVC) is the high point?",
  "A vertical curve is a parabola, so its grade changes at a constant rate r = (g_{2} - g_{1}) / L. The high or low point is where the grade reaches zero: x = -g_{1} / r = g_{1} L / (g_{1} - g_{2}).",
  r"x = \frac{g_{1} L}{g_{1} - g_{2}} = \frac{[g1]([L])}{[g1] - (-[g2])} = \frac{[g1*L]}{[g1+g2]} = [ans|0] ft from the PVC.",
  "g1*L/(g1+g2)", wrong=["g2*L/(g1+g2)", "L/2", "L*g2/g1"], dp=0, fig=lambda e: vcurve(e['g1'], -e['g2'], e['L']), g1=[3, 2, 4, 1.5], g2=[2, 4, 1, 3.5], L=[500, 600, 800, 400])
F('transport-0007', "A flexible pavement has [D1] in of asphalt (layer coefficient 0.44), [D2] in of base (0.14) and [D3] in of subbase (0.11). Drainage coefficients are 1.0. What is the structural number?",
  "In the AASHTO flexible pavement method, each layer contributes its thickness times a layer coefficient that reflects its relative strength, and unbound layers are also multiplied by a drainage coefficient. The sum is the structural number, SN.",
  "SN = a_{1}D_{1} + a_{2}D_{2}m_{2} + a_{3}D_{3}m_{3} = 0.44([D1]) + 0.14([D2])(1.0) + 0.11([D3])(1.0) = [0.44*D1|2] + [0.14*D2|2] + [0.11*D3|2] = [ans|2].",
  "0.44*D1+0.14*D2+0.11*D3", dp=2, D1=[4, 5, 3, 6], D2=[8, 6, 10, 8], D3=[10, 12, 8, 6])
F('transport-0008', "Using the correlation M_{R} = 1,500 × CBR (psi), what is the resilient modulus of a subgrade with a CBR of [CBR]?",
  "The resilient modulus describes subgrade stiffness under repeated wheel loads and is the subgrade input to pavement design. For fine-grained soils with low CBR it is often estimated from the correlation M_{R} = 1,500 × CBR, in psi.",
  "M_{R} = 1,500 × [CBR] = [ans|0] psi.", "1500*CBR", wrong=["150*CBR", "1000*CBR", "2500*CBR"], dp=0, CBR=[6, 4, 8, 10])
F('transport-0009', "A highway lane carries [dly] equivalent single axle loads (ESALs) per day with no growth. How many ESALs does it carry over a [n]-year design life?",
  "Pavement design uses the total number of 18-kip equivalent single axle loads over the design life. With no growth it is the daily ESALs × 365 × years.",
  "Design ESALs = [dly] × 365 × [n] = [dly*365*n|0] = [ans|2] million.",
  "dly*365*n/1e6", wrong=["dly*365/1e6", "dly*n/1000", "dly*365*n/1e5"], dp=2, dly=[500, 800, 300, 1200], n=[20, 15, 25, 20])
F('transport-0010', "A signalized approach has [N] lanes, each with a saturation flow rate of [s] veh/h. The approach gets [gr] s of effective green in a [C] s cycle. What is its capacity?",
  "A signalized lane group can only discharge during its effective green. Capacity is the saturation flow rate times the share of the cycle that is green: c = N s (g / C).",
  r"c = N s \frac{g}{C} = [N]([s]) × \frac{[gr]}{[C]} = [N*s] × [gr/C|3] = [ans|0] veh/h.",
  "N*s*gr/C", dp=0, N=[2, 3, 2, 4], s=[1900, 1800, 1900, 1750], gr=[40, 35, 27, 54], C=[100, 90, 60, 120])
F('transport-0011', "A road follows the Greenshields model with a free-flow speed of [uf] mph and a jam density of [kj] veh/mi. What is its capacity?",
  "Greenshields assumes speed falls linearly with density. Flow = density × speed is then a parabola that peaks at half the jam density and half the free-flow speed, so capacity = u_{f} k_{j} / 4.",
  r"At capacity: k = [kj] / 2 = [kj/2] veh/mi and u = [uf] / 2 = [uf/2] mph. || q_{max} = [kj/2] × [uf/2] = \frac{[uf]([kj])}{4} = [ans|0] veh/h.",
  "uf*kj/4", wrong=["uf*kj/8", "uf*kj/2", "uf*kj"], dp=0, fig=lambda e: greenshields(e['uf'], e['kj']), uf=[60, 50, 70, 45], kj=[120, 160, 110, 200])
F('transport-0012', "A signal approach has a speed of [mph] mph ([fps] ft/s) on level ground. Using a perception-reaction time of 1.0 s and a deceleration rate of 10 ft/s^{2}, what yellow change interval is needed?",
  "The yellow interval must cover the driver's reaction time plus the time to decelerate to a stop, so that a driver too close to stop can enter legally: y = t + v / (2a + 2 g G), with v in ft/s. On level ground the grade term is zero.",
  r"y = t + \frac{v}{2a} = 1.0 + \frac{[fps]}{2(10)} = 1.0 + [fps/20|2] = [ans|2] s.",
  "1.0+fps/20", dp=2, mph=[30, 45, 60, 37.5], fps=[44, 66, 88, 55])
F('transport-0013', "A subdivision has [n] dwelling units. The trip generation rate is [rate|1] trips per dwelling unit per day. How many daily trips does it generate?",
  "Trip generation, the first step of the four-step planning model, estimates trip ends from land use. With an average rate, trips = rate × number of units.",
  "Trips = [rate|1] × [n] = [ans|0] trips per day.", "n*rate", wrong=["n/rate", "n*rate/10", "n*rate*10"], dp=0, n=[250, 400, 120, 650], rate=[9.4, 9.4, 5.8, 7.2])
F('transport-0014', "An intersection has [cr] crashes in one year. Its entering volume is [adt] vehicles per day. What is the crash rate per million entering vehicles?",
  "Crash rates normalise crash counts by exposure so that sites with different volumes can be compared. For intersections: rate = crashes × 1,000,000 / (ADT × 365 × years).",
  r"Entering vehicles in one year = [adt] × 365 = [adt*365]. || Rate = \frac{[cr] × 1,000,000}{[adt*365]} = [ans|2] crashes per million entering vehicles.",
  "cr*1e6/(adt*365)", dp=2, cr=[12, 18, 7, 25], adt=[20000, 32000, 12500, 45000])
F('transport-0015', "A logit mode choice model gives a utility of [Ua|1] for auto and [Ub|1] for bus. What share of travellers choose the bus?",
  "The multinomial logit model gives each mode a share proportional to e raised to its utility: P(mode) = e^{U} / (sum of e^{U} over all modes). Only differences in utility matter.",
  r"e^{[Ua|1]} = [exp(Ua)|4] and e^{[Ub|1]} = [exp(Ub)|4]. || P(bus) = \frac{[exp(Ub)|4]}{[exp(Ua)|4] + [exp(Ub)|4]} = [ans|3], about [ans*100|0]%.",
  "exp(Ub)/(exp(Ua)+exp(Ub))", wrong=["Ua/(Ua+Ub)", "abs(Ua)/abs(Ub)", "exp(Ua)/(exp(Ua)+exp(Ub))"], dp=3, Ua=[-0.5, -0.6, -0.2, -1.0], Ub=[-1.5, -1.8, -2.0, -1.6])
F('transport-0016', "A horizontal curve has a radius of [R] ft and a deflection angle of [D]°. What is the length of the curve?",
  "The length of a circular curve is the arc subtended by the deflection (central) angle: L = R × angle in radians = R × Δ × π / 180.",
  r"L = R Δ \frac{π}{180} = [R] × [D] × \frac{π}{180} = [ans|1] ft.",
  "R*D*pi/180", wrong=["R*D*pi/360", "R*D*pi/90", "R*D"], dp=1, fig=lambda e: hcurve(e['R'], e['D']), R=[1000, 800, 1500, 600], D=[30, 45, 24, 52])
F('transport-0017', "A horizontal curve has a radius of [R] ft and a deflection angle of [D]°. What is the tangent length from the PC to the PI?",
  "The two tangents meet at the PI. Each tangent, from PC to PI or PI to PT, has length T = R tan(Δ / 2), from the right triangle formed by the radius, the tangent and the line from the centre to the PI.",
  "T = R tan(Δ / 2) = [R] × tan([D/2]°) = [R] × [tan(rad(D/2))|4] = [ans|1] ft.",
  "R*tan(rad(D/2))", dp=1, fig=lambda e: hcurve(e['R'], e['D']), R=[1000, 800, 1500, 600], D=[30, 45, 24, 52])
F('transport-0018', "A crest vertical curve joins grades of +[g1]% and -[g2]%. The design requires a rate of vertical curvature K of [K]. What minimum curve length is needed?",
  "K is the horizontal length of curve needed for each 1% of grade change, chosen from the design speed to provide sight distance. Curve length = K × A, where A is the algebraic difference in grades in percent.",
  "A = |-[g2] - [g1]| = [g1+g2]%. || L = K A = [K] × [g1+g2] = [ans|0] ft.",
  "K*(g1+g2)", wrong=["K/(g1+g2)", "K", "K*(g1+g2)**2"], dp=0, fig=lambda e: vcurve(e['g1'], -e['g2'], 'L = ?'), g1=[2, 3, 1.5, 4], g2=[3, 1, 2.5, 2], K=[150, 84, 247, 61])

# ---------------- Water resources and environmental ----------------
F('water-0001', "A [A] acre parking area has a runoff coefficient of [C|2]. The design rainfall intensity is [i|1] in/h. Using the rational method, what is the peak runoff?",
  "The rational method estimates peak runoff from a small catchment as Q = C i A. With intensity in in/h and area in acres, Q comes out in cfs with no conversion factor (the factor is 1.008). The intensity is the one for a storm lasting the time of concentration.",
  "Q = C i A = [C|2] × [i|1] × [A] = [ans|1] cfs.", "C*i*A", wrong=["C*A", "i*A", "A*i/C"], dp=1, A=[12, 20, 8, 35], C=[0.60, 0.45, 0.85, 0.30], i=[2.5, 3.2, 1.8, 4.0])
F('water-0002', "A rectangular concrete channel is [b] m wide and flows [y] m deep on a slope of [S]. Manning's n is [n|3]. What is the discharge?",
  "Manning's equation for uniform open channel flow (SI): Q = (1/n) A R^{2/3} S^{1/2}. The hydraulic radius R is the flow area divided by the wetted perimeter, which counts only the bed and sides in contact with water.",
  r"A = [b] × [y] = [b*y|2] m^{2}. || Wetted perimeter = [b] + 2([y]) = [b+2*y|2] m, so R = [b*y|2] / [b+2*y|2] = [b*y/(b+2*y)|3] m. || Q = \frac{1}{[n|3]}([b*y|2])([b*y/(b+2*y)|3])^{2/3}([S])^{1/2} = [ans|2] m^{3}/s.",
  "1/n*b*y*(b*y/(b+2*y))**(2/3)*S**0.5", dp=2, fig=lambda e: channel(e['b'], e['y']), b=[3, 4, 2, 5], y=[1, 1.5, 0.8, 2], S=[0.001, 0.002, 0.0015, 0.0005], n=[0.015, 0.013, 0.015, 0.020])
F('water-0003', "A pump delivers [Q|2] m^{3}/s of water against a total head of [H] m. The pump is [eff]% efficient. What power must be supplied to the pump?  Use 9.81 kN/m^{3}.",
  "The power added to the water is (specific weight) × Q × H. The pump must be supplied more than that because of its losses: brake power = water power / efficiency.",
  r"Water power = 9.81 × [Q|2] × [H] = [9.81*Q*H|2] kW. || Brake power = \frac{[9.81*Q*H|2]}{[eff/100|2]} = [ans|1] kW.",
  "9.81*Q*H/(eff/100)", wrong=["9.81*Q*H*(eff/100)", "9.81*Q*H", "9.81*Q*H/(eff/100)**2"], dp=1, Q=[0.05, 0.08, 0.12, 0.03], H=[30, 45, 20, 60], eff=[75, 80, 70, 65])
F('water-0004', "A sedimentation tank has a volume of [Vt] m^{3} and treats a flow of [Q] m^{3}/day. What is the detention time?",
  "Hydraulic detention time is the average time water spends in a tank: volume divided by flow rate. Watch the time units; a flow in m^{3}/day gives a time in days.",
  r"t = \frac{V}{Q} = \frac{[Vt]}{[Q]} = [Vt/Q|3] days = [Vt/Q|3] × 24 = [ans] h.",
  "Vt/Q*24", wrong=["Vt/Q", "Vt/Q*12", "Vt/Q*48"], Vt=[1800, 2400, 900, 3600], Q=[7200, 19200, 3600, 43200])
F('water-0005', "An aquifer has a hydraulic conductivity of [K] m/day and a hydraulic gradient of [i]. What is the flow through a cross-section of [A] m^{2}?",
  "Darcy's law for groundwater: Q = K i A. The hydraulic gradient i is the drop in head per unit distance along the flow path and has no units.",
  "Q = K i A = [K] × [i] × [A] = [ans|0] m^{3}/day.", "K*i*A", wrong=["i*A", "K*i*A/2", "K*A"], dp=0, K=[15, 8, 25, 12], i=[0.004, 0.01, 0.002, 0.005], A=[2000, 1500, 3000, 800])
F('water-0007', "A watershed with a curve number of [CN] receives [P|1] in of rain. Using the NRCS (SCS) method, what is the depth of runoff?",
  "The NRCS curve number method converts rainfall to runoff depth. The potential retention is S = 1,000/CN - 10 (inches), the initial abstraction is taken as 0.2 S, and runoff is Q = (P - 0.2S)^{2} / (P + 0.8S) when P exceeds 0.2 S.",
  r"S = \frac{1,000}{[CN]} - 10 = [1000/CN-10|2] in. || Q = \frac{([P|1] - 0.2 × [1000/CN-10|2])^{2}}{[P|1] + 0.8 × [1000/CN-10|2]} = \frac{[(P-0.2*(1000/CN-10))**2|2]}{[P+0.8*(1000/CN-10)|2]} = [ans|2] in.",
  "(P-0.2*(1000/CN-10))**2/(P+0.8*(1000/CN-10))", dp=2, CN=[80, 70, 85, 90], P=[4.0, 5.0, 3.0, 2.5])
F('water-0008', "A rectangular channel carries a flow of [q|1] m^{3}/s per metre of width. What is the critical depth? Use g = 9.81 m/s^{2}.",
  "Critical depth is the depth of minimum specific energy for a given flow, where the Froude number equals 1. For a rectangular channel y_{c} = (q^{2} / g)^{1/3}, with q the flow per unit width. The minimum specific energy is 1.5 y_{c}.",
  r"y_{c} = (\frac{q^{2}}{g})^{1/3} = (\frac{[q|1]^{2}}{9.81})^{1/3} = ([q*q/g|3])^{1/3} = [ans|3] m.",
  "(q*q/g)**(1/3)", wrong=["q/g", "(q/g)**0.5", "1.5*(q*q/g)**(1/3)"], dp=3, q=[3.0, 2.0, 4.5, 1.2])
F('water-0009', "A pump delivers [Q1] L/s at [N1] rpm. Using the affinity laws, what flow does it deliver at [N2] rpm?",
  "The pump affinity laws relate performance at two speeds for the same impeller: flow varies with speed, head with speed squared and power with speed cubed.",
  r"Q_{2} = Q_{1} × \frac{N_{2}}{N_{1}} = [Q1] × \frac{[N2]}{[N1]} = [ans|1] L/s. The head would change by a factor of ([N2] / [N1])^{2} = [(N2/N1)**2|2].",
  "Q1*N2/N1", wrong=["Q1*N1/N2", "Q1*(N2/N1)**2", "Q1*(N2/N1)**3"], dp=1, Q1=[100, 60, 250, 40], N1=[1200, 1750, 900, 1450], N2=[1500, 1450, 1200, 1750])
F('water-0010', "A town of [pop] people uses an average of [lpcd] L per person per day. The maximum-day peaking factor is [pf|1]. What is the maximum-day demand?",
  "Average day demand is population × per capita use. Treatment plants and sources are sized for the maximum day, found by applying a peaking factor to the average.",
  "Average day = [pop] × [lpcd] L = [pop*lpcd/1000|0] m^{3}/day. || Maximum day = [pf|1] × [pop*lpcd/1000|0] = [ans|0] m^{3}/day.",
  "pop*lpcd*pf/1000", dp=0, pop=[25000, 40000, 12000, 85000], lpcd=[400, 350, 450, 300], pf=[1.8, 1.5, 2.0, 1.6])
F('water-0011', "The water surface in an elevated tank is [h] m above a hydrant. With no flow in the system, what is the pressure at the hydrant? Use 9.81 kN/m^{3}.",
  "With no flow there are no friction losses, so the pressure anywhere in the system is hydrostatic: specific weight × the height of the water surface above that point.",
  "p = 9.81 × [h] = [ans|1] kPa.", "9.81*h", wrong=["h", "9.81*h/2", "100*h"], dp=1, fig=lambda e: tank(e['h']), h=[40, 25, 55, 32])
F('water-0012', "What is the probability that a [T]-year flood is equalled or exceeded at least once in a [n]-year period?",
  "A T-year event has probability 1/T in any one year. The chance that it does not occur in n independent years is (1 - 1/T)^{n}, so the risk of at least one occurrence is 1 - (1 - 1/T)^{n}.",
  r"p = 1 / [T] = [1/T|3] per year. || Risk = 1 - (1 - [1/T|3])^{[n]} = 1 - [(1-1/T)**n|4] = [ans|3].",
  "1-(1-1/T)**n", wrong=["1/T", "n/T", "(1-1/T)**n"], dp=3, T=[50, 100, 25, 10], n=[10, 30, 5, 3])
F('water-0013', "What is the annual exceedance probability of a [T]-year flood?",
  "The return period is the average interval between events of a given size or larger. Its reciprocal is the probability of that event being equalled or exceeded in any single year.",
  r"Annual exceedance probability = \frac{1}{T} = \frac{1}{[T]} = [1/T|3] = [ans]%.",
  "100/T", wrong=["T/100", "T/10", "T"], T=[25, 50, 20, 200])
F('water-0014', "Stormwater flows into a detention basin at [qi|1] m^{3}/s and leaves at [qo|1] m^{3}/s for [t] minutes. How much water is stored in the basin during that time?",
  "Storage routing is a volume balance: the change in storage equals inflow minus outflow, multiplied by the time step. Convert the time to seconds to match flows in m^{3}/s.",
  "Change in storage = (inflow - outflow) × time = ([qi|1] - [qo|1]) × ([t] × 60) = [qi-qo|1] × [t*60] = [ans|0] m^{3}.",
  "(qi-qo)*t*60", dp=0, qi=[3.0, 5.5, 2.4, 8.0], qo=[1.0, 2.0, 0.9, 3.5], t=[20, 45, 30, 15])
F('water-0015', "Development raises a site's runoff coefficient from [C1|2] to [C2|2]. With the same rainfall intensity and area, by what factor does the rational-method peak flow increase?",
  "In Q = C i A, peak flow is directly proportional to the runoff coefficient when intensity and area are unchanged. The ratio of the coefficients is the ratio of the peak flows.",
  r"\frac{Q_{after}}{Q_{before}} = \frac{C_{2}}{C_{1}} = \frac{[C2|2]}{[C1|2]} = [ans|2].",
  "C2/C1", wrong=["C1/C2", "1+C2-C1", "(C2/C1)**2"], dp=2, C1=[0.30, 0.25, 0.40, 0.20], C2=[0.80, 0.70, 0.90, 0.85])
F('water-0016', "A [D] mm diameter sewer flows full on a slope of [S] with Manning's n = 0.013. What is the flow velocity?",
  "Manning's equation for velocity (SI): V = (1/n) R^{2/3} S^{1/2}. For a circular pipe flowing full the hydraulic radius is D / 4.",
  r"R = D / 4 = [D/1000|3] / 4 = [D/4000|4] m. || V = \frac{1}{0.013}([D/4000|4])^{2/3}([S])^{1/2} = [ans|3] m/s.",
  "1/0.013*(D/4000)**(2/3)*S**0.5", dp=3, D=[300, 450, 600, 200], S=[0.005, 0.003, 0.002, 0.01])
F('water-0017', "A sewer serves [pop] people who each generate [lpcd] L of wastewater per day. With a peaking factor of [pf|1], what is the peak flow?",
  "Sewers are sized for peak flow, the average flow multiplied by a peaking factor that is larger for small populations. Convert daily volume to L/s by dividing by 86,400 s per day.",
  r"Average flow = [pop] × [lpcd] = [pop*lpcd] L/day = \frac{[pop*lpcd]}{86,400} = [pop*lpcd/86400|1] L/s. || Peak flow = [pf|1] × [pop*lpcd/86400|1] = [ans|1] L/s.",
  "pop*lpcd*pf/86400", wrong=["pop*lpcd/86400", "pop*lpcd/1000", "pop*lpcd*pf/1000"], dp=1, pop=[12000, 30000, 8000, 50000], lpcd=[300, 250, 350, 280], pf=[3.0, 2.5, 3.5, 2.2])
F('water-0018', "Groundwater moves through an aquifer with a hydraulic conductivity of [K] m/day, a hydraulic gradient of [i] and a porosity of [n|2]. What is the average seepage velocity?",
  "Darcy velocity, K i, is flow per unit of total cross-section. Water only moves through the pores, so the actual average (seepage) velocity is larger: v = K i / n. Use seepage velocity for travel times of contaminants.",
  r"Darcy velocity = [K] × [i] = [K*i] m/day. || Seepage velocity = \frac{[K*i]}{[n|2]} = [ans] m/day.",
  "K*i/n", wrong=["K*i*n", "K*i", "K*i/n**2"], K=[15, 8, 25, 40], i=[0.004, 0.01, 0.002, 0.003], n=[0.30, 0.25, 0.40, 0.20])
F('water-0019', "A [Vs] mL wastewater sample is diluted to 300 mL in a BOD bottle. The dissolved oxygen falls from [DOi|1] mg/L to [DOf|1] mg/L in five days. What is the BOD_{5}?",
  "BOD is the oxygen consumed by microorganisms while they break down organic matter. In a diluted test, the drop in dissolved oxygen is divided by the fraction of the bottle that is sample: BOD = (DO_{initial} - DO_{final}) / P, with P = sample volume / bottle volume.",
  r"Dilution fraction P = [Vs] / 300 = [Vs/300|4]. || BOD_{5} = \frac{[DOi|1] - [DOf|1]}{[Vs/300|4]} = [DOi-DOf|1] × [300/Vs|1] = [ans] mg/L.",
  "(DOi-DOf)*300/Vs", wrong=["DOi-DOf", "(DOi-DOf)*5", "(DOi-DOf)*300/Vs*5"], Vs=[5, 10, 6, 15], DOi=[8.0, 8.5, 7.8, 9.0], DOf=[3.5, 4.0, 2.4, 5.5])
F('water-0020', "A water sample contains [Ca] mg/L of calcium and [Mg] mg/L of magnesium. What is the total hardness, expressed as mg/L of CaCO_{3}? Use equivalent weights of 20 for calcium, 12.2 for magnesium and 50 for CaCO_{3}.",
  "Hardness is the sum of the multivalent cations, mainly calcium and magnesium, each converted to its CaCO_{3} equivalent: concentration × (50 / equivalent weight of the ion).",
  r"Calcium: [Ca] × \frac{50}{20} = [Ca*2.5|1] mg/L as CaCO_{3}. || Magnesium: [Mg] × \frac{50}{12.2} = [Mg*50/12.2|1] mg/L as CaCO_{3}. || Total hardness = [Ca*2.5|1] + [Mg*50/12.2|1] = [ans|1] mg/L as CaCO_{3}.",
  "Ca*50/20+Mg*50/12.2", dp=1, Ca=[80, 60, 100, 45], Mg=[24, 18, 30, 12])
F('water-0021', "[nw] machines each produce a sound level of [Ls] dB at a receiver. What is the combined sound level when all of them run?",
  "Decibels are logarithmic, so sound levels cannot be added directly. For n equal sources the combined level is L + 10 log_{10}(n): two equal sources add 3 dB, ten add 10 dB.",
  "Combined level = [Ls] + 10 log_{10}([n]) = [Ls] + [10*log10(n)|1] = [ans|0] dB.",
  "Ls+10*log10(n)", wrong=["Ls", "Ls+20*log10(n)", "n*Ls"], dp=0, n=[2, 4, 2, 10], nw=['Two', 'Four', 'Two', 'Ten'], Ls=[80, 75, 92, 68])
F('water-0023', "A clarifier treats [Q] m^{3}/day and has a surface area of [A] m^{2}. What is its surface overflow rate?",
  "The surface overflow rate, Q / A, is the upward velocity of water in a clarifier. A particle is removed if its settling velocity is at least the overflow rate, so the rate is the key design parameter and depth does not appear.",
  r"Overflow rate = \frac{Q}{A} = \frac{[Q]}{[A]} = [ans|1] m^{3}/m^{2}·day, or [ans|1] m/day.",
  "Q/A", dp=1, Q=[7200, 12000, 5400, 20000], A=[240, 300, 150, 625])
F('water-0024', "A plant treats [Q] m^{3}/day and applies a chlorine dose of [dose|1] mg/L. How much chlorine is used per day?",
  "Mass feed rate = flow × concentration. A dose of 1 mg/L is 1 g/m^{3}, so m^{3}/day × mg/L gives g/day; divide by 1,000 for kg/day.",
  "Chlorine = [Q] m^{3}/day × [dose|1] g/m^{3} = [Q*dose|0] g/day = [ans|1] kg/day.",
  "Q*dose/1000", wrong=["Q*dose/10000", "Q*dose/100", "Q/dose"], Q=[10000, 25000, 4000, 60000], dose=[2, 3.5, 5, 1.2])
if __name__ == '__main__': save()
