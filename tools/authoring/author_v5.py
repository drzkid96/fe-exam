"""Second versions for the rule-and-judgement question types, which cannot be varied by changing numbers."""
import json
from author_v import BANK, _load, EXPR, STATS, save
def B(base, stem, options, ci, concept, sol, calc=None, basis=None):
    bank = _load(base.rsplit('-', 1)[0]); i = next(k for k, x in enumerate(bank) if x['id'] == base); b = bank[i]
    b.update(family=base, version=1, versions=2, eli5=concept)
    q = json.loads(json.dumps(b)); q.update(id=base + '-b', version=2, stem=stem, options=[{'id': 'abcd'[k], 'text': t} for k, t in enumerate(options)], answer='abcd'[ci], solution=sol.replace(' || ', '\n\n'))
    q.pop('figure', None)
    if calc: EXPR[q['id']] = calc; q['verify'] = {'method': 'computed'}
    else: q['verify'] = {'method': 'reference', 'basis': basis or b['verify'].get('basis') or 'Standard definition'}
    bank.insert(i + 1, q); STATS['families'] += 1; STATS['versions'] += 2
MR = "Under the Model Rules the first duty is to the health, safety and welfare of the public, ahead of the duty to an employer or client. When professional judgement is overruled and the public is endangered, the engineer must notify the employer or client and any other authority that may be appropriate."
B('ethics-0001', "During construction an engineer learns that a contractor has left out reinforcement that the drawings require in a public walkway. The engineer's employer says to let it go to stay on schedule. Under the NCEES Model Rules, what must the engineer do?",
  ["Notify the employer and any other authority that may be appropriate", "Accept the decision, because the employer directs the work", "Wait to see whether the walkway shows distress", "Raise the issue anonymously online"], 0, MR,
  "The omission endangers the public and the engineer's judgement has been overruled, so the rule on notification applies: tell the employer formally and, if the hazard remains, the authority that can act on it. || Accepting the decision or waiting leaves the hazard in place. An anonymous post is not notification to an appropriate authority.")
B('ethics-0002', "A colleague who is not licensed completes a drainage design in another office, without a licensed engineer's involvement, and asks her to seal it so it can be submitted today. What should she do?",
  ["Seal it, because the colleague is competent", "Seal it after checking the title sheet", "Decline, because the work was not prepared under her responsible charge", "Let the colleague apply her seal"], 2,
  "A licensee may sign and seal only work prepared under their responsible charge, meaning direct control and personal supervision, and only within their competence. The seal certifies that supervision; it is not a quality stamp added afterwards.",
  "She had no control over or supervision of the design, so sealing it would violate the Model Rules even if the design is correct. || To seal it properly she would need to take responsible charge: review the work thoroughly, direct any changes and take professional responsibility for it. Letting someone else apply her seal is also a violation.")
B('ethics-0003', "An engineer reviewing bids for a city owns shares in one of the bidding contractors. What do the Model Rules require?",
  ["Nothing, provided the review is fair", "Disclosure of the conflict of interest to the employer or client", "Sale of the shares after the award", "A lower score for that bidder to offset any bias"], 1,
  "Licensees must disclose to their employer or client every known or potential conflict of interest, or any circumstance that could influence, or appear to influence, their judgement. Disclosure comes before the decision, and the client decides how to proceed.",
  "Owning shares in a bidder could influence the review or appear to. The rule is disclosure to the city, which can then reassign the review. || Staying silent, selling later or adjusting scores all leave the client uninformed.")
B('ethics-0004', "An engineer licensed only in State A is asked to seal drawings for a project in State B. Which statement is correct?",
  ["The State A seal is valid in every state", "The seal is valid if the client is based in State A", "Passing the FE exam allows practice in any state", "The engineer must first be licensed in State B"], 3,
  "Engineering licences are issued by each state or territory and are valid only there. Practising or offering to practise elsewhere requires that jurisdiction's licence, usually obtained through comity on the strength of the existing licence, exams and experience.",
  "The project is in State B, so State B's licensing law applies. The engineer must obtain a State B licence, normally by comity, before sealing the drawings. || Where the client is based does not matter, and the FE exam alone grants no right to practise.")
B('ethics-0005', "A design followed the practice that reasonably prudent engineers would have used at the time, yet the structure later performed poorly. In a negligence claim, what is the most likely finding on the standard of care?",
  ["It was breached, because the outcome was poor", "It was not breached, because the standard is reasonable care, not perfection", "It was breached, because engineers guarantee results", "It does not apply to engineers"], 1,
  "Negligence requires a duty, a breach of the standard of care, causation and damages. The standard of care is the skill and care ordinarily exercised by reasonably prudent engineers doing similar work in similar circumstances. It does not promise a perfect outcome.",
  "The engineer did what a reasonably prudent engineer would have done, so the standard of care was met and there is no breach, whatever the outcome. || Engineers do not guarantee results unless a contract says so.")
B('ethics-0006', "An employee of an engineering firm is injured while inspecting a construction site. Which insurance pays the employee's medical costs and lost wages?",
  ["Professional liability insurance", "Builder's risk insurance", "Workers' compensation insurance", "A performance bond"], 2,
  "Each policy covers a different risk. Professional liability (errors and omissions) covers losses from design errors. General liability covers injury or property damage to others from operations. Workers' compensation covers a firm's own employees who are hurt at work. Builder's risk covers the structure under construction.",
  "The injured person is the firm's own employee, hurt in the course of work, so workers' compensation responds. || Professional liability answers claims about the design, builder's risk covers the work itself, and a bond is a guarantee of performance, not insurance for injuries.")
B('ethics-0007', "A contractor promises to regrade a client's yard, and the client promises nothing in return. Which element of an enforceable contract is missing?",
  ["Offer", "Competent parties", "Lawful purpose", "Consideration"], 3,
  "An enforceable contract needs an offer, acceptance, consideration, competent parties and a lawful purpose. Consideration is the exchange of something of value by each side; a one-sided promise is a gift, not a contract.",
  "The contractor gives a promise of work but receives nothing, so there is no consideration and the promise cannot be enforced as a contract. || The other elements are present: there is an offer, the parties are competent and regrading is lawful.")
B('ethics-0008', "An owner agrees to reimburse a contractor's actual costs and to pay a fixed fee on top. Which party carries most of the risk of cost overruns?",
  ["The owner", "The contractor", "The engineer", "The surety"], 0,
  "The payment terms of a contract decide who carries cost risk. Under a lump sum the contractor does, because the price is fixed. Under cost plus a fee the owner does, because actual costs are reimbursed. Unit price contracts split it: the contractor carries the unit cost, the owner the quantity.",
  "Costs are reimbursed whatever they turn out to be, so an overrun is paid by the owner. The contractor's fee is fixed and is not at risk. || Under a lump sum contract the answer would be the contractor.")
B('ethics-0009', "A contractor working on an engineer's project offers the engineer free use of a holiday home, with no request attached. What should the engineer do?",
  ["Accept, because nothing was asked in return", "Accept, and disclose it after the project closes", "Decline, because gratuities from contractors in connection with the work are not allowed", "Accept only if colleagues can use it too"], 2,
  "Licensees shall not solicit or accept gratuities, directly or indirectly, from contractors, their agents or other parties in connection with work for employers or clients. No favour needs to be requested; the gift itself compromises independence or appears to.",
  "The offer comes from a contractor on the engineer's own project, so it is a gratuity in connection with the work and must be declined. || Disclosing later or sharing it does not cure the problem.")
B('construction-0008', "On a topographic map, a set of closed contour lines carries short tick marks (hachures) pointing inward. What does this show?",
  ["A hill or summit", "A depression", "A ridge line", "A uniform slope"], 1,
  "Contour lines join points of equal elevation. Close spacing means steep ground and wide spacing means flat ground. Closed loops normally mark a hill; hachures on the downhill side mark a depression. Contours bend upstream where they cross a valley.",
  "Closed contours with inward hachures mean the ground falls toward the centre, which is a depression. Without hachures the same loops would be a hill.")
B('construction-0009', "An owner hires a designer under one contract and, once the design is complete, awards a separate construction contract to the lowest responsive bidder. Which delivery method is this?",
  ["Design-build", "Construction manager at risk", "Design-bid-build", "Integrated project delivery"], 2,
  "Delivery methods differ in who holds which contract. Design-bid-build: separate, sequential contracts for design and construction. Design-build: one contract for both. Construction manager at risk: a manager joins during design and guarantees a maximum price.",
  "Two separate contracts, with construction bid after the design is finished, is design-bid-build, the traditional method. || Design-build would put design and construction under a single contract.")
B('construction-0010', "Which bond guarantees that the contractor will complete the work in accordance with the contract?",
  ["Bid bond", "Payment bond", "Maintenance bond", "Performance bond"], 3,
  "A surety bond is a three-party guarantee from a surety to the owner. A bid bond guarantees that the bidder will sign the contract at its bid price. A performance bond guarantees completion of the work. A payment bond guarantees that subcontractors and suppliers are paid.",
  "Completion of the work is what a performance bond guarantees. If the contractor defaults, the surety arranges or pays for completion up to the bond amount.")
B('construction-0013', "A project has a planned value of $150,000, an earned value of $180,000 and an actual cost of $170,000 at the status date. What is the schedule variance?",
  ["-$30,000", "$10,000", "$20,000", "$30,000"], 3,
  "Earned value analysis measures progress in budget terms. Schedule variance is SV = EV - PV and cost variance is CV = EV - AC. A positive variance is favourable: ahead of schedule or under budget.",
  "SV = EV - PV = 180,000 - 150,000 = $30,000. The project has earned more than was planned by this date, so it is ahead of schedule. || For reference, CV = EV - AC = 180,000 - 170,000 = $10,000, under budget.", calc="180000 - 150000")
B('econ-0011', "Option A pays a certain $45,000. Option B has a 70% chance of paying $80,000 and a 30% chance of losing $20,000. Based on expected value, which option is better and by how much?",
  ["A by $5,000", "B by $5,000", "B by $11,000", "They are equal"], 1,
  "The expected value of an uncertain option is the sum of each outcome times its probability, with losses negative. Comparing expected values ignores risk, so it suits decisions that are repeated often or small relative to the owner's resources.",
  "EV of B = 0.70(80,000) + 0.30(-20,000) = 56,000 - 6,000 = $50,000. || EV of A = $45,000. || B is better by 50,000 - 45,000 = $5,000.", calc="('B' if 0.7*80000 - 0.3*20000 > 45000 else 'A') + ' by $%s' % format(int(abs(0.7*80000 - 0.3*20000 - 45000)), ',')")
B('geotech-0008', "A sand has 2% fines, a coefficient of uniformity of 4 and a coefficient of curvature of 1.2. What is its Unified Soil Classification symbol?",
  ["SW", "SP", "SM", "SC"], 1,
  "In the Unified Soil Classification System a sand with less than 5% fines is classified on gradation alone. It is well graded, SW, only if the coefficient of uniformity is at least 6 and the coefficient of curvature is between 1 and 3. Otherwise it is poorly graded, SP.",
  "Fines are 2%, below 5%, so the choice is between SW and SP. || C_{u} = 4 is less than 6, so the sand fails the well-graded test even though C_{c} = 1.2 is in range. The symbol is SP.", basis="Unified Soil Classification System: clean sands are SW when Cu >= 6 and 1 <= Cc <= 3, otherwise SP")
B('geotech-0017', "Which foundation type carries load down to a deep stratum through a large-diameter, cast-in-place concrete element?",
  ["Mat foundation", "Strip footing", "Drilled shaft", "Spread footing"], 2,
  "Shallow foundations (spread, strip and mat) bear on soil near the surface. Deep foundations (driven piles and drilled shafts) carry load to stronger material at depth or shed it through skin friction along their length.",
  "A drilled shaft, also called a drilled pier or caisson, is made by drilling a hole and filling it with reinforced concrete. || Mats, strips and spread footings are all shallow foundations.")
B('geotech-0022', "A geogrid is placed within the aggregate base of a road built on a soft subgrade. What is its primary function?",
  ["Filtration", "Reinforcement", "Barrier to water", "Drainage"], 1,
  "Geosynthetics are chosen by function. Geotextiles separate, filter, drain or reinforce. Geogrids, with their open apertures, interlock with aggregate and reinforce. Geomembranes are barriers.",
  "A geogrid interlocks with the aggregate and takes tension, which spreads wheel loads and limits rutting. That is reinforcement. || Its open grid cannot filter or act as a barrier.")
B('materials-0007', "Which property does a Charpy test measure?",
  ["Hardness", "Fatigue life", "Creep rate", "Impact toughness"], 3,
  "Mechanical tests each target one property. Hardness tests (Brinell, Rockwell) measure resistance to indentation. The Charpy test breaks a notched bar with a pendulum and measures the energy absorbed, which is impact toughness. Fatigue tests apply cyclic load; creep tests apply sustained load at temperature.",
  "The Charpy test reports the energy absorbed in fracturing a notched specimen, a measure of impact toughness. Run at several temperatures, it locates the ductile-to-brittle transition.")
B('materials-0008', "What is the minimum yield strength of ASTM A992 steel, the usual grade for wide-flange beams?",
  ["250 MPa (36 ksi)", "345 MPa (50 ksi)", "420 MPa (60 ksi)", "450 MPa (65 ksi)"], 1,
  "Steel grades are named or specified by minimum yield strength. A36 has 250 MPa (36 ksi). A992, used for wide-flange shapes, has 345 MPa (50 ksi). Grade 60 reinforcing bar has 420 MPa (60 ksi).",
  "A992 has a minimum yield strength of 345 MPa (50 ksi). || 250 MPa is A36 and 420 MPa is Grade 60 reinforcing bar.", basis="ASTM A992: minimum yield strength 50 ksi (345 MPa)")
B('materials-0011', "What does the area under a material's stress-strain curve, up to the yield point only, represent?",
  ["Toughness", "Ductility", "Modulus of resilience", "Hardness"], 2,
  "The area under a stress-strain curve is energy per unit volume. Up to the yield point it is the modulus of resilience, the energy the material can absorb and fully recover. Up to fracture it is the toughness.",
  "Stopping at the yield point gives the modulus of resilience, which for a linear material equals (yield stress)^{2} / (2E). || The whole area to fracture would be toughness.")
B('math-0003', "Vectors **A** = 2**i** + 2**j** and **B** = 3**i** lie in the same plane. What is the angle between them?",
  ["30°", "45°", "60°", "90°"], 1,
  "The dot product links two vectors to the angle between them: A · B = |A||B| cos(angle). Compute the dot product from components, divide by the product of the magnitudes and take the inverse cosine. A zero dot product means the vectors are perpendicular.",
  r"A · B = 2(3) + 2(0) = 6. || |A| = \sqrt{2^{2} + 2^{2}} = 2.828 and |B| = 3. || cos(angle) = \frac{6}{2.828 × 3} = 0.7071, so the angle is 45°.", calc="acos((2*3 + 2*0)/(hypot(2, 2)*hypot(3, 0)))*180/pi")
B('math-0014', "Two fair dice are rolled. What is the probability that the total is 9?",
  ["0.083", "0.111", "0.139", "0.167"], 1,
  "When all outcomes are equally likely, probability is the number of favourable outcomes divided by the total number. Two dice give 6 × 6 = 36 ordered outcomes, so count the ordered pairs that produce the total.",
  r"Pairs that total 9: (3, 6), (4, 5), (5, 4), (6, 3), which is 4 of 36. || P = \frac{4}{36} = 0.111.", calc="4/36")
B('structural-0001', "A planar truss has 6 joints, 9 members and 3 support reactions. Assuming it is stable, how is it classified?",
  ["Statically determinate", "Statically indeterminate to the first degree", "Statically indeterminate to the second degree", "Statically indeterminate to the third degree"], 0,
  "Each joint of a plane truss gives two equilibrium equations, so there are 2j equations for m member forces and r reactions. If m + r = 2j the truss is determinate; if m + r is larger, the excess is the degree of indeterminacy; if smaller, the truss is unstable.",
  "Unknowns: m + r = 9 + 3 = 12. || Equations: 2j = 2(6) = 12. || They are equal, so the truss is statically determinate.", calc="{0: 'Statically determinate', 1: 'first degree', 2: 'second degree', 3: 'third degree'}[9 + 3 - 2 * 6]")
B('structural-0011', "A beam is fixed at both ends. Counting vertical, horizontal and moment reactions, how is it classified?",
  ["Statically determinate", "Statically indeterminate to the first degree", "Statically indeterminate to the second degree", "Statically indeterminate to the third degree"], 3,
  "A single rigid body in a plane has three equilibrium equations. Count the reaction components: a fixed support gives three, a pin two and a roller one. Reactions beyond three are redundants, and their number is the degree of indeterminacy.",
  "Each fixed end supplies a vertical force, a horizontal force and a moment, so there are 3 + 3 = 6 reactions. || 6 - 3 = 3, so the beam is statically indeterminate to the third degree.", calc="{0: 'determinate', 1: 'first degree', 2: 'second degree', 3: 'third degree'}[(3 + 3) - 3]")
B('water-0022', "Under the U.S. Safe Drinking Water Act, which term is a health goal that is not enforceable, set at the level with no known or expected risk?",
  ["Maximum contaminant level (MCL)", "Maximum contaminant level goal (MCLG)", "Secondary maximum contaminant level", "Treatment technique"], 1,
  "The Safe Drinking Water Act uses paired terms. The maximum contaminant level goal (MCLG) is a health target and is not enforceable. The maximum contaminant level (MCL) is the enforceable limit, set as close to the goal as is feasible. Secondary standards cover taste, odour and appearance.",
  "A non-enforceable health goal is the MCLG. || The MCL is the enforceable limit, and secondary standards are guidelines for aesthetic qualities.")
if __name__ == '__main__': save()
