#!/bin/bash
# 作废草稿（2026-10-29 00:32 用户取消，改由 Searcher→质量评估流程）
# usage: metrics.sh owner/repo ; read-only
r=$1; S=2026-09-29
info=$(gh api repos/$r --jq '"\(.stargazers_count)\t\(.language)\t\(.pushed_at)"')
c(){ sleep 2.2; gh api -X GET search/issues -f q="repo:$r $1" --jq .total_count; }
gfi=$(c 'is:issue is:open label:"good first issue"')
gfiu=$(c 'is:issue is:open label:"good first issue" no:assignee')
hw=$(c 'is:issue is:open label:"help wanted" no:assignee')
merged=$(c "is:pr is:merged merged:>$S")
closedun=$(c "is:pr is:closed is:unmerged closed:>$S")
# median merge hours of last 30 merged PRs
med=$(gh pr list -R $r --state merged -L 30 --json createdAt,mergedAt --jq '[.[]|((.mergedAt|fromdate)-(.createdAt|fromdate))/3600]|sort|.[length/2|floor]|floor')
# median first-response hours on last 20 issues (first comment by someone other than author)
fr=$(gh api "repos/$r/issues?state=all&per_page=20&sort=created" --jq '.[]|select(.pull_request==null)|"\(.number) \(.user.login) \(.created_at)"' | while read n u t; do gh api "repos/$r/issues/$n/comments?per_page=10" | jq -r --arg u "$u" --arg t "$t" '[.[]|select(.user.login!=$u and (.user.type!="Bot"))][0].created_at // empty|((fromdate)-($t|fromdate))/3600'; done | sort -n | awk '{a[NR]=$1} END{if(NR)printf "%.1f(n=%d)",a[int((NR+1)/2)],NR; else print "NA"}')
echo -e "$r\t$info\tgfi=$gfi\tgfi_unassigned=$gfiu\thw_unassigned=$hw\tmerged30d=$merged\tclosedUnmerged30d=$closedun\tmedMergeH=$med\tmedFirstRespH=$fr"
