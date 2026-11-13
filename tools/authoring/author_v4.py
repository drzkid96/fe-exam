"""Version families, part 4: engineering economics, materials, mathematics and statistics, construction."""
from author_v import *
def F(base, stem, concept, sol, ans, wrong=None, dp=None, fig=None, sfig=None, **P): V(base, stem, P, ans, sol, wrong, dp, fig, sfig, concept)
money = lambda x: '$' + nf(x, 0)

# ---------------- Engineering economics ----------------
F('econ-0001', "$[P] is deposited in an account that pays [i]% interest compounded annually. What is the balance after [n] years?",
  "Compound interest earns interest on interest. A single present amount P grows to F = P(1 + i)^{n}; the factor (1 + i)^{n} is the single payment compound amount factor, (F/P, i, n).",
  r"F = P(1 + i)^{n} = [P](1 + [i/100|2])^{[n]} = [P] × [(1+i/100)**n|4] = $[ans|0].",
  "P*(1+i/100)**n", wrong=["P*(1+i/100*n)", "P*(1+i/1200)**(12*n)", "P*(1+i/100)**(n+1)"], dp=0, fig=lambda e: cashflow(e['n'], P=money(e['P']), F='F = ?'), P=[5000, 12000, 2500, 8000], i=[6, 5, 8, 7], n=[10, 15, 6, 12])
F('econ-0002', "A $[P] loan is repaid in [nw] equal end-of-year payments at [i]% annual interest. What is each payment?",
  "A uniform series that repays a present amount is found with the capital recovery factor: A = P × i(1 + i)^{n} / ((1 + i)^{n} - 1), written (A/P, i, n). Each payment covers that year's interest plus some principal.",
  r"(A/P, [i]%, [n]) = \frac{[i/100|2](1 + [i/100|2])^{[n]}}{(1 + [i/100|2])^{[n]} - 1} = [i/100*(1+i/100)**n/((1+i/100)**n-1)|5]. || A = [P] × [i/100*(1+i/100)**n/((1+i/100)**n-1)|5] = $[ans|0] per year.",
  "P*i/100*(1+i/100)**n/((1+i/100)**n-1)", dp=0, fig=lambda e: cashflow(e['n'], P=money(e['P']), A='A = ?'), P=[20000, 50000, 12000, 150000], i=[8, 6, 10, 5], n=[5, 10, 4, 20], nw=['five', 'ten', 'four', 'twenty'])
F('econ-0003', "A plant has fixed costs of $[FC] per year. Each unit costs $[vc] to make and sells for $[pr]. How many units per year must be sold to break even?",
  "At the break-even point total revenue equals total cost. Each unit sold contributes (price - variable cost) toward the fixed costs, so the break-even quantity is fixed cost divided by that contribution margin.",
  r"Contribution per unit = [pr] - [vc] = $[pr-vc]. || Break-even quantity = \frac{[FC]}{[pr-vc]} = [ans|0] units per year.",
  "FC/(pr-vc)", wrong=["FC/pr", "FC/vc", "FC/(pr+vc)"], dp=0, FC=[120000, 84000, 250000, 45000], vc=[18, 22, 40, 6], pr=[30, 36, 65, 15])
F('econ-0004', "A project has a [p1]% chance of losing $[Ls], a [p2]% chance of earning $[G1] and a [100-p1-p2]% chance of earning $[G2]. What is its expected value?",
  "Expected value is the probability-weighted average of all outcomes: the sum of each outcome times its probability. Losses enter as negative values, and the probabilities must sum to 1.",
  "EV = [p1/100|2](-[Ls]) + [p2/100|2]([G1]) + [(100-p1-p2)/100|2]([G2]) = -[p1/100*Ls|0] + [p2/100*G1|0] + [(100-p1-p2)/100*G2|0] = $[ans|0].",
  "-p1/100*Ls+p2/100*G1+(100-p1-p2)/100*G2", wrong=["(-Ls+G1+G2)/3", "p2/100*G1+(100-p1-p2)/100*G2", "-Ls+G1+G2"], dp=0, p1=[20, 10, 25, 30], Ls=[50000, 80000, 20000, 40000], p2=[50, 60, 45, 30], G1=[40000, 30000, 60000, 50000], G2=[100000, 120000, 90000, 150000])
F('econ-0005', "A machine has fixed costs of $[FC] per year and variable costs of $[vc] per unit. What is the average cost per unit at [n] units per year?",
  "Average unit cost is total cost divided by output. Fixed cost is spread over more units as output rises, so average cost falls toward the variable cost per unit.",
  r"Total cost = [FC] + [vc]([n]) = $[FC+vc*n]. || Average cost = \frac{[FC+vc*n]}{[n]} = $[ans] per unit.",
  "FC/n+vc", wrong=["FC/n", "vc", "FC/1000+vc"], FC=[50000, 36000, 120000, 100000], vc=[12, 8, 25, 7], n=[10000, 4000, 8000, 20000])
F('econ-0006', "A task needs [h] hours of direct labor at $[r] per hour and $[m] of materials. Overhead is charged at [oh]% of direct labor. What is the total cost?",
  "Cost estimates build up from direct costs (labor and materials) plus indirect costs. Here overhead is allocated as a percentage of direct labor cost, a common allocation base.",
  "Direct labor = [h] × [r] = $[h*r]. || Overhead = [oh]% × [h*r] = $[h*r*oh/100|0]. || Total = [h*r] + [h*r*oh/100|0] + [m] = $[ans|0].",
  "h*r*(1+oh/100)+m", dp=0, h=[40, 60, 25, 120], r=[35, 42, 50, 38], m=[600, 1500, 400, 2200], oh=[50, 40, 60, 35])
F('econ-0007', "What is the present worth of $[Fv] received [n] years from now at an interest rate of [i]% per year?",
  "Discounting is compounding in reverse. A future amount F is worth P = F / (1 + i)^{n} today; the factor 1 / (1 + i)^{n} is (P/F, i, n).",
  r"P = \frac{F}{(1 + i)^{n}} = \frac{[Fv]}{(1 + [i/100|2])^{[n]}} = \frac{[Fv]}{[(1+i/100)**n|4]} = $[ans|0].",
  "Fv/(1+i/100)**n", wrong=["Fv/(1+i/100*n)", "Fv/(1+i/100)**(n-1)", "Fv*(1+i/100)**n"], dp=0, fig=lambda e: cashflow(e['n'], P='P = ?', F=money(e['Fv'])), Fv=[10000, 25000, 4000, 60000], i=[5, 8, 6, 4], n=[6, 10, 4, 15])
F('econ-0008', "A loan charges a nominal rate of [r]% per year, compounded [per]. What is the effective annual interest rate?",
  "A nominal rate r compounded m times a year charges r/m each period. The effective annual rate is the single yearly rate that gives the same growth: i_{e} = (1 + r/m)^{m} - 1. It is always above the nominal rate when m is greater than 1.",
  r"Rate per period = [r]% / [m] = [r/m|3]%. || i_{e} = (1 + [r/m/100|5])^{[m]} - 1 = [(1+r/m/100)**m-1|5] = [ans|2]%.",
  "((1+r/m/100)**m-1)*100", dp=2, r=[12, 9, 18, 6], m=[12, 4, 12, 2], per=['monthly', 'quarterly', 'monthly', 'semiannually'])
F('econ-0009', "A flood wall costs $[C0] to build and $[Mc] per year to maintain. It prevents $[B] of damage per year. Over [n] years at [i]%, what is the benefit-cost ratio?",
  "Benefit-cost analysis compares benefits and costs on the same time basis. Convert the annual amounts to present worth with (P/A, i, n) = ((1 + i)^{n} - 1) / (i(1 + i)^{n}), then divide present worth of benefits by present worth of costs. A ratio above 1 means the project is justified.",
  r"(P/A, [i]%, [n]) = [((1+i/100)**n-1)/(i/100*(1+i/100)**n)|3]. || PW of benefits = [B] × [((1+i/100)**n-1)/(i/100*(1+i/100)**n)|3] = $[B*((1+i/100)**n-1)/(i/100*(1+i/100)**n)|0]. || PW of costs = [C0] + [Mc] × [((1+i/100)**n-1)/(i/100*(1+i/100)**n)|3] = $[C0+Mc*((1+i/100)**n-1)/(i/100*(1+i/100)**n)|0]. || B/C = [ans|2].",
  "B*((1+i/100)**n-1)/(i/100*(1+i/100)**n)/(C0+Mc*((1+i/100)**n-1)/(i/100*(1+i/100)**n))", wrong=["(C0+Mc*((1+i/100)**n-1)/(i/100*(1+i/100)**n))/(B*((1+i/100)**n-1)/(i/100*(1+i/100)**n))", "B/(C0/n+Mc)", "B*((1+i/100)**n-1)/(i/100*(1+i/100)**n)/C0"], dp=2,
  C0=[300000, 500000, 180000, 1200000], Mc=[15000, 20000, 8000, 40000], B=[60000, 85000, 30000, 150000], i=[6, 5, 8, 4], n=[20, 25, 15, 30])
F('econ-0010', "A machine costs $[P], costs $[Oc] per year to run, and has a salvage value of $[Sv] after [n] years. At [i]% interest, what is its equivalent uniform annual cost?",
  "Equivalent uniform annual cost spreads every cash flow evenly over the life: the first cost times (A/P), minus the salvage value times the sinking fund factor (A/F), plus the annual operating cost. It lets alternatives with different lives be compared.",
  r"(A/P, [i]%, [n]) = [i/100*(1+i/100)**n/((1+i/100)**n-1)|5] and (A/F, [i]%, [n]) = [i/100/((1+i/100)**n-1)|5]. || EUAC = [P]([i/100*(1+i/100)**n/((1+i/100)**n-1)|5]) - [Sv]([i/100/((1+i/100)**n-1)|5]) + [Oc] = [P*i/100*(1+i/100)**n/((1+i/100)**n-1)|0] - [Sv*i/100/((1+i/100)**n-1)|0] + [Oc] = $[ans|0] per year.",
  "P*i/100*(1+i/100)**n/((1+i/100)**n-1)-Sv*i/100/((1+i/100)**n-1)+Oc", dp=0, P=[40000, 75000, 18000, 120000], Oc=[3000, 5500, 1200, 9000], Sv=[5000, 10000, 2000, 15000], n=[8, 10, 5, 12], i=[10, 8, 12, 6])

# ---------------- Materials ----------------
F('materials-0001', "A concrete mix uses [W] kg of water and [C] kg of cement per cubic metre. What is the water-cement ratio?",
  "The water-cement ratio is the mass of water divided by the mass of cement. It is the main control on concrete strength and durability: a lower ratio gives stronger, less permeable concrete but less workability.",
  r"w/c = \frac{[W]}{[C]} = [ans|3].", "W/C", wrong=["W/(W+C)", "(C-W)/C", "C/W"], dp=3, W=[180, 168, 195, 150], C=[400, 350, 450, 375])
F('materials-0002', "A [d] mm diameter concrete cylinder fails at a load of [P] kN in a compression test. What is the compressive strength?",
  "Compressive strength is the failure load divided by the loaded cross-sectional area of the cylinder. Newtons over square millimetres gives MPa.",
  r"A = \frac{π([d])^{2}}{4} = [pi*d*d/4|0] mm^{2}. || f'_{c} = \frac{[P*1000] N}{[pi*d*d/4|0] mm^{2}} = [ans|1] MPa.",
  "P*1000/(pi*d*d/4)", wrong=["P*1000/(pi*d*d)", "P*1000/(d*d)", "P*1000/(pi*d*d/4)*1.5"], dp=1, d=[150, 100, 150, 100], P=[530, 275, 620, 196])
F('materials-0004', "In a tension test, a metal bar reaches a stress of [st] MPa at a strain of [eps], still on the straight-line part of the curve. What is the modulus of elasticity?",
  "On the linear part of the stress-strain curve Hooke's law applies: stress = E × strain. The modulus of elasticity is the slope of that line and measures stiffness, not strength.",
  r"E = \frac{stress}{strain} = \frac{[st]}{[eps]} = [st/eps|0] MPa = [ans|0] GPa.", "st/eps/1000", dp=0, st=[140, 105, 84, 160], eps=[0.0007, 0.0015, 0.0004, 0.0008])
F('materials-0005', "A concrete mix contains [m] kg of cement per cubic metre. The specific gravity of cement is 3.15. What volume does the cement occupy?",
  "In the absolute volume method each ingredient's volume is its mass divided by (specific gravity × density of water). The absolute volumes of cement, water, aggregates and air must add up to one cubic metre.",
  r"V = \frac{mass}{SG × 1,000} = \frac{[m]}{3.15 × 1,000} = [ans|3] m^{3}.",
  "m/3150", wrong=["m/10000", "m/1000", "m*3.15/1000"], dp=3, m=[350, 400, 300, 450])
F('materials-0006', "An asphalt mix sample has a total mass of [tot] g, of which [bn] g is asphalt binder. What is the asphalt content by total mass of mix?",
  "Asphalt content is normally expressed as binder mass over total mix mass, not over aggregate mass. The two bases give different numbers, so check which one a specification uses.",
  r"P_{b} = \frac{[bn]}{[tot]} × 100 = [ans|2]%. By mass of aggregate it would be \frac{[bn]}{[tot-bn]} × 100 = [bn/(tot-bn)*100|2]%.",
  "bn/tot*100", wrong=["bn/(tot+bn)*100", "bn/(tot-bn)*100", "tot/bn"], dp=2, tot=[1200, 1500, 1150, 2000], bn=[60, 84, 46, 130])
F('materials-0009', "Using E_{c} = 4,700 × the square root of f'_{c} (both in MPa), what is the modulus of elasticity of concrete with a compressive strength of [fc] MPa?",
  "The stiffness of normal-weight concrete rises with the square root of its compressive strength, so doubling the strength raises the modulus by only about 41%.",
  r"E_{c} = 4,700 \sqrt{[fc]} = 4,700 × [sqrt(fc)|3] = [ans|0] MPa.",
  "4700*sqrt(fc)", wrong=["4700", "2350*sqrt(fc)", "4700*fc"], dp=0, fc=[25, 36, 30, 49])
F('materials-0010', "A tension specimen has a gauge length of [L0] mm. After fracture the gauge length measures [Lf|1] mm. What is the percent elongation?",
  "Percent elongation is the permanent increase in gauge length at fracture divided by the original gauge length. It is a measure of ductility, along with reduction of area.",
  r"Elongation = \frac{[Lf|1] - [L0]}{[L0]} × 100 = \frac{[Lf-L0|1]}{[L0]} × 100 = [ans|1]%.",
  "(Lf-L0)/L0*100", dp=1, L0=[50, 50, 200, 25], Lf=[62, 58.5, 236, 31.5])

# ---------------- Mathematics and statistics ----------------
F('math-0001', "A straight line passes through the points ([x1], [y1]) and ([x2], [y2]). What is its y-intercept?",
  "A line is y = m x + b. Find the slope from the two points, m = (y_{2} - y_{1}) / (x_{2} - x_{1}), then solve for b by substituting either point.",
  r"m = \frac{[y2] - [y1]}{[x2] - [x1]} = [(y2-y1)/(x2-x1)]. || b = y_{1} - m x_{1} = [y1] - ([(y2-y1)/(x2-x1)])([x1]) = [ans].",
  "y1-(y2-y1)/(x2-x1)*x1", wrong=["-y1", "y1-x1", "(y2-y1)/(x2-x1)"], x1=[2, 1, 2, 3], y1=[3, 5, 10, 1], x2=[6, 4, 6, 9], y2=[11, 14, 2, 4])
F('math-0002', "Find the area between the curve y = [a]x^{2} and the x-axis from x = 0 to x = [b].",
  "The area under a curve is its definite integral. By the power rule the integral of a x^{2} is a x^{3} / 3; evaluate it at the limits and subtract.",
  r"Area = \frac{[a] x^{3}}{3} evaluated from 0 to [b] = \frac{[a]([b])^{3}}{3} - 0 = [ans] square units.",
  "a*b**3/3", a=[3, 6, 1.5, 12], b=[2, 3, 4, 1])
F('math-0004', "A sample of five measurements is [data]. What is the sample standard deviation?",
  "The sample standard deviation divides the sum of squared deviations from the mean by n - 1, not n, because the mean was estimated from the same data. Dividing by n gives the population standard deviation, which is always smaller.",
  r"Mean = [sum(data)/5]. || Sum of squared deviations = [sd(data)**2*4|1]. || s = \sqrt{\frac{[sd(data)**2*4|1]}{5 - 1}} = \sqrt{[sd(data)**2|2]} = [ans|2].",
  "sd(data)", wrong=["psd(data)", "psd(data)**2", "sd(data)**2"], dp=2, data=[[2, 4, 4, 6, 9], [3, 5, 8, 10, 14], [10, 12, 15, 18, 25], [1, 2, 6, 7, 9]])
F('math-0006', "A circle has the equation x^{2} + y^{2} [tx] [ty] = 0. What is its radius?",
  "Complete the square in x and in y to reach the standard form (x - h)^{2} + (y - k)^{2} = r^{2}. For x^{2} + y^{2} + Dx + Ey = 0 the centre is (-D/2, -E/2) and r^{2} = (D/2)^{2} + (E/2)^{2}.",
  r"Centre = ([-D/2], [-E/2]). || r^{2} = ([D/2])^{2} + ([E/2])^{2} = [D*D/4+E*E/4], so r = [ans].",
  "sqrt(D*D/4+E*E/4)", wrong=["abs(D)/2", "abs(E)/2", "D*D/4+E*E/4"], D=[-6, 10, -16, -8], E=[8, -24, 12, -6], tx=['- 6x', '+ 10x', '- 16x', '- 8x'], ty=['+ 8y', '- 24y', '+ 12y', '- 6y'])
F('math-0007', "What is the straight-line distance between the points ([x1], [y1]) and ([x2], [y2])?",
  "The distance formula is the Pythagorean theorem applied to the differences in x and y: d = square root of ((x_{2} - x_{1})^{2} + (y_{2} - y_{1})^{2}).",
  r"d = \sqrt{([x2] - ([x1]))^{2} + ([y2] - ([y1]))^{2}} = \sqrt{[(x2-x1)**2] + [(y2-y1)**2]} = [ans] units.",
  "hypot(x2-x1,y2-y1)", x1=[1, 2, -3, 0], y1=[2, -1, 4, 3], x2=[7, 7, 5, 8], y2=[10, 11, -2, 18])
F('math-0008', "Two sides of a triangle are [sa] m and [sb] m long and meet at an angle of [C]°. How long is the third side?",
  "The law of cosines extends the Pythagorean theorem to any triangle: c^{2} = a^{2} + b^{2} - 2 a b cos(C), where C is the angle between sides a and b. For C = 90° the last term vanishes.",
  r"c^{2} = [sa]^{2} + [sb]^{2} - 2([sa])([sb]) cos [C]° = [sa*sa+sb*sb] - ([2*sa*sb*cos(rad(C))|2]) = [sa*sa+sb*sb-2*sa*sb*cos(rad(C))|2]. || c = [ans|2] m.",
  "sqrt(sa*sa+sb*sb-2*sa*sb*cos(rad(C)))", wrong=["sqrt(sa*sa+sb*sb-2*sa*sb*sin(rad(C)))", "sqrt(sa*sa+sb*sb)", "sqrt(sa*sa+sb*sb+2*sa*sb*cos(rad(C)))"], dp=2, fig=lambda e: triangle(e['sb'], e['sa'], e['C']), sa=[5, 8, 6, 10], sb=[7, 11, 9, 14], C=[60, 40, 75, 110])
F('math-0009', "What is the slope of the curve y = x^{3} - [k]x at x = [x0]?",
  "The slope of a curve at a point is the value of its derivative there. By the power rule, d/dx of x^{3} is 3x^{2} and d/dx of k x is k.",
  "dy/dx = 3x^{2} - [k]. || At x = [x0]: 3([x0])^{2} - [k] = [3*x0*x0] - [k] = [ans].",
  "3*x0*x0-k", wrong=["x0**3-k*x0", "3*x0*x0", "3*x0*x0+k"], k=[6, 4, 10, 2], x0=[2, 3, 2, 1])
F('math-0010', "What is the maximum value of f(x) = -[a]x^{2} + [b]x [cs]?",
  "A maximum or minimum occurs where the first derivative is zero. The second derivative tells which: negative means a maximum. Substitute the critical x back into the function to get the value.",
  r"f'(x) = -[2*a]x + [b] = 0, so x = \frac{[b]}{[2*a]} = [b/(2*a)]. || f''(x) = -[2*a], negative, so this is a maximum. || f([b/(2*a)]) = -[a]([b/(2*a)])^{2} + [b]([b/(2*a)]) [cs] = [ans].",
  "c+b*b/(4*a)", a=[2, 1, 3, 0.5], b=[12, 8, 18, 6], c=[5, -3, 10, 2], cs=['+ 5', '- 3', '+ 10', '+ 2'])
F('math-0011', "A vehicle's speed is v(t) = [a]t + [b], in m/s. How far does it travel between t = 0 and t = [tt] s?",
  "Distance is the integral of speed over time, the area under the speed-time graph. For a straight-line speed function that area is a trapezoid.",
  r"s = \frac{[a] t^{2}}{2} + [b] t evaluated from 0 to [tt] = \frac{[a]([tt])^{2}}{2} + [b]([tt]) = [a*tt*tt/2] + [b*tt] = [ans] m.",
  "a*tt*tt/2+b*tt", a=[4, 3, 6, 2.5], b=[2, 5, 1, 4], tt=[3, 4, 2, 6])
F('math-0012', "For the plane vectors **A** = ([a1], [a2]) and **B** = ([b1], [b2]), what is the magnitude of the cross product **A** × **B**?",
  "For vectors in the x-y plane the cross product points along z and its magnitude is |A_{x} B_{y} - A_{y} B_{x}|. It equals the area of the parallelogram formed by the two vectors, and |A||B| sin(angle between them).",
  "A_{x} B_{y} - A_{y} B_{x} = ([a1])([b2]) - ([a2])([b1]) = [a1*b2] - ([a2*b1]) = [a1*b2-a2*b1]. || Magnitude = [ans].",
  "abs(a1*b2-a2*b1)", wrong=["a1*b1+a2*b2", "abs(a1*b2+a2*b1)", "abs(a1*b1-a2*b2)"], a1=[2, 3, 5, 1], a2=[3, 1, 2, 6], b1=[4, 2, 1, 3], b2=[-1, 5, 4, 2])
F('math-0013', "What is the magnitude of the vector with components ([a1], [a2], [a3])?",
  "The magnitude of a vector is the square root of the sum of the squares of its components, the three-dimensional form of the Pythagorean theorem. Signs do not matter because each component is squared.",
  r"Magnitude = \sqrt{([a1])^{2} + ([a2])^{2} + ([a3])^{2}} = \sqrt{[a1*a1] + [a2*a2] + [a3*a3]} = \sqrt{[a1*a1+a2*a2+a3*a3]} = [ans].",
  "sqrt(a1*a1+a2*a2+a3*a3)", a1=[3, 2, 4, 6], a2=[-4, -6, 4, -2], a3=[12, 9, -7, 3])
F('math-0015', "Concrete strength is normally distributed with a mean of [mu] MPa and a standard deviation of [sv] MPa. What fraction of tests fall below [x] MPa?",
  "Convert the value to a standard normal variable, z = (x - mean) / standard deviation, then read the cumulative probability from the unit normal table in the handbook. By symmetry, the area below -z equals the area above +z.",
  r"z = \frac{[x] - [mu]}{[sv]} = [(x-mu)/sv|2]. || From the unit normal table, F([(x-mu)/sv|2]) = [ans|4].",
  "0.5*(1+erf((x-mu)/sv/sqrt(2)))", wrong=["0.5*(1+erf(0.5*(x-mu)/sv/sqrt(2)))", "abs(0.5*erf((x-mu)/sv/sqrt(2)))", "0.5*(1-erf((x-mu)/sv/sqrt(2)))"], dp=4, mu=[30, 40, 25, 50], sv=[4, 5, 3, 8], x=[26, 32.5, 28, 34])
F('math-0016', "A least-squares line is fitted to the points (1, [y1]), (2, [y2]) and (3, [y3]). What is its slope?",
  "The least-squares line minimises the sum of squared vertical errors. Its slope is S_{xy} / S_{xx}, where S_{xy} is the sum of (x - x-bar)(y - y-bar) and S_{xx} is the sum of (x - x-bar)^{2}.",
  r"x-bar = 2 and y-bar = [(y1+y2+y3)/3|3]. || S_{xy} = (-1)([y1] - [(y1+y2+y3)/3|3]) + 0 + (1)([y3] - [(y1+y2+y3)/3|3]) = [y3-y1]. || S_{xx} = 1 + 0 + 1 = 2. || Slope = \frac{[y3-y1]}{2} = [ans].",
  "(y3-y1)/2", y1=[2, 1, 3, 5], y2=[4, 4, 4, 4], y3=[5, 6, 9, 2])
F('math-0017', "Each item from a process has a [p*100]% chance of being defective. In a sample of [n] items, what is the probability that exactly 2 are defective?",
  "The binomial distribution gives the probability of exactly x successes in n independent trials: P(x) = C(n, x) p^{x} (1 - p)^{n - x}. The combination C(n, x) counts the ways to choose which trials are the successes.",
  "C([n], 2) = [comb(n,2)]. || P(2) = [comb(n,2)] × ([p|2])^{2} × ([1-p|2])^{[n-2]} = [comb(n,2)] × [p*p|4] × [(1-p)**(n-2)|4] = [ans|4].",
  "comb(n,2)*p**2*(1-p)**(n-2)", wrong=["p**2*(1-p)**(n-2)", "n*p*(1-p)**(n-1)", "(1-p)**n"], dp=4, p=[0.10, 0.20, 0.15, 0.25], n=[5, 6, 8, 4])

# ---------------- Construction ----------------
F('construction-0001', "A project has four activities. A takes [dA] days and starts the job. B takes [dB] days and C takes [dC] days; both follow A. D takes [dD] days and follows both B and C. What is the total float of activity B?",
  "In the critical path method the longest path through the network sets the project duration, and activities on it have zero float. Total float is the time an activity can slip without delaying the project: late start minus early start.",
  "Path A-B-D = [dA] + [dB] + [dD] = [dA+dB+dD] days. Path A-C-D = [dA] + [dC] + [dD] = [dA+dC+dD] days, which is critical. || B and C run in parallel between the same events, so B can slip by the difference: total float of B = [dC] - [dB] = [ans] days.",
  "max(dC-dB,0)", wrong=["0", "dB", "dC"], fig=lambda e: network(e['dA'], e['dB'], e['dC'], e['dD']), dA=[3, 2, 5, 4], dB=[4, 3, 6, 5], dC=[6, 8, 10, 9], dD=[2, 4, 3, 2])
F('construction-0002', "At a status date a project has a planned value of $[PV], an earned value of $[EV] and an actual cost of $[AC]. What is the cost performance index?",
  "Earned value management compares the budgeted value of work done (EV) with what it cost (AC) and with what was scheduled (PV). CPI = EV / AC; below 1.0 means over budget. SPI = EV / PV; below 1.0 means behind schedule.",
  r"CPI = \frac{EV}{AC} = \frac{[EV]}{[AC]} = [ans|3]. For reference, SPI = \frac{[EV]}{[PV]} = [EV/PV|3].",
  "EV/AC", wrong=["EV/PV", "AC/EV", "PV/EV"], dp=3, PV=[100000, 250000, 80000, 400000], EV=[90000, 260000, 60000, 380000], AC=[95000, 240000, 72000, 410000])
F('construction-0003', "A slab on grade is [L] m long, [W] m wide and [t] mm thick. Allowing [ws]% for waste, how much concrete should be ordered?",
  "Quantity takeoff for concrete is the neat volume from the drawings, increased by a waste allowance for spillage, over-excavation and uneven subgrade. Convert the thickness to metres first.",
  "Neat volume = [L] × [W] × [t/1000|3] = [L*W*t/1000|2] m^{3}. || With [ws]% waste: [L*W*t/1000|2] × [1+ws/100|2] = [ans|2] m^{3}.",
  "L*W*t/1000*(1+ws/100)", dp=2, L=[30, 24, 45, 18], W=[20, 12, 15, 9], t=[150, 200, 125, 100], ws=[5, 8, 5, 10])
F('construction-0004', "An excavator has a [bk|1] m^{3} bucket and a cycle time of [ct] s. It works [mn] minutes of each hour. What is its hourly production?",
  "Equipment production = volume per cycle × cycles per hour × efficiency. The efficiency factor (working minutes per 60) accounts for delays, operator breaks and repositioning.",
  "Cycles per hour = 3,600 / [ct] = [3600/ct]. || Ideal production = [bk|1] × [3600/ct] = [bk*3600/ct|0] m^{3}/h. || Efficiency = [mn] / 60 = [mn/60|3]. || Production = [bk*3600/ct|0] × [mn/60|3] = [ans|0] m^{3}/h.",
  "bk*3600/ct*mn/60", wrong=["bk*3600/ct*(mn/60)**2", "bk*3600/ct", "bk*3600/ct/(mn/60)"], dp=0, bk=[1.5, 2.0, 1.0, 3.0], ct=[30, 40, 20, 45], mn=[50, 45, 48, 55])
F('construction-0006', "On a plan drawn at a scale of 1 in = [sc] ft, a property line measures [ms] in. How long is the line on the ground?",
  "An engineer's scale states how many feet on the ground one inch on the drawing represents. Ground distance = drawing distance × scale.",
  "Ground length = [ms] in × [sc] ft/in = [ans|1] ft.", "sc*ms", dp=1, sc=[40, 20, 50, 100], ms=[3.25, 6.5, 2.4, 1.85])
F('construction-0007', "A drawing is at a scale of 1:[sc]. A wall measures [mm] mm on the drawing. How long is the wall?",
  "A ratio scale of 1:n means one unit on the drawing is n of the same units in reality. Multiply by n, then convert millimetres to metres.",
  "Real length = [mm] mm × [sc] = [mm*sc] mm = [ans] m.", "mm*sc/1000", wrong=["mm*sc/10000", "sc/mm", "mm*sc/100"], sc=[500, 200, 100, 250], mm=[24, 65, 38, 84])
F('construction-0011', "A contractor has [nr] recordable injuries in a year in which employees worked [hrs] hours. What is the incidence rate per 200,000 hours?",
  "The OSHA incidence rate normalises injury counts to 200,000 hours, the hours worked by 100 full-time employees in a year (100 × 40 h × 50 weeks), so that firms of different sizes can be compared.",
  r"Incidence rate = \frac{[nr] × 200,000}{[hrs]} = [ans|2].", "nr*200000/hrs", dp=2, nr=[6, 4, 9, 3], hrs=[400000, 250000, 600000, 120000])
F('construction-0012', "A loader takes [tl] minutes to fill a truck. Each truck needs [tc] minutes for a full cycle including loading. How many trucks keep the loader working without waiting?",
  "A balanced fleet has just enough trucks that one arrives as the loader finishes the previous one. The number is the truck cycle time divided by the loading time. Fewer trucks leave the loader idle; more leave trucks queuing.",
  r"Trucks = \frac{truck cycle time}{loading time} = \frac{[tc]}{[tl]} = [ans].", "tc/tl", wrong=["tc/tl-1", "tc/tl+2", "tc-tl"], tl=[4, 5, 3, 6], tc=[24, 40, 27, 30])
F('construction-0014', "A crew places [rt] m^{2} of formwork per day. There are [ar] m^{2} to place and [cw] crews working. How many working days are needed?",
  "Activity duration = quantity of work / (crew productivity × number of crews). Durations found this way feed the schedule network.",
  r"Daily output = [cw] × [rt] = [cw*rt] m^{2}/day. || Duration = \frac{[ar]}{[cw*rt]} = [ans] working days.", "ar/(rt*cw)", rt=[40, 55, 30, 80], ar=[1200, 3300, 900, 2400], cw=[2, 3, 2, 4])
F('construction-0015', "A job needs [qy] m^{3} of excavation at a direct cost of $[uc] per m^{3}. Overhead and profit add [mk]%. What is the bid price for this item?",
  "A bid item price is its direct cost (quantity × unit cost) plus a markup that covers overhead and profit.",
  "Direct cost = [qy] × [uc] = $[qy*uc|0]. || Bid price = [qy*uc|0] × [1+mk/100|2] = $[ans|0].", "qy*uc*(1+mk/100)", dp=0, qy=[850, 1200, 430, 2500], uc=[12, 9.5, 28, 6.4], mk=[15, 12, 20, 18])
F('construction-0016', "A concrete wall is [L] m long and [H] m high. What area of formwork is needed to form both faces?",
  "Formwork is measured as contact area, the surface of concrete that touches the forms. A wall has two faces, so the contact area is 2 × length × height (ends ignored here).",
  "Contact area = 2 × [L] × [H] = [ans] m^{2}.", "2*L*H", wrong=["L*H", "3*L*H", "4*L*H"], L=[10, 18, 7.5, 24], H=[3, 2.4, 4, 3.6])
if __name__ == '__main__': save()
