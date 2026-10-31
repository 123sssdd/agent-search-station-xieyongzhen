# Github 管家 平台记忆导出（2026-10-31 14:58，v3-31）
已去掉密钥、密码、cookie、token。原文是英文的条目已译成中文。标「已过时」的条目以括号里的新规则为准。

## 长期事实（profile）
1. 用户要求所有沟通只用简体中文，包括总结、转述、进度。
2. 开源贡献的代码由 copilot bot（id 9f52b10e-b4a6-44c5-9487-a98a33adf77f）写；用户告诉我提交了哪些代码 / PR，我记进度。
3. 2026-10-29 用户直接分派：帮他找可贡献的开源项目和 issue，方法见档案（gh search + Exa，good-first-issues>=3，help wanted 兜底；v3-18、v3-21）。skills/工具评估仍走 Searcher → 质量评估。
4. 用户批准用 Exa 补充候选池：POST https://api.exa.ai/search，请求头 x-api-key 从环境变量 EXA_API_KEY 取；不得打印或写出密钥；每次调用在档案 Exa 节记用量。
5. 开源流程定稿（decisions/oss-contrib/01-final-20261029-0315.md）：我写搜索方案；首轮 B 档（Searcher → 质量评估 → 另一 BrainStorm 复核），之后 C 档由我只读 gh search；我排优先级、管进度、维护 registry.json；Memory 按 issue_key 同步 Notion；copilot 写代码；7 天无进展标阻塞，14 天建议放弃；每周最多认领 1～2 个。（原文写「fork 是 B 类」，已过时：v3-24 起 fork 为 A 类。）
6. v3-24（2026-10-29 03:16 用户原话经 01 转达）：我可直写 Notion 开源库的进度字段（状态、最后活动日、PR链接、优先级）；新建条目和其他字段由 Memory 写；fork 可直接做；push、PR、评论、issue、CLA 仍须用户确认草稿。
7. 2026-10-29 起我是 BrainStorm 01 的 00:00 例会常驻成员：日报九项 + 第十项「开源贡献进展」；只读研究是 A 类，以用户身份的 GitHub 写操作是 B 类；不写密钥；00:00–10:00 的通知攒到 10:00 后发。文件放 /workspace/learning-loop/。
8. 2026-10-29 用户决定周一例会不开、周四照常。（已过时：v3-31 起例会与定时任务时间全部待定、全部暂停，由用户决定。）
9. 「2026-10-29 起我不得自己搜索 skills/工具/项目」（已过时，口径已统一：skills/工具搜索走 Searcher；开源首轮 B 档、增量 C 档由我只读 gh search）。安装连接器、改配置是 B 类。
10. 2026-10-29 03:10 用户提出新开源流程并建议建 Notion「开源项目贡献管理」库（已由第 5 条定稿取代）。
11. 2026-10-30 19:44：改贡献方向 / 仓库优先级 / 首轮池标准前先跑 grill-me（2～4 轮）；日常 gh search 增量不用。
12. 2026-10-30 19:44：开源贡献库与学习中枢并列拆分；我主写进度字段；学习中枢不管贡献进度。
13. 2026-10-30 20:18：用户暂无时间做开源；1944-01 候选先入库、时间待定；本周不认领；CLA/语言问题暂不催。
14. 2026-10-30 20:21：愿意签 CLA；主攻前端 + agent（Python，含 LangChain），会 Java（Spring Boot）和 Go，相关仓可进池；1944-01 只是测试工作流。
15. 2026-10-31 14:07：Notion 开源表新增 issue 打开时间、分配情况；默认按打开时间倒序；Stars记录日改名 issue记录日；写入方为 Memory / 通义千问 / 豆包工作助理，我仍主写进度字段。拟由千问改表。

## 近期经过（journal 摘要，按时间）
- 10-30 19:44 首轮池 B 档开跑，方案 decisions/oss-contrib/plan-20261030-1944.md。
- 10-30 20:07 Searcher 回传 25 条（rounds/oss-20261030-1944-01.md）。
- 10-30 20:14 质量评估草案：入选 21，临界 higress、garak，不入选 cuga-agent、alumnium；我写了优先级草案 priority-draft-20261030-2014.md。
- 10-30 20:17 复核定稿（eval sha256 前缀 97f31634）；deja-vu 更正为无 CLA；写了 registry.json（21 + 2）。
- 10-30 20:18 按用户原话全部「待定」、不认领。
- 10-30 20:21 Notion 新建 23 条、失败 0。
- 10-31 14:3x 补写 context 文件；核对 registry 与 Notion 一致（2 条 CLA 后由 Memory 修正）；缺口清单 decisions/chat-context-cost/github-steward-gaps-20261031-1430.md。
- 10-31 14:3x 档案搜索口径统一；写了指令切片（现在 instance/09-github-steward.md）。
- 10-31 14:49 依用户 14:45 原话建私有仓库 123sssdd/agent-search-station-xieyongzhen 并推送 96b8f43（492 个文件，gitleaks 0 条）。
- 早前：在 zhu1090093659/dsh-web#1970 发过两条评论（issuecomment-6474521571、6475400817）。
