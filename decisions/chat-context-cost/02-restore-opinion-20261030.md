# 02 零聊天恢复意见（2026-10-30 20:04–20:05 发 01，2026-10-31 按 v3-31 存档）

1. 思路成立：聊天只承载本轮对话；真相源 = 仓库文件 + Notion + 各 bot 记忆导出。不另建「聊天全文镜像」作检索主入口，最多作归档备份。
2. 分层：
   - 仓库（learning-loop 私有 + search-station-workflow 公开）= 可 diff、可复盘的真相源：bot-instructions.md、roadmap.md、standards/、decisions/**、rounds/**、meetings/**、profiles/**、retros/**、context/<bot>/、templates。
   - Notion = 看板与检索面：Todos（Todos 唯一写手）、Decisions/工作记录/轮次/沉淀（Memory）、开源贡献进度（Github 管家主写进度字段）。正文以仓库路径为准，Notion 只放摘要 + 路径。
   - 平台记忆 = 跨 bot 短事实，长文不进记忆；脱敏导出到 memory-export/<bot>.md。
3. 新开 01/02 最小恢复集：bot-instructions.md；profiles/brainstorm01.md、brainstorm02.md；context/<bot>/standing.md、active.md、routines.md；roadmap.md；最近例会 meetings/<日>/summary.md + Notion Todos 当天；standards/ 在用版本；decisions/ 近 7 天 + pending-user/；rounds/ 与 decisions/round-*/ 未闭环部分；开源侧 oss/ 或 registry + Github 管家交接说明。不需要：聊天全文、rsshub/searx 日志、tmp*。
4. 与例会/轮次衔接：例会仍写 meetings/<YYYYMMDD>/；轮次仍 rounds/ + decisions/round-<id>/。清聊天前由当前 bot 写 meetings/<日>/handoff-<bot>.md（进行中轮次、待用户 B 类、未回执、已知坑），新 bot 读 handoff + 最小集即可恢复。
5. 执行者（Searcher/质量评估）恢复最短集：bot-instructions.md 职责段、profiles/<bot>.md、standards/ 本领域最新版、templates/；接手进行中轮次读 rounds/<id>/ 的 plan、raw/候选、search 交接、eval，以及 decisions/round-<id>/ 已有裁定与复核。执行者零聊天依赖。
6. 开轮只传路径：给 Searcher/质量评估/复核侧的消息 ≤10 行，只写轮次 id、档位、领域/评审深度 + 相关文件路径；禁止粘贴旧聊天摘要或整份标准；回执只回路径 + 三行摘要。
7. 风险：没落盘的口头约定会随清聊天丢失——拍板前先落 decisions/ 或 pending-user/。新开 bot 属配置变更，需用户确认。
