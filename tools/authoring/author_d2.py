from author_dsl import *
U, US = None, 'USCS'
# ---------------- Fluid Mechanics ----------------
N('fluids-a', "Water discharges through a 50 mm diameter orifice under a head of 3 m. The discharge coefficient is 0.60. What is the flow rate? Use g = 9.81 m/s^{2}.", 9.04, 'L/s',
  "Water squirts out of a hole faster when there is more water piled above it. The coefficient accounts for the jet being a bit narrower and slower than the ideal.",
  r"Area = \frac{π(0.05)^{2}}{4} = 0.001963 m^{2}. || Q = C_{d}A\sqrt{2gh} = 0.60(0.001963)\sqrt{2(9.81)(3)} = 0.00904 m^{3}/s = 9.04 L/s.", "0.6*(pi*0.05**2/4)*sqrt(2*g*3)*1000")
M('fluids-b', "Water flows at 1.5 m/s in a 100 mm diameter pipe. Its kinematic viscosity is 1.0 × 10^{-6} m^{2}/s. What is the Reynolds number?", ['1,500', '15,000', '150,000', '1,500,000'], 2,
  "The Reynolds number compares how hard the flow pushes forward with how sticky the fluid is. Big numbers mean churning, turbulent flow.",
  r"Re = \frac{VD}{kinematic viscosity} = \frac{1.5(0.1)}{1.0 × 10^{-6}} = 150,000, which is turbulent.", "1.5*0.1/1e-6", units=U)
N('fluids-b', "A liquid has a dynamic viscosity of 0.0012 Pa·s and a density of 800 kg/m^{3}. What is its kinematic viscosity? Give the answer in units of 10^{-6} m^{2}/s.", 1.5, '× 10^{-6} m^{2}/s',
  "Dynamic viscosity is how sticky a fluid is. Kinematic viscosity is that stickiness compared with how heavy the fluid is.",
  r"Kinematic viscosity = \frac{dynamic viscosity}{density} = \frac{0.0012}{800} = 1.5 × 10^{-6} m^{2}/s.", "0.0012/800*1e6")
M('fluids-c', "A mercury manometer (specific gravity 13.6) connects two water pipes at the same elevation and shows a deflection of 0.20 m. What is the pressure difference between the pipes? Use 9.81 kN/m^{3} for water.", ['1.96 kPa', '2.0 kPa', '24.7 kPa', '26.7 kPa'], 2,
  "The mercury is pushed down on the high-pressure side. Water fills the space the mercury left, so only the extra weight of mercury over water counts.",
  "Pressure difference = (13.6 - 1)(9.81)(0.20) = 24.7 kPa. || Using 13.6 alone gives 26.7 kPa, which ignores the water on the other side.", "(13.6 - 1)*gw*0.20")
N('fluids-c', "A 0.5 m^{3} block with a specific gravity of 0.60 floats in water. What volume of the block is below the water surface?", 0.30, 'm^{3}',
  "A floating object sinks until the water it pushes aside weighs as much as the object.",
  "Weight of block = weight of displaced water, so submerged volume = 0.60(0.5) = 0.30 m^{3}.", "0.6*0.5")
M('fluids-d', "Water flows in a horizontal pipe. At section 1 the velocity is 2 m/s and the pressure is 200 kPa. At section 2 the pipe is narrower and the velocity is 8 m/s. Ignoring losses, what is the pressure at section 2?", ['140 kPa', '170 kPa', '200 kPa', '230 kPa'], 1,
  "When water speeds up it has to pay for the extra speed with pressure. Faster flow means lower pressure.",
  r"Bernoulli on a level pipe: p_{2} = p_{1} - \frac{density(V_{2}^{2} - V_{1}^{2})}{2} = 200,000 - \frac{1,000(64 - 4)}{2} = 170,000 Pa = 170 kPa.", "200 - 1000*(8**2 - 2**2)/2/1000")
N('fluids-d', "A 50 mm diameter water jet moving at 20 m/s strikes a flat plate at right angles. What force does the jet exert on the plate?", 785, 'N',
  "The plate has to stop the water's forward motion. The force equals how much moving water arrives each second times how fast it was going.",
  r"Q = \frac{π(0.05)^{2}}{4}(20) = 0.0393 m^{3}/s. || F = density × Q × V = 1,000(0.0393)(20) = 785 N.", "1000*(pi*0.05**2/4*20)*20")
M('fluids-d', "Water flows at 2 m/s through 100 m of 200 mm diameter pipe with a friction factor of 0.02. What is the head loss? Use g = 9.81 m/s^{2}.", ['0.20 m', '1.02 m', '2.04 m', '4.08 m'], 2,
  "Water rubbing along a pipe wall loses energy. Longer, narrower and faster all make the loss bigger.",
  r"Darcy-Weisbach: h_{f} = f\frac{L}{D}\frac{V^{2}}{2g} = 0.02(\frac{100}{0.2})(\frac{4}{19.62}) = 2.04 m.", "0.02*(100/0.2)*2**2/(2*g)")
# ---------------- Surveying ----------------
M('surveying-a', "A slope distance of 250.00 m is measured at a vertical angle of 12° above horizontal. What is the horizontal distance?", ['51.98 m', '244.54 m', '250.00 m', '255.59 m'], 1,
  "A tape laid up a hill measures more than the distance on the map. The map distance is the flat leg of the triangle.",
  "Horizontal distance = slope distance × cos(vertical angle) = 250.00 cos 12° = 244.54 m.", "250*cos(rad(12))")
M('surveying-a', "What should the interior angles of a closed five-sided traverse add up to?", ['360°', '540°', '720°', '900°'], 1,
  "Any closed shape can be cut into triangles, and every triangle holds 180°.",
  "Sum = (n - 2)(180°) = (5 - 2)(180°) = 540°. || The difference between this and the measured sum is the angular misclosure.", "(5 - 2)*180", units=U)
N('surveying-b', "Two sides of a triangular parcel are 80 m and 60 m long and meet at an angle of 30°. What is the area of the parcel?", 1200, 'm^{2}',
  "A triangle is half of a slanted rectangle. The sine of the angle accounts for the slant.",
  r"Area = \frac{1}{2}ab sin C = \frac{1}{2}(80)(60) sin 30° = 1,200 m^{2}.", "0.5*80*60*sin(rad(30))")
M('surveying-c', "A borrow pit measures 20 m by 30 m in plan. Its average depth of cut is 2.5 m. What volume is excavated?", ['600 m^{3}', '750 m^{3}', '1,500 m^{3}', '3,000 m^{3}'], 2,
  "Volume is the footprint of the pit times how deep it is on average.",
  "V = plan area × average depth = 20(30)(2.5) = 1,500 m^{3}.", "20*30*2.5")
M('surveying-d', "A traverse line is 200.00 m long with an azimuth of 60°. What is its departure (east-west component)?", ['100.0 m', '173.2 m', '200.0 m', '346.4 m'], 1,
  "Every survey line can be split into how far it goes north and how far it goes east. Departure is the east part.",
  "Departure = L sin(azimuth) = 200 sin 60° = 173.2 m east. || The latitude (north part) is 200 cos 60° = 100.0 m.", "200*sin(rad(60))")
N('surveying-d', "Point A has a northing of 1,000.00 m and an easting of 500.00 m. Point B is 100.00 m from A on a bearing of S 30° E. What is the northing of B?", 913.4, 'm',
  "A bearing that starts with S means you are heading south, so the northing goes down.",
  "Change in northing = -100 cos 30° = -86.6 m. || Northing of B = 1,000.00 - 86.6 = 913.4 m. The easting increases by 100 sin 30° = 50.0 m.", "1000 - 100*cos(rad(30))", tol=0.002)
# ---------------- Water Resources and Environmental ----------------
N('water-a', "A watershed with a curve number of 80 receives 4.0 in of rain. Using the NRCS (SCS) method, what is the depth of runoff?", 2.04, 'in',
  "The first part of a storm soaks in or is caught by plants and puddles. Only what is left after that runs off.",
  r"S = \frac{1,000}{CN} - 10 = \frac{1,000}{80} - 10 = 2.5 in. || Q = \frac{(P - 0.2S)^{2}}{P + 0.8S} = \frac{(4.0 - 0.5)^{2}}{4.0 + 2.0} = 2.04 in.", "(4 - 0.2*(1000/80 - 10))**2/(4 + 0.8*(1000/80 - 10))", units=US)
M('water-b', "A rectangular channel carries a flow of 3.0 m^{3}/s per metre of width. What is the critical depth? Use g = 9.81 m/s^{2}.", ['0.31 m', '0.46 m', '0.97 m', '1.21 m'], 2,
  "Critical depth is the depth at which a given flow moves with the least energy. Shallower and it races, deeper and it drifts.",
  r"y_{c} = (\frac{q^{2}}{g})^{1/3} = (\frac{3.0^{2}}{9.81})^{1/3} = 0.97 m.", "(3**2/g)**(1/3)")
M('water-c', "A pump delivers 100 L/s at 1,200 rpm. Using the affinity laws, what flow does it deliver at 1,500 rpm?", ['80 L/s', '125 L/s', '156 L/s', '195 L/s'], 1,
  "Spin a pump faster and it moves more water in direct proportion. The head goes up faster still, with the square of the speed.",
  r"Q_{2} = Q_{1}(\frac{N_{2}}{N_{1}}) = 100(\frac{1,500}{1,200}) = 125 L/s. || Head would rise by the ratio squared, 1.56.", "100*1500/1200")
N('water-d', "A town of 25,000 people uses an average of 400 L per person per day. The maximum-day peaking factor is 1.8. What is the maximum-day demand?", 18000, 'm^{3}/day',
  "Water systems are sized for the thirstiest day, not the average one.",
  "Average demand = 25,000(400 L) = 10,000,000 L/day = 10,000 m^{3}/day. || Maximum day = 1.8(10,000) = 18,000 m^{3}/day.", "25000*400/1000*1.8")
M('water-d', "The water surface in an elevated tank is 40 m above a hydrant. With no flow in the system, what is the pressure at the hydrant? Use 9.81 kN/m^{3}.", ['40 kPa', '196 kPa', '392 kPa', '4,000 kPa'], 2,
  "A water tower works by height alone. Every metre of water above you adds about 9.8 kPa.",
  "p = specific weight × height = 9.81(40) = 392 kPa.", "gw*40")
M('water-e', "What is the probability that a 50-year flood is equalled or exceeded at least once in a 10-year period?", ['0.020', '0.183', '0.200', '0.817'], 1,
  "A 50-year flood has a 2% chance every year. Work out the chance of dodging it ten years in a row, and the rest is the chance of being hit.",
  r"Chance of no exceedance in one year = 1 - \frac{1}{50} = 0.98. || Over 10 years: 0.98^{10} = 0.817. || Chance of at least one = 1 - 0.817 = 0.183.", "1 - (1 - 1/50)**10", units=U)
M('water-e', "What is the annual exceedance probability of a 25-year flood?", ['0.25%', '2.5%', '4%', '25%'], 2,
  "A 25-year flood does not come every 25 years on schedule. It has a 1 in 25 chance of happening in any given year.",
  r"Annual probability = \frac{1}{return period} = \frac{1}{25} = 0.04 = 4%.", "1/25*100", units=U)
N('water-f', "Stormwater flows into a detention basin at 3.0 m^{3}/s and leaves at 1.0 m^{3}/s for 20 minutes. How much water is stored in the basin during that time?", 2400, 'm^{3}',
  "A detention basin is a bathtub with a small drain. It fills by the difference between what comes in and what goes out.",
  "Storage = (inflow - outflow) × time = (3.0 - 1.0)(20 × 60 s) = 2,400 m^{3}.", "(3 - 1)*20*60")
M('water-f', "Development raises a site's runoff coefficient from 0.30 to 0.80. With the same rainfall intensity and area, by what factor does the rational-method peak flow increase?", ['0.38', '1.50', '2.67', '5.00'], 2,
  "Pavement and roofs shed almost all the rain that lands on them, where grass and soil soak much of it up.",
  r"Q = CiA, so with i and A unchanged the peak scales with C. || Factor = \frac{0.80}{0.30} = 2.67.", "0.8/0.3", units=U)
N('water-g', "A 300 mm diameter sewer flows full on a slope of 0.005 with Manning's n = 0.013. What is the flow velocity?", 0.967, 'm/s',
  "A sewer is a channel with a lid. For a pipe flowing full, the hydraulic radius is a quarter of the diameter.",
  r"R = \frac{D}{4} = 0.075 m. || V = \frac{1}{n}R^{2/3}S^{1/2} = \frac{1}{0.013}(0.075)^{2/3}(0.005)^{1/2} = 0.967 m/s.", "(1/0.013)*(0.3/4)**(2/3)*0.005**0.5")
M('water-g', "A sewer serves 12,000 people who each generate 300 L of wastewater per day. With a peaking factor of 3.0, what is the peak flow?", ['41.7 L/s', '125 L/s', '3,600 L/s', '10,800 L/s'], 1,
  "Everyone showers and flushes at about the same time in the morning, so sewers are sized for the rush, not the average.",
  r"Average flow = \frac{12,000(300)}{86,400 s} = 41.7 L/s. || Peak = 3.0(41.7) = 125 L/s.", "12000*300/86400*3")
M('water-h', "Groundwater moves through an aquifer with a hydraulic conductivity of 15 m/day, a hydraulic gradient of 0.004 and a porosity of 0.30. What is the average seepage velocity?", ['0.018 m/day', '0.06 m/day', '0.20 m/day', '0.60 m/day'], 2,
  "Water can only travel through the gaps between grains, not through the grains. Squeezing the flow into the gaps makes the water itself move faster.",
  r"Darcy velocity = Ki = 15(0.004) = 0.06 m/day. || Seepage velocity = \frac{0.06}{0.30} = 0.20 m/day.", "15*0.004/0.30")
M('water-i', "A 5 mL wastewater sample is diluted to 300 mL in a BOD bottle. The dissolved oxygen falls from 8.0 mg/L to 3.5 mg/L in five days. What is the BOD_{5}?", ['4.5 mg/L', '22.5 mg/L', '270 mg/L', '1,350 mg/L'], 2,
  "Bacteria use up oxygen as they eat the waste. The sample was watered down for the test, so scale the oxygen drop back up.",
  r"Dilution fraction P = \frac{5}{300}. || BOD_{5} = \frac{DO_{initial} - DO_{final}}{P} = \frac{8.0 - 3.5}{5/300} = 270 mg/L.", "(8.0 - 3.5)/(5/300)")
N('water-i', "A water sample contains 80 mg/L of calcium and 24 mg/L of magnesium. What is the total hardness, expressed as mg/L of CaCO_{3}? Use equivalent weights of 20 for calcium, 12.2 for magnesium and 50 for CaCO_{3}.", 298, 'mg/L as CaCO_{3}',
  "Hardness adds up the calcium and magnesium. They are converted to a common yardstick first so they can be added fairly.",
  r"Calcium: 80(\frac{50}{20}) = 200 mg/L. Magnesium: 24(\frac{50}{12.2}) = 98 mg/L. || Total hardness = 298 mg/L as CaCO_{3}.", "80*50/20 + 24*50/12.2")
M('water-j', "Two machines each produce a sound level of 80 dB at a receiver. What is the combined sound level when both run?", ['80 dB', '83 dB', '86 dB', '160 dB'], 1,
  "Decibels do not add like ordinary numbers. Doubling the sound energy only adds about 3 dB.",
  r"Combined level = 10 log(10^{8.0} + 10^{8.0}) = 10 log(2 × 10^{8}) = 83 dB.", "10*log10(2*10**(80/10))", units=U)
M('water-j', "Under the U.S. Safe Drinking Water Act, which term is the enforceable limit on a contaminant in public drinking water?", ['Maximum contaminant level goal (MCLG)', 'Maximum contaminant level (MCL)', 'Secondary standard', 'Reference dose'], 1,
  "One number is the ideal with no known health risk. The other is the limit the law actually enforces, set as close to the ideal as treatment allows.",
  "The MCL is the enforceable standard. The MCLG is a non-enforceable health goal. Secondary standards cover taste, odour and appearance and are guidelines.", basis='U.S. Safe Drinking Water Act definitions (40 CFR Part 141)', units=U)
N('water-k', "A clarifier treats 7,200 m^{3}/day and has a surface area of 240 m^{2}. What is its surface overflow rate?", 30, 'm/day',
  "The overflow rate is how fast water rises through the tank. A particle settles out only if it sinks faster than the water rises.",
  r"Overflow rate = \frac{Q}{A} = \frac{7,200}{240} = 30 m/day.", "7200/240")
M('water-k', "A plant treats 10,000 m^{3}/day and applies a chlorine dose of 2 mg/L. How much chlorine is used per day?", ['2 kg', '20 kg', '200 kg', '5,000 kg'], 1,
  "A dose in mg/L is the same as grams per cubic metre. Multiply by how many cubic metres are treated.",
  "2 mg/L = 2 g/m^{3}. || Mass = 2(10,000) = 20,000 g = 20 kg per day.", "2*10000/1000")
# ---------------- Structural Engineering ----------------
N('structural-a', "A simply supported beam spans 6 m. It carries a uniform load of 5 kN/m over the full span and a 10 kN point load 2 m from the left support. What is the left reaction?", 21.7, 'kN',
  "The uniform load is shared equally. The point load is shared unequally, with more going to the nearer support.",
  r"From the uniform load: \frac{5(6)}{2} = 15 kN. From the point load: 10(\frac{4}{6}) = 6.67 kN. || Left reaction = 21.7 kN.", "5*6/2 + 10*4/6")
M('structural-a', "A simply supported beam spans 6 m and carries a 40 kN point load at midspan. What is the maximum bending moment?", ['30 kN·m', '60 kN·m', '120 kN·m', '240 kN·m'], 1,
  "Each support pushes up with half the load. The bending in the middle is that push times its distance from the middle.",
  r"M_{max} = \frac{PL}{4} = \frac{40(6)}{4} = 60 kN·m.", "40*6/4")
M('structural-b', "A cantilever beam 2 m long carries a 5 kN point load at its free end. EI = 10,000 kN·m^{2}. What is the deflection at the free end?", ['0.33 mm', '0.50 mm', '1.33 mm', '4.00 mm'], 2,
  "The tip of a diving board drops more with a heavier diver or a longer board, and less with a stiffer board.",
  r"Deflection = \frac{PL^{3}}{3EI} = \frac{5(2)^{3}}{3(10,000)} = 0.00133 m = 1.33 mm.", "5*2**3/(3*10000)*1000")
M('structural-c', "A column 5 m long is fixed at its base and pinned at its top. Using the theoretical effective length factor K = 0.7, what is its effective length?", ['2.5 m', '3.5 m', '5.0 m', '10.0 m'], 1,
  "Holding the end of a column stops it bowing as freely, so it behaves like a shorter column.",
  "Effective length = KL = 0.7(5) = 3.5 m. || Pinned-pinned is K = 1.0, fixed-fixed is 0.5 and fixed-free is 2.0.", "0.7*5")
M('structural-d', "A beam is fixed at one end and rests on a roller at the other. How is it classified?", ['Unstable', 'Statically determinate', 'Statically indeterminate to the first degree', 'Statically indeterminate to the second degree'], 2,
  "A flat beam gives you three balance equations. Count the support forces. Any extras are more than statics alone can find.",
  "A fixed support gives three reactions and a roller gives one, for four unknowns. || There are three equations of equilibrium, so 4 - 3 = 1 degree of indeterminacy.", "{0: 'determinate', 1: 'first degree', 2: 'second degree'}[(3 + 1) - 3]", units=U)
N('structural-e', "A beam 4 m long is fixed at one end and supported by a roller at the other. It carries a uniform load of 8 kN/m. What is the reaction at the roller?", 12, 'kN',
  "The fixed end is stiffer, so it attracts more than half of the load. The roller end gets the smaller share.",
  r"For a propped cantilever under uniform load, the roller reaction is \frac{3wL}{8} = \frac{3(8)(4)}{8} = 12 kN. || The fixed end carries the other \frac{5wL}{8} = 20 kN.", "3*8*4/8")
M('structural-e', "A beam fixed at both ends spans 6 m and carries a uniform load of 12 kN/m. What is the magnitude of the moment at each support?", ['18 kN·m', '27 kN·m', '36 kN·m', '54 kN·m'], 2,
  "Clamping both ends shares the bending between the supports and the middle, so the middle bends less than it would on simple supports.",
  r"Fixed-end moment = \frac{wL^{2}}{12} = \frac{12(6)^{2}}{12} = 36 kN·m. || The midspan moment is \frac{wL^{2}}{24} = 18 kN·m.", "12*6**2/12")
M('structural-f', "Floor beams are spaced 3 m apart and support a floor load of 4 kPa. What line load does an interior beam carry?", ['1.33 kN/m', '7 kN/m', '12 kN/m', '36 kN/m'], 2,
  "Each beam looks after the strip of floor that is closer to it than to its neighbours.",
  "Tributary width = 3 m (half the spacing on each side). || Line load = 4 kPa × 3 m = 12 kN/m.", "4*3")
N('structural-g', "A steel tension member has a gross area of 2,000 mm^{2} and a yield strength of 345 MPa. Using LRFD with a resistance factor of 0.90, what is its design strength for yielding on the gross section?", 621, 'kN',
  "A tension member is ruined once the whole bar starts to stretch permanently. The design strength is that load, trimmed by a safety factor.",
  "Design strength = 0.90 F_{y}A_{g} = 0.90(345)(2,000) = 621,000 N = 621 kN.", "0.9*345*2000/1000")
M('structural-g', "A compact, fully braced steel beam has a plastic section modulus of 1.2 × 10^{6} mm^{3} and a yield strength of 345 MPa. With a resistance factor of 0.90, what is its design flexural strength?", ['311 kN·m', '373 kN·m', '414 kN·m', '460 kN·m'], 1,
  "A well-braced steel beam can bend until its whole cross-section has yielded. The plastic modulus measures that full capacity.",
  "Design strength = 0.90 F_{y}Z_{x} = 0.90(345)(1.2 × 10^{6}) = 372.6 × 10^{6} N·mm = 373 kN·m. || Without the 0.90 factor the nominal strength is 414 kN·m.", "0.9*345*1.2e6/1e6")
M('structural-g', "A steel column has an effective length of 4 m and a radius of gyration of 50 mm about the axis of buckling. What is its slenderness ratio?", ['8', '40', '80', '200'], 2,
  "Slenderness compares how long a column is with how spread out its cross-section is. Skinny columns buckle sooner.",
  r"Slenderness = \frac{KL}{r} = \frac{4,000}{50} = 80.", "4000/50", units=U)
N('structural-h', "A reinforced concrete beam is 250 mm wide with 1,200 mm^{2} of tension steel. The steel yield strength is 420 MPa and the concrete strength is 30 MPa. What is the depth of the equivalent rectangular stress block?", 79.1, 'mm',
  "The squeezed concrete at the top of the beam has to push exactly as hard as the steel at the bottom pulls. That balance sets how deep the squeezed zone is.",
  r"a = \frac{A_{s}f_{y}}{0.85f'_{c}b} = \frac{1,200(420)}{0.85(30)(250)} = 79.1 mm.", "1200*420/(0.85*30*250)")
M('structural-h', "Using V_{c} = 0.17 × the square root of f'_{c} × b × d (MPa and mm), what shear does the concrete carry in a beam 300 mm wide with an effective depth of 500 mm and a concrete strength of 25 MPa?", ['63.8 kN', '127.5 kN', '255 kN', '750 kN'], 1,
  "Concrete can carry some shear by itself before stirrups are needed. Bigger sections and stronger concrete carry more.",
  r"V_{c} = 0.17\sqrt{25}(300)(500) = 0.17(5)(150,000) = 127,500 N = 127.5 kN.", "0.17*sqrt(25)*300*500/1000")
N('structural-h', "A 400 mm square tied column has 3,200 mm^{2} of longitudinal steel with a yield strength of 420 MPa. The concrete strength is 28 MPa. What is the nominal axial strength at zero eccentricity, P_{0}?", 5076, 'kN',
  "A short concrete column carries load on its concrete and on its steel bars. Add the two strengths together.",
  "P_{0} = 0.85f'_{c}(A_{g} - A_{st}) + f_{y}A_{st} = 0.85(28)(160,000 - 3,200) + 420(3,200) = 3,732,000 + 1,344,000 = 5,076,000 N = 5,076 kN.", "(0.85*28*(400*400 - 3200) + 420*3200)/1000")
# ---------------- Geotechnical Engineering ----------------
M('geotech-a', "A sand has 3% fines, a coefficient of uniformity of 7 and a coefficient of curvature of 1.5. What is its Unified Soil Classification symbol?", ['SP', 'SW', 'SM', 'GW'], 1,
  "A well-graded sand has a good mix of grain sizes, so small grains fill the gaps between big ones.",
  "With less than 5% fines the sand is clean, so it is SW or SP. || A sand is well graded when C_{u} is at least 6 and C_{c} is between 1 and 3. Both hold, so the symbol is SW.", basis='Unified Soil Classification System, ASTM D2487', units=U)
N('geotech-a', "A grain size curve gives D_{60} = 0.84 mm, D_{30} = 0.42 mm and D_{10} = 0.12 mm. What is the coefficient of uniformity?", 7, '',
  "The coefficient of uniformity compares a fairly coarse grain with a fairly fine one from the same soil. A big ratio means a wide spread of sizes.",
  r"C_{u} = \frac{D_{60}}{D_{10}} = \frac{0.84}{0.12} = 7.0.", "0.84/0.12", units=U)
N('geotech-c', "A field density test gives a dry unit weight of 17.1 kN/m^{3}. The maximum dry unit weight from the Proctor test is 18.0 kN/m^{3}. What is the relative compaction?", 95, '%',
  "The Proctor test finds the densest the soil can be packed in the lab. Relative compaction says how close the crew got to that in the field.",
  r"Relative compaction = \frac{17.1}{18.0} × 100 = 95%.", "17.1/18.0*100", units=U)
M('geotech-c', "In a constant-head permeability test, 600 cm^{3} of water passes through a sample in 300 s. The sample is 15 cm long with a cross-section of 40 cm^{2}, and the head difference is 30 cm. What is the coefficient of permeability?", ['0.0025 cm/s', '0.025 cm/s', '0.25 cm/s', '0.40 cm/s'], 1,
  "Permeability is how easily water passes through soil. Measure how much water gets through, how hard it was pushed and how far it had to travel.",
  r"k = \frac{QL}{Aht} = \frac{600(15)}{40(30)(300)} = 0.025 cm/s.", "600*15/(40*30*300)")
N('geotech-e', "A 4 m high wall retains dry sand with a unit weight of 18 kN/m^{3}. The Rankine active coefficient is 0.333. What is the total active force per metre of wall?", 48, 'kN/m',
  "The sideways push from soil grows with depth, so it forms a triangle. The total force is the area of that triangle.",
  r"P_{a} = \frac{1}{2}K_{a}(unit weight)H^{2} = \frac{1}{2}(0.333)(18)(4)^{2} = 48 kN/m, acting one third of the way up the wall.", "0.5*(1/3)*18*4**2")
M('geotech-f', "An unconfined compression test on a clay gives a compressive strength of 120 kPa. What is the undrained shear strength?", ['30 kPa', '60 kPa', '120 kPa', '240 kPa'], 1,
  "Squeezing a clay cylinder until it fails makes it slide along a slanted surface. The shear on that surface is half the squeezing stress.",
  r"s_{u} = \frac{q_{u}}{2} = \frac{120}{2} = 60 kPa.", "120/2")
N('geotech-g', "A strip footing bears 1 m below the surface of a clay with a cohesion of 50 kPa and a unit weight of 18 kN/m^{3}. Using bearing capacity factors N_{c} = 5.7, N_{q} = 1.0 and a zero third factor, what is the ultimate bearing capacity?", 303, 'kPa',
  "The ground under a footing resists being squeezed out sideways. The soil's stickiness and the weight of soil beside the footing both help.",
  "q_{ult} = cN_{c} + (unit weight × depth)N_{q} = 50(5.7) + 18(1)(1.0) = 285 + 18 = 303 kPa.", "50*5.7 + 18*1*1.0")
N('geotech-g', "A square footing must carry a 600 kN column load. The ultimate bearing capacity is 450 kPa and the factor of safety is 3. What footing width is required?", 2.0, 'm',
  "Divide what the soil can take before failing by a safety factor, then make the footing big enough that the pressure stays under that.",
  r"Allowable pressure = \frac{450}{3} = 150 kPa. || Area = \frac{600}{150} = 4.0 m^{2}, so the width is \sqrt{4.0} = 2.0 m.", "sqrt(600/(450/3))")
N('geotech-h', "A 0.3 m square pile is 10 m long. The average skin friction is 40 kPa and the end bearing resistance is 2,000 kPa. What is the ultimate capacity of the pile?", 660, 'kN',
  "A pile holds load two ways: the soil grips its sides, and the soil under its tip pushes back.",
  "Skin friction = 40 × (4 × 0.3 m perimeter) × 10 m = 480 kN. || End bearing = 2,000 × (0.3)^{2} = 180 kN. || Total = 660 kN.", "40*(4*0.3)*10 + 2000*0.3**2")
M('geotech-h', "Which foundation type is a single thick slab that supports all the columns of a building?", ['Spread footing', 'Mat foundation', 'Drilled shaft', 'Strip footing'], 1,
  "When separate footings would be so big that they nearly touch, it is simpler to pour one slab under the whole building.",
  "A mat, or raft, foundation spreads the building load over the whole footprint. || Spread footings carry single columns, strip footings carry walls, and drilled shafts are deep foundations.", basis='Standard foundation type definitions', units=U)
N('geotech-i', "A 4 m thick normally consolidated clay layer has a compression index of 0.30 and an initial void ratio of 1.0. The effective stress at mid-layer rises from 100 kPa to 200 kPa. What is the primary consolidation settlement?", 181, 'mm',
  "Loaded clay slowly squeezes water out, like a wet sponge under a book, and the ground settles as it does.",
  r"S = \frac{C_{c}H}{1 + e_{0}} log(\frac{200}{100}) = \frac{0.30(4,000)}{2.0}(0.301) = 181 mm.", "0.30*4000/(1 + 1.0)*log10(200/100)")
M('geotech-i', "A 4 m thick clay layer drains from both its top and bottom. Its coefficient of consolidation is 2.0 m^{2}/year. Using a time factor of 0.197 for 50% consolidation, how long does 50% consolidation take?", ['0.099 years', '0.394 years', '0.788 years', '1.576 years'], 1,
  "Water has to escape for clay to settle. With drainage at both faces, no drop of water travels more than half the thickness.",
  r"Drainage path H_{dr} = \frac{4}{2} = 2 m. || t = \frac{T_{v}H_{dr}^{2}}{c_{v}} = \frac{0.197(2)^{2}}{2.0} = 0.394 years, about 4.7 months. || Using the full 4 m would give 1.576 years.", "0.197*(4/2)**2/2.0")
M('geotech-j', "A long slope of dry sand stands at 25° to the horizontal. The friction angle of the sand is 35°. What is the factor of safety against sliding?", ['0.67', '1.00', '1.50', '2.14'], 2,
  "Dry sand can stand no steeper than its own friction angle. The gentler the slope compared with that angle, the safer it is.",
  r"For an infinite slope in dry cohesionless soil: FS = \frac{tan 35°}{tan 25°} = \frac{0.700}{0.466} = 1.50.", "tan(rad(35))/tan(rad(25))", units=U)
N('geotech-j', "A circular slip surface in clay has a radius of 15 m and an arc length of 20 m. The undrained shear strength is 30 kPa. The sliding mass weighs 1,500 kN per metre and its centroid is 4 m horizontally from the centre of the circle. What is the factor of safety?", 1.5, '',
  "The weight of the soil tries to rotate the mass downhill. The strength along the slip surface holds it back. Compare the two turning effects.",
  r"Resisting moment = s_{u} × arc length × R = 30(20)(15) = 9,000 kN·m. || Driving moment = W × x = 1,500(4) = 6,000 kN·m. || FS = \frac{9,000}{6,000} = 1.5.", "30*20*15/(1500*4)", units=U)
M('geotech-k', "A geotextile is placed between a soft clay subgrade and a crushed stone base. What is its primary function there?", ['Separation', 'Drainage of the base course', 'Increasing the plasticity of the clay', 'Chemical stabilization'], 0,
  "The fabric is a divider. It stops the stone being pushed down into the mud and the mud pumping up into the stone.",
  "In this position a geotextile mainly provides separation, keeping the two materials from mixing so the base keeps its thickness and strength. || Geosynthetics can also filter, drain and reinforce, depending on type and placement.", basis='Standard geosynthetic functions: separation, filtration, drainage, reinforcement', units=U)
N('geotech-k', "A clay subgrade is to be treated with 5% lime by dry mass. The soil has a dry density of 1,800 kg/m^{3} and 300 m^{3} is to be treated. How much lime is needed?", 27000, 'kg',
  "Lime dries out and firms up sticky clay. The amount needed is a set share of the weight of soil being treated.",
  "Dry mass of soil = 1,800(300) = 540,000 kg. || Lime = 0.05(540,000) = 27,000 kg.", "0.05*1800*300")
# ---------------- Transportation Engineering ----------------
N('transport-b', "A flexible pavement has 4 in of asphalt (layer coefficient 0.44), 8 in of base (0.14) and 10 in of subbase (0.11). Drainage coefficients are 1.0. What is the structural number?", 3.98, '',
  "The structural number adds up the layers, giving more credit per inch to the stronger materials.",
  "SN = a_{1}D_{1} + a_{2}D_{2}m_{2} + a_{3}D_{3}m_{3} = 0.44(4) + 0.14(8)(1.0) + 0.11(10)(1.0) = 1.76 + 1.12 + 1.10 = 3.98.", "0.44*4 + 0.14*8 + 0.11*10", units=US)
M('transport-b', "Using the correlation M_{R} = 1,500 × CBR (psi), what is the resilient modulus of a subgrade with a CBR of 6?", ['900 psi', '4,000 psi', '9,000 psi', '15,000 psi'], 2,
  "CBR is a quick test of how firm the subgrade is. A simple multiplier turns it into the stiffness value that pavement design needs.",
  "M_{R} = 1,500(6) = 9,000 psi.", "1500*6", units=US)
M('transport-b', "A highway lane carries 500 equivalent single axle loads (ESALs) per day with no growth. How many ESALs does it carry over a 20-year design life?", ['0.18 million', '3.65 million', '10 million', '36.5 million'], 1,
  "Pavement wears out from the total number of heavy axle passes over its life, so add up every day for the whole design period.",
  "Total = 500 × 365 × 20 = 3,650,000 = 3.65 million ESALs.", "500*365*20/1e6", units=U)
N('transport-c', "A signalized approach has two lanes, each with a saturation flow rate of 1,900 veh/h. The approach gets 40 s of effective green in a 100 s cycle. What is its capacity?", 1520, 'veh/h',
  "Cars can only leave the stop line while the light is green. Capacity is what the lanes could discharge nonstop, scaled by the share of time they get green.",
  r"Capacity = saturation flow × lanes × \frac{g}{C} = 1,900(2)(\frac{40}{100}) = 1,520 veh/h.", "1900*2*40/100", units=U)
M('transport-c', "A road follows the Greenshields model with a free-flow speed of 60 mph and a jam density of 120 veh/mi. What is its capacity?", ['900 veh/h', '1,800 veh/h', '3,600 veh/h', '7,200 veh/h'], 1,
  "An empty road moves fast but carries few cars. A jammed road is full but nothing moves. The most cars get through halfway between.",
  r"Maximum flow occurs at half the free-flow speed and half the jam density. || q_{max} = \frac{v_{f}k_{j}}{4} = \frac{60(120)}{4} = 1,800 veh/h.", "60*120/4", units=US)
N('transport-d', "A signal approach has a speed of 30 mph (44 ft/s) on level ground. Using a perception-reaction time of 1.0 s and a deceleration rate of 10 ft/s^{2}, what yellow change interval is needed?", 3.2, 's',
  "The yellow has to last long enough for a driver who is too close to stop to keep going and reach the intersection.",
  r"y = t + \frac{v}{2a} = 1.0 + \frac{44}{2(10)} = 3.2 s.", "1.0 + 44/(2*10)", units=US)
M('transport-e', "A subdivision has 250 single-family homes. The trip generation rate is 9.4 trips per dwelling unit per day. How many daily trips does it generate?", ['27', '235', '2,350', '23,500'], 2,
  "Trip generation is a head count of journeys. Multiply the number of homes by how many trips a typical home makes.",
  "Trips = 250 × 9.4 = 2,350 per day.", "250*9.4", units=U)
N('transport-e', "An intersection has 12 crashes in one year. Its entering volume is 20,000 vehicles per day. What is the crash rate per million entering vehicles?", 1.64, 'per MEV',
  "Busy intersections have more crashes simply because more cars pass through. A rate lets you compare a busy one fairly with a quiet one.",
  r"Rate = \frac{crashes × 10^{6}}{ADT × 365} = \frac{12 × 10^{6}}{20,000(365)} = 1.64 crashes per million entering vehicles.", "12*1e6/(20000*365)", units=U)
M('transport-e', "A logit mode choice model gives a utility of -0.5 for auto and -1.5 for bus. What share of travellers choose the bus?", ['0.25', '0.27', '0.33', '0.73'], 1,
  "Each choice gets a score. People mostly pick the better score, but not everyone, and the model turns the scores into shares.",
  r"P(bus) = \frac{e^{-1.5}}{e^{-0.5} + e^{-1.5}} = \frac{0.223}{0.607 + 0.223} = 0.27.", "exp(-1.5)/(exp(-0.5) + exp(-1.5))", units=U)
M('transport-a', "A horizontal curve has a radius of 1,000 ft and a deflection angle of 30°. What is the length of the curve?", ['261.8 ft', '523.6 ft', '1,047 ft', '30,000 ft'], 1,
  "A curve is a slice of a circle. Its length is the radius times the angle it turns through, with the angle in radians.",
  r"L = R × angle in radians = 1,000(30 × \frac{π}{180}) = 523.6 ft.", "1000*rad(30)", units=US)
N('transport-a', "For the same curve (radius 1,000 ft, deflection angle 30°), what is the tangent length from the PC to the PI?", 267.9, 'ft',
  "The two straight roads would meet at a corner, the PI. The tangent length is how far back from that corner the curve begins.",
  r"T = R tan(\frac{30°}{2}) = 1,000 tan 15° = 267.9 ft.", "1000*tan(rad(15))", units=US)
M('transport-a', "A crest vertical curve joins grades of +2% and -3%. The design requires a rate of vertical curvature K of 150. What minimum curve length is needed?", ['30 ft', '150 ft', '750 ft', '3,750 ft'], 2,
  "K is the length of curve needed for each 1% change in grade. A bigger change in grade needs a longer curve to keep the hilltop from hiding the road ahead.",
  "A = |2 - (-3)| = 5%. || L = KA = 150(5) = 750 ft.", "150*abs(2 - -3)", units=US)
# ---------------- Construction Engineering ----------------
N('construction-e', "On a plan drawn at a scale of 1 in = 40 ft, a property line measures 3.25 in. How long is the line on the ground?", 130, 'ft',
  "A scale is a fixed exchange rate between paper and ground.",
  "Ground length = 3.25 in × 40 ft/in = 130 ft.", "3.25*40", units=US)
M('construction-e', "A drawing is at a scale of 1:500. A wall measures 24 mm on the drawing. How long is the wall?", ['1.2 m', '12 m', '20.8 m', '120 m'], 1,
  "At 1:500, everything on the ground is 500 times bigger than on the paper.",
  "Length = 24 mm × 500 = 12,000 mm = 12 m.", "24*500/1000")
M('construction-e', "On a grading plan, what do closely spaced contour lines indicate?", ['Flat ground', 'A steep slope', 'A property boundary', 'A drainage easement'], 1,
  "Each contour line is one step up or down. If the steps are crowded together, you climb a lot in a short distance.",
  "Contours join points of equal elevation at a fixed vertical interval. || The closer they are in plan, the less horizontal distance per interval, so the steeper the slope.", basis='Standard topographic drawing convention', units=U)
M('construction-a', "Under which project delivery method does the owner hold a single contract with one entity for both design and construction?", ['Design-bid-build', 'Design-build', 'Construction manager as agent', 'Multiple prime'], 1,
  "One team, one contract, one point of responsibility for both the drawings and the building.",
  "In design-build the owner contracts with one entity that designs and builds. || In design-bid-build the owner holds separate contracts with a designer and a contractor.", basis='Standard project delivery method definitions', units=U)
M('construction-a', "Which bond guarantees that a contractor will pay its subcontractors and suppliers?", ['Bid bond', 'Performance bond', 'Payment bond', 'Warranty bond'], 2,
  "Each bond is a promise backed by a surety. One covers the bid, one covers finishing the job, and one covers paying the people who helped.",
  "A payment bond protects subcontractors and suppliers. || A bid bond guarantees the bidder will sign the contract, and a performance bond guarantees the work will be completed.", basis='Standard construction surety bond definitions', units=U)
N('construction-b', "A contractor has 6 recordable injuries in a year in which employees worked 400,000 hours. What is the incidence rate per 200,000 hours?", 3.0, '',
  "The rate scales injuries to what 100 full-time workers would have in a year, so big and small firms can be compared.",
  r"Incidence rate = \frac{injuries × 200,000}{hours worked} = \frac{6(200,000)}{400,000} = 3.0.", "6*200000/400000", units=U)
M('construction-b', "A loader takes 4 minutes to fill a truck. Each truck needs 24 minutes for a full cycle including loading. How many trucks keep the loader working without waiting?", ['4', '6', '8', '20'], 1,
  "While one truck is away, the loader should be filling others. Match the fleet so a truck returns just as the loader is free.",
  r"Trucks = \frac{truck cycle time}{loading time} = \frac{24}{4} = 6.", "24/4", units=U)
M('construction-c', "A project has a planned value of $100,000 and an earned value of $90,000 at the status date. What is the schedule variance?", ['-$10,000', '-$5,000', '$5,000', '$10,000'], 0,
  "Schedule variance is the value of work done minus the value of work that should have been done by now. Negative means behind.",
  "SV = EV - PV = 90,000 - 100,000 = -$10,000, so the project is behind schedule.", "90000 - 100000", units=U)
N('construction-c', "A crew places 40 m^{2} of formwork per day. There are 1,200 m^{2} to place and two crews working. How many working days are needed?", 15, 'days',
  "Duration is the amount of work divided by how fast it gets done. Two crews do it twice as fast.",
  r"Duration = \frac{1,200}{2(40)} = 15 days.", "1200/(2*40)", units=U)
N('construction-d', "A job needs 850 m^{3} of excavation at a direct cost of $12 per m^{3}. Overhead and profit add 15%. What is the bid price for this item?", 11730, '$',
  "Start with what the work costs to do, then add the contractor's share for running the business and making a profit.",
  "Direct cost = 850(12) = $10,200. || Bid price = 10,200(1.15) = $11,730.", "850*12*1.15", units=U)
M('construction-d', "A concrete wall is 10 m long and 3 m high. What area of formwork is needed to form both faces?", ['30 m^{2}', '60 m^{2}', '90 m^{2}', '120 m^{2}'], 1,
  "Forms are the mould for wet concrete. A wall needs a mould on both sides.",
  "Area per face = 10(3) = 30 m^{2}. || Both faces = 60 m^{2}.", "2*10*3")
save('d2')
