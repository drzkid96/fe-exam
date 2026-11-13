// Tests the pure logic block of site/index.html (grading, learner model, selection, search).
// Run: node tools/test_core.js
const fs = require('fs'), path = require('path'), assert = require('assert');
const root = path.join(__dirname, '..', 'site');
const html = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
const src = html.split('/*CORE-START*/')[1].split('/*CORE-END*/')[0];
const Core = new Function('module', src + '; return module.exports;')({});
const read = p => JSON.parse(fs.readFileSync(path.join(root, p), 'utf8'));
const manifest = read('content/manifest.json'), exam = read(manifest.exam);
const questions = JSON.parse(fs.readFileSync(path.join(__dirname, 'fixtures', 'samples.json'), 'utf8'));   // one sample per question format
const q = id => questions.find(x => x.id === id);
let n = 0; const ok = (c, m) => { assert.ok(c, m); n++; };

// grading, one case right and one wrong per format
ok(Core.grade(q('sample-mcq'), 'b').correct && !Core.grade(q('sample-mcq'), 'a').correct, 'mcq');
ok(Core.grade(q('sample-multi'), ['c', 'a']).correct && !Core.grade(q('sample-multi'), ['a']).correct && !Core.grade(q('sample-multi'), ['a', 'c', 'e']).correct, 'multi needs the exact set');
ok(Core.grade(q('sample-numeric'), '5.04').correct && Core.grade(q('sample-numeric'), ' 5 ').correct && !Core.grade(q('sample-numeric'), '5.2').correct, 'numeric tolerance');
ok(!Core.grade(q('sample-numeric'), 'five').answered && Core.parseNumber('1,250.5') === 1250.5 && Core.parseNumber('2e3') === 2000, 'numeric parsing');
ok(Core.grade(q('sample-hotspot'), {x: 340, y: 77}).correct && !Core.grade(q('sample-hotspot'), {x: 60, y: 80}).correct && !Core.grade(q('sample-hotspot'), {x: 200, y: 20}).correct, 'hotspot regions');
ok(Core.grade(q('sample-match'), {pa: 'stress', j: 'energy', w: 'power'}).correct && !Core.grade(q('sample-match'), {pa: 'stress', j: 'energy', w: 'power', n: 'power'}).correct && !Core.grade(q('sample-match'), {pa: 'energy', j: 'stress', w: 'power'}).correct, 'match with a distractor');
ok(Core.grade(q('sample-order'), ['ft', 'm', 'km', 'mi']).correct && !Core.grade(q('sample-order'), ['km', 'ft', 'mi', 'm']).correct, 'order');
ok(Core.hitRegion([{id: 'p', shape: 'poly', points: [[0, 0], [10, 0], [0, 10]]}], 2, 2) && !Core.hitRegion([{id: 'p', shape: 'poly', points: [[0, 0], [10, 0], [0, 10]]}], 9, 9), 'polygon hit test');

// rich text never passes raw HTML through
ok(!Core.rich('<img onerror=x>').includes('<img') && Core.rich('a_{1}^{2} \\frac{x}{y}').includes('<sub>1</sub>') && Core.rich('- a\n- b').startsWith('<ul>'), 'rich text');

// exam allocation follows the specification and sums exactly
const alloc = Core.allocate(exam, 110);
ok(Object.values(alloc).reduce((a, b) => a + b, 0) === 110, 'allocation sums to 110');
ok(exam.topics.every(t => alloc[t.id] >= t.min && alloc[t.id] <= t.max), 'each topic lands inside its specification range');
ok(Object.values(Core.allocate(exam, 28)).reduce((a, b) => a + b, 0) === 28, 'quarter exam sums');

// learner model
const DAY = Core.DAY, t0 = Date.parse('2026-11-01T18:00:00Z'), iso = ms => new Date(ms).toISOString();
const att = (qid, correct, confidence, at) => { const x = q(qid); return {qid, topic: x.topic, subtopic: x.subtopic, format: x.format, correct, confidence, ms: 60000, at: iso(at), sample: true}; };
const sessions = [{id: 's1', mode: 'adaptive', attempts: [att('sample-mcq', true, 3, t0), att('sample-multi', false, 2, t0 + 1000), att('sample-numeric', true, 1, t0 + 2000)]},
                  {id: 's2', mode: 'adaptive', attempts: [att('sample-mcq', true, 3, t0 + DAY)]}];
let m = Core.buildModel(exam, questions, sessions, t0 + DAY + 1000);
ok(m.totals.n === 4 && m.totals.correct === 3 && m.totals.bank === 6 && m.totals.seen === 3, 'totals');
ok(m.byQ.get('sample-mcq').box === 2 && m.byQ.get('sample-multi').box === 0 && m.byQ.get('sample-numeric').box === 1, 'Leitner boxes: two sure-correct, a miss, a correct guess');
ok(Core.qStatus(m.byQ.get('sample-multi'), t0 + DAY) === 'missed' && Core.qStatus(m.byQ.get('sample-mcq'), t0 + DAY + 1000) === 'learning' && Core.qStatus(undefined, 0) === 'new', 'statuses');
ok(Core.qStatus(m.byQ.get('sample-mcq'), t0 + 5 * DAY) === 'due', 'a box 2 question is due after 3 days');
ok(m.byTopic.math.n === 3 && m.byTopic.math.mastery === 0 && m.totals.weighted === 0 && m.totals.secure === 0, 'answers so far master nothing');
ok(m.totals.streak === 2, 'two-day streak');
// one question answered correctly six times in a minute is still not mastery: promotion needs spaced occasions
const many = [{id: 's3', mode: 'topic', attempts: Array.from({length: 6}, (_, i) => att('sample-mcq', true, 3, t0 + i * 1000))}];
m = Core.buildModel(exam, questions, many, t0 + DAY);
ok(m.byQ.get('sample-mcq').box === 1 && m.bySub['math-a'].secure === 0 && m.byTopic.math.mastery === 0, 'repeating one question in one sitting does not master it');
// three correct answers on spaced days make that one family secure, and the topic is still far from mastered
const spaced = [{id: 's4', mode: 'topic', attempts: [att('sample-mcq', true, 3, t0), att('sample-mcq', true, 3, t0 + 1.1 * DAY), att('sample-mcq', true, 3, t0 + 4.5 * DAY)]}];
m = Core.buildModel(exam, questions, spaced, t0 + 5 * DAY);
ok(m.byQ.get('sample-mcq').box === 3 && Core.qStatus(m.byQ.get('sample-mcq'), t0 + 5 * DAY) === 'strong' && m.bySub['math-a'].mastery === 1, 'three spaced correct answers secure one family');
ok(m.byTopic.math.mastery === 0.5 && m.totals.weighted > 0 && m.totals.weighted < 0.2, 'a topic is only as mastered as the share of its subtopics that are secure');
// versions of one problem share a family: its state is shared, and the next version served is a different one
const vq = ['a', 'b', 'c'].map((x, i) => Object.assign({}, q('sample-mcq'), {id: 'fam-1' + (i ? '-' + x : ''), family: 'fam-1', version: i + 1, versions: 3, sample: undefined}));
const va = (qid, at) => ({qid, family: 'fam-1', topic: 'math', subtopic: 'math-a', format: 'mcq', correct: true, confidence: 3, ms: 1000, at: iso(at)});
m = Core.buildModel(exam, vq, [{id: 's5', mode: 'adaptive', attempts: [va('fam-1', t0)]}], t0 + 2 * DAY);
ok(m.totals.bank === 1 && m.totals.versions === 3 && m.byQ.get('fam-1-b') === m.byQ.get('fam-1') && m.totals.due === 1, 'three versions are one family with shared state');
const nxt = Core.pick({mode: 'due', count: 5}, {pool: m.live, model: m, exam, flags: {}, now: t0 + 2 * DAY, rng: Math.random});
ok(nxt.length === 1 && nxt[0].id !== 'fam-1', 'a due family comes back as a different version');
// sample attempts stop counting once a real question exists
const withReal = questions.concat([{id: 'statics-0001', topic: 'statics', subtopic: 'statics-a', format: 'mcq', status: 'live', stem: 'x', options: [{id: 'a', text: '1'}, {id: 'b', text: '2'}], answer: 'a'}]);
m = Core.buildModel(exam, withReal, sessions, t0 + DAY);
ok(m.totals.n === 0 && m.live.length === 1 && m.totals.bank === 1, 'samples drop out of the model when real questions exist');

// selection
m = Core.buildModel(exam, questions, sessions, t0 + 10 * DAY);
const rng = (() => { let s = 7; return () => (s = (s * 16807) % 2147483647) / 2147483647; })();
const ctx = {pool: m.live, model: m, exam, flags: {'sample-order': {at: 'x'}}, now: t0 + 10 * DAY, rng};
ok(Core.pick({mode: 'missed', count: 10}, ctx).map(x => x.id).join() === 'sample-multi', 'missed mode');
ok(Core.pick({mode: 'flagged', count: 10}, ctx).map(x => x.id).join() === 'sample-order', 'flagged mode');
ok(Core.pick({mode: 'due', count: 10}, ctx).length === 3, 'due mode: all three seen questions are due after 10 days');
let p = Core.pick({mode: 'adaptive', count: 4}, ctx).map(x => x.id);
ok(p.length === 4 && new Set(p).size === 4 && ['sample-mcq', 'sample-multi', 'sample-numeric'].every(id => p.includes(id)), 'adaptive puts due reviews first and never repeats');
ok(Core.pick({mode: 'topic', topics: ['statics'], count: 10}, ctx).every(x => x.topic === 'statics'), 'topic filter');
ok(Core.pick({mode: 'topic', formats: ['order'], count: 10}, ctx).map(x => x.id).join() === 'sample-order', 'format filter');
p = Core.pick({mode: 'exam', count: 6}, ctx);
ok(p.length === 6 && p.every((x, i) => !i || exam.topics.find(t => t.id === p[i - 1].topic).n <= exam.topics.find(t => t.id === x.topic).n), 'exam mode fills from spare questions and keeps specification order');

// search
const idx = Core.buildIndex(exam, questions, {statics: {sections: [{id: 'g1', subtopic: 'statics-d', title: 'Method of joints', body: 'Zero-force members', formulas: [], pitfalls: []}]}}, {sections: []});
ok(Core.search(idx, 'mannin', null)[0].doc.id === 'water-b', 'prefix search finds the Manning subtopic');
ok(Core.search(idx, 'roller support', d => d.type === 'question')[0].doc.id === 'sample-hotspot', 'question search with a type filter');
ok(Core.search(idx, 'joints', null)[0].doc.type === 'guide' && Core.search(idx, 'zzzz', null).length === 0, 'guide search and no-match');
ok(Core.search(idx, '', d => d.topic === 'geotech').length === 12, 'browse by filter alone');
console.log('core tests passed:', n);
