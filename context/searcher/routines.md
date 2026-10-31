# Searcher 定时任务登记（2026-10-31）
按 v3-31：内容不变，时间待定，全部暂停，后续由用户决定。

| 名称 | folder | 原时间 | 内容摘要 | 状态 |
|---|---|---|---|---|
| 每周五 00:40 兜底：执行 Todos 分配的 A 类任务（当周有周一例会时周二另行添加） | 00-40-todos-a | `CRON_TZ=Asia/Shanghai 40 0 * * 5`（每周五 00:40 左右，前后 15 分钟浮动） | 查 Notion Todos 里当天分配给 Searcher 的 A 类待办并执行；没有任务就安静结束 | 暂停 |

已删除的历史定时任务：10:05 夜间通知（10-00，v3-26 取消）、10-29 任务 11 Playwright MCP 实测（已于 10-30 手动完成后删除）。

## 保存原文（2026-10-31 15:07 用 UpdateRoutine get 取出）
- folder id：`00-40-todos-a`
- 状态：暂停（paused）
- schedule：`CRON_TZ=Asia/Shanghai 40 0 * * 5`；timing：flexible，可提前 15 分钟、可延后 15 分钟；服务器实际选定的触发时间：`CRON_TZ=Asia/Shanghai 48 0 * * 5`

```
名称：每周五 00:40 兜底：执行 Todos 分配的 A 类任务（当周有周一例会时周二另行添加）
读取 Notion「学习中枢」的 Todos 库（https://app.notion.com/p/78895c6f295243adab9a17217c75f450），只读，用 Notion 连接器。找出计划日为今天、负责 bot 为 Searcher 的 A 类任务。如果某项已经有一次性定时任务在跑或已经完成，就跳过；其余按 /workspace/learning-loop/bot-instructions.md 的「公共条款」和「3. Searcher」规则执行（搜索先 firecrawl --status，链接必须真实请求核实）。B 类只准备材料，标「待用户决定」。每完成一项，就用 SendToAgent 告诉 Todos（id afed6ca6-33c4-4108-9474-23987854d7a8，priority:true）把状态改为已完成并附结果路径，再把要点（路径+摘要）发给 Memory（id 1fa421df-287b-498b-b84e-c606f397c733）。夜间除安全问题外不打扰用户；没有任务就安静结束。
```
