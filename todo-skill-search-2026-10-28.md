# Todo / 计划类 Skill 调研（2026-10-28，给 Todos bot）

## 说明
- **SkillHub 数据**：14 个关键词经 api.skillhub.cn 搜索，候选的详情、文件、评测、源码均用接口实际请求过。
  - 「评测」是站内 AI 评测各子项分（满分 5）的平均值，是我算的，站内没有直接给总分。
  - 「收藏/下载/安装」取自详情接口的 stats。
  - 「创建日期」取自接口；所有条目的 updated 都显示今天，像是平台同步时间，不作参考。
- **SkillHub 链接**：skillhub.cn 是前端渲染的单页应用，任何路径都返回 200，所以无法单靠访问证明页面存在。我用接口 /api/v1/skills/{slug}?namespace= 确认存在。
- **ClawHub 链接**：都请求过，返回 200（原始来源）。
- **GitHub 链接**：SKILL.md 的 blob 页都用 curl 请求过，返回 200，另有注明的除外。星标数和最近推送时间取自 GitHub API。
- **Notion 判定**：依据是 SKILL.md 或脚本里是否真的调用 api.notion.com、NOTION_ 环境变量或 Notion MCP 工具名。
- **存储位置**：写的是代码里的默认值，以及能不能改。
- **范围**：只搜索、只读，没有安装任何东西。
- **Firecrawl 消耗**：调用前剩余 11,022，调用后 11,016，共用 6 credits（2 次 search）。之后改用 GitHub API 和 curl，因为 Firecrawl search 较慢，第 3 条查询被中断。

## 方向 1：todo / 任务管理

### 1. todo-management（lstpsche）
- 链接：https://clawhub.ai/lstpsche/todo-management
- SkillHub：@clawhub_lstpsche/todo-management
- 数据：评测 4.54，收藏 12，下载 9,022，安装 777，创建 2026-03-06
- 形态：脚本型，scripts/todo.sh，用 SQLite
- 存储：默认 `./todo.db`，可通过 `TODO_DB` 修改；原文写明不写任何 md 文件
- Notion：不支持
- 一句话：按工作区存放的 SQLite 待办，支持分组和 pending/in_progress/done/skipped 四种状态

### 2. todo-tracker（jdrhyne）
- 链接：https://clawhub.ai/jdrhyne/todo-tracker
- 数据：评测 4.31，收藏 2，下载 14,126，安装 318，创建 2026-03-06
- 形态：脚本型，scripts/todo.sh
- 存储：默认工作区里的 `TODO.md`，可通过 `TODO_FILE` 修改
- Notion：不支持
- 一句话：跨会话的 TODO 便签本，可接入 HEARTBEAT 做提醒

### 3. FocusFlow专注力神器
- SkillHub：@user_5206bb12/focusflow
- 数据：评测 4.47，收藏 11，下载 26,602，创建 2026-08-06
- 形态：脚本型，focusflow.py 和 report_generator.py
- 存储：写死在 `~/.workbuddy/focusflow/data.json`，代码里是常量，没看到可配置项
- Notion：不支持
- 一句话：中文待办加番茄钟，把模糊的 todo 拆成 15 到 60 分钟的专注单元，生成日报和周报

### 4. task-planner（xueyetianya）
- 链接：https://clawhub.ai/xueyetianya/task-planner
- 数据：评测 4.28，收藏 3，下载 6,196，创建 2026-03-12
- 形态：脚本型，script.sh
- 存储：默认 `~/.task-planner/tasks.json`，可通过 `TASK_PLANNER_DIR` 修改
- Notion：不支持，原文写明 no cloud sync
- 一句话：本地任务管理，带优先级和截止日期，中英双语

### 5. clawdo
- 链接：https://clawhub.ai/lepetitpince/clawdo
- 数据：评测 4.35，收藏 3，下载 3,705，创建 2026-03-06
- 形态：依赖外部 CLI，需 `npm install -g clawdo`
- 存储：SQLite，具体路径由 CLI 决定，SKILL.md 没写
- Notion：不支持
- 一句话：给 Agent 用的待办，Agent 提议、人来批准，有自主级别

### 6. Todo for AI（线索来自小红书）
- 链接：https://github.com/todo-for-ai/todo-for-ai （1,187★，推送于 2026-09-19）
- SKILL：https://github.com/todo-for-ai/todo-for-ai/blob/main/docs/AGENT_RUNTIME_SKILL.md
- 形态：一个完整的任务平台（MySQL），配一个运行时 skill，走 HTTP API 加 Agent Key
- 存储：在自建或官方的服务端，`API_BASE_URL` 可配置
- Notion：不支持
- 一句话：专门给 AI 助手做的任务管理系统，支持拉取任务、租约、上报进度

### 第三方任务 App 接入（作为备选）
- **Todoist（mjrussell）** https://clawhub.ai/mjrussell/todoist
  - 评测 4.14，收藏 56，下载 31,977
  - 只有提示词，依赖 todoist-ts-cli，需要 `TODOIST_API_TOKEN`，数据存在 Todoist 云端
- **滴答清单 dida365-skill（woodcoal）** https://clawhub.ai/woodcoal/dida365-skill
  - 评测 4.55，收藏 0，下载 5,569
  - Python 脚本，需要 `DIDA_ACCESS_TOKEN`，数据在滴答云端
- **dida-cli（ilooch）** https://clawhub.ai/ilooch/dida-cli
  - 评测 4.31，下载 6,392，依赖 @suibiji/dida-cli
- **Apple Reminders** https://clawhub.ai/steipete/apple-reminders
  - 评测 4.32，收藏 56，下载 36,197，只能在 macOS 上用 remindctl
- **Things 3** https://clawhub.ai/steipete/things-mac
  - 评测 4.29，收藏 20，下载 19,241，只能在 macOS 上用
- **Kairusi（日刻 Todo）** SkillHub @user_9c85a73f/kairusi-skill
  - 评测 4.59，下载 4,378，创建 2026-08-26
  - 有 kairusi_mcp.py 脚本，走 Kairusi MCP，token 存在本地配置目录

## 方向 2：计划拆解

### 1. writing-plans（obra/superpowers）
- 链接：https://github.com/obra/superpowers （306,711★）
- SKILL：https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md
- 形态：只有提示词
- 存储：默认 `docs/superpowers/plans/YYYY-MM-DD-<feature>.md`，原文是固定约定，能不能改没写
- Notion：不支持
- 一句话：把需求写成可执行的分步实施计划。配套的执行 skill 是 executing-plans：https://github.com/obra/superpowers/blob/main/skills/executing-plans/SKILL.md

### 2. planning-with-files（OthmanAdi）
- 链接：https://github.com/OthmanAdi/planning-with-files （27,721★）
- SKILL：https://raw.githubusercontent.com/OthmanAdi/planning-with-files/HEAD/.agents/skills/planning-with-files/SKILL.md （200）。注意：按 main 分支拼的 blob 链接返回 404。
- 形态：脚本加 hooks
- 存储：`task_plan.md`、`findings.md`、`progress.md`，放在项目根目录或选定的计划目录，可通过 `PLAN_ID` 和 `PWF_PLAN_ROOT` 配置
- Notion：不支持
- 一句话：用文件做持久化计划，适合长任务和断点恢复

### 3. agent-long-task-skill（leswww）（线索来自小红书）
- 链接：https://github.com/leswww/agent-long-task-skill （5★）
- SKILL：https://github.com/leswww/agent-long-task-skill/blob/main/SKILL.md
- 形态：提示词加一份 JSON schema
- 存储：写死在 `.agent/task-plan.json`、`status.json`、`final-report.md`、`handoff.md`
- Notion：不支持
- 一句话：长任务的需求细化、进度跟踪、验收和交接报告

### 4. leader（KKKKhazix/khazix-skills）（线索来自小红书）
- 链接：https://github.com/KKKKhazix/khazix-skills （21,705★）
- SKILL：https://github.com/KKKKhazix/khazix-skills/blob/main/leader/SKILL.md （第一次请求超时，重试后 200）
- 形态：只有提示词
- 存储：执行时用 `PROGRESS.md` 和 `BLOCKED.md`，属于约定，不可配置
- Notion：不支持
- 一句话：把一句话的想法拆成 Agent 能独立跑完的目标任务书，不超过 4000 字

### 5. to-tickets / to-spec（mattpocock/skills）（线索来自小红书）
- 链接：https://github.com/mattpocock/skills （305,102★）
- SKILL：
  - https://github.com/mattpocock/skills/blob/main/skills/engineering/to-tickets/SKILL.md
  - https://github.com/mattpocock/skills/blob/main/skills/engineering/to-spec/SKILL.md
- 线索核对：线索里说的 to-issues、to-prd，在当前仓库里没找到。现在叫 to-tickets 和 to-spec，deprecated 目录下只有一个 README。
- 形态：只有提示词
- 存储：发布到配置好的 issue tracker，或者本地一票一个文件，通过 /setup-matt-pocock-skills 配置
- Notion：不支持
- 一句话：把计划拆成带阻塞依赖的工单

### 6. WBS Planner（ycz87）
- 链接：https://clawhub.ai/ycz87/wbs-planner
- 数据：评测 4.44，下载 3,335
- 形态：提示词加模板
- 存储：约定为 `roadmap/roadmap.md`、Epic 目录、task 文件
- Notion：不支持
- 一句话：按 Roadmap → Epic → Task 三层拆解，带粒度标准

## 方向 3：GTD 与日 / 周复盘

### 1. Productivity（ivangdavila）
- 链接：https://clawhub.ai/ivangdavila/productivity
- 数据：评测 4.53，收藏 84，下载 35,455，安装 2,529
- 形态：只有提示词，多份 md
- 存储：写死在 `~/productivity/`（tasks、goals、planning/daily.md 等）
- Notion：不支持
- 一句话：时间块、目标、习惯、回顾、优先级的综合生产力系统

### 2. ADHD Founder Planner（jankutschera）
- 链接：https://clawhub.ai/jankutschera/adhd-founder-planner
- 数据：评测 4.47，收藏 14，下载 3,698
- 形态：脚本型，plan.sh，带模板
- 存储：写死在 `~/.openclaw/skills/adhd-daily-planner/`，下分 daily 和 collections 目录
- Notion：不支持
- 一句话：子弹笔记风格的早间计划、晚间复盘和任务迁移

### 3. ADHD Daily Planner（mikecourt）
- 链接：https://clawhub.ai/mikecourt/adhd-daily-planner
- 数据：评测 4.39，收藏 30，下载 10,671
- 形态：只有提示词，不存储
- Notion：不支持
- 一句话：适合时间感弱人群的每日规划

### 4. Agent Daily Planner（gpunter）
- 链接：https://clawhub.ai/gpunter/agent-daily-planner
- 数据：评测 3.98，下载 4,336
- 形态：只有提示词
- 存储：约定为 `memory/YYYY-MM-DD.md` 和 `memory/projects.json`
- Notion：不支持
- 一句话：给 Agent 的日计划和产出记录

### 5. Weekly-Planner-Skill（Liviaaaaa33333）（线索来自小红书）
- 链接：https://github.com/Liviaaaaa33333/Weekly-Planner-Skill （0★，推送于 2026-10-06）
- SKILL：https://github.com/Liviaaaaa33333/Weekly-Planner-Skill/blob/main/weekly-planner-for-everyone/SKILL.md
- 形态：只有提示词，繁体中文
- 存储：写入 Google 日历（连接器，可以设成 none），另外维护一个可打勾的周行程页面
- Notion：不支持
- 一句话：按课表和截止日排出具体到时段的每周行程

### 周报类（作为补充）
- **Report Generator（wscats）** https://clawhub.ai/wscats/smart-weekly-report
  - 评测 4.57，收藏 39，下载 30,421
  - 只有提示词，自动提炼本周工作并写下周计划
- **周报/日报生成与润色** SkillHub @user_c5e5dc86/weekly-report-pro
  - 评测 4.49，收藏 7，下载 17,405
  - 只有提示词，6 种模板，包括 OKR 版

## 方向 4：优先级、截止提醒、Notion 同步

### 1. Notion 官方 Claude Code 插件（makenotion）（线索来自小红书，已核实）
- 链接：https://github.com/makenotion/claude-code-notion-plugin （500★）
- 4 个 skill，链接都核实为 200：
  - spec-to-implementation：https://github.com/makenotion/claude-code-notion-plugin/blob/main/skills/notion/spec-to-implementation/SKILL.md
  - knowledge-capture：https://github.com/makenotion/claude-code-notion-plugin/blob/main/skills/notion/knowledge-capture/SKILL.md
  - meeting-intelligence 和 research-documentation 在同一目录
- 形态：只有提示词，依赖 Notion MCP
- Notion：**支持**，SKILL.md 直接调用 `Notion:notion-search`、`notion-fetch`、`notion-create-pages`。spec-to-implementation 会把 PRD 拆成任务，写进 Notion 的任务数据库
- 存储：用户自己的 Notion 数据库，运行时搜索确定，可配置

### 2. Notion MCP（官方远程服务）（线索来自小红书）
- 地址：https://mcp.notion.com/mcp 。请求返回 401，这是正常的，需要 OAuth 登录。
- 文档：https://developers.notion.com/docs/mcp （200）
- 开源版：https://github.com/makenotion/notion-mcp-server （4,684★）
- 线索给的添加命令是 `claude mcp add --transport http notion https://mcp.notion.com/mcp`，未执行。

### 3. notion-project-tracker / NPT（parallized）（线索来自小红书）
- 链接：https://github.com/parallized/notion-project-tracker （14★）
- SKILL：https://github.com/parallized/notion-project-tracker/blob/main/.claude/skills/npt/SKILL.md
- 形态：只有提示词，通过 MCP 连接 Notion
- Notion：**支持**，通过 MCP 自动建 NPT 页面（配置项、系统信息、会话日志），并给每个项目建一个 TODO 数据库
- 存储：Notion 中按固定结构建立
- 一句话：从 Notion 读取当前项目的 TODO，执行完再写回去

### 4. notion-sync（robansuini）
- 链接：https://clawhub.ai/robansuini/notion-sync
- 数据：评测 4.48，收藏 6，下载 7,374
- 形态：脚本型，用 Node 脚本 add-to-database、batch-update、md↔notion 互转
- Notion：**支持**，脚本直接调 api.notion.com，需要 `NOTION_API_KEY` 或 `~/.notion-token`
- 存储：用户指定的 database id，可配置
- 一句话：Notion 页面和数据库的双向同步

### 5. Notion（steipete）
- 链接：https://clawhub.ai/steipete/notion
- 数据：评测 4.05，收藏 271，下载 133,211，安装 10,208
- 形态：只有提示词，示范用 curl 调用 api.notion.com
- Notion：**支持**，key 存在 `~/.config/notion/api_key`
- 一句话：通用的 Notion API 操作，可增删改查数据库

### 6. notion-api-automation（tristanmanchester）
- 链接：https://clawhub.ai/tristanmanchester/notion-api-automation
- 数据：评测 4.48，下载 7,335
- 形态：提示词加示例 triage 规则
- Notion：**支持**，需要 `NOTION_API_KEY`
- 一句话：以 JSON 为主的 Notion CLI 用法，可用于收件箱分拣

### 7. notion-cli（makenotion/skills，官方）
- SKILL：https://github.com/makenotion/skills/blob/main/skills/notion-cli/SKILL.md
- 形态：依赖官方 `ntn` CLI
- Notion：**支持**，可查询数据库、创建页面
- 相关：官方的 Notion↔skills 同步说明 https://developers.notion.com/guides/agent-skills/overview （200）

### 8. 提醒类
- **Reminder（reed1898）** https://clawhub.ai/reed1898/reminder
  - 评测 4.15，收藏 10，下载 15,015
  - 存储写死在 `~/.openclaw/workspace/reminders/events.yml`，经 OpenClaw cron 发 Telegram 提醒
  - Notion：不支持
- **Cron Mastery（i-mw）** https://clawhub.ai/i-mw/cron-mastery
  - 评测 4.43，收藏 38，下载 23,814
  - 讲 OpenClaw 定时和提醒的可靠用法
  - Notion：不支持

## 小红书线索（未验证，box 上小红书未登录，以下链接都没有请求）
- https://www.xiaohongshu.com/explore/6a4536c4000000001700a6da
  - 作者「金页匠」，5 个 skill 组成的 Notion 系统，叫 FIOS，没给仓库
  - 我在 GitHub 上也没去搜，状态：未找到
- https://www.xiaohongshu.com/explore/6a994964000000002503650c
  - 一个 Notion API skill，付费安装包，无法核实
- https://www.xiaohongshu.com/explore/69f2177c000000002003ad89
  - Claude Code 每日待办 skill，作者自建，约 115 赞，无仓库

## 给 Todos bot 的建议
- **记待办的底座**：用 todo-management（SQLite，路径可配），或 todo-tracker（单个 TODO.md，路径可配）。FocusFlow、Productivity、ADHD Founder 的存储路径写死，不适合直接用。
- **计划拆解**：用 writing-plans 或 planning-with-files，再配 leader。
- **复盘**：可参考 Productivity 和 ADHD Founder 的模板。
- **Notion**：官方 MCP 配 spec-to-implementation，或者 NPT。只想用脚本、不走 MCP，就用 notion-sync。
