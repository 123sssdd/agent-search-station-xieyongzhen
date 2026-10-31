# Memory 定时任务登记（2026-10-31）
按 v3-31：内容不变，时间待定，全部暂停，后续由用户决定。

| 名称 | folder | 原时间 | 内容摘要 | 状态 |
|---|---|---|---|---|
| 周二/周五 00:40 兜底：执行 Todos 分配的 A 类任务 | 00-40-todos-a | `CRON_TZ=Asia/Shanghai 40 0 * * 2,5` | 查 Notion Todos 当天分配给 Memory 的 A 类未完成项并执行；周二先判断当周周一是否开会，没开就跳过；无事不打扰；夜间日志写 meetings/<日期>/memory-0040-fallback.md | 暂停（时间待定） |
| 10-31 16:05 复查贡献库「未建关联」备注 | 10-31-16-05 | 一次性，原定 2026-10-31 16:05 | 查开源项目贡献管理里备注仍含「未建关联」的行并改为已关联文字 | 暂停（时间待定） |

## 保存原文（2026-10-31 15:08 导出，内容未改）

### 1. 周二/周五 00:40 兜底（folder 00-40-todos-a）
- schedule：`CRON_TZ=Asia/Shanghai 40 0 * * 2,5`；timing flexible（early 0 / late 15）；状态：暂停

```text
每周二、周五 00:40（UTC+8）兜底运行，依据【v3-26】：定时任务跟例会对齐。周五必跑。周二只在本周周一开过例会时才跑；看 /workspace/learning-loop/meetings/ 下有没有本周一日期的会议目录，或 Decisions 里有没有本周一的例会记录。没开过就什么都不做，也不发消息。

读 Notion「学习中枢」下的 Todos 库（https://app.notion.com/p/78895c6f295243adab9a17217c75f450），找出计划日为今天、负责方为 Memory 的 A 类任务，逐条执行。

Memory 夜间允许的 A 类工作：
- 写工作记录（每日×bot 一行，log_key=<YYYYMMDD>-<bot>，只记要点并脱敏）
- 写 Decisions 草稿
- 整理归档

不做 B 类：不推 manifest、不同步轮次/沉淀条目库、不改 bot 指令或配置、不删除、不对外发消息。这些只准备材料，并标「待用户决定」。

规则以 /workspace/learning-loop/bot-instructions.md 的公共条款和「5. Memory」段为准。

Notion 写入失败要重试；连续 3 次失败，标 B 类并通知当值主 bot（单号日 BrainStorm 01，双号日 Brainstorm 02）。

每完成一项，通过 Grok Bot 告诉 Todos（id afed6ca6-33c4-4108-9474-23987854d7a8）该任务已完成，请它改状态（priority:true）。

夜间产出写入文件或 Todos，供 BrainStorm 01 的 10:00 早报汇总（v3-26）。

结果去向：完成情况只发给 Grok Bot 里的 Todos。夜间除安全问题外不打扰用户。所有给用户的消息只用简体中文（v3-25）。没有分配给 Memory 的任务时，什么都不发。
```

### 2. 10-31 16:05 复查贡献库「未建关联」备注（folder 10-31-16-05）
- schedule：`CRON_TZ=Asia/Shanghai 5 16 31 10 *`；timing exact；一次性；状态：暂停

```text
一次性复查：Notion「开源项目贡献管理」库 collection://ff0c0a33-17f7-4f10-93ee-9699a5240691 里，查有没有哪一行的备注还含「未建关联」或「轮次库尚未有该轮」。优先用 rows 模式（filter 备注 string_contains），SQL 额度不够就用 rows。查到了就把那段旧文字换成「；已关联轮次 20261030-1944-01（2026-10-31）」，其余备注保留，进度四字段（状态/优先级/最后活动日/PR链接）不动，改完回读确认。全部干净就安静结束，不用通知谁。修了哪一行就给 BrainStorm 01 发一句（priority false），再用简体中文告诉用户一行，结尾写「无需回复」。做完删掉这个 routine。
```
