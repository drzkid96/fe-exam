# Study log format

The study log lives in the site's own database, not in this repository. The site writes it; Claude reads it. Nothing in the study flow touches GitHub.

## Documents

| Path | Written when | Contents |
|---|---|---|
| `sessions/<id>` | After every checked answer, and again when the session ends | One study session with its attempts |
| `meta/flags` | A question is flagged or unflagged | `{items: {questionId: {at}}}` |
| `meta/settings` | A setting changes | `{examDate, dailyGoal, sessionLength}` |
| `asks/<id>` | *Explain further with Claude* is used | `{id, at, kind, prompt, on: "question" or "lesson", qid, family, topic, subtopic, correct}` or `{..., lesson}`. `kind` is the preset (`steps`, `wrong`, `formula`, `similar`, `simpler`, `example`, `quiz`, `exam`) or `own` for a typed question. Claude's reply is not stored. |

Only the site owner can read or write these documents.

## Session document

```json
{
  "v": 1,
  "id": "s-20261113-121455-k3fa",
  "mode": "adaptive",
  "config": {"mode": "adaptive", "topics": [], "subtopics": [], "formats": [], "count": 10},
  "startedAt": "2026-11-13T20:14:55.000Z",
  "endedAt": "2026-11-13T20:31:02.000Z",
  "status": "done",
  "planned": 10,
  "contentVersion": "0.1.0-structure",
  "attempts": []
}
```

`mode` is `adaptive`, `topic`, `exam`, `missed`, `due`, `flagged` or `single`. Single-question answers from search and review collect in documents named `adhoc-<date>-<suffix>`. `status` is `active` while a session is under way and `done` after. `planned` larger than the number of attempts means the session ended early.

## Attempt

```json
{
  "qid": "statics-0007",
  "topic": "statics",
  "subtopic": "statics-d",
  "format": "numeric",
  "correct": false,
  "response": "12.4",
  "ms": 201345,
  "confidence": 3,
  "at": "2026-11-13T20:18:10.000Z"
}
```

| Field | Notes |
|---|---|
| `response` | What was entered: option id, array of ids, typed text, `{x, y}`, `{token: target}` or an ordered array |
| `ms` | Time the question was on screen, paused while the tab was hidden |
| `confidence` | 0 not rated, 1 guessing, 2 unsure, 3 sure |
| `skipped` | Present and true for an exam-simulation question left blank (scored wrong) |
| `sample` | Present and true for the format samples; ignored once real questions exist |

Attempts are only ever appended. Everything else the site shows (mastery, due dates, streaks) is recomputed from them on every load.

## How the site turns the log into a learner model

| Figure | Rule |
|---|---|
| Review schedule | Leitner boxes 0 to 5 with intervals of 0, 1, 3, 7, 14 and 30 days. Wrong: back to box 0. Correct: up one box. Correct but marked as a guess: no promotion. |
| Topic mastery | Exponentially weighted accuracy, newest answer weighted 0.2. A correct guess counts 0.7. Shown after 5 answers in the topic. |
| Weighted accuracy | Topic mastery averaged by exam weight (midpoint of each topic's question range), over topics that have a mastery figure. |
| Adaptive session | Up to 60% due reviews, oldest first. The rest are unseen questions drawn with odds proportional to exam weight times (1.05 minus mastery). |
| Exam simulation | Questions split across topics in proportion to the specification, in specification order, timed at 320 minutes per 110 questions. |

These rules live in the `Core` block of `site/index.html` and are covered by `tools/test_core.js`.
