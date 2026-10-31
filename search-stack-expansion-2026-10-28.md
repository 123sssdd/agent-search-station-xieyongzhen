# 搜索/抓取能力扩搜候选清单（2026-10-28，UTC+8，Searcher）
在 search-stack-2026-10-28.md 基础上扩展，不重复已测项。链接均于 2026-10-28 14:18–14:30（UTC+8）用 curl（UA+Referer，30s，失败重试）实际请求；Stars/License/最近 push 均来自 GitHub API 当日实时返回（push 时间已换算 UTC+8 日期）。价格/免费额度数字未逐一核实，故不写具体数字，以官网为准。
状态：200=有效；未能确认=超时/000/403。

## 一、面向 Agent 的搜索 API 与自建元搜索
| # | 名称 | 链接（状态） | 类型 | 免费/许可 | 能做什么 | 对 agent 的价值 | 风险 |
|---|---|---|---|---|---|---|---|
|1|Tavily|https://tavily.com ，https://docs.tavily.com （200）|API|有免费层，需 key|搜索+摘要+extract/crawl/research|为 LLM 设计的返回格式，一步拿到干净正文|闭源托管；查询外发|
|2|Exa|https://exa.ai ，https://docs.exa.ai （200）|API|有免费额度，需 key|神经/语义搜索、相似页、contents|找"类似这篇"的技术文章/仓库很强|中文覆盖一般；付费|
|3|Brave Search API|https://brave.com/search/api/ ，https://api-dashboard.search.brave.com （200）|API|有免费档，需 key|独立索引的网页/新闻搜索|非 Google/Bing 转售，独立索引，可做兜底|中文结果偏弱|
|4|Jina Search/Reader|https://jina.ai/reader （200）|API|Reader 免 key 可用；s.jina.ai 需 key（已测 401）|URL→md；搜索→md|已实测 Reader 可用，零成本读单页|知乎/B站被拦（已测）|
|5|Perplexity Sonar API|https://docs.perplexity.ai （200）|API|付费，需 key|带引用的联网问答|直接拿"答案+引用"，适合快速事实核查|成本较高；答案需二次核验|
|6|SerpAPI|https://serpapi.com （200）|API|有少量免费次数，需 key|Google/Baidu/Bing 等 SERP 结构化 JSON|支持百度等中文引擎 SERP|抓取 Google 结果的法律灰度由服务商承担，但仍属第三方 ToS 争议|
|7|Serper|https://serper.dev （200）|API|有免费额度，需 key|低价 Google SERP JSON|便宜、快，适合高频|同上|
|8|SearchApi.io|https://www.searchapi.io （200）|API|有免费试用，需 key|多引擎 SERP（含百度、YouTube 等）|SerpAPI 替代|同上|
|9|Linkup|https://linkup.so （200）|API|有免费层，需 key|面向 agent 的深度搜索|Tavily 同类备选|较新，生态小|
|10|Firecrawl Search|https://docs.firecrawl.dev （200）|API/自托管(AGPL)|免费 credits，需 key|search+scrape 一步|已装 CLI+skills，只差 key|AGPL；box IP 免 key 被拒|
|11|SearXNG（+docker 部署）|https://docs.searxng.org （200）；https://github.com/searxng/searxng-docker （200，3,265★，AGPL-3.0，已 archived，最近 push 2026-03-29）|自托管|免费 AGPL|聚合 70+ 引擎的元搜索，JSON 输出|零费用、无 key 的搜索层|上游引擎会限流/封 IP；searxng-docker 仓库已归档，以官方文档的容器部署为准|
|12|Vane（原 Perplexica，旧链接 301 跳转）|https://github.com/ItzCrazyKns/Vane （200，37,793★，MIT，2026-09-01）|自托管|MIT|基于 SearXNG+LLM 的开源"Perplexity"|自建带引用问答|需自配 LLM；更名后文档可能不同步|
|13|GPT Researcher|https://github.com/assafelovic/gpt-researcher （首次超时，重试 200；30,321★，Apache-2.0，2026-10-11）|库/自托管|Apache-2.0|多源检索→生成研究报告|深度调研流程参考|费 token；需搜索 key|
|14|LLocalSearch|https://github.com/nilsherzig/LLocalSearch （200，5,940★，Apache-2.0，已 archived）|自托管|Apache-2.0|本地 LLM+搜索 agent|仅作参考|已归档，不建议使用|

## 二、中文平台（小红书 / B站 / 知乎）合规读取
总体结论：三平台均**没有面向个人开发者的公开内容读取 API**；最合规路径是"官方开放平台（需企业/创作者资质）"或"用户本人登录后在浏览器中人工节奏阅读"。第三方工具均属非官方接口，ToS 风险需诚实告知。
| # | 名称 | 链接（状态） | 类型 | 许可 | 能做什么 | 对 agent 的价值 | 合规/ToS 风险 |
|---|---|---|---|---|---|---|---|
|1|B站开放平台|https://open.bilibili.com （200）；openapi.bilibili.com（000，未能确认）|官方 API|需申请资质|创作者/直播/商业授权接口|唯一官方通道|低；但不提供任意内容检索|
|2|小红书开放平台|https://open.xiaohongshu.com （200）|官方 API|需企业入驻|电商/商家/广告类接口|官方通道|低；不能读笔记内容做研究|
|3|robots.txt（三平台）|https://www.zhihu.com/robots.txt ，https://www.bilibili.com/robots.txt ，https://www.xiaohongshu.com/robots.txt （均 200）|规则|—|声明允许/禁止抓取路径|自动化前必须先查|—|
|4|知乎用户协议|https://www.zhihu.com/term/zhihu-terms （200）|条款|—|约定禁止未授权抓取|风险判定依据|—|
|5|RSSHub|https://github.com/DIYgod/RSSHub （200，46,695★，AGPL-3.0，2026-10-27）；路由文档 https://docs.rsshub.app/routes/bilibili 、/routes/zhihu 、/routes/xiaohongshu （均 200）|自托管/库|AGPL-3.0|把 B站 UP 主动态、知乎专栏/用户、小红书用户笔记等转成 RSS|订阅型低频读取，最"轻"的方式|中：仍是非官方抓取；公共实例常被封，部分路由要 cookie；自建+低频+只读公开内容|
|6|bilibili-API-collect|https://github.com/SocialSisterYi/bilibili-API-collect （200，20,158★，无 license，**已 archived**，2026-01-30）|文档|无|B站 Web 接口民间整理|了解公开接口（视频信息、字幕等）|中：非官方，已停更；GitHub Pages 站点 404|
|7|bilibili-api（Python）|https://github.com/Nemo2011/bilibili-api （200，4,167★，**已 archived**，2026-07-06）|库|无 license 字段|封装 B站接口|获取视频元信息/字幕|中；已归档，可能失效|
|8|yt-dlp|https://github.com/yt-dlp/yt-dlp （200，203,123★，Unlicense，2026-10-26）|库/CLI|Unlicense|支持 B站视频元数据/字幕提取（--skip-download）|读视频标题、简介、字幕做摘要|中：仅限公开内容、个人使用；勿批量下载|
|9|xiaohongshu-mcp|https://github.com/xpzouying/xiaohongshu-mcp （200，16,618★，Apache-2.0，2026-10-26）|MCP|Apache-2.0|用本人账号登录后搜索/读笔记（也能发布）|小红书在 agent 中最直接的读取方式|**高**：自动化操作违反小红书 ToS，可能封号；仅本人账号、只读、低频；禁用发布功能|
|10|MediaCrawler（前文已列）|github.com/NanmiCoder/MediaCrawler|库|仅限学习|多平台爬取|—|**高**，最后选项|
|11|Spider_XHS|https://github.com/cv-cat/Spider_XHS （200，8,286★，无 license，2026-10-22）|库|无|小红书数据采集|仅作线索|**高**：签名逆向，明显违反 ToS，不建议使用|
|12|box 浏览器 + 用户本人登录|（内部能力）|流程|—|人工节奏阅读|最合规的实用路径|低；需用户登录|
建议：知乎/小红书走 12（必要时 9 只读）；B站优先 RSSHub 自建 + yt-dlp 元数据/字幕；小红书只作线索来源。

## 三、爬虫/搜索相关 Skill 与 MCP
| # | 名称 | 链接（状态） | 类型 | 许可/Stars | 能做什么 | 对 agent 的价值 | 风险 |
|---|---|---|---|---|---|---|---|
|1|Firecrawl MCP|https://github.com/firecrawl/firecrawl-mcp-server （200，7,704★，MIT，2026-10-28）|MCP|MIT|search/scrape/crawl/extract 工具|Grok Bot 可装连接器|需 key|
|2|Firecrawl skills（firecrawl/cli）|https://github.com/firecrawl/cli/blob/main/skills/firecrawl-search/SKILL.md 、…/firecrawl-scrape/SKILL.md 、…/firecrawl-crawl/SKILL.md （均 200；仓库 673★，无 license 字段）|skill|—|13 个 skill（search/scrape/crawl/map/interact/monitor 等）|本 bot 已装，同源|需 key|
|3|Tavily skills|https://github.com/tavily-ai/skills/blob/main/skills/tavily-search/SKILL.md （首次超时，重试 200）；仓库 https://github.com/tavily-ai/skills （200，491★，MIT，2026-10-28）|skill|MIT|8 个 skill：search/extract/crawl/map/research/best-practices 等|与 Tavily API 配套|需 key|
|4|Tavily MCP|https://github.com/tavily-ai/tavily-mcp （200，2,462★，MIT，2026-10-28）|MCP|MIT|搜索/提取|官方 MCP|需 key|
|5|Exa MCP|https://github.com/exa-labs/exa-mcp-server （200，5,190★，MIT，2026-10-28）|MCP|MIT|语义搜索、代码上下文搜索|找代码示例很好用|需 key|
|6|Brave Search MCP|https://github.com/brave/brave-search-mcp-server （200，1,537★，MIT，2026-10-27）|MCP|MIT|网页/新闻/图片搜索|官方 MCP|需 key|
|7|Jina MCP|https://github.com/jina-ai/MCP （200，896★，Apache-2.0，2026-10-16）|MCP|Apache-2.0|read_url/search 等|Reader 免 key 可用|搜索需 key|
|8|mcp-searxng|https://github.com/ihor-sokoliuk/mcp-searxng （200，1,331★，MIT，2026-10-27）|MCP|MIT|把自建 SearXNG 接成 MCP|免费搜索层接入 agent|需先部署 SearXNG|
|9|MCP 官方 Fetch server|https://github.com/modelcontextprotocol/servers/tree/main/src/fetch （200；仓库 91,620★）|MCP|仓库 NOASSERTION|URL→md|最轻量的读页 MCP|无 JS 渲染|
|10|Playwright MCP|https://github.com/microsoft/playwright-mcp （200，38,730★，Apache-2.0，2026-10-23）|MCP|Apache-2.0|基于可访问性树操控浏览器|JS 页面/交互/登录流程|消耗较大；注意登录态安全|
|11|MarkItDown MCP|https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp （200）|MCP|MIT|文件/URL→md|配合已装 MarkItDown|—|
|12|Apify MCP + Apify Ultimate Scraper skill|https://github.com/apify/apify-mcp-server （200，13,534★，MIT，2026-10-28）；skill https://clawhub.ai/apify/skills/apify-ultimate-scraper （200，clawhub 下载 3,775）|MCP/skill|MIT|调用 Apify 上数千个现成 Actor（含各平台爬虫）|现成平台爬虫多|付费；第三方 Actor 对中文平台同样有 ToS 风险|
|13|Browserbase MCP|https://github.com/browserbase/mcp-server-browserbase （200，3,397★，Apache-2.0，2026-07-21）|MCP|Apache-2.0|云端浏览器自动化|无本地浏览器时备选|付费|
|14|Bright Data MCP|https://github.com/brightdata/brightdata-mcp （200，2,693★，MIT，2026-10-26）|MCP|MIT|带代理/解封的搜索与抓取|难抓站点兜底|付费；"解封"类能力有合规争议，慎用|
|15|anthropics/skills（相关：webapp-testing、pdf、mcp-builder）|https://github.com/anthropics/skills/blob/main/skills/webapp-testing/SKILL.md 、…/pdf/SKILL.md 、…/mcp-builder/SKILL.md （均 200；仓库 184,315★）|skill|仓库 license 字段为空|Playwright 测试网页 / PDF 解析 / 自建 MCP|官方无专门爬虫 skill；mcp-builder 适合自写搜索 MCP|—|
|16|browser-use skill|https://github.com/browser-use/browser-use/blob/main/skills/browser-use/SKILL.md （200）|skill|MIT|浏览器 agent 用法说明|与 browser-use 配套|需 LLM key|
|17|clawhub「Crawl」skill|https://clawhub.ai/barneyjm/skills/crawl （200，下载 2,281，bookmarks 0；源码链接未提供）|skill|—|通用爬取|仅作线索|无源码仓库链接，不满足"附源码"要求，需打开详情页审 SKILL.md|

## 备注
- skillhub.cn（200）本轮未逐个搜到专门的爬虫类高分 skill；clawhub.ai 搜索 API 可用（数据见上）。
- 未能确认：openapi.bilibili.com（连接超时）。404：socialsisteryi.github.io/bilibili-API-collect/、docs.rsshub.app/routes/social-media（已改用分平台路由页）。github.com/exa-labs/skills 404（Exa 无官方 skills 仓库）。
- 推荐增量：①有 key 后首选 Tavily 或 Exa MCP+skills 补搜索；②自建 SearXNG+mcp-searxng 做零成本兜底；③Playwright MCP 处理 JS/交互；④中文平台：RSSHub 自建（B站/知乎）+ yt-dlp（B站字幕），小红书只读线索，必要时用户授权后 xiaohongshu-mcp 只读。

## 实测 10-28（14:36–15:00 UTC+8，box，匿名、只读、低频，未用任何登录 cookie；Firecrawl credits 消耗 0）
环境：box 无 docker，三者均以源码/npm 方式运行。

### 1) RSSHub（源码 + Node 22.23.4 便携版 + pnpm 12.15，`pnpm start`）
服务：http://localhost:1200 （监听 *:1200，所有网卡；日志 rsshub-run.log；代码 /workspace/learning-loop/rsshub）
| 路由 | HTTP | 条目数 | 需 cookie？ | 备注 |
|---|---|---|---|---|
|/bilibili/ranking/0|200|100|否|全站排行榜正常|
|/bilibili/popular/all|200|20|否|综合热门正常|
|/bilibili/user/video/946974|503|0|匿名被拒|上游 B站 API 返回 412（风控）；文档称配 B站 cookie 可改善——按规则未配|
|/bilibili/user/dynamic/946974|503|0|匿名被拒|上游 412，同上|
|/zhihu/hot|200|30|否|热榜正常|
|/zhihu/daily|200|3|否|知乎日报正常|
|/zhihu/people/activities/excited-vczh|503|0|匿名被拒|上游 zhihu api/v3 返回 403|
结论：榜单/热门类路由匿名可用；UP 主视频/动态、知乎用户动态在 box 出口 IP 下被风控，需要 cookie 或换出口，未强行处理。

### 2) yt-dlp 2026.10.26（--skip-download）
视频：BV1HYnh6CEJc、BV1ekx56cETg（取自 B站热门 API，首次请求 code 0 成功）、BV1QQn96fEoG（SearXNG 结果）。
- 三个视频元数据均失败：`HTTP Error 412: Precondition Failed`；加 `--impersonate chrome`（curl_cffi）仍 412。
- 随后连 api.bilibili.com/x/web-interface/view 也返回 412，说明 box 出口 IP 已被 B站风控（短时间内首个热门 API 请求成功，之后全部 412）。
- 字幕（含 AI 中文字幕）未能测到。已知背景（未本次验证）：B站 AI 字幕通常需要登录态。按规则未使用 cookie，未继续重试。
结论：box 上 yt-dlp 读 B站目前不可用；需在用户本机网络或经用户同意的 cookie 下复测。

### 3) SearXNG（源码 master + venv，`python -m searx.webapp`）
服务：http://127.0.0.1:8888 （仅本机；配置 searx-etc/settings.yml，formats 含 json，limiter 关闭；日志 searx-run.log）
JSON 接口：`/search?q=...&format=json&language=zh-CN`
| 查询 | 结果数 | 有结果的引擎 | 相关性（前 4 条） |
|---|---|---|---|
|Rspack 和 Vite 对比|28|google cse 20、duckduckgo 10|高：Moonvy 迁移文、icodex 对比、rspack.rs 官方、CSDN|
|MCP 服务器 开发教程|29|google cse、duckduckgo|高：GitHub 中文入门、博客园、知乎专栏、CSDN|
|LangGraph 多智能体 实战|30|同上|高：知乎、博客园、腾讯云、B站|
|Playwright 爬虫 反爬 处理|28|同上|高（多为博客园/腾讯云/CSDN）|
|pnpm workspace monorepo 最佳实践|30|同上|高：掘金×3、知乎|
错误：brave「Too many requests」被挂起 180s；duckduckgo 首次测试出现 CAPTCHA（之后 5 次查询均正常返回）。默认未启用百度/搜狗等中文引擎，可后续在 settings.yml 打开再测。
mcp-searxng v1.16.0（`npx -y mcp-searxng`，SEARXNG_URL=http://127.0.0.1:8888）：initialize/tools/list/searxng_web_search 均成功，"MCP 服务器 开发教程" 905ms 返回 20 条。可直接接入 MCP 客户端。

### 运行中的服务
- RSSHub :1200（node，pid 581995）
- SearXNG 127.0.0.1:8888（python，pid 579433）
