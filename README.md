# FE Civil study site

Source for a personal study site for the NCEES FE Civil exam: a question bank, a study guide and a quiz engine that logs every answer and adapts to it.

- **Site:** https://claude.ai/artifact/FoWz91vEfXDoy7NjWWcfD1
- **To study:** open the site. Nothing here is needed.
- **To develop:** ask Claude to work on this repository. Claude starts with `PROTOCOL.md`.

## Layout

```
PROTOCOL.md          rules for development sessions
site/                the published files, exactly as served
  index.html         the whole site: views, quiz engine, tracking
  content/
    manifest.json    list of content files and the content version
    exam.json        exam map: topics, subtopics, question ranges, formats
    questions/       one file per topic
    guide/           one file per topic
    reference.json   handbook map and study materials list
schema/
  question.md        question, guide and handbook formats
  study-log.md       what the site records and how it scores it
tools/
  check.sh           runs every check below
  validate.py        checks content structure
  verify_answers.py  recomputes every answer key from the question's numbers
  test_core.js       tests grading, scheduling, selection and search
  smoke_browser.js   end-to-end test in headless Chrome
  fixtures/          one sample question per format, for the tests
  scaffold.py        regenerates the exam map and any missing empty files
snapshots/           optional dated exports of the study log
```

## Status

Version 0.4.0. All 79 subtopics of the exam specification have a lesson (explanation, key formulas, worked example, common mistakes; 33 with a figure) and questions. The bank holds 746 original questions in 212 question types; most types come in four numeric versions, and a type counts as secure only after three correct answers on separate, spaced days. Each question has a verified answer, a concept note and a solution worked with its own numbers, and 210 have a drawn figure. On the published artifact, an *Explain further with Claude* panel under each answer and lesson asks Claude for more, with the question and solution as context. `PROTOCOL.md` has the plan for deepening the content.

No text, problems or figures from NCEES or commercial prep books are included. The site points to them by section and page only.
