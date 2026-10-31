# Github 管家｜仅靠仓库 + Notion 恢复的缺口清单（2026-10-31 14:3x）

## A. registry 与 Notion 核对结果
- 条数：本地 23 / Notion 23，issue_key 一一对应，无单边条目。
- 状态、优先级、语言、Stars、Issue 链接全部一致。
- **不一致 2 条（CLA要求）**：`AgenticResourceRegistry/AgenticResourceRegistry#1971`、`IBM/mcp-context-forge#5986`，本地为「需 CLA」，Notion 为未勾选。以 eval 定稿为准应为「需 CLA」。CLA 字段不属我主写，需 Memory（或千问）修正。
- Notion「关联轮次」relation 为空：轮次库里还没有 1944-01 页，只在备注写了 round_id。
- **registry.json 只在本地**：`/workspace/learning-loop/` 不是 git 仓库，search-station-workflow 仓库里没有 registry、oss-contrib、profiles、context 等文件。删掉 box 后只剩 Notion 镜像，registry 专有字段会丢（排序、eval 均分、适合理由、风险、未指派 gfi/hw、示例 issue 列表、week_plan、user_prefs、pending_user_B）。

## B. 只在记忆/聊天里、文件或 Notion 缺失或不全的内容
1. 例会安排：用户 2026-10-29 决定 11-02（周一）例会不开、11-05（周四）照常。文件里只有「待用户决定」，没有结论。
2. 已发的 GitHub 写操作：在 zhu1090093659/dsh-web#1970 发过 2 条评论（issuecomment-6474521571、-6475400817）。档案只写了「已发 dsh-web#1970 评论」，没有链接。
3. 档案自相矛盾：`profiles/github-steward.md` 第 94 行写「本角色不再自行做搜索调研」，与 01-final 的 C 档「管家只读跑 gh search」冲突。应改为「skills/工具的搜索走 Searcher；开源增量 C 档由管家只读 gh search」。
4. 本角色没有指令切片：`search-station-workflow/instance-xieyongzhen/` 下有 01–08、90 号文件，但没有 github-steward。bot-instructions.md 里的 v3-18/21/24/28 是零散条款。
5. 我的定时任务：原 10:05 那个已删除，现在没有任何定时任务（只记在 meetings/20261029/routines-inventory.md）。
6. 1944-01 的定性：用户 20:18、20:21 的两次拍板（暂无时间、仅测流、全部待定；愿签 CLA；主攻前端+agent/Python/LangChain，Java/Go 可进池）只写进了本地 registry、档案、草案和 Notion 备注，没有进 Decisions 库或 bot-instructions。
7. 2026-10-31 14:07 的 Notion 字段变更要求（新增 issue 打开时间、分配情况；改名；默认排序；写入方加千问/豆包）只记在我的档案和 schema 笔记里，执行状态未知。
8. 中文硬规则 + 00:00–10:00 静默：在档案和共享记忆里都有，但 standing.md 之前是空的（本次已补）。

## C. 本次已补
- `context/github-steward/standing.md`（38 行）、`active.md`（4 行）。

## D. 建议（供优化规划师并入审计）
1. 把 `oss-contrib/registry.json`、`profiles/github-steward.md`、`context/github-steward/`、`decisions/oss-contrib/` 纳入 search-station 仓库（脱敏后），推送属 B 类。
2. 在 instance-xieyongzhen 增加 github-steward 指令切片（如 09-github-steward.md）。
3. 请 Memory 修正 2 条 CLA 字段，并在轮次库建 1944-01 页后补 relation。
4. 把 B 节第 1、6、7 条写进 Decisions 库。
