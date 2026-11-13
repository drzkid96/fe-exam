#!/bin/sh
# Runs every check. Usage: sh tools/check.sh [screenshot dir]
# The browser test needs Chrome and puppeteer-core (set NODE_PATH to its node_modules); it is skipped if they are missing.
set -e
cd "$(dirname "$0")/.."
python3 tools/validate.py
python3 tools/verify_answers.py
node tools/test_core.js
if node -e "require('puppeteer-core')" 2>/dev/null && [ -x /usr/bin/google-chrome ]; then
  FIX=$(mktemp -d)
  mkdir -p "$FIX/content/questions"
  cp site/index.html "$FIX/"; cp site/content/exam.json "$FIX/content/"
  cp tools/fixtures/samples.json "$FIX/content/questions/_samples.json"
  echo '{"sections": []}' > "$FIX/content/reference.json"
  echo '{"version": "fixture", "updated": "", "exam": "content/exam.json", "questions": ["content/questions/_samples.json"], "guide": [], "reference": "content/reference.json"}' > "$FIX/content/manifest.json"
  (cd "$FIX" && python3 -m http.server 8765 >/dev/null 2>&1) & P1=$!
  (cd site && python3 -m http.server 8766 >/dev/null 2>&1) & P2=$!
  trap 'kill $P1 $P2 2>/dev/null; rm -rf "$FIX"' EXIT
  sleep 1
  node tools/smoke_browser.js ${1:-} --real=http://localhost:8766/index.html
else
  echo "browser test skipped (needs Chrome and puppeteer-core)"
fi
echo "ALL CHECKS PASSED"
