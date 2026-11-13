# Question format

One JSON object per question, stored in `site/content/questions/<topic>.json` (an array). `tools/validate.py` enforces everything below.

## Fields every question has

| Field | Type | Notes |
|---|---|---|
| `id` | string | `<topic>-<4 digits>`, for example `statics-0007`. Letters, digits and hyphens only. Never reuse or change an id: the study log refers to it. |
| `topic` | string | A topic id from `exam.json`, for example `statics`. |
| `subtopic` | string | A subtopic id under that topic, for example `statics-d`. |
| `format` | string | `mcq`, `multi`, `numeric`, `hotspot`, `match` or `order`. |
| `status` | string | `live` or `draft`. Drafts are never served. |
| `difficulty` | 1, 2 or 3 | 2 is exam level. |
| `units` | `"SI"`, `"USCS"` or null | The exam uses both. |
| `stem` | rich text | The question. |
| `figure` | object or null | `{viewBox, svg, alt, caption}` for an inline drawing, or `{src, alt, caption}` for a file under `content/figures/`. |
| `answer` | varies | See each format. |
| `eli5` | rich text | The idea in plain words, one or two sentences, with an everyday comparison. Shown before the worked solution. Required. |
| `solution` | rich text | Worked solution shown after answering. Required. |
| `verify` | object | `{method: "computed"}` when `tools/verify_answers.py` recomputes the key from the numbers in the stem. `{method: "reference", basis: "..."}` when the answer is a definition or a rule; `basis` names the source. Required. |
| `handbook` | array | `[{section, page}]`: where the needed formula sits in the reference handbook. |
| `tags` | array of strings | Searchable keywords. |
| `source` | string | `original`. Questions are written for this site, never copied. |

## Format-specific fields

| Format | Exam item type | Extra fields | `answer` |
|---|---|---|---|
| `mcq` | Multiple choice | `options: [{id, text}]`, four of them | One option id |
| `multi` | Multiple correct | `options`, optional `selectCount` | Array of option ids. Scored right only when the whole set matches. |
| `numeric` | Fill in the blank | none | `{value, tolerance, toleranceType, unit}`. `toleranceType` is `rel` (default, fraction of the value) or `abs`. Or `{min, max, unit}`. |
| `hotspot` | Point and click | `figure` with `svg`; `regions: [{id, label, shape, ...}]` with `rect` (`x y w h`), `circle` (`cx cy r`) or `poly` (`points: [[x, y], ...]`) in viewBox units | One region id, or an array of accepted ids |
| `match` | Drag and drop | `tokens: [{id, text}]`, `targets: [{id, label, multi}]` | `{tokenId: targetId or null}`. Null marks a distractor that stays unplaced. |
| `order` | Drag and drop | `items: [{id, text}]`, listed in scrambled order | Array of item ids in the correct order |

## Rich text

Albert Sans has no sigma, tau, rho, gamma, phi or theta, so name those quantities in words ("stress", "friction angle") instead of using the symbols. Delta, mu, pi and omega are available.

Plain text plus: `**bold**`, `*italic*`, `` `code` ``, `x_{sub}`, `x^{sup}`, `\frac{a}{b}`, `\sqrt{x}`, blank line for a new paragraph, lines starting with `- ` for a list. HTML is escaped, not rendered.

## Guide sections

`site/content/guide/<topic>.json` holds `{topic, sections: [...]}`. Each section: `{id, subtopic, title, body, formulas: [{name, expr, handbook}], pitfalls: [string], read: [{source, where}], updated}`. `body`, `expr` and pitfalls are rich text. A section with `subtopic: null` is the topic overview and shows at the top of the topic page. `read` points into the study materials by name, never by link.

## Handbook map

`site/content/reference.json` holds `{handbook: {title, edition, note}, sections: [{id, title, topics: [topic ids], pages, notes}], sources: [{title, file, use, note}]}`. `sources` lists the owner's own study materials by file name.
