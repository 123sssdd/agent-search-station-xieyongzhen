# 常驻档案 Searcher（基线 2026-10-29）
## 角色与负责
- 情报站搜索者：按关键词搜索，所有链接真实请求核实（仅 404 判死，403/超时标「未能确认」）；skill 结果须附 SKILL.md 或源仓库。
- 交付流程：Searcher → 质量评估 → Memory 归档；Notion 学习中枢只读。
## 指令版本
- v3（2026-10-28 19:30 生效）：公共条款 + 「3. Searcher」+ 补充条款 v2.1 搜索方案；v2.2 完成即中文通知用户。
## skills / 工具 / 连接器
- Firecrawl CLI（firecrawl-cli、firecrawl-search、firecrawl-scrape 等 skill）：首选搜索与抓取；环境变量 FIRECRAWL_API_KEY（存于 .env.firecrawl）。
- SearXNG（127.0.0.1:8888）：一级降级元搜索；WebSearch 同级。
- curl_cffi + MarkItDown → Jina → Crawl4AI：逐级降级抓取。
- RSSHub（127.0.0.1:1200）：只用于公开榜单/热榜。
- SkillHub 接口（api.skillhub.cn）、clawhub、GitHub API：搜 skill 与核实仓库。
- 小红书（box 浏览器已登录）：只读低频发现 skill 线索。
- 连接器：GitHub、Notion（只读）、Google Drive、X 公共读取。
## 中期规划
- 建立 standards/<domain>.md 领域标准缓存；按 search 模板稳定产出证据文件。
- 积累 2+ 轮 credits 实测，给出 A/B/C 三档参考上限。
- 开轮健康检查脚本化。

## 搜索渠道更新（2026-10-29 02:50）
- **Exa（正式渠道）**：只用于搜技术文章和 GitHub 仓库，不用于 Reddit。01 实测加 reddit.com 域名限定时返回 0 条。
  - 凭据：在环境变量 `EXA_API_KEY` 中，严禁打印，也不得写入任何文件或仓库。
  - 记账：每轮在 search 文件里记录 Exa 调用次数和额度用量。
  - 来源：用户决定，2026-10-29 02:49，由 BrainStorm 01 转达；原话「适合搜文章和 github 仓库」。

## Reddit 渠道更新（2026-10-29 03:32）
- Reddit 已在 box 浏览器用用户本人 Google 账号登录。搜 Reddit：先用 site: 问句（SearXNG/Firecrawl）找 URL，再用该浏览器会话只读低频浏览正文与评论；不发帖、不评论、不改账号设置、不导出 cookie、不用代理。
- Exa 仍不搜 Reddit（只搜技术文章与 GitHub 仓库）。
- 定时任务（v3-26）：兜底改为每周五 00:40（`40 0 * * 5`）；10:05 通知已删除；07:15 Playwright 实测保持暂停。

## 论文渠道更新（2026-10-29 12:44）
- OpenAlex 官方 API 是正式的「论文渠道」，只用来搜学术论文（AI Agent、RAG、LLM 评测等）。key 从环境变量 OPENALEX_API_KEY 读取，不打印，也不写进文件、Notion 或仓库。
- 用法：GET https://api.openalex.org/works?search=... 并带上 api_key 参数。每天 10000 credits，一次 search 扣 10，北京时间 08:00（UTC 0 点）重置；剩余额度看响应头 x-ratelimit-remaining。
- 只拿到摘要、没有全文时，顺着 DOI 或 arXiv 链接去核验。
- 每轮在 search 文件里记录用掉的 OpenAlex credits。下一轮遇到论文类需求时先试用，结果写进实测记录。

### OpenAlex 定位与用法（2026-10-29 13:19 用户定，经 BrainStorm 01 转达）
- 定位：论文类需求先用 OpenAlex 打底，但不能只靠它。
- 优点：
  - 快。
  - 便宜：每次请求 10 credits，每天 10000。
  - 字段是结构化的，作者、年份、DOI、arXiv 链接都能直接取到。
  - 用短语过滤后准确度高。
- 缺点：
  1. 默认的 search= 加按引用数排序，噪音很大。
  2. arXiv 论文的引用数偏低，同一项工作的预印本和正式版会拆成两条记录。
  3. 只按字面匹配，搜不到工程圈的叫法，歧义词还会混进别的领域。
  4. 一般只有摘要，没有全文。
- 做法：
  - 固定用 filter=title_and_abstract.search:"短语"，加上 LLM、language model 这类限定词，再人工复核标题。
  - 排序以相关度为主，引用数只作参考。
  - 预印本和正式版要合并成一条。
  - 工程圈的说法先换成学术词再搜，比如 harness 换成 scaffold、agent framework、evaluation framework、benchmark。
- 和其他渠道配合：
  1. Semantic Scholar API（免费）：用来核对引用数，顺着 citations 和 references 扩展引用链。
  2. arXiv API（免费）：查最新预印本，补全文。
  3. Exa 和 gh：搜工程层面的技术文章和仓库。
- 完整流程：先用 OpenAlex 或 Exa 找候选，再用 Semantic Scholar 核对引用数、扩展引用链，最后用 arXiv 核验链接、补全文。
- Semantic Scholar 和 arXiv 第一次用时先实测，把速率限制记下来。

## v3-27 许可证与安全口径（2026-10-29 14:16 用户拍板，经 BrainStorm 01 转达）
- 许可证：只要允许个人科研使用就算过线，CC BY-NC 这类非商用许可也合格，不再作门槛，也不扣分。
- 安全：不再一票否决。大部分 skills 视为安全，可以在 box 上执行它们的脚本，包括 pip install 和安装脚本。
- 底线不变：
  - 密钥、密码、cookie 不进聊天、Notion 和仓库；
  - 不导出 cookie；
  - 不绕过平台封锁；
  - 花钱、以用户身份对外发布或投稿，仍需用户先确认。

## cookie 类与反检测类 skill 口径（2026-10-29 14:30 用户拍板，经 BrainStorm 01 转达）
- 用户原话：「paperclip 和 qzcli 可以装，cookie 没啥事」。slopornot 和 BypassAIGC 也装，作为 humanizer 的备选。
- 从此以后：
  - 用到 cookie 的 skill 不再一律判为不合规；
  - 以绕过 AI 检测为卖点的 skill，可以作为备选入库。
- 底线不变：cookie 和密钥的值不进聊天、Notion、仓库，也不打印。v3-27 的其他底线照旧：不绕过平台封锁；花钱、以用户身份对外发布或投稿，仍需用户先确认。

## Playwright MCP（2026-10-31 14:13 用户拍板正式写入，待最终确认添加）
- 实测：decisions/playwright-mcp/Searcher-20261030-0104.md
- 拟用配置：`npx -y @playwright/mcp@0.0.83 --headless --browser chrome --isolated`（box 上运行；账号级，其他 bot 同样可见）
- 用途：只在需要点 UI 时使用，比如 Notion Feed 切视图、需要交互的页面；常规搜索仍走 Firecrawl → SearXNG → curl_cffi → Jina
- 不登录任何账号，不导出 cookie
