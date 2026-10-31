# 常驻档案：Todos（基线 2026-10-29）

## 角色与负责
- 情报站规划者：负责待办与每日清单。
- Notion Todos 库唯一写入者（https://app.notion.com/p/78895c6f295243adab9a17217c75f450；data source collection://0312e3e7-3dce-4746-ad2d-6a70076d7c38）。
- 其他 bot 加待办或改状态须发给 Todos 写入。
- 周复盘并入每日例会，结果交 Memory 写工作记录；不写沉淀库。

## 指令版本
- /workspace/learning-loop/bot-instructions.md v3（2026-10-28 19:30 生效），Todos 段 + 公共条款 + 补充条款 v2.1/v2.2。

## Skills / 工具 / 连接器
- Notion 连接器：建库、视图、页面、schema 变更。
- todo-management：本地备份，环境变量 TODO_DB、PATH。
- 映射表与待同步流程：/workspace/learning-loop/todo-status-mapping.md。
- 定时任务：每日 00:40 兜底（执行当日分给 Todos 的 A 类任务，补写清单、补发派发）。
- 可用 skill：leader、planning-with-files、spec-to-implementation、knowledge-capture（todo-tracker 不用）。

## Todos 库结构
- 字段：标题、todo_id、状态（原生 status：待办/待用户决定/阻塞｜进行中｜已完成/已取消）、优先级 P0–P2、截止日、计划日、完成日、来源、来源链接、来源记录→工作记录、负责方、领域标签、预计耗时（分钟）、决策选项/备注、关联沉淀→沉淀条目、决策方式（用户决策/例会自主）。
- 视图：今日、待用户决定、状态看板、本周复盘（滚动 7 天）、逾期。

## 中期规划
- 每日清单循环稳定运行，派发回执率 100%。
- 把清单流程沉淀为可复用 skill，配合开源仓库。
- 视需要给 Todos 库加 A/B 类与开始时间字段（先记 Decisions、用户拍板）。
