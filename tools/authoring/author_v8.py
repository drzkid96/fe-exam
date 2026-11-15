"""Third written versions for the rule-and-judgement question types (multiple choice). Run after the other version scripts."""
import json
from author_v import BANK, _load, EXPR, STATS, save
def C3(base, stem, options, ci, sol, calc=None, basis=None):
    bank = _load(base.rsplit('-', 1)[0]); i = next(k for k, x in enumerate(bank) if x['id'] == base); b = bank[i]
    j = i + 1
    while j < len(bank) and bank[j].get('family') == base: j += 1
    n = j - i + 1
    q = json.loads(json.dumps(b)); q.update(id=base + '-' + 'bcdefgh'[n - 2], version=n, stem=stem, options=[{'id': 'abcd'[k], 'text': t} for k, t in enumerate(options)], answer='abcd'[ci], solution=sol.replace(' || ', '\n\n'))
    q.pop('figure', None); q.pop('solutionFigure', None)
    if calc: EXPR[q['id']] = calc; q['verify'] = {'method': 'computed'}
    else: q['verify'] = {'method': 'reference', 'basis': basis or b['verify'].get('basis') or 'Standard definition'}
    bank.insert(j, q)
    for k in range(i, j + 1): bank[k]['versions'] = n
    STATS['versions'] += 1
MR = 'NCEES Model Rules, Rules of Professional Conduct'
C3('construction-0008', "On a contour map, the contour lines across a site are evenly spaced and far apart. What does this indicate?", ["A gentle, uniform slope", "A cliff", "A closed depression", "A ridge line"], 0,
   "Each contour is a line of equal elevation, so the ground rises by one contour interval between neighbours. Lines far apart mean a long run for that rise, a gentle slope; even spacing means the slope is uniform.", basis='Definition of a contour line')
C3('construction-0009', "Under which delivery method does the owner first hire a designer to complete the plans, then award a separate construction contract by competitive bid?", ["Design-build", "Design-bid-build", "Construction manager at risk", "Integrated project delivery"], 1,
   "Design-bid-build keeps design and construction in two separate contracts held by the owner, in sequence. || Design-build puts both in one contract; a construction manager at risk joins during design and guarantees a maximum price.", basis='Standard definitions of project delivery methods')
C3('construction-0010', "Which bond protects the owner if the low bidder refuses to sign the contract at its bid price?", ["Payment bond", "Performance bond", "Bid bond", "Maintenance bond"], 2,
   "A bid bond guarantees that the bidder will enter into the contract at the price bid. If it does not, the surety pays the owner the difference up to the bond amount. || A performance bond covers completion of the work; a payment bond covers subcontractors and suppliers.", basis='Standard definitions of construction surety bonds')
C3('construction-0013', "A project has a planned value of $240,000 and an earned value of $255,000 at the status date. What is the schedule variance?", ["-$15,000", "$15,000", "$495,000", "$1.06"], 1,
   "Schedule variance = earned value - planned value = 255,000 - 240,000 = $15,000. || A positive value means more work has been completed than was planned by this date: the project is ahead of schedule.", calc="255000-240000")
C3('econ-0011', "Option A pays a certain $45,000. Option B has a 70% chance of paying $70,000 and a 30% chance of paying nothing. Which has the higher expected value, and by how much?", ["A by $1,000", "B by $4,000", "B by $25,000", "They are equal"], 1,
   "Expected value of B = 0.70 × 70,000 + 0.30 × 0 = $49,000. || That is 49,000 - 45,000 = $4,000 more than the certain $45,000 from A. Expected value says nothing about risk: B can also pay nothing.", calc="0.7*70000-45000")
C3('ethics-0001', "An engineer finds that a bridge railing detail approved by her supervisor does not meet the required crash-test standard. The supervisor tells her to issue the plans anyway. Under the NCEES Model Rules, what must she do?",
   ["Issue the plans, because the supervisor is responsible", "Notify her employer in writing and, if the hazard remains, the appropriate authority", "Quietly change the detail without telling anyone", "Resign without comment"], 1,
   "Her professional judgement has been overruled in a way that endangers the public. The rule requires her to notify the employer or client and any other authority that may be appropriate. || Issuing the plans or leaving silently leaves the hazard in place.", basis=MR)
C3('ethics-0002', "A firm buys standard plans from a vendor and asks its licensed engineer to seal them, unchanged, for a local project. When may she seal them?",
   ["At once, because the vendor is reputable", "Never, under any conditions", "Only after reviewing and adapting them thoroughly enough to take responsible charge of the work", "After the client signs a waiver"], 2,
   "A seal certifies work done by the licensee or under her responsible charge. Plans prepared by others can be sealed only once she has reviewed them in detail, made them fit the site and taken professional responsibility for them.", basis=MR)
C3('ethics-0003', "An engineer sits on a city planning commission that is about to vote on a project her firm designed. What do the Model Rules require?",
   ["Vote, since she knows the project best", "Disclose the interest and take no part in the decision", "Vote only if the result would be the same anyway", "Ask a colleague to lobby the other members"], 1,
   "A licensee serving on a public body must not take part in decisions about services provided by her own firm. She discloses the conflict and abstains.", basis=MR)
C3('ethics-0004', "What must an engineer licensed in one state normally show in order to be licensed in a second state by comity?",
   ["That the original licence was earned under requirements at least equal to the second state's", "Only that a fee has been paid", "That the engineer has a client in the second state", "A new passing score on the FE exam"], 0,
   "Comity lets a board license an engineer already licensed elsewhere without repeating the exams, provided the education, examinations and experience behind the first licence meet the second state's standards.", basis='NCEES Model Law, licensure by comity')
C3('ethics-0005', "Which statement about the standard of care for engineers is correct?",
   ["It requires a perfect result", "It is whatever the client specifies", "It requires the skill and care a reasonably competent engineer would use in the same circumstances", "It applies only to licensed structural engineers"], 2,
   "The law compares an engineer's work with what a reasonably competent peer would have done in the same place and time. A bad outcome alone is not negligence.", basis='General principles of professional liability')
C3('ethics-0006', "Which type of insurance covers injuries to a firm's own employees while they are working?",
   ["Professional liability", "Commercial general liability", "Builder's risk", "Workers' compensation"], 3,
   "Workers' compensation pays medical costs and lost wages for employees injured on the job, whoever was at fault. || Professional liability covers design errors; general liability covers injury or damage to third parties.", basis='Standard definitions of insurance types')
C3('ethics-0007', "A contractor promises to repave a driveway, and the owner promises nothing in return. Why is this not an enforceable contract?",
   ["There is no consideration", "It is not notarised", "Paving is not a lawful purpose", "The contractor is licensed"], 0,
   "Each party to a contract must give something of value, called consideration. A one-sided promise with nothing given in exchange is a gift, not a contract.", basis='General principles of contract law')
C3('ethics-0008', "Under which contract type is the contractor paid its actual costs plus a fee, leaving most of the cost risk with the owner?",
   ["Lump sum", "Unit price", "Cost-plus", "Guaranteed maximum price"], 2,
   "In a cost-plus contract the owner reimburses actual costs and adds a fee. The contractor's risk is low and the owner's final cost is uncertain. || Lump sum puts the cost risk on the contractor; unit price shares it, with quantities at the owner's risk.", basis='Standard definitions of construction contract types')
C3('ethics-0009', "A vendor offers an engineer a free tablet computer for attending a product demonstration while the engineer is evaluating that vendor's bid. What should the engineer do?",
   ["Accept it, because it was offered to everyone", "Decline it", "Accept it and give it to charity later", "Accept it but score the vendor lower"], 1,
   "A valuable gift from a party whose bid the engineer is judging could influence, or appear to influence, that judgement. The rules require declining it.", basis=MR)
C3('ethics-0010', "A licensed engineer leaves a firm in the middle of a project she was directing. Who may seal the completed plans?",
   ["Any licensed engineer in the firm, at once", "The project manager, whether licensed or not", "A licensed engineer who takes over responsible charge and reviews the earlier work thoroughly", "No one; the project must restart"], 2,
   "The successor may seal the work only after taking responsible charge: reviewing what was done, directing what remains and accepting professional responsibility for all of it.", basis=MR)
C3('ethics-0011', "A client asks an engineer to delete a paragraph from a traffic study that says a proposed driveway does not meet sight distance requirements. What should the engineer do?",
   ["Delete it, since the client owns the report", "Keep the finding in the report", "Move it to a footnote in small type", "Delete it and tell the reviewing agency by phone"], 1,
   "Reports must be objective and truthful and include all relevant information. Removing a safety finding would make the report misleading.", basis=MR)
C3('ethics-0012', "A contractor offers to pave an inspector's home driveway at cost while the inspector is assigned to that contractor's project. What should the inspector do?",
   ["Accept, since full cost is being paid", "Accept after the project ends", "Decline", "Accept and report it afterwards"], 2,
   "A favour of value from a contractor whose work the inspector judges is a prohibited gratuity, whether or not a price is paid, because it could influence or appear to influence the inspector's judgement.", basis=MR)
C3('ethics-0013', "Which fact would most strongly support a claim that an engineer breached the standard of care?",
   ["The project cost more than estimated", "The engineer ignored a mandatory requirement of the governing code", "Another engineer would have chosen a different layout", "The client was unhappy with the schedule"], 1,
   "Competent engineers follow mandatory code requirements, so ignoring one is strong evidence of falling below the standard of care. Cost overruns and differences of professional opinion are not, by themselves.", basis='General principles of professional liability')
C3('ethics-0014', "A consultant did extra design work at a client's verbal request and was later refused payment for it. What would best have protected the consultant?",
   ["A written contract amendment agreed before the work began", "A higher hourly rate", "Finishing the extra work faster", "A verbal reminder at the next meeting"], 0,
   "Work outside the agreed scope should be authorised in writing, with its fee and schedule, before it is done. Without that, the consultant has little proof that the client agreed to pay.", basis='General principles of contract law')
C3('ethics-0015', "A graduate has passed the FE exam and is certified as an engineer in training. What may the engineer in training do?",
   ["Seal plans for small projects", "Offer engineering services directly to the public", "Do engineering work under the supervision of a licensed engineer, without sealing it", "Use the title Professional Engineer"], 2,
   "An engineer in training is not yet licensed. The certificate records progress toward licensure; the work must be done under a licensed engineer's responsible charge, and only that licensee may seal it.", basis='NCEES Model Law and Model Rules, licensure provisions')
C3('geotech-0008', "A gravel has 2% fines, a coefficient of uniformity of 3 and a coefficient of curvature of 0.8. What is its Unified Soil Classification?", ["GW", "GP", "GM", "SP"], 1,
   "With less than 5% fines, a gravel is GW (well graded) only if its coefficient of uniformity is at least 4 and its coefficient of curvature lies between 1 and 3. Here the uniformity coefficient is 3, so the gravel is poorly graded: GP.", basis='Unified Soil Classification System criteria')
C3('geotech-0017', "Which foundation type carries load through weak surface soil down to a deeper, stronger layer?", ["Spread footing", "Mat foundation", "Pile foundation", "Wall footing"], 2,
   "Piles are long, slender members driven or drilled through weak soil. They carry load by friction along their length and by bearing on the stronger layer at their tip. Footings and mats bear near the surface.", basis='Standard definitions of foundation types')
C3('geotech-0022', "A geotextile is wrapped around the stone of a subsurface drain. What is its main function?", ["Reinforcement", "Filtration", "Waterproofing", "Compaction"], 1,
   "Around a drain the fabric lets water pass into the stone while holding back the surrounding soil particles, so the drain does not clog. That is filtration.", basis='Standard geosynthetic functions: separation, filtration, drainage, reinforcement')
C3('materials-0007', "Which property does a Charpy test measure?", ["Hardness", "Impact toughness", "Tensile strength", "Fatigue life"], 1,
   "A Charpy test breaks a notched bar with a swinging pendulum and records the energy absorbed. That energy is a measure of the material's toughness under sudden loading.", basis='Standard test definitions')
C3('materials-0008', "What is the minimum yield strength of Grade 420 (metric) reinforcing steel?", ["280 MPa", "420 MPa", "520 MPa", "620 MPa"], 1,
   "The grade number of reinforcing steel is its minimum yield strength: Grade 420 yields at 420 MPa, the metric counterpart of Grade 60 (60 ksi).", basis='ASTM A615 grade designations')
C3('materials-0011', "What does the slope of the straight, initial part of a stress-strain curve represent?", ["Toughness", "Yield strength", "Modulus of elasticity", "Ductility"], 2,
   "While the material is elastic, stress is proportional to strain. The constant of proportionality, the slope of that straight line, is the modulus of elasticity: the material's stiffness.", basis="Hooke's law")
C3('math-0003', "Vectors **A** = 2**i** + 2**j** and **B** = 3**i** lie in the same plane. What is the angle between them?", ["30°", "45°", "60°", "90°"], 1,
   r"A · B = 2(3) + 2(0) = 6. |A| = \sqrt{2^{2} + 2^{2}} = 2.828 and |B| = 3. || cos(angle) = \frac{6}{2.828 × 3} = 0.7071, so the angle is 45°.", calc="acos(6/(sqrt(8)*3))*180/pi")
C3('math-0014', "Two fair dice are rolled. What is the probability that the total is 4?", ["0.056", "0.083", "0.111", "0.167"], 1,
   "There are 36 equally likely outcomes. A total of 4 comes from (1, 3), (2, 2) and (3, 1): three outcomes. || P = 3 / 36 = 0.083.", calc="3/36")
C3('structural-0001', "A planar truss has 10 joints, 17 members and 3 support reactions. Assuming it is stable, how is it classified?", ["Unstable", "Statically determinate", "Statically indeterminate to the first degree", "Statically indeterminate to the second degree"], 1,
   "Each joint of a planar truss gives two equilibrium equations: 2 × 10 = 20. The unknowns are the member forces and the reactions: 17 + 3 = 20. || Unknowns equal equations, so the truss is statically determinate.", basis='Truss determinacy: m + r compared with 2j')
C3('structural-0011', "A beam is fixed at both ends and carries loads in its own plane. How is it classified?", ["Statically determinate", "Statically indeterminate to the first degree", "Statically indeterminate to the second degree", "Statically indeterminate to the third degree"], 3,
   "Each fixed end supplies three reaction components: two forces and a moment, six in all. Only three equilibrium equations are available, so the beam is indeterminate to the 6 - 3 = third degree.", basis='Beam determinacy: reactions compared with three equilibrium equations')
C3('water-0022', "Under the U.S. Safe Drinking Water Act, which term is the non-enforceable health goal for a contaminant?", ["Maximum contaminant level (MCL)", "Maximum contaminant level goal (MCLG)", "Treatment technique", "Secondary standard"], 1,
   "The MCLG is the level at which no health effect is expected, with a margin of safety. It is a goal. The MCL, set as close to it as is feasible, is the limit that is enforced.", basis='Safe Drinking Water Act definitions')
def X3(base, sol, calc=None, basis=None, **over):
    """A further version of a drag, ordering, select-several or click-the-figure type: a copy of the first version with the given fields replaced."""
    bank = _load(base.rsplit('-', 1)[0]); i = next(k for k, x in enumerate(bank) if x['id'] == base); j = i + 1
    while j < len(bank) and bank[j].get('family') == base: j += 1
    n = j - i + 1; q = json.loads(json.dumps(bank[i])); q.update(over); q.update(id=base + '-' + 'bcdefgh'[n - 2], version=n, solution=sol.replace(' || ', '\n\n')); q.pop('solutionFigure', None)
    if calc: EXPR[q['id']] = calc; q['verify'] = {'method': 'computed'}
    else: q['verify'] = {'method': 'reference', 'basis': basis}
    bank.insert(j, q)
    for k in range(i, j + 1): bank[k]['versions'] = n
    STATS['versions'] += 1
_o = lambda *t: [{'id': 'abcde'[k], 'text': x} for k, x in enumerate(t)]
_i = lambda *t: [{'id': a, 'text': b} for a, b in t]
X3('construction-0005', "Activities and their dependencies come first, because they define the network. Durations are then estimated. || The forward pass works from the start to give the earliest dates; the backward pass works from the finish to give the latest dates. Float, late minus early, comes last, and the activities with zero float form the critical path.",
   basis='Critical path method procedure', stem="Put the steps of critical path scheduling in order, from first (top) to last (bottom).",
   items=_i(('fwd', 'Forward pass: earliest start and finish dates'), ('list', 'List the activities'), ('float', 'Calculate float and mark the critical path'), ('dur', 'Estimate each duration'), ('dep', 'Set which activities depend on which'), ('back', 'Backward pass: latest start and finish dates')),
   answer=['list', 'dep', 'dur', 'fwd', 'back', 'float'])
X3('geotech-0007', "Consolidation is the slow squeezing of water out of a soil under new load. Water escapes from sand almost at once, so sand settles as the fill is placed. || Clay lets water through thousands of times more slowly, so the clay layer goes on settling for months or years.",
   basis='Consolidation settlement occurs in saturated fine-grained soil of low permeability', stem="A wide fill is placed on the ground surface. Click the layer that will go on settling slowly for a long time afterwards.", answer='clay')
X3('materials-0003', "A cylinder break gives the compressive strength of concrete. The Rockwell test presses an indenter into a metal to measure hardness. The pressure meter measures the air content of fresh concrete. The California bearing ratio test compares a soil's resistance to penetration with that of a standard crushed stone, as a measure of subgrade strength.",
   basis='Standard test methods: ASTM C39 (compressive strength of cylinders), ASTM E18 (Rockwell hardness), ASTM C231 (air content by the pressure method), ASTM D1883 (California bearing ratio)',
   tokens=_i(('cbr', 'California bearing ratio test'), ('cyl', 'Cylinder break'), ('meter', 'Pressure meter'), ('rock', 'Rockwell test')),
   targets=[{'id': 'hard', 'label': 'Hardness of a metal'}, {'id': 'air', 'label': 'Air content of fresh concrete'}, {'id': 'sub', 'label': 'Strength of a subgrade soil'}, {'id': 'comp', 'label': 'Compressive strength of concrete'}],
   answer={'cyl': 'comp', 'rock': 'hard', 'meter': 'air', 'cbr': 'sub'})
X3('math-0005', "The median is the middle value of the sorted data, so half the values lie at or below it. One extreme value moves the mean but hardly moves the middle value. || It equals the mean only for symmetric data. The most frequent value is the mode. With an even number of values the median is the average of the two middle ones, so it need not be one of the data.",
   basis='FE Reference Handbook 10.0.1, Engineering Probability and Statistics, median and mode', stem="Which statements about the median of a set of data are true? Select the two that apply.",
   options=_o("Half of the values lie at or below it", "It is affected less by one extreme value than the mean is", "It always equals the mean", "It is the most frequent value", "It is always one of the data values"), answer=['a', 'b'])
X3('mechmat-0006', r"Elongation = \frac{PL}{AE}, where P is the force, L the length, A the cross-sectional area and E the modulus of elasticity. || A and E are on the bottom, so a larger area or a stiffer material reduces the elongation. L is on top, so a shorter bar stretches less. || More force stretches it more. Aluminium has about a third of the stiffness of steel, so the same bar in aluminium stretches about three times as far.",
   calc="sorted(k for k, r in {'a': 1/2, 'b': 1/2, 'c': 1/2, 'd': 2, 'e': 200/70}.items() if r < 1)", stem="A steel bar is pulled by an axial force. Which changes reduce its elongation? Select all that apply.",
   options=_o("Double the cross-sectional area", "Halve the length", "Use a material with twice the modulus of elasticity", "Double the force", "Replace the steel (E = 200 GPa) with aluminium (E = 70 GPa) of the same size"), answer=['a', 'b', 'c'])
X3('mechmat-0007', r"Take moments about B: R_{A} × L = P × \frac{2L}{3}, so R_{A} = \frac{2P}{3}. Vertical balance then gives R_{B} = P - \frac{2P}{3} = \frac{P}{3}. || R_{A} is the reaction at A and R_{B} the reaction at B. The support nearer the load always carries the larger share.",
   calc="max({'a': 2/3, 'b': 1/3}.items(), key=lambda kv: kv[1])[0]", stem="A simply supported beam carries one point load P at a third of the span from A. Click the support that carries the larger reaction.", answer='a')
X3('surveying-0004', "75° is in the north-east quadrant: N 75° E. || 105° is in the south-east quadrant: 180° - 105° = 75°, so S 75° E. || 255° is in the south-west quadrant: 255° - 180° = 75°, so S 75° W. || 285° is in the north-west quadrant: 360° - 285° = 75°, so N 75° W.",
   calc="{'az%d' % a: ('ne' if a < 90 else 'se' if a < 180 else 'sw' if a < 270 else 'nw') for a in (75, 105, 255, 285)}",
   tokens=_i(('az255', '255°'), ('az105', '105°'), ('az75', '75°'), ('az285', '285°')), targets=[{'id': 'ne', 'label': 'N 75° E'}, {'id': 'se', 'label': 'S 75° E'}, {'id': 'sw', 'label': 'S 75° W'}, {'id': 'nw', 'label': 'N 75° W'}],
   answer={'az75': 'ne', 'az105': 'se', 'az255': 'sw', 'az285': 'nw'})
X3('transport-0006', "Guide signs give directions and information: street names, route numbers, destinations and distances. || A No Parking sign states a rule, so it is regulatory. A Stop Ahead sign warns of a condition ahead, so it is a warning sign.",
   basis='MUTCD Part 2: Chapter 2D guide signs (street name, route and destination signs); Chapter 2B regulatory signs (parking); Chapter 2C warning signs (Stop Ahead W3-1)', stem="Which of these are guide signs under the MUTCD? Select the three that apply.",
   options=_o("Street name sign", "Route marker", "Stop Ahead sign", "Destination and distance sign", "No Parking sign"), answer=['a', 'b', 'd'])
X3('water-0006', "Thickening removes free water first, so the later units can be smaller. Digestion then stabilises the solids: microorganisms break down the organic matter and reduce odour and pathogens. || Dewatering squeezes the digested solids to a cake that can be hauled, and the cake is finally applied to land or disposed of.",
   basis='Conventional wastewater solids (sludge) handling sequence', stem="Put the steps of handling wastewater sludge in order, from first (top) to last (bottom).",
   items=_i(('dew', 'Dewatering'), ('thick', 'Thickening'), ('disp', 'Land application or disposal'), ('dig', 'Stabilisation by digestion')), answer=['thick', 'dig', 'dew', 'disp'])
if __name__ == '__main__': save()
