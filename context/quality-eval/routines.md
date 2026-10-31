# 质量评估 定时任务登记（2026-10-31，按 v3-31 第 2 条：内容不变、时间待定、全部暂停）

| 名称 | 原时间 | 内容摘要 | 状态 |
|---|---|---|---|
| 每周五 00:40 兜底：执行 Todos 分配的 A 类任务（folder 00-40-todos-a） | 每周五 00:40（Asia/Shanghai，前后浮动 15 分钟） | 只读查 Notion Todos 库里计划日为当天、负责 bot 为「质量评估」的未完成 A 类任务，按指令逐条评估；已有一次性任务处理的跳过；完成后通知 Todos 改状态、把要点发给 Memory；B 类只备材料标「待用户决定」；没任务就安静结束。 | 暂停（时间待用户决定） |

已删除、不再存在：10-29 10:05 夜间通知（v3-26 取消）、各轮一次性评估任务（完成即删）。

## 保存原文（2026-10-31 15:07 用 UpdateRoutine get 取出）
- folder id：`00-40-todos-a`
- 状态：暂停（paused）
- 原 schedule：`CRON_TZ=Asia/Shanghai 40 0 * * 5`，flexible，前后各 15 分钟

```text
兜底任务。用 Notion 连接器只读查询 Notion Todos 库（https://app.notion.com/p/78895c6f295243adab9a17217c75f450），找出计划日为今天、负责 bot 是「质量评估」、类型为 A 类，且状态还没有完成的任务。逐条按情报站指令 v2（/workspace/learning-loop/bot-instructions.md 的公共条款和第 4 段）执行评估。如果已有一次性定时任务在处理同一项，就跳过它，不重复做。不要写 Notion。每完成一项，用 SendToAgent（priority:true）告诉 Todos（id afed6ca6-33c4-4108-9474-23987854d7a8），请它改状态并附结果文件路径；同时把要点（路径加摘要）发给 Memory（id 1fa421df-287b-498b-b84e-c606f397c733）。B 类事项只准备材料，标「待用户决定」。没有任务就安静结束，不打扰用户。
```
