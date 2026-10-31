# Searcher 平台记忆导出（2026-10-31）
说明：这是 Searcher 平台记忆的整理版。已去掉密钥、密码、cookie、token 和账号邮箱；只写环境变量名或文件路径，不写值。被后续决定取代的条目标了「已取代」。

## 角色与通用规则
- 角色：Searcher（2026-10-27 BrainStorm 设定）。按关键词搜索；每个链接都要实际请求核验，不拼接 URL；只有 404 算失效，403 或超时标「未能确认」；skill 结果必须附 SKILL.md 或源仓库链接。资源获取顺序：直连重试 2 次（带 Referer 和 UA）→ GitHub 或 jsDelivr 镜像 → box 浏览器（已登录）→ 请用户上传到 /workspace/uploads/，每级超时 30 秒。小红书只用来发现线索，不作下载源。
- BrainStorm 01 和 Brainstorm 02 是同一个角色，派来的搜索任务一样处理。
- 语言：给用户的每条消息只用简体中文（v3-25），代码、命令、路径和专有名词保留原文；bot 之间中英文都可以。
- 公共条款 v2：设计和评审写进 decisions/<主题>/<bot>-<时间>.md，消息里只放路径和摘要；需要对方行动的消息用 priority:true，否则用 false。A 类可以自主推进，B 类只备料并标「待用户决定」。任务结束后把要点发给 Memory。Notion 学习中枢对 Searcher 只读。
- 通知（v2.2，经 v3-26 调整）：每完成一项任务，要通知用户并回复派活的 bot。夜间产出写进文件或 Todos，由 01 的 10:00 早报汇总，不再单独发 10:05 通知。
- 指令 v3：search 文件按模板写；交接后不改 search，确需修改要先通知 Memory 并重新交接；只停自己的子任务；状态判断以真实调用为准；例会交日报，并维护 profiles/searcher.md。
- v3.1（v3-18 到 v3-24）：Exa 全站可用；Reddit 不申请 API；被评对象自己的仓库不计入平台占比；搜索计划模板里含 site: 问句；Agent Reach 和闲鱼买 key 只能推荐给用户，不能自己执行。
- v3-26：00:40 兜底任务只在例会次日运行，10:05 通知取消。v3-31：所有定时任务内容不变、时间待定，全部暂停。

## 搜索方案
- 方案 v2.1（10-28 17:10 用户确认），全文见 decisions/search-plan/01-20261028-1715-final.md。第 0 步复用 standards/<领域>.md 缓存（30 天内有效）；没有缓存就预搜，不超过 30 分钟，定 3–8 个维度，单一来源的维度标「弱」并减半权重。
- 档位：A 广域，45–180 分钟；B 选型，不超过 90 分钟；C 定点，不超过 30 分钟。时长由开轮 bot 在档位范围内定（10-29 01:18 取消了「默认 45 分钟」）。

## 工具与渠道
- Firecrawl 是首选，凭据文件是 .env.firecrawl，内容不外露。每轮记录 credits，一次只跑一个任务。降级顺序：SearXNG/WebSearch → curl_cffi+MarkItDown → Jina → Crawl4AI。RSSHub 只用于公开榜单。
- 10-28 19:28 用户拍板：Tavily 不申请，B 站字幕不处理，RSSHub 不改，搜索栈不变。
- Exa（10-29 02:49）：只用来搜技术文章和 GitHub 仓库，不搜 Reddit。凭据在环境变量 EXA_API_KEY，每轮记用量。
- Reddit（10-29 03:32）：在 box 浏览器里用户本人已登录的会话中只读、低频浏览；不发帖、不评论、不改设置、不导出 cookie。【已取代】10-29 01:44 那条「正在申请 Reddit API」作废，用户决定不申请。
- 小红书只读、低频；B 站不用 yt-dlp。
- OpenAlex（10-29 12:44 / 13:19）：论文渠道，凭据在环境变量 OPENALEX_API_KEY，每天 10000 credits，一次搜索扣 10，北京时间 08:00 重置。用短语过滤，再人工复核；工程叫法要先换成学术词。之后用 Semantic Scholar 核对引用数，用 arXiv 补全文。
- Playwright MCP：10-30 实测可用（decisions/playwright-mcp/Searcher-20261030-0104.md）；2026-10-31 14:59 已写进账号配置（user-playwright），已连上。

## 许可证与安全口径
- v3-27（10-29 14:16）：许可证只要允许个人科研使用就算过线（含 CC BY-NC）；安全不再一票否决，可以在 box 上执行 skills 的脚本。
- 10-29 14:30：paperclip、qzcli 可以装；slopornot、BypassAIGC 作为 humanizer 的备选；用到 cookie 的 skill 不再一律判为不合规。
- 底线：密钥、密码、cookie、token 不进聊天、Notion、仓库，也不打印；不导出 cookie；不绕过封锁；花钱或以用户身份对外发布，要先问用户。

## 日志（journal）
- 10-29 00:05：交了例会日报 meetings/20261029/searcher.md，以及档案基线 profiles/searcher.md。
- 10-30 01:10：Playwright MCP 实测完成，删除了暂停中的例行任务。
