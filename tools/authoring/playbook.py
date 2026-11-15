"""Exam playbooks: for each subtopic, how the question shows up on the FE exam and the fastest move that answers it.
Each row is (if the question..., fast move). Written for speed on the exam, not for depth."""

PLAY = {
# ---------------- Mathematics ----------------
'math-a': [
 ('Gives two points and asks for a slope, distance or midpoint', 'Slope = Δy/Δx; distance = √(Δx² + Δy²); midpoint = averages. No handbook needed.'),
 ('Asks for a line perpendicular or parallel to another', 'Parallel: same slope. Perpendicular: slope = -1/m. Plug one point into y - y1 = m (x - x1).'),
 ('Gives an equation like x² + y² + Dx + Ey + F = 0', 'Complete the square to get the centre and radius; or check the answer choices by substituting.'),
 ('Asks for an area or volume of a standard shape', 'Open the Mensuration of Areas and Volumes pages and copy the formula. Do not derive.'),
],
'math-b': [
 ('Asks for a slope, rate or "derivative at x ="', 'Differentiate term by term, then plug in. Check by evaluating f at x ± 0.001 on the calculator if unsure.'),
 ('Asks for a maximum or minimum', 'Set f′(x) = 0 and solve. If the choices are numbers, plug each into f and pick the largest or smallest.'),
 ('Asks for an area under a curve or a definite integral', 'Integrate and subtract limits, or use the calculator\'s numeric integral if it has one (TI-36X Pro does).'),
 ('Asks for a limit giving 0/0', 'L\'Hôpital: differentiate top and bottom separately, then plug in. Or plug in a number very close to the limit.'),
],
'math-c': [
 ('Asks for a resultant or magnitude', 'Add components; magnitude = √(x² + y² + z²).'),
 ('Asks for the angle between two vectors', 'cos θ = A·B / (|A||B|). Dot product = Ax Bx + Ay By + Az Bz.'),
 ('Asks for a cross product, moment vector or area of a parallelogram', 'Use the 3×3 determinant (i j k / A / B). The calculator\'s vector mode does it in seconds.'),
 ('Asks for a unit vector or a component along a direction', 'Unit vector = A / |A|. Component of F along u = F·u.'),
],
'math-d': [
 ('Gives a short data set and asks for mean, median, mode or standard deviation', 'Use the calculator\'s 1-variable statistics. Check whether they want sample (n - 1) or population (n).'),
 ('Asks for a probability from a normal distribution', 'z = (x - μ)/σ, then read the unit normal table in the handbook. Sketch the bell to see which tail.'),
 ('Asks for a confidence interval', 'mean ± z σ/√n (σ known) or ± t s/√n with n - 1 degrees of freedom. Find z or t in the handbook tables.'),
 ('Asks for the best-fit line or correlation', 'Calculator 2-variable statistics gives slope, intercept and r directly.'),
 ('Asks a counting or "exactly k of n" question', 'Combinations nCr for choices; binomial P = nCk p^k (1 - p)^(n - k).'),
],
# ---------------- Statics ----------------
'statics-a': [
 ('Gives forces at angles and asks for the resultant', 'Fx = F cos θ, Fy = F sin θ for each; sum them; R = √(ΣFx² + ΣFy²); angle = atan(ΣFy/ΣFx).'),
 ('Gives a force by its line of action (two points, or 3-4-5 slopes)', 'Use the ratios: components are F × (run/length) and F × (rise/length). No angles needed.'),
 ('Three-dimensional force', 'Unit vector along the line × F. Components = F × (dx, dy, dz)/length.'),
],
'statics-b': [
 ('Asks for the moment of a force about a point', 'Resolve the force into x and y parts at a convenient point; M = Fx × (y distance) + Fy × (x distance) with signs. Faster than finding d.'),
 ('Asks for an equivalent force-couple system', 'Resultant force is the vector sum; couple = sum of moments about the new point.'),
 ('Gives a couple', 'Couple moment = F × distance between the two forces, the same about any point.'),
 ('Distributed load', 'Replace with its resultant: rectangle w L at L/2; triangle w L/2 at L/3 from the big end.'),
],
'statics-c': [
 ('Asks for support reactions of a beam or frame', 'Draw the free body. Take moments about one support to get the other reaction in one step; then ΣFy = 0.'),
 ('Two-force member or cable at an angle', 'The force acts along the member, so its components follow the member\'s geometry.'),
 ('Pulley or cable hanging a weight', 'Tension is the same on both sides of a frictionless pulley; balance at the hanging point.'),
 ('Checking answers', 'Plug back into the equation you did not use. Reactions must add to the total load.'),
],
'statics-d': [
 ('Asks for one interior member force', 'Method of sections: cut through it and two others, take moments about where those two meet. One equation, one unknown.'),
 ('Asks for a member at a support', 'Method of joints at that support: vertical balance gives the inclined member directly.'),
 ('Unloaded joint with two members not in line, or three members with two in line', 'Zero-force members: spot them first. Saves time and is a common question on its own.'),
 ('Asks tension or compression', 'Assume tension; a negative answer is compression.'),
],
'statics-e': [
 ('Composite shape centroid', 'Table: area, x̄, ȳ for each piece; holes are negative area. x̄ = ΣA x / ΣA.'),
 ('Standard shape (triangle, semicircle, quarter circle)', 'Read the centroid from the handbook table: triangle h/3 from the base, semicircle 4r/(3π) from the diameter.'),
 ('Symmetric shape', 'The centroid is on the axis of symmetry: only one coordinate to compute.'),
],
'statics-f': [
 ('Moment of inertia of a rectangle or circle about its centroid', 'Handbook table: b h³/12; π d⁴/64. h is the dimension perpendicular to the axis.'),
 ('About an axis that is not through the centroid', 'Parallel axis: I = Ī + A d². Do it piece by piece for composite shapes.'),
 ('Radius of gyration', 'r = √(I / A).'),
 ('Polar moment J', 'J = Ix + Iy; for a solid circle π d⁴/32.'),
],
'statics-g': [
 ('Block on a slope: will it slide?', 'Slides if tan θ > μs. Otherwise friction equals the needed force, not μN.'),
 ('Force to start moving a block', 'P = μs N, with N from vertical balance (watch an inclined push changing N).'),
 ('Belt or rope around a drum', 'T2 = T1 e^(μ θ) with θ in radians; T2 is the tight side.'),
 ('Tipping versus sliding', 'Compare the force to slide (μ W) with the force to tip (from moments about the corner); the smaller wins.'),
],
# ---------------- Dynamics ----------------
'dynamics-a': [
 ('Constant acceleration in a straight line', 'Pick the equation without the unknown you do not need: v = v0 + a t; s = v0 t + ½ a t²; v² = v0² + 2 a s.'),
 ('Projectile', 'Horizontal: constant velocity. Vertical: a = -g. Time of flight from the vertical equation, then range = vx × t.'),
 ('Circular motion', 'an = v²/r toward the centre; at = dv/dt; ω = v / r.'),
 ('Velocity or position given as a function of time', 'Differentiate for acceleration, integrate for distance.'),
],
'dynamics-b': [
 ('Mass moment of inertia of a standard body', 'Copy from the handbook table (rod about centre m L²/12, about end m L²/3; disc ½ m r²).'),
 ('About a different axis', 'Parallel axis: I = Ic + m d².'),
 ('Radius of gyration', 'I = m k², so k = √(I / m).'),
],
'dynamics-c': [
 ('Force and acceleration of a block (with friction or on a slope)', 'Free body, then ΣF = m a along the motion; N from the perpendicular direction.'),
 ('Two blocks linked by a cord over a pulley', 'Same acceleration; write ΣF = m a for each, or treat the system: a = (net driving force) / (total mass).'),
 ('Rotation about a fixed axis', 'ΣM = I α. Linear acceleration of a point = α r.'),
 ('Car on a curve', 'Friction or banking supplies m v²/r. Flat curve: v max = √(μ g r).'),
],
'dynamics-d': [
 ('Asks for speed after a drop, a slope or a spring', 'Energy: initial PE + KE + spring = final, minus friction work. No time needed.'),
 ('Asks for impact, collision or a force over a short time', 'Impulse-momentum: F Δt = m Δv. Collisions: momentum is conserved; e relates the separation speed.'),
 ('Power', 'P = F v = work / time. Watch the efficiency: input = output / η.'),
 ('Spring', 'Energy stored = ½ k x²; force = k x.'),
],
# ---------------- Mechanics of materials ----------------
'mechmat-a': [
 ('Maximum moment of a simple beam', 'Use the handbook beam diagrams: UDL w L²/8 at midspan; point load P L/4 at midspan.'),
 ('Shear or moment at a section', 'Cut there, keep the left piece, sum forces for V and moments for M.'),
 ('Where is the maximum moment?', 'Where the shear diagram crosses zero.'),
 ('Sketch matching (which diagram is right)', 'UDL: shear linear, moment parabolic. Point loads: shear steps, moment straight lines.'),
],
'mechmat-b': [
 ('Axial stress, shear stress, bearing stress', 'σ = P/A (area perpendicular); τ = V/A (area of the shear plane, ×2 for double shear); bearing on d × t.'),
 ('Bending stress', 'σ = M c / I, or M / S. c is half the depth for symmetric sections.'),
 ('Strain and Poisson', 'ε = σ/E; lateral strain = -ν ε.'),
 ('Torsion stress', 'τ = T r / J; J = π d⁴/32 for a solid shaft.'),
 ('Thin-walled pressure vessel', 'Hoop σ = p r / t; axial σ = p r / (2t).'),
],
'mechmat-c': [
 ('Elongation of a bar', 'δ = P L / (A E). Several segments: add each segment\'s δ.'),
 ('Temperature change', 'Free: δ = α L ΔT. Restrained: σ = E α ΔT.'),
 ('Beam deflection', 'Copy the case from the handbook beam table; superpose for combined loads.'),
 ('Angle of twist', 'φ = T L / (J G), in radians.'),
],
'mechmat-d': [
 ('Principal stresses', 'σ1,2 = (σx + σy)/2 ± √(((σx - σy)/2)² + τ²). Centre and radius of Mohr\'s circle.'),
 ('Maximum in-plane shear', 'τmax = radius = √(((σx - σy)/2)² + τ²).'),
 ('Angle to the principal planes', 'tan 2θp = 2τ / (σx - σy).'),
 ('Combined axial and bending', 'Add: σ = P/A ± M c / I at each edge.'),
],
# ---------------- Materials ----------------
'materials-a': [
 ('Concrete batch weights or volumes', 'Absolute volume method: each ingredient\'s volume = weight / (SG × 62.4 lb/ft³); add air; total 27 ft³ per yd³.'),
 ('Water-cement ratio', 'w/c = weight of water / weight of cement. Higher w/c, lower strength.'),
 ('Asphalt mix volumetrics (VMA, VFA, air voids)', 'Use the handbook\'s definitions; they are ratios of the mix specific gravities.'),
],
'materials-b': [
 ('Names a test and asks what it measures', 'Slump: workability. Cylinder break: f′c. Charpy: impact toughness. Brinell or Rockwell: hardness. Proctor: compaction.'),
 ('Gives a cylinder load and diameter', 'f′c = P / (π d²/4).'),
 ('Gives a split-tension or flexure test', 'Read the formula from the handbook and plug in.'),
],
'materials-c': [
 ('Stress-strain curve questions', 'Initial slope = E; flat step = yield; peak = ultimate; area under = toughness.'),
 ('Modulus or strain from a load test', 'E = σ/ε = (P/A)/(δ/L).'),
 ('Ductile versus brittle, or which material is which', 'Steel: long plastic range. Concrete and cast iron: brittle, strong in compression.'),
 ('Corrosion, fatigue, creep', 'Definitions: answer from the plain meaning; check the handbook Materials Science section if unsure.'),
],
# ---------------- Fluids ----------------
'fluids-a': [
 ('Orifice or tank draining', 'Q = Cd A √(2 g h). Cd is given or about 0.6.'),
 ('Venturi or pitot', 'Venturi: Q from the Δh with the area-ratio formula. Pitot: V = √(2 g Δh).'),
 ('Weir', 'Rectangular: Q = C L H^(3/2). V-notch: Q = C H^(5/2). Constants from the handbook, units matter.'),
],
'fluids-b': [
 ('Density, specific weight, specific gravity', 'γ = ρ g; SG = ρ / ρwater. Water: 62.4 lb/ft³ or 9.81 kN/m³.'),
 ('Viscosity, shear between plates', 'τ = μ V / y; force = τ × area. Kinematic ν = μ / ρ.'),
 ('Capillary rise or surface tension', 'Copy the handbook formula; check whether d or r is used.'),
],
'fluids-c': [
 ('Pressure at depth or a manometer', 'p = γ h. Manometer: walk from one end to the other, + going down, - going up.'),
 ('Force on a submerged plane surface', 'F = γ hc A (hc to the centroid). Acts at yp = yc + I / (yc A), below the centroid.'),
 ('Buoyancy or floating', 'FB = γ × submerged volume. Floating: FB = weight, so submerged fraction = SG.'),
],
'fluids-d': [
 ('Two pipe sections, find velocity or pressure', 'Continuity A1 V1 = A2 V2, then Bernoulli with head losses.'),
 ('Head loss in a pipe', 'Darcy: hf = f (L/D) V²/(2g). f from the Moody chart (Re and ε/D), or 64/Re if laminar.'),
 ('Force from a jet or a bend', 'F = ρ Q ΔV in each direction (plus p A terms for a bend).'),
 ('Pump power', 'P = γ Q H / η.'),
],
# ---------------- Water resources ----------------
'water-a': [
 ('Peak runoff from a small watershed', 'Rational method: Q = C i A (acres and in/h give ft³/s directly).'),
 ('Runoff depth from a storm (SCS)', 'S = 1000/CN - 10; Q = (P - 0.2S)² / (P + 0.8S).'),
 ('Unit hydrograph', 'Scale ordinates by the runoff depth; shift and add for longer storms.'),
 ('Return period and risk', 'Risk of at least one in n years = 1 - (1 - 1/T)^n.'),
],
'water-b': [
 ('Open channel flow', 'Manning: Q = (1.49/n) A R^(2/3) S^(1/2) in US units (1.0 in SI). R = A / wetted perimeter.'),
 ('Critical depth', 'Rectangular: yc = (q²/g)^(1/3). Froude > 1 supercritical, < 1 subcritical.'),
 ('Hydraulic jump', 'y2/y1 = ½(-1 + √(1 + 8 Fr1²)).'),
 ('Pipe flow (Hazen-Williams)', 'Copy the handbook form for the units given; C is given.'),
],
'water-c': [
 ('Pump power or efficiency', 'Water power = γ Q H; brake power = water power / η.'),
 ('Operating point', 'Where the pump curve meets the system curve.'),
 ('Changing speed or impeller (affinity laws)', 'Q ∝ N, H ∝ N², P ∝ N³.'),
 ('Cavitation', 'NPSH available = atmospheric + static - vapour - losses (in head); must exceed NPSH required.'),
],
'water-d': [
 ('Pressure at a point in a network', 'Energy from the tank surface to the point minus losses; static case p = γ × elevation difference.'),
 ('Pipes in series or parallel', 'Series: flows equal, losses add. Parallel: losses equal, flows add.'),
 ('Storage or demand sizing', 'Average day × peaking factor; fire flow adds to maximum day.'),
],
'water-e': [
 ('Detention pond outflow or storage', 'Storage = area between the inflow and outflow hydrographs.'),
 ('Probability of a flood', 'P(at least once in n years) = 1 - (1 - 1/T)^n.'),
 ('Culvert or spillway capacity', 'Treat as an orifice or weir and read the coefficient from the question.'),
],
'water-f': [
 ('Peak flow from a site', 'Q = C i A; composite C = Σ C A / Σ A; i from the IDF curve at duration = tc.'),
 ('Time of concentration', 'Add the travel times of each segment along the longest path.'),
 ('Pond volume to treat', 'Water quality volume = rainfall depth × runoff coefficient × area.'),
],
'water-g': [
 ('Sewer capacity or slope', 'Manning for a full pipe; for a partly full pipe use the hydraulic elements chart.'),
 ('Design flow', 'Population × per-capita flow × peaking factor, plus infiltration.'),
 ('Self-cleansing check', 'Velocity at least about 2 ft/s (0.6 m/s) when flowing full.'),
],
'water-h': [
 ('Flow through soil or an aquifer', 'Darcy: Q = K i A, i = Δh / L.'),
 ('Well drawdown (two observation wells)', 'Unconfined: Q = π K (h2² - h1²)/ln(r2/r1). Confined: Q = 2π K b (h2 - h1)/ln(r2/r1).'),
 ('Seepage velocity', 'v = K i / n (porosity), faster than the Darcy velocity.'),
],
'water-i': [
 ('BOD at t days, or ultimate BOD', 'BODt = L0 (1 - e^(-k t)). Check whether k is base e or base 10.'),
 ('BOD from a test bottle', 'BOD = (DO initial - DO final) / P, P = sample volume / bottle volume.'),
 ('Mixing a discharge into a river', 'Mass balance: C = (Q1 C1 + Q2 C2) / (Q1 + Q2).'),
 ('Oxygen sag', 'Copy the Streeter-Phelps form from the handbook; critical time first, then deficit.'),
],
'water-j': [
 ('MCL versus MCLG', 'MCLG is the health goal (not enforced); MCL is the enforceable limit.'),
 ('Hardness or alkalinity as CaCO3', 'mg/L as CaCO3 = mg/L × (50 / equivalent weight of the ion).'),
 ('Solids tests', 'Total = suspended + dissolved; volatile = burned off at 550 °C.'),
],
'water-k': [
 ('Settling tank sizing', 'Overflow rate = Q / surface area; detention time = volume / Q.'),
 ('Filter loading', 'Loading rate = Q / filter area.'),
 ('Disinfection', 'CT = residual concentration × contact time; chlorine dose = demand + residual.'),
 ('Activated sludge', 'F/M = Q S0 / (V X); SRT = mass in the system / mass wasted per day.'),
],
# ---------------- Structural ----------------
'structural-a': [
 ('Reactions or internal forces of a determinate beam or frame', 'Statics: moments about a support first.'),
 ('Maximum moment for a standard case', 'Handbook beam tables: simple UDL w L²/8; cantilever UDL w L²/2; point P L/4 or P L.'),
 ('Truss member force', 'Method of sections for one member.'),
 ('Influence line or moving load', 'Place the load at the ordinate peak; for a simple beam the maximum moment is at midspan.'),
],
'structural-b': [
 ('Deflection of a standard beam', 'Handbook table: simple UDL 5 w L⁴/(384 E I); cantilever tip load P L³/(3 E I).'),
 ('Two loads', 'Superpose the table cases.'),
 ('Units trap', 'Keep consistent units: kip and in with E in ksi and I in in⁴, or N and mm.'),
],
'structural-c': [
 ('Euler buckling load', 'P = π² E I / (K L)²; use the weak-axis I.'),
 ('Effective length factor', 'Pinned-pinned 1.0, fixed-free 2.0, fixed-pinned 0.7, fixed-fixed 0.5 (theoretical).'),
 ('Slenderness', 'K L / r with r = √(I/A); larger means more likely to buckle.'),
],
'structural-d': [
 ('Is the beam or frame determinate?', 'Count reactions (r) against 3; for frames also count internal releases.'),
 ('Truss determinacy', 'm + r = 2j determinate; more is indeterminate; fewer is unstable.'),
 ('Unstable cases', 'All reactions parallel or all meeting at one point: unstable even if the count looks fine.'),
],
'structural-e': [
 ('Propped cantilever or fixed beam reactions', 'Use the handbook table: propped cantilever with UDL, prop reaction 3 w L/8; fixed-end moments w L²/12.'),
 ('Continuous beam (two equal spans, UDL)', 'Middle support reaction 5 w L/4 (1.25 w L).'),
 ('Superposition by compatibility', 'Remove the redundant, find the deflection there, apply the force that cancels it.'),
],
'structural-f': [
 ('Load combination', 'Write each LRFD combination (1.4D; 1.2D + 1.6L; ...) and take the largest.'),
 ('Tributary area', 'Beam: load × tributary width. Column: half a bay each way × floors.'),
 ('Live load reduction', 'Copy the ASCE 7 formula given or from the handbook; check the minimum.'),
],
'structural-g': [
 ('Tension member capacity', 'Smaller of 0.9 Fy Ag and 0.75 Fu Ae.'),
 ('Beam moment capacity (compact, braced)', 'φ Mn = 0.9 Fy Zx.'),
 ('Column capacity', 'Use the handbook column table or the AISC formulas for K L / r.'),
 ('Bolt shear', 'φ Rn = 0.75 Fnv Ab × number of bolts × shear planes.'),
],
'structural-h': [
 ('Flexural capacity of a singly reinforced beam', 'a = As fy / (0.85 f′c b); φ Mn = 0.9 As fy (d - a/2). Check tension control.'),
 ('Required steel area', 'Assume a, solve As, recheck a; or guess from the answer choices.'),
 ('Shear capacity', 'Vc = 2 λ √f′c b d (psi); φ = 0.75.'),
 ('Column axial capacity', 'Copy the ACI tied or spiral formula from the handbook.'),
],
# ---------------- Geotechnical ----------------
'geotech-a': [
 ('Classify a soil (USCS)', 'Under 50% passing the No. 200: coarse (G or S); then gradation (Cu, Cc) and fines. Over 50%: fine; use the plasticity chart (LL, PI).'),
 ('AASHTO classification', 'Use the handbook table left to right; group index from the formula.'),
 ('Atterberg limits', 'PI = LL - PL; LI = (w - PL)/PI.'),
 ('Uniformity and curvature', 'Cu = D60/D10; Cc = D30²/(D10 D60).'),
],
'geotech-b': [
 ('Any phase relationship', 'Assume Vs = 1 (or V = 1) and fill in the phase diagram, or use S e = w Gs.'),
 ('Unit weights', 'γd = Gs γw / (1 + e); γsat = (Gs + e) γw / (1 + e).'),
 ('Relative density', 'Dr = (emax - e)/(emax - emin).'),
],
'geotech-c': [
 ('Compaction (Proctor)', 'Relative compaction = field γd / max γd. Peak of the curve gives OMC.'),
 ('Permeability test', 'Constant head: k = Q L / (A h t). Falling head: k = (a L / (A t)) ln(h1/h2).'),
 ('SPT or CPT', 'N60 = N × (Em / 60); correct for overburden if asked.'),
 ('Which test measures what', 'Triaxial and direct shear: strength. Consolidometer: settlement. Proctor: compaction.'),
],
'geotech-d': [
 ('Effective stress at a depth', 'σ = Σ γ h (saturated below the water table); u = γw × depth below the water table; σ′ = σ - u.'),
 ('Shortcut below the water table', 'σ′ = Σ γ′ h, with γ′ = γsat - γw.'),
 ('Quick condition or upward flow', 'Critical gradient ic = γ′ / γw (about 1).'),
],
'geotech-e': [
 ('Active force on a wall', 'Ka = tan²(45° - φ/2); Pa = ½ Ka γ H², acting at H/3.'),
 ('Passive', 'Kp = tan²(45° + φ/2) = 1/Ka.'),
 ('Surcharge or water table', 'Uniform surcharge: Ka q over the full height. Water: use γ′ for soil plus full water pressure.'),
 ('Overturning or sliding factor of safety', 'Resisting moments / overturning moments about the toe; sliding: friction on the base / Pa.'),
],
'geotech-f': [
 ('Shear strength at a stress', 'τ = c + σ′ tan φ.'),
 ('Triaxial test result', 'σ1 = σ3 tan²(45° + φ/2) + 2 c tan(45° + φ/2).'),
 ('Unconfined compression of clay', 'Undrained shear strength su = qu / 2.'),
 ('Direct shear: find φ', 'tan φ = τ / σ at failure (for c = 0).'),
],
'geotech-g': [
 ('Bearing capacity of a strip or square footing', 'qult = c Nc + q Nq + ½ γ B Nγ (shape factors for square or round). N from the handbook table at φ.'),
 ('Allowable', 'qall = qult / FS (often 3).'),
 ('Eccentric load', 'e = M / P; e < B/6: qmax,min = (P/B)(1 ± 6e/B).'),
 ('Water table near the footing', 'Use γ′ in the term the water reaches.'),
],
'geotech-h': [
 ('Pile capacity', 'Q = skin friction (f × perimeter × length) + end bearing (q × tip area).'),
 ('Pile group', 'Group capacity = efficiency × n × single pile.'),
 ('Which foundation to use', 'Weak soil near the surface, strong below: deep foundation. Good soil near the surface: spread footing.'),
],
'geotech-i': [
 ('Settlement of normally consolidated clay', 'S = Cc H / (1 + e0) × log(σ′f / σ′0).'),
 ('Overconsolidated', 'Stays below σ′p: use Cr. Crosses σ′p: Cr to σ′p, then Cc.'),
 ('Time to consolidate', 't = Tv Hdr² / cv; Hdr is half the layer if it drains both ways.'),
],
'geotech-j': [
 ('Infinite slope, dry sand', 'FS = tan φ / tan β.'),
 ('Infinite slope with seepage', 'FS ≈ (γ′/γsat) tan φ / tan β, about half the dry value.'),
 ('Circular slip in clay', 'FS = su × arc length × R / (W × arm).'),
],
'geotech-k': [
 ('Name the stabilization method or geosynthetic function', 'Separation, filtration, drainage, reinforcement; lime for plastic clays, cement for granular soils.'),
 ('Compaction equipment', 'Sheepsfoot for clay, smooth drum or vibratory for granular soil.'),
],
# ---------------- Transportation ----------------
'transport-a': [
 ('Horizontal curve geometry', 'T = R tan(Δ/2); L = π R Δ / 180; E and M from the handbook.'),
 ('Superelevation or minimum radius', 'R = V² / (15 (e + f)) with V in mph.'),
 ('Stopping sight distance', 'SSD = 1.47 V t + V² / (30 (a/32.2 ± G)) in ft (use the handbook form).'),
 ('Vertical curve: elevation or high point', 'y = PVC elevation + (g1/100) x + ((g2 - g1)/(200 L)) x², grades in %, x and L in ft from the PVC; high point at x = g1 L / (g1 - g2).'),
 ('Vertical curve length for sight distance', 'Copy the crest or sag formula for S < L or S > L, then check which case holds.'),
],
'transport-b': [
 ('Flexible pavement structural number', 'SN = a1 D1 + a2 D2 m2 + a3 D3 m3.'),
 ('ESALs', 'Sum (trucks × load equivalency factor) over the design life with growth.'),
 ('Layer names and order', 'Surface, base, subbase, subgrade.'),
],
'transport-c': [
 ('Flow, speed, density', 'q = k v. Capacity = vf kj / 4 at k = kj / 2 (Greenshields).'),
 ('Peak hour factor', 'PHF = hourly volume / (4 × peak 15-min volume).'),
 ('Level of service of a freeway', 'Density = flow per lane / speed, then read the LOS table.'),
 ('Space-mean versus time-mean speed', 'Space-mean is the harmonic mean of spot speeds; time-mean is the arithmetic mean.'),
],
'transport-d': [
 ('Cycle length', 'Webster: C = (1.5 L + 5) / (1 - ΣY), L = total lost time, Y = flow ratios.'),
 ('Yellow and all-red intervals', 'Copy the ITE change-interval formula; V in ft/s.'),
 ('Lane group capacity', 'c = s × g / C.'),
 ('Sign or marking meaning', 'MUTCD shapes and colours: regulatory, warning (yellow diamond), guide (green).'),
],
'transport-e': [
 ('Trip generation', 'Trips = rate × units (from the regression or rate given).'),
 ('Trip distribution (gravity model)', 'Tij = Pi × (Aj Fij) / Σ(Aj Fij).'),
 ('Mode choice (logit)', 'P(mode) = e^U / Σ e^U.'),
 ('Crash rate', 'Per million entering vehicles: crashes × 10⁶ / (ADT × 365 × years).'),
],
# ---------------- Surveying ----------------
'surveying-a': [
 ('Azimuth or bearing conversion', 'Sketch the quadrant. NE: same; SE: 180 - az; SW: az - 180; NW: 360 - az.'),
 ('Horizontal distance from a slope distance', 'H = S cos(vertical angle) or √(S² - Δh²).'),
 ('Angle closure of a traverse', 'Interior angles sum to (n - 2) × 180°; distribute the error equally.'),
],
'surveying-b': [
 ('Area from coordinates', 'Cross-multiply (shoelace): Area = ½ |Σ (xi yi+1 - xi+1 yi)|.'),
 ('Irregular boundary with offsets', 'Trapezoidal rule or Simpson\'s rule (odd number of offsets).'),
 ('Unit conversion', '1 acre = 43,560 ft²; 1 ha = 10,000 m².'),
],
'surveying-c': [
 ('Volume between two sections', 'Average end area: L (A1 + A2)/2. Divide ft³ by 27 for yd³.'),
 ('More exact volume', 'Prismoidal: L (A1 + 4 Am + A2)/6.'),
 ('Swell or shrinkage', 'Loose = bank × (1 + swell); compacted = bank × (1 - shrinkage).'),
 ('Mass diagram', 'Rising: cut; falling: fill; a horizontal line gives balanced haul.'),
],
'surveying-d': [
 ('Coordinates of the next point', 'Latitude = L cos(az), departure = L sin(az); add to the previous N and E.'),
 ('Traverse misclosure and precision', 'Misclosure = √(ΣLat² + ΣDep²); precision = 1 : (perimeter / misclosure).'),
 ('Adjusting a traverse (compass rule)', 'Correction to each leg = -(total error) × (leg length / perimeter).'),
],
'surveying-e': [
 ('Elevation from rod readings', 'Elev = BM + ΣBS - ΣFS. Make a BS / HI / FS / Elev table.'),
 ('Curvature and refraction', 'Copy the handbook formula; distance in thousands of feet or km.'),
 ('Trigonometric leveling', 'Δh = S sin(vertical angle) + HI - rod reading.'),
],
# ---------------- Construction ----------------
'construction-a': [
 ('Delivery method or contract type', 'DBB: two contracts, low bid. DB: one contract. CMAR: CM joins during design, guarantees a maximum price.'),
 ('Bonds and insurance', 'Bid bond: will sign. Performance: will finish. Payment: will pay subs and suppliers.'),
 ('Change orders, claims, documents', 'Answer from the plain contract logic: written change before work, follow the order of precedence.'),
],
'construction-b': [
 ('Earthwork quantities and trucks', 'Convert bank to loose with swell; trucks = loose volume / truck capacity.'),
 ('Equipment production', 'Production = capacity × cycles per hour × efficiency.'),
 ('Formwork pressure or crane questions', 'Copy the formula given in the handbook or the question; check units.'),
],
'construction-c': [
 ('Critical path', 'Forward pass (ES, EF) then backward pass (LS, LF); zero float = critical; project length = largest EF.'),
 ('Float of an activity', 'Total float = LS - ES.'),
 ('Earned value', 'SV = EV - PV, CV = EV - AC, SPI = EV/PV, CPI = EV/AC; negative or below 1 is bad.'),
 ('Estimate at completion', 'EAC = BAC / CPI (if the cost trend continues).'),
],
'construction-d': [
 ('Unit cost or crew cost', '(Labor + equipment per hour) / production per hour, plus materials per unit.'),
 ('Quantity take-off', 'Convert units carefully: ft³ / 27 = yd³; add waste if stated.'),
 ('Markups', 'Apply in the order given; overhead on direct cost, profit on cost plus overhead unless stated.'),
],
'construction-e': [
 ('Scale reading', 'Real distance = drawing distance × scale; check whether the drawing is reduced.'),
 ('Slope or grade from a plan or profile', 'Grade = rise / run × 100%; elevation difference between contours × number of intervals.'),
 ('Symbols, sections, views', 'Section cut arrows point the way you look.'),
],
# ---------------- Economics ----------------
'econ-a': [
 ('Find P, F or A', 'Use the factor tables or formulas: F = P(1 + i)^n; P = A[(1 + i)^n - 1]/[i(1 + i)^n]. Name the factor (want/have, i, n).'),
 ('Effective rate from a nominal rate', 'ie = (1 + r/m)^m - 1.'),
 ('Gradient series', 'Use the (P/G) or (A/G) factor; the gradient starts at the end of year 2.'),
 ('Calculator shortcut', 'TVM keys (or one formula) beat interpolating tables.'),
],
'econ-b': [
 ('Break-even quantity', 'Q = fixed cost / (price - variable cost per unit).'),
 ('Depreciation', 'Straight line (C - S)/n; MACRS: cost × table percentage (ignore salvage).'),
 ('Book value', 'Cost minus accumulated depreciation.'),
],
'econ-c': [
 ('Choose between alternatives', 'Same study period, then compare PW, AW or FW at the MARR; for costs pick the lowest.'),
 ('Different lives', 'Annual worth handles it directly: no need to repeat cycles.'),
 ('Benefit-cost ratio', 'B/C = PW of benefits / PW of costs; accept if at least 1; for two options use the incremental ratio.'),
 ('Rate of return', 'IRR: the rate where PW = 0; compare with the MARR.'),
],
'econ-d': [
 ('Expected value', 'Σ (probability × outcome); pick the best expected value.'),
 ('Decision tree', 'Work from the right: average chance nodes, pick the best branch at decision nodes.'),
 ('Sensitivity', 'Change one input and see whether the decision flips.'),
],
# ---------------- Ethics ----------------
'ethics-a': [
 ('Any ethics scenario', 'Pick the answer that protects the public first, is honest, and stays within the engineer\'s competence.'),
 ('Gifts, conflicts, bribes', 'Decline gifts from parties whose work you judge; disclose conflicts and step aside.'),
 ('Pressure from a client or boss', 'Report the danger to the employer, then to the authority if it is not fixed.'),
],
'ethics-b': [
 ('Negligence', 'Needs duty, breach of the standard of care, causation and damages.'),
 ('Standard of care', 'What a reasonably competent engineer would do: not perfection.'),
 ('Insurance', 'Professional liability: design errors. General liability: third-party injury. Workers\' comp: own employees.'),
],
'ethics-c': [
 ('Who may seal', 'Only a licensed PE in responsible charge of the work.'),
 ('Engineer intern', 'May do engineering under a PE; cannot seal or offer services to the public.'),
 ('Licence in another state', 'Comity, when the original licence meets that state\'s requirements.'),
],
'ethics-d': [
 ('Is it a valid contract?', 'Offer, acceptance, consideration, competent parties, lawful purpose: all five.'),
 ('Contract types and risk', 'Cost-plus: owner bears cost risk. Lump sum: contractor does. Unit price: owner takes quantity risk.'),
 ('Breach or change', 'Written amendment before the extra work; damages follow the breach.'),
],
}
