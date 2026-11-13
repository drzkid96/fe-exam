from author_dsl import *
U = None
# ---------------- Mathematics and Statistics ----------------
M('math-a', r"A circle has the equation x^{2} + y^{2} - 6x + 8y = 0. What is its radius?", ['3', '4', '5', '25'], 2,
  "Rearranging the equation shows where the centre is. The leftover number on the other side is the radius squared.",
  r"Complete the square: (x - 3)^{2} + (y + 4)^{2} = 9 + 16 = 25. || Radius = \sqrt{25} = 5.", "sqrt(3**2 + 4**2)", units=U)
N('math-a', "What is the straight-line distance between the points (1, 2) and (7, 10)?", 10, 'units',
  "Draw a right triangle between the two points. The distance is its long side.",
  r"d = \sqrt{(7 - 1)^{2} + (10 - 2)^{2}} = \sqrt{36 + 64} = 10.", "hypot(7-1, 10-2)", units=U)
M('math-a', "Two sides of a triangle are 5 m and 7 m long and meet at an angle of 60°. How long is the third side?", ['4.36 m', '6.24 m', '8.60 m', '10.44 m'], 1,
  "The law of cosines is the right-triangle rule with a correction for triangles that are not right-angled.",
  r"c^{2} = 5^{2} + 7^{2} - 2(5)(7) cos 60° = 25 + 49 - 35 = 39. || c = \sqrt{39} = 6.24 m.", "sqrt(25 + 49 - 2*5*7*cos(rad(60)))")
M('math-b', r"What is the slope of the curve y = x^{3} - 6x at x = 2?", ['-4', '6', '12', '18'], 1,
  "The derivative tells you how steep the curve is at one spot, like the grade of a road at one station.",
  r"\frac{dy}{dx} = 3x^{2} - 6. At x = 2: 3(4) - 6 = 6. || The value -4 is the height of the curve there, not its slope.", "3*2**2 - 6", units=U)
N('math-b', r"What is the maximum value of f(x) = -2x^{2} + 12x + 5?", 23, '',
  "At the very top of a hill the ground is flat. Find where the slope is zero, then read the height there.",
  r"f'(x) = -4x + 12 = 0 gives x = 3. || f(3) = -2(9) + 12(3) + 5 = 23.", "max(-2*x*x + 12*x + 5 for x in [i/1000 for i in range(6001)])", units=U)
N('math-b', "A vehicle's speed is v(t) = 4t + 2, in m/s. How far does it travel between t = 0 and t = 3 s?", 24, 'm',
  "Distance is speed added up over time, which is the area under the speed graph.",
  r"Distance = integral of (4t + 2) dt = 2t^{2} + 2t, from 0 to 3 = 18 + 6 = 24 m.", "simpson(lambda t: 4*t + 2, 0, 3)")
M('math-c', "For **A** = 2**i** + 3**j** and **B** = 4**i** - **j**, what is the magnitude of the cross product **A** × **B**?", ['5', '10', '14', '20'], 2,
  "The cross product measures how much two arrows are not lined up. Its size is the area of the parallelogram they form.",
  "For vectors in a plane, |A × B| = |A_{x}B_{y} - A_{y}B_{x}| = |2(-1) - 3(4)| = 14. || The value 5 is the dot product.", "abs(2*-1 - 3*4)", units=U)
N('math-c', "What is the magnitude of the vector 3**i** - 4**j** + 12**k**?", 13, '',
  "The length of an arrow in three dimensions is the right-triangle rule used twice.",
  r"|V| = \sqrt{3^{2} + 4^{2} + 12^{2}} = \sqrt{169} = 13.", "sqrt(9 + 16 + 144)", units=U)
M('math-d', "Two fair dice are rolled. What is the probability that the total is 7?", ['0.083', '0.139', '0.167', '0.194'], 2,
  "Count the ways to win and divide by all the ways the dice can land.",
  r"There are 36 equally likely outcomes. Six of them total 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1). || P = \frac{6}{36} = 0.167.", "6/36", units=U)
M('math-d', "Concrete strength is normally distributed with a mean of 30 MPa and a standard deviation of 4 MPa. What fraction of tests fall below 26 MPa?", ['0.0228', '0.1587', '0.3413', '0.8413'], 1,
  "Turn the value into a count of standard deviations from the average, then look that count up in the normal table.",
  r"z = \frac{26 - 30}{4} = -1. || From the unit normal table, the area below z = -1 is 0.1587.", "0.5*(1 + erf(-1/sqrt(2)))")
N('math-d', "A least-squares line is fitted to the points (1, 2), (2, 4) and (3, 5). What is its slope?", 1.5, '',
  "The best-fit line is the one that leaves the smallest total squared miss. Its slope compares how y moves with x to how x moves by itself.",
  r"Means: x = 2, y = 3.67. || S_{xy} = (-1)(-1.67) + 0 + (1)(1.33) = 3.0 and S_{xx} = 1 + 0 + 1 = 2. || Slope = \frac{3.0}{2} = 1.5.",
  "sum((x-2)*(y-11/3) for x, y in [(1,2),(2,4),(3,5)]) / sum((x-2)**2 for x in (1,2,3))", units=U)
M('math-d', "Each item from a process has a 10% chance of being defective. In a sample of 5 items, what is the probability that exactly 2 are defective?", ['0.0081', '0.0729', '0.3281', '0.5905'], 1,
  "Work out the chance of one particular pattern of two bad and three good, then multiply by how many such patterns exist.",
  r"P = C(5, 2)(0.1)^{2}(0.9)^{3} = 10(0.01)(0.729) = 0.0729.", "comb(5,2)*0.1**2*0.9**3", units=U)
# ---------------- Ethics and Professional Practice ----------------
COMMON = 'Common-law principle of professional negligence (standard of care for design professionals)'
M('ethics-b', "In a negligence claim, an engineer's work is judged against which standard?", ['A guarantee that the finished work is free of defects', 'The care and skill ordinarily used by competent engineers in similar circumstances', 'Whatever the client instructed', 'The lowest-cost design that meets code'], 1,
  "Engineers are not expected to be perfect. They are expected to be as careful as a good engineer normally is.",
  "The standard of care is what a reasonably prudent engineer would do in the same situation. || It is not a warranty of a perfect result, and following a client's instruction does not excuse careless work.", basis=COMMON, units=U)
M('ethics-b', "Which type of insurance covers claims that an engineer's design errors caused a client financial loss?", ['General liability', 'Professional liability (errors and omissions)', "Workers' compensation", "Builder's risk"], 1,
  "Different policies cover different kinds of trouble. Mistakes in professional advice have their own policy.",
  "Professional liability insurance covers negligent acts, errors and omissions in professional services. || General liability covers bodily injury and property damage, workers' compensation covers employee injuries, and builder's risk covers the work while it is being built.", basis='Standard insurance definitions used in construction and design contracts', units=U)
M('ethics-d', "Which of the following is required for a contract to be enforceable?", ['Notarization of all signatures', 'Consideration exchanged by the parties', 'Approval by the state licensing board', 'A written document in every case'], 1,
  "A contract is a trade. Each side has to give something of value, or it is only a promise.",
  "A valid contract needs an offer, acceptance, consideration, competent parties and a lawful purpose. || Many contracts are enforceable without being written or notarized.", basis='Common-law elements of a valid contract', units=U)
M('ethics-d', "An owner agrees to pay a contractor one fixed price for the whole job, whatever it actually costs the contractor. What type of contract is this?", ['Unit price', 'Cost plus fixed fee', 'Lump sum', 'Time and materials'], 2,
  "With one fixed price, the builder keeps the savings if the job goes well and eats the loss if it does not.",
  "A lump sum contract fixes the total price, so the contractor carries the cost risk. || Unit price pays per measured quantity. Cost plus and time and materials reimburse actual costs.", basis='Standard construction contract types', units=U)
M('ethics-a', "A supplier offers an engineer a paid holiday if the engineer specifies the supplier's pumps on a client's project. Under the NCEES Model Rules, what should the engineer do?", ['Accept, provided the pumps meet the specification', 'Accept, then tell the client afterwards', 'Decline the offer', 'Accept only if the value is modest'], 2,
  "A gift tied to a decision you make for a client is a bribe, whatever it is called.",
  "The Model Rules forbid soliciting or accepting gratuities from contractors, suppliers or other parties in connection with work for an employer or client. || The quality of the product does not change that.", basis='FE Reference Handbook 10.0.1, Ethics and Professional Practice, Model Rules of Professional Conduct: obligation to employers and clients', units=U)
# ---------------- Engineering Economics ----------------
M('econ-b', "A machine has fixed costs of $50,000 per year and variable costs of $12 per unit. What is the average cost per unit at 10,000 units per year?", ['$5', '$12', '$17', '$62'], 2,
  "Fixed costs are shared out over everything you make. The more you make, the smaller each unit's share.",
  r"Total cost = 50,000 + 12(10,000) = $170,000. || Average cost = \frac{170,000}{10,000} = $17 per unit.", "(50000 + 12*10000)/10000", units=U)
N('econ-b', "A task needs 40 hours of direct labor at $35 per hour and $600 of materials. Overhead is charged at 50% of direct labor. What is the total cost?", 2700, '$',
  "Direct costs are the hands and the materials on the job. Overhead is everything in the background, added as a share of the direct cost.",
  "Direct labor = 40(35) = $1,400. Overhead = 0.50(1,400) = $700. || Total = 1,400 + 600 + 700 = $2,700.", "40*35 + 600 + 0.5*40*35", units=U)
M('econ-a', "What is the present worth of $10,000 received 6 years from now at an interest rate of 5% per year?", ['$7,462', '$7,692', '$7,835', '$13,401'], 0,
  "Money you have to wait for is worth less today, because today's money could have been earning interest the whole time.",
  r"P = \frac{F}{(1 + i)^{n}} = \frac{10,000}{(1.05)^{6}} = $7,462.", "10000/1.05**6", units=U)
N('econ-a', "A loan charges a nominal rate of 12% per year, compounded monthly. What is the effective annual interest rate?", 12.68, '%',
  "Charging 1% twelve times is slightly more than charging 12% once, because each month's interest earns interest too.",
  r"i_{e} = (1 + \frac{0.12}{12})^{12} - 1 = (1.01)^{12} - 1 = 0.1268 = 12.68%.", "((1 + 0.12/12)**12 - 1)*100", tol=0.005, units=U)
M('econ-c', "A flood wall costs $300,000 to build and $15,000 per year to maintain. It prevents $60,000 of damage per year. Over 20 years at 6%, what is the benefit-cost ratio?", ['0.69', '1.20', '1.46', '2.29'], 2,
  "Put all the good the project does and all it costs into today's dollars, then see how many dollars of good you get per dollar spent.",
  r"(P/A, 6%, 20) = 11.47. || Benefits = 60,000(11.47) = $688,200. Costs = 300,000 + 15,000(11.47) = $472,000. || B/C = \frac{688,200}{472,000} = 1.46.",
  "60000*((1.06**20-1)/(0.06*1.06**20)) / (300000 + 15000*((1.06**20-1)/(0.06*1.06**20)))", units=U)
N('econ-c', "A machine costs $40,000, costs $3,000 per year to run, and has a salvage value of $5,000 after 8 years. At 10% interest, what is its equivalent uniform annual cost?", 10060, '$ per year',
  "Spread the purchase price over the years like a loan payment, add the yearly running cost, and take off the yearly value of what you get back at the end.",
  "EUAC = 40,000(A/P, 10%, 8) + 3,000 - 5,000(A/F, 10%, 8) = 40,000(0.1874) + 3,000 - 5,000(0.0874) = $10,060.",
  "40000*(0.1*1.1**8/(1.1**8-1)) + 3000 - 5000*(0.1/(1.1**8-1))", units=U)
M('econ-d', "Option A pays a certain $30,000. Option B has a 60% chance of paying $60,000 and a 40% chance of losing $10,000. Based on expected value, which option is better and by how much?", ['A by $2,000', 'B by $2,000', 'B by $6,000', 'They are equal'], 1,
  "Compare the sure thing with the average result of the gamble.",
  "EV of B = 0.60(60,000) + 0.40(-10,000) = 36,000 - 4,000 = $32,000. || That is $2,000 more than the certain $30,000.",
  "('B' if 0.6*60000 - 0.4*10000 > 30000 else 'A') + ' by $%s' % format(int(abs(0.6*60000 - 0.4*10000 - 30000)), ',')", units=U)
# ---------------- Statics ----------------
N('statics-b', "Two parallel 50 N forces act in opposite directions, 0.4 m apart. What is the moment of this couple?", 20, 'N·m',
  "Two equal and opposite pushes that are not in line make a pure twist, like turning a steering wheel with both hands.",
  "M = F × d = 50(0.4) = 20 N·m. || A couple has the same moment about every point.", "50*0.4")
M('statics-b', "A 200 N downward force acts 0.3 m to the right of point O. It is replaced by a force at O plus a couple. What is the magnitude of the couple?", ['6 N·m', '60 N·m', '200 N·m', '667 N·m'], 1,
  "You can slide a force sideways to a new point as long as you add the twist it used to make about that point.",
  "The equivalent system is the same 200 N force at O plus a couple M = 200(0.3) = 60 N·m, clockwise.", "200*0.3")
M('statics-d', "A symmetric triangular truss spans 8 m and is 3 m high. A 24 kN load acts at the apex. What is the force in each inclined member?", ['12 kN', '15 kN', '16 kN', '20 kN'], 3,
  "Each sloping member has to hold up half the load, but it leans, so it must push harder than the share it supports.",
  r"Each support reaction is 12 kN. The inclined member is 5 m long (3-4-5 triangle), so sin(angle) = \frac{3}{5}. || At a support joint: F(\frac{3}{5}) = 12, so F = 20 kN, in compression.", "12/(3/hypot(3,4))")
N('statics-d', "For the same truss (8 m span, 3 m high, 24 kN at the apex), what is the force in the horizontal bottom member?", 16, 'kN',
  "The sloping members push outward at the supports. The bottom member is the tie that stops the feet spreading apart.",
  r"The inclined member carries 20 kN. Its horizontal part is 20(\frac{4}{5}) = 16 kN, which the bottom member resists in tension.", "12/(3/5)*(4/5)")
M('statics-a', "A 150 N force is applied to the end of a 2 m lever, at 30° to the lever's axis. What is the moment about the pivot?", ['75 N·m', '150 N·m', '260 N·m', '300 N·m'], 1,
  "Only the part of the push that is square to the lever turns it. The part along the lever just pulls on the pivot.",
  "M = F d sin(angle) = 150(2) sin 30° = 150 N·m.", "150*2*sin(rad(30))")
N('statics-c', "A simply supported beam spans 10 m. It carries a uniform load of 4 kN/m over its full length and a 20 kN point load at midspan. What is each support reaction?", 30, 'kN',
  "When the loads are placed evenly about the middle, the two supports share the total equally.",
  r"Total load = 4(10) + 20 = 60 kN. By symmetry each reaction = \frac{60}{2} = 30 kN.", "(4*10 + 20)/2")
M('statics-e', "An L-shaped area is made of a vertical leg 20 mm wide and 80 mm tall, with a horizontal leg 60 mm wide and 20 mm tall attached to the bottom of its right side. How far is the centroid from the left edge?", ['20.0 mm', '27.1 mm', '32.9 mm', '40.0 mm'], 1,
  "Split the shape into two rectangles, treat each as a weight at its own centre, and find the balance point.",
  r"Vertical leg: 1,600 mm^{2} at x = 10 mm. Horizontal leg: 1,200 mm^{2} at x = 50 mm. || x = \frac{1,600(10) + 1,200(50)}{2,800} = 27.1 mm.", "(1600*10 + 1200*50)/2800")
N('statics-f', "A rectangle is 100 mm wide and 200 mm tall. What is its moment of inertia about its base? Give the answer in units of 10^{6} mm^{4}.", 266.7, '× 10^{6} mm^{4}',
  "Moving the axis away from the middle of a shape makes it look stiffer, because all the material is now farther from the axis.",
  r"Parallel axis theorem: I = \frac{bh^{3}}{12} + Ad^{2} = 66.67 × 10^{6} + (20,000)(100)^{2} = 266.7 × 10^{6} mm^{4}. || The shortcut is \frac{bh^{3}}{3}.", "(100*200**3/12 + 100*200*100**2)/1e6")
N('statics-g', "A 500 N crate sits on a level floor with a static friction coefficient of 0.35. A rope pulls on it at 30° above the horizontal. What rope force starts the crate moving?", 168, 'N',
  "Pulling upward at an angle does two things: it drags the crate forward and it lifts some weight off the floor, which reduces the grip.",
  "Horizontal: P cos 30° = 0.35 N. Vertical: N = 500 - P sin 30°. || P(0.866) = 0.35(500 - 0.5P), so P(0.866 + 0.175) = 175 and P = 168 N.", "0.35*500/(cos(rad(30)) + 0.35*sin(rad(30)))")
M('statics-c', "A 1,000 N weight hangs from two cables. Each cable makes an angle of 30° with the horizontal. What is the tension in each cable?", ['500 N', '577 N', '866 N', '1,000 N'], 3,
  "Only the upward part of each cable's pull holds the weight. The flatter the cables, the harder they must pull to get the same lift.",
  r"Vertical equilibrium: 2T sin 30° = 1,000. || T = \frac{1,000}{2(0.5)} = 1,000 N.", "1000/(2*sin(rad(30)))")
# ---------------- Dynamics ----------------
M('dynamics-a', "A ball is launched from level ground at 20 m/s, at 30° above the horizontal. Ignoring air resistance, how far away does it land? Use g = 9.81 m/s^{2}.", ['17.7 m', '20.4 m', '35.3 m', '40.8 m'], 2,
  "The ball moves sideways at a steady speed while gravity pulls it back down. How long it stays in the air decides how far it gets.",
  r"Range = \frac{v^{2} sin(2 × 30°)}{g} = \frac{400(0.866)}{9.81} = 35.3 m.", "20**2*sin(rad(60))/g")
N('dynamics-a', "A car travels at a constant 20 m/s around a curve of radius 80 m. What is its acceleration toward the centre of the curve?", 5, 'm/s^{2}',
  "Even at steady speed, turning means the direction of travel keeps changing. That change is an acceleration pointing into the turn.",
  r"a_{n} = \frac{v^{2}}{r} = \frac{20^{2}}{80} = 5 m/s^{2}.", "20**2/80")
M('dynamics-b', "A solid uniform disk has a mass of 10 kg and a radius of 0.3 m. What is its mass moment of inertia about its central axis?", ['0.15 kg·m^{2}', '0.45 kg·m^{2}', '0.90 kg·m^{2}', '1.50 kg·m^{2}'], 1,
  "A disk is easier to spin than a ring of the same mass, because much of its mass sits near the middle.",
  r"I = \frac{1}{2}mr^{2} = \frac{1}{2}(10)(0.3)^{2} = 0.45 kg·m^{2}. || A thin ring would be mr^{2} = 0.90 kg·m^{2}.", "0.5*10*0.3**2")
M('dynamics-c', "A block slides down a frictionless incline at 30° to the horizontal. What is its acceleration? Use g = 9.81 m/s^{2}.", ['4.91 m/s^{2}', '5.66 m/s^{2}', '8.50 m/s^{2}', '9.81 m/s^{2}'], 0,
  "Only the part of gravity that points down the slope speeds the block up. The rest presses it into the surface.",
  "a = g sin 30° = 9.81(0.5) = 4.91 m/s^{2}. || The mass cancels.", "g*sin(rad(30))")
N('dynamics-c', "A net torque of 12 N·m acts on a flywheel with a mass moment of inertia of 3 kg·m^{2}. What is its angular acceleration?", 4, 'rad/s^{2}',
  "Torque is the turning version of force, and moment of inertia is the turning version of mass.",
  r"Angular acceleration = \frac{T}{I} = \frac{12}{3} = 4 rad/s^{2}.", "12/3")
M('dynamics-d', "A hoist lifts a 500 kg load at a constant 2 m/s. What power is delivered to the load? Use g = 9.81 m/s^{2}.", ['1.0 kW', '4.9 kW', '9.8 kW', '19.6 kW'], 2,
  "Power is how fast work is done. Lifting a heavier load, or lifting faster, takes more power.",
  "P = F × v = (500)(9.81)(2) = 9,810 W = 9.8 kW.", "500*g*2/1000")
N('dynamics-d', "A spring with a stiffness of 2,000 N/m is compressed 0.1 m and released against a 0.5 kg block on a frictionless surface. What speed does the block reach?", 6.32, 'm/s',
  "A squeezed spring stores energy. When it lets go, that energy becomes the block's motion.",
  r"\frac{1}{2}kx^{2} = \frac{1}{2}mv^{2}: \frac{1}{2}(2,000)(0.1)^{2} = 10 J. || v = \sqrt{\frac{2(10)}{0.5}} = 6.32 m/s.", "sqrt(2000*0.1**2/0.5)")
# ---------------- Mechanics of Materials ----------------
M('mechmat-a', "A simply supported beam spans 8 m and carries a uniform load of 10 kN/m. What is the maximum shear force?", ['20 kN', '40 kN', '80 kN', '160 kN'], 1,
  "Shear is biggest right next to a support, where the beam hands its whole share of the load to that support.",
  r"Each reaction = \frac{wL}{2} = \frac{10(8)}{2} = 40 kN, and the largest shear equals the reaction.", "10*8/2")
M('mechmat-b', "A solid circular shaft 50 mm in diameter carries a torque of 2 kN·m. What is the maximum shear stress?", ['20.4 MPa', '40.7 MPa', '81.5 MPa', '163 MPa'], 2,
  "Twisting a shaft shears it. The outside surface works hardest because it is farthest from the centre.",
  r"Shear stress = \frac{Tc}{J} = \frac{16T}{π d^{3}} = \frac{16(2 × 10^{6})}{π(50)^{3}} = 81.5 MPa.", "16*2e6/(pi*50**3)")
N('mechmat-b', "A steel bar is held rigidly between two walls and heated by 40 °C. Its coefficient of thermal expansion is 12 × 10^{-6} per °C and E = 200 GPa. What compressive stress develops?", 96, 'MPa',
  "A heated bar wants to grow. If the walls will not let it, the bar pushes on them, and that push is stress.",
  "Stress = E × expansion coefficient × temperature change = 200,000(12 × 10^{-6})(40) = 96 MPa.", "200e3*12e-6*40")
N('mechmat-c', "A steel rail 10 m long warms by 30 °C. Its coefficient of thermal expansion is 12 × 10^{-6} per °C. How much longer does it get if it is free to expand?", 3.6, 'mm',
  "Almost everything grows a little when it warms up. Longer pieces and bigger temperature swings mean more growth.",
  "Change in length = expansion coefficient × length × temperature change = 12 × 10^{-6}(10,000 mm)(30) = 3.6 mm.", "12e-6*10000*30")
M('mechmat-d', "The principal stresses at a point are 120 MPa in tension and 40 MPa in compression. What is the maximum in-plane shear stress?", ['40 MPa', '80 MPa', '120 MPa', '160 MPa'], 1,
  "The biggest shear is half the gap between the largest pull and the largest push.",
  r"Maximum shear = \frac{120 - (-40)}{2} = 80 MPa. || It is the radius of Mohr's circle.", "(120 - -40)/2")
M('mechmat-d', "A thin-walled cylindrical tank has a radius of 500 mm and a wall thickness of 10 mm. The internal pressure is 2 MPa. What is the hoop stress in the wall?", ['25 MPa', '50 MPa', '100 MPa', '200 MPa'], 2,
  "Pressure tries to split the tank along its length, like a sausage splitting when it is cooked. The stress around the tank is twice the stress along it.",
  r"Hoop stress = \frac{pr}{t} = \frac{2(500)}{10} = 100 MPa. || The axial stress is half that, 50 MPa.", "2*500/10")
# ---------------- Materials ----------------
M('materials-a', "A concrete mix contains 350 kg of cement per cubic metre. The specific gravity of cement is 3.15. What volume does the cement occupy?", ['0.035 m^{3}', '0.111 m^{3}', '0.350 m^{3}', '1.10 m^{3}'], 1,
  "Mix design is like filling a one cubic metre box. Each ingredient takes up space according to how heavy and how dense it is.",
  r"Volume = \frac{mass}{specific gravity × density of water} = \frac{350}{3.15(1,000)} = 0.111 m^{3}.", "350/(3.15*1000)")
M('materials-a', "An asphalt mix sample has a total mass of 1,200 g, of which 60 g is asphalt binder. What is the asphalt content by total mass of mix?", ['4.8%', '5.0%', '5.3%', '20%'], 1,
  "Asphalt content is the share of the whole mix that is binder. Be clear whether the share is of the whole mix or of the stone alone.",
  r"Asphalt content = \frac{60}{1,200} × 100 = 5.0%. || Dividing by the aggregate mass (1,140 g) instead gives 5.3%, which is a different measure.", "60/1200*100", units=U)
M('materials-b', "Which property does a Rockwell test measure?", ['Hardness', 'Fatigue life', 'Impact toughness', 'Creep rate'], 0,
  "A Rockwell tester presses a small point into the metal and measures how deep the dent goes.",
  "The Rockwell test measures hardness: resistance to permanent indentation. || Impact toughness is measured by Charpy, fatigue by repeated load cycles, and creep by long-term loading.", basis='ASTM E18, Rockwell hardness of metallic materials', units=U)
M('materials-b', "What is the minimum yield strength of Grade 60 reinforcing steel?", ['36 ksi', '40 ksi', '60 ksi', '75 ksi'], 2,
  "The grade number of rebar is its yield strength in thousands of pounds per square inch.",
  "Grade 60 bars have a minimum yield strength of 60 ksi, about 420 MPa. || 36 ksi is the yield strength of A36 structural steel.", basis='ASTM A615, deformed carbon-steel bars for concrete reinforcement', units='USCS')
M('materials-c', "Using E_{c} = 4,700 × the square root of f'_{c} (both in MPa), what is the modulus of elasticity of concrete with a compressive strength of 25 MPa?", ['4,700 MPa', '11,750 MPa', '23,500 MPa', '117,500 MPa'], 2,
  "Stronger concrete is also stiffer, but stiffness grows more slowly than strength.",
  r"E_{c} = 4,700\sqrt{25} = 4,700(5) = 23,500 MPa.", "4700*sqrt(25)")
N('materials-c', "A tension specimen has a gauge length of 50 mm. After fracture the gauge length measures 62 mm. What is the percent elongation?", 24, '%',
  "Percent elongation tells you how far a material stretches before it breaks. A high number means a ductile material.",
  r"Elongation = \frac{62 - 50}{50} × 100 = 24%.", "(62 - 50)/50*100", units=U)
M('materials-c', "What does the total area under a material's stress-strain curve, up to fracture, represent?", ['Stiffness', 'Hardness', 'Toughness', 'Yield strength'], 2,
  "A tough material soaks up a lot of energy before it breaks. That takes both strength and stretch.",
  "Toughness is the energy absorbed per unit volume up to fracture, which is the area under the whole curve. || Stiffness is the slope of the straight portion.", basis='Standard definition of toughness (modulus of toughness)', units=U)
save('d1')
