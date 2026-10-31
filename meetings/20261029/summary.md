# 例会汇总 2026-10-29 00:00（覆盖 2026-10-28；主持：BrainStorm 01）
日报 8/8 已交（00:01）：brainstorm01/02、searcher、quality-eval、memory、todos、optimizer、diagram（meetings/20261029/）。
常驻档案基线：8/8 已写（memory、diagram 00:05 前补齐）。
健康检查（00:02 真实调用）：firecrawl --status 已认证、并发 0/2；SearXNG 127.0.0.1:8888 与 RSSHub 127.0.0.1:1200 均无响应（000，进程不在，疑 box 重启后未拉起）。

## 1. 能力矩阵（重复与缺口）
| bot | 关键 skills/工具 | 说明 |
|---|---|---|
| 01/02 | brainstorming、grill-me、writing-plans、leader、planning-with-files；Notion/GitHub 连接器 | 02 另装 todo-management、静态 sqlite3、brainstorm-getting-started |
| Searcher | firecrawl-*、SearXNG、RSSHub、curl_cffi/MarkItDown/Jina/Crawl4AI/Scrapling、SkillHub 接口 | 搜索唯一执行方 |
| 质量评估 | 评估流程、Notion notion-update-view | 证据门禁 |
| Memory | Notion 四库写入、build_round3.py、gh | manifest/CHANGELOG 唯一写入 |
| Todos | Notion Todos 库、todo-management、leader、planning-with-files、spec-to-implementation | 清单与派发 |
| 优化规划师 | 方案评审、路线图 | — |
| 配图 | project-diagram-studio、excalidraw、cairosvg | redskill 下载不可用 |
- 重复：leader/planning-with-files 在 02、Todos、01 三处；可接受（各自用途不同），不建议合并。
- 缺口：①开轮健康检查脚本（v3-4，多人提出）；②standards/ 领域标准目录未建；③Firecrawl 三档 credits 数据只有 1 个点；④manifest 构建脚本缺 url 可达性校验；⑤服务掉线无自动拉起。

## 2. 进展（10-28）
v2→v2.1→v2.2→v3 指令落地并全员采用；Notion 学习中枢五库建成并首轮同步；搜索栈两轮（rounds/*-1606-02、*-1627-02）；仓库 search-station-workflow 公开（PolyForm NC，至 31fb72c）；todo 类 skill 6 个安装；配图 4 张。

## 3. 经验 / 问题：见 retros/2026-10-29.md（引用各日报⑥⑦⑧）。

## 4. 路线图（单一来源 /workspace/learning-loop/roadmap.md，本次首建）
本周：v2.1 方案首个真实 A 档轮次；健康检查脚本；standards/ 首批；旧 eval 5 分制换算；Firecrawl 三档参考值（B 类写入指令）；Todos 库派发字段；Excalidraw 源文件重出；capabilities.md 草稿。

## 5. 固定议题「搜索方案持续进化」（基线 v2.1）
- 数据：10-28 两轮均早于 v2.1，无档位/计时/饱和数据（Searcher、质量评估、02 一致）；credits 仅 1 点（12 条=12 credits）。
- 结论：今晚跑首个 v2.1 A 档夜间轮次以采集基线数据（时长、条数、credits、饱和曲线）。
- A 类（自主补充）：建 standards/ 目录与模板（每维注来源 URL+核验日期，采纳质量评估建议②）；关键词矩阵模板；平台质量信号阈值参考表初稿；均写 decisions/search-plan/ 并记 CHANGELOG（Memory）。
- B 类（待用户）：Firecrawl A/B/C 参考上限写入指令正文（02 建议②），需再 1–2 轮数据后出 diff 草案。

## 6. 分工三栏
- 评审：02（优化提案，全面评审）、优化规划师（清单审查）。
- 执行：见当日清单（Todos 写入 Notion）。
- 待定：B 类见 decisions/pending-user/20261029/。
