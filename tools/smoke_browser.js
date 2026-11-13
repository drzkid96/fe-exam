// End-to-end smoke test in headless Chrome with a stand-in for the artifact database.
// Run through tools/check.sh, which serves the fixture site on 8765 and the real site on 8766.
const puppeteer = require('puppeteer-core'), assert = require('assert'), path = require('path');
const URL = 'http://localhost:8765/index.html', shots = process.argv.slice(2).find(a => !a.startsWith('--'));
const fakeDb = () => {
  const load = () => JSON.parse(localStorage.getItem('__fakedb') || '{}'), save = s => localStorage.setItem('__fakedb', JSON.stringify(s));
  const snap = (id, d) => ({id, exists: d !== undefined, data: () => d, metadata: {fromCache: false, hasPendingWrites: false}});
  const db = {
    doc: p => ({id: p.split('/').pop(), path: p, get: async () => snap(p.split('/').pop(), load()[p]), set: async d => { if (window.__failWrites) throw {code: 'unavailable', message: 'forced failure'}; const s = load(); s[p] = JSON.parse(JSON.stringify(d)); save(s); }}),
    collection: p => { const q = {orderBy: () => q, limit: () => q, where: () => q, get: async () => { const s = load(); const docs = Object.keys(s).filter(k => k.startsWith(p + '/') && k.split('/').length === p.split('/').length + 1).map(k => snap(k.split('/').pop(), s[k])); return {docs, size: docs.length, empty: !docs.length}; }}; return q; }
  };
  // stand-in for the "sample" capability: streams one partial, then answers; records what it was sent
  const sample = async (input, opts) => { window.__asked = input; if (opts && opts.onText) opts.onText({text: 'Partial', delta: 'Partial'}); await new Promise(r => setTimeout(r, 30)); if (window.__askFail) throw {code: 'rate_limited', message: 'slow down'}; return {text: 'Stub **reply** with \\frac{1}{2}.', truncated: false}; };
  window.claude = {use: async n => n === 'db' ? db : n === 'sample' ? sample : null};
};
(async () => {
  const browser = await puppeteer.launch({executablePath: '/usr/bin/google-chrome', headless: 'new', args: ['--no-sandbox']});
  const page = await browser.newPage(); await page.setViewport({width: 1280, height: 860});
  const errors = []; page.on('pageerror', e => errors.push(String(e))); page.on('console', m => { if (m.type() === 'error' && !/fonts\.g|ERR_|Failed to load resource/.test(m.text())) errors.push(m.text()); });
  await page.evaluateOnNewDocument(fakeDb);
  const status = () => page.$eval('#status span', e => e.textContent);
  const waitSaved = () => page.waitForFunction(() => document.querySelector('#status span').textContent === 'Progress saved', {timeout: 8000});
  const text = () => page.$eval('#view', e => e.innerText);
  const goto = async h => { await page.evaluate(x => { location.hash = x; }, h); await new Promise(r => setTimeout(r, 120)); };
  const click = sel => page.evaluate(s => { const e = document.querySelector(s); if (!e) throw new Error('missing ' + s); e.click(); }, sel);
  let n = 0; const ok = (c, m) => { assert.ok(c, m); n++; };

  await page.goto(URL); await waitSaved();
  ok((await text()).includes('The question bank is empty'), 'dashboard shows the empty-bank note');
  for (const h of ['topics', 'topic-statics', 'topic-water', 'practice', 'search', 'review', 'progress', 'reference', 'setup', 'q-sample-hotspot', 'results', 'quiz', 'home']) {
    await goto(h); ok(!(await text()).includes('This page hit an error'), 'view renders: ' + h);
  }
  ok((await page.$$eval('.side nav a[aria-current]', a => a.length)) === 1, 'one nav item is current');

  // adaptive session over the six format samples; answer the multiple-correct one wrong
  await click('[data-act="quick"][data-mode="adaptive"]'); await new Promise(r => setTimeout(r, 150));
  const seen = [];
  for (let i = 0; i < 6; i++) {
    const q = await page.evaluate(() => { const s = S.session; return S.qById.get(s.qids[s.idx]); });
    seen.push(q.format);
    if (q.format === 'mcq') await click('.opt[data-id="' + q.answer + '"]');
    else if (q.format === 'multi') await click('.opt[data-id="b"]');
    else if (q.format === 'numeric') { await page.type('#num-in', '5.0'); }
    else if (q.format === 'hotspot') { const pt = await page.evaluate(() => { const svg = document.querySelector('#hot-svg'), p = svg.createSVGPoint(); p.x = 340; p.y = 78; const s = p.matrixTransform(svg.getScreenCTM()); return {x: s.x, y: s.y}; }); await page.mouse.click(pt.x, pt.y); }
    else if (q.format === 'match') { for (const [tok, tgt] of Object.entries(q.answer)) if (tgt) { await click('.tok[data-id="' + tok + '"]'); await click('.target[data-id="' + tgt + '"]'); } }
    else if (q.format === 'order') { for (let pass = 0; pass < 12; pass++) { const cur = await page.evaluate(() => { const s = S.session; return s.slots[s.qids[s.idx]].r; }); const bad = q.answer.findIndex((id, k) => cur[k] !== id); if (bad < 0) break; const from = cur.indexOf(q.answer[bad]); await click('.oitem[data-i="' + from + '"] [data-act="up"]'); } }
    await click('[data-act="conf"][data-v="3"]'); await click('#primary');
    const fb = await page.$eval('.fb', e => e.className);
    ok(q.format === 'multi' ? fb.includes('no') : fb.includes('ok'), 'graded ' + q.format + ': ' + fb);
    await click('#primary'); await new Promise(r => setTimeout(r, 120));
  }
  ok(new Set(seen).size === 6, 'all six formats were served');
  ok((await text()).includes('5 of 6 correct'), 'results page score');
  await waitSaved();
  let store = await page.evaluate(() => JSON.parse(localStorage.getItem('__fakedb')));
  let sess = Object.entries(store).filter(([k]) => k.startsWith('sessions/'));
  ok(sess.length === 1 && sess[0][1].attempts.length === 6 && sess[0][1].status === 'done' && sess[0][1].attempts.every(a => a.confidence === 3 && a.sample && a.at && a.ms >= 0), 'session document holds all six attempts');
  ok(await page.evaluate(() => Object.keys(JSON.parse(localStorage.getItem('fe.outbox') || '{}')).length === 0 && !localStorage.getItem('fe.active')), 'outbox is empty and no active session remains');

  // reload: everything comes back from storage
  await page.reload(); await waitSaved(); await goto('home');
  ok(/ANSWERED TODAY\s*6 \/ 20/i.test(await text()), 'dashboard counts today after reload');
  await goto('review'); ok((await text()).includes('Missed (1)'), 'one missed question listed');
  await goto('progress'); ok((await text()).includes('6 answers logged'), 'progress totals');

  // a failed write stays in the outbox, shows in the status, and is sent on retry
  await goto('q-sample-mcq'); await page.evaluate(() => { window.__failWrites = true; });
  await click('.opt[data-id="b"]'); await click('#primary');
  await page.waitForFunction(() => /unsent/.test(document.querySelector('#status span').textContent), {timeout: 9000});
  ok(await page.evaluate(() => Object.keys(JSON.parse(localStorage.getItem('fe.outbox'))).length === 1), 'failed write is held in the outbox');
  await page.reload(); await waitSaved();
  store = await page.evaluate(() => JSON.parse(localStorage.getItem('__fakedb')));
  ok(Object.keys(store).filter(k => k.startsWith('sessions/adhoc-')).length === 1, 'held write was delivered after reload');

  // flag, settings, search
  await goto('q-sample-order'); await click('[data-act="flag"]'); await goto('setup');
  await page.$eval('#set-date', e => { e.value = '2027-03-01'; e.dispatchEvent(new Event('change', {bubbles: true})); }); await waitSaved();
  store = await page.evaluate(() => JSON.parse(localStorage.getItem('__fakedb')));
  ok(store['meta/flags'].items['sample-order'] && store['meta/settings'].examDate === '2027-03-01', 'flags and settings stored');
  await page.type('#gsearch', 'roller'); await page.keyboard.press('Enter'); await new Promise(r => setTimeout(r, 150));
  ok((await text()).includes('point and click') && (await page.$$eval('a.res', a => a.length)) >= 1 && (await page.$$eval('mark', a => a.length)) >= 1, 'search finds and highlights');
  await page.$eval('#s-q', e => { e.value = 'manning'; e.dispatchEvent(new Event('input', {bubbles: true})); });
  ok((await page.$eval('#s-res', e => e.innerText)).includes('Basic hydraulics'), 'live search on topics');

  // exam simulation: answer one, submit, unanswered are scored wrong
  await goto('practice'); await click('[data-act="setMode"][data-mode="exam"]');
  await page.select('#p-len', 'quarter'); await click('[data-act="start"]'); await new Promise(r => setTimeout(r, 150));
  ok(/left/.test(await page.$eval('#clock', e => e.textContent)) && (await page.$$eval('.palette button', b => b.length)) === 6, 'exam mode shows a countdown and the question palette');
  await click('[data-act="next"]'); await click('[data-act="mark"]'); await click('[data-act="prev"]');
  await page.reload(); await waitSaved(); await goto('quiz');
  ok((await page.$$eval('.palette button.mk', b => b.length)) === 1, 'an exam in progress survives a reload');
  await click('.qbar [data-act="askSubmit"]'); await click('#modal-ok'); await new Promise(r => setTimeout(r, 200));
  ok((await text()).includes('0 of 6 correct') && (await text()).includes('Not answered'), 'submitted exam scores unanswered questions as wrong');

  if (shots) {
    await goto('home'); await page.screenshot({path: path.join(shots, 'dashboard.png')});
    await goto('q-sample-match'); await click('.tok[data-id="pa"]'); await click('.target[data-id="stress"]'); await page.screenshot({path: path.join(shots, 'question.png')});
    await page.setViewport({width: 400, height: 800}); await goto('topics'); await page.screenshot({path: path.join(shots, 'mobile.png')});
  }
  // second pass, on the real content: every answer key must grade as correct in the browser, and every page must render
  const real = (process.argv.find(a => a.startsWith('--real=')) || '').slice(7);
  if (real) {
    const p2 = await browser.newPage(); await p2.setViewport({width: 1280, height: 1100});
    p2.on('pageerror', e => errors.push('real: ' + String(e)));
    await p2.evaluateOnNewDocument(fakeDb); await p2.goto(real);
    await p2.waitForFunction(() => typeof S !== 'undefined' && S.exam && S.store.mode === 'cloud', {timeout: 10000});
    const res = await p2.evaluate(() => {
      const bad = [], broke = () => document.querySelector('#view').innerText.includes('This page hit an error'), show = h => { location.hash = h; R = parseRoute(); render(true); return broke(); };
      const mid = g => g.shape === 'rect' ? {x: g.x + g.w / 2, y: g.y + g.h / 2} : g.shape === 'circle' ? {x: g.cx, y: g.cy} : {x: g.points.reduce((s, p) => s + p[0], 0) / g.points.length, y: g.points.reduce((s, p) => s + p[1], 0) / g.points.length};
      for (const q of S.questions) {
        const a = q.answer; let r = a;
        if (q.format === 'numeric') r = String(a.value != null ? a.value : (a.min + a.max) / 2);
        else if (q.format === 'hotspot') r = mid(q.regions.find(g => g.id === (Array.isArray(a) ? a[0] : a)));
        else if (q.format === 'match') { r = {}; Object.keys(a).forEach(k => { if (a[k]) r[k] = a[k]; }); }
        if (!Core.grade(q, r).correct) bad.push(q.id + ': its own key is not graded correct');
        if (q.format === 'hotspot') q.regions.forEach(g => { const hit = Core.hitRegion(q.regions, mid(g).x, mid(g).y); if (!hit || hit.id !== g.id) bad.push(q.id + ': regions overlap at ' + g.id); });
        if (show('q-' + q.id)) bad.push(q.id + ': page error');
      }
      S.exam.topics.forEach(t => { if (show('topic-' + t.id)) bad.push(t.id + ': topic page error'); });
      ['home', 'practice', 'topics', 'review', 'progress', 'reference', 'search', 'setup'].forEach(h => { if (show(h)) bad.push(h + ': page error'); });
      return {bad, n: S.questions.length, real: S.model.real, samples: S.questions.filter(q => q.sample).length};
    });
    ok(res.bad.length === 0, 'real content: ' + res.bad.join(' | '));
    // Explain further with Claude: answer one question, ask, and check the reply, the context sent and the log entry
    await p2.evaluate(() => { location.hash = 'q-statics-0002'; }); await new Promise(r => setTimeout(r, 200));
    await p2.evaluate(() => { document.querySelector('[data-act="opt"]').click(); }); await p2.evaluate(() => { document.querySelector('[data-act="check"]').click(); });
    await new Promise(r => setTimeout(r, 150));
    const ask1 = await p2.evaluate(() => ({on: document.body.classList.contains('has-claude'), box: !!document.querySelector('.ask'), chips: document.querySelectorAll('.ask [data-act="ask"]').length, sfig: !!document.querySelector('.fb .sol svg'), heads: [...document.querySelectorAll('.fb .sol h3')].map(e => e.textContent)}));
    ok(ask1.on && ask1.box && ask1.chips >= 3, 'the Claude panel shows after an answer');
    ok(ask1.sfig && ask1.heads.join('|') === 'Concept|Solution with the numbers|Check in the handbook', 'feedback shows the concept, the calculation and a solution figure');
    ok(await p2.evaluate(() => /Statics<\/strong>, pages 107.113/.test(document.querySelector('.fb').innerHTML) && /equilibrium requirements/.test(document.querySelector('.fb').innerHTML)), 'feedback says where to look in the handbook');
    await p2.evaluate(() => { document.querySelector('.ask [data-act="ask"][data-kind="steps"]').click(); }); await new Promise(r => setTimeout(r, 300));
    const ask2 = await p2.evaluate(() => ({thread: document.querySelector('.ask .ask-thread').innerHTML, sent: window.__asked, logged: Object.keys(JSON.parse(localStorage.getItem('__fakedb') || '{}')).filter(k => k.startsWith('asks/')).length, entry: Object.entries(JSON.parse(localStorage.getItem('__fakedb') || '{}')).filter(e => e[0].startsWith('asks/')).map(e => e[1])[0]}));
    ok(/<strong>reply<\/strong>/.test(ask2.thread) && /frac/.test(ask2.thread) && !/Thinking/.test(ask2.thread), 'the reply is rendered in the thread');
    ok(Array.isArray(ask2.sent) && ask2.sent.length === 1 && /QUESTION statics-0002/.test(ask2.sent[0].content) && /Stored solution/.test(ask2.sent[0].content) && /Student answer/.test(ask2.sent[0].content), 'Claude is sent the question, the solution and the answer given');
    ok(ask2.logged === 1 && ask2.entry.qid === 'statics-0002' && ask2.entry.kind === 'steps' && ask2.entry.on === 'question', 'the request is written to the study log');
    await p2.evaluate(() => { const i = document.querySelector('.ask .ask-in'); i.value = 'Why moments about A?'; document.querySelector('.ask [data-act="askSend"]').click(); }); await new Promise(r => setTimeout(r, 300));
    const ask3 = await p2.evaluate(() => ({n: window.__asked.length, last: window.__asked[window.__asked.length - 1], msgs: document.querySelectorAll('.ask .ask-m').length}));
    ok(ask3.n === 3 && ask3.last.role === 'user' && ask3.last.content === 'Why moments about A?' && ask3.msgs === 4, 'a typed follow-up carries the thread');
    await p2.evaluate(() => { window.__askFail = true; document.querySelector('.ask [data-act="ask"][data-kind="formula"]').click(); }); await new Promise(r => setTimeout(r, 300));
    const ask4 = await p2.evaluate(() => { window.__askFail = false; return {err: (document.querySelector('.ask .ask-err') || {}).textContent || '', busy: document.querySelector('.ask [data-act="askSend"]').disabled}; });
    ok(/busy/.test(ask4.err) && !ask4.busy, 'a refused call shows a message and frees the panel');
    await p2.evaluate(() => { location.hash = 'topic-statics'; }); await new Promise(r => setTimeout(r, 200));
    const ask5 = await p2.evaluate(() => ({lessons: document.querySelectorAll('details.ask').length, figs: document.querySelectorAll('.gsec > figure svg').length}));
    ok(ask5.lessons >= 7 && ask5.figs >= 5, 'lessons carry figures and a Claude panel');
    const les = await p2.evaluate(() => { const t = document.querySelector('#view').textContent; return {ideas: document.querySelectorAll('.idea').length, exs: document.querySelectorAll('.sol.ex').length, exfigs: document.querySelectorAll('.sol.ex svg').length, look: /Check in the handbook/i.test(t) && /Search the handbook for/.test(t), deep: document.querySelectorAll('.deep').length, method: document.querySelectorAll('ol.method li').length, why: document.querySelectorAll('.sol.ex .why').length, links: [...document.querySelectorAll('.gsec a')].filter(a => /youtube\.com|engineeronup|ncees\.org/.test(a.href)).length, num: /Worked example 3/i.test(t)}; });
    ok(les.ideas >= 15 && les.exs >= 20 && les.exfigs >= 8 && les.look && les.num, 'lessons are built out: key ideas, several worked examples with figures, handbook lookup');
    ok(les.deep >= 7 && les.method >= 28 && les.why >= 15 && les.links >= 4, 'lessons have an in-depth explanation, a solving method, example reasoning and outside links');
    await p2.evaluate(() => { location.hash = 'setup'; }); await new Promise(r => setTimeout(r, 200));
    await p2.evaluate(() => { const i = document.querySelector('#set-hb'); i.value = 'https://example.org/handbook.pdf'; i.dispatchEvent(new Event('change', {bubbles: true})); }); await new Promise(r => setTimeout(r, 200));
    await p2.evaluate(() => { location.hash = 'topic-statics'; }); await new Promise(r => setTimeout(r, 200));
    ok(await p2.evaluate(() => [...document.querySelectorAll('.gsec a')].some(a => a.textContent === 'Open my handbook' && a.href === 'https://example.org/handbook.pdf')), 'the saved handbook link shows beside the lookups');
    // resets: answers stop counting but stay in the log, and undo brings them back
    const r0 = await p2.evaluate(() => ({n: S.model.totals.n, raw: S.sessions.reduce((k, s) => k + (s.attempts || []).length, 0)}));
    await p2.evaluate(() => { location.hash = 'topic-statics'; }); await new Promise(r => setTimeout(r, 200));
    await p2.evaluate(() => { document.querySelector('[data-act="askReset"][data-kind="topic"]').click(); }); await p2.evaluate(() => { document.querySelector('#modal-ok').click(); }); await new Promise(r => setTimeout(r, 200));
    const r1 = await p2.evaluate(() => ({n: S.model.totals.n, raw: S.sessions.reduce((k, s) => k + (s.attempts || []).length, 0), mark: !!(S.settings.resets.topics || {}).statics, saved: !!((JSON.parse(localStorage.getItem('__fakedb'))['meta/settings'] || {}).resets || {}).topics.statics}));
    ok(r0.n >= 1 && r1.n === 0 && r1.raw === r0.raw && r1.mark && r1.saved, 'a topic reset clears progress without deleting answers');
    await p2.evaluate(() => { location.hash = 'setup'; }); await new Promise(r => setTimeout(r, 200));
    await p2.evaluate(() => { document.querySelector('[data-act="askUndoReset"]').click(); }); await p2.evaluate(() => { document.querySelector('#modal-ok').click(); }); await new Promise(r => setTimeout(r, 200));
    ok(await p2.evaluate(n => S.model.totals.n === n, r0.n), 'undoing resets brings the answers back');
    await p2.evaluate(() => { document.querySelector('[data-act="askReset"][data-kind="all"]').click(); }); await p2.evaluate(() => { document.querySelector('#modal-ok').click(); }); await new Promise(r => setTimeout(r, 200));
    ok(await p2.evaluate(() => S.model.totals.n === 0 && !!S.settings.resets.all), 'resetting everything gives a clean start');
    ok(res.n > 0 && res.real && res.samples === 0, 'real content is loaded and no samples remain');
    console.log('real content checked:', res.n, 'questions');
    if (shots) {
      await p2.evaluate(() => { location.hash = 'q-mechmat-0007'; }); await new Promise(r => setTimeout(r, 200));
      const pt = await p2.evaluate(() => { const svg = document.querySelector('#hot-svg'), p = svg.createSVGPoint(); p.x = 200; p.y = 70; const s = p.matrixTransform(svg.getScreenCTM()); return {x: s.x, y: s.y}; });
      await p2.mouse.click(pt.x, pt.y); await p2.evaluate(() => document.querySelector('#primary').click()); await new Promise(r => setTimeout(r, 200));
      await p2.screenshot({path: path.join(shots, 'real_question.png')});
      await p2.evaluate(() => { S.ui.open = 'geotech-d'; location.hash = 'topic-geotech'; }); await new Promise(r => setTimeout(r, 200)); await p2.screenshot({path: path.join(shots, 'real_topic.png')});
    }
  }
  ok(errors.length === 0, 'no page errors: ' + errors.join(' | '));
  console.log('browser smoke test passed:', n);
  await browser.close();
})().catch(e => { console.error('FAILED:', e.message || e); process.exit(1); });
