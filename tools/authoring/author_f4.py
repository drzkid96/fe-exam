"""Further question types: fluid mechanics, water resources and environmental, and surveying. See author_fx.py for the format."""
from author_fx import *
FM, EN, CE = 'Fluid Mechanics', 'Environmental Engineering', 'Civil Engineering'
# ================= Fluid mechanics =================
NQ('fluids-a', 'venturi meters', 'L/s', 1, 31.5, "A venturi meter in a [d1] mm water pipe has a [d2] mm throat. The piezometric head drops by [dh|1] m between inlet and throat, and the meter coefficient is 0.98. What is the flow rate? Use g = 9.81 m/s^{2}.",
   "A venturi speeds the flow up in its throat, and Bernoulli's equation turns the resulting drop in head into a velocity. Continuity brings in the area ratio: Q = C_{v} A_{2} × square root of (2 g × head drop / (1 - (A_{2}/A_{1})^{2})).",
   r"A_{2} = \frac{π([d2/1000|3])^{2}}{4} = [pi*(d2/1000)**2/4|5] m^{2}, and (A_{2}/A_{1})^{2} = ([d2] / [d1])^{4} = [(d2/d1)**4|4]. || Q = 0.98([pi*(d2/1000)**2/4|5]) \sqrt{\frac{2(9.81)([dh|1])}{1 - [(d2/d1)**4|4]}} = [0.98*pi*(d2/1000)**2/4*sqrt(2*g*dh/(1-(d2/d1)**4))|5] m^{3}/s = [ans|1] L/s.",
   "0.98*pi*(d2/1000)**2/4*sqrt(2*g*dh/(1-(d2/d1)**4))*1000", d1=[200, 300, 150], d2=[100, 150, 90], dh=[0.8, 0.5, 1.2])
NQ('fluids-a', CE + '::weir formulas', 'L/s', 1, 43.8, "A 90° V-notch weir has a head of [H|2] m above the bottom of the notch. Using Q = 1.40 H^{5/2} in SI units, what is the discharge?",
   "Flow through a triangular notch grows with the head to the 5/2 power, because both the depth and the width of the flow section increase with head. That makes a V-notch sensitive at low flows.",
   "Q = 1.40([H|2])^{2.5} = 1.40 × [H**2.5|5] = [1.4*H**2.5|5] m^{3}/s = [ans|1] L/s.",
   "1.4*H**2.5*1000", H=[0.25, 0.40, 0.15])
NQ('fluids-a', 'orifices', 'L/s', 2, 9.43, "An orifice plate with a [d] mm opening and a discharge coefficient of 0.62 is installed in a water line. The pressure drop across it is [dpk] kPa. What is the flow rate? Take the density of water as 1,000 kg/m^{3} and ignore the approach velocity.",
   "An orifice turns pressure into velocity: the ideal velocity is the square root of (2 × pressure drop / density). The discharge coefficient allows for the contraction of the jet and for friction.",
   r"A = \frac{π([d/1000|3])^{2}}{4} = [pi*(d/1000)**2/4|6] m^{2}. || Q = 0.62([pi*(d/1000)**2/4|6]) \sqrt{\frac{2([dpk*1000|0])}{1,000}} = [0.62*pi*(d/1000)**2/4*sqrt(2*dpk)|5] m^{3}/s = [ans|2] L/s.",
   "0.62*pi*(d/1000)**2/4*sqrt(2*dpk*1000/1000)*1000", d=[50, 75, 40], dpk=[30, 18, 50])
NQ('fluids-b', 'capillary rise', 'mm', 1, 29.7, "A clean glass tube with an inside diameter of [d|1] mm stands in water. The surface tension is [sig|4] N/m and the contact angle is 0°. How high does the water rise in the tube? Use 9,810 N/m^{3} for water.",
   "Surface tension pulling up around the tube's wall supports the weight of the raised column: h = 4 (surface tension) cos(contact angle) / (specific weight × diameter). Narrower tubes give a higher rise.",
   r"h = \frac{4([sig|4])(1)}{9,810([d/1000|4])} = [4*sig/(9810*d/1000)|5] m = [ans|1] mm.",
   "4*sig/(9810*d/1000)*1000", d=[1.0, 0.5, 2.5], sig=[0.0728, 0.0728, 0.0712])
NQ('fluids-b', 'stress, pressure, and viscosity', 'N', 1, 125, "A flat plate with an area of [A|2] m^{2} slides at [V|1] m/s over a fixed surface on an oil film [h|1] mm thick. The oil's dynamic viscosity is [mu|2] Pa·s. What force keeps the plate moving?",
   "For a thin film the velocity varies linearly across the gap, so the shear stress is viscosity times velocity divided by film thickness (Newton's law of viscosity). Force is stress times area.",
   r"Shear stress = \frac{[mu|2]([V|1])}{[h/1000|4]} = [mu*V/(h/1000)|1] Pa. || Force = [mu*V/(h/1000)|1] × [A|2] = [ans|1] N.",
   "mu*V/(h/1000)*A", mu=[0.25, 0.08, 1.2], A=[0.5, 0.2, 0.05], V=[2, 0.5, 0.3], h=[2, 0.5, 1.5])
NQ('fluids-b', 'buoyancy', '', 3, 2.5, "A sample weighs [Wa|1] N in air and [Ww|1] N when fully submerged in water. What is its specific gravity?",
   "The loss of weight in water equals the weight of water displaced, which has the sample's volume. Specific gravity is therefore the weight in air divided by the loss of weight.",
   r"SG = \frac{[Wa|1]}{[Wa|1] - [Ww|1]} = \frac{[Wa|1]}{[Wa-Ww|1]} = [ans|3].",
   "Wa/(Wa-Ww)", Wa=[50, 120, 7.5], Ww=[30, 75, 4.7])
NQ('fluids-c', 'center of pressure', 'm', 3, 3.714, "A vertical rectangular gate is [h|1] m tall. Its top edge is [a|1] m below the water surface. How far below the surface is the centre of pressure?",
   "Pressure grows with depth, so the resultant force acts below the centroid of the gate. The centre of pressure is at the centroid depth plus I / (centroid depth × A); for a rectangle that extra distance is h^{2} / (12 × centroid depth).",
   r"Centroid depth = [a|1] + \frac{[h|1]}{2} = [a+h/2|2] m. || Centre of pressure = [a+h/2|2] + \frac{[h|1]^{2}}{12([a+h/2|2])} = [ans|3] m.",
   "(a+h/2)+h*h/(12*(a+h/2))", a=[2, 1, 4], h=[3, 2, 1.5])
NQ('fluids-c', 'pressure field in a static liquid', 'N', 0, 5000, "A hydraulic jack has an input piston [d1] mm in diameter and an output piston [d2] mm in diameter. A force of [F1] N is applied to the input piston. Ignoring friction, what force does the output piston deliver?",
   "Pressure in a confined static fluid is the same throughout (Pascal's law). The same pressure on a larger piston gives a larger force, in proportion to the areas, which go with diameter squared.",
   r"F_{2} = F_{1} (\frac{d_{2}}{d_{1}})^{2} = [F1] (\frac{[d2]}{[d1]})^{2} = [ans|0] N.",
   "F1*(d2/d1)**2", wrong=["F1*d2/d1", "F1*(d2/d1)**2/2", "F1*(d2/d1)**3"], F1=[200, 150, 400], d1=[20, 25, 15], d2=[100, 150, 120])
NQ('fluids-c', 'forces on submerged surfaces', 'kN', 2, 44.38, "A circular access cover [d|1] m in diameter is set in the vertical wall of a water tank. Its centre is [hc|1] m below the water surface. What is the hydrostatic force on the cover? Use 9.81 kN/m^{3}.",
   "The force on any flat submerged surface is the pressure at its centroid times its area. The shape affects only the area and where the force acts.",
   r"F = (9.81)([hc|1]) × \frac{π([d|1])^{2}}{4} = [9.81*hc|2] × [pi*d*d/4|4] = [ans|2] kN.",
   "9.81*hc*pi*d*d/4", d=[1.2, 0.8, 2.0], hc=[4, 6.5, 3])
NQ('fluids-d', 'minor losses', 'm', 3, 0.413, "Water flows at [v|1] m/s through a fitting with a loss coefficient of [K|1]. What head is lost in the fitting? Use g = 9.81 m/s^{2}.",
   "Losses in fittings, valves, bends and entrances are written as a coefficient times the velocity head, v^{2} / 2g. They add to the friction loss in the pipe.",
   r"h = K \frac{v^{2}}{2g} = [K|1] × \frac{[v|1]^{2}}{2(9.81)} = [ans|3] m.",
   "K*v*v/(2*g)", K=[0.9, 10, 0.5], v=[3, 2, 4.5])
NQ('fluids-d', 'Reynolds number', '', 3, 0.04, "Flow in a pipe is laminar with a Reynolds number of [Re]. What is the Darcy friction factor?",
   "In laminar flow the friction factor depends only on the Reynolds number: f = 64 / Re. Pipe roughness matters only once the flow is turbulent, where the Moody diagram is needed.",
   r"f = \frac{64}{[Re]} = [ans|3].",
   "64/Re", wrong=["16/Re", "0.316/Re**0.25", "128/Re"], Re=[1600, 800, 2000, 1250])
NQ('fluids-d', 'pump power equation', 'kW', 0, 4662, "A turbine receives [Q|1] m^{3}/s of water under a net head of [H] m and is [eff]% efficient. What power does it deliver? Use 9.81 kN/m^{3}.",
   "The power available in flowing water is specific weight × flow × head. A turbine delivers that times its efficiency; a pump needs that divided by its efficiency.",
   "Water power = 9.81([Q|1])([H]) = [9.81*Q*H|0] kW. || Output = [eff/100|2] × [9.81*Q*H|0] = [ans|0] kW.",
   "eff/100*9.81*Q*H", Q=[12, 3.5, 40], H=[45, 120, 18], eff=[88, 90, 85])
NQ('fluids-d', 'drag force', 'N', 1, 1296, "A sign panel with an area of [A|1] m^{2} faces a [V|1] m/s flow of fluid with a density of [rho|1] kg/m^{3}. Its drag coefficient is [Cd|2]. What is the drag force on it?",
   "Drag on a body is the drag coefficient times the dynamic pressure, (1/2)(density)(velocity)^{2}, times the projected area facing the flow.",
   r"F = \frac{C_{D} (density) V^{2} A}{2} = \frac{[Cd|2]([rho|1])([V|1])^{2}([A|1])}{2} = [ans|1] N.",
   "Cd*rho*V*V*A/2", Cd=[1.2, 0.35, 1.0], V=[30, 25, 1.5], A=[2, 2.2, 0.8], rho=[1.2, 1.2, 1000])
# ================= Water resources and environmental =================
NQ('water-a', 'rational formula', '', 3, 0.525, "A drainage area has [A1|1] ha of pavement with a runoff coefficient of [C1|2] and [A2|1] ha of landscaping with a runoff coefficient of [C2|2]. What composite runoff coefficient should be used in the rational formula?",
   "For mixed surfaces the rational method uses an area-weighted runoff coefficient: the sum of each C times its area, divided by the total area.",
   r"C = \frac{[C1|2]([A1|1]) + [C2|2]([A2|1])}{[A1|1] + [A2|1]} = \frac{[C1*A1+C2*A2|3]}{[A1+A2|1]} = [ans|3].",
   "(C1*A1+C2*A2)/(A1+A2)", A1=[3, 1.2, 10], C1=[0.90, 0.85, 0.95], A2=[5, 2.8, 30], C2=[0.30, 0.20, 0.25])
NQ('water-a', 'unit hydrograph', 'm^{3}/s', 1, 117.5, "A catchment's unit hydrograph, for 1 cm of rainfall excess, peaks at [qu] m^{3}/s. A storm of the same duration produces [R|1] cm of excess, and base flow is [bf] m^{3}/s. What is the peak stream flow?",
   "A unit hydrograph is the direct runoff from one unit of rainfall excess. Runoff scales in proportion to the excess, and base flow is added afterwards.",
   "Peak direct runoff = [R|1] × [qu] = [R*qu|1] m^{3}/s. || Peak flow = [R*qu|1] + [bf] = [ans|1] m^{3}/s.",
   "R*qu+bf", qu=[45, 120, 18], R=[2.5, 1.8, 4], bf=[5, 10, 2])
NQ('water-a', '-', 'mm', 1, 51.0, "Three rain gauges represent [a1], [a2] and [a3] km^{2} of a catchment and record [p1], [p2] and [p3] mm of rain. What is the area-weighted average rainfall over the catchment?",
   "When gauges represent unequal areas, as in the Thiessen polygon method, the average rainfall weights each gauge by the area it represents.",
   r"P = \frac{[a1]([p1]) + [a2]([p2]) + [a3]([p3])}{[a1] + [a2] + [a3]} = \frac{[a1*p1+a2*p2+a3*p3]}{[a1+a2+a3]} = [ans|1] mm.",
   "(a1*p1+a2*p2+a3*p3)/(a1+a2+a3)", a1=[20, 15, 8], a2=[30, 25, 12], a3=[50, 10, 20], p1=[40, 22, 65], p2=[60, 30, 80], p3=[50, 18, 50])
NQ('water-a', '-', 'mm/h', 2, 35.75, "Infiltration follows f = f_{c} + (f_{0} - f_{c}) e^{-kt}, with an initial rate of [f0] mm/h, a final rate of [fc] mm/h and k = [k|1] per hour. What is the infiltration rate after [t|2] h?",
   "Horton's equation describes infiltration decaying exponentially from a high initial rate, when the soil is dry, toward a steady final rate as it wets up.",
   "f = [fc] + ([f0] - [fc]) e^{-[k|1] × [t|2]} = [fc] + [f0-fc] × [exp(-k*t)|4] = [ans|2] mm/h.",
   "fc+(f0-fc)*exp(-k*t)", f0=[80, 60, 120], fc=[10, 5, 20], k=[2, 1.5, 4], t=[0.5, 1, 0.25])
NQ('water-b', "Manning's equation; hydraulic radius", 'm', 3, 0.927, "A trapezoidal roadside channel has a bottom width of [b|1] m, side slopes of [z|1] horizontal to 1 vertical, and flows [y|1] m deep. What is its hydraulic radius?",
   "Hydraulic radius is flow area divided by wetted perimeter. For a trapezoid the area is (b + z y) y, and the wetted perimeter is the bottom plus two sloping sides, each y × square root of (1 + z^{2}) long.",
   r"A = ([b|1] + [z|1] × [y|1])([y|1]) = [(b+z*y)*y|3] m^{2}. || P = [b|1] + 2([y|1])\sqrt{1 + [z|1]^{2}} = [b+2*y*sqrt(1+z*z)|3] m. || R = \frac{[(b+z*y)*y|3]}{[b+2*y*sqrt(1+z*z)|3]} = [ans|3] m.",
   "(b+z*y)*y/(b+2*y*sqrt(1+z*z))", b=[3, 5, 1.5], y=[1.5, 2, 0.8], z=[2, 1.5, 3])
NQ('water-b', 'specific energy', 'm', 3, 1.519, "A rectangular channel carries [q|1] m^{3}/s per metre of width at a depth of [y|1] m. What is the specific energy of the flow? Use g = 9.81 m/s^{2}.",
   "Specific energy is the energy head measured from the channel bottom: depth plus velocity head. In a rectangular channel the velocity is the unit discharge divided by the depth.",
   r"V = \frac{[q|1]}{[y|1]} = [q/y|3] m/s. || E = [y|1] + \frac{[q/y|3]^{2}}{2(9.81)} = [y|1] + [(q/y)**2/(2*g)|3] = [ans|3] m.",
   "y+(q/y)**2/(2*g)", y=[1.2, 0.6, 2.0], q=[3, 2.4, 8])
NQ('water-b', "Manning's equation", 'L/s', 1, 137.3, "A [D] mm concrete storm drain (n = 0.013) on a slope of [S|3] flows exactly half full. What flow does it carry?",
   "A circular pipe flowing half full has the same hydraulic radius as when full, D / 4, because area and wetted perimeter are both halved. The velocity is therefore the full-pipe velocity and the flow is half the full-pipe flow.",
   r"R = [D/4000|4] m. V = \frac{1}{0.013}([D/4000|4])^{2/3}([S|3])^{1/2} = [(D/4000)**(2/3)*sqrt(S)/0.013|3] m/s. || Half area = \frac{π([D/1000|2])^{2}}{8} = [pi*(D/1000)**2/8|4] m^{2}. || Q = [(D/4000)**(2/3)*sqrt(S)/0.013|3] × [pi*(D/1000)**2/8|4] = [ans|1] L/s.",
   "(D/4000)**(2/3)*sqrt(S)/0.013*pi*(D/1000)**2/8*1000", D=[600, 450, 900], S=[0.002, 0.005, 0.001])
NQ('water-c', FM + '::affinity laws', 'm', 1, 46.9, "A centrifugal pump develops a head of [H1] m at [N1] rpm. Using the affinity laws, what head does it develop at [N2] rpm?",
   "For the same pump, flow varies with speed, head with speed squared and power with speed cubed.",
   r"H_{2} = H_{1} (\frac{N_{2}}{N_{1}})^{2} = [H1] (\frac{[N2]}{[N1]})^{2} = [ans|1] m.",
   "H1*(N2/N1)**2", wrong=["H1*N2/N1", "H1*(N2/N1)**3", "H1*(N1/N2)**2"], H1=[30, 45, 18], N1=[1200, 1750, 900], N2=[1500, 1450, 1200])
NQ('water-c', FM + '::NPSH', 'm', 2, 6.29, "A pump draws water from an open sump whose surface is [zs|1] m below the pump inlet. Atmospheric pressure is 101.3 kPa, the vapour pressure of the water is [pv|1] kPa and suction-pipe losses are [hL|1] m. What net positive suction head is available? Use 9.81 kN/m^{3}.",
   "NPSH available is the absolute head at the pump inlet above the vapour pressure head: atmospheric head, minus vapour pressure head, minus the suction lift, minus suction losses. It must exceed what the pump requires, or the pump cavitates.",
   r"\frac{101.3 - [pv|1]}{9.81} = [(101.3-pv)/9.81|3] m. || NPSH_{A} = [(101.3-pv)/9.81|3] - [zs|1] - [hL|1] = [ans|2] m.",
   "(101.3-pv)/9.81-zs-hL", pv=[2.3, 4.2, 7.4], zs=[3, 4.5, 2], hL=[0.8, 0.6, 1.5])
NQ('water-c', FM + '::pump power equation', '%', 1, 78.5, "A pump delivers [Q|3] m^{3}/s of water against a total head of [H] m while drawing [Pin] kW of shaft power. What is its efficiency? Use 9.81 kN/m^{3}.",
   "Efficiency is the power put into the water, specific weight × flow × head, divided by the shaft power supplied.",
   r"Water power = 9.81([Q|3])([H]) = [9.81*Q*H|2] kW. || Efficiency = \frac{[9.81*Q*H|2]}{[Pin]} × 100 = [ans|1]%.",
   "9.81*Q*H/Pin*100", Q=[0.08, 0.25, 0.012], H=[30, 18, 55], Pin=[30, 60, 9])
NQ('water-d', 'Hazen-Williams', 'm', 2, 5.01, "A water main is [L] m long and [D|2] m in diameter, with a Hazen-Williams coefficient of [C]. It carries [Q|2] m^{3}/s. Using h_{f} = 10.67 L Q^{1.852} / (C^{1.852} D^{4.87}) in SI units, what is the friction head loss?",
   "The Hazen-Williams equation is an empirical formula for water in pressure pipes. Head loss rises with flow to the 1.852 power and falls steeply with diameter, to the 4.87 power.",
   r"h_{f} = \frac{10.67([L])([Q|2])^{1.852}}{([C])^{1.852}([D|2])^{4.87}} = \frac{10.67([L])([Q**1.852|6])}{([C**1.852|1])([D**4.87|6])} = [ans|2] m.",
   "10.67*L*Q**1.852/(C**1.852*D**4.87)", L=[1000, 600, 2500], Q=[0.05, 0.02, 0.15], C=[120, 100, 130], D=[0.25, 0.15, 0.40])
NQ('water-d', 'head loss', 'L/s', 1, 73.4, "Two parallel pipes of equal length and friction factor join the same two junctions. Their diameters are [D1] mm and [D2] mm, and together they carry [Q] L/s. How much flows in the [D1] mm pipe?",
   "Pipes in parallel have the same head loss. With the Darcy-Weisbach equation and equal length and friction factor, each pipe's flow is proportional to its diameter to the 5/2 power.",
   r"D^{2.5}: [D1**2.5|0] and [D2**2.5|0]. || Q_{1} = [Q] × \frac{[D1**2.5|0]}{[D1**2.5|0] + [D2**2.5|0]} = [ans|1] L/s.",
   "Q*D1**2.5/(D1**2.5+D2**2.5)", D1=[300, 400, 150], D2=[200, 250, 100], Q=[100, 250, 30])
NQ('water-d', 'Bernoulli equation', 'kPa', 1, 233.2, "The pressure at point A in a water main is [pA] kPa. Point B, downstream, is [dz] m higher than A, and the friction loss between them is [hf|1] m. The pipe size is constant. What is the pressure at B? Use 9.81 kN/m^{3}.",
   "With a constant pipe size the velocity head cancels in the energy equation. Pressure head at B is the pressure head at A minus the rise in elevation and minus the head lost to friction.",
   "p_{B} = [pA] - 9.81([dz] + [hf|1]) = [pA] - [9.81*(dz+hf)|1] = [ans|1] kPa.",
   "pA-9.81*(dz+hf)", pA=[400, 550, 300], dz=[12, 25, 8], hf=[5, 8.5, 3])
NQ('water-e', 'weir formulas', 'm^{3}/s', 1, 80.8, "A spillway crest is [L] m long and has a discharge coefficient of 2.2 in SI units. What does it discharge under a head of [H|1] m, using Q = C L H^{3/2}?",
   "A spillway crest behaves as a weir: discharge is proportional to the crest length and to the head raised to the 3/2 power. Doubling the head nearly triples the flow.",
   "Q = 2.2([L])([H|1])^{1.5} = 2.2 × [L] × [H**1.5|4] = [ans|1] m^{3}/s.",
   "2.2*L*H**1.5", L=[20, 35, 12], H=[1.5, 2.2, 0.9])
NQ('water-e', FM + '::forces on submerged surfaces', '', 2, 3.19, "A concrete gravity dam with a rectangular section is [b|1] m wide and [h] m high, with water level with its top on one side. Concrete weighs 23.5 kN/m^{3} and uplift is ignored. What is the factor of safety against overturning about the downstream toe?",
   "Overturning is a moment check about the toe. The water thrust, the area of the triangular pressure diagram, acts one third of the depth above the base. The dam's weight acts at half its width from the toe.",
   r"Resisting moment = 23.5([b|1])([h]) × \frac{[b|1]}{2} = [23.5*b*h*b/2|0] kN·m/m. || Overturning moment = \frac{1}{2}(9.81)([h])^{2} × \frac{[h]}{3} = [9.81*h**3/6|0] kN·m/m. || FS = \frac{[23.5*b*h*b/2|0]}{[9.81*h**3/6|0]} = [ans|2].",
   "23.5*b*h*b/2/(9.81*h**3/6)", b=[4, 5, 3.5], h=[6, 9, 5])
NQ('water-f', '-', 'm^{3}', 0, 600, "A stormwater treatment facility must capture the runoff from the first [P] mm of rain on a [A|1] ha site whose volumetric runoff coefficient is [Rv|2]. What water quality volume is required?",
   "The water quality volume is the depth of rain to be captured, times the fraction that runs off, times the drainage area. One hectare is 10,000 m^{2}.",
   "Volume = [P/1000|3] m × [Rv|2] × [A*10000|0] m^{2} = [ans|0] m^{3}.",
   "P/1000*Rv*A*10000", P=[25, 30, 13], Rv=[0.60, 0.45, 0.80], A=[4, 10, 1.5])
NQ('water-f', CE + '::rational formula', 'm^{3}/s', 3, 0.833, "Local rainfall intensity is i = 2,500 / (t + 15) mm/h, with t in minutes. A [A] ha site with a runoff coefficient of [C|2] has a time of concentration of [tc] min. Using Q = C i A / 360 (i in mm/h, A in ha), what is the peak runoff?",
   "The rational method takes the storm duration equal to the time of concentration, because that is the shortest storm for which the whole site contributes at once. Longer times of concentration mean lower intensities.",
   r"i = \frac{2,500}{[tc] + 15} = [2500/(tc+15)|2] mm/h. || Q = \frac{[C|2]([2500/(tc+15)|2])([A])}{360} = [ans|3] m^{3}/s.",
   "C*2500/(tc+15)*A/360", C=[0.70, 0.50, 0.90], A=[6, 25, 2], tc=[20, 45, 10])
NQ('water-f', '-', '%', 0, 76, "Runoff passes through two stormwater treatment devices in series. The first removes [r1]% of suspended solids and the second removes [r2]% of what reaches it. What is the overall removal?",
   "Removals in series do not add. The second device only sees what the first lets through, so multiply the fractions that pass and subtract from one.",
   "Fraction passing = (1 - [r1/100|2])(1 - [r2/100|2]) = [(1-r1/100)*(1-r2/100)|2]. || Overall removal = 1 - [(1-r1/100)*(1-r2/100)|2] = [ans|0]%.",
   "(1-(1-r1/100)*(1-r2/100))*100", wrong=["r1+r2", "(r1+r2)/2", "r1*r2/100"], r1=[60, 80, 50], r2=[40, 50, 30])
NQ('water-g', '-', 'm', 2, 101.92, "A sewer leaves a manhole at an invert elevation of [e0|2] m and runs [L] m at a slope of [S|2]% to the next manhole. What is the invert elevation where it arrives?",
   "A gravity sewer falls at its design slope. The drop is slope, as a decimal, times the run.",
   r"Drop = \frac{[S|2]}{100} × [L] = [S/100*L|2] m. || Invert = [e0|2] - [S/100*L|2] = [ans|2] m.",
   "e0-S/100*L", tol=0.0005, e0=[102.40, 56.85, 231.10], S=[0.4, 0.25, 1.2], L=[120, 100, 75])
NQ('water-h', 'well drawdown', 'm^{3}/day', 0, 1637, "A well fully penetrates a confined aquifer with a transmissivity of [T] m^{2}/day. At steady state, the piezometric level at [r2] m from the well is [dh|1] m higher than at [r1] m. What is the pumping rate?",
   "For steady radial flow to a well in a confined aquifer, Q = 2π T (h_{2} - h_{1}) / ln(r_{2} / r_{1}). Transmissivity is hydraulic conductivity times aquifer thickness.",
   r"Q = \frac{2π([T])([dh|1])}{ln([r2] / [r1])} = \frac{[2*pi*T*dh|1]}{[log(r2/r1)|4]} = [ans|0] m^{3}/day.",
   "2*pi*T*dh/log(r2/r1)", T=[500, 250, 1200], dh=[1.2, 2.0, 0.6], r1=[10, 5, 20], r2=[100, 60, 150])
NQ('water-h', '-', 'm^{3}', 0, 900000, "The water table in an unconfined aquifer with a specific yield of [Sy|2] falls by [dh|1] m over an area of [A|1] km^{2}. What volume of water has drained from storage?",
   "Specific yield is the volume of water an unconfined aquifer releases per unit area per unit drop of the water table. It is less than the porosity because some water stays held on the grains.",
   "Volume = [Sy|2] × [A*1e6|0] m^{2} × [dh|1] m = [ans|0] m^{3}.",
   "Sy*A*1e6*dh", Sy=[0.15, 0.22, 0.08], A=[2, 0.5, 12], dh=[3, 1.5, 0.8])
NQ('water-h', "Darcy's law", 'days', 0, 1875, "Groundwater flows through sand with a hydraulic conductivity of [K] m/day and an effective porosity of [n|2] under a hydraulic gradient of [i|3]. How long does water take to travel [L] m?",
   "Darcy's law gives the flow per unit of total area. Water moves only through the pores, so the actual (seepage) velocity is the Darcy velocity divided by the effective porosity.",
   r"Seepage velocity = \frac{[K]([i|3])}{[n|2]} = [K*i/n|4] m/day. || Time = \frac{[L]}{[K*i/n|4]} = [ans|0] days.",
   "L*n/(K*i)", L=[500, 200, 1200], n=[0.30, 0.25, 0.35], K=[20, 8, 50], i=[0.004, 0.01, 0.002])
NQ('water-i', '-', 'mg/L', 2, 5.11, "A stream flowing at [Qr|1] m^{3}/s with a pollutant concentration of [Cr|1] mg/L receives a discharge of [Qw|1] m^{3}/s at [Cw] mg/L. What is the concentration just after complete mixing?",
   "Mass is conserved at a mixing point: the load after mixing is the sum of the loads coming in. Concentration is that total load divided by the total flow.",
   r"C = \frac{[Qr|1]([Cr|1]) + [Qw|1]([Cw])}{[Qr|1] + [Qw|1]} = \frac{[Qr*Cr+Qw*Cw|1]}{[Qr+Qw|1]} = [ans|2] mg/L.",
   "(Qr*Cr+Qw*Cw)/(Qr+Qw)", Qr=[8, 25, 3.5], Cr=[2, 1.5, 3], Qw=[1, 2, 0.5], Cw=[30, 25, 40])
NQ('water-i', '-', 'mg/L as CaCO_{3}', 1, 100, "A water sample contains [h] mg/L of bicarbonate (HCO_{3}^{-}, equivalent weight 61). Express this as mg/L as CaCO_{3} (equivalent weight 50).",
   "Concentrations are put on a common basis by converting to calcium carbonate equivalents: multiply by 50 and divide by the ion's own equivalent weight.",
   r"[h] × \frac{50}{61} = [ans|1] mg/L as CaCO_{3}.",
   "h*50/61", h=[122, 183, 85])
NQ('water-i', '-', 'kg/day', 0, 5000, "A treatment plant receives [Q] m^{3}/day of wastewater with a BOD of [C] mg/L. What is the BOD loading?",
   "Mass loading is flow times concentration. Since 1 mg/L is 1 g/m^{3}, multiplying m^{3}/day by mg/L gives g/day; divide by 1,000 for kg/day.",
   r"Loading = \frac{[Q]([C])}{1,000} = [ans|0] kg/day.",
   "Q*C/1000", Q=[20000, 7500, 48000], C=[250, 180, 30])
NQ('water-i', '-', '', 2, 5.6, "A solution has a hydrogen ion concentration of [a|1] × 10^{-[b]} mol/L. What is its pH?",
   "pH is the negative base-10 logarithm of the hydrogen ion concentration in mol/L. Each unit of pH is a factor of ten in concentration.",
   "pH = -log([a|1] × 10^{-[b]}) = [b] - log([a|1]) = [b] - [log10(a)|3] = [ans|2].",
   "b-log10(a)", a=[2.5, 4.0, 6.3], b=[6, 9, 4])
NQ('water-j', '-', 'mg/L', 0, 224, "In a suspended solids test, a filter weighs [Wi|4] g before and [Wf|4] g after filtering and drying a [V] mL sample. What is the total suspended solids concentration?",
   "Total suspended solids is the dry mass caught on the filter divided by the volume filtered. Convert grams to milligrams and millilitres to litres.",
   r"Mass retained = [Wf|4] - [Wi|4] = [Wf-Wi|4] g = [(Wf-Wi)*1000|1] mg. || TSS = \frac{[(Wf-Wi)*1000|1]}{[V/1000|3]} = [ans|0] mg/L.",
   "(Wf-Wi)*1000/(V/1000)", Wi=[1.5420, 1.2085, 0.9860], Wf=[1.5532, 1.2139, 0.9915], V=[50, 100, 25])
NQ('water-j', 'Safety::noise', 'dB', 1, 78.0, "Construction equipment produces a sound level of [L1] dB at [r1] m. Treating it as a point source in open ground, what is the level at [r2] m?",
   "Sound from a point source spreads over a sphere, so its intensity falls with distance squared. In decibels that is a drop of 20 log(r_{2} / r_{1}), about 6 dB for each doubling of distance.",
   r"L_{2} = [L1] - 20 log(\frac{[r2]}{[r1]}) = [L1] - [20*log10(r2/r1)|2] = [ans|1] dB.",
   "L1-20*log10(r2/r1)", L1=[90, 85, 100], r1=[10, 15, 5], r2=[40, 60, 50])
NQ('water-k', EN + '::activated sludge', 'per day', 3, 0.32, "An aeration tank of [V] m^{3} holds mixed liquor at [X] mg/L and receives [Q] m^{3}/day of wastewater with a BOD of [S0] mg/L. What is the food-to-microorganism ratio?",
   "The food-to-microorganism ratio compares the daily mass of BOD fed with the mass of microorganisms in the tank: Q S_{0} / (V X).",
   r"F/M = \frac{[Q]([S0])}{[V]([X])} = [ans|3] per day.",
   "Q*S0/(V*X)", Q=[10000, 4000, 25000], S0=[200, 250, 150], V=[2500, 1500, 8000], X=[2500, 2000, 3000])
NQ('water-k', EN + '::solids residence time', 'days', 2, 7.81, "An aeration tank of [V] m^{3} holds mixed liquor at [X] mg/L. Sludge is wasted at [Qw] m^{3}/day with a concentration of [Xw] mg/L, and solids lost in the effluent are negligible. What is the solids residence time?",
   "Solids residence time, or sludge age, is the mass of solids in the system divided by the mass leaving it each day.",
   r"SRT = \frac{V X}{Q_{w} X_{w}} = \frac{[V]([X])}{[Qw]([Xw])} = [ans|2] days.",
   "V*X/(Qw*Xw)", V=[2500, 4000, 1200], X=[2500, 3000, 2200], Qw=[100, 150, 40], Xw=[8000, 10000, 7500])
NQ('water-k', '-', 'm/h', 2, 8.33, "A rapid sand filter with a surface area of [A] m^{2} treats [Q] m^{3}/day. What is its filtration rate?",
   "Filtration rate is flow divided by filter surface area, a velocity. Convert days to hours when the rate is wanted in m/h.",
   r"Rate = \frac{[Q]}{[A] × 24} = [ans|2] m/h.",
   "Q/A/24", Q=[12000, 30000, 4800], A=[60, 125, 40])
NQ('water-k', EN + "::Stokes' law", 'mm/s', 3, 2.248, "A spherical particle [d|2] mm in diameter with a density of [rp] kg/m^{3} settles in water (density 1,000 kg/m^{3}, viscosity 0.001 Pa·s). Using Stokes' law, what is its settling velocity?",
   "For small particles in laminar conditions, the settling velocity is g (particle density - fluid density) d^{2} / (18 × viscosity). It depends on diameter squared, so fine particles settle very slowly.",
   r"v = \frac{9.81([rp] - 1,000)([d/1000|5])^{2}}{18(0.001)} = [g*(rp-1000)*(d/1000)**2/0.018|6] m/s = [ans|3] mm/s.",
   "g*(rp-1000)*(d/1000)**2/(18*0.001)*1000", d=[0.05, 0.02, 0.08], rp=[2650, 2650, 1200])
NQ('water-k', '-', 'min', 1, 50, "Disinfection requires a CT value of [CT] mg·min/L. The chlorine residual is [C|1] mg/L. What contact time is needed?",
   "CT is disinfectant concentration times contact time. A given level of inactivation needs a fixed CT, so a lower residual needs a proportionally longer contact time.",
   r"t = \frac{[CT]}{[C|1]} = [ans|1] min.",
   "CT/C", CT=[40, 90, 12], C=[0.8, 1.5, 0.5])
# ================= Surveying =================
NQ('surveying-a', '-', 'm', 4, 0.0435, "A steel tape, correct at 20 °C, is used to measure [L] m at [T] °C. The coefficient of thermal expansion of steel is 11.6 × 10^{-6} per °C. What correction should be applied to the measured length?",
   "A warm tape is longer than its marks say, so it reads short and the correction is positive; a cold tape reads long and the correction is negative. The size is (coefficient)(temperature difference)(length).",
   "Correction = 11.6 × 10^{-6} × ([T] - 20) × [L] = [ans|4] m.",
   "11.6e-6*(T-20)*L", L=[250, 480, 125], T=[35, 5, 42])
NQ('surveying-a', '-', 'seconds', 0, -10, "The measured interior angles of a closed [n]-sided traverse add up to [exc]\" more than the geometric total. If the error is shared equally, what correction is applied to each angle?",
   "The interior angles of a closed polygon must total (n - 2) × 180°. The misclosure is shared equally among the angles, with the opposite sign.",
   r"Correction = -\frac{[exc]}{[n]} = [ans|0]\" per angle.",
   "-exc/n", n=[5, 6, 4, 8], exc=[50, 36, 48, 56])
NQ('surveying-a', '-', '°', 1, 247.5, "A line has an azimuth of [az|1]°. What is its back azimuth?",
   "The back azimuth is the direction of the same line seen from its other end. It differs from the forward azimuth by 180°: add 180° if the azimuth is less than 180°, otherwise subtract.",
   "Back azimuth = [az|1]° [sgn] 180° = [ans|1]°.",
   "(az+180)%360", wrong=["360-az", "(az+90)%360", "(az+270)%360"], az=[67.5, 215, 301, 142.5], sgn=["+", "-", "-", "+"])
NQ('surveying-b', "Simpson's 1/3 rule", 'm^{2}', 2, 176.67, "Offsets from a baseline to a curved boundary, measured every [dx] m, are [o0|1], [o1|1], [o2|1], [o3|1] and [o4|1] m. Using Simpson's 1/3 rule, what is the area between the baseline and the boundary?",
   "Simpson's 1/3 rule fits parabolas through the offsets in pairs of intervals, so it needs an even number of intervals. The end offsets count once, odd-numbered interior offsets four times and even-numbered interior offsets twice.",
   r"A = \frac{[dx]}{3}([o0|1] + 4([o1|1]) + 2([o2|1]) + 4([o3|1]) + [o4|1]) = \frac{[dx]}{3}([o0+4*o1+2*o2+4*o3+o4|1]) = [ans|2] m^{2}.",
   "dx/3*(o0+4*o1+2*o2+4*o3+o4)", dx=[10, 5, 20], o0=[3, 1.2, 8], o1=[5, 2.5, 11], o2=[6, 3.1, 13], o3=[4, 2.8, 10], o4=[2, 1.5, 6])
NQ('surveying-b', 'area formulas', 'm^{2}', 1, 8400, "A triangular parcel has sides of [a], [b] and [c] m. What is its area?",
   "With three sides known and no angles, use Heron's formula: area = square root of s(s - a)(s - b)(s - c), where s is half the perimeter.",
   r"s = \frac{[a] + [b] + [c]}{2} = [(a+b+c)/2|1] m. || Area = \sqrt{[(a+b+c)/2|1]([(a+b+c)/2-a|1])([(a+b+c)/2-b|1])([(a+b+c)/2-c|1])} = [ans|1] m^{2}.",
   "sqrt((a+b+c)/2*((a+b+c)/2-a)*((a+b+c)/2-b)*((a+b+c)/2-c))", a=[130, 60, 85], b=[140, 75, 120], c=[150, 95, 140])
NQ('surveying-b', '-', 'acres', 3, 3.099, "A rectangular lot measures [L|1] ft by [W|1] ft. What is its area in acres?",
   "An acre is 43,560 square feet. Work out the area in square feet, then divide.",
   r"Area = [L|1] × [W|1] = [L*W|0] ft^{2}. || \frac{[L*W|0]}{43,560} = [ans|3] acres.",
   "L*W/43560", units='USCS', L=[300, 660, 208.7], W=[450, 330, 208.7])
NQ('surveying-c', '-', 'm^{3}', 0, 5682, "An embankment needs [Vf] m^{3} of compacted fill. The borrow material shrinks by [sh]% when compacted. What bank volume must be excavated from the borrow pit?",
   "Soil compacted in a fill usually occupies less volume than it did in the ground. Divide the compacted volume by (1 - shrinkage) to find the bank volume needed.",
   r"Bank volume = \frac{[Vf]}{1 - [sh/100|2]} = [ans|0] m^{3}.",
   "Vf/(1-sh/100)", Vf=[5000, 12000, 800], sh=[12, 15, 8])
NQ('surveying-c', 'earthwork formulas', 'm^{2}', 2, 42.5, "A roadway cut on level ground has a base width of [b|1] m, a centreline depth of [d|1] m and side slopes of [s|1] horizontal to 1 vertical. What is the cross-sectional area of the cut?",
   "A level section is a trapezoid: the base width plus a triangle on each side whose width is the side slope times the depth. Area = d(b + s d).",
   "A = [d|1]([b|1] + [s|1] × [d|1]) = [d|1] × [b+s*d|2] = [ans|2] m^{2}.",
   "d*(b+s*d)", b=[12, 10, 7.5], d=[2.5, 1.8, 3.2], s=[2, 3, 1.5])
NQ('surveying-c', '-', 'm^{3}', 1, 628.3, "A conical stockpile of aggregate has a base diameter of [d] m and a height of [h|1] m. What is its volume?",
   "The volume of a cone is one third of the base area times the height.",
   r"V = \frac{π([d/2|1])^{2}([h|1])}{3} = [ans|1] m^{3}.",
   "pi*(d/2)**2*h/3", d=[20, 12, 35], h=[6, 4.5, 9])
NQ('surveying-d', 'latitude; departure', 'm', 2, 500, "Point A is at N [NA|2], E [EA|2] and point B is at N [NB|2], E [EB|2], in metres. What is the horizontal distance from A to B?",
   "The difference in northings is the latitude of the line and the difference in eastings is its departure. The distance is the hypotenuse.",
   r"Latitude = [NB-NA|2] m, departure = [EB-EA|2] m. || Distance = \sqrt{[NB-NA|2]^{2} + [EB-EA|2]^{2}} = [ans|2] m.",
   "hypot(NB-NA, EB-EA)", tol=0.001, NA=[1000, 5250.5, 820], EA=[2000, 3100.2, 1460], NB=[1300, 5010.5, 1000], EB=[2400, 3280.2, 1535])
NQ('surveying-d', 'latitude; departure', '', 0, 20000, "A closed traverse [per] m long has a misclosure of [eL|3] m in latitude and [eD|3] m in departure. Its relative precision is 1 in N. What is N?",
   "The linear misclosure is the hypotenuse of the latitude and departure misclosures. Relative precision is the perimeter divided by that misclosure, written as 1 in N.",
   r"Misclosure = \sqrt{[eL|3]^{2} + [eD|3]^{2}} = [hypot(eL,eD)|4] m. || N = \frac{[per]}{[hypot(eL,eD)|4]} = [ans|0].",
   "per/hypot(eL,eD)", eL=[0.03, 0.06, 0.012], eD=[0.04, 0.08, 0.035], per=[1000, 850, 925])
NQ('surveying-d', '-', 'm', 2, 1519.77, "A ground distance of [d|2] m is to be reduced to the state plane grid. The combined scale factor is [cf|5]. What is the grid distance?",
   "State plane coordinates lie on a projection surface. The combined factor allows for both the elevation of the ground above the ellipsoid and the scale of the projection at that place: grid = ground × combined factor.",
   "Grid distance = [d|2] × [cf|5] = [ans|2] m.",
   "d*cf", tol=0.00003, d=[1520, 2640.5, 825.25], cf=[0.99985, 0.99992, 1.00012])
NQ('surveying-e', '-', 'm', 3, 98.43, "A level run starts on a benchmark at [BM|2] m. The readings are: backsight [b1|3], foresight [f1|3] on a turning point, then backsight [b2|3] on the turning point and foresight [f2|3] on the new point. What is the new point's elevation?",
   "Each set-up adds the backsight to get the height of instrument and subtracts the foresight to get the next elevation. Over the whole run, elevation = start + sum of backsights - sum of foresights.",
   "Elevation = [BM|2] + ([b1|3] + [b2|3]) - ([f1|3] + [f2|3]) = [BM|2] + [b1+b2|3] - [f1+f2|3] = [ans|3] m.",
   "BM+b1+b2-f1-f2", tol=0.0002, BM=[100, 45.72, 212.35], b1=[1.52, 2.105, 0.845], f1=[2.31, 0.672, 2.910], b2=[0.98, 1.980, 1.215], f2=[1.76, 1.254, 3.005])
NQ('surveying-e', '-', 'm', 4, 0.0972, "Using c = 0.0675 K^{2}, with c in metres and K in kilometres, what is the combined correction for earth curvature and refraction on a level sight [K|1] km long?",
   "Over a long sight the level surface curves away below the line of sight, while refraction bends the line slightly back down. The combined effect grows with the square of the distance, which is why backsight and foresight distances are kept equal.",
   "c = 0.0675([K|1])^{2} = [ans|4] m.",
   "0.0675*K*K", K=[1.2, 0.8, 2.5])
NQ('surveying-e', '-', 'm', 2, 141.25, "A profile grade line passes through elevation [e0|2] m and runs at a grade of [gr|1]%. What is its elevation [dL] m farther along?",
   "A grade in percent is metres of rise per 100 m of run; a negative grade falls. Elevation change = grade / 100 × distance.",
   r"Elevation = [e0|2] + \frac{[gr|1]}{100}([dL]) = [e0|2] + ([gr/100*dL|2]) = [ans|2] m.",
   "e0+gr/100*dL", tol=0.0005, e0=[150, 82.4, 310.75], gr=[-2.5, 1.8, 4.0], dL=[350, 225, 480])
NQ('surveying-e', 'trigonometry', 'm', 2, 9.21, "A total station with a height of instrument of [HI|2] m measures a slope distance of [S|1] m at a vertical angle of +[va|2]° to a prism on a [rod|2] m rod. How much higher is the ground at the rod than the ground at the instrument?",
   "The vertical component of the slope distance is S sin(vertical angle). Add the instrument height, because the measurement starts above the ground, and subtract the rod height, because it ends above the ground.",
   "Difference = [S|1] sin [va|2]° + [HI|2] - [rod|2] = [S*sin(rad(va))|3] + [HI|2] - [rod|2] = [ans|2] m.",
   "S*sin(rad(va))+HI-rod", S=[85.3, 142.0, 60.5], va=[6.5, 3.25, 12], HI=[1.55, 1.48, 1.62], rod=[2.00, 1.48, 1.30])
if __name__ == '__main__': run('f4')
