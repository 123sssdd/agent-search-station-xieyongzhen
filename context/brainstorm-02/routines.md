# Brainstorm 02 定时任务登记（v3-31，2026-10-31）

| 名称 | 原时间 | 内容摘要 | 状态 |
|---|---|---|---|
| 每日 00:40 兜底任务（平台 folder 00-40） | 最初每天 00:40 → 10/29 改周二+周五 00:40 → 10/31 v3-30 改周日 00:40（平台上目前填的是 `40 0 * * 0`，仅作占位） | 读 Notion Todos 库当天分给 Brainstorm 02、未完成的 A 类任务并执行（搜索走 Searcher → 质量评估，产出写 decisions/）；B 类只准备材料、标「待用户决定」；完成后 priority 通知 Todos 改状态；夜间除安全问题不打扰用户；没有任务就安静结束。 | 暂停；时间待用户决定（v3-31 取代 v3-30 的周日时间） |

用户 2026-10-31 因额度不足暂停了所有例行任务。按 v3-31，内容不变，恢复时间由用户之后决定。

## 定时任务完整保存原文（2026-10-31 15:07 用 UpdateRoutine get 取出）

- 名称：每日 00:40 兜底任务
- folder id：`00-40`
- 状态：暂停（paused）
- 平台上保存的触发时间：`CRON_TZ=Asia/Shanghai 40 0 * * 0`，flexible，earlyMinutes 0，lateMinutes 15。这只是占位，按 v3-31 时间待定。

```text
Nightly fallback for the 情报站 loop. Read the Notion 学习中枢 Todos database (read-only for me; https://app.notion.com/p/78895c6f295243adab9a17217c75f450) for today's tasks assigned to Brainstorm 02 that are A-class and not done. Skip any I already completed or have a one-off routine running for. Execute each A-class task following /workspace/learning-loop/bot-instructions.md (searches go via Searcher → 质量评估; write outputs to /workspace/learning-loop/decisions/... as files). For B-class items only prepare materials and mark 待用户决定. When a task finishes, message Todos (id afed6ca6-33c4-4108-9474-23987854d7a8, priority true) with the task, result path, and ask it to update the status. Don't message the user overnight except for a security issue. If there's nothing assigned, end quietly.
```
