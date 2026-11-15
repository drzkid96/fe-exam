"""Writes the guide for a reader who finished a civil engineering degree years ago, has kept little of it, and works in
transportation. Nothing is assumed: every lesson opens with the idea from zero, says which lessons it builds on and which
build on it, and every explanation lists the technical terms it uses in plain words. Run after author_rev.py."""
import json, os, re, glob
from author_common import ROOT
from plain_terms import TERMS
B = {
'math': dict(plain="Mathematics on this exam is a toolkit: lines, curves and triangles; slopes and areas from calculus; quantities that have a direction (vectors); and ways to summarise data and chance.",
   core=["A slope is rise divided by run. A derivative is the slope of a curve at one point.", "An integral adds up thin strips, for example to get an area.", "A vector is handled one component at a time.", "Mean and standard deviation describe the centre and the spread of data."],
   links="Statics uses trigonometry and vectors for forces. Beam diagrams and centroids use areas. Surveying is trigonometry. Traffic and hydrology use statistics.", exam="The handbook lists the formulas. The skill tested is choosing one and using the calculator well."),
'ethics': dict(plain="This topic asks what a professional engineer must do when duties pull in different directions, and how licences, contracts and liability work.",
   core=["Public health, safety and welfare come first.", "Work only within your competence, and seal only work done under your direct control.", "Disclose conflicts of interest; refuse gifts that could sway your judgement.", "A contract needs an offer, acceptance, something of value exchanged, and a lawful purpose."],
   links="It stands apart from the technical topics, but every design topic ends in someone sealing the work.", exam="Answer from the NCEES Model Rules printed in the handbook, not from one state's law or a firm's policy."),
'econ': dict(plain="Engineering economics compares amounts of money at different times. A dollar today is worth more than a dollar next year, because it can earn interest in between.",
   core=["Draw a time line with every payment on it.", "Interest factors move money along that line: to the present, to the future, or into equal yearly amounts.", "Compare options only after putting them on the same basis."],
   links="Construction uses it for estimates and schedules of payment; transportation and water projects use benefit-cost ratios to justify funding.", exam="The handbook tabulates the factors. Most errors come from putting a payment at the wrong point on the time line."),
'statics': dict(plain="Statics is the study of things that do not move. If an object stays still, every push on it is cancelled by another, and every turning effect is cancelled too. From that one fact you can find the unknown forces holding it up.",
   core=["A force has a size and a direction; split it into a horizontal and a vertical part.", "A moment is a force's turning effect: force times perpendicular distance.", "Draw the object alone with every force on it (a free-body diagram), then write: sum of horizontal forces = 0, sum of vertical forces = 0, sum of moments = 0.", "Shape properties, the centroid and the moment of inertia, are found by adding up simple pieces."],
   links="Everything structural starts here: mechanics of materials turns these forces into stresses, structural analysis applies them to beams and frames, geotechnics uses them for walls and slopes, and fluids uses them for water pressure on surfaces.", exam="Finding support reactions is the first step of a large share of exam questions, so it is the first skill to rebuild."),
'dynamics': dict(plain="Dynamics is the study of things that move and speed up or slow down. A net force makes a mass accelerate; without one, it keeps its velocity.",
   core=["Position, velocity and acceleration are linked: velocity is how fast position changes, acceleration is how fast velocity changes.", "Force = mass × acceleration, written along one direction at a time.", "Energy and momentum give shortcuts when forces act over a distance or over a time."],
   links="It rests on statics (free-body diagrams) and calculus. Stopping distance and banking of curves in transportation are dynamics problems.", exam="Check whether mass is given in kilograms or weight in newtons or pounds before substituting."),
'mechmat': dict(plain="Mechanics of materials asks what happens inside a member that carries load: how hard the material is being pulled, squeezed or sheared (stress), and how much it stretches or bends (strain and deflection).",
   core=["Stress is force divided by area. Strain is change in length divided by length.", "For most materials stress = stiffness × strain, until yielding.", "A beam carries load by bending: the top squeezes and the bottom stretches, or the reverse.", "Shear and moment diagrams show the internal forces along a beam."],
   links="It needs statics to get the internal forces. Structural design (steel and concrete) and the strength of soils in geotechnics build on it.", exam="Work in newtons and millimetres so stresses come out in megapascals, or in kips and inches for ksi."),
'materials': dict(plain="This topic covers what concrete, asphalt, steel, aggregate and wood are made of, how their quality is tested, and how they behave under load.",
   core=["Concrete is cement, water and aggregate; less water for the same cement means stronger concrete.", "Asphalt mix is aggregate glued with asphalt binder, with a little air left in it.", "A stress-strain curve from a tension test gives stiffness, yield strength, ultimate strength and ductility."],
   links="Structural design uses these strengths; pavement design in transportation uses the mix properties; geotechnics uses the same density and moisture ideas for soil.", exam="Many questions only ask which test measures which property."),
'fluids': dict(plain="Fluid mechanics describes water and other fluids at rest and in motion. At rest, pressure grows with depth. In motion, a fluid trades pressure, speed and height against each other, and loses some energy to friction.",
   core=["Pressure = unit weight × depth.", "Flow rate = velocity × area, and it is the same at every section of a full pipe.", "The energy equation tracks pressure, speed and elevation, minus losses, along the flow.", "A fluid that changes speed or direction pushes on whatever turns it."],
   links="Water resources applies it to pipes, pumps, channels and drains. Geotechnics uses the pressure ideas for groundwater. Statics supplies the force and centroid methods.", exam="Fluid mechanics has its own handbook chapter; open-channel formulas also appear in the civil chapter."),
'surveying': dict(plain="Surveying measures where things are: distances, directions, elevations, areas and volumes of earth.",
   core=["A direction is an angle from north.", "A line can be split into a north-south part and an east-west part.", "Elevations are carried from a known point by reading a rod through a level.", "Earthwork volume is cross-section area times distance."],
   links="It is applied trigonometry. Road geometry in transportation and quantities in construction use its results.", exam="The exam expects the hand method: set out a small table and fill it in."),
'water': dict(plain="Water resources covers rain becoming runoff, water moving through channels, pipes, pumps and soil, and how water is cleaned before and after use.",
   core=["Runoff depends on how much rain falls, on what surface, over what area.", "Open channels are sized by how area, wall roughness and slope set the velocity.", "Pumps add energy; friction removes it.", "Treatment is a chain of steps: settle, filter, disinfect; or use microorganisms to consume waste."],
   links="Hydraulics is fluid mechanics applied. Groundwater links to geotechnics. Water chemistry stands largely on its own.", exam="The handbook splits this between the civil chapter (hydrology, hydraulics) and the environmental chapter (treatment, chemistry)."),
'structural': dict(plain="Structural engineering works out the forces that loads cause in beams, columns, trusses and frames, and then checks that steel or concrete members are strong and stiff enough.",
   core=["Loads follow a path: floor to beam to column to foundation.", "Analysis finds internal forces: axial force, shear and bending moment.", "Design compares a factored load effect with a reduced strength.", "Slender columns fail by buckling before the material is crushed."],
   links="It applies statics (reactions, trusses) and mechanics of materials (stress, deflection, buckling), and uses material strengths. Foundations hand the loads to geotechnics.", exam="Design questions follow the steel and concrete code extracts printed in the handbook."),
'geotech': dict(plain="Geotechnical engineering treats soil as a building material. Soil is grains with water and air in the gaps, and its strength comes from the grains pressing and rubbing on each other.",
   core=["Describe a soil by how much of it is solid, water and air.", "Water in the gaps carries part of the load; only the rest (effective stress) gives the soil strength.", "Clay squeezes slowly under load, which causes settlement.", "Strength is friction plus cohesion; it governs walls, footings and slopes."],
   links="It uses water pressure from fluids, stress and Mohr's circle from mechanics of materials, and force balance from statics. Pavement subgrades link it to transportation.", exam="Draw the three-part soil diagram or the soil profile every time."),
'transport': dict(plain="Transportation engineering covers the geometry of roads, how traffic flows and is controlled, pavement thickness, and forecasting travel.",
   core=["Road geometry follows from how far a driver needs to see and how fast a vehicle can turn.", "Traffic flow links volume, speed and density.", "Signals share time between conflicting movements.", "Pavement thickness depends on truck loads and the soil beneath."],
   links="Sight distance and curves come from dynamics; alignment geometry from mathematics and surveying; pavement from materials and geotechnics; traffic data from statistics.", exam="Use the handbook's equations and constants, which follow national references, even where daily practice uses a state manual or a newer edition."),
'construction': dict(plain="Construction engineering covers how a project is bought, scheduled, measured, priced and built safely.",
   core=["An estimate is quantity × unit cost, plus overhead and profit.", "A schedule is a network of activities; the longest chain sets the duration.", "Earned value compares work done with money spent and time used."],
   links="Quantities come from surveying and drawings; costs over time use engineering economics; contracts link to ethics and professional practice.", exam="Scheduling and earned value are quick once the definitions are fixed in memory."),
}
PRIMER = {
 'math-a': "A point on a plane is a pair of numbers (x, y). A straight line is described by its slope, how much it rises for each unit it runs, and where it crosses the y-axis. Circles and parabolas have standard equations too. Trigonometry relates the sides and angles of a triangle: sine, cosine and tangent are ratios of sides.",
 'math-b': "Calculus deals with change. The derivative of a function is its slope at each point: how fast the result changes when the input changes. Where the slope is zero the function is at a peak or a valley. The integral does the reverse: it adds up thin strips to give a total, such as the area under a curve.",
 'math-c': "A vector is anything with both a size and a direction, such as a force or a velocity. It is written as components along x, y and z, and vectors are added component by component. Two kinds of multiplication exist: the dot product gives a number and tells how much two vectors point the same way; the cross product gives a vector at right angles to both.",
 'math-d': "Statistics describes a set of numbers. The mean is the average. The standard deviation says how far values typically lie from the mean. Probability is a number from 0 to 1 for how likely an outcome is. A distribution, such as the bell-shaped normal curve, describes how likely each value is.",
 'ethics-a': "A code of ethics is a written list of duties. For engineers the first duty is to the public's safety, then to clients and employers, then to the profession. Questions describe a situation and ask which action the rules require.",
 'ethics-b': "Liability means being legally answerable for harm. An engineer is expected to work as carefully as a competent peer would. Falling short of that is negligence. Insurance and contract terms decide who pays.",
 'ethics-c': "A licence is the state's permission to practise engineering. It is earned by education, exams (the FE, then the PE) and experience, and it is kept by renewal. A seal on a drawing means a licensed engineer takes responsibility for it.",
 'ethics-d': "A contract is an agreement the law will enforce. It needs an offer, an acceptance, something of value given by each side, parties able to agree, and a lawful purpose. Construction contracts differ mainly in who carries the risk of cost.",
 'econ-a': "Money now and money later are not equal, because money now can earn interest. To compare them, move every amount to the same moment using interest factors. P is an amount now, F an amount in the future, A an equal amount every period.",
 'econ-b': "Costs are sorted by how they behave. Fixed costs stay the same whatever the output; variable costs grow with each unit. Direct costs belong to one job; indirect costs (overhead) are shared. Depreciation spreads an asset's cost over its life.",
 'econ-c': "An analysis decides between options. Break-even finds the quantity at which two options cost the same. Benefit-cost divides the value of benefits by the cost. Life-cycle cost adds everything spent over the whole life, moved to one point in time.",
 'econ-d': "When outcomes are uncertain, weight each one by its probability and add them up. The result, the expected value, is the average outcome if the choice were repeated many times.",
 'statics-a': "A force is a push or a pull with a size and a direction. Any force can be replaced by two parts at right angles: a horizontal component and a vertical component, found with sine and cosine. To combine several forces, add their horizontal parts, add their vertical parts, and the two totals give the single resultant force.",
 'statics-b': "A force also tries to turn an object. That turning effect is its moment: the force times the perpendicular distance from the force's line to the point of interest. Any set of forces can be replaced by one force plus one moment that have the same overall effect.",
 'statics-c': "An object at rest is in equilibrium: the forces on it add to zero in every direction, and so do their moments. Draw the object by itself with every load and every support force (a free-body diagram), write those balance equations, and solve them for the unknown support forces, called reactions.",
 'statics-d': "A truss is a frame of straight bars joined at their ends, loaded only at the joints, so each bar is purely pulled (tension) or pushed (compression). Find a bar's force by isolating one joint, or by cutting through the truss and balancing one side.",
 'statics-e': "The centroid of a shape is its balance point. For a shape made of simple pieces, multiply each piece's area by the distance to its own centre, add those up, and divide by the total area.",
 'statics-f': "The moment of inertia of an area measures how far its material lies from an axis. Material far from the axis counts much more, by distance squared. It decides how stiff and strong a beam's cross-section is in bending. For built-up shapes, add the pieces, shifting each to the common axis.",
 'statics-g': "Friction is the force that resists sliding between two surfaces. It can grow only up to a limit: the coefficient of friction times the normal force pressing the surfaces together. Below the limit the object stays put; at the limit it is about to slide.",
 'dynamics-a': "Kinematics describes motion without asking what causes it. Velocity is the rate of change of position; acceleration is the rate of change of velocity. With constant acceleration a few standard equations link distance, speed and time.",
 'dynamics-b': "A spinning object resists changes to its spin. The mass moment of inertia measures that resistance: it grows with the mass and with the square of its distance from the axis.",
 'dynamics-c': "Newton's second law says a net force makes a mass accelerate: force = mass × acceleration. Draw the free-body diagram, add the forces in the direction of motion, and set the total equal to mass times acceleration. For rotation, net moment = mass moment of inertia × angular acceleration.",
 'dynamics-d': "Work is force times the distance moved along it. Doing work on an object changes its kinetic energy, the energy of motion. Raising it stores potential energy. Power is how fast work is done. Tracking energy often avoids having to find acceleration.",
 'mechmat-a': "Inside a loaded beam there are two internal effects at every section: a shear force, which tries to slide one side past the other, and a bending moment, which bends the beam. A shear diagram and a moment diagram plot these along the beam, starting from the support reactions.",
 'mechmat-b': "Stress is how hard the material is working: force divided by the area that carries it. Pulling gives tension, pushing gives compression, sliding gives shear. Strain is how much the material deforms: change in length divided by original length. Bending and twisting give stresses that are largest at the outer surface.",
 'mechmat-c': "Members change shape under load. A bar under tension gets longer, a beam sags, a shaft twists and a heated bar expands. Each has a formula with the load on top and a stiffness underneath: a stiffer material or a bigger section deforms less.",
 'mechmat-d': "The stress at a point depends on the direction you look in. Turning an imaginary cut changes how much is normal stress and how much is shear. Mohr's circle is a picture that gives the stresses on every such cut, including the largest ones, the principal stresses.",
 'materials-a': "A mix design is a recipe. For concrete it sets the cement, water, sand and stone for one cubic metre; the ratio of water to cement controls strength. For asphalt it sets the binder content and the small amount of air left after compaction.",
 'materials-b': "Materials are accepted on the basis of standard tests. Each test measures one property: a cylinder break gives concrete strength, a slump test gives workability, a tension test gives a metal's strength and ductility, a sieve analysis gives the range of particle sizes.",
 'materials-c': "Mechanical properties describe how a material responds to load: how stiff it is, the stress at which it yields, the stress at which it breaks, and how much it stretches first. They are read from a stress-strain curve.",
 'fluids-a': "Flow is measured by making the fluid do something that can be read. A narrowing speeds the flow up and lowers its pressure; a weir makes water spill over at a depth that depends on the flow. Each device has a formula that turns the reading into a flow rate.",
 'fluids-b': "Fluid properties say how heavy and how thick a fluid is. Density is mass per volume; specific weight is weight per volume; specific gravity compares the density with water's. Viscosity measures resistance to flowing.",
 'fluids-c': "In a fluid at rest, pressure depends only on depth: unit weight times depth. That pressure pushes at right angles on every surface it touches. An object in a fluid is pushed up by a force equal to the weight of the fluid it displaces.",
 'fluids-d': "Moving fluid carries energy in three forms: pressure, speed and height. Along a pipe or stream their total stays the same except for what friction takes away. Flow rate, velocity times area, stays constant, so a narrower section means faster flow.",
 'surveying-a': "Survey measurements are distances and angles. A direction is given as an azimuth (an angle clockwise from north) or a bearing (an angle from north or south toward east or west). Sloping distances are converted to horizontal ones with trigonometry.",
 'surveying-b': "The area of a parcel can be found from the coordinates of its corners, from its sides and angles, or, for a curved edge, by adding up strips measured at regular spacing.",
 'surveying-c': "Earthwork is measured from cross-sections drawn at intervals along a route. The volume between two sections is roughly their average area times the distance between them. Soil also changes volume when it is dug up and when it is compacted.",
 'surveying-d': "A coordinate system gives every point a northing and an easting. Moving along a line changes them by the line's north-south part (latitude) and east-west part (departure), found from its length and direction.",
 'surveying-e': "Levelling finds elevations. A level gives a horizontal line of sight; reading a rod on a known point and then on a new point gives the difference in height. A grade is the rise or fall per hundred units of distance.",
 'water-a': "Hydrology follows rain. Some soaks in, some evaporates and the rest runs off. Peak runoff from a small area is estimated from the rain intensity, the area, and a coefficient for how much the surface sheds.",
 'water-b': "Water in a channel or a part-full pipe flows downhill under gravity. Its speed depends on the slope, the roughness of the walls and the shape of the flow section. Manning's equation ties these together.",
 'water-c': "A pump adds energy to water so it can rise or overcome friction. The energy added per unit weight is the pump head, in metres or feet. Power is flow times head times the unit weight of water, divided by efficiency.",
 'water-d': "A distribution system delivers water under pressure through a network of pipes. Pressure falls with elevation and with friction along the pipes, and the system must meet the peak demand.",
 'water-e': "Flood control stores or passes high flows safely. A flood's size is described by how often it is expected: a 100-year flood has a 1 in 100 chance in any year. Dams must also resist the push of the water behind them.",
 'water-f': "Paving land makes more rain run off, faster. Stormwater management holds runoff back in basins and releases it slowly, and treats the first, dirtiest part of it.",
 'water-g': "Collection systems are pipes that carry wastewater or stormwater by gravity. They are laid on a slope steep enough to keep solids moving and sized for the peak flow.",
 'water-h': "Groundwater moves slowly through the gaps in soil and rock. The flow is proportional to how easily the ground lets water through and to the slope of the water table. Pumping a well lowers the water level around it.",
 'water-i': "Water quality is described by what is dissolved or suspended in the water, in milligrams per litre. Organic pollution is measured by the oxygen that microorganisms need to break it down.",
 'water-j': "Standards set the limits that drinking water, discharges, air and noise must meet, and standard tests measure against them.",
 'water-k': "Treatment removes what should not be in water. Drinking water is settled, filtered and disinfected. Wastewater is settled and then fed to microorganisms that consume the organic matter.",
 'structural-a': "A structure is determinate when balance alone gives every support force. From the reactions, cut the member at any point to find the internal axial force, shear and bending moment there.",
 'structural-b': "Deflection is how far a member moves under load. It grows with load and span and shrinks with material stiffness and section size. The handbook tabulates formulas for common beams.",
 'structural-c': "A slender column can bow sideways and fail well before the material is crushed. The load at which this happens depends on the column's stiffness and on its length between points held in place.",
 'structural-d': "A structure must have enough supports and members to stay put, and it is determinate only if it has no more than the balance equations can solve. Counting unknowns against equations gives the answer.",
 'structural-e': "An indeterminate structure has extra supports. Balance alone cannot solve it, so the way it deforms is used as an additional condition. The handbook gives results for the common cases.",
 'structural-f': "Loads come from the structure's own weight, its use, wind, snow and earthquakes. Codes combine them with factors to give a safe design load, and each member carries the load from the area that drains to it.",
 'structural-g': "Steel members are checked by comparing the factored load effect with a design strength: the member's calculated strength reduced by a safety factor. Tension, bending, shear and compression each have their own formula.",
 'structural-h': "Concrete is strong when squeezed and weak when pulled, so steel bars are cast in to carry tension. A reinforced beam's strength comes from the steel pulling and the concrete pushing, a distance apart.",
 'geotech-a': "Soils are named by their grain sizes and by how they behave when wet. Gravels and sands are coarse; silts and clays are fine. The water contents at which a clay changes behaviour are the Atterberg limits.",
 'geotech-b': "A lump of soil is three things: solid grains, water and air. Phase relationships are ratios between their volumes and masses, such as void ratio, water content and unit weight. Sketching the three parts as stacked blocks makes them easy to find.",
 'geotech-c': "Laboratory and field tests turn a soil sample into numbers for design: how dense it can be compacted, how fast water passes through it, and how strong it is.",
 'geotech-d': "Below the water table, water in the gaps between grains carries part of the weight above. Only the remainder, the effective stress, presses the grains together, and only that gives the soil strength.",
 'geotech-e': "Soil pushes sideways on a wall that holds it back. The push grows with depth and depends on the soil's friction angle and on whether the wall can move away from the soil or is pushed into it.",
 'geotech-f': "Soil fails by sliding along a surface. Its resistance to sliding has two parts: friction, which grows with the pressure on the surface, and cohesion, which does not.",
 'geotech-g': "A footing spreads a load over the ground. If the pressure is too high the soil beneath shears and the footing sinks or tilts. Bearing capacity is that limiting pressure.",
 'geotech-h': "Foundations pass structural loads to the ground. Shallow footings bear near the surface; deep foundations such as piles carry load down to stronger soil by friction along their length and bearing at their tip.",
 'geotech-i': "A loaded clay settles slowly as water is squeezed out of it. The amount depends on how compressible the clay is and how much the stress increases; the time depends on how far the water must travel to escape.",
 'geotech-j': "A slope fails when the weight trying to slide it exceeds the soil's shear strength along the slip surface. The ratio of resistance to driving force is the factor of safety.",
 'geotech-k': "Weak ground can be improved by compacting it, mixing in lime or cement, draining it, or reinforcing it with fabric or grids.",
 'transport-a': "Road geometry is set by what drivers and vehicles can do: how far ahead a driver must see to stop, how sharply a vehicle can turn at speed, and how grades change smoothly through vertical curves.",
 'transport-b': "A pavement spreads wheel loads so the soil beneath is not overstressed. Its thickness depends on the number and weight of truck axles and on the strength of the soil.",
 'transport-c': "Traffic on a road is described by flow (vehicles per hour), speed and density (vehicles per mile). Flow = speed × density. Capacity is the most flow a road or signal approach can carry.",
 'transport-d': "Signs, markings and signals tell road users what to do. A national manual standardises them. Signal timing gives each movement enough green and safe clearance between movements.",
 'transport-e': "Planning estimates how many trips people will make, where they go, by what mode and on what route. Safety analysis measures crashes relative to traffic.",
 'construction-a': "Project administration covers who is responsible for what: the documents that make up a contract, how the builder is chosen, and how payments and changes are handled.",
 'construction-b': "Construction operations are the work on site: how much earth a machine moves in an hour, how crews are organised, and how workers are kept safe.",
 'construction-c': "Project control keeps a job on time and on budget. A schedule orders the activities; earned value compares the work actually done with the plan and with the money spent.",
 'construction-d': "An estimate is a list of quantities, each multiplied by a unit cost, with allowances for waste, overhead and profit.",
 'construction-e': "Engineering drawings describe a project to scale. Plans look down, profiles look from the side along the route, and sections cut across it. Reading them means converting measured lengths with the scale and reading levels from contours and grades.",
}
NEEDS = {'math-b': ['math-a'], 'math-c': ['math-a'], 'statics-a': ['math-a', 'math-c'], 'statics-b': ['statics-a'], 'statics-c': ['statics-b'], 'statics-d': ['statics-c'], 'statics-e': ['math-b'], 'statics-f': ['statics-e'], 'statics-g': ['statics-c'],
 'dynamics-a': ['math-b'], 'dynamics-b': ['statics-f'], 'dynamics-c': ['statics-c', 'dynamics-a'], 'dynamics-d': ['dynamics-c'], 'mechmat-a': ['statics-c'], 'mechmat-b': ['mechmat-a', 'statics-f'], 'mechmat-c': ['mechmat-b'], 'mechmat-d': ['mechmat-b'],
 'materials-b': ['mechmat-b'], 'materials-c': ['mechmat-b'], 'fluids-c': ['fluids-b', 'statics-e'], 'fluids-d': ['fluids-c'], 'fluids-a': ['fluids-d'], 'surveying-a': ['math-a'], 'surveying-b': ['surveying-a'], 'surveying-c': ['surveying-b'], 'surveying-d': ['surveying-a'],
 'water-b': ['fluids-d'], 'water-c': ['fluids-d'], 'water-d': ['fluids-d', 'water-c'], 'water-e': ['water-a', 'fluids-c'], 'water-f': ['water-a'], 'water-g': ['water-b'], 'water-h': ['fluids-b'], 'water-j': ['water-i'], 'water-k': ['water-i'],
 'structural-a': ['statics-c', 'mechmat-a'], 'structural-b': ['mechmat-c'], 'structural-c': ['mechmat-b', 'statics-f'], 'structural-d': ['statics-d'], 'structural-e': ['structural-a', 'structural-b'], 'structural-f': ['structural-a'], 'structural-g': ['mechmat-b', 'structural-f'], 'structural-h': ['mechmat-b', 'materials-c', 'structural-f'],
 'geotech-b': ['geotech-a'], 'geotech-c': ['geotech-b'], 'geotech-d': ['geotech-b', 'fluids-c'], 'geotech-e': ['geotech-d', 'geotech-f'], 'geotech-f': ['geotech-d', 'mechmat-d'], 'geotech-g': ['geotech-f'], 'geotech-h': ['geotech-g'], 'geotech-i': ['geotech-d'], 'geotech-j': ['geotech-f', 'statics-g'], 'geotech-k': ['geotech-c'],
 'transport-a': ['math-a', 'dynamics-a'], 'transport-b': ['geotech-a', 'materials-a'], 'transport-c': ['math-d'], 'transport-d': ['dynamics-a'], 'transport-e': ['math-d'], 'construction-a': ['ethics-d'], 'construction-e': ['surveying-e'], 'econ-b': ['econ-a'], 'econ-c': ['econ-a'], 'econ-d': ['math-d']}
WORK = {'statics-b': "A signal mast arm carries its signal heads at a distance from the pole, so the pole base feels both their weight and a moment.", 'statics-g': "Tyre grip on the road is this same friction model; it sets stopping distance and how fast a curve can be taken.",
 'dynamics-a': "Stopping sight distance is this topic applied: distance covered while reacting, plus distance covered while braking.", 'dynamics-c': "The curve design formula for superelevation and side friction is Newton's second law for a vehicle turning.",
 'fluids-d': "Wind pushing on a sign panel is a drag force: fluid speed squared, times area, times a coefficient.", 'water-a': "Street drainage design starts here: runoff coefficient, rain intensity and drainage area.", 'water-b': "Gutters and roadside ditches are open channels.",
 'geotech-c': "Relative compaction against a laboratory maximum is the acceptance test for subgrade and trench backfill.", 'geotech-e': "A retaining wall beside a road carries the soil's push plus extra from traffic above.", 'surveying-c': "Cut and fill quantities on a road project come from end areas at each cross-section.",
 'construction-d': "An engineer's estimate uses the same quantity times unit price logic.", 'transport-a': "Answer with the handbook's values for reaction time, deceleration and friction, even where an agency manual differs.", 'transport-d': "The exam cites the national manual; where a state supplement differs, the national one is the answer."}
def find_terms(text, topic, cap):
    low = text.lower(); hits = []
    for t, (d, topics) in TERMS.items():
        if topics and topic not in topics: continue
        m = re.search(r'(?<![a-z])' + re.escape(t) + r"(?:s|es)?(?![a-z])", low)
        if m: hits.append((m.start(), t, d))
    return [[t, d] for _, t, d in sorted(hits)[:cap]]
def main():
    names = {}; used = {}
    exam = json.load(open(os.path.join(ROOT, 'exam.json')))
    for t in exam['topics']:
        for u in t['subtopics']: names[u['id']] = [t['id'], t['name'] + ': ' + re.sub(r' \(.*$', '', u['name'])]
    for k, v in NEEDS.items():
        for x in v: used.setdefault(x, []).append(k)
    link = lambda ids: [[i, names[i][0], names[i][1]] for i in ids if i in names]
    nb = npr = nq = 0
    for f in sorted(glob.glob(os.path.join(ROOT, 'guide', '*.json'))):
        g = json.load(open(f))
        for s in g['sections']:
            sub = s.get('subtopic'); s.pop('bridge', None); s.pop('work', None)
            if not sub:
                if g['topic'] in B: s['bridge'] = B[g['topic']]; nb += 1
                continue
            if sub in PRIMER: s['primer'] = PRIMER[sub]; npr += 1
            s['needs'] = link(NEEDS.get(sub, [])); s['leads'] = link(used.get(sub, [])[:5])
            if sub in WORK: s['work'] = WORK[sub]
            txt = ' '.join([s.get('primer') or '', s.get('body') or '', s.get('deep') or ''] + [x['text'] for x in s.get('ideas', [])]); s['terms'] = find_terms(txt, g['topic'], 14)
        json.dump(g, open(f, 'w'), indent=1, ensure_ascii=False); open(f, 'a').write('\n')
    for f in sorted(glob.glob(os.path.join(ROOT, 'questions', '*.json'))):
        qs = json.load(open(f))
        for q in qs:
            t = find_terms((q.get('stem') or '') + ' ' + (q.get('eli5') or '') + ' ' + (q.get('solution') or ''), q['topic'], 6)
            if t: q['terms'] = t; nq += 1
            else: q.pop('terms', None)
            q['needs'] = link(NEEDS.get(q['subtopic'], []))
        json.dump(qs, open(f, 'w'), indent=1, ensure_ascii=False); open(f, 'a').write('\n')
    print('topic openers:', nb, '| lesson primers:', npr, '| questions with terms in plain words:', nq)
if __name__ == '__main__': main()
