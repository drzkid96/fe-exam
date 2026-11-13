"""One-time scaffold: writes the FE Civil exam map and empty content files. Safe to re-run; never overwrites question or guide files that already hold content."""
import json, os, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site", "content")
SPEC = [
 ("math","Mathematics and Statistics",8,12,["Analytic geometry","Single-variable calculus","Vector operations","Statistics (e.g., distributions, mean, mode, standard deviation, confidence interval, regression and curve fitting)"]),
 ("ethics","Ethics and Professional Practice",4,6,["Codes of ethics (professional and technical societies)","Professional liability","Licensure","Contracts and contract law"]),
 ("econ","Engineering Economics",5,8,["Time value of money (e.g., equivalence, present worth, equivalent annual worth, future worth, rate of return)","Cost (e.g., fixed, variable, direct and indirect labor, incremental, average, sunk)","Analyses (e.g., break-even, benefit-cost, life cycle, sustainability, renewable energy)","Uncertainty (e.g., expected value and risk)"]),
 ("statics","Statics",8,12,["Resultants of force systems","Equivalent force systems","Equilibrium of rigid bodies","Frames and trusses","Centroid of area","Area moments of inertia","Static friction"]),
 ("dynamics","Dynamics",4,6,["Kinematics (e.g., particles, rigid bodies)","Mass moments of inertia","Force acceleration (e.g., particles, rigid bodies)","Work, energy, and power (e.g., particles, rigid bodies)"]),
 ("mechmat","Mechanics of Materials",7,11,["Shear and moment diagrams","Stresses and strains (e.g., diagrams, axial, torsion, bending, shear, thermal)","Deformations (e.g., axial, torsion, bending, thermal)","Combined stresses, principal stresses, and Mohr's circle"]),
 ("materials","Materials",5,8,["Mix design of concrete and asphalt","Test methods and specifications of metals, concrete, aggregates, asphalt, and wood","Physical and mechanical properties of metals, concrete, aggregates, asphalt, and wood"]),
 ("fluids","Fluid Mechanics",6,9,["Flow measurement","Fluid properties","Fluid statics","Energy, impulse, and momentum of fluids"]),
 ("surveying","Surveying",6,9,["Angles, distances, and trigonometry","Area computations","Earthwork and volume computations","Coordinate systems (e.g., state plane, latitude/longitude)","Leveling (e.g., differential, elevations, percent grades)"]),
 ("water","Water Resources and Environmental Engineering",10,15,["Basic hydrology (e.g., infiltration, rainfall, runoff, watersheds)","Basic hydraulics (e.g., Manning equation, Bernoulli theorem, open-channel flow)","Pumps","Water distribution systems","Flood control (e.g., dams, routing, spillways)","Stormwater (e.g., detention, routing, quality)","Collection systems (e.g., wastewater, stormwater)","Groundwater (e.g., flow, wells, drawdown)","Water quality (e.g., ground and surface, basic water chemistry)","Testing and standards (e.g., water, wastewater, air, noise)","Water and wastewater treatment (e.g., biological processes, softening, drinking water treatment)"]),
 ("structural","Structural Engineering",10,15,["Analysis of statically determinant beams, columns, trusses, and frames","Deflection of statically determinant beams, trusses, and frames","Column analysis (e.g., buckling, boundary conditions)","Structural determinacy and stability analysis of beams, trusses, and frames","Elementary statically indeterminate structures","Loads, load combinations, and load paths (e.g., dead, live, lateral, influence lines and moving loads, tributary areas)","Design of steel components (e.g., codes and design philosophies, beams, columns, tension members, connections)","Design of reinforced concrete components (e.g., codes and design philosophies, beams, columns)"]),
 ("geotech","Geotechnical Engineering",10,15,["Index properties and soil classifications","Phase relations","Laboratory and field tests","Effective stress","Stability of retaining structures (e.g., active/passive/at-rest pressure)","Shear strength","Bearing capacity","Foundation types (e.g., spread footings, deep foundations, wall footings, mats)","Consolidation and differential settlement","Slope stability (e.g., fills, embankments, cuts, dams)","Soil stabilization (e.g., chemical additives, geosynthetics)"]),
 ("transport","Transportation Engineering",9,14,["Geometric design (e.g., streets, highways, intersections)","Pavement system design (e.g., thickness, subgrade, drainage, rehabilitation)","Traffic capacity and flow theory","Traffic control devices","Transportation planning (e.g., travel forecast modeling, safety, trip generation)"]),
 ("construction","Construction Engineering",8,12,["Project administration (e.g., documents, management, procurement, project delivery methods)","Construction operations and methods (e.g., safety, equipment, productivity analysis, temporary erosion control)","Project controls (e.g., earned value, scheduling, allocation of resources, activity relationships)","Construction estimating","Interpretation of engineering drawings"]),
]
def w(path, data, keep=False):
    p = os.path.join(ROOT, path)
    if keep and os.path.exists(p): return
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w") as f: json.dump(data, f, indent=1, ensure_ascii=False); f.write("\n")
topics = []
for n, (tid, name, lo, hi, subs) in enumerate(SPEC, 1):
    topics.append({"id": tid, "n": n, "name": name, "min": lo, "max": hi,
                   "subtopics": [{"id": f"{tid}-{chr(97+i)}", "code": chr(65+i), "name": s} for i, s in enumerate(subs)]})
    w(f"questions/{tid}.json", [], keep=True)
    w(f"guide/{tid}.json", {"topic": tid, "sections": []}, keep=True)
w("exam.json", {
 "id": "fe-civil", "name": "FE Civil",
 "spec": "NCEES FE Civil CBT exam specifications, effective July 2020",
 "specSource": "https://ncees.org/exams/fe-exam/",
 "questionCount": 110, "examMinutes": 320, "appointmentMinutes": 360,
 "units": ["SI", "USCS"],
 "formats": [
  {"id": "mcq", "label": "Multiple choice", "exam": "Multiple choice, one correct answer"},
  {"id": "multi", "label": "Multiple correct", "exam": "Alternative item type: multiple correct"},
  {"id": "numeric", "label": "Fill in the blank", "exam": "Alternative item type: fill in the blank"},
  {"id": "hotspot", "label": "Point and click", "exam": "Alternative item type: point and click"},
  {"id": "match", "label": "Drag and drop: match", "exam": "Alternative item type: drag and drop"},
  {"id": "order", "label": "Drag and drop: rank", "exam": "Alternative item type: drag and drop"}],
 "topics": topics})
w("reference.json", {"handbook": {"title": "NCEES FE Reference Handbook", "edition": "", "note": ""}, "sections": []}, keep=True)
w("manifest.json", {"version": "0.1.0-structure", "updated": "2026-11-13", "exam": "content/exam.json",
 "questions": ["content/questions/_samples.json"] + [f"content/questions/{t['id']}.json" for t in topics],
 "guide": [f"content/guide/{t['id']}.json" for t in topics], "reference": "content/reference.json"})
print(len(topics), "topics,", sum(len(t["subtopics"]) for t in topics), "subtopics, midpoint sum", sum((t["min"]+t["max"])/2 for t in topics))
