# 科研 skills 总清单（已装 / 备查 / 已删，按环节与卡点索引）

更新：2026-10-29 14:3x（UTC+8），依据评分轮 20261029-1345-01（`/workspace/learning-loop/rounds/eval-20261029-1345-01.md`）、用户 14:08、14:10 的决定和 v3-27 口径（许可证只要允许个人科研使用即可；可以执行 skill 自带脚本；底线：密钥/密码/cookie 不外泄、不导出 cookie、花钱和对外发布先问用户）。上一版留档在 `_work/master-catalog.before-20261029-1415.md`。

状态图例：✅ 已装（在 `/workspace/research-skills/installed/`）；⚠✅ 已装（有风险提示，看 WARNING.md）；备查 = 留在 `library/` 里，没装；🗑 已删除。

> **当前实际状态**：已全部执行完毕——按 deleted.txt 删除 711 项、删除原始 zip 和空的 quarantine/；P21 两个 skill 及 3 个风险项已在 `installed/`。已装共 33 个（26 个按分入选 + 3 个用户特批 + 4 个用户 14:30 特批）。

## 〇、已装清单

### 按分入选 26 个（入选 22 + NC 三项 + P21，均已在 installed/）

| ID | 名称 | 环节 | 路径 | 来源 @ commit | 许可证 | 备注 |
|---|---|---|---|---|---|---|
| L08 | nature-ref-verifier | 文献/自查（防编造引用） | `installed/nature-ref-verifier` | Yuan1z0825/nature-skills（zip） | Apache-2.0 | 所有引用必须过它 |
| L15 | ml-paper-writing | 写作 | `installed/ml-paper-writing` | Orchestra AI-Research-SKILLs（zip） | MIT | 含 NeurIPS/ICML/ICLR/ACL LaTeX 模板 |
| L10 | evaluating-llms-harness | LLM 评测 | `installed/evaluating-llms-harness` | Orchestra（zip） | MIT | 上游框架见 lm-evaluation-harness |
| P32 | lm-evaluation-harness（随 L10） | LLM 评测框架 | `installed/lm-evaluation-harness` | github.com/EleutherAI/lm-evaluation-harness @ d6de81643928 | MIT | 框架源码；需 pip+GPU/API，安装待用户同意 |
| P07 | humanizer | 去 AI 味（英文） | `installed/humanizer` | github.com/blader/humanizer @ 0ef9fe5bc357 | MIT | 只用于润色最后一步，不用于规避检测 |
| L03 | brainstorming-research-ideas | 选题 | `installed/brainstorming-research-ideas` | Orchestra（zip） | MIT |  |
| L24 | ara-research-manager | 科研管理/溯源 | `installed/ara-research-manager` | Orchestra（zip） | MIT |  |
| P20 | research-paper-lifecycle（select-venue / plan-submission / tailor-to-venue / write-rebuttal） | 选会/投稿/rebuttal/转投 | `installed/research-paper-lifecycle-skills/skills/{select-venue,plan-submission,tailor-to-venue,write-rebuttal}` | github.com/ShaishavMaisuria/research-paper-lifecycle-skills @ cf30d6452cc6 | Apache-2.0 | 仓库共 42 个 skill，只启用这 4 个；dblp 邮箱不填，见该目录“科研大师-启用说明.md” |
| P01 | inspect_ai | agent 评测底座 | `installed/inspect_ai` | github.com/UKGovernmentBEIS/inspect_ai @ 2f78dcb29eb0 | MIT | 框架；需 pip、Docker、模型额度，安装待用户同意 |
| L04 | creative-thinking-for-research | 选题卡点 | `installed/creative-thinking-for-research` | Orchestra（zip） | MIT |  |
| L07 | nature-paper-card | 读论文 | `installed/nature-paper-card` | nature-skills（zip） | Apache-2.0 | 依赖 installed/nature-shared |
| L12 | statistical-analysis | 数据分析 | `installed/statistical-analysis` | K-Dense（zip） | MIT |  |
| L14 | scientific-visualization | 画图 | `installed/scientific-visualization` | K-Dense（zip） | MIT |  |
| L21 | scholar-evaluation | 审稿自查 | `installed/scholar-evaluation` | K-Dense（zip） | MIT |  |
| L18 | venue-templates | 排版/LaTeX 模板 | `installed/venue-templates` | K-Dense（zip） | MIT |  |
| L13 | academic-plotting | 画图 | `installed/academic-plotting` | Orchestra（zip） | MIT | 可选 GEMINI key |
| P03 | ccf-deadlines | 截稿/CCF 分级 | `installed/ccf-deadlines` | github.com/ccfddl/ccf-deadlines @ 2e5a397ce363 | MIT | 数据仓库（YAML），直接读 conference/ 下文件 |
| L06 | literature-review（OpenAlex） | 文献检索 | `installed/literature-review` | HughYau/AcademicForge（zip） | MIT | 需 OPENALEX_API_KEY（从加密存储读） |
| P24 | claim2evidence-skill | 写作（实验日志→论述） | `installed/claim2evidence-skill` | github.com/Gatsby0916/claim2evidence-skill @ 34684f6baa18 | MIT |  |
| L17 | paper-narrative | 故事线 | `installed/paper-narrative` | AcademicForge（zip） | MIT |  |
| L09 | experimental-design | 实验设计 | `installed/experimental-design` | aiming-lab/AutoResearchClaw（zip） | MIT |  |
| L02 | autoresearch | 自动跑实验 | `installed/autoresearch` | Orchestra（zip） | MIT | 会自主消耗 GPU/API，先设预算上限 |
| L22 | scientific-critical-thinking | 卡点排查 | `installed/scientific-critical-thinking` | qinyan-academic-skills（zip） | MIT |  |
| L01 | academic-pipeline（NC） | 全流程编排 | `installed/imbad-academic-research-skills-NC/academic-pipeline` | Imbad0202/academic-research-skills（zip） | CC BY-NC 4.0 | 仅限个人非商用；依赖同目录 deep-research、academic-paper、academic-paper-reviewer |
| L05 | deep-research（NC） | 深度调研/查新 | `installed/imbad-academic-research-skills-NC/deep-research` | Imbad（zip） | CC BY-NC 4.0 | 仅限个人非商用 |
| L20 | academic-paper-reviewer（NC） | 模拟审稿（5 席） | `installed/imbad-academic-research-skills-NC/academic-paper-reviewer` | Imbad（zip） | CC BY-NC 4.0 | 仅限个人非商用 |

配套（不单独计数）：

- nature-shared：`installed/nature-shared` — L07/L08 的共享资源（../nature-shared 相对引用）
- academic-paper（NC，L01 的依赖）：`installed/imbad-academic-research-skills-NC/academic-paper` — academic-pipeline 的写作/修改阶段要用；不单独算入选
- Imbad 仓库根目录文件：`installed/imbad-academic-research-skills-NC/{shared,docs,scripts,agents,tools,skills,commands,LICENSE,NOTICE.md,README*…}` — NC 三项的相对引用（../../shared 等）需要；未带 evals/tests/examples/hooks/.claude/.github
- _licenses/：`installed/_licenses` — zip 内 6 个上游包的 LICENSE 原文

### P21 ARIS rebuttal + resubmit-pipeline（计 1 项，含 2 个 skill，已在 installed/）

| ID | 名称 | 环节 | 路径 | 来源 @ commit | 许可证 | 备注 |
|---|---|---|---|---|---|---|
| P21 | rebuttal（ARIS） | OpenReview 式 rebuttal | `installed/rebuttal` | ARIS @ a3a847b421c6 | MIT | 审阅通过（review-P21.md），已装；共享文档 `installed/shared-references`，脚本 `installed/_aris-tools/` |
| P21 | resubmit-pipeline（ARIS） | 被拒后转投 | `installed/resubmit-pipeline` | ARIS @ a3a847b421c6 | MIT | 同上；不传 overleaf-target |

### ⚠✅ 用户特批（3 个，各带 WARNING.md，用户 14:10 同意）

| 来源分类 | 名称 | 用途 | 位置 | 来源 @ commit | 许可证 | 风险与规则 |
|---|---|---|---|---|---|---|
| b1 | overleaf-sync（ARIS） | LaTeX/Overleaf 协作 | `installed/overleaf-sync` | ARIS @ a3a847b421c6 | MIT | ⚠ 会把 token 写进 keychain；使用前必须征得用户同意 |
| b1 | lambda-labs | 租云 GPU 跑实验 | `installed/lambda-labs` | Orchestra（zip） | MIT | ⚠ 会写 ~/.ssh、会花钱；使用前必须征得用户同意 |
| P31 | hal-harness | agent 评测参考 | `installed/hal-harness` | github.com/princeton-pli/hal-harness @ 16bb03ebc115 | 无许可证（已归档） | ⚠ 只能作参考，不能把代码复制进论文的开源代码 |

合计：已装 33 个 = 按分入选 26 个（入选 22 + NC 三项 + P21）+ 用户特批 3 个 + 用户 14:30 特批 4 个。已用 `installed/` 实际目录核对。

### 用户 14:30 特批（4 个，来源/commit/许可证见 `installed/_licenses/SOURCES-1430.md`）

| 名称 | 用途 | 路径 | 来源 @ commit | 许可证 | 备注 |
|---|---|---|---|---|---|
| paperclip | 用浏览器登录态下载付费论文全文 | `installed/paperclip` | github.com/K-Dense-AI/scientific-agent-skills @ 5f2bc0341354 | MIT | ⚠ 用到 cookie：cookie 值不要打印到聊天、日志或文件里 |
| ARIS qzcli | 平台账号同步/查询 CLI | `installed/qzcli` | ARIS @ a3a847b421c6 | MIT | ⚠ 用到 cookie：不要运行 `qzcli cookie --show`，cookie 值不要打印到聊天、日志或文件里 |
| P14 slopornot | 去 AI 味备选 | `installed/_ai-rate-fallback/slopornot` | github.com/numen-tech/slopornot @ 71bf2ea2862 | MIT | 只在 humanizer 实测不过时用 |
| P15 BypassAIGC | 降 AIGC 率备选 | `installed/_ai-rate-fallback/BypassAIGC` | github.com/chi111i/BypassAIGC @ d9fab8193d0 | CC BY-NC-SA 4.0 | 只在 humanizer 实测不过时用；仅个人非商用 |

**去 AI 味流程**：humanizer 改写 → 到专门的 AI 率检测网站实测 → 没通过才用 slopornot / BypassAIGC（改完再测）。说明见 `installed/_ai-rate-fallback/README.md`。

## 一、遇到问题时看哪个（先用已装的，不够再看备查）

| 卡点 | 先用（已装） | 不够时备查 |
|---|---|---|
| 还没选题/不知道做什么 | brainstorming-research-ideas → creative-thinking-for-research；deep-research（查新） | scientific-brainstorming、qinyan-topic-analysis（需付费 key）；公开备查 P19 asta-bench（选题素材） |
| idea 枯竭、想法都被做过 | creative-thinking-for-research；deep-research 查新模式；literature-review（OpenAlex） | hypothesis-generation |
| 不确定 idea 是否新颖 | deep-research + literature-review（OpenAlex）；ccf-deadlines 看近期会议 | citation-management |
| 读不懂/读太慢 | nature-paper-card | nature-reader、pdf-explore |
| 参考文献可能是编的 | nature-ref-verifier（所有引用必过） | citation-management |
| baseline/消融怎么设 | experimental-design + scientific-critical-thinking | statistical-method-design |
| 实验不出结果/效果不显著 | scientific-critical-thinking → statistical-analysis（效应量与功效）→ autoresearch 换方向 | — |
| 要评测 LLM | evaluating-llms-harness + lm-evaluation-harness | L11 evaluating-code-models（代码模型）、nemo-evaluator-sdk |
| 要评测 agent（harness 方向核心） | inspect_ai；hal-harness（⚠ 只作参考） | 公开备查：P16 harbor、P17 terminal-bench、P18 agentevals、P02 SWE-bench |
| 训练/显存/分布式 | — | pytorch-training、mixed-precision、distributed-training、pytorch-fsdp2；需要云 GPU 时 lambda-labs（⚠ 先问用户） |
| 实验记录乱、复现不了 | ara-research-manager | nature-experiment-log、weights-and-biases / mlflow / tensorboard |
| 图丑/不合规 | scientific-visualization、academic-plotting | figure-style、figure-composer |
| 论文故事讲不清 | paper-narrative、ml-paper-writing、claim2evidence-skill | 公开备查 P22 Research-Paper-Writing-Skills |
| 不会写某个章节 | ml-paper-writing；academic-paper（NC，随 L01） | L16 systems-paper-writing、nature-writing |
| LaTeX 模板/格式 | venue-templates；tailor-to-venue（P20） | — |
| 和合作者用 Overleaf | overleaf-sync（⚠ 写 keychain，先问用户） | — |
| 英文差/中译英 | humanizer（只做最后一步润色） | L19 nature-polishing、qinyan-paper-polish；公开备查 P08 qu-ai-wei（中文） |
| 担心 AI 味/查重 | humanizer（改文风，不用于规避检测） | 降重没有合格 skill：用学校查重 + 人工改写 |
| 投稿前想被挑刺 | academic-paper-reviewer（NC，5 席）+ scholar-evaluation | nature-reviewer、ara-rigor-reviewer |
| 不知道投哪、截稿何时 | select-venue（P20）+ ccf-deadlines | 公开备查 P05 ai-deadlines(hf)、P06 ccfddl-skills |
| 投稿计划/清单 | plan-submission（P20） | — |
| 要写 rebuttal | write-rebuttal（P20）；rebuttal（ARIS） | L23 nature-response（期刊式）、P25 awesome-rebuttal；只读参考 P27/P28/P29 |
| 被拒稿要转投 | plan-submission + tailor-to-venue + select-venue；resubmit-pipeline（ARIS） | — |
| 做报告/海报 | — | L25 presenting-conference-talks、scientific-slides、latex-posters |
| 想全自动跑一遍 | academic-pipeline（NC，人只在关口拍板）；autoresearch | researchclaw（参考） |


## 二、按环节（含已装与备查；已删的不再列，见第四节）

路径以 `installed/` 开头的已装；`library/科研skill/` 开头的是备查（相对 `/workspace/research-skills/`）。粗分是脚本粗估，入选项以评分轮分数为准。

### 选题与idea

| 名称 | 状态 | 粗分 | 路径 |
|---|---|---|---|
| statistical-analysis | ✅ 已装 | 3.8 | `installed/statistical-analysis` |
| deep-research | ✅ 已装 | 3.8 | `installed/imbad-academic-research-skills-NC/deep-research` |
| creative-thinking-for-research | ✅ 已装 | 3.8 | `installed/creative-thinking-for-research` |
| brainstorming-research-ideas | ✅ 已装 | 3.8 | `installed/brainstorming-research-ideas` |
| scientific-brainstorming | 备查 | 3.8 | `library/科研skill/skill/03-研究方法与设计` |
| pdf-explore | 备查 | 3.8 | `library/科研skill/完整技能包/HughYau__AcademicForge/AcademicForge-site-first/skills/claude-science/pdf-explore` |
| matplotlib | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/matplotlib` |
| arbor | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/arbor` |
| matplotlib | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/11-数据分析与统计建模/matplotlib` |
| scientific-brainstorming | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/04-研究方法与科学思维/scientific-brainstorming` |
| researchclaw | 备查 | 3.6 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/.claude/skills/researchclaw` |
| qinyan-nature-review | 备查 | 3.6 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/沁言学术skills/qinyan-nature-review` |
| qinyan-topic-analysis | 备查 | 3.4 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/沁言学术skills/qinyan-topic-analysis` |

### 文献检索与综述

| 名称 | 状态 | 粗分 | 路径 |
|---|---|---|---|
| statistical-analysis | ✅ 已装 | 3.8 | `installed/statistical-analysis` |
| venue-templates | ✅ 已装 | 3.8 | `installed/venue-templates` |
| deep-research | ✅ 已装 | 3.8 | `installed/imbad-academic-research-skills-NC/deep-research` |
| academic-pipeline | ✅ 已装 | 3.8 | `installed/imbad-academic-research-skills-NC/academic-pipeline` |
| nature-paper-card | ✅ 已装 | 3.8 | `installed/nature-paper-card` |
| ara-research-manager | ✅ 已装 | 3.8 | `installed/ara-research-manager` |
| creative-thinking-for-research | ✅ 已装 | 3.8 | `installed/creative-thinking-for-research` |
| brainstorming-research-ideas | ✅ 已装 | 3.8 | `installed/brainstorming-research-ideas` |
| ml-paper-writing | ✅ 已装 | 3.8 | `installed/ml-paper-writing` |
| autoresearch | ✅ 已装 | 3.8 | `installed/autoresearch` |
| scholar-evaluation | ✅ 已装 | 3.6 | `installed/scholar-evaluation` |
| nature-polishing | 备查 | 3.6 | `library/科研skill/完整技能包/Yuan1z0825__nature-skills/nature-skills-main/skills/nature-polishing` |
| literature-review | ✅ 已装 | 3.4 | `installed/literature-review` |
| academic-plotting | ✅ 已装 | 2.8 | `installed/academic-plotting` |
| scientific-brainstorming | 备查 | 3.8 | `library/科研skill/skill/03-研究方法与设计` |
| pptx-posters | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/pptx-posters` |
| pathml | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/pathml` |
| peer-review | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/peer-review` |
| academic-paper | ✅ 已装 | 3.8 | `installed/imbad-academic-research-skills-NC/academic-paper` |
| researchwrite | 备查 | 3.8 | `library/科研skill/完整技能包/Yuan1z0825__nature-skills/nature-skills-main/skills/nature-proposal-writer` |
| ara-rigor-reviewer | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/22-agent-native-research-artifact/rigor-reviewer` |
| ara-compiler | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/22-agent-native-research-artifact/compiler` |
| huggingface-tokenizers | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/02-tokenization/huggingface-tokenizers` |
| faiss | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/15-rag/faiss` |
| chroma | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/15-rag/chroma` |
| transformer-lens-interpretability | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/04-mechanistic-interpretability/transformer-lens` |
| stat-research-orchestrator | 备查 | 3.8 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/external/agents/stat_research_agent/skills/stat-research-orchestrator` |
| pptx-posters | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/03-学术演示与可视化/pptx-posters` |
| openalex-database | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/01-论文检索与文献管理/openalex-database` |
| literature-review | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/01-论文检索与文献管理/literature-review` |
| statistical-analysis | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/11-数据分析与统计建模/statistical-analysis` |
| scientific-writing | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/02-科学写作与学术交流/scientific-writing` |
| research-proposal | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/02-科学写作与学术交流/research-proposal` |
| venue-templates | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/02-科学写作与学术交流/venue-templates` |
| research-grants | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/04-研究方法与科学思维/research-grants` |
| scholar-evaluation | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/04-研究方法与科学思维/scholar-evaluation` |
| scientific-brainstorming | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/04-研究方法与科学思维/scientific-brainstorming` |
| qinyan-citation | 备查 | 3.6 | `library/科研skill/skill/01-文献检索与知识管理` |
| nature-paper-to-patent | 备查 | 3.6 | `library/科研skill/skill/06-论文写作与润色` |
| research-grants | 备查 | 3.6 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/research-grants` |
| scientific-slides | 备查 | 3.6 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/scientific-slides` |
| bgpt-paper-search | 备查 | 3.6 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/bgpt-paper-search` |
| infographics | 备查 | 3.6 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/infographics` |
| nature-citation | 备查 | 3.6 | `library/科研skill/完整技能包/Yuan1z0825__nature-skills/nature-skills-main/skills/nature-citation` |
| nature-reader | 备查 | 3.6 | `library/科研skill/完整技能包/Yuan1z0825__nature-skills/nature-skills-main/skills/nature-reader` |
| nature-literature-pipeline | 备查 | 3.6 | `library/科研skill/完整技能包/Yuan1z0825__nature-skills/nature-skills-main/skills/nature-literature-pipeline` |
| scientific-writing | 备查 | 3.6 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/researchclaw/skills/builtin/experiment/scientific-writing` |
| literature-search | 备查 | 3.6 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/researchclaw/skills/builtin/experiment/literature-search` |
| researchclaw | 备查 | 3.6 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/.claude/skills/researchclaw` |
| scientific-writing | 备查 | 3.6 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/.claude/skills/scientific-writing` |
| literature-search | 备查 | 3.6 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/.claude/skills/literature-search` |
| scientific-slides | 备查 | 3.6 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/03-学术演示与可视化/scientific-slides` |
| infographics | 备查 | 3.6 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/03-学术演示与可视化/infographics` |
| qinyan-citation | 备查 | 3.6 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/沁言学术skills/qinyan-citation` |
| bgpt-paper-search | 备查 | 3.6 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/01-论文检索与文献管理/bgpt-paper-search` |
| research-lookup | 备查 | 3.4 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/research-lookup` |
| parallel-web | 备查 | 3.4 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/parallel-web` |
| exa-search | 备查 | 3.4 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/exa-search` |
| nature-paper-to-patent | 备查 | 3.4 | `library/科研skill/完整技能包/Yuan1z0825__nature-skills/nature-skills-main/skills/nature-paper-to-patent` |
| systematic-review | 备查 | 3.4 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/researchclaw/skills/builtin/experiment/systematic-review` |
| qinyan-topic-analysis | 备查 | 3.4 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/沁言学术skills/qinyan-topic-analysis` |
| qinyan-paper-search | 备查 | 3.4 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/沁言学术skills/qinyan-paper-search` |
| research-lookup | 备查 | 3.4 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/01-论文检索与文献管理/research-lookup` |
| perplexity-search | 备查 | 3.4 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/01-论文检索与文献管理/perplexity-search` |
| uspto-database | 备查 | 3.2 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/12-科学数据库/uspto-database` |
| paper-lookup | 备查 | 3.0 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/paper-lookup` |
| autoskill | ⚠ 备查（有疑点，勿用） | 3.0 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/autoskill` |

### 读论文

| 名称 | 状态 | 粗分 | 路径 |
|---|---|---|---|
| scientific-visualization | ✅ 已装 | 3.8 | `installed/scientific-visualization` |
| nature-paper-card | ✅ 已装 | 3.8 | `installed/nature-paper-card` |
| ml-paper-writing | ✅ 已装 | 3.8 | `installed/ml-paper-writing` |
| nature-polishing | 备查 | 3.6 | `library/科研skill/完整技能包/Yuan1z0825__nature-skills/nature-skills-main/skills/nature-polishing` |
| presenting-conference-talks | 备查 | 3.2 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/20-ml-paper-writing/presenting-conference-talks` |
| pdf-explore | 备查 | 3.8 | `library/科研skill/完整技能包/HughYau__AcademicForge/AcademicForge-site-first/skills/claude-science/pdf-explore` |
| figure-composer | 备查 | 3.8 | `library/科研skill/完整技能包/HughYau__AcademicForge/AcademicForge-site-first/skills/claude-science/figure-composer` |
| scientific-visualization | 备查 | 3.8 | `library/科研skill/完整技能包/HughYau__AcademicForge/AcademicForge-site-first/skills/scientific-visualization` |
| stable-baselines3 | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/stable-baselines3` |
| matplotlib | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/matplotlib` |
| liteparse | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/liteparse` |
| flowio | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/flowio` |
| academic-paper | ✅ 已装 | 3.8 | `installed/imbad-academic-research-skills-NC/academic-paper` |
| ara-compiler | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/22-agent-native-research-artifact/compiler` |
| training-llms-megatron | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/08-distributed-training/megatron-core` |
| nemo-guardrails | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/07-safety-alignment/nemo-guardrails` |
| stable-baselines3 | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/09-机器学习与人工智能/stable-baselines3` |
| pptx-posters | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/03-学术演示与可视化/pptx-posters` |
| matplotlib | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/11-数据分析与统计建模/matplotlib` |
| qinyan-nature-figures | 备查 | 3.6 | `library/科研skill/skill/05-科研绘图与可视化` |
| nature-paper2ppt | 备查 | 3.6 | `library/科研skill/完整技能包/Yuan1z0825__nature-skills/nature-skills-main/skills/nature-paper2ppt` |
| nature-reader | 备查 | 3.6 | `library/科研skill/完整技能包/Yuan1z0825__nature-skills/nature-skills-main/skills/nature-reader` |
| scientific-visualization | 备查 | 3.6 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/researchclaw/skills/builtin/experiment/scientific-visualization` |
| scientific-visualization | 备查 | 3.6 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/.claude/skills/scientific-visualization` |
| qinyan-nature-figures | 备查 | 3.6 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/沁言学术skills/qinyan-nature-figures` |
| qinyan-nature-polishing | 备查 | 3.6 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/沁言学术skills/qinyan-nature-polishing` |
| nature-shared | ✅ 已装 | 3.4 | `installed/nature-shared` |
| qinyan-paper-analysis | 备查 | 3.4 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/沁言学术skills/qinyan-paper-analysis` |

### 实验设计

| 名称 | 状态 | 粗分 | 路径 |
|---|---|---|---|
| scientific-critical-thinking | ✅ 已装 | 3.8 | `installed/scientific-critical-thinking` |
| experimental-design | ✅ 已装 | 3.4 | `installed/experimental-design` |
| stable-baselines3 | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/stable-baselines3` |
| opentrons-integration | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/opentrons-integration` |
| statistical-power | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/statistical-power` |
| peer-review | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/peer-review` |
| experimental-design | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/experimental-design` |
| stable-baselines3 | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/09-机器学习与人工智能/stable-baselines3` |
| opentrons-integration | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/13-实验室自动化与集成/opentrons-integration` |
| statistical-method-design | 备查 | 3.6 | `library/科研skill/skill/11-自动研究pipeline` |
| scientific-critical-thinking | 备查 | 3.6 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/scientific-critical-thinking` |
| bgpt-paper-search | 备查 | 3.6 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/bgpt-paper-search` |
| statistical-reporting | 备查 | 3.6 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/researchclaw/skills/builtin/experiment/statistical-reporting` |
| statistical-reporting | 备查 | 3.6 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/.claude/skills/statistical-reporting` |
| statistical-experimental-evaluation | 备查 | 3.6 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/external/agents/stat_research_agent/skills/statistical-experimental-evaluation` |
| statistical-method-design | 备查 | 3.6 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/external/agents/stat_research_agent/skills/statistical-method-design` |
| bgpt-paper-search | 备查 | 3.6 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/01-论文检索与文献管理/bgpt-paper-search` |

### 写代码与跑实验

| 名称 | 状态 | 粗分 | 路径 |
|---|---|---|---|
| evaluating-llms-harness | ✅ 已装 | 3.8 | `installed/evaluating-llms-harness` |
| scientific-critical-thinking | ✅ 已装 | 3.8 | `installed/scientific-critical-thinking` |
| scholar-evaluation | ✅ 已装 | 3.6 | `installed/scholar-evaluation` |
| evaluating-code-models | 备查 | 3.2 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/11-evaluation/bigcode-evaluation-harness` |
| awq-quantization | 备查 | 3.8 | `library/科研skill/skill/12-ML工程与分布式训练` |
| customize | 备查 | 3.8 | `library/科研skill/完整技能包/HughYau__AcademicForge/AcademicForge-site-first/skills/claude-science/customize` |
| vaex | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/vaex` |
| scikit-learn | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/scikit-learn` |
| pymoo | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/pymoo` |
| pytorch-lightning | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/pytorch-lightning` |
| scikit-survival | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/scikit-survival` |
| arbor | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/arbor` |
| paperzilla | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/paperzilla` |
| statsmodels | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/statsmodels` |
| liteparse | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/liteparse` |
| uncertainty-and-units | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/uncertainty-and-units` |
| openpiv | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/openpiv` |
| pathml | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/pathml` |
| ara-rigor-reviewer | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/22-agent-native-research-artifact/rigor-reviewer` |
| huggingface-tokenizers | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/02-tokenization/huggingface-tokenizers` |
| training-llms-megatron | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/08-distributed-training/megatron-core` |
| model-merging | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/19-emerging-techniques/model-merging` |
| model-pruning | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/19-emerging-techniques/model-pruning` |
| speculative-decoding | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/19-emerging-techniques/speculative-decoding` |
| implementing-llms-litgpt | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/01-model-architecture/litgpt` |
| llamaindex | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/14-agents/llamaindex` |
| crewai-multi-agent | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/14-agents/crewai` |
| nemo-curator | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/05-data-processing/nemo-curator` |
| faiss | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/15-rag/faiss` |
| chroma | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/15-rag/chroma` |
| openrlhf-training | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/06-post-training/openrlhf` |
| simpo-training | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/06-post-training/simpo` |
| torchforge-rl-training | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/06-post-training/torchforge` |
| fine-tuning-with-trl | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/06-post-training/trl-fine-tuning` |
| verl-rl-training | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/06-post-training/verl` |
| serving-llms-vllm | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/12-inference-serving/vllm` |
| llama-cpp | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/12-inference-serving/llama-cpp` |
| tensorrt-llm | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/12-inference-serving/tensorrt-llm` |
| gptq | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/10-optimization/gptq` |
| quantizing-models-bitsandbytes | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/10-optimization/bitsandbytes` |
| awq-quantization | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/10-optimization/awq` |
| peft-fine-tuning | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/03-fine-tuning/peft` |
| axolotl | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/03-fine-tuning/axolotl` |
| evaluating-cosmos-policy | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/18-multimodal/cosmos-policy` |
| blip-2-vision-language | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/18-multimodal/blip-2` |
| nemo-guardrails | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/07-safety-alignment/nemo-guardrails` |
| prompt-guard | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/07-safety-alignment/prompt-guard` |
| tensorboard | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/13-mlops/tensorboard` |
| scikit-learn | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/09-机器学习与人工智能/scikit-learn` |
| pymoo | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/09-机器学习与人工智能/pymoo` |
| pufferlib | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/09-机器学习与人工智能/pufferlib` |
| pytorch-lightning | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/09-机器学习与人工智能/pytorch-lightning` |
| scikit-survival | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/09-机器学习与人工智能/scikit-survival` |
| openalex-database | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/01-论文检索与文献管理/openalex-database` |
| vaex | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/11-数据分析与统计建模/vaex` |
| statsmodels | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/11-数据分析与统计建模/statsmodels` |
| polars | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/11-数据分析与统计建模/polars` |
| peer-review | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/02-科学写作与学术交流/peer-review` |
| scholar-evaluation | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/04-研究方法与科学思维/scholar-evaluation` |
| nature-paper-to-patent | 备查 | 3.6 | `library/科研skill/skill/06-论文写作与润色` |
| scientific-critical-thinking | 备查 | 3.6 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/scientific-critical-thinking` |
| pi-agent | 备查 | 3.6 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/pi-agent` |
| distributed-llm-pretraining-torchtitan | 备查 | 3.6 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/01-model-architecture/torchtitan` |
| evolving-ai-agents | 备查 | 3.6 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/14-agents/a-evolve` |
| langchain | 备查 | 3.6 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/14-agents/langchain` |
| autogpt-agents | 备查 | 3.6 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/14-agents/autogpt` |
| llama-factory | 备查 | 3.6 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/03-fine-tuning/llama-factory` |
| dspy | 备查 | 3.6 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/16-prompt-engineering/dspy` |
| langsmith-observability | 备查 | 3.6 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/17-observability/langsmith` |
| experiment-tracking-swanlab | 备查 | 3.6 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/13-mlops/swanlab` |
| weights-and-biases | 备查 | 3.6 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/13-mlops/weights-and-biases` |
| statistical-experimental-evaluation | 备查 | 3.6 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/external/agents/stat_research_agent/skills/statistical-experimental-evaluation` |
| pufferlib | 备查 | 3.4 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/pufferlib` |
| parallel-web | 备查 | 3.4 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/parallel-web` |
| nature-paper-to-patent | 备查 | 3.4 | `library/科研skill/完整技能包/Yuan1z0825__nature-skills/nature-skills-main/skills/nature-paper-to-patent` |
| nemo-evaluator-sdk | 备查 | 3.4 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/11-evaluation/nemo-evaluator` |
| nnsight-remote-interpretability | 备查 | 3.4 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/04-mechanistic-interpretability/nnsight` |
| phoenix-observability | 备查 | 3.4 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/17-observability/phoenix` |
| rl-policy-optimization | 备查 | 3.4 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/researchclaw/skills/builtin/domain/rl-policy-optimization` |
| skill-creator | ⚠ 备查（有疑点，勿用） | 3.0 | `library/科研skill/完整技能包/HughYau__AcademicForge/AcademicForge-site-first/skills/claude-science/skill-creator` |
| autoskill | ⚠ 备查（有疑点，勿用） | 3.0 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/autoskill` |
| nature-downloader | ⚠ 备查（有疑点，勿用） | 3.0 | `library/科研skill/完整技能包/Yuan1z0825__nature-skills/nature-skills-main/skills/nature-downloader` |

### 数据分析与画图

| 名称 | 状态 | 粗分 | 路径 |
|---|---|---|---|
| scientific-visualization | ✅ 已装 | 3.8 | `installed/scientific-visualization` |
| paper-narrative | ✅ 已装 | 3.6 | `installed/paper-narrative` |
| academic-plotting | ✅ 已装 | 2.8 | `installed/academic-plotting` |
| figure-composer | 备查 | 3.8 | `library/科研skill/完整技能包/HughYau__AcademicForge/AcademicForge-site-first/skills/claude-science/figure-composer` |
| customize | 备查 | 3.8 | `library/科研skill/完整技能包/HughYau__AcademicForge/AcademicForge-site-first/skills/claude-science/customize` |
| figure-style | 备查 | 3.8 | `library/科研skill/完整技能包/HughYau__AcademicForge/AcademicForge-site-first/skills/claude-science/figure-style` |
| scientific-visualization | 备查 | 3.8 | `library/科研skill/完整技能包/HughYau__AcademicForge/AcademicForge-site-first/skills/scientific-visualization` |
| markdown-mermaid-writing | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/markdown-mermaid-writing` |
| vaex | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/vaex` |
| matlab | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/matlab` |
| pytorch-lightning | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/pytorch-lightning` |
| scientific-writing | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/scientific-writing` |
| statsmodels | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/statsmodels` |
| seaborn | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/seaborn` |
| flowio | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/flowio` |
| openpiv | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/openpiv` |
| statistical-power | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/statistical-power` |
| experimental-design | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/experimental-design` |
| llamaindex | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/14-agents/llamaindex` |
| nemo-curator | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/05-data-processing/nemo-curator` |
| hqq-quantization | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/10-optimization/hqq` |
| instructor | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/16-prompt-engineering/instructor` |
| prompt-guard | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/07-safety-alignment/prompt-guard` |
| tensorboard | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/13-mlops/tensorboard` |
| pytorch-lightning | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/09-机器学习与人工智能/pytorch-lightning` |
| scikit-survival | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/09-机器学习与人工智能/scikit-survival` |
| matlab | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/10-材料科学与物理计算/matlab` |
| markdown-mermaid-writing | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/03-学术演示与可视化/markdown-mermaid-writing` |
| literature-review | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/01-论文检索与文献管理/literature-review` |
| vaex | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/11-数据分析与统计建模/vaex` |
| statsmodels | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/11-数据分析与统计建模/statsmodels` |
| seaborn | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/11-数据分析与统计建模/seaborn` |
| polars | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/11-数据分析与统计建模/polars` |
| plotly | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/11-数据分析与统计建模/plotly` |
| statistical-analysis | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/11-数据分析与统计建模/statistical-analysis` |
| scientific-writing | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/02-科学写作与学术交流/scientific-writing` |
| peer-review | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/02-科学写作与学术交流/peer-review` |
| statistical-method-design | 备查 | 3.6 | `library/科研skill/skill/11-自动研究pipeline` |
| qinyan-nature-figures | 备查 | 3.6 | `library/科研skill/skill/05-科研绘图与可视化` |
| correct-scientific-figure | 备查 | 3.6 | `library/科研skill/skill/05-科研绘图与可视化/icebird1998__scientific-illustrator/plugins/scientific-illustrator/skills/correct-scientific-figure` |
| recreate-scientific-figure-in-drawio | 备查 | 3.6 | `library/科研skill/skill/05-科研绘图与可视化/icebird1998__scientific-illustrator/plugins/scientific-illustrator/skills/recreate-scientific-figure-in-drawio` |
| design-scientific-figure | 备查 | 3.6 | `library/科研skill/skill/05-科研绘图与可视化/icebird1998__scientific-illustrator/plugins/scientific-illustrator/skills/design-scientific-figure` |
| audit-scientific-figure | 备查 | 3.6 | `library/科研skill/skill/05-科研绘图与可视化/icebird1998__scientific-illustrator/plugins/scientific-illustrator/skills/audit-scientific-figure` |
| omero-integration | 备查 | 3.6 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/omero-integration` |
| infographics | 备查 | 3.6 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/infographics` |
| nature-figure | 备查 | 3.6 | `library/科研skill/完整技能包/Yuan1z0825__nature-skills/nature-skills-main/skills/nature-figure` |
| nature-writing | 备查 | 3.6 | `library/科研skill/完整技能包/Yuan1z0825__nature-skills/nature-skills-main/skills/nature-writing` |
| nature-statistics | 备查 | 3.6 | `library/科研skill/完整技能包/Yuan1z0825__nature-skills/nature-skills-main/skills/nature-statistics` |
| nature-paper2ppt | 备查 | 3.6 | `library/科研skill/完整技能包/Yuan1z0825__nature-skills/nature-skills-main/skills/nature-paper2ppt` |
| langsmith-observability | 备查 | 3.6 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/17-observability/langsmith` |
| weights-and-biases | 备查 | 3.6 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/13-mlops/weights-and-biases` |
| scientific-visualization | 备查 | 3.6 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/researchclaw/skills/builtin/experiment/scientific-visualization` |
| statistical-reporting | 备查 | 3.6 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/researchclaw/skills/builtin/experiment/statistical-reporting` |
| scientific-visualization | 备查 | 3.6 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/.claude/skills/scientific-visualization` |
| statistical-reporting | 备查 | 3.6 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/.claude/skills/statistical-reporting` |
| statistical-problem-formulation | 备查 | 3.6 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/external/agents/stat_research_agent/skills/statistical-problem-formulation` |
| statistical-theory-analysis | 备查 | 3.6 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/external/agents/stat_research_agent/skills/statistical-theory-analysis` |
| statistical-method-design | 备查 | 3.6 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/external/agents/stat_research_agent/skills/statistical-method-design` |
| infographics | 备查 | 3.6 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/03-学术演示与可视化/infographics` |
| qinyan-nature-figures | 备查 | 3.6 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/沁言学术skills/qinyan-nature-figures` |
| qinyan-nature-statistics | 备查 | 3.6 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/沁言学术skills/qinyan-nature-statistics` |
| datacommons-client | 备查 | 3.6 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/12-科学数据库/datacommons-client` |
| phoenix-observability | 备查 | 3.4 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/17-observability/phoenix` |
| meta-analysis | 备查 | 3.4 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/researchclaw/skills/builtin/experiment/meta-analysis` |
| research-lookup | 备查 | 3.4 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/01-论文检索与文献管理/research-lookup` |
| uspto-database | 备查 | 3.2 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/12-科学数据库/uspto-database` |

### 论文写作

| 名称 | 状态 | 粗分 | 路径 |
|---|---|---|---|
| venue-templates | ✅ 已装 | 3.8 | `installed/venue-templates` |
| academic-pipeline | ✅ 已装 | 3.8 | `installed/imbad-academic-research-skills-NC/academic-pipeline` |
| ara-research-manager | ✅ 已装 | 3.8 | `installed/ara-research-manager` |
| systems-paper-writing | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/20-ml-paper-writing/systems-paper-writing` |
| paper-narrative | ✅ 已装 | 3.6 | `installed/paper-narrative` |
| dhdna-profiler | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/dhdna-profiler` |
| markdown-mermaid-writing | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/markdown-mermaid-writing` |
| scientific-writing | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/scientific-writing` |
| researchwrite | 备查 | 3.8 | `library/科研skill/完整技能包/Yuan1z0825__nature-skills/nature-skills-main/skills/nature-proposal-writer` |
| implementing-llms-litgpt | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/01-model-architecture/litgpt` |
| torchforge-rl-training | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/06-post-training/torchforge` |
| opentrons-integration | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/13-实验室自动化与集成/opentrons-integration` |
| matlab | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/10-材料科学与物理计算/matlab` |
| markdown-mermaid-writing | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/03-学术演示与可视化/markdown-mermaid-writing` |
| qinyan-paper-polish | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/沁言学术skills/qinyan-paper-polish` |
| dhdna-profiler | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/04-研究方法与科学思维/dhdna-profiler` |
| research-grants | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/04-研究方法与科学思维/research-grants` |
| design-scientific-figure | 备查 | 3.6 | `library/科研skill/skill/05-科研绘图与可视化/icebird1998__scientific-illustrator/plugins/scientific-illustrator/skills/design-scientific-figure` |
| research-grants | 备查 | 3.6 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/research-grants` |
| omero-integration | 备查 | 3.6 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/omero-integration` |
| nature-writing | 备查 | 3.6 | `library/科研skill/完整技能包/Yuan1z0825__nature-skills/nature-skills-main/skills/nature-writing` |
| scientific-writing | 备查 | 3.6 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/researchclaw/skills/builtin/experiment/scientific-writing` |
| literature-search | 备查 | 3.6 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/researchclaw/skills/builtin/experiment/literature-search` |
| scientific-writing | 备查 | 3.6 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/.claude/skills/scientific-writing` |
| literature-search | 备查 | 3.6 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/.claude/skills/literature-search` |
| qinyan-nature-polishing | 备查 | 3.6 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/沁言学术skills/qinyan-nature-polishing` |
| qinyan-nature-review | 备查 | 3.6 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/沁言学术skills/qinyan-nature-review` |
| research-lookup | 备查 | 3.4 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/research-lookup` |
| nature-shared | ✅ 已装 | 3.4 | `installed/nature-shared` |

### LaTeX与排版

| 名称 | 状态 | 粗分 | 路径 |
|---|---|---|---|
| systems-paper-writing | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/20-ml-paper-writing/systems-paper-writing` |
| presenting-conference-talks | 备查 | 3.2 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/20-ml-paper-writing/presenting-conference-talks` |
| venue-templates | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/02-科学写作与学术交流/venue-templates` |
| pi-agent | 备查 | 3.6 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/pi-agent` |
| scientific-slides | 备查 | 3.6 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/scientific-slides` |
| scientific-slides | 备查 | 3.6 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/03-学术演示与可视化/scientific-slides` |

### 润色与降重

| 名称 | 状态 | 粗分 | 路径 |
|---|---|---|---|
| qinyan-paper-polish | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/沁言学术skills/qinyan-paper-polish` |

### 审稿模拟与自查

| 名称 | 状态 | 粗分 | 路径 |
|---|---|---|---|
| academic-paper-reviewer | ✅ 已装 | 3.8 | `installed/imbad-academic-research-skills-NC/academic-paper-reviewer` |
| literature-review | ✅ 已装 | 3.4 | `installed/literature-review` |
| nature-ref-verifier | ✅ 已装 | 3.2 | `installed/nature-ref-verifier` |
| matlab | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/matlab` |
| pptx-posters | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/pptx-posters` |
| opentrons-integration | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/opentrons-integration` |
| scikit-survival | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/scikit-survival` |
| nature-reviewer | 备查 | 3.8 | `library/科研skill/完整技能包/Yuan1z0825__nature-skills/nature-skills-main/skills/nature-reviewer` |
| correct-scientific-figure | 备查 | 3.6 | `library/科研skill/skill/05-科研绘图与可视化/icebird1998__scientific-illustrator/plugins/scientific-illustrator/skills/correct-scientific-figure` |
| audit-scientific-figure | 备查 | 3.6 | `library/科研skill/skill/05-科研绘图与可视化/icebird1998__scientific-illustrator/plugins/scientific-illustrator/skills/audit-scientific-figure` |
| pufferlib | 备查 | 3.4 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/pufferlib` |
| systematic-review | 备查 | 3.4 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/researchclaw/skills/builtin/experiment/systematic-review` |

### 投稿选刊

| 名称 | 状态 | 粗分 | 路径 |
|---|---|---|---|
| academic-paper-reviewer | ✅ 已装 | 3.8 | `installed/imbad-academic-research-skills-NC/academic-paper-reviewer` |

### rebuttal与修改

| 名称 | 状态 | 粗分 | 路径 |
|---|---|---|---|
| nature-response | 备查 | 3.0 | `library/科研skill/完整技能包/Yuan1z0825__nature-skills/nature-skills-main/skills/nature-response` |
| instructor | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/16-prompt-engineering/instructor` |

### 科研管理与协作

| 名称 | 状态 | 粗分 | 路径 |
|---|---|---|---|
| autoresearch | ✅ 已装 | 3.8 | `installed/autoresearch` |
| evaluating-code-models | 备查 | 3.2 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/11-evaluation/bigcode-evaluation-harness` |
| scikit-learn | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/scikit-learn` |
| paperzilla | 备查 | 3.8 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/paperzilla` |
| nature-experiment-log | 备查 | 3.8 | `library/科研skill/完整技能包/Yuan1z0825__nature-skills/nature-skills-main/skills/nature-experiment-log` |
| crewai-multi-agent | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/14-agents/crewai` |
| stat-research-orchestrator | 备查 | 3.8 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/external/agents/stat_research_agent/skills/stat-research-orchestrator` |
| scikit-learn | 备查 | 3.8 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/09-机器学习与人工智能/scikit-learn` |
| nature-literature-pipeline | 备查 | 3.6 | `library/科研skill/完整技能包/Yuan1z0825__nature-skills/nature-skills-main/skills/nature-literature-pipeline` |
| experiment-tracking-swanlab | 备查 | 3.6 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/13-mlops/swanlab` |
| paper-2-web | 备查 | 3.4 | `library/科研skill/完整技能包/LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/02-科学写作与学术交流/paper-2-web` |
| paper-lookup | 备查 | 3.0 | `library/科研skill/完整技能包/K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/paper-lookup` |

### 领域工具/其他

| 名称 | 状态 | 粗分 | 路径 |
|---|---|---|---|
| llamaguard | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/07-safety-alignment/llamaguard` |
| mlflow | 备查 | 3.8 | `library/科研skill/完整技能包/Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/13-mlops/mlflow` |
| nlp-alignment | 备查 | 3.4 | `library/科研skill/完整技能包/aiming-lab__AutoResearchClaw/AutoResearchClaw-main/researchclaw/skills/builtin/domain/nlp-alignment` |

## 三、风险项

| skill | 位置 | 风险 | 处理 |
|---|---|---|---|
| overleaf-sync | installed/overleaf-sync | 把 Overleaf token 写进 keychain | ⚠✅ 已装（有风险提示），使用前必须征得用户同意 |
| lambda-labs | installed/lambda-labs；库内原件已删除 | 写 ~/.ssh/authorized_keys、租 GPU 花钱 | ⚠✅ 已装（有风险提示），使用前必须征得用户同意 |
| hal-harness | installed/hal-harness | 无许可证、已归档、含云/SSH 脚本 | ⚠✅ 已装（有风险提示），只作参考，代码不能进论文开源代码 |
| rebuttal / resubmit-pipeline（ARIS） | installed/rebuttal、installed/resubmit-pipeline | `allowed-tools: Bash(*)`；外部审稿模型 MCP 会外发论文；resubmit 可选推 Overleaf | 审阅通过（review-P21.md），按 README 约束用 |
| remote-compute-ssh | library/…/claude-science/remote-compute-ssh | 操作 ~/.ssh 与远程主机（有逐文件确认） | 备查，用前问用户 |
| skill-creator | library/…/claude-science/skill-creator | 会调用 ANTHROPIC_API_KEY | 备查 |
| autoskill | library/…K-Dense…/skills/autoskill | 用 screenpipe 监视屏幕，脚本涉及多种密钥 | ⚠ 勿用 |
| nature-downloader | library/…/nature-skills…/nature-downloader | 机构全文下载，涉及登录会话（自述不导出 cookie） | 备查，谨慎 |
| open-notebook（K-Dense 与 qinyan 副本） | library/… | 向 open-notebook 服务上传资料与凭据配置 | 备查，勿配凭据 |
| AutoResearchClaw 的 notify.py / ssh_sandbox.py | library/…/AutoResearchClaw-main/researchclaw/… | 外发 webhook、SSH 远程执行 | 备查，不运行 |
| Orchestra autogpt | library/…/14-agents/autogpt | 部署外部 webhook 入口 | 备查 |


## 四、已删（🗑 已执行 2026-10-29，完整路径与理由见 `/workspace/research-skills/deleted.txt`）

- **b2 与 CS/AI 无关（142 个名称，所有包里的同名副本都删）**：生物信息/基因组、化学与药物发现、蛋白质结构、临床医学、神经科学、天文/物理/材料/流体、量子计算、金融经济、地理遥感、实验室自动化等。名单见 eval 文件 (b) 节；保留了 aeon、openalex-database、uspto-database、geopandas。删除前已逐个核对描述，没有拿不准的。
- **b1 不合规，删除**：paperclip（读浏览器 cookie + curl|bash）、nextflow（生物流程 + curl|bash）、K-Dense 版 literature-review（与 L06 重复，且要 curl parallel.ai/install.sh | bash）、qinyan install.sh（curl|bash 安装方式）。
- **b1 不取用（库里本来就没有）**：ARIS qzcli（读/存 cookie）、feishu-notify / feishu-bridge（外发 webhook、开端口）、P14 slopornot、P15 BypassAIGC（以绕过 AI 检测为卖点，违背学术诚信）、P04 ai-deadlines（pwc 版，停更两年）。
- **原始压缩包** `research-skills.zip` 和空的 `quarantine/`：已删除。

本清单上一版第二部分列出、现被删除的条目（18 个名称）：market-research-reports、qutip、biorxiv-database、imaging-data-commons、hedgefundmonitor、pubmed-database、fred-economic-data、literature-review、iso-standards-readiness、pydicom、pylabrobot、cirq、waypoint-bio、fluidsim、geomaster、usfiscaldata、nextflow、medical-imaging-review

## 五、公开仓库备查（没装，需要时再评估）

| ID | 名称 | URL | 为什么没装 |
|---|---|---|---|
| P16 | harbor | https://github.com/harbor-framework/harbor | 与 inspect_ai 二选一，保留 inspect_ai |
| P17 | terminal-bench | https://github.com/laude-institute/terminal-bench | 已并入 harbor |
| P02 | SWE-bench | https://github.com/SWE-bench/SWE-bench | 方案 A 3.75；做编程 agent 时再装（Docker+大磁盘） |
| P18 | agentevals | https://github.com/langchain-ai/agentevals | 方案 A 3.75 |
| P19 | asta-bench | https://github.com/allenai/asta-bench | 选题素材 |
| P05 | ai-deadlines（hf） | https://github.com/huggingface/ai-deadlines | 与 ccf-deadlines 重复 |
| P06 | ccfddl-skills | https://github.com/neverbiasu/ccfddl-skills | 2★，需人工审 |
| P08 | qu-ai-wei | https://github.com/LifelongLazyLearner/qu-ai-wei | 只在中文材料用 |
| P09 | avoid-ai-writing | https://github.com/conorbronsdon/avoid-ai-writing | 与 humanizer 同功能 |
| P10 | humanizer-skill | https://github.com/Aboudjem/humanizer-skill | 与 humanizer 同功能 |
| P22 | Research-Paper-Writing-Skills | https://github.com/Master-cai/Research-Paper-Writing-Skills | 与 ml-paper-writing 重叠 |
| P25 | awesome-rebuttal | https://github.com/xiongqi123123/awesome-rebuttal | 方案 A 3.80 |
| P27/P28/P29/P30/P12/P13 | Rebuttal-Skill、Paper2Rebuttal、Paper-Rebuttal-Tips 等 | 见 /workspace/learning-loop/rounds/search-20261029-1345-01.md | 许可证不合规，只能只读参考 |

本地备查里值得记住的：L11 evaluating-code-models、L16 systems-paper-writing、L19 nature-polishing、L23 nature-response、L25 presenting-conference-talks（都在 library/ 里，见第二节）。

## 六、已装 skill 不够用时怎么办

1. **先查本总清单**：第一节按卡点找，第二节按环节找“备查”项。备查项在 `library/科研skill/` 里，可以直接读它的 SKILL.md 来用；要正式装进 installed/，属于配置变更，先问用户。
2. **再查 `gaps.md`**：看这个缺口是不是已知的（例如降重没有合格 skill），以及已经核验过的公开补充仓库。
3. **最后找 Searcher 开搜索轮**：通过 BrainStorm 发起，写清缺口、目标环节、档位（一般 A 档）；候选交质量评估按 standards/research-skills-selection.md 打分、02 复核，再由用户拍板是否装。
4. 不要自己从网上随手装 skill。按 v3-27 口径，可以在 box 上执行 skill 自带脚本；但不用会外泄或导出 cookie/密钥的东西，lambda-labs（写 ~/.ssh、花钱）和 overleaf-sync（写 keychain）使用前先问用户。
