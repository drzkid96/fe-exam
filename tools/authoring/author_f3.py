"""Further question types: mathematics, statics, dynamics and mechanics of materials. See author_fx.py for the format."""
from author_fx import *
PS, ST, DY, MM = 'Engineering Probability and Statistics', 'Statics', 'Dynamics', 'Mechanics of Materials'
# ================= Mathematics =================
NQ('math-a', 'straight line', '', 3, -0.5, "A line passes through the points ([x1], [y1]) and ([x2], [y2]). What is the slope of a line perpendicular to it?",
   "Perpendicular lines have slopes that are negative reciprocals of each other: m_{2} = -1 / m_{1}. Find the slope of the given line first, as rise over run.",
   r"m_{1} = \frac{[y2] - ([y1])}{[x2] - ([x1])} = [(y2-y1)/(x2-x1)|3]. || m_{2} = -\frac{1}{[(y2-y1)/(x2-x1)|3]} = [ans|3].",
   "-(x2-x1)/(y2-y1)", wrong=["(y2-y1)/(x2-x1)", "-(y2-y1)/(x2-x1)", "(x2-x1)/(y2-y1)"], x1=[1, 0, 2], y1=[2, 1, -1], x2=[5, 4, 6], y2=[10, 13, 1])
NQ('math-a', 'law of sines', 'm', 2, 14.14, "In a triangle, side a is [a] m long and lies opposite a [A]° angle. What is the length of the side opposite a [B]° angle?",
   "The law of sines says each side divided by the sine of its opposite angle gives the same value: a / sin A = b / sin B. It applies whenever a side and its opposite angle are known.",
   r"b = \frac{a sin B}{sin A} = \frac{[a] sin [B]°}{sin [A]°} = \frac{[a]([sin(rad(B))|4])}{[sin(rad(A))|4]} = [ans|2] m.",
   "a*sin(rad(B))/sin(rad(A))", a=[10, 8, 25], A=[30, 50, 40], B=[45, 70, 100])
NQ('math-a', 'straight line', 'units', 3, 4.0, "What is the perpendicular distance from the point ([x0], [y0]) to the line [a]x + [b]y + ([c]) = 0?",
   "For a line written as Ax + By + C = 0, the perpendicular distance from a point is |A x_{0} + B y_{0} + C| divided by the square root of (A^{2} + B^{2}).",
   r"d = \frac{|[a]([x0]) + [b]([y0]) + ([c])|}{\sqrt{[a]^{2} + [b]^{2}}} = \frac{[abs(a*x0+b*y0+c)]}{[hypot(a,b)|3]} = [ans|3] units.",
   "abs(a*x0+b*y0+c)/hypot(a,b)", a=[3, 5, 8], b=[4, 12, 6], c=[-10, -4, 5], x0=[2, 1, 3], y0=[6, 3, -2])
NQ('math-a', '-', 'm', 2, 15.71, "A circular arc has a radius of [r] m and subtends a central angle of [th]°. What is the arc length?",
   "Arc length is radius times the central angle in radians. Convert degrees to radians by multiplying by π / 180.",
   r"Angle = [th] × \frac{π}{180} = [rad(th)|4] rad. || s = r × angle = [r] × [rad(th)|4] = [ans|2] m.",
   "r*rad(th)", r=[12, 250, 40], th=[75, 18, 130])
NQ('math-b', 'integral calculus', '', 2, 18, "What is the average value of f(x) = [a]x^{2} + [b] over the interval from x = 0 to x = [L]?",
   "The average value of a function over an interval is its definite integral divided by the length of the interval.",
   r"Integral from 0 to [L] = \frac{[a]([L])^{3}}{3} + [b]([L]) = [a*L**3/3+b*L|2]. || Average = \frac{[a*L**3/3+b*L|2]}{[L]} = [ans|2].",
   "a*L*L/3+b", a=[3, 6, 1.5], b=[2, -4, 10], L=[4, 2, 6])
NQ('math-b', 'differential calculus', '', 2, 2, "At what value of x does f(x) = x^{3} - [p]x^{2} + [q]x have its inflection point?",
   "An inflection point is where the curvature changes sign, so the second derivative is zero there. For a cubic there is exactly one.",
   "f'(x) = 3x^{2} - [2*p]x + [q], and f''(x) = 6x - [2*p]. || Setting f''(x) = 0 gives x = [2*p] / 6 = [ans|2].",
   "p/3", wrong=["p/6", "p/2", "2*p/3"], p=[6, 9, 4.5], q=[5, 2, 7])
NQ('math-b', 'differential calculus', 'm/s^{2}', 1, 36, "A particle's position is s(t) = [a]t^{3} - [b]t, with s in metres and t in seconds. What is its acceleration at t = [t] s?",
   "Velocity is the first derivative of position and acceleration is the second. Differentiate twice, then substitute the time.",
   "v(t) = [3*a]t^{2} - [b]. || a(t) = [6*a]t, so a([t]) = [6*a] × [t] = [ans|1] m/s^{2}.",
   "6*a*t", a=[2, 0.5, 1.5], b=[4, 3, 10], t=[3, 4, 2])
NQ('math-b', '-', '', 4, 0.1895, "A quantity decays exponentially with a half-life of [T] years. What fraction of it remains after [t] years?",
   "Each half-life halves what is left, so the fraction remaining is 0.5 raised to the number of half-lives elapsed. This is the same as e^{-kt} with k = ln 2 / half-life.",
   r"Half-lives elapsed = \frac{[t]}{[T]} = [t/T|3]. || Fraction remaining = 0.5^{[t/T|3]} = [ans|4].",
   "0.5**(t/T)", T=[5, 8, 30], t=[12, 20, 45])
NQ('math-b', 'differential calculus', '', 0, 90, "For f(x, y) = [a]x^{2}y + [b]y^{3}, what is the partial derivative of f with respect to x at the point ([x0], [y0])?",
   "A partial derivative with respect to x treats every other variable as a constant. Terms without x drop out.",
   "∂f/∂x = [2*a]xy, because [b]y^{3} has no x in it. || At ([x0], [y0]): [2*a]([x0])([y0]) = [ans|0].",
   "2*a*x0*y0", wrong=["a*x0*x0+3*b*y0*y0", "2*a*x0", "a*x0*x0*y0"], a=[3, 2, 5], b=[1, 4, 2], x0=[3, 1, 4], y0=[5, 3, -1])
NQ('math-c', 'cross product', 'square units', 0, 17, "Vectors **A** = [a1]**i** + [a2]**j** and **B** = [b1]**i** + [b2]**j** form two sides of a parallelogram. What is its area?",
   "The magnitude of the cross product of two vectors equals the area of the parallelogram they span. For vectors in the x-y plane it reduces to |a_{1}b_{2} - a_{2}b_{1}|.",
   "Area = |[a1]([b2]) - [a2]([b1])| = |[a1*b2] - [a2*b1]| = [ans|0] square units.",
   "abs(a1*b2-a2*b1)", a1=[3, 2, 6], a2=[4, 7, 1], b1=[5, 4, 2], b2=[1, 2, 8])
NQ('math-c', '-', '', 4, 0.2857, "What is the x-component of the unit vector in the direction of ([a], [b], [c])?",
   "A unit vector has length 1 and the same direction as the original. Divide each component by the vector's magnitude.",
   r"Magnitude = \sqrt{[a]^{2} + ([b])^{2} + [c]^{2}} = [sqrt(a*a+b*b+c*c)|3]. || x-component = \frac{[a]}{[sqrt(a*a+b*b+c*c)|3]} = [ans|4].",
   "a/sqrt(a*a+b*b+c*c)", a=[2, 4, 1], b=[-3, 4, 2], c=[6, 7, 2])
NQ('math-c', 'dot product', '', 3, 10, "What is the scalar projection of **A** = ([a1], [a2]) onto **B** = ([b1], [b2])?",
   "The scalar projection of A onto B is the length of A's shadow along B. It equals the dot product divided by the magnitude of B.",
   r"A · B = [a1]([b1]) + [a2]([b2]) = [a1*b1+a2*b2]. |B| = [hypot(b1,b2)|3]. || Projection = \frac{[a1*b1+a2*b2]}{[hypot(b1,b2)|3]} = [ans|3].",
   "(a1*b1+a2*b2)/hypot(b1,b2)", a1=[6, 5, 2], a2=[8, 2, 9], b1=[3, 12, 8], b2=[4, 5, 6])
NQ('math-d', PS + '::confidence interval', '', 3, 3.92, "A sample of [n] measurements comes from a population with a known standard deviation of [s]. What is the half-width of the 95% confidence interval for the mean? Use z = 1.96.",
   "With the population standard deviation known, the confidence interval for the mean is the sample mean plus or minus z times the standard deviation divided by the square root of the sample size.",
   r"Half-width = z \frac{σ}{\sqrt{n}} = 1.96 × \frac{[s]}{\sqrt{[n]}} = 1.96 × [s/sqrt(n)|4] = [ans|3].",
   "1.96*s/sqrt(n)", s=[12, 4.5, 30], n=[36, 25, 100])
NQ('math-d', PS + '::coefficient of variation', '%', 1, 22.6, "A sample of five values is [data]. What is its coefficient of variation, using the sample standard deviation?",
   "The coefficient of variation expresses scatter relative to size: the standard deviation divided by the mean. The sample standard deviation divides the sum of squared deviations by n - 1.",
   r"Mean = [sum(data)/5|2]. Sample standard deviation = [sd(data)|3]. || CV = \frac{[sd(data)|3]}{[sum(data)/5|2]} × 100 = [ans|1]%.",
   "sd(data)/(sum(data)/5)*100", data=[[10, 12, 14, 16, 18], [4, 7, 7, 9, 13], [20, 25, 30, 45, 55], [3, 5, 8, 10, 14]])
NQ('math-d', PS + '::conditional probability', '', 4, 0.1333, "A box holds [r] red and [b] blue parts. Two parts are drawn at random without replacement. What is the probability that both are red?",
   "Without replacement the second draw depends on the first. Multiply the probability of red on the first draw by the probability of red on the second, given one red is already gone.",
   r"P = \frac{[r]}{[r+b]} × \frac{[r-1]}{[r+b-1]} = [r/(r+b)|4] × [(r-1)/(r+b-1)|4] = [ans|4].",
   "r*(r-1)/((r+b)*(r+b-1))", wrong=["(r/(r+b))**2", "r/(r+b)", "2*r*b/((r+b)*(r+b-1))"], r=[4, 5, 3], b=[6, 3, 9])
NQ('math-d', PS + '::combinations', '', 0, 56, "In how many different ways can a team of [k] be chosen from [n] people, if the order of selection does not matter?",
   "When order does not matter the count is a combination: n! / (k!(n - k)!). A permutation, where order matters, is larger by a factor of k!.",
   r"C([n], [k]) = \frac{[n]!}{[k]!([n-k])!} = [ans|0].",
   "comb(n,k)", wrong=["comb(n,k)*2", "n*k", "comb(n,k-1)"], n=[8, 10, 12], k=[3, 4, 2])
# ================= Statics =================
NQ('statics-a', 'resultant', '°', 1, 47.0, "Two forces act at a point: [F1] N at [t1]° and [F2] N at [t2]°, both measured counterclockwise from the positive x-axis. What angle does their resultant make with the positive x-axis?",
   "Resolve each force into x and y components, add the components, then take the inverse tangent of the summed y over the summed x.",
   r"R_{x} = [F1] cos [t1]° + [F2] cos [t2]° = [F1*cos(rad(t1))+F2*cos(rad(t2))|1] N. || R_{y} = [F1] sin [t1]° + [F2] sin [t2]° = [F1*sin(rad(t1))+F2*sin(rad(t2))|1] N. || Angle = tan^{-1}(\frac{[F1*sin(rad(t1))+F2*sin(rad(t2))|1]}{[F1*cos(rad(t1))+F2*cos(rad(t2))|1]}) = [ans|1]°.",
   "atan((F1*sin(rad(t1))+F2*sin(rad(t2)))/(F1*cos(rad(t1))+F2*cos(rad(t2))))*180/pi", F1=[200, 120, 500], t1=[30, 10, 20], F2=[150, 90, 300], t2=[70, 60, 80])
NQ('statics-a', 'resultant', '°', 1, 73.4, "A force has components F_{x} = [a] kN, F_{y} = [b] kN and F_{z} = [c] kN. What angle does it make with the x-axis?",
   "The direction cosine with an axis is the component along that axis divided by the magnitude of the force. The magnitude is the square root of the sum of the squared components.",
   r"|F| = \sqrt{[a]^{2} + ([b])^{2} + ([c])^{2}} = [sqrt(a*a+b*b+c*c)|3] kN. || cos(angle) = \frac{[a]}{[sqrt(a*a+b*b+c*c)|3]} = [a/sqrt(a*a+b*b+c*c)|4], so the angle is [ans|1]°.",
   "acos(a/sqrt(a*a+b*b+c*c))*180/pi", a=[2, 4, 3], b=[3, 4, -4], c=[6, -7, 12])
NQ('statics-b', 'systems of forces', 'm', 2, 3.17, "Three parallel downward forces act on a beam: [F1] kN at the left end, [F2] kN at [x2] m and [F3] kN at [x3] m from the left end. How far from the left end does their single resultant act?",
   "A single force replaces a set of parallel forces if it has the same total and the same moment about any point. Its position is the sum of the moments divided by the sum of the forces.",
   r"Sum of forces = [F1] + [F2] + [F3] = [F1+F2+F3] kN. || Sum of moments about the left end = [F2]([x2]) + [F3]([x3]) = [F2*x2+F3*x3|1] kN·m. || Position = \frac{[F2*x2+F3*x3|1]}{[F1+F2+F3]} = [ans|2] m.",
   "(F2*x2+F3*x3)/(F1+F2+F3)", F1=[10, 5, 40], F2=[20, 15, 10], F3=[30, 10, 25], x2=[2, 3, 1.5], x3=[5, 8, 4])
NQ('statics-b', 'systems of forces', 'm', 2, 3.6, "A distributed load on a beam [L] m long increases linearly from [w1] kN/m at the left end to [w2] kN/m at the right end. How far from the left end does its resultant act?",
   "Split a trapezoidal load into a rectangle, whose resultant acts at mid-length, and a triangle, whose resultant acts two thirds of the way toward its tall end. Then take moments.",
   r"Rectangle: [w1]([L]) = [w1*L|1] kN at [L/2|2] m. Triangle: \frac{1}{2}([w2-w1])([L]) = [(w2-w1)*L/2|1] kN at [2*L/3 if w2>w1 else L/3|2] m. || Position = \frac{[w1*L|1]([L/2|2]) + [(w2-w1)*L/2|1]([2*L/3|2])}{[(w1+w2)*L/2|1]} = [ans|2] m.",
   "L*(w1+2*w2)/(3*(w1+w2))", w1=[2, 4, 3], w2=[8, 10, 12], L=[6, 9, 4])
NQ('statics-b', 'moments', 'N·m', 0, 100, "A force with components F_{x} = [Fx] N and F_{y} = [Fy] N acts at the point ([x], [y]) m. What is its moment about the origin, counterclockwise positive?",
   "The moment of a force about the origin in a plane is x F_{y} - y F_{x}. Each component has its own lever arm: the y-component acts at distance x and the x-component at distance y, turning the opposite way.",
   "M = x F_{y} - y F_{x} = [x]([Fy]) - [y]([Fx]) = [x*Fy|0] - ([y*Fx|0]) = [ans|0] N·m.",
   "x*Fy-y*Fx", wrong=["x*Fy+y*Fx", "x*Fx+y*Fy", "x*Fy"], x=[3, 4, 1.5], y=[2, 1, 2.5], Fx=[40, -30, 80], Fy=[60, 50, 20])
NQ('statics-c', 'equilibrium requirements', 'kN', 2, 13.5, "A beam rests on a pin at A and a roller at B, [L] m apart, and overhangs [a] m beyond B. It carries a [Q] kN load [c] m from A and a [P] kN load at the tip of the overhang. What is the reaction at B?",
   "Take moments about A so the unknown reaction there drops out. A load on the overhang has a lever arm longer than the span, so it adds more than its own weight to the reaction at B.",
   r"Moments about A: B_{y}([L]) = [Q]([c]) + [P]([L] + [a]). || B_{y} = \frac{[Q*c|1] + [P*(L+a)|1]}{[L]} = [ans|2] kN.",
   "(Q*c+P*(L+a))/L", L=[8, 10, 6], a=[2, 3, 1.5], Q=[12, 20, 9], c=[4, 6, 2], P=[6, 5, 10])
NQ('statics-c', 'equilibrium requirements', 'N', 1, 1400, "A uniform horizontal bar weighing [Wb] N is pinned to a wall at one end. A cable from its other end to the wall makes [th]° with the bar. A [W] N load hangs from the cable end of the bar. What is the cable tension?",
   "Take moments about the pin. Only the vertical component of the tension has a lever arm, the full bar length. The bar's own weight acts at mid-length.",
   r"T sin [th]° (L) = [W](L) + [Wb](\frac{L}{2}), and the length cancels. || T = \frac{[W] + [Wb/2|1]}{sin [th]°} = \frac{[W+Wb/2|1]}{[sin(rad(th))|4]} = [ans|1] N.",
   "(W+Wb/2)/sin(rad(th))", W=[600, 900, 250], Wb=[200, 300, 100], th=[30, 40, 55])
NQ('statics-c', 'equilibrium requirements; concurrent forces', 'N', 1, 490.5, "A [m] kg load hangs from two cables. Cable 1 makes [al]° with the horizontal and cable 2 makes [be]° with the horizontal on the other side. What is the tension in cable 1? Use g = 9.81 m/s^{2}.",
   "Three forces meet at the knot, so their horizontal and vertical components must each balance. Solving the two equations gives T_{1} = W cos(angle 2) / sin(angle 1 + angle 2).",
   r"W = [m](9.81) = [m*g|1] N. || T_{1} = \frac{W cos [be]°}{sin([al]° + [be]°)} = \frac{[m*g|1]([cos(rad(be))|4])}{[sin(rad(al+be))|4]} = [ans|1] N.",
   "m*g*cos(rad(be))/sin(rad(al+be))", m=[100, 250, 60], al=[30, 45, 20], be=[60, 30, 50])
NQ('statics-d', 'method of sections', 'kN', 1, 80, "A parallel-chord truss is [h] m deep. A vertical section is cut through one panel. The loads and reactions to the left of the cut give a moment of [M] kN·m about the top-chord joint at the cut. What is the force in the bottom chord?",
   "In the method of sections, take moments about the joint where the other two cut members meet. Only the bottom chord then has a moment, with a lever arm equal to the truss depth.",
   r"Bottom chord force × [h] = [M], so the force = \frac{[M]}{[h]} = [ans|1] kN. Under gravity loads on a simple span it is tension.",
   "M/h", M=[240, 450, 96], h=[3, 2.5, 1.6])
NQ('statics-d', 'method of sections', 'kN', 2, 50, "A parallel-chord truss has panels [p] m long and [h] m high. In one panel the shear carried across a vertical cut is [V] kN, and the diagonal is the only cut member with a vertical component. What is the force in the diagonal?",
   "The chords are horizontal, so only the diagonal can carry the panel shear. Its vertical component must equal the shear, and the force is larger by the ratio of the diagonal's length to its height.",
   r"Diagonal length = \sqrt{[p]^{2} + [h]^{2}} = [hypot(p,h)|3] m. || Force = [V] × \frac{[hypot(p,h)|3]}{[h]} = [ans|2] kN.",
   "V*hypot(p,h)/h", V=[30, 45, 18], p=[4, 3, 2.4], h=[3, 4, 1])
NQ('statics-d', 'moments', 'N', 0, 400, "A hand force of [P] N is applied to each handle of a pair of pliers, [a] mm from the pivot. The jaws grip a wire [b] mm from the pivot. What force do the jaws apply to the wire?",
   "Each half of the pliers is a lever in equilibrium about the pivot pin. The moments of the hand force and the gripping force about the pin are equal.",
   r"P × a = F × b, so F = \frac{[P]([a])}{[b]} = [ans|0] N.",
   "P*a/b", P=[80, 120, 50], a=[150, 200, 180], b=[30, 25, 45])
NQ('statics-e', 'centroid', 'mm', 2, 38.0, "A plate is a rectangle [b] mm wide and [h] mm high with a right triangle of base [bt] mm and the same height attached along its right side, tapering to the right. How far is the centroid from the left edge?",
   "For a composite area, the centroid is the sum of each part's area times its centroid distance, divided by the total area. A triangle's centroid is one third of its base from the side it tapers away from.",
   r"Rectangle: [b*h] mm^{2} at [b/2|1] mm. Triangle: [bt*h/2|0] mm^{2} at [b] + \frac{[bt]}{3} = [b+bt/3|1] mm. || x = \frac{[b*h]([b/2|1]) + [bt*h/2|0]([b+bt/3|1])}{[b*h+bt*h/2|0]} = [ans|2] mm.",
   "(b*h*b/2+bt*h/2*(b+bt/3))/(b*h+bt*h/2)", b=[60, 100, 40], bt=[30, 60, 30], h=[40, 80, 20])
NQ('statics-e', 'centroid', 'mm', 2, 91.77, "A rectangular plate [W] mm wide and [H] mm high has a [d] mm diameter hole whose centre is [xh] mm from the left edge, at mid-height. How far is the centroid of the plate from its left edge?",
   "Treat a hole as a negative area. Subtract its area and its area moment from those of the full rectangle.",
   r"Rectangle: [W*H] mm^{2} at [W/2|1] mm. Hole: \frac{π([d])^{2}}{4} = [pi*d*d/4|1] mm^{2} at [xh] mm. || x = \frac{[W*H]([W/2|1]) - [pi*d*d/4|1]([xh])}{[W*H] - [pi*d*d/4|1]} = [ans|2] mm.",
   "(W*H*W/2-pi*d*d/4*xh)/(W*H-pi*d*d/4)", W=[200, 300, 120], H=[100, 150, 80], d=[60, 80, 40], xh=[150, 75, 90])
NQ('statics-e', 'centroid', 'mm', 2, 21.47, "A channel section has two flanges [b] mm long and a web [h] mm high overall, all [t] mm thick. How far is its centroid from the back (outer face) of the web?",
   "Divide the channel into two flanges and the web between them. The web's centroid is half a thickness from the back; each flange's centroid is half its length from the back.",
   r"Flanges: 2 × [b*t] mm^{2} at [b/2|1] mm. Web: ([h] - 2 × [t])([t]) = [(h-2*t)*t] mm^{2} at [t/2|1] mm. || x = \frac{2([b*t])([b/2|1]) + [(h-2*t)*t]([t/2|1])}{2([b*t]) + [(h-2*t)*t]} = [ans|2] mm.",
   "(2*b*t*b/2+(h-2*t)*t*t/2)/(2*b*t+(h-2*t)*t)", b=[80, 100, 60], t=[10, 12, 8], h=[200, 300, 150])
NQ('statics-f', 'moment of inertia', '× 10^{6} mm^{4}', 2, 39.36, "A hollow rectangular section is [B] mm wide and [H] mm deep outside, with a centred rectangular opening [bi] mm wide and [hi] mm deep. What is its moment of inertia about the horizontal centroidal axis?",
   "When shapes share the same centroidal axis their moments of inertia add or subtract directly. Take the outer rectangle's b h^{3} / 12 and subtract the opening's.",
   r"I = \frac{[B]([H])^{3} - [bi]([hi])^{3}}{12} = \frac{[B*H**3|0] - [bi*hi**3|0]}{12} = [ans|2] × 10^{6} mm^{4}.",
   "(B*H**3-bi*hi**3)/12/1e6", B=[100, 150, 60], H=[200, 300, 120], bi=[80, 130, 40], hi=[160, 260, 100])
NQ('statics-f', 'parallel axis; moment of inertia', '× 10^{6} mm^{4}', 1, 132.4, "A symmetric I-section has flanges [bf] mm wide and [tf] mm thick, and a web [tw] mm thick and [hw] mm high between them. What is its moment of inertia about the horizontal centroidal axis?",
   "The web sits on the centroidal axis, so only its own b h^{3} / 12 counts. Each flange is offset, so the parallel axis theorem adds its area times the square of the distance from the axis to the flange's centroid. That term usually dominates.",
   r"Web: \frac{[tw]([hw])^{3}}{12} = [tw*hw**3/12/1e6|3] × 10^{6}. || Each flange: \frac{[bf]([tf])^{3}}{12} + [bf*tf]([hw/2+tf/2|1])^{2} = [(bf*tf**3/12+bf*tf*(hw/2+tf/2)**2)/1e6|3] × 10^{6}. || I = [tw*hw**3/12/1e6|3] + 2([(bf*tf**3/12+bf*tf*(hw/2+tf/2)**2)/1e6|3]) = [ans|1] × 10^{6} mm^{4}.",
   "(tw*hw**3/12+2*(bf*tf**3/12+bf*tf*(hw/2+tf/2)**2))/1e6", bf=[150, 200, 100], tf=[20, 25, 12], tw=[10, 12, 8], hw=[260, 350, 176])
NQ('statics-f', 'radius of gyration', 'mm', 1, 86.6, "A rectangular section is [b] mm wide and [h] mm deep. What is its radius of gyration about the horizontal centroidal axis?",
   "The radius of gyration is the square root of the moment of inertia divided by the area. For a rectangle about its centroidal axis this is h divided by the square root of 12.",
   r"r = \sqrt{\frac{I}{A}} = \sqrt{\frac{[b]([h])^{3} / 12}{[b]([h])}} = \frac{[h]}{\sqrt{12}} = [ans|1] mm.",
   "h/sqrt(12)", wrong=["h/sqrt(3)", "h/6", "h/2"], b=[200, 150, 90], h=[300, 450, 240])
NQ('statics-f', 'moment of inertia', '× 10^{6} mm^{4}', 2, 5.80, "A hollow circular shaft has an outside diameter of [do] mm and an inside diameter of [di] mm. What is its polar moment of inertia?",
   "The polar moment of inertia of a circle is π d^{4} / 32, twice the moment of inertia about a diameter. For a tube, subtract the bore.",
   r"J = \frac{π([do]^{4} - [di]^{4})}{32} = \frac{π([do**4-di**4|0])}{32} = [ans|2] × 10^{6} mm^{4}.",
   "pi*(do**4-di**4)/32/1e6", do=[100, 60, 150], di=[80, 40, 120])
NQ('statics-g', 'friction', 'N', 1, 312.0, "A [W] N block rests on a plane inclined at [th]° to the horizontal. The coefficient of static friction is [mu|2]. What force, applied parallel to the plane, will start the block moving up the plane?",
   "To start motion up the plane the force must overcome both the component of weight down the plane and the maximum friction, which also acts down the plane when motion is impending upward.",
   r"Weight component down the plane = [W] sin [th]° = [W*sin(rad(th))|1] N. Normal force = [W] cos [th]° = [W*cos(rad(th))|1] N. || P = [W*sin(rad(th))|1] + [mu|2]([W*cos(rad(th))|1]) = [ans|1] N.",
   "W*(sin(rad(th))+mu*cos(rad(th)))", W=[500, 800, 120], th=[20, 30, 15], mu=[0.30, 0.25, 0.40])
NQ('statics-g', 'belt friction', 'N', 1, 513.3, "A rope passes over a fixed drum with a wrap angle of [wrap]°. The coefficient of friction is [mu|2] and the tension on the slack side is [T2] N. What is the largest tension the other side can hold before the rope slips?",
   "Friction around a curved surface multiplies tension exponentially: tight-side tension = slack-side tension × e^{(coefficient × wrap angle)}, with the angle in radians.",
   r"Wrap angle = [wrap]° = [rad(wrap)|4] rad. || T_{1} = [T2] e^{[mu|2] × [rad(wrap)|4]} = [T2] × [exp(mu*rad(wrap))|4] = [ans|1] N.",
   "T2*exp(mu*rad(wrap))", T2=[200, 150, 400], mu=[0.30, 0.25, 0.20], wrap=[180, 270, 90])
NQ('statics-g', 'friction', 'N', 0, 160, "A [W] N crate is [b|1] m wide and [h|1] m tall, with its weight acting through its centre. A horizontal force is applied at its top edge, and friction is high enough to prevent sliding. What force makes the crate start to tip?",
   "At the point of tipping the floor reaction moves to the edge the crate would rotate about. Take moments about that edge: the push at height h overturns, and the weight at half the width resists.",
   r"P × [h|1] = [W] × \frac{[b|1]}{2}, so P = \frac{[W]([b/2|2])}{[h|1]} = [ans|0] N.",
   "W*b/(2*h)", W=[600, 900, 240], b=[0.8, 0.6, 0.5], h=[1.5, 2.0, 1.0])
# ================= Dynamics =================
NQ('dynamics-a', 'projectile motion', 'm', 2, 18.95, "A projectile is launched from level ground at [v] m/s, [th]° above the horizontal. What maximum height does it reach? Use g = 9.81 m/s^{2}.",
   "Only the vertical component of the launch velocity carries the projectile upward, and at the top it is zero. The height is that component squared divided by 2g.",
   r"Vertical component = [v] sin [th]° = [v*sin(rad(th))|3] m/s. || h = \frac{([v*sin(rad(th))|3])^{2}}{2(9.81)} = [ans|2] m.",
   "(v*sin(rad(th)))**2/(2*g)", v=[30, 25, 40], th=[40, 60, 35])
NQ('dynamics-a', 'particle kinematics; constant angular acceleration', 'revolutions', 2, 31.83, "A wheel starts from rest and accelerates at a constant [al] rad/s^{2} for [t] s. How many revolutions does it turn in that time?",
   "Rotation under constant angular acceleration follows the same equations as straight-line motion: angle = (1/2)(angular acceleration)(time)^{2} from rest. One revolution is 2π radians.",
   r"Angle = \frac{1}{2}([al])([t])^{2} = [0.5*al*t*t|1] rad. || Revolutions = \frac{[0.5*al*t*t|1]}{2π} = [ans|2].",
   "0.5*al*t*t/(2*pi)", al=[4, 2.5, 6], t=[10, 8, 5])
NQ('dynamics-a', 'constant acceleration', 'm/s', 2, 20.43, "A stone is thrown straight down at [v0] m/s from a bridge [h] m above the water. Ignoring air resistance, how fast is it moving when it reaches the water? Use g = 9.81 m/s^{2}.",
   "For constant acceleration, v^{2} = v_{0}^{2} + 2 a s. The initial speed is squared, so it adds less than its full value to the final speed.",
   r"v = \sqrt{[v0]^{2} + 2(9.81)([h])} = \sqrt{[v0*v0+2*g*h|1]} = [ans|2] m/s.",
   "sqrt(v0*v0+2*g*h)", v0=[5, 8, 3], h=[20, 45, 12])
NQ('dynamics-a', 'normal and tangential components', 'm/s^{2}', 2, 4.47, "A car moving at [v] m/s on a curve of radius [r] m is speeding up at [at|1] m/s^{2}. What is the magnitude of its total acceleration?",
   "On a curve, acceleration has two perpendicular parts: tangential, which changes the speed, and normal, v^{2} / r toward the centre, which changes the direction. Combine them by Pythagoras.",
   r"Normal: \frac{[v]^{2}}{[r]} = [v*v/r|3] m/s^{2}. || Total = \sqrt{[at|1]^{2} + [v*v/r|3]^{2}} = [ans|2] m/s^{2}.",
   "hypot(at, v*v/r)", at=[2, 1.5, 3], v=[20, 15, 30], r=[100, 50, 250])
NQ('dynamics-b', 'mass moment of inertia', 'kg·m^{2}', 3, 1.3, "A hollow cylinder has a mass of [m] kg, an outer radius of [ro|2] m and an inner radius of [ri|2] m. What is its mass moment of inertia about its central axis?",
   "For a hollow cylinder about its own axis, I = m(r_{o}^{2} + r_{i}^{2}) / 2. The radii are added, not subtracted, because for a given mass a hollow shape has its material farther from the axis than a solid one.",
   r"I = \frac{[m]([ro|2]^{2} + [ri|2]^{2})}{2} = \frac{[m]([ro*ro+ri*ri|4])}{2} = [ans|3] kg·m^{2}.",
   "m*(ro*ro+ri*ri)/2", m=[20, 8, 50], ro=[0.3, 0.15, 0.5], ri=[0.2, 0.10, 0.4])
NQ('dynamics-b', 'radius of gyration', 'm', 3, 0.3, "A rotor has a mass of [m] kg and a mass moment of inertia of [I] kg·m^{2} about its axis. What is its radius of gyration?",
   "The radius of gyration is the distance from the axis at which all the mass could be concentrated to give the same moment of inertia: I = m k^{2}.",
   r"k = \sqrt{\frac{I}{m}} = \sqrt{\frac{[I]}{[m]}} = [ans|3] m.",
   "sqrt(I/m)", I=[3.6, 0.5, 18], m=[40, 8, 50])
NQ('dynamics-b', 'mass moment of inertia; parallel axis', 'kg·m^{2}', 2, 1.35, "A solid uniform disk has a mass of [m] kg and a radius of [r|1] m. What is its mass moment of inertia about an axis through its rim, perpendicular to the disk?",
   "The parallel axis theorem moves a moment of inertia from the centre of mass to a parallel axis: add the mass times the square of the distance between the axes. For a disk about its rim that gives m r^{2} / 2 + m r^{2}.",
   r"I = \frac{1}{2}([m])([r|1])^{2} + [m]([r|1])^{2} = [0.5*m*r*r|3] + [m*r*r|3] = [ans|2] kg·m^{2}.",
   "1.5*m*r*r", wrong=["0.5*m*r*r", "m*r*r", "2*m*r*r"], m=[10, 4, 25], r=[0.3, 0.5, 0.4])
NQ('dynamics-c', "Newton's second law", 'N', 1, 791.7, "A [m] kg person stands on a scale in a lift that is accelerating upward at [a|1] m/s^{2}. What force does the scale read? Use g = 9.81 m/s^{2}.",
   "The scale reads the normal force. Newton's second law for the person, with upward positive, is N - m g = m a, so the reading exceeds the weight while the lift accelerates upward.",
   "N = m(g + a) = [m](9.81 + [a|1]) = [ans|1] N.",
   "m*(g+a)", m=[70, 85, 60], a=[1.5, 2.0, 0.8])
NQ('dynamics-c', 'normal and tangential components', 'm/s', 2, 16.61, "A curve of radius [r] m is banked at [th]°. At what speed can a car take it with no reliance on friction? Use g = 9.81 m/s^{2}.",
   "With no friction, the road's normal force alone must both support the weight and supply the inward force m v^{2} / r. Dividing the two component equations gives tan(bank angle) = v^{2} / (g r).",
   r"v = \sqrt{g r tan [th]°} = \sqrt{9.81([r])([tan(rad(th))|4])} = [ans|2] m/s.",
   "sqrt(g*r*tan(rad(th)))", r=[200, 120, 400], th=[8, 12, 5])
NQ('dynamics-c', "Newton's second law", 'm/s^{2}', 3, 1.962, "Masses of [m1] kg and [m2] kg hang from the two ends of a light cord over a frictionless pulley. What is the acceleration of the masses? Use g = 9.81 m/s^{2}.",
   "Treat the two masses as one system along the cord. The net driving force is the difference of the weights, and it accelerates the sum of the masses.",
   r"a = \frac{(m_{1} - m_{2}) g}{m_{1} + m_{2}} = \frac{([m1] - [m2])(9.81)}{[m1] + [m2]} = [ans|3] m/s^{2}.",
   "(m1-m2)*g/(m1+m2)", wrong=["m1*g/(m1+m2)", "(m1-m2)*g/m1", "g"], m1=[6, 10, 5], m2=[4, 7, 2])
NQ('dynamics-c', 'kinetics of a rigid body; mass moment of inertia', 'm/s^{2}', 2, 3.27, "A solid uniform disk rolls without slipping down a slope inclined at [th]°. What is the acceleration of its centre? Use g = 9.81 m/s^{2}.",
   "Gravity must speed up both the translation and the rotation of a rolling body, so it accelerates more slowly than a sliding block. For a solid disk, a = (2/3) g sin(angle); the mass and radius cancel.",
   r"a = \frac{2}{3} g sin [th]° = \frac{2}{3}(9.81)([sin(rad(th))|4]) = [ans|2] m/s^{2}.",
   "2/3*g*sin(rad(th))", wrong=["g*sin(rad(th))", "0.5*g*sin(rad(th))", "5/7*g*sin(rad(th))"], th=[30, 20, 45])
NQ('dynamics-c', 'impulse and momentum', 'N', 0, 1200, "A [m] kg object moving at [v] m/s is brought to rest in [dt] s. What average force acts on it during that time?",
   "Impulse equals the change in momentum: average force × time = mass × change in velocity. A shorter stopping time means a larger force for the same momentum.",
   r"F = \frac{m v}{time} = \frac{[m]([v])}{[dt]} = [ans|0] N.",
   "m*v/dt", m=[0.15, 1200, 0.045], v=[40, 15, 70], dt=[0.005, 0.4, 0.0005])
NQ('dynamics-d', 'principle of work and energy; friction', 'm', 2, 53.09, "A car travelling at [v] m/s locks its wheels on a level road where the coefficient of kinetic friction is [mu|2]. How far does it slide before stopping? Use g = 9.81 m/s^{2}.",
   "The work done by friction equals the kinetic energy removed: (coefficient) m g d = (1/2) m v^{2}. The mass cancels, and the distance grows with the square of the speed.",
   r"d = \frac{v^{2}}{2 (coefficient) g} = \frac{[v]^{2}}{2([mu|2])(9.81)} = [ans|2] m.",
   "v*v/(2*mu*g)", v=[25, 15, 30], mu=[0.6, 0.4, 0.75])
NQ('dynamics-d', 'power', 'kW', 1, 147.2, "A [m] kg truck climbs a [G]% grade at a steady [v] m/s. Ignoring rolling and air resistance, what power does the climb require? Use g = 9.81 m/s^{2}.",
   "Power is force times speed. At steady speed the driving force equals the weight component along the slope, m g times the grade as a decimal (for small slopes the sine equals the grade).",
   r"Force = [m](9.81)([G/100|2]) = [m*g*G/100|0] N. || Power = [m*g*G/100|0] × [v] = [m*g*G/100*v|0] W = [ans|1] kW.",
   "m*g*G/100*v/1000", m=[20000, 1500, 36000], G=[5, 8, 3], v=[15, 25, 20])
NQ('dynamics-d', 'kinetic energy; mass moment of inertia', 'kJ', 2, 23.69, "A flywheel with a mass moment of inertia of [I] kg·m^{2} spins at [N] rpm. What is its kinetic energy?",
   "Rotational kinetic energy is (1/2) I (angular speed)^{2}, with the angular speed in rad/s. Convert rpm by multiplying by 2π / 60.",
   r"Angular speed = [N] × \frac{2π}{60} = [N*2*pi/60|2] rad/s. || KE = \frac{1}{2}([I])([N*2*pi/60|2])^{2} = [0.5*I*(N*2*pi/60)**2|0] J = [ans|2] kJ.",
   "0.5*I*(N*2*pi/60)**2/1000", I=[12, 2.5, 40], N=[600, 1800, 300])
NQ('dynamics-d', 'principle of work and energy; spring', 'm', 3, 0.2, "A [m] kg block sliding at [v] m/s on a frictionless surface runs into a spring of stiffness [k] N/m. What is the maximum compression of the spring?",
   "At maximum compression the block is momentarily at rest and all its kinetic energy is stored in the spring: (1/2) m v^{2} = (1/2) k x^{2}.",
   r"x = v \sqrt{\frac{m}{k}} = [v] \sqrt{\frac{[m]}{[k]}} = [ans|3] m.",
   "v*sqrt(m/k)", m=[4, 10, 0.5], v=[3, 2, 6], k=[900, 4000, 200])
NQ('dynamics-d', 'principle of work and energy; friction', 'm/s', 2, 5.66, "A block starts from rest and slides [d] m down a plane inclined at [th]°. The coefficient of kinetic friction is [mu|2]. How fast is it moving at the end? Use g = 9.81 m/s^{2}.",
   "Work and energy: the work of gravity along the slope minus the work of friction equals the kinetic energy gained. Friction is the coefficient times the normal force, m g cos(angle).",
   r"v^{2} = 2 g d (sin [th]° - [mu|2] cos [th]°) = 2(9.81)([d])([sin(rad(th))-mu*cos(rad(th))|4]) = [2*g*d*(sin(rad(th))-mu*cos(rad(th)))|2]. || v = [ans|2] m/s.",
   "sqrt(2*g*d*(sin(rad(th))-mu*cos(rad(th))))", d=[5, 8, 3], th=[30, 25, 40], mu=[0.2, 0.15, 0.3])
# ================= Mechanics of materials =================
NQ('mechmat-a', 'shear and moment diagrams', 'kN·m', 2, 30.72, "A simply supported beam spans [L] m. A uniform load of [w] kN/m covers the first [a] m from the left support only. What is the maximum bending moment?",
   "The maximum moment is where the shear is zero. Under a uniform load the shear falls by w for every metre, so it reaches zero a distance (left reaction) / w from the left support. The moment there is the area of the shear triangle up to that point.",
   r"Left reaction = \frac{[w]([a])([L] - [a/2|2])}{[L]} = [w*a*(L-a/2)/L|3] kN. || Zero shear at \frac{[w*a*(L-a/2)/L|3]}{[w]} = [a*(L-a/2)/L|2] m, inside the loaded length. || M_{max} = \frac{1}{2}([w*a*(L-a/2)/L|3])([a*(L-a/2)/L|2]) = [ans|2] kN·m.",
   "(w*a*(L-a/2)/L)**2/(2*w)", L=[10, 8, 12, 9], w=[6, 10, 4, 8], a=[4, 5, 6, 4.5])
NQ('mechmat-a', 'shear and moment diagrams', 'kN·m', 1, 14, "A beam rests on supports A and B, [L] m apart, and overhangs [a] m beyond B. It carries [P1] kN at [c] m from A and [P2] kN at the tip of the overhang. What is the largest bending moment magnitude in the beam?",
   "The moment peaks where the shear changes sign: under the load in the span and over support B. The moment at B is simply the overhang load times its arm, and it is negative. Compare the two magnitudes.",
   r"Moment at B = -[P2]([a]) = -[P2*a|1] kN·m. || Reaction at A = \frac{[P1]([L] - [c]) - [P2]([a])}{[L]} = [(P1*(L-c)-P2*a)/L|3] kN, so the moment under the span load = [(P1*(L-c)-P2*a)/L|3] × [c] = [(P1*(L-c)-P2*a)/L*c|1] kN·m. || The larger magnitude is [ans|1] kN·m.",
   "max(P2*a, (P1*(L-c)-P2*a)/L*c)", L=[8, 10, 6], c=[4, 6, 2], P1=[10, 8, 30], a=[2, 3, 1.5], P2=[6, 5, 10])
NQ('mechmat-a', 'shear and moment diagrams', 'kN·m', 2, 73.5, "The shear diagram of a beam starts at +[V1] kN at the left support, where the moment is zero, and falls in a straight line to -[V2] kN at a point [d] m away. What is the maximum bending moment in that length?",
   "The moment is greatest where the shear crosses zero. Similar triangles locate the crossing, and the moment there is the area of the positive shear triangle.",
   r"Zero shear at [d] × \frac{[V1]}{[V1] + [V2]} = [d*V1/(V1+V2)|2] m from the support. || M_{max} = \frac{1}{2}([V1])([d*V1/(V1+V2)|2]) = [ans|2] kN·m.",
   "0.5*V1*d*V1/(V1+V2)", V1=[21, 16, 45], V2=[9, 24, 15], d=[10, 8, 6])
NQ('mechmat-a', 'shear and moment diagrams', 'kN·m', 1, 48, "A cantilever beam [L|1] m long carries a uniform load of [w] kN/m over its whole length and a [P] kN point load at its free end. What is the magnitude of the bending moment at the fixed support?",
   "For a cantilever, cut at the support and take moments of everything outboard. The uniform load acts as w L at mid-length. The moment is negative (tension on top) and zero at the free end.",
   r"M = \frac{[w]([L|1])^{2}}{2} + [P]([L|1]) = [w*L*L/2|1] + [P*L|1] = [ans|1] kN·m.",
   "w*L*L/2+P*L", L=[3, 2.5, 4], w=[4, 8, 2], P=[10, 6, 15])
NQ('mechmat-a', 'shear and moment diagrams', 'kN', 1, 24, "A simply supported beam spans [L] m and carries a uniform load of [w] kN/m over the whole span. What is the shear force [x|1] m from the left support?",
   "The shear starts at the reaction, w L / 2, and falls by w for every metre of uniform load. It passes through zero at midspan.",
   r"V = \frac{[w]([L])}{2} - [w]([x|1]) = [w*L/2|1] - [w*x|1] = [ans|1] kN.",
   "w*(L/2-x)", L=[8, 10, 6], w=[12, 9, 20], x=[2, 3.5, 1])
NQ('mechmat-b', 'shear stress', 'MPa', 1, 99.5, "A clevis is pinned by a single [d] mm diameter bolt that is loaded in double shear by a force of [P] kN. What is the average shear stress in the bolt?",
   "In double shear the bolt is cut on two planes, so each plane carries half the load. Average shear stress is the force on one plane divided by the bolt's cross-sectional area.",
   r"A = \frac{π([d])^{2}}{4} = [pi*d*d/4|1] mm^{2}. || Stress = \frac{[P*1000|0] / 2}{[pi*d*d/4|1]} = [ans|1] MPa.",
   "P*1000/2/(pi*d*d/4)", wrong=["P*1000/(pi*d*d/4)", "P*1000/2/(pi*d*d)", "2*P*1000/(pi*d*d/4)"], P=[40, 110, 24], d=[16, 24, 12])
NQ('mechmat-b', '-', 'MPa', 1, 150, "A [d] mm diameter bolt bears against a plate [t] mm thick and transfers [P] kN to it. What is the average bearing stress on the plate?",
   "Bearing stress is taken on the projected area of contact, the bolt diameter times the plate thickness, not on the curved surface.",
   r"Bearing stress = \frac{P}{d t} = \frac{[P*1000|0]}{[d]([t])} = [ans|1] MPa.",
   "P*1000/(d*t)", P=[30, 75, 18], d=[20, 22, 16], t=[10, 12, 8])
NQ('mechmat-b', "uniaxial loading and deformation; Hooke's law", '× 10^{-6}', 0, 667, "A cable with a cross-sectional area of [A] mm^{2} and a modulus of elasticity of [E] GPa carries a tension of [P] kN. What is the strain in the cable, in millionths?",
   "Stress is force over area, and Hooke's law gives strain as stress divided by E. Strain has no units and does not depend on the cable's length.",
   r"Stress = \frac{[P*1000|0]}{[A]} = [P*1000/A|1] MPa. || Strain = \frac{[P*1000/A|1]}{[E*1000|0]} = [P/A/E|6] = [ans|0] × 10^{-6}.",
   "P*1000/A/(E*1000)*1e6", P=[20, 45, 8], A=[150, 300, 50], E=[200, 200, 70])
NQ('mechmat-b', 'transverse shear', 'MPa', 2, 4.5, "A rectangular beam [b] mm wide and [h] mm deep carries a shear force of [V] kN. What is the maximum transverse shear stress?",
   "Transverse shear stress in a rectangle varies parabolically, from zero at the top and bottom to a maximum at the neutral axis of 1.5 times the average, V / A.",
   r"Maximum stress = \frac{3V}{2A} = \frac{3([V*1000|0])}{2([b])([h])} = [ans|2] MPa.",
   "1.5*V*1000/(b*h)", wrong=["V*1000/(b*h)", "2*V*1000/(b*h)", "4*V*1000/(3*b*h)"], V=[60, 24, 150], b=[100, 50, 200], h=[200, 150, 400])
NQ('mechmat-b', "Poisson's ratio", 'mm', 5, 0.006, "A [d] mm diameter rod carries an axial tensile stress of [s] MPa. E = [E] GPa and Poisson's ratio is [nu|2]. By how much does its diameter decrease?",
   "Poisson's ratio is lateral strain divided by axial strain, with opposite sign: a bar that stretches gets thinner. Find the axial strain from Hooke's law, multiply by the ratio, then by the diameter.",
   r"Axial strain = \frac{[s]}{[E*1000|0]} = [s/E/1000|6]. || Lateral strain = [nu|2] × [s/E/1000|6] = [nu*s/E/1000|6]. || Change in diameter = [nu*s/E/1000|6] × [d] = [ans|5] mm.",
   "nu*s/(E*1000)*d", d=[25, 40, 12], s=[160, 105, 210], E=[200, 70, 200], nu=[0.30, 0.33, 0.29])
NQ('mechmat-b', 'stresses in beams', '× 10^{3} mm^{3}', 1, 300, "A beam must resist a bending moment of [M] kN·m without the bending stress exceeding [s] MPa. What section modulus is required?",
   "Bending stress is M / S, where the section modulus S is I / c. The required section modulus is the moment divided by the allowable stress.",
   r"S = \frac{M}{stress} = \frac{[M] × 10^{6}}{[s]} = [M*1e6/s|0] mm^{3} = [ans|1] × 10^{3} mm^{3}.",
   "M*1e6/s/1000", M=[45, 120, 18], s=[150, 165, 10])
NQ('mechmat-b', 'shear stress-strain', 'GPa', 1, 76.9, "A material has a modulus of elasticity of [E] GPa and a Poisson's ratio of [nu|2]. What is its shear modulus?",
   "For an isotropic elastic material only two of E, G and Poisson's ratio are independent: G = E / (2(1 + Poisson's ratio)).",
   r"G = \frac{[E]}{2(1 + [nu|2])} = [ans|1] GPa.",
   "E/(2*(1+nu))", E=[200, 70, 110], nu=[0.30, 0.33, 0.34])
NQ('mechmat-b', 'torsion', 'MPa', 2, 43.65, "A hollow shaft with an outside diameter of [do] mm and an inside diameter of [di] mm carries a torque of [T] kN·m. What is the maximum shear stress?",
   "Torsional shear stress is T r / J and is greatest at the outer surface. For a tube, J is the outer circle's polar moment of inertia minus the bore's.",
   r"J = \frac{π([do]^{4} - [di]^{4})}{32} = [pi*(do**4-di**4)/32|0] mm^{4}. || Stress = \frac{([T] × 10^{6})([do/2|1])}{[pi*(do**4-di**4)/32|0]} = [ans|2] MPa.",
   "T*1e6*(do/2)/(pi*(do**4-di**4)/32)", T=[3, 10, 0.8], do=[80, 120, 50], di=[60, 100, 40])
NQ('mechmat-c', 'uniaxial loading and deformation', 'kN', 1, 47.0, "A steel bar (E = 200 GPa) [L1] mm long with an area of [A1] mm^{2} is joined end to end with an aluminium bar (E = 70 GPa) [L2] mm long with an area of [A2] mm^{2}. What axial force stretches the pair by a total of [dl|1] mm?",
   "Bars in series carry the same force, and their elongations add. Write the total as P times the sum of L / (A E) for the two bars, then solve for P. Working in N and mm gives the force in N.",
   r"\frac{L}{AE}: steel \frac{[L1]}{[A1](200,000)} = [L1/(A1*200000)*1e5|4] × 10^{-5} mm/N; aluminium \frac{[L2]}{[A2](70,000)} = [L2/(A2*70000)*1e5|4] × 10^{-5} mm/N. || P = \frac{[dl|1]}{[(L1/(A1*200000)+L2/(A2*70000))*1e5|4] × 10^{-5}} = [dl/(L1/(A1*200000)+L2/(A2*70000))|0] N = [ans|1] kN.",
   "dl/(L1/(A1*200000)+L2/(A2*70000))/1000", dl=[2, 1.5, 3], L1=[1500, 2000, 800], A1=[400, 900, 250], L2=[1000, 1200, 1500], A2=[600, 1200, 500])
NQ('mechmat-c', 'thermal deformations', '°C', 1, 20.8, "A bar [L|1] m long has a gap of [gap|1] mm between its free end and a rigid wall. Its coefficient of thermal expansion is [al] × 10^{-6} per °C. What temperature rise just closes the gap?",
   "A free bar lengthens by (coefficient)(length)(temperature change). Set that equal to the gap. No stress develops until the gap has closed.",
   r"Temperature rise = \frac{gap}{(coefficient) L} = \frac{[gap|1]}{([al] × 10^{-6})([L*1000|0])} = [ans|1] °C.",
   "gap/(al*1e-6*L*1000)", L=[2, 3, 1.2], gap=[0.5, 1.2, 0.4], al=[12, 23, 17])
NQ('mechmat-c', 'deflection of beams', 'mm', 2, 4.22, "A simply supported beam spans [L] m and carries a uniform load of [w] kN/m. Its flexural rigidity EI is [EI] kN·m^{2}. What is the midspan deflection?",
   "For a simply supported beam under uniform load, the maximum deflection is at midspan and equals 5 w L^{4} / (384 EI). The fourth power makes deflection very sensitive to span.",
   r"Deflection = \frac{5 w L^{4}}{384 EI} = \frac{5([w])([L])^{4}}{384([EI])} = [5*w*L**4/(384*EI)|6] m = [ans|2] mm.",
   "5*w*L**4/(384*EI)*1000", L=[6, 8, 4], w=[10, 5, 25], EI=[40000, 60000, 15000])
NQ('mechmat-c', 'uniaxial loading and deformation', 'kN', 2, 40, "A uniform bar [L|1] m long is fixed to rigid walls at both ends. An axial force of [P] kN is applied at a point [a|1] m from the left wall. What is the reaction at the left wall?",
   "The bar is statically indeterminate, so use compatibility: the part on one side stretches as much as the other side shortens. For a uniform bar each wall takes a share of the load in proportion to the length of the opposite segment.",
   r"R_{left} = P × \frac{L - a}{L} = [P] × \frac{[L-a|1]}{[L|1]} = [ans|2] kN. The right wall takes the other [P*a/L|2] kN.",
   "P*(L-a)/L", P=[60, 90, 25], L=[3, 4.5, 2], a=[1, 1.5, 0.5])
NQ('mechmat-d', 'stresses in beams; uniaxial loading and deformation', 'MPa', 2, 19.44, "A square column [b] mm on a side carries a compressive load of [P] kN applied [ec] mm from its centroid, on one axis of symmetry. What is the maximum tensile stress on the cross-section?",
   "An eccentric load is an axial force plus a moment P e. The axial part compresses the whole section by P / A. The bending part adds M c / I in compression on the loaded side and in tension on the far side.",
   r"Axial: \frac{[P*1000|0]}{[b*b]} = [P*1000/b/b|3] MPa compression. || Bending: \frac{M c}{I} = \frac{6 P e}{b^{3}} = \frac{6([P*1000|0])([ec])}{[b]^{3}} = [6*P*1000*ec/b**3|3] MPa. || Far face: [6*P*1000*ec/b**3|3] - [P*1000/b/b|3] = [ans|2] MPa tension.",
   "6*P*1000*ec/b**3-P*1000/b/b", P=[20, 35, 12], b=[120, 150, 100], ec=[300, 400, 250])
NQ('mechmat-d', 'cylindrical pressure vessel', 'MPa', 1, 45, "A thin-walled cylindrical tank with closed ends has a radius of [r] mm and a wall thickness of [t] mm. The internal pressure is [p|1] MPa. What is the longitudinal (axial) stress in the wall?",
   "The pressure on the end cap, p π r^{2}, is carried by the wall's ring of area 2π r t, giving p r / (2t). The hoop stress, p r / t, is twice as large, which is why pipes split lengthwise.",
   r"Longitudinal stress = \frac{p r}{2 t} = \frac{[p|1]([r])}{2([t])} = [ans|1] MPa.",
   "p*r/(2*t)", wrong=["p*r/t", "p*r/(4*t)", "2*p*r/t"], p=[1.2, 2.0, 0.8], r=[600, 400, 750], t=[8, 10, 6])
NQ('mechmat-d', "Mohr's Circle", 'MPa', 2, 51.96, "A bar carries a uniaxial tensile stress of [s] MPa. What is the shear stress on a plane whose normal makes [th]° with the bar's axis?",
   "On an inclined plane a uniaxial stress resolves into a normal part and a shear part. The shear stress is (stress) sin(angle) cos(angle), which peaks at half the axial stress on the 45° plane.",
   r"Shear stress = [s] sin [th]° cos [th]° = [s]([sin(rad(th))|4])([cos(rad(th))|4]) = [ans|2] MPa.",
   "s*sin(rad(th))*cos(rad(th))", s=[120, 80, 200], th=[30, 45, 20])
NQ('mechmat-d', "Mohr's Circle", 'MPa', 1, 90, "At a point on a shaft surface there is a bending stress of [s] MPa in tension and a torsional shear stress of [t] MPa. There is no other stress. What is the maximum principal stress?",
   "With one normal stress and a shear stress, Mohr's circle is centred at half the normal stress. Its radius is the hypotenuse of half the normal stress and the shear stress. The larger principal stress is centre plus radius.",
   r"Centre = \frac{[s]}{2} = [s/2|1] MPa. Radius = \sqrt{[s/2|1]^{2} + [t]^{2}} = [hypot(s/2,t)|2] MPa. || Maximum principal stress = [s/2|1] + [hypot(s/2,t)|2] = [ans|1] MPa.",
   "s/2+hypot(s/2,t)", s=[80, 60, 100], t=[30, 40, 120])
if __name__ == '__main__': run('f3')
