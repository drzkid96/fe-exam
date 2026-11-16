# Protocol for Claude

Read this first in any session that works on this repository. It describes the development flow. The owner's study flow is separate: he opens the site and answers questions, and never needs this repository.

## The two flows

| | Study flow | Development flow |
|---|---|---|
| Who | The owner | Claude, at the owner's request |
| Where | The published site | This repository, then a republish |
| Writes | The study log (automatic) | Questions, guide, handbook map, site code |
| Reads | Content | The study log |

The flows meet only at two formats: `schema/question.md` (content going in) and `schema/study-log.md` (attempts coming out). Keep both stable. If either must change, bump the `v` field and keep the site able to read the old shape.

## Where things are

| Thing | Location |
|---|---|
| Published site | https://claude.ai/artifact/FoWz91vEfXDoy7NjWWcfD1 (slug `77dea237-87cd-446f-bb79-eba6189a4878`) |
| Site code | `site/index.html`, one file |
| Exam map | `site/content/exam.json`: 14 topics, 79 subtopics, question ranges, from the NCEES FE Civil specification effective July 2020 |
| Question bank | `site/content/questions/<topic>.json` |
| Study guide | `site/content/guide/<topic>.json` |
| Handbook map and study materials list | `site/content/reference.json` |
| Answer calculations | `tools/verify_answers.py`, `tools/calc_expr.json` (questions) and `tools/guide_checks.json` (lesson examples) |
| Test fixtures | `tools/fixtures/samples.json`: one sample per question format, used only by the tests |
| Study log | The site's database: `sessions/*`, `meta/flags`, `meta/settings` |
| Log snapshots | `snapshots/`: optional dated exports, for history in git |

`site/` mirrors the published files exactly. Paths in the manifest are the published paths.

## Adding or changing content

1. Edit files under `site/content/`. Follow `schema/question.md`.
2. For every calculation question, add a line to `CALC` in `tools/verify_answers.py` that recomputes the answer from the numbers in the stem. Write it from the stem, not from the key.
3. Run `sh tools/check.sh`. It validates the content, recomputes every key, runs the logic tests and, where Chrome is available, the browser tests. Fix every error.
4. Bump `version` and `updated` in `site/content/manifest.json`.
5. Commit, then republish only the changed files to the artifact (patch mode, with the current base version).
6. Never rename or reuse a question id. To retire a question, set `status` to `draft`.

## Content rules

- **Original only.** Every question and every explanation is written for this site. Do not copy or closely paraphrase NCEES material, the reference handbook, the Lindeburg books, the GeniePrep workbook or any other prep material. The owner's copies of those are for reading and for checking facts.
- **Pointers, not excerpts.** Refer to the handbook and the books by section, topic and page. Do not reproduce their text, tables or figures, and do not put links to the files in this repository.
- **Every answer verified.** A calculation question is `computed`: its key is recomputed by `tools/verify_answers.py`, and a multiple-choice distractor may not sit within 1% of the right value. A definition or rule question is `reference` and names its basis. Prefer `computed`.
- **Every question explained twice.** `eli5` gives the idea in plain words with an everyday comparison. `solution` gives the worked steps and says why the tempting wrong answer is wrong.
- **Match the exam.** Both SI and USCS, four options on multiple choice, about three minutes of work, alternative item types mixed in. Keep the bank's topic mix close to the exam's; `tools/validate.py` prints both shares.
- **Look.** The site follows the owner's personal brand: Gill Sans MT only (Arial where it is not installed), headings in capitals, Charcoal text on a warm Ground background, Chaparral green and Manzanita plum as the two highlights, tints and Sand as fills, hairline rules instead of boxes, nothing dark or reversed out. Figures are drawn with working colour names and mapped onto that palette by `tools/authoring/author_fitfig.py`. Gill Sans may lack Greek letters, so name quantities in words. See `schema/question.md`.

## Reading the study log

Query the `sessions` collection of the artifact database, newest first. Each document holds its attempts. `schema/study-log.md` gives the fields and the model rules.

A review session looks at:

- Topics and subtopics with low mastery relative to their exam weight
- Questions missed more than once, and what the wrong responses have in common
- Answers marked sure that were wrong (misconceptions) against answers marked guessing (gaps)
- Time per question against the exam pace of 2:55
- Subtopics with few or no questions left unseen

Then it acts in content: write questions for weak subtopics, add a guide section or a "common mistakes" entry aimed at the observed error, and tell the owner in a few lines what changed and why. Never edit or delete attempts.

## Regenerating content

Questions, lessons and figures are generated by the scripts in `tools/authoring/` (see its README). To change content, edit those scripts, run `sh tools/authoring/build.sh`, then `sh tools/check.sh`. The browser part of the check needs Chrome and `npm install puppeteer-core`, with `NODE_PATH` pointing at its `node_modules`. Bump `site/content/manifest.json` by hand, republish the artifact's changed files and push.

## Resets

Progress can be reset for everything (Setup), for one topic (the topic page) or for one question type (the question page). A reset writes a time to `meta/settings.resets` (`all`, `topics[id]`, `families[id]`, plus a `log` of the last 50 resets) and answers logged before that time stop counting toward mastery, due dates and the missed list. Nothing is deleted, in keeping with the append-only log, and Setup has an undo that clears the marks. When reading the log, apply the same marks before judging weak areas.

## Outside sources

Each topic overview links to free outside material: Mark Mattson's 2022 FE review sessions (video and problem set per topic), the Marshall University FE review lectures, Texas A&M's FE review page and the NCEES specification. These are links only. The lesson text is original and nothing from those sources is copied. Thirteen topic overviews carry a short list of points the instructor stresses in those sessions (all but materials, whose transcript would not load). They were first written in this site's own words after sampling the session transcripts through the owner's browser. In versions 0.8.0 and 0.9.0 all fourteen session transcripts were then read in full. From those notes, 69 lessons gained key ideas and common mistakes, each marked with a `credit` line naming the session, and 47 question families were added for problem types the sessions work and the bank lacked (`tools/authoring/author_f2.py`), on top of the nine added earlier. Nothing is quoted: the notes record methods and cautions, and the lesson text and every problem are written fresh with their own numbers. Where an instructor misspoke or a transcript was garbled, the point was left out rather than guessed. Each list names and links its source. Every outside video link has been opened and its title confirmed.

In the exam the handbook is searched with the search box beside the reference, not with Ctrl+F, so the site says "search the handbook for".

## Handbook reader

The FE Reference Handbook is copyrighted by NCEES and may not be redistributed, so the site and this repository do not contain it. Instead the site reads the student's own copy: the *Handbook* button opens a panel, the student chooses the PDF once, and the browser keeps it (IndexedDB). The panel shows pages with PDF.js 3.11.174 (Apache 2.0, loaded from cdnjs when the reader is first opened), searches the full text, and highlights the search word. Page buttons on every lookup, in answers and lessons, jump to the right page. `site/content/hbindex.json` holds only search words and page numbers. When a copy is loaded, *Explain further with Claude* also receives a short plain-text extract of the page a question points to, so the tutor can cite real page numbers. Run `python3 tools/hb_index.py <handbook.pdf>` after changing search words or moving to a new edition; it lists any word the handbook does not contain.

## Calculator, goals and statistics

The calculator is shown on every question page by default, docked beside the question on a wide screen and as a strip at the bottom on a narrow one (its keypad can be hidden, and *Close* hides it until the next visit). It is a small scientific calculator with its own parser (no `eval`), degree and radian modes, an answer memory and a short history. *Progress* and the dashboard show goals: today and the last seven days against the daily goal, the number of correct answers still needed to make every type secure and the daily pace that implies before the exam date, exam-weighted mastery against a target set in Setup, accuracy and pace for the last seven days against the week before, types not yet tried, and the six weakest subtopics.

## Explain further with Claude

After an answer is checked, and under every lesson, the site shows an *Explain further with Claude* panel: preset requests (step by step, why my answer is wrong, which handbook formula, a similar problem; for lessons: simpler, another example, quiz me, how the exam tests this) and a box for a typed question.

- It uses the artifact's `sample` capability. Claude has no memory between calls, so each call carries the question or lesson, the stored solution, the answer given and the thread so far. The instructions tell it to use the question's numbers, name handbook sections without inventing page numbers, flag a stored solution that looks wrong, and write original material only.
- Replies are live tutoring. They are not part of the checked answer key, and the panel says so.
- Every request is written to `asks/<id>` in the study log (what was asked, on which question or lesson, whether the answer had been correct). Claude reads these with the session log: a cluster of requests on one subtopic is a signal to rewrite that lesson or add questions there.
- The panel is hidden when the capability is absent, for example on a GitHub Pages copy.

## Publishing to GitHub

- The repository holds only original work and public facts (the exam specification's topic names, handbook section names and page ranges). It is safe to make public, but private is the better default while the bank is small.
- Nothing from the study log is stored here unless a snapshot is deliberately exported to `snapshots/`. Do not commit snapshots to a public repository.
- Commit with a GitHub no-reply address so no personal email is published.
- The site also runs as plain static files (for example on GitHub Pages). There it has no database, so progress stays in that browser and Claude cannot read it. The published artifact is the version that tracks progress.

## Goal and status

The owner's goal: the site replaces his reading material and his practice exams. Every subtopic gets a fully built-out lesson and many questions.

- **Content, version 0.13.0:** 2,000 questions in 510 question types, every type with at least three versions (470 types have four numeric versions; 40 rule, judgement, ordering, matching and click-the-figure types have three written versions, the third added in `author_v8.py`). Each numeric type comes from one template whose formula is checked against a separately hand-worked value for its first version; for the newer types the fourth version is derived by averaging two written versions and is kept only if every number in it has the sign and scale of the written ones (`author_fx.py`). 1,906 answers are recomputed by code and 94 are checked against a stated reference. 558 questions carry a drawn figure (140 of the 510 types) and 459 have a figure in the explanation (115 types); force, vector, beam, truss and cross-section types get a free-body, vector, loaded-beam or bending-moment diagram in the solution, and so do pressure, jet, connection, pressure-vessel, soil-strength, slip-circle and tributary-area types (`tools/authoring/fig2.py`). Types whose question already shows the figure, and pure formula or definition types, have none in the explanation. 93 guide sections: one overview per topic and one lesson per subtopic, with 470 worked examples whose final numbers are recomputed.
- **Lessons are exam-first (0.12.0).** Each lesson opens with an exam playbook: a table of the ways the topic shows up on the exam and the fastest move for each (278 rows, written in `tools/authoring/playbook.py`), then every question type in the lesson listed by its actual question line, with the handbook page to open, a target time (about 1 minute for a rule or definition, about 3 for a calculation) and a link that opens that type. Then come the fast method, the formulas with their handbook pages, the worked examples, the traps the wrong answers are built from, and the handbook lookup. The plain-words background (from-zero primer, how it connects, in-depth text, key ideas, terms and symbols) is folded under "Background, if a step above does not make sense". Topic overviews give the topic's share of the exam and the minutes it is worth. Question feedback opens with a fast route (handbook page and search words), then the solution with the numbers, then why it works. The tutor is told to lead with the fastest exam route and explain only as far as needed.
- **Concept figures.** Every lesson has at least one drawing of the idea itself (83 in all, `concept_figs.py`, attached by `author_concept.py`), shown under "Picture it", and every topic overview has a map of how its subtopics connect: a suggested study order, the earlier lessons to refresh first and the later topics that use it. `author_fitfig.py` runs last in the build and keeps every figure label inside its drawing.
- **Symbols:** 1,228 explanations use symbols, and each lists what every symbol stands for (`symbols`); lessons do the same. The meanings live in `tools/authoring/sym_glossary.py`, and `author_sym.py` reports any symbol left undefined (none at this version). A symbol with more than one use (A as an area or an annual amount, for example) is given the one meaning that fits the question, chosen by subtopic and by the question's own wording.
- **Audience:** the reader finished a civil degree about six years ago, works in transportation, and has kept little of statics, mechanics, structures, fluids, water resources or geotechnics. The guide therefore assumes nothing. Each topic overview opens with the topic in plain words, the few ideas everything else hangs on, and how the topic connects to the others. Each of the 79 lessons opens with the idea from zero, links to the lessons it builds on and the lessons that use it (`NEEDS` in `author_me.py`), and lists its technical terms in plain words. 1,201 question explanations list their terms the same way (`plain_terms.py`) and link back one step to the prerequisite lessons. The dashboard suggests a study order that follows those prerequisites, and the tutor instructions say the same: start from the idea, define everything, show every step.
- **Explanations:** every answer shows a *Concept* note (the principle, stated technically) and a *Solution with the numbers* (each step with the question's own values and units). A *Check in the handbook* line follows: the handbook chapter, its page range in edition 10.0.1 and the words to search for in the PDF. 1,720 questions have one; the other 280 are marked as not a handbook lookup and point to the lesson, because the handbook has no entry for them (quantity take-offs, levelling, traffic signal capacity, asphalt mix volumetrics and similar): each was searched for in the handbook text before being left unlinked. Every search word has now been checked against the full handbook (edition 10.0.1): `tools/hb_index.py` reads the owner's PDF and records the printed pages each word appears on in `site/content/hbindex.json`, and words the handbook does not use were replaced with its own wording. Each lookup therefore shows page buttons.
- **Coverage:** all 79 subtopics have a lesson and questions. A full 110-question simulation can be drawn without repeats.
- **Still open.** The lesson examples come from the same templates as the questions, with fresh numbers, so they teach the same methods the bank tests; methods the bank does not test yet are covered only by the lesson text. Every question type now has at least three versions. The primers, topic openers and plain-language term meanings were read through once against the handbook's own definitions at version 0.11.0; they have not been reviewed by a second person.

## Build plan to reach the goal

Work one topic per session, heaviest exam weight first: water, structural, geotechnical, transportation, statics, math, construction, mechanics of materials, fluids, surveying, materials, economics, dynamics, ethics. For each subtopic:

1. Expand the lesson: every item in the specification's "e.g." list explained, each handbook formula it needs, at least three worked examples of rising difficulty, figures as inline SVG where a picture helps, and a short "how the exam asks this" note.
2. Bring the subtopic to at least 10 questions, mixing formats, SI and USCS, and three difficulty levels. Add each calculation to `tools/calc_expr.json` or `CALC`.
3. Run `sh tools/check.sh`, bump the version, commit, republish.
4. Read the study log first and weight the new questions toward what the owner is missing.

## Open items

- **Handbook material:** nothing is copied from the handbook. Formulas are typeset by the site, and lookups give the chapter, page range and search words. The owner can paste a link to their own handbook PDF under Setup; it is stored in `meta/settings` and shown beside every lookup.
- **Handbook edition:** the map follows edition 10.0.1 in the owner's Drive. NCEES has published newer editions; re-map pages when the current one is on hand.
- **Lindeburg chapter map:** pointers are at topic level. The scans' text layer is too rough to read chapter titles reliably. The 2018 manual predates the July 2020 specification.
- **Specification check:** confirm on ncees.org that the July 2020 specification is still in force for the exam date.
- **Formula typesetting:** the built-in rich text covers subscripts, superscripts, fractions and roots. Integrals, summations and matrices would need more. Greek letters are written as words.
