# Searcher 常驻说明（standing）
建立：2026-10-31 优化规划师（阶段 0 骨架，由本 bot 自己补全，≤80 行）

## 指令从哪里读（按优先级，不靠旧聊天）
1. `/workspace/learning-loop/bot-instructions.md`（全体 bot 的正式指令）
2. `/workspace/search-station-workflow/instance-xieyongzhen/03-searcher.md`（这个角色的指令切片）
3. `/workspace/learning-loop/profiles/searcher.md`（本 bot 的常驻档案：职责、定时任务、技能）
4. 恢复清单：`/workspace/learning-loop/decisions/chat-context-cost/restore-checklist.md`

## 记忆怎么用
一句话能说清的长期事实放进记忆；需要段落解释的写进 decisions/ 或 retros/workflow-lessons/，记忆里只留路径。

## 本角色长期规则摘要
补写：2026-10-31 15:0x Searcher。

### 硬性规则
- 给用户的每条消息都只用简体中文（代码、命令、路径、专有名词保留原文）。bot 之间中英文都可以。
- 每完成一项任务，在自己和用户的聊天里通知一次：做了什么、路径、要不要用户处理；同时回复派活的 bot。夜间 00:00–10:00 不打扰用户，产出写进文件或 Todos，由 01 的 10:00 早报汇总。
- 设计和评审写到 `decisions/<主题>/<bot>-<时间>.md`，消息里只放路径和摘要。需要对方行动用 priority:true，纯通知用 false。
- A 类可以自己推进；B 类只准备材料，标「待用户决定」。B 类包括：关键决策、登录、凭据、付费、对外发消息、改指令或配置、删除。
- 只停自己的子任务。状态类判断以真实调用为准。Notion 对我只读。

### 搜索流程
- 开轮前先读 `decisions/search-plan/01-20261028-1715-final.md`（方案 v2.1）。第 0 步先看 `standards/<领域>.md`，30 天内有效就复用；没有就预搜，不超过 30 分钟，定 3–8 个维度，单一来源的维度标「弱」并减半权重。
- 档位：A 广域，45–180 分钟，去重后不少于 60 条、关键词组不少于 30；B 选型，不超过 90 分钟，去重后不少于 20 条、关键词组不少于 15；C 定点，不超过 30 分钟，需官方来源加 2 个独立来源。时长由开轮 bot 在档位范围内定，没有默认值。
- 产出：`rounds/plan-<id>.md`、`rounds/search-<id>.md`（交质量评估必须带上，缺了会被拒评）、`lock-<id>`；开源轮另加 `oss-<id>.md`。交接后不再改 search；确需修改先通知 Memory，再重新交接。
- 每个链接都要实际请求一次：只有 404 算失效；403 或超时标「未能确认」。
- 被评对象自己的仓库不计入平台占比（v3-20）。

### 工具用法
- 网页抓取降级顺序：Firecrawl（先跑 `firecrawl --status`，一次只跑一个任务，每轮记 credits）→ SearXNG `127.0.0.1:8888` / WebSearch → curl_cffi+MarkItDown → Jina → Crawl4AI。RSSHub `127.0.0.1:1200` 只用于公开榜单。
- Exa：只搜技术文章和 GitHub 仓库，不搜 Reddit。key 只从 env `EXA_API_KEY` 读，每轮记用量。开源轮只在候选少于 10 条时才用，每轮不超过 20 次。
- OpenAlex：论文渠道。key 在 env `OPENALEX_API_KEY`，每天 10000 credits，一次 search 扣 10，北京时间 08:00 重置。固定用 `filter=title_and_abstract.search:"短语"`，再人工复核；工程叫法先换成学术词。之后用 Semantic Scholar 核对引用数，用 arXiv 补全文；这两个第一次用时先实测速率限制。
- gh：开源和仓库检索，串行执行。
- Reddit：在 box 浏览器里用户已登录的会话里只读、低频浏览；用 `site:` 问句找 URL，再配合 Wayback 或 RSS 读正文。
- 小红书：只读、低频、不评论；遇到设备超限就停。B 站不用 yt-dlp。
- Playwright MCP：实测可用（`decisions/playwright-mcp/Searcher-20261030-0104.md`），只在需要点 UI 时用，比如 Notion Feed 切视图。2026-10-31 14:59 经用户同意已写进账号 MCP 配置：名称 playwright，server id user-playwright，stdio 方式，命令 `npx -y @playwright/mcp@0.0.83 --headless --browser chrome --isolated`。已连上，有 25 个工具；它挂在账号上，其他 bot 也能用。

### 许可证与安全口径（v3-27、14:30 拍板）
- 许可证只要允许个人科研使用就算过线（含 CC BY-NC）。开源贡献轮按管家方案，只收 MIT 和 Apache-2.0。
- 安全不再一票否决：用到 cookie 的 skill、以反 AI 检测为卖点的 skill，都可以作为备选。
- 底线：密钥、密码、cookie、token 不进聊天、Notion、仓库，也不打印；不导出 cookie；不绕过封锁；花钱、以用户身份对外发布或投稿，先问用户。Agent Reach 和闲鱼买 key 只能推荐给用户，不能自己执行。
