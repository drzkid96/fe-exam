"""Builds a page index into the owner's copy of the FE Reference Handbook: for every search term the site uses, the printed
page numbers where that term appears. Only terms and page numbers are stored; no handbook text is copied.
Usage: python3 tools/hb_index.py /path/to/fe-handbook.pdf   (needs pdftotext). Writes tools/authoring/hb_pages.json and site/content/hbindex.json."""
import sys, os, re, json, glob, subprocess, collections
HERE = os.path.dirname(os.path.abspath(__file__)); AUTH = os.path.join(HERE, 'authoring'); sys.path.insert(0, AUTH)
# Tables whose headings are not searchable text in the PDF; pages taken from the handbook's own index.
PINNED = {'beam slopes and deflections': [140, 141], 'simply supported beam slopes and deflections': [140], 'cantilevered beam slopes and deflections': [141], 'cantilever': [141]}
OFFSET = 4          # PDF page number minus printed page number, edition 10.0.1
def norm(t): return re.sub(r'\s+', ' ', t.replace('’', "'").replace('‘', "'").replace('–', '-').replace('—', '-').replace('­', '')).lower()
def main(pdf):
    raw = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True).stdout.decode('utf8', 'ignore').split('\f')
    pages = [norm(p) for p in raw]; heads = [(p.strip().split('\n') or [''])[0].strip() for p in raw]
    chapters = collections.OrderedDict()
    for i, h in enumerate(heads):
        if 9 <= i + 1 <= 474 and h and len(h) < 60: chapters.setdefault(h, [i + 1 - OFFSET, i + 1 - OFFSET])[1] = i + 1 - OFFSET
    sys.argv = ['x']; import author_hb
    terms = collections.OrderedDict()
    for v in author_hb.FIND.values():
        for t in author_hb.terms_of(v)[1]: terms[t] = 1
    out, missing = {}, []
    for t in terms:
        hits = PINNED.get(t) or [i + 1 - OFFSET for i, p in enumerate(pages) if 5 <= i + 1 <= 464 and norm(t) in p]
        if hits: out[t] = hits
        else: missing.append(t)
    idx = {'edition': '10.0.1', 'offset': OFFSET, 'numPages': len(pages) - (1 if not pages[-1].strip() else 0), 'terms': out}
    for path in (os.path.join(AUTH, 'hb_pages.json'), os.path.join(HERE, '..', 'site', 'content', 'hbindex.json')):
        json.dump(idx, open(path, 'w'), separators=(',', ':'), ensure_ascii=False); open(path, 'a').write('\n')
    print('terms:', len(terms), 'found:', len(out), 'not found:', len(missing)); print('\n'.join(sorted(missing)))
if __name__ == '__main__': main(sys.argv[1])
