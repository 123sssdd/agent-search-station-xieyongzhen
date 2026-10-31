# 当日清单 v1（2026-10-29，Todos 起草 00:08）
依据：conclusions.md、decisions/optimizations-20261029/01-final-0010.md。A 类 10:00 前完成；B 类只备材料、10:00 后由用户决策。
todo_id 拟编号 todo-20261029-01…13；计划日均为 2026-10-29；状态均为「待办」；决策方式 A=例会自主、B=用户决策。

| todo_id | 任务 | 类 | 负责 | 用时 | 开始 | 依赖 | 产出 |
|---|---|---|---|---|---|---|---|
| 01 | Decisions 登记 Todos 库加字段（A/B类、建议用时、开始时间，只加不删） | A | Memory | 10m | 00:50 | — | Decisions dec-20261029-01 |
| 02 | Todos 库加上述字段并重读确认 | A | Todos | 20m | 01:35 | 01 | Todos 库 schema |
| 03 | 拉起 SearXNG/RSSHub（仅现有启动命令）+ health-check.sh，结果写 plan 头部 | A | Searcher | 45m | 01:00 | — | scripts/health-check.sh；rounds/plan-20261029-0200-01.md |
| 04 | 旧 eval 两份换算 5 分制 + 门禁头 + 公式 | A | 质量评估 | 30m | 01:15 | — | rounds/eval-20261028-1606-02.md、-1627-02.md |
| 05 | 夜间 A 档轮次 0200-01（standards、搜索、keywords、实测记录） | A | Searcher | 150m | 02:00 | 03 | rounds/search-20261029-0200-01.md |
| 06 | 轮次 0200-01 评估（v3 eval 模板，复核 standards） | A | 质量评估 | 90m | 04:45 | 05 | rounds/eval-20261029-0200-01.md |
| 07 | 轮次 0200-01 复核 + 饱和提前结束审批（如申请） | A | Brainstorm 02 | 30m | 06:30 | 06 | decisions/round-20261029-0200-01/02-<HHMM>.md |
| 08 | 搜索方案 A 类补充（standards/_template、platform-thresholds、plan 实测记录节、capabilities 草稿） | A | 优化规划师 | 60m | 01:45 | — | 对应路径；capabilities-draft.md |
| 09 | Memory build 脚本通用化 + hash 比对 + url 校验，dry-run（不推送） | A | Memory | 60m | 02:00 | — | 脚本 + dry-run 报告 |
| 10 | Excalidraw 重出 .excalidraw（箭头绑定） | A | 手绘风技术配图 | 60m | 03:00 | — | /workspace/learning-loop/diagrams/ |
| 11 | Playwright MCP 实测（并入 todo-20261028-03，不新建）：仅 box 本地 npx，不改连接器配置 | A | Searcher | 45m | 07:15 | 05 结束 | decisions/playwright-mcp/searcher-20261029-<HHMM>.md |
| 12 | 本地 CHANGELOG 记今晚 A 类产出（不推送） | A | Memory | 20m | 08:30 | 01–11 | search-station-workflow/CHANGELOG.md |
| 13 | 整理 B 类与夜间成果包，10:00 后随 v2.2 发用户 | A | BrainStorm 01 | 10m | 09:45 | 全部 | decisions/pending-user/20261029/01-B类汇总.md |
| B1–B7 | 见 01-B类汇总.md（自启、credits 上限、仓库推送、manifest 推送与 url 清理、两条缺文件决定、02 模板发布、周日复盘任务） | B | 各方备材料 | — | 10:00 后 | — | 待用户决定 |

## Todos 处理说明
- 11 是旧条目 todo-20261028-03：只改计划日、负责方、备注，不新建（去重规则）。因此新建条目为 12 条，编号顺延。
- 沿用：todo-20261028-01 B站字幕、-02 Tavily 维持「阻塞（延后）」，不改计划日。
- B1–B7 合并写 1 条「待用户决定」汇总条目，链接 B 类汇总文件。
- 字段未加完前（02 未完成），A/B、用时、开始时间写进「决策选项/备注」。

## 请审查方注意
- Searcher 当晚 3 项（03、05、11）共 240m，05 若超时会压 11 的 07:15 开始。
- 12 依赖全部 A 类，08:30 开始可能早于 06/07 完成；建议 12 允许补记。
