# 手绘风技术配图 定时任务登记（2026-10-31，按 v3-31：内容不变、时间待定、全部暂停）

| 名称 | 原时间 | 内容摘要 | 状态 |
|---|---|---|---|
| 周五 00:40 兜底：执行 Todos 分配的 A 类任务 | 每周五 00:40 左右（前后 15 分钟浮动，北京时间）；10-29 之前是每天 00:40 | 读 Notion Todos 库里当天分配给本 bot 的 A 类任务，用 project-diagram-studio 执行；B 类只准备材料；把 todo_id 和新状态告诉 Todos、把要点告诉 Memory（都设 priority:true）；夜间不打扰用户，没有任务就安静结束 | 暂停 |
| 10-29 10:15 重试上传 Excalidraw 三张图 | 一次性，2026-10-29 10:15 | 把 architecture、daily-meeting、learning-workflow 三个 .excalidraw 文件上传到 excalidraw.com，链接写进 diagrams/excalidraw-links.md，再告诉 01；10-29 运行时被中断，没有完成 | 暂停 |

已删除：10:05 夜间工作汇总通知用户（10-29 按 v3-26 删除）。

## 保存原文（2026-10-31 15:07 用 UpdateRoutine get 取出，内容未改）

### folder id: 00-40-todos-a ｜ 状态：暂停
```
名称：周五 00:40 兜底：执行 Todos 分配的 A 类任务
schedule: CRON_TZ=Asia/Shanghai 40 0 * * 5
timing: flexible, earlyMinutes 15, lateMinutes 15
Saved prompt:
Read /workspace/learning-loop/bot-instructions.md (公共条款 + section 7) and follow it. Through the Notion connector, read the Notion Todos database (https://app.notion.com/p/78895c6f295243adab9a17217c75f450) and find today's tasks (计划日 = today, UTC+8) whose responsible bot is 手绘风技术配图 and whose class is A. Execute each with the project-diagram-studio skill. Skip B-class: only prepare materials and mark 待用户决定. Never write Notion yourself. When done, SendToAgent Todos (afed6ca6-33c4-4108-9474-23987854d7a8) the todo_id and new status with priority:true; SendToAgent Memory (1fa421df-287b-498b-b84e-c606f397c733) key points (paths + summary) with priority:true. Per v2.2: do not message the user during 00:00–10:00 except for safety; write a short digest of what was done (paths + whether user action is needed) to /workspace/learning-loop/meetings/pending-user-notify/手绘风技术配图-<YYYYMMDD>.md so the 10:00+ digest can send it. If there are no tasks, end quietly with no user message.
```

### folder id: 10-29-10-15-excalidraw ｜ 状态：暂停
```
名称：10-29 10:15 重试上传 Excalidraw 三张图
schedule: CRON_TZ=Asia/Shanghai 15 10 29 10 *
timing: exact
Saved prompt:
The user asked (01:11 on 10-29, relayed by BrainStorm 01; earlier uploads timed out) to upload three diagrams to excalidraw.com with the user-Excalidraw connector's export_to_excalidraw, each going through the approval card: /workspace/learning-loop/diagrams/architecture.excalidraw, /workspace/learning-loop/diagrams/daily-meeting.excalidraw, /workspace/learning-hub/docs/learning-workflow.excalidraw (pass json as "$file:<path>"). One at a time; if Auto-review blocks, retry with the approval flag. Per v3-26 (user 03:23): do NOT notify the user separately; results go to files for BrainStorm 01's 10:00 morning report. If it succeeds, write the three links to /workspace/learning-loop/diagrams/excalidraw-links.md and SendToAgent BrainStorm 01 (71051128-1b36-431e-b4d2-be64a4fbb9c9, priority:true) the file path. If it still times out, stop, record the blocker in /workspace/learning-loop/diagrams/excalidraw-links.md and /workspace/learning-loop/meetings/pending-user-notify/手绘风技术配图-20261029.md, and tell BrainStorm 01 (priority:true). Then delete this routine.
```
