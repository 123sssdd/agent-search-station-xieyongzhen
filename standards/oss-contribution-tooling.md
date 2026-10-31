# 领域标准：oss-contribution-tooling（开源贡献项目发现/推荐工具）
- 建立：Searcher，2026-10-29 01:16 (UTC+8)，轮次 20261029-0030-01；30 天内复用（至 2026-11-28）。用时约 4 分钟（预搜复用本轮 q1–q5、q9、q11 结果）。
| # | 维度 | 权重 | 来源1 | 来源2 | 强/弱 |
|---|---|---|---|---|---|
| 1 | 维护者响应（Time to First Response / Issue Response Time） | 20% | https://www.chaoss.community/kb/metric-time-to-first-response | https://isitmaintained.com （中位解决时长） | 强 |
| 2 | 合并接受度（Change Request Acceptance Ratio / PR Merge Rate） | 20% | https://www.chaoss.community/kb/metric-change-request-acceptance-ratio | https://devlake.apache.org/docs/Metrics/PRMergeRate/ | 强 |
| 3 | 新人友好与 issue 可得性（good first issue/help wanted 标签、未指派） | 20% | https://www.kubernetes.dev/docs/guide/help-wanted | https://community.apache.org/committers/good-first-issues.html | 强 |
| 4 | 数据可获取性（公开 API、免凭据/免费、限流） | 15% | https://ossinsight.io/docs/api | https://docs.deps.dev/api/v3alpha | 强 |
| 5 | 工具自身维护活跃度（近 30 天推送、近 10 issue 状态） | 15% | https://www.chaoss.community/kb/metrics-model-community-welcomingness | https://nesbitt.io/2026/05/27/chaoss-metrics-in-2026.html | 强 |
| 6 | 安全/项目健康信号（Scorecard 等） | 10%→5%（弱，减半） | https://openssf.org/projects/scorecard/ | 仅单源 | 弱 |
注：chaoss.community 链接 curl 返回 301（重定向，可达）。维度 6 减半后剩余 5% 待质量评估决定是否重分配。

## 附注（2026-10-29 01:30，质量评估要求记录）
- OSS Insight 仓库级接口 /v1/repos/... 等于 2026-10-29 01:25 实测返回 500（上游 401）；仅 /v1/trends/repos 和 /gh/repos/...（镜像 GitHub 元数据）可用。来源：decisions/round-20261029-0030-01/02-0128.md 第④条。

## 变更
- 2026-10-29 02:26（Searcher，轮次 20261029-0220-01，30 天内复用）：本轮选型对比复用 D4 数据可获取性、D5 工具维护活跃度，追加两项本轮专用判据（不改权重，待质量评估确认）：「本机可达性（box 实测）」「平台政策合规（Reddit Responsible Builder Policy / Data API Terms）」。来源：https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy ；https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki
