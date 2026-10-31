# Todo / 计划类 Skill 评分排序（质量评估，2026-10-28，UTC+8）
依据：Searcher 的 todo-skill-search-2026-10-28.md。我没有另外打开各个 SKILL.md 或源码重新核实，也没有安装任何东西。站内评分和下载量只作参考。
评分标准：
- 第一轮：是否贴合定位、能否直接作为 SKILL.md 装入、存储是否写死（写死扣分）。
- 第二轮：维护是否活跃、与已有的 writing-plans、executing-plans、scheduling 是否重复。
- 综合分满分 10。
补充：Grok Bot 里已经有 Notion 连接器（user-Notion），所以依赖 Notion MCP 的 skill 加分。

## 推荐装（按综合分排序）
| # | Skill | 综合 | 理由 |
|---|---|---|---|
| 1 | Notion 官方插件 spec-to-implementation（makenotion） | 9.0 | 官方出品，直接调用 Notion MCP 把 PRD 拆成任务写进任务库；存储在用户自己的数据库，可配置；已装的 Notion 连接器正好能用 |
| 2 | todo-management（lstpsche） | 8.0 | 最贴合“记待办”：四种状态加分组，SQLite 路径可以通过 TODO_DB 修改。短期内作为本地底座，等 Notion 接好后作为离线备份 |
| 3 | planning-with-files（OthmanAdi） | 7.5 | 用 task_plan、findings、progress 三个文件做断点恢复，目录可配置，27.7k★ 维护活跃。和 writing-plans 互补：后者负责写计划，它负责跟进度。要注意 main 分支的 blob 链接是 404，安装时要用 HEAD 版本 |
| 4 | leader（khazix-skills） | 7.0 | 只有提示词，中文作者，能把一句话的想法变成 Agent 可以独立跑完的任务书，补上了 writing-plans 不擅长的模糊需求入口。PROGRESS.md 是固定约定，扣 1 分 |
| 5 | knowledge-capture（makenotion） | 7.0 | 把复盘和笔记写进 Notion，补上复盘这一环，避免用存储路径写死的 Productivity 类 skill |
| 6 | todo-tracker（jdrhyne） | 6.5 | 单个 TODO.md，路径可以改，最轻量；和 todo-management 二选一时选 todo-management（状态更完整），这个作为备选 |
| 7 | to-tickets（mattpocock） | 6.5 | 把计划拆成带阻塞依赖的工单，适合编程项目；通过 setup 配置存储位置。只在开发场景用 |

## 不推荐（附理由）
- writing-plans 和 executing-plans：已经装了，不重复安装；存储路径是固定约定，以后可以让 Todos 在提示里改写输出位置。
- WBS Planner（5.5）：和 writing-plans、to-tickets 的拆解功能重复。
- agent-long-task-skill（4.5）：只有 5★，存储写死在 .agent/ 目录，功能被 planning-with-files 覆盖。
- NPT（5.5）：思路好，但只有 14★，会在 Notion 里按固定结构建页面，侵入性强；官方插件已经够用。
- notion-sync、Notion（steipete）、notion-api-automation、notion-cli（5 到 6 分）：都要另外申请 API key 或装 CLI，Notion MCP 已经连上了，属于重复，只在不走 MCP 时才考虑。
- FocusFlow（4.0）：存储写死在 ~/.workbuddy/，依赖特定平台；番茄钟拆分的思路可以借鉴，但不要装。
- Productivity（ivangdavila，5.0）：存储写死在 ~/productivity/，和 scheduling、knowledge-capture 重复，只参考它的复盘模板。
- ADHD Founder Planner（4.0）：存储写死在 ~/.openclaw/ 路径，依赖特定平台。ADHD Daily Planner（5.0）：只有提示词，不存储，价值有限。Agent Daily Planner（4.0）：站内分偏低，和 Memory 的职责重复。
- Weekly-Planner-Skill（4.5）：0★，繁体中文，按课表排时段，和 scheduling 重复。
- clawdo（5.0）：依赖外部 npm CLI，存储路径没写清楚。Todo for AI（5.0）：要自建 MySQL 服务端，太重。
- Reminder 和 Cron Mastery（3.5）：依赖 OpenClaw cron 和 Telegram；Grok Bot 用 routines 做提醒，属于重复。
- 第三方 App（Todoist、滴答、Apple Reminders、Things、Kairusi，3 到 5 分）：数据会锁在别家云端，或者只能在 macOS 上用，和以后接 Notion 的方向冲突。只有用户本来就在用滴答或 Todoist 时，才考虑用来同步。
- 周报类（Report Generator、weekly-report-pro）：属于内容创作，不是 Todos 的职责，需要的话交给写作类 skill。
- 小红书线索（3 条）：没有仓库，无法核实，不评分。

## 推荐组合
- 记待办：主力用 Notion 任务库，通过 Notion MCP 读写，配合 spec-to-implementation；todo-management 作为本地备份。
- 做计划：模糊想法先用 leader 写成任务书，再用 writing-plans（已装）写成步骤，用 planning-with-files 跟进度；开发项目可以用 to-tickets 拆工单。
- 复盘：用 knowledge-capture 写进 Notion。
- 提醒：用 Grok Bot 的 routines 和已装的 scheduling，不另外装提醒类 skill。

## 补充核验（10-28 15:40，UTC+8）
- clawhub.ai 对任何路径都返回 200。我抽查了不存在的路径，同样返回 200，标题直接回显路径里的 slug，页面约 65KB。所以只看状态码不能证明页面存在。
- 我改用“页面大小加真实标题”判断，逐个检查了调研文件里全部 20 个 clawhub 链接：都在 86KB 以上，标题也都是 skill 的真实名称，判定全部存在。todo-tracker 的标题和 slug 一样，但页面有 95KB，也判为存在。
- 漏评补上：task-planner（xueyetianya）6.0 分。路径可以通过 TASK_PLANNER_DIR 修改，有优先级和截止日期，但和 todo-management 重复，留作备选。
- 更正：小红书那一节其实已经登录并读过笔记，只是三条线索都没有找到仓库，所以仍然不评分。mattpocock 仓库里的 to-issues 和 to-prd 已更名为 to-tickets 和 to-spec，本清单评的就是新名字。
- 以上核验不改变排序。
