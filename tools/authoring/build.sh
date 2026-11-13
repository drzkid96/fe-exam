#!/bin/sh
# Rebuilds all site content from the authoring scripts in this folder, then verifies it.
# Order matters: base questions, version families, handbook lookups, overviews and lessons, figures, examples, depth.
set -e
cd "$(dirname "$0")"
REPO="$(cd ../.. && pwd)"
rm -f "$REPO/tools/calc_expr.json" "$REPO/tools/guide_checks.json" find2.json
for f in author_a author_b author_d1 author_d2 author_n0; do python3 $f.py > /dev/null; done
python3 author_f2.py base
for f in author_v1 author_v2 author_v3 author_v4 author_v5 author_v6 author_v7; do python3 $f.py; done
python3 author_f2.py versions
python3 author_hb.py | tail -1
for f in author_c author_g1 author_g2 author_g3; do python3 $f.py > /dev/null; done
python3 author_fig.py
python3 author_ex.py
python3 author_deep.py
python3 author_rev.py
cd "$REPO" && python3 tools/verify_answers.py | tail -3 && python3 tools/validate.py | tail -1
