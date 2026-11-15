"""Further question types: transportation, construction, engineering economics and ethics. See author_fx.py for the format."""
from author_fx import *
CE, EC = 'Civil Engineering', 'Engineering Economics'
# ================= Transportation =================
NQ('transport-a', 'horizontal curves', 'ft', 2, 48.25, "A horizontal curve has a radius of [R] ft and a deflection angle of [I]°. What is its middle ordinate?",
   "The middle ordinate is the distance from the midpoint of the long chord to the midpoint of the curve: M = R(1 - cos(I / 2)). It sets how far an obstruction on the inside of the curve must be kept back for sight distance.",
   r"M = [R](1 - cos [I/2|1]°) = [R](1 - [cos(rad(I/2))|5]) = [ans|2] ft.",
   "R*(1-cos(rad(I/2)))", units='USCS', R=[800, 1200, 500], I=[40, 24, 60])
NQ('transport-a', 'vertical curves', 'ft', 2, 245.5, "A sag vertical curve [L] ft long joins a [g1|1]% grade to a +[g2|1]% grade. The PVC elevation is [e0|2] ft. What is the elevation of the low point?",
   "The low point is where the grade along the curve passes through zero, at x = -g_{1} L / (g_{2} - g_{1}) from the PVC. Its elevation follows from the parabola y = y_{PVC} + g_{1} x + ((g_{2} - g_{1}) / 2L) x^{2}, with grades as decimals.",
   r"x = \frac{-([g1|1])([L])}{[g2|1] - ([g1|1])} = [-g1*L/(g2-g1)|1] ft. || Elevation = [e0|2] + \frac{[g1|1]}{100}([-g1*L/(g2-g1)|1]) + \frac{[g2-g1|1] / 100}{2([L])}([-g1*L/(g2-g1)|1])^{2} = [ans|2] ft.",
   "e0+g1/100*(-g1*L/(g2-g1))+(g2-g1)/100/(2*L)*(-g1*L/(g2-g1))**2", tol=0.001, units='USCS', g1=[-3, -2, -4], g2=[2, 3, 1.5], L=[500, 400, 660], e0=[250, 612.4, 88.2])
NQ('transport-a', 'superelevation', '%', 2, 2.67, "A curve of radius [R] ft is designed for [V] mph with a side friction factor of [f|2]. Using 0.01e + f = V^{2} / (15R), what superelevation rate is required?",
   "On a curve, superelevation and side friction together supply the inward force a vehicle needs. Whatever V^{2} / (15R) calls for beyond the friction factor has to come from superelevation.",
   r"\frac{V^{2}}{15R} = \frac{[V]^{2}}{15([R])} = [V*V/(15*R)|4]. || e = ([V*V/(15*R)|4] - [f|2]) × 100 = [ans|2]%.",
   "(V*V/(15*R)-f)*100", units='USCS', V=[50, 60, 40], R=[1000, 1200, 500], f=[0.14, 0.12, 0.16])
NQ('transport-a', 'stopping sight distance', 'ft', 1, 454.5, "A vehicle travels at [V] mph on a [G]% grade (negative is downhill). Using a 2.5 s perception-reaction time and a deceleration of 11.2 ft/s^{2}, what is the stopping sight distance?",
   "Stopping sight distance is reaction distance plus braking distance: 1.47 V t + V^{2} / (30(a / 32.2 ± G)). A downgrade lengthens braking because gravity works against the brakes; an upgrade shortens it.",
   r"Reaction distance = 1.47([V])(2.5) = [1.47*V*2.5|1] ft. || Braking distance = \frac{[V]^{2}}{30(\frac{11.2}{32.2} + ([G/100|2]))} = [V*V/(30*(11.2/32.2+G/100))|1] ft. || SSD = [ans|1] ft.",
   "1.47*V*2.5+V*V/(30*(11.2/32.2+G/100))", units='USCS', V=[50, 65, 40], G=[-4, 3, -6])
NQ('transport-b', 'structural number', 'in', 2, 14.29, "A flexible pavement needs a structural number of [SN|1]. It will have [D1|1] in of asphalt with a layer coefficient of 0.44, on a granular base with a layer coefficient of [a2|2] and a drainage coefficient of [m2|1]. How thick must the base be?",
   "The AASHTO structural number is the sum, over the layers, of layer coefficient × thickness × drainage coefficient. Subtract what the asphalt provides and divide the remainder by the base's coefficient times its drainage coefficient.",
   r"Asphalt provides 0.44([D1|1]) = [0.44*D1|2]. || D_{2} = \frac{[SN|1] - [0.44*D1|2]}{[a2|2]([m2|1])} = [ans|2] in.",
   "(SN-0.44*D1)/(a2*m2)", units='USCS', SN=[4.2, 3.6, 5.0], D1=[5, 4, 6.5], a2=[0.14, 0.13, 0.14], m2=[1.0, 0.9, 1.1])
NQ('transport-b', '-', 'ESALs', 0, 157680, "A road carries [adt] vehicles per day, of which [pt]% are trucks with an average truck factor of [tf|1] ESALs per truck. Half the traffic uses the design lane. How many ESALs does the design lane receive in one year?",
   "Pavement damage is counted in equivalent 18-kip single axle loads. Yearly ESALs = daily traffic × truck share × truck factor × 365 × the share in the design lane. Cars are ignored because their damage is negligible.",
   "ESALs = [adt] × [pt/100|2] × [tf|1] × 365 × 0.5 = [ans|0].",
   "adt*pt/100*tf*365*0.5", units='USCS', adt=[8000, 22000, 3500], pt=[12, 8, 20], tf=[0.9, 1.2, 0.6])
NQ('transport-b', '-', '', 3, 3.16, "Using the fourth-power rule, how many passes of an 18-kip single axle do the same pavement damage as one pass of a [W] kip single axle?",
   "Pavement damage rises very steeply with axle load, roughly with the fourth power of the load ratio. A modest overload therefore does several times the damage, which is why weight limits matter.",
   r"Equivalency = (\frac{[W]}{18})^{4} = [ans|3].",
   "(W/18)**4", units='USCS', W=[24, 30, 12])
NQ('transport-c', 'traffic flow relationships', 'mph', 2, 40, "Three vehicles cross a short road section at [s1], [s2] and [s3] mph. What is the space mean speed?",
   "Space mean speed is the harmonic mean of the individual speeds: the number of vehicles divided by the sum of 1 / speed. It is the speed that ties flow to density, and it is never more than the arithmetic (time) mean.",
   r"Space mean speed = \frac{3}{\frac{1}{[s1]} + \frac{1}{[s2]} + \frac{1}{[s3]}} = \frac{3}{[1/s1+1/s2+1/s3|5]} = [ans|2] mph. The arithmetic mean is [(s1+s2+s3)/3|2] mph.",
   "3/(1/s1+1/s2+1/s3)", units='USCS', s1=[30, 45, 25], s2=[40, 50, 35], s3=[60, 65, 50])
NQ('transport-c', 'traffic flow relationships', 'veh/h', 0, 1500, "Vehicles in a lane pass a point with an average time headway of [h|1] s. What is the flow rate?",
   "Flow is the reciprocal of the average time headway. With the headway in seconds, flow in vehicles per hour is 3,600 divided by it.",
   r"Flow = \frac{3,600}{[h|1]} = [ans|0] veh/h.",
   "3600/h", h=[2.4, 1.8, 4.5])
NQ('transport-c', '-', '', 3, 0.875, "A signalised lane group has a saturation flow rate of [s] veh/h and receives [gr] s of effective green in a [C] s cycle. The demand is [v] veh/h. What is its volume-to-capacity ratio?",
   "Capacity at a signal is the saturation flow rate times the share of the cycle that is effectively green. The volume-to-capacity ratio compares demand with that; values near or above 1 mean the approach is saturated.",
   r"Capacity = [s] × \frac{[gr]}{[C]} = [s*gr/C|0] veh/h. || v/c = \frac{[v]}{[s*gr/C|0]} = [ans|3].",
   "v/(s*gr/C)", v=[700, 950, 420], s=[1800, 1900, 1750], gr=[40, 55, 24], C=[90, 100, 80])
NQ('transport-c', 'traffic flow relationships', 'mph', 2, 15, "Traffic approaches a stopped queue at a flow of [q1] veh/h and a density of [k1] veh/mi. In the queue the density is [kj] veh/mi and the flow is zero. How fast does the back of the queue move upstream?",
   "The boundary between two traffic states is a shock wave. Its speed is the change in flow divided by the change in density between the states; a negative value means it travels upstream.",
   r"Wave speed = \frac{0 - [q1]}{[kj] - [k1]} = [-q1/(kj-k1)|2] mph, so the back of the queue moves upstream at [ans|2] mph.",
   "q1/(kj-k1)", units='USCS', q1=[1800, 1500, 1200], k1=[30, 25, 40], kj=[150, 180, 200])
NQ('transport-d', 'yellow interval', 's', 2, 1.82, "An intersection is [W] ft wide between stop line and far-side conflict point, and the design vehicle is 20 ft long. Approach speed is [v|1] ft/s. Using r = (W + L) / v, what all-red clearance interval is needed?",
   "The all-red interval gives a vehicle that entered at the end of yellow time to clear the intersection. It must cover the crossing width plus the vehicle's own length at the approach speed.",
   r"r = \frac{[W] + 20}{[v|1]} = [ans|2] s.",
   "(W+20)/v", units='USCS', W=[60, 84, 48], v=[44, 51.3, 36.7])
NQ('transport-d', '-', 's', 1, 57.5, "A signal has a total lost time of [L] s per cycle, and the sum of the critical flow ratios is [Y|2]. Using Webster's formula C = (1.5L + 5) / (1 - Y), what is the optimum cycle length?",
   "Webster's formula balances two effects: short cycles waste a large share of time on lost time at each phase change, and long cycles make stopped vehicles wait. As the critical flow ratios approach 1 the best cycle grows without limit.",
   r"C = \frac{1.5([L]) + 5}{1 - [Y|2]} = \frac{[1.5*L+5|1]}{[1-Y|2]} = [ans|1] s.",
   "(1.5*L+5)/(1-Y)", L=[12, 16, 10], Y=[0.60, 0.72, 0.55])
NQ('transport-d', '-', 's', 1, 20, "A crosswalk is [W] ft long. Using a walking speed of 3.5 ft/s, what pedestrian clearance time is needed?",
   "The pedestrian clearance time lets someone who steps off the kerb at the end of the walk interval finish crossing. It is the crossing distance divided by the walking speed; the MUTCD uses 3.5 ft/s.",
   r"Clearance time = \frac{[W]}{3.5} = [ans|1] s.",
   "W/3.5", wrong=["W/4", "W/3", "W/2.5"], units='USCS', W=[70, 56, 98])
NQ('transport-e', 'crash reduction', 'crashes', 2, 5.5, "A site had [N] crashes in the study period. A countermeasure with a crash reduction factor of [crf]% is planned. The ADT was [a0] before and is forecast at [a1] after. How many crashes are expected to be prevented?",
   "Crashes prevented = expected crashes without the improvement × crash reduction factor × (ADT after / ADT before). The traffic ratio scales the benefit to the exposure in the period being forecast.",
   r"Prevented = [N] × [crf/100|2] × \frac{[a1]}{[a0]} = [ans|2] crashes.",
   "N*crf/100*a1/a0", N=[20, 36, 12], crf=[25, 40, 15], a0=[10000, 18000, 7500], a1=[11000, 21600, 7500])
NQ('transport-e', 'crash rates', 'per HMVM', 1, 137.0, "A [L|1] mi road segment with an ADT of [adt] had [C] crashes in one year. What is its crash rate per hundred million vehicle-miles?",
   "Segment crash rates are expressed per unit of exposure, vehicle-miles travelled: rate = crashes × 100,000,000 / (ADT × 365 × years × length).",
   r"Rate = \frac{[C] × 100,000,000}{[adt] × 365 × 1 × [L|1]} = [ans|1] crashes per hundred million vehicle-miles.",
   "C*1e8/(adt*365*L)", units='USCS', C=[30, 18, 45], adt=[12000, 8000, 30000], L=[5, 2.5, 8])
NQ('transport-e', '-', 'veh/h', 0, 2160, "A highway has an AADT of [aadt]. The design-hour factor K is [K|2] and the directional split D is [D|2]. What is the directional design-hour volume?",
   "The directional design-hour volume turns a daily volume into the hourly, one-direction volume used to size the road: DDHV = AADT × K × D.",
   "DDHV = [aadt] × [K|2] × [D|2] = [ans|0] veh/h.",
   "aadt*K*D", aadt=[40000, 25000, 62000], K=[0.09, 0.10, 0.08], D=[0.60, 0.55, 0.65])
# ================= Construction =================
NQ('construction-a', '-', '$', 0, 110000, "A contractor has completed work worth $[wk] to date. The contract holds [ret]% retainage, and $[prev] has already been paid. How much is due on this progress payment?",
   "A progress payment is the value of work done to date, less the retainage the owner holds until completion, less what has already been paid.",
   "Earned less retainage = [wk] × (1 - [ret/100|2]) = $[wk*(1-ret/100)|0]. || Due now = [wk*(1-ret/100)|0] - [prev] = $[ans|0].",
   "wk*(1-ret/100)-prev", wk=[400000, 1250000, 86000], ret=[10, 5, 10], prev=[250000, 900000, 40500])
NQ('construction-a', '-', '$', 0, 993600, "An estimate has direct costs of $[dc] and indirect costs of $[ic]. The contractor adds a [mk]% markup for profit and contingency. What is the bid price?",
   "The bid is the total estimated cost, direct plus indirect (overhead), increased by the markup.",
   "Bid = ([dc] + [ic]) × (1 + [mk/100|2]) = [dc+ic] × [1+mk/100|2] = $[ans|0].",
   "(dc+ic)*(1+mk/100)", dc=[800000, 2400000, 150000], ic=[120000, 300000, 30000], mk=[8, 6, 12])
NQ('construction-b', '-', 'loads', 1, 75, "A job must haul [Vb] m^{3} of soil measured in the bank. The soil swells [sw]% when excavated, and each truck carries [cap] m^{3} loose. How many truckloads are needed?",
   "Excavated soil loosens and takes up more room than it did in the ground. Trucks are filled with loose soil, so convert bank volume to loose volume before dividing by truck capacity.",
   r"Loose volume = [Vb] × (1 + [sw/100|2]) = [Vb*(1+sw/100)|0] m^{3}. || Loads = \frac{[Vb*(1+sw/100)|0]}{[cap]} = [ans|1].",
   "Vb*(1+sw/100)/cap", Vb=[600, 1500, 240], sw=[25, 30, 20], cap=[10, 12, 8])
NQ('construction-b', '-', 'm^{3}/h', 1, 400, "A roller [W|1] m wide travels at [S] km/h and compacts lifts [lift|2] m thick in [n] passes, working at [E|2] efficiency. What is its hourly production of compacted fill?",
   "Compaction production is the volume covered in an hour, width × speed × lift thickness, divided by the number of passes each strip needs, times job efficiency.",
   r"Production = \frac{[W|1] × [S*1000|0] × [lift|2] × [E|2]}{[n]} = [ans|1] m^{3}/h.",
   "W*S*1000*lift*E/n", W=[2, 1.8, 2.1], S=[5, 4, 6], lift=[0.2, 0.15, 0.25], n=[4, 6, 5], E=[0.80, 0.75, 0.83])
NQ('construction-b', '-', 'kPa', 1, 72, "Fresh concrete with a unit weight of [gam|1] kN/m^{3} is placed quickly to a height of [h|1] m in a wall form. Treating it as a liquid, what is the maximum pressure on the form?",
   "Until it begins to set, fresh concrete behaves like a heavy liquid, so form pressure rises linearly with depth to unit weight × height at the bottom. Slower placing lets the lower concrete stiffen and caps the pressure.",
   "Maximum pressure = [gam|1] × [h|1] = [ans|1] kPa at the base of the form.",
   "gam*h", wrong=["gam*h/2", "gam*h/3", "gam*h*h/2"], h=[3, 4.2, 2.4], gam=[24, 23.5, 24])
NQ('construction-c', 'earned-value analysis', '$', 0, 625000, "A project has a budget at completion of $[bac]. To date the earned value is $[ev] and the actual cost is $[ac]. If cost performance continues at the same rate, what is the estimate at completion?",
   "The cost performance index is earned value divided by actual cost: the value produced per dollar spent. If that rate holds, the estimate at completion is the budget divided by the index.",
   r"CPI = \frac{[ev]}{[ac]} = [ev/ac|3]. || EAC = \frac{[bac]}{[ev/ac|3]} = $[ans|0].",
   "bac/(ev/ac)", bac=[500000, 1200000, 80000], ev=[200000, 450000, 30000], ac=[250000, 420000, 36000])
NQ('construction-c', '-', 'days', 2, 7, "An activity has an optimistic duration of [a] days, a most likely duration of [m] days and a pessimistic duration of [b] days. What is its PERT expected duration?",
   "PERT weights the most likely estimate four times as heavily as the two extremes: expected time = (optimistic + 4 × most likely + pessimistic) / 6.",
   r"t_{e} = \frac{[a] + 4([m]) + [b]}{6} = [ans|2] days.",
   "(a+4*m+b)/6", wrong=["(a+m+b)/3", "m", "(a+b)/2"], a=[4, 10, 2], m=[6, 14, 5], b=[14, 24, 9])
NQ('construction-c', '-', '$ per day', 0, 2000, "An activity normally takes [nd] days at a cost of $[nc]. It can be crashed to [cd] days at a cost of $[cc]. What is its crash cost per day saved?",
   "The cost slope is the extra cost divided by the time saved. When shortening a schedule, crash the critical activity with the lowest cost slope first.",
   r"Cost slope = \frac{[cc] - [nc]}{[nd] - [cd]} = $[ans|0] per day.",
   "(cc-nc)/(nd-cd)", nc=[10000, 24000, 6500], cc=[14000, 33000, 8000], nd=[8, 12, 5], cd=[6, 9, 4])
NQ('construction-d', '-', 'blocks', 1, 472.5, "A block wall is [L] m long and [H|1] m high. Each block covers 0.40 m by 0.20 m of wall face including its mortar joint. Allowing [waste]% for waste, how many blocks should be ordered?",
   "Divide the wall area by the face area of one block, joint included, then add the waste allowance.",
   r"Blocks = \frac{[L] × [H|1]}{0.40 × 0.20} × (1 + [waste/100|2]) = [L*H/0.08|0] × [1+waste/100|2] = [ans|1].",
   "L*H/0.08*(1+waste/100)", L=[12, 20, 8], H=[3, 2.4, 3.6], waste=[5, 8, 10])
NQ('construction-d', '-', 't', 1, 240, "A street overlay covers [A] m^{2} at a compacted thickness of [t] mm. The asphalt has a compacted density of [rho|2] t/m^{3}. How many tonnes are needed?",
   "Asphalt is ordered and paid for by mass. Quantity = area × compacted thickness × compacted density.",
   "Mass = [A] × [t/1000|3] × [rho|2] = [ans|1] t.",
   "A*t/1000*rho", A=[2000, 7500, 640], t=[50, 40, 75], rho=[2.4, 2.35, 2.4])
NQ('construction-e', '-', '%', 2, 8, "On a grading plan with a contour interval of [ci|1] m, two adjacent contours are [d] m apart on the ground. What is the average slope between them?",
   "Slope is rise over run. Between adjacent contours the rise is the contour interval and the run is the horizontal distance between them.",
   r"Slope = \frac{[ci|1]}{[d]} × 100 = [ans|1]%.",
   "ci/d*100", wrong=["d/ci", "ci/d*200", "ci/d*50"], ci=[2, 0.5, 5], d=[25, 20, 40])
NQ('construction-e', '-', '', 0, 600, "A plan sheet is drawn at 1 in = [ft] ft. Written as a ratio 1:N, what is N?",
   "A ratio scale needs both sides in the same unit. One foot is 12 inches, so 1 in = X ft is 1:12X.",
   "N = [ft] × 12 = [ans|0], so the scale is 1:[ans|0].",
   "ft*12", wrong=["ft", "ft*100", "ft*3"], ft=[50, 20, 100])
# ================= Engineering economics =================
NQ('econ-a', 'uniform series', '$', 0, 6710, "What is the present worth of $[A] received at the end of each year for [n] years, at [i]% interest?",
   "The uniform series present worth factor (P/A, i, n) converts equal end-of-year amounts into a single equivalent amount today: ((1 + i)^{n} - 1) / (i (1 + i)^{n}).",
   r"(P/A, [i]%, [n]) = \frac{(1 + [i/100|2])^{[n]} - 1}{[i/100|2](1 + [i/100|2])^{[n]}} = [((1+i/100)**n-1)/(i/100*(1+i/100)**n)|4]. || P = [A] × [((1+i/100)**n-1)/(i/100*(1+i/100)**n)|4] = $[ans|0].",
   "A*((1+i/100)**n-1)/(i/100*(1+i/100)**n)", A=[1000, 2500, 12000], i=[8, 5, 10], n=[10, 20, 6])
NQ('econ-a', 'sinking fund', '$', 0, 7587, "An agency needs $[F] in [n] years to replace equipment. What equal end-of-year deposit builds that amount at [i]% interest?",
   "The sinking fund factor (A/F, i, n) gives the equal annual deposit that grows to a required future amount: i / ((1 + i)^{n} - 1).",
   r"(A/F, [i]%, [n]) = \frac{[i/100|2]}{(1 + [i/100|2])^{[n]} - 1} = [i/100/((1+i/100)**n-1)|5]. || A = [F] × [i/100/((1+i/100)**n-1)|5] = $[ans|0].",
   "F*i/100/((1+i/100)**n-1)", F=[100000, 50000, 1000000], i=[6, 4, 7], n=[10, 5, 20])
NQ('econ-a', 'capitalized costs', '$', 0, 2500000, "A facility costs $[C0] to build and $[A] per year to maintain, forever. At [i]% interest, what is its capitalized cost?",
   "Capitalized cost is the present worth of something that lasts indefinitely. A perpetual annual cost A has a present worth of A / i, because that sum earns exactly A in interest each year.",
   r"Capitalized cost = [C0] + \frac{[A]}{[i/100|2]} = [C0] + [A/(i/100)|0] = $[ans|0].",
   "C0+A/(i/100)", wrong=["A/(i/100)", "C0*(1+i/100)+A", "C0+A*10"], C0=[2000000, 750000, 5000000], A=[25000, 40000, 120000], i=[5, 8, 6])
NQ('econ-a', 'compound amount', 'years', 2, 10.24, "At [i]% interest compounded annually, how long does a sum of money take to double?",
   "Set (1 + i)^{n} = 2 and solve with logarithms: n = ln 2 / ln(1 + i). The rule of 72, 72 divided by the rate in percent, is a quick check.",
   r"n = \frac{ln 2}{ln(1 + [i/100|2])} = \frac{0.6931}{[log(1+i/100)|5]} = [ans|2] years.",
   "log(2)/log(1+i/100)", i=[7, 4, 12])
NQ('econ-a', 'rate of return', '%', 2, 10.0, "An investment of $[P] grows to $[F] in [n] years. What annual rate of return did it earn?",
   "For a single sum, F = P(1 + i)^{n}. Solve for the rate: i = (F / P)^{1/n} - 1.",
   r"i = (\frac{[F]}{[P]})^{1/[n]} - 1 = [(F/P)**(1/n)|5] - 1 = [ans|2]%.",
   "((F/P)**(1/n)-1)*100", P=[10000, 5000, 25000], F=[16105, 8000, 35000], n=[5, 6, 4])
NQ('econ-a', 'inflation', '%', 2, 4.85, "An investment earns a market interest rate of [i|1]% while inflation runs at [f|1]%. What is the real (inflation-free) rate of return?",
   "The market rate d combines the real rate i and inflation f: d = i + f + i f. Solving for the real rate gives (1 + d) / (1 + f) - 1, slightly less than the simple difference.",
   r"Real rate = \frac{1 + [i/100|3]}{1 + [f/100|3]} - 1 = [ans|2]%.",
   "((1+i/100)/(1+f/100)-1)*100", i=[8, 6, 12], f=[3, 2.5, 5])
NQ('econ-b', 'MACRS', '$', 0, 16000, "Equipment costing $[C], with an expected salvage value of $[Sv], is depreciated by MACRS. The MACRS factor for year [yr] is [fac|2]%. What is the depreciation in year [yr]?",
   "MACRS depreciation is the tabulated factor times the full cost. Salvage value is not subtracted, unlike straight-line depreciation, because the factors already write the asset down to zero.",
   "D = [fac/100|4] × [C] = $[ans|0]. The salvage value plays no part.",
   "fac/100*C", wrong=["fac/100*(C-Sv)", "C/5", "(C-Sv)/5"], C=[50000, 120000, 36000, 80000], Sv=[5000, 20000, 6000, 8000], fac=[32, 19.2, 11.52, 5.76], yr=['2', '3', '4', '6'])
NQ('econ-b', 'Chemical Engineering::cost indexes', '$', 0, 2600000, "A facility cost $[C1] when the construction cost index stood at [I1]. The index is now [I2]. What would the same facility cost today?",
   "A cost index tracks how construction prices change over time. Scale a historical cost by the ratio of the current index to the index when the cost was recorded.",
   r"Cost today = [C1] × \frac{[I2]}{[I1]} = $[ans|0].",
   "C1*I2/I1", C1=[2000000, 450000, 12500000], I1=[180, 220, 150], I2=[234, 275, 210])
NQ('econ-c', '-', 'years', 2, 3.75, "A signal retiming project costs $[C] and saves $[s] per year. What is its simple payback period?",
   "Simple payback is the first cost divided by the annual saving. It ignores interest and anything after the payback date, so it screens projects but does not rank them.",
   r"Payback = \frac{[C]}{[s]} = [ans|2] years.",
   "C/s", C=[45000, 180000, 9600], s=[12000, 40000, 3200])
NQ('econ-c', 'uniform series; single payment', '$', 0, 19933, "A project costs $[C] now, returns $[A] at the end of each year for [n] years and has a salvage value of $[Sv] at the end. At [i]% interest, what is its net present worth?",
   "Net present worth brings every cash flow to today: the annual returns by the (P/A) factor and the salvage by the (P/F) factor, less the first cost. A positive value means the project earns more than the interest rate.",
   r"(P/A, [i]%, [n]) = [((1+i/100)**n-1)/(i/100*(1+i/100)**n)|4] and (P/F, [i]%, [n]) = [(1+i/100)**-n|4]. || NPW = -[C] + [A]([((1+i/100)**n-1)/(i/100*(1+i/100)**n)|4]) + [Sv]([(1+i/100)**-n|4]) = $[ans|0].",
   "-C+A*((1+i/100)**n-1)/(i/100*(1+i/100)**n)+Sv*(1+i/100)**-n", C=[100000, 250000, 40000], A=[30000, 55000, 12000], n=[5, 8, 4], i=[10, 8, 12], Sv=[10000, 30000, 0])
NQ('econ-d', 'Engineering Probability and Statistics::expected value', '$', 0, 49500, "A firm estimates a [pw]% chance of winning a contract that would earn a profit of $[pr]. Preparing the proposal costs $[bc], which is lost if the firm does not win. What is the expected value of pursuing it?",
   "Expected value weights each outcome by its probability: the chance of winning times the profit, minus the chance of losing times the cost of the proposal.",
   "EV = [pw/100|2]([pr]) - [1-pw/100|2]([bc]) = [pw/100*pr|0] - [(1-pw/100)*bc|0] = $[ans|0].",
   "pw/100*pr-(1-pw/100)*bc", pw=[30, 20, 45], pr=[200000, 750000, 80000], bc=[15000, 40000, 6000])
NQ('econ-d', 'Engineering Probability and Statistics::expected value', '', 2, 0.2, "A venture gains $[G] if it succeeds and loses $[Ls] if it fails. At what probability of success is its expected value zero?",
   "Set the expected value to zero: p × gain = (1 - p) × loss. Solving gives p = loss / (gain + loss). Above that probability the venture is worth taking on expected value alone.",
   r"p = \frac{[Ls]}{[G] + [Ls]} = [ans|2].",
   "Ls/(G+Ls)", wrong=["Ls/G", "G/(G+Ls)", "0.5"], G=[80000, 150000, 45000], Ls=[20000, 50000, 5000])
# ================= Ethics and professional practice =================
MRB = 'NCEES Model Rules, Rules of Professional Conduct'
CQ('ethics-c', 'responsible charge', "A seal certifies that the work was prepared by the licensee or under the licensee's responsible charge, meaning direct control and personal supervision. It is not a formatting step and cannot be lent, and a licensee seals only work within their own competence.", MRB,
   ("A licensed engineer is designer of record for the signing and striping sheets in a plan set. The client asks her to also seal the structural sheets for a sign bridge, which another firm prepared without her involvement. What should she do?",
    ["Seal them, since they are in the same plan set", "Seal only the sheets prepared under her responsible charge", "Seal them after checking the title block", "Ask a colleague to apply her seal"], 1,
    "She may seal only work she prepared or supervised, and only within her competence. The structural sheets need the seal of the engineer who was in responsible charge of them. || Sharing a plan set does not transfer responsibility, and nobody else may apply her seal."),
   ("An engineer in training drafts a traffic signal plan under the day-to-day direction of a licensed engineer, who reviews the calculations and directs revisions. Who may seal the plan?",
    ["The engineer in training, who did most of the work", "Any licensed engineer in the firm", "The licensed engineer who directed and reviewed the work", "No one, because an unlicensed person worked on it"], 2,
    "Work by unlicensed staff may be sealed by the licensee who had direct control and personal supervision of it. That is what responsible charge means. || The engineer in training cannot seal, and a licensee who had no part in the work cannot either."))
CQ('ethics-a', 'conflict of interest', "A reviewer's duty is to give an honest professional opinion. Licensees must be objective and truthful in reports and statements, and must not let a business interest, a schedule or a relationship change a technical finding.", MRB,
   ("While checking a colleague's plans as the QA/QC reviewer, an engineer finds a sight distance deficiency. The project manager asks him to sign off without comment to meet the submittal date. What should he do?",
    ["Sign off, because the designer of record is responsible", "Record the comment and see that it is resolved or formally answered", "Fix the plans himself without telling anyone", "Refuse to review any more of the project"], 1,
    "The review exists to catch exactly this. He records the finding and makes sure the designer of record resolves or answers it, even if the date slips. || Staying silent would make his sign-off untruthful, and a safety issue left in place puts the public at risk."),
   ("An engineer preparing a corridor study for a city finds that the alternative the city prefers performs worse on safety than another alternative. What should the report say?",
    ["Only the results that support the preferred alternative", "The full findings, including the safety comparison", "Nothing about safety", "Whatever the city's project manager asks for"], 1,
    "Reports must be objective and truthful and include all relevant information. The city may still choose its preferred alternative, but it must be able to do so knowing the findings. || Leaving out an unfavourable result would mislead the client and the public."))
CQ('ethics-a', 'conflict of interest', "Licensees must not solicit or accept gratuities from contractors, suppliers or others dealing with their client in connection with work for which they are responsible. The test is whether it could influence, or appear to influence, their judgement.", MRB,
   ("A striping contractor whose work an engineer inspects for a city offers the engineer tickets to a playoff game. What should the engineer do?",
    ["Accept, since the tickets are not cash", "Accept, but disclose it afterwards", "Decline the tickets", "Accept if the inspection is already finished"], 2,
    "The contractor's work is subject to the engineer's judgement, so a valuable gift from that contractor is a prohibited gratuity. || The form of the gift and the timing do not change that."),
   ("A signal equipment supplier offers to pay an engineer a commission for each controller the engineer specifies on public projects. What do the rules require?",
    ["Accept if the equipment is good", "Accept and split it with the employer", "Refuse the arrangement", "Accept only for projects outside the home state"], 2,
    "Taking compensation from a supplier for specifying its product is a conflict of interest that cannot be cured by good equipment. The engineer must refuse and specify on technical merit."))
CQ('ethics-b', 'standard of care', "Negligence is judged against the standard of care: the skill and diligence that a reasonably prudent engineer would use in the same place and circumstances. Engineers are not required to be perfect, and following the governing standards in force at the time is strong evidence of meeting it.", 'General principles of professional liability',
   ("An engineer's intersection design followed the governing design manual, but a crash later occurs there. In a negligence claim, what must the plaintiff show about the engineer's work?",
    ["That a crash happened", "That it fell below what a reasonably prudent engineer would have done", "That a better design was possible", "That the engineer was licensed"], 1,
    "A bad outcome alone does not prove negligence, and neither does the existence of a better design. The question is whether the engineer met the standard of care."),
   ("Which act is most likely to breach the standard of care?",
    ["Using a design that later research improves on", "Omitting a required check that competent practitioners routinely perform", "Choosing the lower-cost of two acceptable designs", "Documenting a design exception approved by the agency"], 1,
    "Skipping a check that competent engineers routinely make is the kind of lapse a reasonably prudent engineer would not commit. || The other choices reflect ordinary professional judgement."))
CQ('ethics-d', 'contract', "A scope of services defines what the engineer has agreed to do. Work outside it should be covered by a written amendment before it is done; otherwise payment is uncertain and the extra work may fall outside the contract's protections.", 'General principles of contract law',
   ("Midway through a design contract, the client's project manager verbally asks the consultant to add a traffic study that is not in the scope. What should the consultant do first?",
    ["Do the study and bill for it at the end", "Decline all changes", "Get a written amendment covering scope, fee and schedule", "Do it at no charge to keep the client happy"], 2,
    "Changes to a contract should be agreed in writing before the work is done, covering scope, fee and schedule. A verbal request from someone who may lack authority to bind the client is a weak basis for payment."),
   ("A contract requires the engineer to perform services 'to the highest possible standard'. Why is this wording a concern for the engineer?",
    ["It lowers the fee", "It may promise more than the ordinary standard of care, and professional liability insurance may not cover it", "It makes the contract void", "It transfers the risk to the client"], 1,
    "Agreeing to a standard above the ordinary standard of care is a contractual warranty. Liability insurance generally covers negligence, not failure to meet a higher promised standard."))
CQ('ethics-c', 'continuing', "A licence is granted by a state board and must be kept current under that board's rules, usually by renewal and continuing professional competency hours. Practising, or offering to practise, without a current licence in the state where the project lies is unlawful.", 'NCEES Model Law and Model Rules, licensure provisions',
   ("An engineer's licence expired two months ago because a renewal was missed. A plan set is due this week. What may the engineer do?",
    ["Seal it, since the lapse is short", "Seal it and renew afterwards", "Not seal it until the licence is reinstated", "Seal it with a colleague's seal"], 2,
    "Without a current licence the engineer may not seal engineering work, however short the lapse. The licence must be reinstated first, or another licensee must take responsible charge of the work."),
   ("What do most state boards require for a professional engineer to renew a licence?",
    ["Retaking the PE exam", "Continuing professional competency hours and a renewal fee", "A new set of references each cycle", "Nothing, because a licence is permanent"], 1,
    "Renewal normally requires a fee and a set number of continuing professional competency hours in each renewal period. Exams are not repeated."))
if __name__ == '__main__': run('f6')
