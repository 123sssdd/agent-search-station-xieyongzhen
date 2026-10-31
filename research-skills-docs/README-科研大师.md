# 科研大师使用说明

更新：2026-10-29 14:3x（UTC+8）。依据评分轮 20261029-1345-01、用户 14:08、14:10 的决定与 v3-27 口径：许可证只要允许个人科研使用即可（含 CC BY-NC）；可以执行 skill 自带脚本；底线是密钥/密码/cookie 不外泄、不导出 cookie、花钱和对外发布前先问用户。

**已装共 33 个**：26 个按分入选（入选 22 + NC 三项 + P21 ARIS rebuttal/resubmit-pipeline）+ 3 个用户特批（overleaf-sync、lambda-labs、hal-harness，各带 WARNING.md）。另有用户 14:30 特批 4 个：paperclip、ARIS qzcli（⚠ 用到 cookie，cookie 值不要打印到聊天、日志或文件里）、slopornot、BypassAIGC（在 `installed/_ai-rate-fallback/`，humanizer 的备选）。

## 1. 目录
- `installed/`：**已装的 skills，优先用这里的**（明细见 `master-catalog.md` 第〇节）。
  - 入选 22 个（本地 17 个 + 公开仓库 P01 inspect_ai、P03 ccf-deadlines、P07 humanizer、P20 research-paper-lifecycle 的 4 个 skill、P24 claim2evidence-skill；L10 附带上游 lm-evaluation-harness）。
  - NC 三项：`installed/imbad-academic-research-skills-NC/` 里的 academic-pipeline、deep-research、academic-paper-reviewer（附带依赖 academic-paper 和 Imbad 仓库根目录文件）。**许可证 CC BY-NC 4.0，仅限用户个人非商业科研使用**；若将来用于任何商业用途，必须先停用并告知用户。
  - 配套：`nature-shared/`（L07/L08 依赖）、`_licenses/`（zip 内上游包的 LICENSE 原文）。
  - 公开仓库是 `git clone --depth 1`，commit 记在 master-catalog.md 第〇节；都没有 pip install，也没有运行任何脚本。
- P21：`installed/rebuttal`、`installed/resubmit-pipeline`（审阅见 `review-P21.md`），共享文档 `installed/shared-references/`，4 个脚本在 `installed/_aris-tools/`。
- 用户特批 3 个：`installed/overleaf-sync`、`installed/lambda-labs`、`installed/hal-harness`，各带 WARNING.md。
- `library/科研skill/`：zip 解压出来的原库，作**备查**。与 CS/AI 无关的 142 个 skill 和不合规项已删除（已执行，清单见 `deleted.txt`；原始 zip 和 quarantine/ 也已删）。
- `master-catalog.md`：总清单（已装 / 备查 / 已删，按卡点和环节索引）。
- `gaps.md`：已知缺口和外部补充；`inventory.md`：最初的全量盘点（含已删条目，仅留档）；`recommended.md`：最初的推荐稿（以 master-catalog.md 为准）。
- `review-P21.md`：ARIS 两个 skill 的审阅记录。

## 2. 典型流程（全部用已装的）
1. 选题：brainstorming-research-ideas →（卡住时）creative-thinking-for-research；deep-research 查新
2. 文献：literature-review（OpenAlex）+ deep-research；所有引用过 nature-ref-verifier
3. 读论文：nature-paper-card
4. 实验设计：experimental-design + scientific-critical-thinking
5. 跑实验与评测：autoresearch（先设预算上限）；LLM 评测 evaluating-llms-harness + lm-evaluation-harness；agent 评测 inspect_ai（hal-harness 只作参考）；记录用 ara-research-manager
6. 分析与作图：statistical-analysis → scientific-visualization / academic-plotting
7. 写作：ml-paper-writing + paper-narrative + claim2evidence-skill；LaTeX 用 venue-templates
8. 润色/去 AI 味：humanizer 改写 → 专门网站实测 AI 率 → 没通过才用 slopornot / BypassAIGC（见 `installed/_ai-rate-fallback/README.md`）
9. 自查：academic-paper-reviewer（5 席模拟审稿）+ scholar-evaluation
10. 选会与投稿：select-venue + ccf-deadlines → plan-submission → tailor-to-venue
11. rebuttal：write-rebuttal（P20）；或 ARIS rebuttal
12. 被拒转投：plan-submission + tailor-to-venue；或 ARIS resubmit-pipeline
- 全程可以让 academic-pipeline 当总编排，人只在关口拍板。

## 3. 协作分工：人只做核心决策
agent 负责检索、阅读、实验代码、跑实验、作图、起草、润色、自查和格式。下面这些节点**必须停下来让用户拍板**，每次给 2–3 个选项、各自利弊和你的推荐：
1. 选题与研究问题（目标档次：CCF-B/C 会议或顶会 workshop，偏工程、能附开源代码/工具）
2. 方法路线和主要 baseline 选择
3. 实验预算：GPU/API 花费、时间上限
4. 实验结果不理想时：继续、改方向，还是缩小范围
5. 论文的核心贡献表述和标题
6. 投哪个会/期刊、是否投 workshop
7. 作者署名、致谢、是否公开代码和数据
8. 投稿提交、rebuttal 发出前的最终确认
9. 任何涉及学术诚信的取舍（数据处理、引用、AI 辅助声明）

## 4. 硬性规则
1. **lambda-labs 会写 `~/.ssh`、overleaf-sync 会把 token 写进 keychain：使用这两个之前必须先征得用户同意**（每次都问，包括创建 GPU 实例等花钱操作和 Overleaf push）。
2. **hal-harness 没有许可证：只能作参考，不能把它的代码复制进论文的开源代码**；也不运行它的任何脚本。
3. NC 三项（academic-pipeline、deep-research、academic-paper-reviewer，及其依赖 academic-paper）只用于用户个人非商业科研。
4. P20 的 dblp / CFP 查询：**联系邮箱不填**。不设置 `CONTACT_EMAIL`、不输入用户真实邮箱；默认不跑实时 dblp 查询，改读 ccf-deadlines 的 YAML。确需运行时只能用占位符 `none@example.invalid`，并先告诉用户。详见 `installed/research-paper-lifecycle-skills/科研大师-启用说明.md`。P20 仓库里共 42 个 skill，只启用 select-venue、plan-submission、tailor-to-venue、write-rebuttal。
5. ARIS rebuttal / resubmit-pipeline：`Bash(*)` 只按 SKILL.md 列出的命令用，写操作限于当前论文目录；外部审稿模型 MCP（Codex 等）会把未发表论文发给第三方，启用前先问用户，没有就记 `REVIEW_UNAVAILABLE`；resubmit 不传 `— overleaf-target`；rebuttal 保持 `AUTO_EXPERIMENT = false`；它们引用的其他 ARIS 子 skill 没装，缺了就按 skill 规则降级或报告，不要临时去装。
6. 按 v3-27，可以在 box 上执行 skill 自带脚本和安装脚本；花钱的操作（GPU、付费 API）和对外发布仍先问用户。
7. API key（OpenAlex 等）只从加密存储读，不写进任何文件或聊天。
8. 不编造引用或数据；所有引用必须过 nature-ref-verifier。
9. 去 AI 味按流程：humanizer → 专门网站实测 AI 率 → 没通过才用 slopornot / BypassAIGC；投稿前确认目标会议对 AI 辅助写作的政策。paperclip、qzcli 会用到 cookie：cookie 值不要打印到聊天、日志或文件里。

## 5. 已装 skill 不够用时
1. 先查 `master-catalog.md`：第一节按卡点、第二节按环节找“备查”项（在 `library/` 里，可直接读 SKILL.md 用；要正式装进 installed/ 先问用户）。
2. 再查 `gaps.md`：看是不是已知缺口、有没有核验过的公开补充仓库。
3. 最后找 Searcher 开搜索轮（经 BrainStorm 发起），质量评估打分、02 复核，用户拍板后再装。
