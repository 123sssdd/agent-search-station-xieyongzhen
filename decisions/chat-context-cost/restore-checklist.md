# 新 bot / 执行者恢复清单（正式版）
建立：2026-10-31 14:15 优化规划师，依据用户 14:13 拍板与 `优化规划师-20261030-2005.md` 第 5、7 节。

## 通用原则（所有 bot）
1. 只从文件恢复，不要求用户粘贴旧聊天，也不把旧聊天当指令。
2. 指令优先级：`/workspace/learning-loop/bot-instructions.md`（全体正式指令）高于私有仓库 `agent-search-station-xieyongzhen` 里的角色切片（原 `search-station-workflow/instance-xieyongzhen/`，迁移后以私有仓库为准），高于 `profiles/<bot>.md`（常驻档案），高于记忆。
3. 恢复顺序：先读指令 → 再读常驻档案 → 再读 `context/<bot>/standing.md`（长期规则摘要）和 `active.md`（当前任务）→ 需要跨 bot 事实时再查共享记忆。
4. 一句话能说清的事实进记忆；长文写进 `decisions/` 或 `retros/workflow-lessons/`（工作流经验）。
5. 读不到必读文件时，标「阻塞」并回报 BrainStorm 01，不要猜。

## 仓库分工（v3-30，2026-10-31 14:45）
- 私有仓库 `agent-search-station-xieyongzhen`：个人工作流的主要真相源，放 learning-loop 的工作区内容、个人实例指令、context、registry 等。由 Github 管家建仓并推送。
- 公开仓库 `search-station-workflow`：只放通用模板、schema、适配器，不放个人数据和内部编号。
- 换电脑或删掉 bot 后，先把私有仓库克隆到 `/workspace/learning-loop/`，再按本清单读文件。

以下路径如无特别说明都在 `/workspace/learning-loop/` 下（即私有仓库克隆后的位置）。

## BrainStorm 01 / Brainstorm 02（主持与拍板）
- 必读：`bot-instructions.md`；`profiles/brainstorm01.md` 或 `profiles/brainstorm02.md`；`context/brainstorm-01|02/standing.md`、`active.md`
- 当天：`meetings/<当天日期>/` 下的日报与 summary；`roadmap.md`（路线图唯一来源）
- 待决：`decisions/pending-user/<日期>/`（等用户拍板的事）
- 进行中的搜索轮次：`rounds/plan-<轮次编号>.md`

## Searcher（搜索执行者）
- 必读：`profiles/searcher.md`；`context/searcher/active.md`（写着当前轮次编号）
- 本轮任务书：`rounds/plan-<轮次编号>.md`（例如 `rounds/plan-20261030-1944-01.md` 就是 10 月 30 日 19:44 开的第 1 轮）
- 评分标准：`standards/<领域>.md`（没有就用 `standards/_template.md`）
- 写作模板：`/workspace/search-station-workflow/templates/evidence/plan.md`、`search.md`
- 渠道口径：只看任务书里勾选的渠道。OpenAlex 等学术渠道看 `decisions/search-plan/`；Reddit 用浏览器低频只读（v3-19）；Exa 只搜技术文章和 GitHub，密钥只从环境变量读（v3-18）；GitHub 按 v3-21。
- 可选：`keywords/`、`decisions/search-plan/platform-thresholds.md`
- 不读：其他轮次的全文、历史聊天
- 交付：`rounds/search-<轮次编号>.md`，再把轮次编号和路径发给质量评估

## 质量评估
- 必读：`profiles/quality-eval.md`；`context/quality-eval/active.md`
- 本轮交付：`rounds/search-<轮次编号>.md`
- 评分标准：同轮 `standards/<领域>.md`（许可证、安全口径按 v3-27）
- 打分模板：`/workspace/search-station-workflow/templates/evidence/eval.md`
- 可选：同领域上一份 `rounds/eval-*.md` 只看校准部分
- 交付：`rounds/eval-<轮次编号>.md`，发路径和三行摘要给开轮方

## Github 管家
- 必读：`profiles/github-steward.md`；`context/github-steward/standing.md`、`active.md`
- 开源贡献：`decisions/oss-contrib/` 里最新的 final、plan、priority 文件；本轮 `rounds/plan|search|eval-<轮次编号>.md`
- 规则：fork 可直接做；push、PR、评论、issue、CLA 都要用户先确认草稿

## Memory（唯一归档写入者）
- 必读：`profiles/memory.md`；`context/memory/standing.md`、`active.md`
- 写入依据：Notion 字段定稿 `notion-design-2026-10-28.md`；开源库字段 `decisions/oss-contrib/notion-schema-*.md` 最新一份；工作流经验库 `decisions/chat-context-cost/notion-workflow-lessons-spec.md`
- 待归档：`retros/workflow-lessons/`、各 bot 发来的路径
- 规则：manifest 推送和 schema 变更前先记 Decisions；推送仓库需用户确认

## Todos（唯一待办写入者）
- 必读：`profiles/todos.md`；`context/todos/standing.md`、`active.md`
- 字段和状态：`notion-design-2026-10-28.md`、`todo-status-mapping.md`
- 当天：`meetings/<当天日期>/` 的会议结论
- 本地备份：todo-management（数据库 `/workspace/todos/todo.db`）

## 优化规划师 / 手绘风技术配图
- 必读：各自的 `profiles/` 和 `context/<bot>/`；优化规划师另读 `decisions/` 下各主题 `INDEX.md`；配图另读 `diagrams/`

## 抽测（验证清单是否够用）
- [ ] 任选 Searcher 或质量评估，在新会话中只按本清单读文件，完成一次 dry-run，不翻聊天
- [ ] 发现缺的文件补进本清单，并在 `retros/workflow-lessons/` 记一条经验

## 人工步骤（文件替代不了）
详见 zero-chat-audit-20261031.md 第 4 节。
1. 新建 bot 本体（名字、头像），贴入私有仓库里的指令切片——用户。
2. 按 memory-export/<bot>.md 写回平台记忆——各 bot。
3. 按 routines.md 重建定时任务——各 bot。
4. 重新授权连接器（Notion、GitHub、Google Drive、Excalidraw）——用户。
5. box 浏览器重新登录（如 Reddit 的 Google 登录，两步验证）——用户，网站见 sites-to-login.md。
6. 重设密钥环境变量（如 EXA_API_KEY），值不进文件——用户。
7. 按 scripts/ 重装 SearXNG、RSSHub 等——Github 管家/Searcher。

## 补充（v3-31，2026-10-31 14:57）
- 每个 bot 恢复时还要读：`context/<bot>/routines.md`（定时任务登记，记录内容和原时间；按 v3-31 时间待定、全部暂停，由用户决定何时恢复）和 `memory-export/<bot>.md`（平台记忆的脱敏导出，用来在新 bot 里重建记忆）。
- 人工步骤由用户本人做：连接器授权、浏览器登录、密钥设置、新建 bot 本体，bot 不用代办。
- 恢复抽测（dry-run）暂不做。
- 定时任务的完整保存原文在 `context/<bot>/routines.md`；用户自建的 skills 在 `skills/user-workflows/`；千问、豆包的指令在 `prompts/`。
