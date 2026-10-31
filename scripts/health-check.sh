#!/usr/bin/env bash
# 搜索栈健康检查：Firecrawl / SearXNG / RSSHub。不读取、不输出任何密钥。
SEARX=${SEARX_URL:-http://127.0.0.1:8888}
RSS=${RSSHUB_URL:-http://127.0.0.1:1200}
ROUTE=${RSSHUB_ROUTE:-/zhihu/hot}
fail=0; summary=()
echo "== health-check $(date '+%F %T %Z') =="
# 1 Firecrawl
out=$(timeout 60 firecrawl --status 2>&1 | sed "s/\x1b\[[0-9;]*m//g" | grep -viE 'key|token|fc-' )
if echo "$out" | grep -qiE 'authenticated|logged in|credits'; then
  echo "[OK]   firecrawl: $(echo "$out" | tr '\n' ' ' | sed 's/  */ /g')"; summary+=("firecrawl=OK")
else echo "[FAIL] firecrawl: $(echo "$out" | head -3 | tr '\n' ' ')"; summary+=("firecrawl=FAIL"); fail=1; fi
# 2 SearXNG
tmp=$(mktemp)
code=$(curl -s -m 30 -o "$tmp" -w '%{http_code}' "$SEARX/search?q=test&format=json")
n=$(python3 -c 'import json,sys;print(len(json.load(open(sys.argv[1])).get("results",[])))' "$tmp" 2>/dev/null || echo 0)
if [ "$code" = 200 ] && [ "$n" -gt 0 ]; then echo "[OK]   searxng: HTTP $code, results=$n"; summary+=("searxng=OK")
else echo "[FAIL] searxng: HTTP $code, results=$n"; summary+=("searxng=FAIL"); fail=1; fi
# 3 RSSHub
code=$(curl -s -m 60 -o "$tmp" -w '%{http_code}' "$RSS$ROUTE")
items=$(grep -o '<item>' "$tmp" 2>/dev/null | wc -l)
if [ "$code" = 200 ]; then echo "[OK]   rsshub: $ROUTE HTTP $code, items=$items"; summary+=("rsshub=OK")
else echo "[FAIL] rsshub: $ROUTE HTTP $code (000=未监听/超时)"; summary+=("rsshub=FAIL"); fail=1; fi
rm -f "$tmp"
echo "== summary: ${summary[*]} => $([ $fail = 0 ] && echo ALL OK || echo FAILED) =="
exit $fail
