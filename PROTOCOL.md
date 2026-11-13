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
- **Typeface.** The site uses Albert Sans only. It lacks most Greek letters, so name quantities in words. See `schema/question.md`.

## Reading the study log

Query the `sessions` collection of the artifact database, newest first. Each document holds its attempts. `schema/study-log.md` gives the fields and the model rules.

A review session looks at:

- Topics and subtopics with low mastery relative to their exam weight
- Questions missed more than once, and what the wrong responses have in common
- Answers marked sure that were wrong (misconceptions) against answers marked guessing (gaps)
- Time per question against the exam pace of 2:55
- Subtopics with few or no questions left unseen

Then it acts in content: write questions for weak subtopics, add a guide section or a "common mistakes" entry aimed at the observed error, and tell the owner in a few lines what changed and why. Never edit or delete attempts.

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

- **Content, version 0.4.0:** 746 questions in 212 question types. 178 types have four numeric versions each, generated from one template whose formula is checked against the independently written calculation for version 1; 722 answers are recomputed by code and 24 are checked against a stated reference. 210 questions carry a drawn figure and 24 also have a figure in the solution. 93 guide sections: one overview per topic and one lesson per subtopic, 73 with a recomputed worked example and 33 with a figure.
- **Explanations:** every answer shows a *Concept* note (the principle, stated technically) and a *Solution with the numbers* (each step with the question's own values and units). A *Check in the handbook* line follows: the handbook chapter, its page range in edition 10.0.1 and the words to search for in the PDF. 640 questions have one; the other 106 are marked as not a handbook lookup and point to the lesson. Search terms for the chapters after Engineering Probability and Statistics were written from knowledge of the handbook and have not been checked against the PDF, because only the first 84 pages could be read through Drive.
- **Coverage:** all 79 subtopics have a lesson and questions. A full 110-question simulation can be drawn without repeats.
- **Not yet at the goal.** Lessons are one screen each: explanation, key formulas, one example, common mistakes. The 34 question types without versions are the conceptual ones and the multi-select, hotspot, matching and ordering items; they need written variants, not number changes.

## Build plan to reach the goal

Work one topic per session, heaviest exam weight first: water, structural, geotechnical, transportation, statics, math, construction, mechanics of materials, fluids, surveying, materials, economics, dynamics, ethics. For each subtopic:

1. Expand the lesson: every item in the specification's "e.g." list explained, each handbook formula it needs, at least three worked examples of rising difficulty, figures as inline SVG where a picture helps, and a short "how the exam asks this" note.
2. Bring the subtopic to at least 10 questions, mixing formats, SI and USCS, and three difficulty levels. Add each calculation to `tools/calc_expr.json` or `CALC`.
3. Run `sh tools/check.sh`, bump the version, commit, republish.
4. Read the study log first and weight the new questions toward what the owner is missing.

## Open items

- **Handbook edition:** the map follows edition 10.0.1 in the owner's Drive. NCEES has published newer editions; re-map pages when the current one is on hand.
- **Lindeburg chapter map:** pointers are at topic level. The scans' text layer is too rough to read chapter titles reliably. The 2018 manual predates the July 2020 specification.
- **Specification check:** confirm on ncees.org that the July 2020 specification is still in force for the exam date.
- **Formula typesetting:** the built-in rich text covers subscripts, superscripts, fractions and roots. Integrals, summations and matrices would need more. Greek letters are written as words.
