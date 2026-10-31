# 「零聊天依赖」全面审计（优化规划师牵头，2026-10-31）

## 1. 一句话结论
现在还做不到。大部分内容是写成了文件，但都放在 box 本地的 `/workspace/learning-loop/` 里（这个文件夹不是 git 仓库，从没推送到远端）。GitHub 上的 search-station-workflow 只有 10/29 以前的一部分内容；各 bot 的记忆存在平台那边；连接器授权和登录也只能手动重建。如果现在把 box 和所有 bot 都删掉，最近两天的轮次、决策和 context/ 目录都会丢。差距大约是：一次私有仓库推送 + 把记忆导出成文件 + 一份人工步骤清单。

## 2. 盘点表
图例：「box」= 只在 box 本地文件，没进 GitHub；「GitHub(旧)」= 仓库里有，但是 10/29 的版本；「平台」= 存在 Grok Bot 平台里（记忆、定时任务），没有文件。

| bot | 指令全文 | 记忆要点 | 定时任务 | 待办 | 轮次 | 决策 | 经验 | 标准 | registry（技能登记表） | 连接器配置 |
|---|---|---|---|---|---|---|---|---|---|---|
| BrainStorm 01 | box 有 bot-instructions.md（到 v3-29）；GitHub(旧) 有 instance 切片 01 | 平台，未导出 | 平台；清单里没有 01 那一行，待自报 | Notion Todos 库 | box rounds/、decisions/round-* | box decisions/；Notion Decisions（由 Memory 写） | box retros/workflow-lessons/（刚建，空） | 不适用 | 待 Github 管家自报 | 平台，待自报 |
| Brainstorm 02 | 同上，切片 02 | 平台 | 平台；清单记录：每日 00:40（03:23 后可能已改，待自报） | Notion Todos | 不适用 | box | box | 不适用 | 不适用 | 平台，待自报 |
| Searcher | 同上，切片 03；box profiles/searcher.md | 平台 | 平台：周五 00:40 | Notion Todos | box rounds/plan-*、search-*（没推送） | box | box | box standards/（模板 GitHub(旧)） | 不适用 | 平台；Exa 密钥在环境变量 |
| 质量评估 | 切片 04；box profile | 平台 | 平台：清单记录每日 00:40，待自报 | Notion Todos | box rounds/eval-* | box | box | box standards/ | 不适用 | 待自报 |
| Memory | 切片 05 | 平台 | 平台：每日 00:40 | Notion Todos | 不适用 | Notion Decisions/工作记录（唯一写入者） | Notion「工作流经验」库已于 10/31 14:17 建好（决定 dec-20261031-01） | 不适用 | manifest.json，待自报 | Notion 授权在平台 |
| Todos | 切片 08 | 平台 | 平台：周二/周五 00:40 | Notion Todos（唯一写入者） | 不适用 | 不适用 | box | 不适用 | 不适用 | Notion 授权在平台 |
| 优化规划师 | 切片 06；box profiles/optimizer.md | 平台 | 平台：周五 00:40（03:23 后已改） | Notion Todos | 不适用 | box decisions/（多数没推送） | box | box standards/_template.md（GitHub 里是旧版） | 不适用 | 只读 Notion |
| Github 管家 | GitHub(旧)：instance 里没有单独切片，待自报 | 平台 | 平台：清单写「无」 | Notion Todos | box rounds/oss-* | box decisions/oss-contrib/ | box | 不适用 | 待自报（推测在仓库 skills/） | GitHub 授权在平台 |
| 手绘风技术配图 | 切片 07 | 平台 | 平台：每日 00:40 + 每日 10:05（03:23 后可能已改，待自报） | Notion Todos | 不适用 | 不适用 | box | 不适用 | 不适用 | Excalidraw 连接器在平台 |
| 科研大师 | 没找到指令文件和 profile，待自报 | 平台 | 清单里没有，待自报 | 待自报 | 待自报 | 待自报 | 待自报 | 待自报 | 待自报 | 待自报 |

### 按类别汇总
| 类别 | 现在的真相源 | 进 GitHub/Notion 了吗 | 缺口 |
|---|---|---|---|
| 指令全文 | box bot-instructions.md | GitHub 只有到 v3 左右的注释版和切片；v3.1、v3-24 到 v3-29 没有 | 要推送 |
| 记忆要点 | 平台记忆 | 都没有 | 要导出成文件 |
| 定时任务 | 平台；清单文件 meetings/20261029/routines-inventory.md 已经过时 | 没有 | 要重新自报，并写成文件 |
| 待办 | Notion Todos | 已进 Notion | 基本可以 |
| 轮次 | box rounds/、decisions/round-* | 没有 | 要推送 |
| 决策 | box decisions/ + Notion Decisions | 部分进了 Notion，完整版在 box | 要推送 |
| 经验 | box retros/（刚建） | Notion 库还没建 | 等用户批准建库 |
| 标准 | box standards/、keywords/ | GitHub(旧) | 要推送 |
| registry | 待 Github 管家自报 | 待自报 | 待自报 |
| 连接器配置 | 平台授权 | 永远进不了文件 | 列成人工步骤（第 4 节） |

## 3. 关键问题
**3.1 有没有推到远端？没有。** 证据：
- `/workspace/learning-loop/` 不是 git 仓库（`git remote` 报错「not a git repository」），所以 context/、rounds/、decisions/ 从来没有推送过。
- 仓库 `/workspace/search-station-workflow/`：远端是 GitHub 上的 search-station-workflow，分支 main，跟远端一致，没有未推送的提交；最新提交是「夜间产出：standards/关键词模板…」（10/29）。只有 CHANGELOG.md 有一处本地修改没提交。
- 仓库里没有 `context/`、`retros/workflow-lessons/`、`decisions/chat-context-cost/`，也没有 restore-checklist.md。

**3.2 公开仓库的风险。** 用 GitHub 命令行只读查过：仓库是**公开（PUBLIC）**的。在 `instance-xieyongzhen/` 里查到带 UUID 格式（一长串 8-4-… 的编号，可能是 agent 编号或 Notion 库编号）的文件 11 个：
- notion-ids.md（5 处）
- _instance/bot-instructions-v2.1.md（16 处）
- _instance/01-brainstorm-01.md（3）、_instance/02-brainstorm-02.md（3）、_instance/03-searcher.md（2）、_instance/04-quality-eval.md（2）、_instance/05-memory.md（1）、_instance/06-optimizer.md（2）
- bot-instructions-v3-annotated.md（1）、_instance/bot-instructions-v3-annotated.md（1）、90-search-plan.md（1）

邮箱格式没有查到。另外还有 sites-to-login.md（要登录的网站清单），算个人信息，建议一起挪走。这些已经在公开历史里，只删文件不够，彻底清掉要改写 git 历史，必须用户决定。

**3.3 私有仓库方案（只出方案，建仓和推送都要用户原话）**
- 仓库名：learning-loop-private（GitHub 私有）。
- 放：bot-instructions.md 全文、instance 切片（含编号）、profiles/、context/、rounds/、decisions/、standards/、keywords/、meetings/、retros/、roadmap.md、memory-export/、notion-ids.md、sites-to-login.md、routines.md（定时任务清单）。
- 不放：密钥、token、cookie、密码（只写环境变量名）；日志 *.log；安装出来的软件目录（node22、searxng、rsshub、nv、tools、tmp0030 等）；大文件。用 .gitignore 挡住。
- 目录：直接用现在 learning-loop/ 的结构，加 memory-export/ 和 routines.md。
- 和公开仓库怎么同步：公开仓库只放通用模板（templates/、schemas/、adapters/、脱敏后的说明）。私有仓库改了通用部分，由 Github 管家脱敏后拷到公开仓库；方向只能私有→公开，不能反过来带出个人数据。
- 谁写：Github 管家负责提交和推送；CHANGELOG 仍由 Memory 写。

## 4. 文件永远替代不了、必须人工重建的部分
| 项目 | 恢复步骤 | 谁做 |
|---|---|---|
| bot 本体（名字、头像、角色） | 在 Grok Bot 平台新建 bot，取原名，把私有仓库里对应的指令切片贴进指令 | 用户（建 bot），01 提供清单 |
| 平台记忆 | 新 bot 读 memory-export/<bot>.md，自己写回记忆 | 各 bot |
| 定时任务 | 按 routines.md 逐条重建 | 各 bot，建完回报 01 |
| 连接器授权（Notion、GitHub、Google Drive、Excalidraw 等） | 在平台连接器页面重新授权，选同一个 Notion 工作区和 GitHub 账号 | 用户本人点授权 |
| box 浏览器登录（如 Reddit 用 Google 账号登录） | 在 box 浏览器登录，两步验证由用户完成；网站清单见 sites-to-login.md | 用户 |
| 密钥 | 重新设置环境变量，例如 EXA_API_KEY、Firecrawl 的密钥、GITHUB_TOKEN；值只由用户填，不进文件 | 用户 |
| box 上装的软件（SearXNG、RSSHub 等） | 按仓库 scripts/ 里的安装脚本重装 | Github 管家/Searcher |
| Notion 数据库本身 | 平时就在 Notion 里，不用重建；只有误删时才按 notion-ids.md 和 schema 文件重建 | Memory |

## 5. 补齐计划
| 谁 | 补什么 | 优先级 | 依赖 | 要用户确认吗 |
|---|---|---|---|---|
| 用户 | 同意建私有仓库并推送；决定要不要清理公开仓库的历史 | P0 | 无 | 要 |
| Github 管家 | 建 learning-loop-private、写 .gitignore、首次推送 | P0 | 用户原话 | 要 |
| Github 管家 | 把公开仓库 instance-xieyongzhen/ 挪到私有仓，公开仓库只留脱敏版 | P0 | 私有仓 | 要（改写历史更要） |
| 各 bot | 自报当前定时任务（03:23 以后的）和记忆要点 | P0 | 无 | 不要 |
| Memory | 汇总成 memory-export/<bot>.md（只写要点、脱敏）和 routines.md | P0 | 各 bot 自报 | 不要 |
| 优化规划师 | 维护这份审计和 restore-checklist.md（已加人工步骤节） | P0 | 无 | 不要 |
| Brainstorm 02 | 复核 bot-instructions.md 和切片是不是一致，补 Github 管家、科研大师的切片 | P1 | 无 | 改指令要 01 拍板 |
| 各 bot | 补全 context/<bot>/standing.md | P1 | 无 | 不要 |
| Memory | Notion「工作流经验」库已建好；还剩「独写还是主写」等 01 确认 | P1 | 01 确认 | 否 |
| Github 管家 | 写清 registry 在哪、怎么恢复 | P2 | 私有仓 | 不要 |

## 6. 「只读清单恢复」dry-run 设计
- 做法：新开一个临时会话（或临时 bot），只给它私有仓库链接、Notion 链接和 restore-checklist.md，不给任何聊天记录。让它扮演 Searcher，恢复后完成一项标准任务：按搜索方案写一份 C 档（30 分钟以内）的 plan 文件。
- 谁执行：Brainstorm 02 出题和比对，优化规划师记录结果；临时 bot 要用户创建。
- 验收（和原 Searcher 的产出比）：
  1. 文件名和轮次编号格式对；
  2. 档位和默认时长对（C 档 30 分钟，A/B 档 45 分钟）；
  3. 用了 site: 问句模板；
  4. 许可证、安全按 v3-27 和 14:30 的口径；
  5. 没有往聊天、Notion、仓库里写密钥；
  6. 不需要问「之前聊过什么」就能开工；
  7. 遇到要花钱或对外发布的步骤会停下来问用户。
- 要用户确认的步骤：创建临时 bot、给它连接器授权、dry-run 结束后删除它。
- 前提：私有仓库已经推送，否则只能用 box 本地路径试跑，算「半程 dry-run」。

---

## 附：Github 管家自报的缺口（2026-10-31 14:32 并入）
来源：`github-steward-gaps-20261031-1430.md`（Github 管家自己写的缺口清单）
1. 开源项目登记表 `registry.json` 只在本地，GitHub 仓库里没有。Notion 和本地各 23 条，但有 2 条的 CLA（贡献者协议是否已签）字段对不上，需要 Github 管家和 Memory 对齐。
2. 下面这些只存在于记忆或聊天里，还没有文件：11 月 2 日例会不开、11 月 5 日照常开；dsh-web 项目 1970 号 issue 下两条评论的链接；本角色还没有单独的指令切片。
3. 管家档案里写着「不自行搜索」，但开源流程又让它用 gh search 做快速补充搜索，两处互相矛盾，需要 01 统一口径。
4. 10 月 30 日 20:18、20:21 两次拍板，以及 10 月 31 日 14:07 的字段变更，还没记进 Notion 的 Decisions 库，需要 Memory 补记。
5. Github 管家的 `context/github-steward/standing.md` 和 `active.md` 已经补好。

补齐计划追加：
| 谁 | 补什么 | 优先级 |
|---|---|---|
| Github 管家 + Memory | 对齐 2 条 CLA 字段；registry.json 随私有仓库一起推送 | P0 |
| Memory | 补记三条拍板和字段变更到 Decisions | P0 |
| 01 | 统一「不自行搜索」和 C 档 gh search 的口径；写 Github 管家指令切片 | P1 |
| Github 管家 | 把例会安排、评论链接写进 active.md 或 journal | P1 |

---

## 附：Brainstorm 02 自报的缺口（2026-10-31 14:34 并入）
来源：`02-gaps-20261031.md`（02 自己核对过的 7 条）
1. 02 的兜底定时任务已经改成每周二、周五 00:40。02 说用户 10/29 03:28 在它的聊天里确认过「以后固定两次例会」，但正式指令 v3-26、02 的档案和定时任务清单都没更新。**优化规划师自己的兜底任务目前是「只在周五」，而且显示「已暂停」，是谁停的、为什么停，没有任何记录。**
2. 02 的兜底任务也是「暂停」，同样没有记录。
3. 02 在 10/30 20:04 发给 01 的零聊天恢复意见没有落盘。
4. 02 的分享模板草稿还在等用户确认，文件和 Todos 里都没有记录。
5. 「其他 bot 说用户同意了不算批准」这条只在推送规则里写过，还没有写成适用于所有动作的通用条文。
6. 「用原命令重启服务算可直接做（A 类），改配置或设自启动要用户确认（B 类）」没写进 A/B 分类列表。
7. 「弱维度空出来的权重默认按比例分给其他维度」没有条文；用 cookie 的 skill 合规、slopornot 和 BypassAIGC 作为备选，这些只写在 Searcher 档案和 1345-01 轮次的裁定里，正式指令没写（算半个缺口）。
另：`profiles/github-steward.md` 第 11 行有 GitHub 账号名，进公开仓库前要打码。

补齐计划追加：
| 谁 | 补什么 | 优先级 |
|---|---|---|
| 01 | 定下兜底任务是「周五」还是「周二+周五」并改 v3-26；查明各 bot 兜底任务被暂停的原因并记录 | P0 |
| 01 | 把第 5、6、7 条写成正式条文 | P1 |
| 02 | 补写 10/30 恢复意见和分享模板草稿的文件 | P1 |
| Github 管家 | 档案里的账号名打码 | P0（推公开仓库前） |

### 进展（2026-10-31 14:36，Github 管家回报）
- 例会安排（11 月 2 日不开、11 月 5 日照常）和 dsh-web 项目 1970 号 issue 的两条评论链接，已写进 `context/github-steward/active.md`。
- 「不自行搜索」和自己用 gh search 的口径矛盾，管家说已经修正。指令切片放在 `instance-xieyongzhen/09-github-steward.md`，还没推送。
- 2 条 CLA 字段，管家说 Notion 那边已经一致了。

### 已转为待办（2026-10-31 14:49，Todos 写入 Notion）
| 待办编号 | 内容 | 优先级 | 负责 | 计划日 |
|---|---|---|---|---|
| todo-20261031-01 | 公开仓库清理（需用户确认；改写历史另问） | P0 | Github 管家 | 11-05 |
| todo-20261031-02 | 恢复抽测 dry-run（临时 bot 增删需用户确认） | P1 | 优化规划师设计、01 组织 | 11-06 |
| todo-20261031-03 | 私有仓库建仓并推送（需用户确认） | P0 | Github 管家 | 11-05 |
| todo-20261031-04 | 平台记忆脱敏导出 | P1 | Memory | 11-06 |
| todo-20261031-05 | 重收定时任务清单 | P1 | 01 | 11-06 |
| todo-20261031-06 | 科研大师补指令切片和档案 | P1 | 科研大师 | 11-06 |
| todo-20261031-07 | 补记 Decisions | P0 | Memory | 11-05 |
| todo-20261031-08 | 02 补写草稿 | P2 | 02 | 11-07 |
