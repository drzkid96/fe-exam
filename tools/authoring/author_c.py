from author_common import *
HBNAME = 'NCEES handbook 10.0.1'
L1, L2, L3 = 'Lindeburg review manual, file 1 of 3', 'Lindeburg review manual, file 2 of 3', 'Lindeburg review manual, file 3 of 3'
def sec(topic, body, pitfalls, read):
    with open(os.path.join(ROOT, 'guide', topic + '.json'), 'w') as f:
        json.dump({'topic': topic, 'sections': [{'id': topic + '-overview', 'subtopic': None, 'title': 'Start here', 'body': body, 'formulas': [], 'pitfalls': pitfalls, 'read': [{'source': a, 'where': b} for a, b in read], 'updated': '2026-11-13'}]}, f, indent=1, ensure_ascii=False); f.write('\n')
def H(section): return (HBNAME, section + ', pages ' + HBP[section])

sec('math', 'This topic is the toolkit the rest of the exam leans on: lines and curves, slopes and areas, arrows with direction, and making sense of scattered data.\n\nMost questions are one or two steps. The skill being tested is picking the right tool quickly, then doing clean arithmetic on the calculator.',
    ['Using the population formula when the question says sample: a sample divides by n - 1.', 'Leaving the calculator in radians for a question given in degrees.'],
    [H('Mathematics'), H('Engineering Probability and Statistics'), (L1, 'Topic I, Mathematics, and Topic II, Probability and Statistics'), ('GeniePrep cheat sheet', 'Math pages at the front')])
sec('ethics', 'Ethics questions ask what a licensed engineer must do when duties pull in different directions. The order never changes: the public first, then the client or employer, then other engineers.\n\nThe handbook prints the rules. You do not need to memorise them, but you need to know they are there and how they are organised.',
    ['Choosing the answer that protects the client or the engineer when the public is at risk.', 'Treating a seal as a formality: it means the work was done under your direct control.'],
    [H('Ethics and Professional Practice'), (L3, 'Topic XVI, Ethics and Professional Practice')])
sec('econ', 'Money today is worth more than the same money later, because money today can earn interest. Every question here moves money through time so that amounts can be compared fairly.\n\nDraw a timeline, mark each payment, and pick the factor that converts what you have into what you want.',
    ['Mixing up the factor direction: finding a future amount when the question wants a present one.', 'Forgetting that a sunk cost has already been spent and does not belong in the comparison.'],
    [H('Engineering Economics'), (L3, 'Topic XV, Engineering Economics')])
sec('statics', 'Statics is about things that are not moving. If a beam or a truss sits still, every push on it is cancelled by another push, and every twist by another twist.\n\nAlmost every question is the same three steps: draw the body on its own, mark every force, and write that forces and moments each add to zero.',
    ['Leaving a support reaction off the free body diagram.', 'Taking moments about a point that makes the arithmetic harder. Pick a point where an unknown force passes through.'],
    [H('Statics'), (L2, 'Topic VII, Statics')])
sec('dynamics', 'Dynamics is statics with motion added. Forces that do not cancel make things speed up, slow down or turn.\n\nThere are three ways in: follow position, speed and acceleration through time; balance force against mass times acceleration; or track energy from start to finish. Energy is usually the fastest when the question does not ask about time.',
    ['Using an energy method when the question asks for time, or a time method when it asks only for final speed.', 'Forgetting that friction acts against the direction of motion.'],
    [H('Dynamics'), (L2, 'Topic VIII, Dynamics')])
sec('mechmat', 'Mechanics of materials looks inside a loaded part. Stress is how hard the material is being pushed or pulled per unit of area. Strain is how much it deforms in response.\n\nFour loadings cover the topic: pulling along the length, twisting, bending and shear. Each has one formula for stress and one for deformation.',
    ['Mixing units: stay in N, mm and MPa and the numbers work out.', 'Reading the maximum moment at midspan when the load is not symmetric. The peak is where shear crosses zero.'],
    [H('Mechanics of Materials'), (L2, 'Topic IX, Mechanics of Materials')])
sec('materials', 'This topic covers what civil works are built from: concrete, asphalt, steel, aggregate and wood. Questions ask how a mix is proportioned, how a material is tested and what the test result means.\n\nMuch of it is recognising which test goes with which property and reading a stress-strain curve.',
    ['Confusing the water-cement ratio (by mass) with a volume ratio.', 'Using a cylinder diameter as if it were the radius when computing area.'],
    [H('Materials Science/Structure of Matter'), H('Civil Engineering'), (L2, 'Topic X, Materials')])
sec('fluids', 'Fluids at rest press equally in all directions, and the pressure grows with depth. Fluids in motion trade pressure, speed and height against each other while keeping the total the same, apart from losses.\n\nTwo ideas carry most questions: what goes in must come out, and energy is conserved along the flow.',
    ['Mixing gauge and absolute pressure.', 'Using pipe diameter where the formula needs area: area changes with the square of diameter.'],
    [H('Fluid Mechanics'), (L1, 'Topic III, Fluid Mechanics')])
sec('surveying', 'Surveying turns measurements on the ground into positions, areas, volumes and elevations. Angles and distances give horizontal position. A level and a rod give height.\n\nMost questions are careful bookkeeping: add and subtract in the right order and keep track of direction.',
    ['Swapping backsight and foresight. Backsight is added to the known elevation and foresight is subtracted.', 'Mixing bearings and azimuths without converting.'],
    [H('Civil Engineering'), (L3, 'Topic XII, Transportation and Surveying')])
sec('water', 'This is the largest topic. It follows water from rain, across the land, through channels, pipes and pumps, into the ground, and through treatment before and after people use it.\n\nSplit it into three parts when studying: how much water there is (hydrology), how it moves (hydraulics) and how it is cleaned (treatment).',
    ['Using the wrong form of Manning\'s equation: the SI form has no 1.49 factor.', 'Giving detention time in days when the options are in hours.'],
    [H('Civil Engineering'), H('Environmental Engineering'), H('Fluid Mechanics'), (L1, 'Topic IV, Hydraulics and Hydrologic Systems, and Topic V, Environmental Engineering')])
sec('structural', 'Structural questions ask two things: what forces and deflections does a structure experience, and is a given steel or concrete member strong enough?\n\nThe analysis half is statics and mechanics of materials applied to whole beams, trusses and frames. The design half adds load factors and the capacity formulas for steel and reinforced concrete.',
    ['Comparing a factored load with a nominal strength without applying the strength reduction factor.', 'Using actual length instead of effective length for a column whose ends are not pinned.'],
    [H('Civil Engineering'), H('Mechanics of Materials'), (L2, 'Topic XI, Structural Design, first chapters'), (L3, 'Topic XI, Structural Design, from structural steel onward')])
sec('geotech', 'Soil is grains, water and air. Geotechnical questions start by describing that mixture, then ask how much load it can carry and how it will settle or push on a wall.\n\nThe idea behind most of the topic is effective stress: the grains carry only the part of the load that the water does not.',
    ['Using total stress where effective stress is needed below the water table.', 'Confusing void ratio (voids over solids) with porosity (voids over total volume).'],
    [H('Civil Engineering'), (L2, 'Topic VI, Geotechnical Engineering')])
sec('transport', 'Transportation questions cover the shape of a road, how traffic moves along it, the signs and signals that control it, the pavement underneath and how demand is forecast.\n\nGeometric design questions come down to what a driver can see and how quickly a vehicle can stop or turn at the design speed.',
    ['Using mph in a formula that expects ft/s, or the reverse. The 1.47 factor converts mph to ft/s.', 'Entering grades as percentages where the formula expects decimals.'],
    [H('Civil Engineering'), (L3, 'Topic XII, Transportation and Surveying')])
sec('construction', 'Construction questions are about running a project: who is responsible for what, how long the work takes, what it costs and whether it is on track.\n\nScheduling and earned value questions are arithmetic once the network or the three cost figures are laid out clearly.',
    ['Mixing up the cost index (earned value over actual cost) and the schedule index (earned value over planned value).', 'Forgetting to convert thickness to the same unit as length and width in a quantity takeoff.'],
    [H('Civil Engineering'), (L3, 'Topic XIII, Construction')])

T = {'Ethics and Professional Practice': ['ethics'], 'Mathematics': ['math'], 'Engineering Probability and Statistics': ['math'], 'Materials Science/Structure of Matter': ['materials'],
     'Statics': ['statics'], 'Dynamics': ['dynamics'], 'Mechanics of Materials': ['mechmat', 'structural'], 'Fluid Mechanics': ['fluids', 'water'], 'Engineering Economics': ['econ'],
     'Civil Engineering': ['surveying', 'water', 'structural', 'geotech', 'transport', 'construction', 'materials'], 'Environmental Engineering': ['water']}
NOTES = {'Civil Engineering': 'The longest section for this exam: geotechnical, structural, hydrology and hydraulics, transportation, surveying and construction.',
         'Environmental Engineering': 'Water and wastewater treatment, water quality and testing.', 'Mechanics of Materials': 'Also holds beam deflection formulas and column buckling.',
         'Fluid Mechanics': 'Also holds pump and pipe flow formulas used in water resources.'}
ref = {'handbook': {'title': 'NCEES FE Reference Handbook', 'edition': '10.0.1',
                    'note': 'Page ranges follow your copy, edition 10.0.1. NCEES has issued newer editions since, so download the current one from your MyNCEES account and expect pages to shift.'},
       'sections': [{'id': 'hb-' + str(i), 'title': s, 'topics': T[s], 'pages': HBP[s], 'notes': NOTES.get(s, '')} for i, s in enumerate(HBP, 1)],
       'sources': [
        {'title': 'NCEES FE Reference Handbook 10.0.1', 'file': '2026-03-04_FE-HANDBOOK-10-1.pdf', 'use': 'The only reference allowed in the exam. Practise finding formulas in it.', 'note': 'Not the current edition.'},
        {'title': 'Lindeburg FE Civil Review Manual (2018), file 1 of 3', 'file': '2026-03-04_PE-FE-LINDEBURG-REVIEW-MANUAL-1-OF-3-2018.pdf', 'use': 'Reading for math, statistics, fluid mechanics, hydraulics, hydrology and environmental.', 'note': 'Written for the pre-2020 exam specification.'},
        {'title': 'Lindeburg FE Civil Review Manual (2018), file 2 of 3', 'file': '2026-03-04_PE-FE-LINDEBURG-REVIEW-MANUAL-2-OF-3-2018.pdf', 'use': 'Reading for geotechnical, statics, dynamics, mechanics of materials, materials and the start of structural design.', 'note': 'Starts at chapter 17.'},
        {'title': 'Lindeburg FE Civil Review Manual (2018), file 3 of 3', 'file': '2026-03-04_PE-FE-LINDEBURG-REVIEW-MANUAL-3-OF-3-2018.pdf', 'use': 'Reading for structural steel, transportation, surveying, construction, economics and ethics.', 'note': 'Starts at chapter 42. Its Computational Tools topic is no longer on the exam.'},
        {'title': 'Lindeburg FE Civil Practice Problems (2018)', 'file': '2026-03-04_PE-FE-LINDEBURG-PRACTICE-PROBLEMS-2018.pdf', 'use': 'Extra practice by topic once a topic\'s questions here run out.', 'note': 'Pre-2020 specification.'},
        {'title': 'GeniePrep FE Civil problems workbook (2025)', 'file': '2026-03-04_FE-FULL-GUIDE-GENIEPREP-2025.pdf', 'use': 'Worked problems by topic with linked video solutions.', 'note': ''},
        {'title': 'GeniePrep FE cheat sheet (2025)', 'file': '2026-03-04_FE-CHEAT-SHEET-GENIEPREP-2025.pdf', 'use': 'Quick formula review.', 'note': 'Not allowed in the exam. Use the handbook for lookup practice.'}]}
with open(os.path.join(ROOT, 'reference.json'), 'w') as f:
    json.dump(ref, f, indent=1, ensure_ascii=False); f.write('\n')
print('guide and reference written')
