"""Hand-written key ideas for the subtopics that are about rules and judgement rather than calculation."""
MANUAL = {
 'ethics-a': [
  ('Order of obligations', "The NCEES Model Rules set three duties in this order: to the public, to the employer or client, and to other licensees. The first and foremost responsibility is the health, safety and welfare of the public. When two duties pull in different directions, the public comes first."),
  ('When you are overruled', "If your professional judgement is overruled and public safety is endangered, you must notify your employer or client and whatever other authority is appropriate. Staying quiet, or resigning without telling anyone, does not meet the duty."),
  ('Conflicts of interest', "Disclose every known or potential conflict of interest to your employer or client. You may be paid by more than one party for the same project only if the circumstances are fully disclosed and all parties agree in writing."),
  ('Gifts and payments', "Do not solicit or accept gratuities from contractors, their agents or other parties in connection with work for an employer or client, and do not give anything of value to secure work. The test is whether it could influence, or appear to influence, your judgement."),
  ('Competence and truthfulness', "Take on only the work you are qualified for by education or experience. Professional statements must be objective and truthful, and a public opinion must rest on adequate knowledge of the facts."),
  ('How the exam asks this', "Expect a short scenario with four possible actions. The right answer protects the public, discloses rather than conceals, and stays within the engineer's competence and authority. Doing nothing and quietly complying are almost never correct.")],
 'ethics-b': [
  ('Negligence', "A negligence claim needs four elements: a duty owed, a breach of that duty, causation and actual damages. All four must be shown."),
  ('Standard of care', "An engineer is judged against the care and skill ordinarily used by reasonably prudent engineers doing similar work in similar circumstances. The standard is competence, not perfection, so a bad outcome alone does not prove negligence."),
  ('Kinds of liability', "Liability can arise in tort (negligence), in contract (failing to do what was agreed) or, for product makers, as strict liability, where fault need not be proved."),
  ('Insurance', "Professional liability insurance, also called errors and omissions, covers claims that design errors caused loss. General liability covers bodily injury and property damage from operations. Workers' compensation covers a firm's own employees."),
  ('Time limits', "A statute of limitations starts when the damage is discovered. A statute of repose starts at a fixed event such as substantial completion and sets an outer limit however late the defect appears."),
  ('Reducing exposure', "Use a written scope, keep records of decisions, have work checked, stay within your competence and state clearly what was and was not relied upon.")],
 'ethics-c': [
  ('The path to a license', "The usual route is an accredited engineering degree, the FE exam, about four years of progressive experience under a licensed engineer, then the PE exam. Each state or territory board sets its own requirements. Passing the FE leads to engineer intern status."),
  ('One jurisdiction at a time', "A license is valid only where it was issued. To practise or offer services in another state you need that state's license, normally obtained through comity, where the second board accepts your existing credentials instead of re-examining you."),
  ('Responsible charge and the seal', "Sign and seal only documents prepared under your responsible charge, meaning your direct control and personal supervision, and only in areas where you are competent. Sealing work you did not supervise is a violation even if the work is correct."),
  ('Discipline', "Boards can reprimand, fine, suspend or revoke a license for fraud, gross negligence, incompetence or misconduct. Licensees who know of a violation are expected to report it to the board and cooperate with it."),
  ('Keeping the license', "Renewal usually requires continuing education, and a licensee must follow the laws and rules of every jurisdiction in which they practise.")],
 'ethics-d': [
  ('What makes a contract', "An enforceable contract needs an offer, acceptance, consideration (something of value exchanged), competent parties and a lawful purpose. A missing element makes the agreement void or voidable."),
  ('Payment types and who carries the risk', "Lump sum or fixed price: the contractor carries the cost risk. Unit price: payment follows measured quantities, so the owner carries quantity risk. Cost plus a fee: the owner carries the cost risk. A guaranteed maximum price caps the owner's exposure."),
  ('Breach and remedies', "A material breach excuses the other party from performing and allows a claim for damages. Compensatory damages put the injured party where performance would have. Liquidated damages are a sum agreed in advance, typically per day of late completion."),
  ('Changes', "A change order is a written amendment to scope, price or time, signed by the parties after award. Work done on an oral instruction is a common source of disputes."),
  ('Privity and agency', "Only the parties to a contract can enforce it; that relationship is privity. An engineer administering a construction contract usually acts as the owner's agent and has no contract with the contractor.")],
 'construction-a': [
  ('Delivery methods', "Design-bid-build: the owner holds separate contracts with the designer and the contractor, in sequence. Design-build: one entity holds a single contract for both. Construction manager at risk: the manager commits to a guaranteed maximum price and holds the trade contracts. Agency construction management: the manager only advises."),
  ('Contract documents', "The set is the agreement, the general and supplementary conditions, the specifications, the drawings and any addenda. Addenda change the documents before bids are opened; change orders change them after award."),
  ('Bonds', "A bid bond guarantees the low bidder will sign the contract at the bid price. A performance bond guarantees the work will be completed. A payment bond guarantees subcontractors and suppliers will be paid."),
  ('Sequence of a job', "Advertise, receive bids, award, notice to proceed, construction, substantial completion, punch list, final completion and final payment. Retainage is a share of each payment held back until the work is accepted."),
  ('Paper flow during construction', "A request for information asks the designer to clarify the documents. A submittal or shop drawing shows how the contractor intends to meet them and is reviewed for conformance with the design intent, not for means and methods.")],
 'materials-b': [
  ('Fresh and hardened concrete', "Slump measures workability. Air content is measured by the pressure or volumetric method. Compressive strength comes from cylinders, normally at 28 days. The split-cylinder test gives tensile strength and a beam test gives the modulus of rupture."),
  ('Steel', "A tension test gives yield strength, ultimate strength, modulus of elasticity and percent elongation. Common grades: A36 with a yield of 250 MPa (36 ksi), A992 with 345 MPa (50 ksi), and Grade 60 reinforcing bar with 420 MPa (60 ksi)."),
  ('Hardness and impact', "Brinell and Rockwell tests measure resistance to indentation and correlate with tensile strength. The Charpy impact test measures the energy absorbed in fracture, which indicates toughness and locates the ductile-to-brittle transition temperature."),
  ('Soils and aggregates', "Sieve analysis gives gradation. The Proctor test gives maximum dry density and optimum moisture content. Atterberg limits describe plasticity. The Los Angeles abrasion test measures aggregate toughness, and the CBR test measures subgrade strength."),
  ('Asphalt', "Marshall testing reports stability and flow. Superpave binders carry a performance grade written PG high-low, the pavement temperatures in degrees Celsius between which the binder is expected to perform."),
  ('Who writes the standards', "ASTM and AASHTO publish test methods and material specifications. ACI and AISC publish the design specifications for concrete and steel.")],
 'structural-d': [
  ('Beams and frames', "A rigid body in a plane has three equilibrium equations. With r reaction components and n bodies: r = 3n is statically determinate, r greater than 3n is indeterminate to the degree r - 3n, and r less than 3n is unstable. Each internal hinge adds one condition equation."),
  ('Trusses', "For a plane truss with m members, r reactions and j joints, each joint gives two equations. m + r = 2j is determinate, m + r greater than 2j is indeterminate to the degree m + r - 2j, and m + r less than 2j is unstable."),
  ('Counting is necessary, not sufficient', "A structure that passes the count can still be unstable if its reactions are all parallel or all pass through one point, or if a panel can deform without stressing any member. Check the geometry as well as the count."),
  ('Why the class matters', "A determinate structure is solved with equilibrium alone and is unaffected by support settlement or temperature. An indeterminate one also needs compatibility of deformations, but its redundancy gives alternative load paths.")],
 'geotech-d': [
  ('Working down a layered profile', "Add the total stress layer by layer: unit weight times thickness, using the saturated unit weight below the water table. Pore pressure is zero above the water table and rises at 9.81 kPa per metre below it. Subtract at the depth of interest."),
  ('A moving water table', "Lowering the water table raises effective stress in the soil below it, because pore pressure falls while total stress barely changes. That increase can cause settlement of compressible layers."),
  ('Seepage and the quick condition', "Upward seepage reduces effective stress. At the critical hydraulic gradient, (saturated unit weight - unit weight of water) / unit weight of water, which is close to 1 for most soils, effective stress reaches zero and the soil loses its strength.")],
 'geotech-h': [
  ('Shallow foundations', "Spread footings carry single columns, combined footings carry two or more, strip footings carry walls and a mat (raft) is one thick slab under the whole structure. They suit sites where competent soil lies near the surface."),
  ('Deep foundations', "Driven piles and drilled shafts carry load down to stronger material or shed it through skin friction. Use them where the upper soils are weak or compressible, loads are heavy, or uplift, lateral load or scour governs."),
  ('Choosing', "A mat is chosen when individual footings would cover more than about half the plan area or when differential settlement must be limited. End-bearing piles rely on a firm stratum at the tip; friction piles rely on the shaft.")],
 'geotech-k': [
  ('Mechanical improvement', "Compaction raises density and strength and is controlled against the Proctor maximum. Preloading with a surcharge, often with wick drains, consolidates soft clay before construction. Vibroflotation and dynamic compaction densify loose sands."),
  ('Chemical stabilisation', "Lime suits plastic clays: it lowers the plasticity index and swell potential and raises strength. Portland cement suits granular and low-plasticity soils. Fly ash and bitumen are also used."),
  ('Geosynthetics', "A geotextile can separate a soft subgrade from an aggregate base, filter, drain or reinforce. Geogrids reinforce. Geomembranes are barriers to water.")],
 'transport-d': [
  ('Sign classes', "The MUTCD sorts signs by function, with matching shapes and colours. Regulatory signs give laws and are mostly white rectangles, with the red octagonal STOP and triangular YIELD as exceptions. Warning signs are yellow diamonds. Guide signs are green. Temporary traffic control signs are orange."),
  ('Pavement markings', "Yellow lines separate traffic moving in opposite directions and mark the left edge of divided roads. White lines separate traffic moving the same way and mark the right edge. A broken line may be crossed, a solid line discourages crossing and a double solid line prohibits it."),
  ('Signals', "A signal is installed only when an engineering study shows that at least one warrant is met, such as vehicle volume, pedestrian volume or crash experience. Meeting a warrant allows a signal; it does not require one."),
  ('What every device must do', "Fulfil a need, command attention, convey a clear and simple meaning, command respect from road users and give adequate time for a proper response.")],
 'water-j': [
  ('Drinking water standards', "Under the Safe Drinking Water Act a maximum contaminant level (MCL) is the enforceable limit. The maximum contaminant level goal is a health target that is not enforceable. Primary standards protect health; secondary standards cover taste, odour and appearance."),
  ('Wastewater standards', "Discharges to surface water need a permit under the Clean Water Act's National Pollutant Discharge Elimination System. Secondary treatment is commonly defined as 30 mg/L of BOD_{5} and 30 mg/L of total suspended solids as 30-day averages, with at least 85% removal."),
  ('Routine tests', "Turbidity measures clarity. Total coliform bacteria are used as indicator organisms for contamination. Other routine measures are pH, alkalinity, hardness, chlorine residual, dissolved oxygen, BOD and total suspended solids."),
  ('Sampling', "A grab sample shows conditions at one moment. A composite sample combines portions collected over time and represents the average.")],
 'econ-d': [
  ('Decision trees', "Draw decisions as squares and chance events as circles. Work from the right: at each chance node take the expected value of its branches, and at each decision node keep the best branch."),
  ('Risk is spread, not just average', "Two options with the same expected value can differ in risk. The variance or standard deviation of the outcomes measures that spread, and a risk-averse owner may prefer the option with the lower expected value and the narrower range."),
  ('Sensitivity analysis', "Change one input at a time and see how much the result moves. The inputs that swing the decision are the ones worth estimating more carefully.")],
}
