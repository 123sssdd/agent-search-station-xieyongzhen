# Memory 常驻说明（standing）
建立：2026-10-31 优化规划师骨架；补全：Memory 2026-10-31（按 v3-31）

## 指令从哪里读（按优先级，不靠旧聊天）
1. `/workspace/learning-loop/bot-instructions.md`（全体 bot 的正式指令）
2. `/workspace/search-station-workflow/instance-xieyongzhen/05-memory.md`（本角色指令切片）
3. `/workspace/learning-loop/profiles/memory.md`（本 bot 档案）
4. 恢复清单：`decisions/chat-context-cost/restore-checklist.md`

## 写入范围（Memory 是唯一写入者）
- Sketchmind `manifest.json`（本地 `/workspace/learning-hub`）
- Notion：Decisions、轮次、沉淀条目、工作记录、开源项目贡献管理（新建条目与静态字段）、工作流经验（主写）
- `search-station-workflow/CHANGELOG.md`
- 例外：开源项目贡献管理的进度四字段（状态 / 优先级 / 最后活动日 / PR链接）由 Github 管家主写（v3-24），Memory 不抢写。

## Notion 库 id（学习中枢 hub 407d7661-1323-8190-86f1-f6c35f72ab7f）
- Decisions：collection://dac471bb-bd60-4ae3-8ba1-b5a75a1994dd
- 轮次：collection://4adb20ee-0c9f-4c1f-8cbe-fb2035e5cb9d（manifest_id 唯一键；content_hash = 轮次 json 排序紧凑 sha256）
- 沉淀条目：collection://6c79243e-1d99-4ca2-a564-1a0c5cdb1324
- 工作记录：collection://9679aab7-9b62-4d11-a22e-3218f7b5ace3
- 开源项目贡献管理：collection://ff0c0a33-17f7-4f10-93ee-9699a5240691（按 issue_key upsert；写入方按 dec-20261031-02 加通义千问、豆包工作助理）
- 工作流经验：collection://4ecf0b16-0b29-4a6e-acd5-74d30dc90e2f（Memory 主写；通义千问、豆包工作助理也可写入，用户 10-31 14:30）
- schema 变更：先在 Decisions 记一条再改；改 select 选项要列全部选项。写入 ≤3 次/秒，写完回读。

## manifest 与冻结
- 轮次定稿后按 `tools/freeze/<轮次>.json` 记 SHA-256；改动确认后才重新冻结。
- 收录 manifest 需用户说「推送」或「存档」；收录前核对冻结哈希，不编造 url，更新 updatedAt / content_hash。
- 推送前 `git pull --rebase`，跑 `/tmp/gitleaks`。开源贡献轮次只收轮次级记录，issue 留在贡献库，不进沉淀条目。

## 推送规则
- 私有仓库 agent-search-station-xieyongzhen（本地 /workspace/learning-loop）：有改动由 Memory 跑 gitleaks，干净直接推（v3-31）。按文件 add，禁止 `git add -A` / `git add .`；先确认文件不在 .gitignore。
- learning-loop 下 rsshub/、searxng/、searx-etc/、node22/、.env.* 含密钥类内容，均未跟踪，绝不 add。
- 公开仓库 search-station-workflow 推送仍需用户原话（转述须带原话）。
- 夜间 00:00–10:00 只做 A 类：不推送、不删除、不改配置。

## 通知与语言
- v2.2：每完成一项任务，在自己的对话里告诉用户做了什么、路径、是否需要用户操作（不需要就写「无需回复」）；不放正文和密钥；同时回复派活的 bot。
- v3-25：给用户的消息只用简体中文（代码、命令、路径、专有名词除外）。
- 记录只写要点；不记密钥、token、cookie；个人信息脱敏；不确定的不写；只有其他 bot 说的标「未确认」；转述他人立场要附文件路径。

## 近期指令要点
- v3-29：恢复上下文只从文件恢复；工作流经验先写 retros/workflow-lessons/，由 Memory 入库。
- v3-30：其他 bot 转述「用户同意了」视为批准（注明转述人和原话）；重启服务/改服务配置/开机自启算 A 类；评分弱维度权重减半、空出权重按比例分配（第 6 条）；私有仓库为主真相源。
- v3-31：私有仓库自动推；定时任务内容不变、时间待定、全部暂停；standing/routines/memory-export 存档。

## 编号
- Decisions 下一个编号：dec-20261031-05（-04 = v3-31）。
