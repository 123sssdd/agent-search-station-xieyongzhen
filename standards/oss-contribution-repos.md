# 领域标准：oss-contribution-repos（开源贡献候选仓库选型）
- 建立：Searcher，2026-10-30 19:46 (UTC+8)，轮次 20261030-1944-01；30 天内复用（至 2026-11-29）。
- 对齐：decisions/oss-contrib/plan-20261030-1944.md；decisions/oss-contrib/01-final-20261029-0315.md；复用 oss-contribution-tooling 中 CHAOSS 维度。
| # | 维度 | 权重 | 来源1 | 来源2 | 强/弱 |
|---|---|---|---|---|---|
| 1 | 新人友好与未指派 issue（gfi≥3 / help wanted 兜底） | 25% | https://www.kubernetes.dev/docs/guide/help-wanted | https://community.apache.org/committers/good-first-issues.html | 强 |
| 2 | 维护活跃度（近 90 天推送、优先近 14 天） | 20% | https://www.chaoss.community/kb/metrics-model-community-welcomingness | standards/oss-contribution-tooling.md | 强 |
| 3 | 合并接受度（参考 merge rate ≥70%） | 15% | https://www.chaoss.community/kb/metric-change-request-acceptance-ratio | https://devlake.apache.org/docs/Metrics/PRMergeRate/ | 强 |
| 4 | 许可证可改（本轮硬过滤 mit/apache-2.0） | 15% | https://choosealicense.com/licenses/ | 管家方案 plan-20261030-1944.md | 强 |
| 5 | 用户画像契合（agent/MCP/RAG/全栈工程） | 15% | 用户画像开轮任务书 | 管家方案领域关键词 | 弱 |
| 6 | Stars 适中（1k–10k） | 10% | decisions/oss-contrib/01-final-20261029-0315.md | — | 弱 |
注：chaoss.community 历史 curl 曾 301；维度 5/6 为弱维，权重已按方案自定，质量评估可复核。
