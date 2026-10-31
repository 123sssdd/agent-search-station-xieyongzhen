# 拦截诊断 2026-10-29（轮次 0200-01 的 52 条未确认链接 + 11 条口碑源）
- 执行：Searcher 执行子任务，01:20–01:45（UTC+8）；原 search 文件未改动
- 实测方式：curl（Chrome UA，30s 超时）；Firecrawl scrape 串行；SearXNG 127.0.0.1:8888（200 正常）；RSSHub 127.0.0.1:1200（首页 200，/reddit/subreddit/* 路由 404）；Wayback availability API + https 回放（注意：http:// 回放一律 500，必须用 https://web.archive.org）
- Firecrawl：开始 10,877 → 结束 10,855，本任务消耗 **22 credits**（26 次请求，期间触发 1 次每分钟限速 429，等待后重试成功）

## 按域名
| 域名 | 链接数 | 直连状态码 | 拦截类型（证据） | 替代通道实测 | 推荐通道 |
|---|---|---|---|---|---|
| www.reddit.com | 18（口碑 9） | 301→200 但仅 8KB 空壳 / 原轮 403 | 反爬拦截页（server: snooserv，无帖子内容；Wayback 有一页显示 "Please wait for verification"） | .json 接口 403；old.reddit 302→登录页（reason=lor2，登录墙）；Firecrawl 明确"不支持该站点"；RSSHub reddit 路由 404；Wayback：14/18 有存档，https 回放实取 4 条正文成功、1 条为验证页、2 条超时；SearXNG：搜标题可命中原 URL 并给出摘要（6/6 测试命中） | Wayback（https）取正文 + SearXNG 摘要兜底 |
| zhuanlan.zhihu.com | 7（口碑 2） | 403 | 反爬（server: BLB，无 CF）；Firecrawl 返回 unhuman?need_login=true（验证/登录墙） | Firecrawl 失败；Wayback 0/7 有存档；SearXNG 3/3 测试命中，给标题+日期+开头摘要 | 仅 SearXNG 摘要（弱证据） |
| medium.com / *.medium.com | 10 | 403 | Cloudflare 挑战（cf-ray，title "Just a moment..."） | Firecrawl 10/10 成功取正文；Wayback 8/10 有存档；作者 RSS（medium.com/feed/@作者）200 | Firecrawl |
| pub.towardsai.net | 2 | 403 | Cloudflare 挑战（Medium 托管） | Firecrawl 2/2 成功；Wayback 无 | Firecrawl |
| python.plainenglish.io | 1 | 403 | Cloudflare 挑战 | Firecrawl 成功（首次撞 429 限速，重试成功） | Firecrawl |
| www.datacamp.com | 4 | 403 | Cloudflare 挑战 | Firecrawl 4/4 成功（课程页仅 3.8KB 偏薄）；Wayback 1/4 | Firecrawl |
| blog.csdn.net | 3 | 521 | WAF（server: WAF） | Firecrawl 3/3 成功（含登录提示，正文可读）；Wayback 1/3 | Firecrawl |
| www.preprints.org | 1 | 403 | 反爬（无 CF 头） | Firecrawl 成功（233KB 全文页） | Firecrawl |
| www.qamadness.com | 1 | 原 406，今 301→200 | 原为 UA/Accept 协商拒绝，现直连正常 | curl -L 200 | 直连 |
| github.com/topics | 2 | 原 429，今 200 | 原为速率限制（短时） | 直连 200 | 直连（降频）/ GitHub API |
| www.skills.google | 1 | 原 403，今 200 | 原为临时拦截 | 直连 200 | 直连 |
| www.bilibili.com | 2 | 412 | 风控（openresty，"出错啦"） | 按用户 19:28 决定暂不处理，未试 | 暂缓 |

## 汇总
- 52 条中（01:40 更新）：**完整可取 34 条**（Firecrawl 21、直连恢复 4、Wayback 正文 9）；**仅摘要 16 条**（reddit 9：存档为验证页或无存档，SearXNG 摘要；知乎 7：SearXNG 摘要）；**未处理 2 条**（B 站，用户决定暂缓）。完整 34/52，含摘要 50/52
- 11 条口碑源：Wayback 正文 5 条（HF 课程、Anthropic、MCP、LangGraph、GraphRAG 知识图谱），SearXNG 摘要 6 条（reddit 4、知乎 2）
- 无一条使用 cookie / 登录 / 绕过封禁

## B 类（待用户决定，未做）
1. Reddit 官方 OAuth API（需注册 app、client_id/secret，改配置）——唯一能稳定拿 reddit 正文与评论的合规通道 「待用户决定」
2. RSSHub 配置 reddit 路由（需 REDDIT 凭据配置）「待用户决定」
3. 知乎：无合规免登录通道；如需正文只能用户自行登录浏览器阅读或换来源 「待用户决定」
4. B 站字幕/信息（用户 19:28 已决定暂缓）
5. 若想避开 Firecrawl 限速：升级套餐（付费）「待用户决定」

## 待用户决定（B 类）
| 项目 | 说明 | 状态 |
|---|---|---|
| Reddit 官方 API | 注册 OAuth app 拿 client_id/secret，可稳定取正文和评论；剩余 9 条 reddit 只能靠它 | 「待用户决定」 |
| 知乎 | 无合规免登录通道（Firecrawl 撞登录墙，无存档）；可选：用户自己登录阅读，或换来源 | 「待用户决定」 |
| Firecrawl 升级 | 免费档每分钟约 11 次请求，会触发 429；升级为付费 | 「待用户决定」 |
