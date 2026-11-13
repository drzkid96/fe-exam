"""Builds each lesson out into a full guide: key ideas, several worked examples with figures (fresh numbers, not used in the
question bank), and a handbook lookup. Reuses the checked question templates. Run after author_fig.py."""
import json, os, re
import author_v; author_v.DRY[0] = True
import author_v1, author_v2, author_v3, author_v4
from author_v import TEMPLATES, NAMES, render, nf, _load
from author_common import ROOT
from author_hb import FIND
EXS, CHECKS = {}, {}
def E(base, **p):
    t = TEMPLATES[base]; b = next(x for x in _load(base.rsplit('-', 1)[0]) if x['id'] == base)
    env = dict(NAMES); env.update(p); val = eval(t['ans'], {'__builtins__': {}}, env); env['ans'] = val; dp = t.get('dp')
    if b['format'] == 'numeric':
        u = b['answer'].get('unit') or ''; ans = ('$' + nf(val, dp) + u[1:]) if u.startswith('$') else (nf(val, dp) + ' ' + u).strip()
    else:
        m = re.match(r'^(\$?)(-?[\d,]*\.?\d+)(.*)$', next(o['text'] for o in b['options'] if o['id'] == b['answer'])); ans = m.group(1) + nf(val, dp) + m.group(3)
    ex = {'family': base, 'problem': render(t['stem'], env), 'idea': render(t['eli5'], env) if t.get('eli5') else '', 'steps': render(t['sol'], env), 'answer': ans, 'value': round(val, 6)}
    f = t.get('sfig') or t.get('fig')
    if f: ex['figure'] = f(env)
    EXS.setdefault(b['subtopic'], []).append(ex)
    CHECKS[f"{b['subtopic']}-lesson#{base}"] = {'expr': f"(lambda {', '.join(p)}: {t['ans']})({', '.join(repr(v) for v in p.values())})", 'value': round(val, 6)}
S = 'statics-'; D = 'dynamics-'; MM = 'mechmat-'; ST = 'structural-'; G = 'geotech-'; FL = 'fluids-'; SV = 'surveying-'; TR = 'transport-'; W = 'water-'; EC = 'econ-'; MT = 'materials-'; MA = 'math-'; C = 'construction-'
E(S+'0001', F1=140, F2=75, th=50); E(S+'0002', L=12, P=48, a=3); E(S+'0003', bf=160, tf=25, tw=25, hw=150); E(S+'0004', mu=0.45); E(S+'0005', b=180, h=360); E(S+'0006', Fc=150, d=0.3); E(S+'0007', Fc=320, d=0.45)
E(S+'0008', span=16, h=6, P=60); E(S+'0009', span=16, h=6, P=60); E(S+'0010', Fa=250, L=1.2, th=50); E(S+'0011', L=9, w=8, P=36); E(S+'0012', t=25, H=120, B=75); E(S+'0013', b=90, h=180); E(S+'0014', W=1000, mu=0.30, th=15); E(S+'0015', W=1500, th=45)
E(D+'0001', v=36, t=10); E(D+'0002', m=120, Fp=700, mu=0.35); E(D+'0003', m=4, h=30); E(D+'0004', m=15, L=3); E(D+'0005', v=40, th=45); E(D+'0006', v=18, r=90); E(D+'0007', m=30, r=0.25); E(D+'0008', th=35); E(D+'0009', Tq=60, I=8); E(D+'0010', m=2000, v=1.2); E(D+'0011', k=3000, x=0.12, m=1.5)
E(MM+'0001', d=32, P=150); E(MM+'0002', d=32, L=5, P=150, E=200); E(MM+'0003', L=12, w=15); E(MM+'0004', sx=60, sy=-60, txy=80); E(MM+'0005', b=250, h=500, M=250); E(MM+'0008', L=12, w=15); E(MM+'0009', d=75, Tq=6); E(MM+'0010', al=12, dT=75, E=200); E(MM+'0011', L=30, dT=45, al=12); E(MM+'0012', s1=140, s2=80); E(MM+'0013', r=900, t=18, p=1.6)
E(ST+'0002', L=8, I=50); E(ST+'0003', L=10, P=50, EI=80000); E(ST+'0004', D=25, Lv=35); E(ST+'0005', b=320, d=560, As=1800, fc=30); E(ST+'0006', L=3.5, P=24); E(ST+'0007', L=12, w=3, P=30, a=4); E(ST+'0008', L=12, P=50); E(ST+'0009', L=3.5, P=12, EI=30000); E(ST+'0010', L=7)
E(ST+'0012', L=10, w=12); E(ST+'0013', L=9, w=16); E(ST+'0014', s=3.5, q=4.8); E(ST+'0015', Ag=2800, Fy=345); E(ST+'0016', Z=1.8, Fy=345); E(ST+'0017', L=7.5, r=60); E(ST+'0018', b=320, As=1800, fc=30); E(ST+'0019', b=320, d=560, fc=30); E(ST+'0020', sd0=550, Ast=6000, fc=35)
E(G+'0001', M=2.10, wc=15); E(G+'0002', rd=1700, Gs=2.72); E(G+'0003', g1=18.5, g2=20, zw=2.5, z=7); E(G+'0004', phi=32); E(G+'0005', c=20, sn=120, phi=25); E(G+'0006', LL=48, PL=21); E(G+'0009', D60=1.8, D30=0.6, D10=0.15); E(G+'0010', fd=17.9, mx=18.6); E(G+'0011', Q=720, t=300, L=18, A=40, h=45)
E(G+'0012', H=7, gam=18.5, Ka=0.307); E(G+'0013', qu=96); E(G+'0014', c=60, D=1.8, gam=18.5); E(G+'0015', P=1500, qu=480, FS=3); E(G+'0016', s=0.5, L=20, fs=45, qp=2200); E(G+'0018', H=8, Cc=0.32, e0=0.9, p1=140, p2=280); E(G+'0019', H=10, cv=2.5); E(G+'0020', b=22, phi=34); E(G+'0021', R=18, La=25, su=35, W=1800, x=5.5); E(G+'0023', pct=4.5, rd=1750, Vol=600)
E(FL+'0001', h=15); E(FL+'0002', SG=0.88); E(FL+'0003', v=2.4, d1=250, d2=125); E(FL+'0004', h=0.60); E(FL+'0005', b=2.5, h=3.6); E(FL+'0006', d=60, h=4, Cd=0.61); E(FL+'0007', v=2.5, d=200, nu=1.0); E(FL+'0008', mu=0.0018, rho=900); E(FL+'0009', h=0.25); E(FL+'0010', Vb=1.5, SG=0.70); E(FL+'0011', u1=2.5, u2=7.5, p1=220); E(FL+'0012', d=80, v=18); E(FL+'0013', v=1.8, L=300, d=250, f=0.02)
E(SV+'0001', BM=75.50, bs=1.84, fs=2.96); E(SV+'0002', bx=70, cx=100, cy=60, dx=20, dy=80); E(SV+'0003', L=30, A1=28, A2=44); E(SV+'0005', e1=150.0, e2=162.6, d=360); E(SV+'0006', S=412.6, va=9); E(SV+'0007', n=7, name='seven'); E(SV+'0008', sa=150, sb=95, C=64); E(SV+'0009', pa=30, pb=45, dc=2.2); E(SV+'0010', L=264.5, az=48); E(SV+'0011', N0=3200, L=145, br=35)
E(TR+'0001', V=55); E(TR+'0002', V=65, e=6, f=0.11); E(TR+'0003', k=48, u=42); E(TR+'0004', Vh=1500, V15=420); E(TR+'0005', g1=2.5, g2=3.5, L=720); E(TR+'0007', D1=5, D2=10, D3=8); E(TR+'0008', CBR=7); E(TR+'0009', dly=950, n=20); E(TR+'0010', N=3, s=1850, gr=45, C=110)
E(TR+'0011', uf=65, kj=140); E(TR+'0012', mph=52.5, fps=77); E(TR+'0013', n=320, rate=8.5); E(TR+'0014', cr=15, adt=27500); E(TR+'0015', Ua=-0.4, Ub=-1.3); E(TR+'0016', R=1200, D=36); E(TR+'0017', R=1200, D=36); E(TR+'0018', g1=2.5, g2=1.5, K=114)
E(W+'0001', A=18, C=0.70, i=2.8); E(W+'0002', b=3.5, y=1.2, S=0.0012, n=0.014); E(W+'0003', Q=0.10, H=36, eff=78); E(W+'0004', Vt=2700, Q=14400); E(W+'0005', K=20, i=0.006, A=1200); E(W+'0007', CN=75, P=6.0); E(W+'0008', q=2.5); E(W+'0009', Q1=150, N1=1150, N2=1750); E(W+'0010', pop=60000, lpcd=380, pf=1.7); E(W+'0011', h=46); E(W+'0012', T=100, n=50)
E(W+'0013', T=500); E(W+'0014', qi=4.2, qo=1.6, t=25); E(W+'0015', C1=0.35, C2=0.75); E(W+'0016', D=375, S=0.004); E(W+'0017', pop=20000, lpcd=320, pf=2.8); E(W+'0018', K=30, i=0.005, n=0.25); E(W+'0019', Vs=8, DOi=8.4, DOf=3.2); E(W+'0020', Ca=70, Mg=20); E(W+'0021', n=5, nw='Five', Ls=85); E(W+'0023', Q=15000, A=420); E(W+'0024', Q=36000, dose=2.5)
E(EC+'0001', P=15000, i=4, n=8); E(EC+'0002', P=80000, i=7, n=8, nw='eight'); E(EC+'0003', FC=200000, vc=45, pr=70); E(EC+'0004', p1=15, Ls=60000, p2=55, G1=35000, G2=110000); E(EC+'0005', FC=75000, vc=14, n=15000); E(EC+'0006', h=80, r=45, m=1800, oh=45); E(EC+'0007', Fv=40000, i=7, n=8); E(EC+'0008', r=8, m=4, per='quarterly')
E(EC+'0009', C0=750000, Mc=25000, B=110000, i=6, n=30); E(EC+'0010', P=60000, Oc=4000, Sv=8000, n=10, i=9)
E(MT+'0001', W=175, C=390); E(MT+'0002', d=150, P=710); E(MT+'0004', st=150, eps=0.00075); E(MT+'0005', m=380); E(MT+'0006', tot=1250, bn=65); E(MT+'0009', fc=40); E(MT+'0010', L0=50, Lf=61)
E(MA+'0001', x1=4, y1=7, x2=10, y2=4); E(MA+'0002', a=9, b=2); E(MA+'0004', data=[4, 7, 9, 12, 18]); E(MA+'0006', D=-10, E=24, tx='- 10x', ty='+ 24y'); E(MA+'0007', x1=-2, y1=1, x2=10, y2=6); E(MA+'0008', sa=12, sb=15, C=50); E(MA+'0009', k=5, x0=4); E(MA+'0010', a=4, b=24, c=-6, cs='- 6')
E(MA+'0011', a=5, b=3, tt=4); E(MA+'0012', a1=6, a2=-1, b1=2, b2=5); E(MA+'0013', a1=2, a2=3, a3=-6); E(MA+'0015', mu=35, sv=5, x=42.5); E(MA+'0016', y1=4, y2=5, y3=9); E(MA+'0017', p=0.12, n=7)
E(C+'0001', dA=4, dB=5, dC=12, dD=3); E(C+'0002', PV=600000, EV=540000, AC=580000); E(C+'0003', L=40, W=25, t=175, ws=7); E(C+'0004', bk=2.5, ct=36, mn=50); E(C+'0006', sc=30, ms=4.75); E(C+'0007', sc=200, mm=47); E(C+'0011', nr=5, hrs=310000); E(C+'0012', tl=5, tc=35); E(C+'0014', rt=45, ar=1620, cw=3); E(C+'0015', qy=1600, uc=11.5, mk=16); E(C+'0016', L=32, H=4.5)

# key ideas: the concept note of every question type in the subtopic, titled by its handbook search word
IDEAS, LOOK = {}, {}
for f in sorted(os.listdir(os.path.join(ROOT, 'questions'))):
    for q in json.load(open(os.path.join(ROOT, 'questions', f))):
        if q.get('version', 1) != 1: continue
        base = q.get('family') or q['id']; v = FIND.get(base, '-')
        if base in TEMPLATES:
            title = v.split('::')[-1].split(';')[0].strip() if v != '-' else ''
            IDEAS.setdefault(q['subtopic'], []).append({'title': title[:1].upper() + title[1:], 'text': q['eli5']})
        for h in q.get('handbook', []):
            if h.get('find'): LOOK.setdefault(q['subtopic'], {}).setdefault((h['section'], h['page']), []).extend(x for x in h['find'] if x not in LOOK[q['subtopic']][(h['section'], h['page'])])
try: from author_depth import MANUAL
except ImportError: MANUAL = {}
n = ni = 0; thin = []
for f in sorted(os.listdir(os.path.join(ROOT, 'guide'))):
    path = os.path.join(ROOT, 'guide', f); g = json.load(open(path))
    for s in g['sections']:
        sub = s.get('subtopic')
        if not sub: continue
        ideas = [{'title': a, 'text': b.replace(' || ', '\n\n')} for a, b in MANUAL.get(sub, [])] + IDEAS.get(sub, [])
        s['ideas'] = ideas; s['examples'] = EXS.get(sub, []); n += len(s['examples']); ni += len(ideas)
        s['lookup'] = [{'section': k[0], 'page': k[1], 'find': v} for k, v in LOOK.get(sub, {}).items()]
        if len(ideas) < 2 or (not s['examples'] and len(ideas) < 3): thin.append(f"{sub}({len(ideas)} ideas, {len(s['examples'])} ex)")
    json.dump(g, open(path, 'w'), indent=1, ensure_ascii=False); open(path, 'a').write('\n')
path = __import__('os').environ.get('FE_REPO', __import__('os').path.abspath(__import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))) + '/tools/guide_checks.json'; allc = json.load(open(path)); allc.update(CHECKS)
json.dump(dict(sorted(allc.items())), open(path, 'w'), indent=1); open(path, 'a').write('\n')
print('lesson examples added:', n, 'key ideas:', ni); print('thin:', ' '.join(thin))
