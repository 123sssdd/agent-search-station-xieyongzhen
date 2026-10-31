# 迁移指南（2026-11-01 01:56，BrainStorm 01）
用户目标：个人助理、资源收集、开源贡献团队、经验沉淀；工具：Hermes、千问/豆包、codex/grok build/Antigravity/deepseek cli、Notion、Obsidian；Grok Bot 只做并行短任务、多 bot 头脑风暴、云电脑动手；codex app 留给公司重型工作流。
总原则：Notion=结构化（待办/开源/资源库）；Obsidian=知识与经验（双链图谱）；私有仓库=规则与指令。
① 个人助理（Hermes+清单）：随手记→拆 Notion 待办（截止日/优先级/用时/能否交给 AI）→每天早上推今日三件→可交给 AI 的经 webhook 派给千问豆包（文字）或 codex/grok cli（代码）→回写结果、待验收→周日周报。
② 资源收集（千问豆包+Exa）：定时按关键词搜→去重→实用性/可信度/新鲜度打分→Notion 资源库；4 分以上去 AI 味后写 Obsidian 白话笔记加 [[双链]]。打分标准沿用 standards/。
③ 开源（Hermes 调度，codex/grok 干活）：每天 gh 搜（good-first-issues>=3，Py/TS/Go/Java，1k-10k star，3 个月内活跃）→打分写 Notion→每周方案卡 1-2 个→用户回「做」→codex fork/改/测/PR 草稿→用户看后提交→Hermes 跟踪评论与 CI。提交 PR、发评论、签 CLA 前必须等用户回复。
④ 经验沉淀（Hermes+Obsidian，豆包去 AI 味）：统一格式（踩坑=症状/原因/解法；原则=一句话/什么时候用/什么时候不用），自动加 3-5 个双链，每月合并相似条目、标出过时条目。
接入顺序：Hermes 个人助理 → 千问豆包资源收集 → 开源跑一个真实 issue → 经验沉淀。旧情报站 bot 停用，仓库和 Notion 保留。
