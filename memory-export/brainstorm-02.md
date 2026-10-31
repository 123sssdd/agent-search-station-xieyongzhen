# Brainstorm 02 平台记忆导出（脱敏，2026-10-31）

不含密钥、密码、cookie、token，也不含账号邮箱等个人标识。以仓库和 Notion 为准，本文件仅作恢复参考。

## 长期（profile）
- 与 BrainStorm 01 共同主持学习环路：用户内容 → 发散选题 → Searcher 搜索（所有链接都要核验）→ 质量评估两轮打分 → 主 bot 发排序清单 → 用户挑选。Sketchmind 看板（manifest.json）只由 Memory 写；问题提给优化规划师，由主 bot 决定；配图全部交给手绘风技术配图。流程文档：bot-instructions.md。
- 用户用中文交流；bot 之间可以中英混用，但发给用户的每条消息都只用简体中文（v3-25：代码、命令、路径、专有名词原文除外）。
- v2.2：每完成一项任务或交付，用中文通知用户（做了什么、路径、是否需要回复）。夜间 00:00–10:00 的通知合并到 10:00 后发，安全问题除外。同时回复派任务的 bot。（v3-26 已把 10:05 通知并入 01 的 10:00 早报。）
- v2.1 搜索计划：本人开轮时，先发搜索计划卡（档位、时长、领域、日期范围、目标条数、5–8 个关键词、平台、退出条件），10 分钟没回复就按默认开始；夜间不发卡。非开轮方根据证据批准饱和提前退出，并抽检 10%。
- v3：终审默认全面评审；结论先写进文件再发消息；评审、执行、待定都要报路径；Memory 归档消息一律 priority:true；日报按 9 项模板写。
- v3.1：Exa 只用于技术文章和 GitHub 仓库搜索，key 只从环境变量读，不打印也不保存；Reddit 不用 API，只通过 box 浏览器只读，不导出 cookie，不绕过封锁；被评条目自己的仓库不计入平台占比；Github 管家候选池用 good-first-issues 搜索。
- v3-27：许可证只要允许个人科研使用就算过线（含 NC），安全不再一票否决，可以在 box 上执行 skill 脚本；底线不变。
- 2026-10-29 14:30（01 转述）：用 cookie 的 skill 不再判不合规；slopornot、BypassAIGC 作为 humanizer 在实测 AI 检测站没通过后的备选；paperclip、qzcli 获批。
- v3-28：改流程、B 类规矩或做例会重大取舍之前先跑 grill-me，一般 2～4 轮；日常开轮执行不用。
- v3-30：例会改为每周六，兜底改为周日。已被 v3-31 取代：所有定时任务内容不变、时间待定、全部暂停。

## 近期（journal）
- 10-28 15:15：给 01 的 Notion 设计评审（沉淀条目和轮次分库，与 manifest 一一对应；用 manifest_id + content_hash 做 upsert；Notion 只读镜像；Memory 是唯一写入者）。
- 10-28 19:28 用户决定：终审默认全面评审；仓库公开并采用 NonCommercial 许可；Todos 状态改用 Notion 原生 status；Tavily 和 Bilibili 暂缓。
- 10-29 00:05：已提交日报 meetings/20261029/brainstorm02.md 和档案 profiles/brainstorm02.md；已评审优化规划师-0005 和 plan-20261029-0200-01（都没有阻断项）。
- 10-29 夜间轮次复核：0030-01、0200-01、0220-01、0236-01 都通过或有条件通过，文件在 decisions/round-*/02-*.md。
- 10-29 14:04：1345-01 有条件通过（decisions/round-20261029-1345-01/02-1403.md）。权重方案 A 后来被 standards/research-skills-selection.md 的最新口径取代。
- 10-30 20:16：1944-01 有条件通过（decisions/round-20261030-1944-01/02-2016.md），deja-vu 的 CLA 是误判，已改正。
- 10-31：零聊天审计缺口清单写在 decisions/chat-context-cost/02-gaps-20261031.md；context/brainstorm-02/ 已补齐。
