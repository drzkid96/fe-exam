"""Version families, part 1: statics, dynamics, mechanics of materials, structural."""
from author_v import *
def F(base, stem, concept, sol, ans, wrong=None, dp=None, fig=None, sfig=None, **P): V(base, stem, P, ans, sol, wrong, dp, fig, sfig, concept)
def lsec(t, H, B):
    k = 130 / max(H, t + B); x, y = 120, 20
    s = f"<path d='M{x} {y} L{x+t*k:.0f} {y} L{x+t*k:.0f} {y+(H-t)*k:.0f} L{x+(t+B)*k:.0f} {y+(H-t)*k:.0f} L{x+(t+B)*k:.0f} {y+H*k:.0f} L{x} {y+H*k:.0f} Z' fill='{CR}' stroke='{SL}' stroke-width='2'/>"
    s += T(x - 8, y + H * k / 2, f"{nf(H)} mm", a='end') + T(x + t * k / 2, y - 6, f"{nf(t)} mm") + T(x + (t + B / 2) * k, y + H * k + 16, f"{nf(B)} mm") + T(x + (t + B) * k + 8, y + (H - t / 2) * k + 4, f"{nf(t)} mm", a='start')
    return {'viewBox': f"0 0 400 {y + H * k + 26:.0f}", 'svg': s, 'alt': f"An L-shaped area: a vertical leg {nf(t)} mm wide and {nf(H)} mm tall with a horizontal leg {nf(B)} mm wide and {nf(t)} mm tall at the bottom right."}

# ---------------- Statics ----------------
F('statics-0001', "A [F1] N force acts along the positive x-axis. A [F2] N force acts at the same point, [th]° above the positive x-axis. What is the magnitude of the resultant?",
  "Concurrent forces add as vectors. Resolve each force into x and y components, add the components, then recombine with the Pythagorean theorem. The resultant is always less than the arithmetic sum unless the forces are parallel.",
  r"R_{x} = [F1] + [F2] cos [th]° = [F1+F2*cos(rad(th))|1] N. || R_{y} = [F2] sin [th]° = [F2*sin(rad(th))|1] N. || R = \sqrt{[F1+F2*cos(rad(th))|1]^{2} + [F2*sin(rad(th))|1]^{2}} = [ans|1] N.",
  "sqrt(F1**2+F2**2+2*F1*F2*cos(rad(th)))", dp=1, fig=lambda e: forces(e['F1'], e['F2'], e['th']), F1=[100, 120, 90, 150], F2=[80, 50, 60, 100], th=[60, 40, 30, 70])
F('statics-0002', "A simply supported beam spans [L] m between a pin at A and a roller at B. A single [P] kN load acts [a] m from A. What is the vertical reaction at A?",
  "A beam in equilibrium satisfies two conditions: the moments about any point sum to zero and the vertical forces sum to zero. Taking moments about A removes A_{y} from the equation and gives B_{y} directly. The support nearer the load carries the larger share.",
  "Moments about A: B_{y}([L]) = [P]([a]), so B_{y} = [P*a/L] kN. || Vertical forces: A_{y} = [P] - [P*a/L] = [ans] kN. || Check with the lever rule: A_{y} = [P] × ([L] - [a]) / [L] = [ans] kN.",
  "P - P*a/L", wrong=["P*a/L", "P/2", "P"], fig=lambda e: beam(e['L'], [(e['a'], e['P'])]), sfig=lambda e: beam(e['L'], [(e['a'], e['P'])], R=(e['ans'], e['P'] - e['ans'])), L=[6, 8, 10, 9], P=[30, 40, 25, 36], a=[2, 3, 4, 6])
F('statics-0003', "A T-shaped section has a flange [bf] mm wide and [tf] mm thick on top of a web [tw] mm wide and [hw] mm tall. How far is the centroid above the bottom of the web?",
  "The centroid of a composite area is the area-weighted average of the centroids of its parts: y-bar = (sum of A × y) / (sum of A). Measure every y from the same datum, here the bottom of the web.",
  r"Web: A = [tw] × [hw] = [tw*hw] mm^{2}, centre [hw/2] mm above the bottom. || Flange: A = [bf] × [tf] = [bf*tf] mm^{2}, centre [hw] + [tf/2] = [hw+tf/2] mm above the bottom. || y-bar = \frac{[tw*hw]([hw/2]) + [bf*tf]([hw+tf/2])}{[tw*hw] + [bf*tf]} = \frac{[tw*hw*hw/2+bf*tf*(hw+tf/2)]}{[tw*hw+bf*tf]} = [ans|1] mm.",
  "(tw*hw*hw/2 + bf*tf*(hw+tf/2))/(tw*hw+bf*tf)", wrong=["(hw+tf)/2", "(hw/2+hw+tf/2)/2", "hw+tf-(tw*hw*hw/2 + bf*tf*(hw+tf/2))/(tw*hw+bf*tf)"], dp=1,
  fig=lambda e: tsec(e['bf'], e['tf'], e['tw'], e['hw']), bf=[100, 120, 150, 80], tf=[20, 20, 30, 10], tw=[20, 30, 30, 20], hw=[80, 100, 120, 60])
F('statics-0004', "A crate rests on a ramp. The coefficient of static friction between the crate and the ramp is [mu|2]. What is the steepest ramp angle at which the crate stays put?",
  "On an incline the weight component along the slope is W sin(angle) and the largest friction force available is (coefficient) × W cos(angle). Sliding is about to start when these are equal, which gives tan(angle) = coefficient of static friction. The weight cancels, so the angle does not depend on it.",
  "At impending motion: W sin(angle) = [mu|2] × W cos(angle). || tan(angle) = [mu|2], so angle = arctan([mu|2]) = [ans|1]°.",
  "atan(mu)*180/pi", wrong=["mu*45", "asin(mu)*180/pi", "90-atan(mu)*180/pi"], dp=1, fig=lambda e: incline(0, 'Coefficient of static friction ' + nf(e['mu'], 2)), mu=[0.50, 0.30, 0.40, 0.60])
F('statics-0005', "A rectangular section is [b] mm wide and [h] mm deep. What is its moment of inertia about the horizontal axis through its centroid? Give the answer in units of 10^{6} mm^{4}.",
  "For a rectangle about its own centroidal axis, I = b h^{3} / 12, where h is the dimension perpendicular to the axis. Depth is cubed, so doubling the depth gives eight times the stiffness.",
  r"I = \frac{b h^{3}}{12} = \frac{[b]([h])^{3}}{12} = [b*h**3/12/1e6|2] × 10^{6} mm^{4}.",
  "b*h**3/12/1e6", dp=2, fig=lambda e: rect(e['b'], e['h']), b=[100, 150, 120, 200], h=[200, 300, 240, 400])
F('statics-0006', "Two parallel [Fc] N forces act in opposite directions, [d] m apart. What is the moment of this couple?",
  "A couple is two equal, opposite, parallel forces. Its moment is force × perpendicular distance between the lines of action, and it is the same about every point, so a couple is a free vector.",
  "M = F d = [Fc] × [d] = [ans] N·m.", "Fc*d", Fc=[50, 80, 120, 200], d=[0.4, 0.25, 0.5, 0.15])
F('statics-0007', "A [Fc] N downward force acts [d] m to the right of point O. It is replaced by a force at O plus a couple. What is the magnitude of the couple?",
  "A force can be moved to a parallel line of action if a couple is added equal to the moment of the original force about the new point. The force keeps its magnitude and direction; the couple is M = F d.",
  "The equivalent system at O is a [Fc] N downward force plus a couple M = F d = [Fc] × [d] = [ans] N·m (clockwise).",
  "Fc*d", wrong=["Fc*d/10", "Fc", "Fc/d"], Fc=[200, 150, 400, 250], d=[0.3, 0.4, 0.25, 0.6])
F('statics-0008', "A symmetric triangular truss spans [span] m and is [h] m high. A [P] kN load acts at the apex. What is the force in each inclined member?",
  "Use the method of joints at a support. Only the inclined member has a vertical component there, so its vertical component must equal the support reaction. The member force is the reaction divided by the sine of the member's angle.",
  r"By symmetry each reaction is [P] / 2 = [P/2] kN. || Inclined member length = \sqrt{[span/2]^{2} + [h]^{2}} = [hypot(span/2,h)] m, so sin(angle) = [h] / [hypot(span/2,h)]. || Joint at the support, vertical forces: F × \frac{[h]}{[hypot(span/2,h)]} = [P/2], so F = [ans] kN (compression).",
  "P/2*hypot(span/2,h)/h", wrong=["P/2", "P/2*hypot(span/2,h)/(span/2)", "P/2*(span/2)/h"], fig=lambda e: truss(e['span'], e['h'], e['P']), span=[8, 6, 10, 12], h=[3, 4, 12, 2.5], P=[24, 40, 48, 30])
F('statics-0009', "A symmetric triangular truss spans [span] m and is [h] m high. A [P] kN load acts at the apex. What is the force in the horizontal bottom member?",
  "At a support joint the horizontal component of the inclined member must be balanced by the bottom member. The inclined member is in compression, so the bottom chord is in tension and acts as a tie.",
  r"Each reaction is [P/2] kN. The inclined member carries a vertical component of [P/2] kN, so its horizontal component is [P/2] × \frac{[span/2]}{[h]} = [ans] kN. || Horizontal forces at the support joint: bottom member force = [ans] kN (tension).",
  "P/2*(span/2)/h", dp=2, fig=lambda e: truss(e['span'], e['h'], e['P']), span=[8, 6, 10, 12], h=[3, 4, 12, 2.5], P=[24, 40, 48, 30])
F('statics-0010', "A [Fa] N force is applied to the end of a [L] m lever, at [th]° to the lever's axis. What is the moment about the pivot?",
  "Only the force component perpendicular to the lever arm produces moment: M = F L sin(angle between force and arm). The component along the arm passes through the pivot and contributes nothing.",
  "Perpendicular component = [Fa] sin [th]° = [Fa*sin(rad(th))|1] N. || M = [Fa*sin(rad(th))|1] × [L] = [ans|1] N·m.",
  "Fa*L*sin(rad(th))", wrong=["Fa*sin(rad(th))", "Fa*L*cos(rad(th))", "Fa*L"], fig=lambda e: lever(e['L'], e['Fa'], e['th']), Fa=[150, 200, 120, 80], L=[2, 1.5, 2.5, 3], th=[30, 40, 60, 25])
F('statics-0011', "A simply supported beam spans [L] m. It carries a uniform load of [w] kN/m over its full length and a [P] kN point load at midspan. What is each support reaction?",
  "Replace the uniform load by its resultant, w L, acting at midspan. With every load centred, the loading is symmetric and each support carries half of the total.",
  "Total load = [w]([L]) + [P] = [w*L+P] kN. || By symmetry each reaction = [w*L+P] / 2 = [ans] kN.",
  "(w*L+P)/2", fig=lambda e: beam(e['L'], [(e['L'] / 2, e['P'])], w=e['w']), L=[10, 8, 12, 6], w=[4, 6, 5, 10], P=[20, 30, 24, 18])
F('statics-0012', "An L-shaped area is made of a vertical leg [t] mm wide and [H] mm tall, with a horizontal leg [B] mm wide and [t] mm tall attached to the bottom of its right side. How far is the centroid from the left edge?",
  "Split the shape into rectangles, then take the area-weighted average of their centroid distances from the left edge: x-bar = (sum of A × x) / (sum of A).",
  r"Vertical leg: A = [t*H] mm^{2}, x = [t/2] mm. || Horizontal leg: A = [B*t] mm^{2}, x = [t] + [B/2] = [t+B/2] mm. || x-bar = \frac{[t*H]([t/2]) + [B*t]([t+B/2])}{[t*H] + [B*t]} = [ans|1] mm.",
  "(t*H*t/2 + B*t*(t+B/2))/(t*H+B*t)", wrong=["t", "(t/2+t+B/2)/2", "(t+B)/2"], dp=1, fig=lambda e: lsec(e['t'], e['H'], e['B']), t=[20, 10, 30, 20], H=[80, 60, 90, 100], B=[60, 50, 60, 40])
F('statics-0013', "A rectangle is [b] mm wide and [h] mm tall. What is its moment of inertia about its base? Give the answer in units of 10^{6} mm^{4}.",
  "The parallel axis theorem moves a moment of inertia from the centroidal axis to a parallel axis: I = I_{c} + A d^{2}. For a rectangle about its base, d = h/2, which gives I = b h^{3} / 3, four times the centroidal value.",
  r"I_{c} = \frac{[b]([h])^{3}}{12} = [b*h**3/12/1e6|2] × 10^{6} mm^{4}. || A d^{2} = ([b] × [h])([h/2])^{2} = [b*h*(h/2)**2/1e6|2] × 10^{6} mm^{4}. || I_{base} = [b*h**3/12/1e6|2] + [b*h*(h/2)**2/1e6|2] = [ans|1] × 10^{6} mm^{4}, the same as b h^{3} / 3.",
  "b*h**3/3/1e6", dp=1, fig=lambda e: rect(e['b'], e['h']), b=[100, 80, 150, 120], h=[200, 150, 200, 300])
F('statics-0014', "A [W] N crate sits on a level floor with a static friction coefficient of [mu|2]. A rope pulls on it at [th]° above the horizontal. What rope force starts the crate moving?",
  "The upward component of the rope force reduces the normal force, which reduces the friction available. Write equilibrium in both directions at impending motion: horizontal pull = coefficient × (weight minus vertical pull).",
  r"Normal force: N = [W] - P sin [th]°. || Impending motion: P cos [th]° = [mu|2]([W] - P sin [th]°). || P = \frac{[mu|2]([W])}{cos [th]° + [mu|2] sin [th]°} = \frac{[mu*W]}{[cos(rad(th))+mu*sin(rad(th))|3]} = [ans|1] N.",
  "mu*W/(cos(rad(th))+mu*sin(rad(th)))", dp=1, W=[500, 800, 600, 400], mu=[0.35, 0.25, 0.40, 0.30], th=[30, 20, 25, 35])
F('statics-0015', "A [W] N weight hangs from two cables. Each cable makes an angle of [th]° with the horizontal. What is the tension in each cable?",
  "At the joint the vertical components of the two cable tensions must carry the weight: 2 T sin(angle) = W. The flatter the cables, the larger the tension, and it grows without limit as the angle approaches zero.",
  r"Vertical forces at the joint: 2 T sin [th]° = [W]. || T = \frac{[W]}{2 sin [th]°} = \frac{[W]}{[2*sin(rad(th))|3]} = [ans|0] N.",
  "W/(2*sin(rad(th)))", wrong=["W/2", "W/(2*cos(rad(th)))", "W*cos(rad(th))"], dp=0, fig=lambda e: cables(e['W'], e['th']), W=[1000, 600, 800, 1200], th=[30, 20, 25, 35])

# ---------------- Dynamics ----------------
F('dynamics-0001', "A car starts from rest and accelerates uniformly to [v] m/s in [t] s. How far does it travel in that time?",
  "With constant acceleration, velocity rises linearly, so the average velocity is the mean of the start and end values. Distance = average velocity × time, which is the area under the velocity-time line.",
  r"Acceleration a = [v] / [t] = [v/t|2] m/s^{2}. || s = \frac{1}{2} a t^{2} = \frac{1}{2}([v/t|2])([t])^{2} = [ans|1] m. || Check: average speed [v/2] m/s × [t] s = [ans|1] m.",
  "v*t/2", wrong=["v*t/3", "v*t", "1.5*v*t"], dp=1, v=[27, 20, 30, 24], t=[9, 8, 12, 6])
F('dynamics-0002', "A [m] kg crate is pulled along a level floor by a [Fp] N horizontal force. The coefficient of kinetic friction is [mu|2]. What is the acceleration of the crate? Use g = 9.81 m/s^{2}.",
  "Newton's second law uses the net force. Kinetic friction equals the coefficient times the normal force, and on a level floor with a horizontal pull the normal force equals the weight.",
  r"N = m g = [m](9.81) = [m*9.81|1] N. || Friction = [mu|2] × [m*9.81|1] = [mu*m*9.81|1] N. || a = \frac{[Fp] - [mu*m*9.81|1]}{[m]} = [ans|2] m/s^{2}.",
  "(Fp-mu*m*g)/m", dp=2, m=[50, 40, 80, 25], Fp=[300, 250, 500, 150], mu=[0.30, 0.25, 0.40, 0.20])
F('dynamics-0003', "A [m] kg ball is dropped from rest from a height of [h] m. Ignoring air resistance, how fast is it moving just before it lands? Use g = 9.81 m/s^{2}.",
  "With no air resistance, mechanical energy is conserved: m g h of potential energy becomes (1/2) m v^{2} of kinetic energy. The mass cancels, so v = square root of 2 g h for any object.",
  r"m g h = \frac{1}{2} m v^{2}, so v = \sqrt{2 g h} = \sqrt{2(9.81)([h])} = [ans|1] m/s. The [m] kg mass is not needed.",
  "sqrt(2*g*h)", wrong=["sqrt(g*h)", "2*sqrt(g*h)", "g*h"], dp=1, m=[2, 5, 1, 3], h=[10, 20, 5, 15])
F('dynamics-0004', "A thin uniform rod has a mass of [m] kg and a length of [L] m. What is its mass moment of inertia about an axis through one end, perpendicular to the rod?",
  "For a slender rod, I = m L^{2} / 12 about its centre. The parallel axis theorem moves it to the end: I = m L^{2} / 12 + m (L/2)^{2} = m L^{2} / 3. Moving the axis away from the centre of mass always increases I.",
  r"I_{end} = \frac{m L^{2}}{3} = \frac{[m]([L])^{2}}{3} = [ans] kg·m^{2}.",
  "m*L**2/3", wrong=["m*L**2/12", "m*L**2/4", "m*L**2"], m=[6, 3, 12, 9], L=[2, 4, 1, 2])
F('dynamics-0005', "A ball is launched from level ground at [v] m/s, at [th]° above the horizontal. Ignoring air resistance, how far away does it land? Use g = 9.81 m/s^{2}.",
  "Projectile motion is constant horizontal velocity combined with constant downward acceleration. On level ground the time of flight is 2 v sin(angle) / g, and the range is R = v^{2} sin(2 × angle) / g.",
  r"Time of flight = \frac{2([v]) sin [th]°}{9.81} = [2*v*sin(rad(th))/g|2] s. || Horizontal speed = [v] cos [th]° = [v*cos(rad(th))|2] m/s. || Range = [v*cos(rad(th))|2] × [2*v*sin(rad(th))/g|2] = [ans|1] m.",
  "v**2*sin(rad(2*th))/g", wrong=["v**2*sin(rad(2*th))/g/2", "v**2/(2*g)", "v**2/g"], dp=1, fig=lambda e: projectile(e['v'], e['th']), v=[20, 25, 30, 15], th=[30, 20, 35, 25])
F('dynamics-0006', "A car travels at a constant [v] m/s around a curve of radius [r] m. What is its acceleration toward the centre of the curve?",
  "Constant speed on a curve still means acceleration, because the direction of the velocity changes. The normal (centripetal) acceleration is v^{2} / r, directed toward the centre of curvature.",
  r"a_{n} = \frac{v^{2}}{r} = \frac{[v]^{2}}{[r]} = [ans|2] m/s^{2}.", "v**2/r", dp=2, v=[20, 15, 30, 25], r=[80, 50, 200, 125])
F('dynamics-0007', "A solid uniform disk has a mass of [m] kg and a radius of [r] m. What is its mass moment of inertia about its central axis?",
  "For a solid disk or cylinder about its axis, I = m r^{2} / 2. A thin ring with the same mass and radius has I = m r^{2}, twice as much, because all its mass sits at the full radius.",
  r"I = \frac{1}{2} m r^{2} = \frac{1}{2}([m])([r])^{2} = [ans|3] kg·m^{2}.",
  "m*r**2/2", wrong=["m*r**2/4", "m*r**2", "m*r"], dp=3, m=[10, 20, 8, 50], r=[0.3, 0.2, 0.5, 0.4])
F('dynamics-0008', "A block slides down a frictionless incline at [th]° to the horizontal. What is its acceleration? Use g = 9.81 m/s^{2}.",
  "Resolve the weight along and perpendicular to the slope. Only the component along the slope, m g sin(angle), accelerates the block; the perpendicular component is balanced by the normal force. The mass cancels.",
  "a = g sin [th]° = 9.81 × [sin(rad(th))|3] = [ans|2] m/s^{2}.",
  "g*sin(rad(th))", wrong=["g*tan(rad(th))", "g*cos(rad(th))", "g"], dp=2, fig=lambda e: incline(e['th']), th=[30, 20, 40, 25])
F('dynamics-0009', "A net torque of [Tq] N·m acts on a flywheel with a mass moment of inertia of [I] kg·m^{2}. What is its angular acceleration?",
  "Rotation about a fixed axis follows the rotational form of Newton's second law: net torque = I × angular acceleration. It is the direct counterpart of F = m a.",
  r"Angular acceleration = \frac{T}{I} = \frac{[Tq]}{[I]} = [ans] rad/s^{2}.", "Tq/I", Tq=[12, 30, 45, 8], I=[3, 6, 15, 0.5])
F('dynamics-0010', "A hoist lifts a [m] kg load at a constant [v] m/s. What power is delivered to the load? Use g = 9.81 m/s^{2}.",
  "Power is force times velocity in the direction of the force. At constant speed the hoist force equals the weight, so P = m g v.",
  "Force = m g = [m](9.81) = [m*9.81|0] N. || P = F v = [m*9.81|0] × [v] = [m*9.81*v|0] W = [ans|2] kW.",
  "m*g*v/1000", wrong=["m*v/1000", "m*g*v/2000", "2*m*g*v/1000"], dp=2, m=[500, 800, 300, 1200], v=[2, 1.5, 3, 0.5])
F('dynamics-0011', "A spring with a stiffness of [k] N/m is compressed [x] m and released against a [m] kg block on a frictionless surface. What speed does the block reach?",
  "Energy is conserved: the elastic energy stored in the spring, (1/2) k x^{2}, becomes the kinetic energy of the block, (1/2) m v^{2}.",
  r"\frac{1}{2}([k])([x])^{2} = [0.5*k*x*x|2] J of spring energy. || \frac{1}{2}([m]) v^{2} = [0.5*k*x*x|2], so v = \sqrt{\frac{2([0.5*k*x*x|2])}{[m]}} = [ans|2] m/s.",
  "x*sqrt(k/m)", dp=2, k=[2000, 5000, 800, 1200], x=[0.1, 0.08, 0.15, 0.2], m=[0.5, 2, 0.4, 3])

# ---------------- Mechanics of materials ----------------
F('mechmat-0001', "A [d] mm diameter steel rod carries a [P] kN tensile load. What is the axial stress?",
  "Average normal stress is force divided by the cross-sectional area perpendicular to the force. With newtons and square millimetres the result is in MPa.",
  r"A = \frac{π([d])^{2}}{4} = [pi*d*d/4|1] mm^{2}. || Stress = \frac{P}{A} = \frac{[P*1000] N}{[pi*d*d/4|1] mm^{2}} = [ans|1] MPa.",
  "P*1000/(pi*d*d/4)", wrong=["P*1000/(pi*d*d/4)/2", "P*1000/(d*d)", "P*1000/(pi*d*d/4)*2"], dp=1, fig=lambda e: bar(e['d'], None, e['P']), d=[20, 25, 16, 30], P=[50, 80, 40, 120])
F('mechmat-0002', "A rod is [d] mm in diameter and [L] m long. It carries a [P] kN tensile load. The modulus of elasticity is [E] GPa. How much does the rod stretch?",
  "In the elastic range, stress = E × strain. Combining stress = P/A and strain = elongation/L gives elongation = P L / (A E). Keep units consistent: N, mm and MPa.",
  r"A = \frac{π([d])^{2}}{4} = [pi*d*d/4|1] mm^{2}. || Elongation = \frac{P L}{A E} = \frac{([P*1000])([L*1000])}{([pi*d*d/4|1])([E*1000])} = [ans|2] mm.",
  "P*1000*L*1000/(pi*d*d/4*E*1000)", dp=2, fig=lambda e: bar(e['d'], e['L'], e['P']), d=[20, 25, 16, 30], L=[2, 3, 1.5, 4], P=[50, 80, 40, 120], E=[200, 200, 200, 70])
F('mechmat-0003', "A simply supported beam spans [L] m and carries a uniform load of [w] kN/m over its full length. What is the maximum bending moment?",
  "For a simply supported beam under full uniform load, shear is zero at midspan, so the moment peaks there: M_{max} = w L^{2} / 8. It equals the area under the shear diagram from the support to midspan.",
  r"Reaction = [w]([L]) / 2 = [w*L/2] kN. || M_{max} = \frac{w L^{2}}{8} = \frac{[w]([L])^{2}}{8} = [ans] kN·m, at midspan.",
  "w*L**2/8", wrong=["w*L**2/16", "w*L**2/4", "w*L**2/2"], fig=lambda e: beam(e['L'], w=e['w']), sfig=lambda e: beam(e['L'], w=e['w'], R=(e['w'] * e['L'] / 2, e['w'] * e['L'] / 2)), L=[8, 6, 10, 4], w=[10, 12, 8, 25])
F('mechmat-0004', "At a point in a plate, the normal stresses on two perpendicular faces are [sx] MPa and [sy] MPa (tension positive). The shear stress on those faces is [txy] MPa. What is the maximum principal stress?",
  "Principal stresses are the largest and smallest normal stresses at a point, found on the planes where shear is zero. On Mohr's circle the centre is the average normal stress and the radius is the square root of ((difference/2)^{2} + shear^{2}); the maximum principal stress is centre + radius.",
  r"Centre = \frac{[sx] + ([sy])}{2} = [(sx+sy)/2] MPa. || Radius = \sqrt{(\frac{[sx] - ([sy])}{2})^{2} + [txy]^{2}} = [hypot((sx-sy)/2,txy)] MPa. || Maximum principal stress = [(sx+sy)/2] + [hypot((sx-sy)/2,txy)] = [ans] MPa.",
  "(sx+sy)/2+hypot((sx-sy)/2,txy)", wrong=["(sx+sy)/2", "(sx+sy)/2+txy", "sx+abs(sy)+txy"], fig=lambda e: stressblock(e['sx'], e['sy'], e['txy']), sfig=lambda e: mohr(e['sx'], e['sy'], e['txy']), sx=[80, 100, 90, 120], sy=[20, 40, -30, 60], txy=[40, 40, 80, 40])
F('mechmat-0005', "A rectangular beam is [b] mm wide and [h] mm deep. It carries a bending moment of [M] kN·m about its strong axis. What is the maximum bending stress?",
  "Bending stress varies linearly from zero at the neutral axis to a maximum at the extreme fibre: stress = M c / I = M / S. For a rectangle the section modulus is S = b h^{2} / 6.",
  r"S = \frac{b h^{2}}{6} = \frac{[b]([h])^{2}}{6} = [b*h*h/6|0] mm^{3}. || Stress = \frac{M}{S} = \frac{[M] × 10^{6} N·mm}{[b*h*h/6|0] mm^{3}} = [ans|1] MPa.",
  "M*1e6*6/(b*h*h)", wrong=["M*1e6*3/(b*h*h)", "M*1e6*12/(b*h*h)", "M*1e6*24/(b*h*h)"], dp=1, fig=lambda e: rect(e['b'], e['h']), b=[100, 150, 200, 120], h=[200, 300, 400, 240], M=[20, 90, 160, 50])
F('mechmat-0008', "A simply supported beam spans [L] m and carries a uniform load of [w] kN/m. What is the maximum shear force?",
  "Shear is largest where the beam meets its supports and equals the reaction there. For a full uniform load each reaction is w L / 2, and shear falls linearly to zero at midspan.",
  r"V_{max} = \frac{w L}{2} = \frac{[w]([L])}{2} = [ans] kN, at each support.",
  "w*L/2", wrong=["w*L/4", "w*L", "2*w*L"], fig=lambda e: beam(e['L'], w=e['w']), L=[8, 6, 10, 5], w=[10, 15, 12, 24])
F('mechmat-0009', "A solid circular shaft [d] mm in diameter carries a torque of [Tq] kN·m. What is the maximum shear stress?",
  "Torsional shear stress in a circular shaft grows linearly with radius: stress = T r / J. For a solid shaft J = π d^{4} / 32, so the maximum, at the surface, is 16 T / (π d^{3}).",
  r"Maximum shear stress = \frac{16 T}{π d^{3}} = \frac{16([Tq] × 10^{6})}{π([d])^{3}} = [ans|1] MPa.",
  "16*Tq*1e6/(pi*d**3)", wrong=["4*Tq*1e6/(pi*d**3)", "8*Tq*1e6/(pi*d**3)", "32*Tq*1e6/(pi*d**3)"], dp=1, d=[50, 60, 40, 80], Tq=[2, 4, 1.2, 10])
F('mechmat-0010', "A metal bar is held rigidly between two walls and heated by [dT] °C. Its coefficient of thermal expansion is [al] × 10^{-6} per °C and E = [E] GPa. What compressive stress develops?",
  "A free bar would lengthen by (coefficient × temperature change × L). The walls prevent that, which is the same as compressing the bar by the same strain. Stress = E × coefficient × temperature change, independent of length and area.",
  "Restrained strain = [al] × 10^{-6} × [dT] = [al*dT] × 10^{-6}. || Stress = E × strain = ([E*1000] MPa)([al*dT] × 10^{-6}) = [ans|1] MPa (compression).",
  "al*1e-6*dT*E*1000", dp=1, al=[12, 12, 23, 17], dT=[40, 60, 30, 50], E=[200, 200, 70, 110])
F('mechmat-0011', "A steel rail [L] m long warms by [dT] °C. Its coefficient of thermal expansion is [al] × 10^{-6} per °C. How much longer does it get if it is free to expand?",
  "Free thermal expansion: change in length = coefficient × temperature change × original length. No stress develops because nothing resists the movement.",
  "Change in length = ([al] × 10^{-6})([dT])([L*1000] mm) = [ans|2] mm.",
  "al*1e-6*dT*L*1000", dp=2, L=[10, 25, 12, 40], dT=[30, 40, 50, 25], al=[12, 12, 12, 12])
F('mechmat-0012', "The principal stresses at a point are [s1] MPa in tension and [s2] MPa in compression. What is the maximum in-plane shear stress?",
  "The maximum in-plane shear stress is the radius of Mohr's circle, half the difference between the principal stresses. Compression is negative, so a tension and a compression add when you take the difference.",
  r"Maximum shear = \frac{[s1] - (-[s2])}{2} = \frac{[s1+s2]}{2} = [ans] MPa.",
  "(s1+s2)/2", wrong=["(s1-s2)/2", "s1", "s1+s2"], s1=[120, 100, 150, 90], s2=[40, 60, 50, 30])
F('mechmat-0013', "A thin-walled cylindrical tank has a radius of [r] mm and a wall thickness of [t] mm. The internal pressure is [p] MPa. What is the hoop stress in the wall?",
  "In a thin-walled cylinder the circumferential (hoop) stress is p r / t and the longitudinal stress is p r / (2 t). The hoop stress is twice the longitudinal stress, which is why such vessels split along their length.",
  r"Hoop stress = \frac{p r}{t} = \frac{[p]([r])}{[t]} = [ans] MPa. The longitudinal stress is half of that, [p*r/t/2] MPa.",
  "p*r/t", wrong=["p*r/t/4", "p*r/t/2", "2*p*r/t"], r=[500, 400, 600, 750], t=[10, 8, 12, 15], p=[2, 1.5, 1.2, 3])

# ---------------- Structural ----------------
F('structural-0002', "A steel column is [L] m long with pinned ends. E = 200 GPa and the moment of inertia about the weak axis is [I|1] × 10^{6} mm^{4}. What is the Euler buckling load?",
  "A slender column fails by elastic buckling at the Euler load, P_{cr} = π^{2} E I / (K L)^{2}. Pinned ends give K = 1. Buckling happens about the axis with the smaller moment of inertia.",
  r"P_{cr} = \frac{π^{2} E I}{(K L)^{2}} = \frac{π^{2}(200,000)([I|1] × 10^{6})}{([L*1000])^{2}} = [ans*1000|0] N = [ans|0] kN.",
  "pi**2*200000*I*1e6/(L*1000)**2/1000", dp=0, fig=lambda e: column(e['L'], 1), L=[4, 3, 5, 6], I=[8.0, 4.5, 20, 36])
F('structural-0003', "A simply supported beam spans [L] m and carries a [P] kN point load at midspan. Its flexural stiffness EI is [EI] kN·m^{2}. What is the midspan deflection?",
  "For a simply supported beam with a central point load, the maximum deflection is P L^{3} / (48 EI), at midspan. Span is cubed, so deflection is very sensitive to length.",
  r"Deflection = \frac{P L^{3}}{48 EI} = \frac{[P]([L])^{3}}{48([EI])} = [P*L**3/(48*EI)|5] m = [ans|2] mm.",
  "P*L**3/(48*EI)*1000", wrong=["P*L**3/(96*EI)*1000", "P*L**3/(24*EI)*1000", "P*L**3/(12*EI)*1000"], dp=2, fig=lambda e: beam(e['L'], [(e['L'] / 2, e['P'])]), L=[6, 8, 5, 4], P=[20, 30, 48, 60], EI=[30000, 40000, 50000, 20000])
F('structural-0004', "A floor beam carries a dead load of [D] kN/m and a live load of [Lv] kN/m. Checking the load combinations 1.4D and 1.2D + 1.6L, what factored load governs?",
  "In strength design (LRFD) each load is multiplied by a load factor that reflects its uncertainty, and the largest combination governs. Live load has the larger factor because it is less predictable than dead load.",
  "1.4D = 1.4([D]) = [1.4*D] kN/m. || 1.2D + 1.6L = 1.2([D]) + 1.6([Lv]) = [1.2*D+1.6*Lv] kN/m. || The larger value governs: [ans] kN/m.",
  "max(1.4*D, 1.2*D+1.6*Lv)", wrong=["1.4*D", "D+Lv", "1.6*(D+Lv)"], D=[20, 15, 30, 12], Lv=[30, 25, 20, 40])
F('structural-0005', "A singly reinforced concrete beam is [b] mm wide with an effective depth of [d] mm. It has [As] mm^{2} of tension steel with a yield strength of 420 MPa, and the concrete strength is [fc] MPa. Assuming the steel yields, what is the nominal moment capacity?",
  "At nominal strength the steel force T = A_{s} f_{y} is balanced by a rectangular concrete stress block of intensity 0.85 f'_{c} and depth a. The moment capacity is that force times the lever arm between them, d - a/2.",
  r"a = \frac{A_{s} f_{y}}{0.85 f'_{c} b} = \frac{[As](420)}{0.85([fc])([b])} = [As*420/(0.85*fc*b)|1] mm. || M_{n} = A_{s} f_{y}(d - \frac{a}{2}) = [As](420)([d] - [As*420/(1.7*fc*b)|1]) = [ans|0] × 10^{6} N·mm = [ans|0] kN·m.",
  "As*420*(d-As*420/(1.7*fc*b))/1e6", wrong=["As*420*(d-As*420/(0.85*fc*b))/1e6", "As*420*d/1e6", "As*420*(d+As*420/(1.7*fc*b))/1e6"], dp=0,
  fig=lambda e: rcbeam(e['b'], e['d'], e['As']), sfig=lambda e: rcbeam(e['b'], e['d'], e['As'], e['As'] * 420 / (0.85 * e['fc'] * e['b'])), b=[300, 350, 250, 400], d=[500, 550, 450, 600], As=[1500, 2000, 1200, 2400], fc=[28, 28, 35, 21])
F('structural-0006', "A cantilever beam is [L] m long and carries a [P] kN point load at its free end. What is the magnitude of the bending moment at the fixed support?",
  "A cantilever resists load through shear and moment at its fixed end. For a tip load the moment grows linearly from zero at the free end to P L at the support.",
  "M = P L = [P] × [L] = [ans] kN·m at the fixed support (tension on the top face).",
  "P*L", wrong=["P", "P*L/2", "1.5*P*L"], fig=lambda e: beam(e['L'], [(e['L'], e['P'])], kind='cantilever'), L=[3, 2.5, 4, 5], P=[12, 20, 15, 18])
F('structural-0007', "A simply supported beam spans [L] m. It carries a uniform load of [w] kN/m over the full span and a [P] kN point load [a] m from the left support. What is the left reaction?",
  "Reactions from several loads can be found one load at a time and added (superposition). The uniform load splits equally; the point load splits in inverse proportion to its distance from each support.",
  r"From the uniform load: [w]([L]) / 2 = [w*L/2] kN. || From the point load: [P] × \frac{[L] - [a]}{[L]} = [P*(L-a)/L|2] kN. || Left reaction = [w*L/2] + [P*(L-a)/L|2] = [ans|1] kN.",
  "w*L/2+P*(L-a)/L", dp=1, fig=lambda e: beam(e['L'], [(e['a'], e['P'])], w=e['w']), L=[6, 8, 10, 5], w=[5, 4, 6, 8], P=[10, 24, 15, 20], a=[2, 2, 4, 3])
F('structural-0008', "A simply supported beam spans [L] m and carries a [P] kN point load at midspan. What is the maximum bending moment?",
  "With a central point load each reaction is P/2, and the moment under the load is the reaction times half the span: M_{max} = P L / 4.",
  r"Reaction = [P] / 2 = [P/2] kN. || M_{max} = [P/2] × [L/2] = \frac{P L}{4} = [ans] kN·m, under the load.",
  "P*L/4", wrong=["P*L/8", "P*L/2", "P*L"], fig=lambda e: beam(e['L'], [(e['L'] / 2, e['P'])]), sfig=lambda e: beam(e['L'], [(e['L'] / 2, e['P'])], R=(e['P'] / 2, e['P'] / 2)), L=[6, 8, 5, 10], P=[40, 30, 64, 18])
F('structural-0009', "A cantilever beam [L] m long carries a [P] kN point load at its free end. EI = [EI] kN·m^{2}. What is the deflection at the free end?",
  "For a cantilever with a tip load, the free-end deflection is P L^{3} / (3 EI). It is 16 times the midspan deflection of a simply supported beam of the same span and central load.",
  r"Deflection = \frac{P L^{3}}{3 EI} = \frac{[P]([L])^{3}}{3([EI])} = [P*L**3/(3*EI)|5] m = [ans|3] mm.",
  "P*L**3/(3*EI)*1000", wrong=["P*L**3/(12*EI)*1000", "P*L**3/(8*EI)*1000", "P*L**3/EI*1000"], dp=3, fig=lambda e: beam(e['L'], [(e['L'], e['P'])], kind='cantilever'), L=[2, 3, 2.5, 4], P=[5, 10, 8, 6], EI=[10000, 20000, 12500, 40000])
F('structural-0010', "A column [L] m long is fixed at its base and pinned at its top. Using the theoretical effective length factor K = 0.7, what is its effective length?",
  "The effective length K L is the length of the equivalent pinned-pinned column, the distance between inflection points of the buckled shape. End restraint shortens it: K = 0.5 fixed-fixed, 0.7 fixed-pinned, 1.0 pinned-pinned, 2.0 fixed-free.",
  "Effective length = K L = 0.7 × [L] = [ans|1] m.",
  "0.7*L", wrong=["0.5*L", "L", "2*L"], dp=1, fig=lambda e: column(e['L'], 0.7, 'Pinned', 'Fixed'), L=[5, 4, 6, 3])
F('structural-0012', "A beam [L] m long is fixed at one end and supported by a roller at the other. It carries a uniform load of [w] kN/m. What is the reaction at the roller?",
  "A propped cantilever has one more reaction than statics can solve, so a compatibility condition is needed: the deflection at the roller is zero. Setting the downward deflection from the load, w L^{4} / (8 EI), equal to the upward deflection from the reaction, R L^{3} / (3 EI), gives R = 3 w L / 8.",
  r"\frac{R L^{3}}{3 EI} = \frac{w L^{4}}{8 EI}, so R = \frac{3 w L}{8} = \frac{3([w])([L])}{8} = [ans] kN. The fixed end carries the other [w*L-3*w*L/8] kN.",
  "3*w*L/8", L=[4, 6, 5, 8], w=[8, 10, 16, 6])
F('structural-0013', "A beam fixed at both ends spans [L] m and carries a uniform load of [w] kN/m. What is the magnitude of the moment at each support?",
  "Fixed ends prevent rotation, which attracts negative moment to the supports. For a full uniform load the fixed-end moment is w L^{2} / 12 and the midspan moment drops to w L^{2} / 24; together they still add to the simple-span value w L^{2} / 8.",
  r"Fixed-end moment = \frac{w L^{2}}{12} = \frac{[w]([L])^{2}}{12} = [ans] kN·m. Midspan moment = [w*L*L/24] kN·m.",
  "w*L**2/12", wrong=["w*L**2/24", "w*L**2/16", "w*L**2/8"], L=[6, 4, 8, 5], w=[12, 18, 9, 24])
F('structural-0014', "Floor beams are spaced [s] m apart and support a floor load of [q] kPa. What line load does an interior beam carry?",
  "A beam collects floor load from its tributary width, half the spacing on each side. Line load = area load × tributary width.",
  "Tributary width of an interior beam = [s] m. || w = [q] kPa × [s] m = [ans] kN/m.",
  "q*s", wrong=["q/s", "q+s", "q*s*s"], s=[3, 2.5, 4, 2], q=[4, 6, 3.5, 5])
F('structural-0015', "A steel tension member has a gross area of [Ag] mm^{2} and a yield strength of [Fy] MPa. Using LRFD with a resistance factor of 0.90, what is its design strength for yielding on the gross section?",
  "Tension yielding is checked on the gross area: nominal strength P_{n} = F_{y} A_{g}, and design strength is the resistance factor times P_{n}. Rupture on the net section is a separate check with a factor of 0.75.",
  "P_{n} = F_{y} A_{g} = [Fy] × [Ag] = [Fy*Ag] N = [Fy*Ag/1000] kN. || Design strength = 0.90 × [Fy*Ag/1000] = [ans|1] kN.",
  "0.9*Fy*Ag/1000", dp=1, Ag=[2000, 3200, 1500, 4500], Fy=[345, 345, 250, 345])
F('structural-0016', "A compact, fully braced steel beam has a plastic section modulus of [Z|1] × 10^{6} mm^{3} and a yield strength of [Fy] MPa. With a resistance factor of 0.90, what is its design flexural strength?",
  "A compact, laterally braced beam can reach its full plastic moment, M_{p} = F_{y} Z, where every fibre has yielded. The design strength is the resistance factor times M_{p}.",
  "M_{p} = F_{y} Z = [Fy] × [Z|1] × 10^{6} N·mm = [Fy*Z|1] kN·m. || Design strength = 0.90 × [Fy*Z|1] = [ans|1] kN·m.",
  "0.9*Fy*Z", wrong=["0.75*Fy*Z", "Fy*Z", "Fy*Z/0.9"], dp=1, Z=[1.2, 0.8, 2.0, 1.5], Fy=[345, 345, 250, 345])
F('structural-0017', "A steel column has an effective length of [L] m and a radius of gyration of [r] mm about the axis of buckling. What is its slenderness ratio?",
  "The slenderness ratio K L / r measures how prone a column is to buckling; the larger it is, the lower the critical stress. Use the radius of gyration for the axis about which buckling occurs, with both lengths in the same units.",
  r"Slenderness ratio = \frac{K L}{r} = \frac{[L*1000] mm}{[r] mm} = [ans].",
  "L*1000/r", wrong=["L*100/r", "L*500/r", "L*2500/r"], L=[4, 6, 3, 5], r=[50, 75, 40, 100])
F('structural-0018', "A reinforced concrete beam is [b] mm wide with [As] mm^{2} of tension steel. The steel yield strength is 420 MPa and the concrete strength is [fc] MPa. What is the depth of the equivalent rectangular stress block?",
  "Horizontal equilibrium of the section sets the stress block depth: the concrete compression 0.85 f'_{c} a b equals the steel tension A_{s} f_{y}.",
  r"0.85 f'_{c} a b = A_{s} f_{y}. || a = \frac{[As](420)}{0.85([fc])([b])} = \frac{[As*420]}{[0.85*fc*b]} = [ans|1] mm.",
  "As*420/(0.85*fc*b)", dp=1, b=[250, 300, 350, 400], As=[1200, 1500, 2000, 2500], fc=[30, 28, 35, 25])
F('structural-0019', "Using V_{c} = 0.17 × the square root of f'_{c} × b × d (MPa and mm), what shear does the concrete carry in a beam [b] mm wide with an effective depth of [d] mm and a concrete strength of [fc] MPa?",
  "The concrete contribution to shear strength depends on the square root of the compressive strength, because shear failure is governed by diagonal tension, and on the web area b d.",
  r"V_{c} = 0.17 \sqrt{[fc]}([b])([d]) = 0.17([sqrt(fc)|2])([b*d]) = [ans*1000|0] N = [ans|1] kN.",
  "0.17*sqrt(fc)*b*d/1000", wrong=["0.085*sqrt(fc)*b*d/1000", "0.34*sqrt(fc)*b*d/1000", "fc*b*d/5000"], dp=1, b=[300, 350, 250, 400], d=[500, 600, 450, 550], fc=[25, 36, 30, 28])
F('structural-0020', "A [sd0] mm square tied column has [Ast] mm^{2} of longitudinal steel with a yield strength of 420 MPa. The concrete strength is [fc] MPa. What is the nominal axial strength at zero eccentricity, P_{0}?",
  "Under pure axial load the concrete and steel act together: the concrete carries 0.85 f'_{c} on the net concrete area and the steel carries its yield strength on its own area.",
  "Gross area A_{g} = [sd0]^{2} = [sd0*sd0] mm^{2}. || Concrete: 0.85([fc])([sd0*sd0] - [Ast]) = [0.85*fc*(sd0*sd0-Ast)|0] N. || Steel: 420([Ast]) = [420*Ast] N. || P_{0} = [0.85*fc*(sd0*sd0-Ast)|0] + [420*Ast] = [ans*1000|0] N = [ans|0] kN.",
  "(0.85*fc*(sd0*sd0-Ast)+420*Ast)/1000", dp=0, sd0=[400, 450, 500, 350], Ast=[3200, 4000, 4900, 2500], fc=[28, 35, 28, 21])
if __name__ == '__main__': save()
