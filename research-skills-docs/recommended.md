# 推荐安装的 skills（25 个）

评分：5 分制，维度＝契合度（工程/agent/harness 优先）、质量、覆盖环节、省心程度、依赖成本。门槛：均分 ≥4.0 且单项 ≥3。同功能只留最优，其余进 master-catalog.md 的“备选”。

路径相对 `/workspace/research-skills/library/科研skill/完整技能包/`。安装＝把整个文件夹（含 references/、scripts/）复制到科研大师的 skills 目录；scripts 先人工审阅再运行。

| # | 名称 | 环节 | 契合/质量/覆盖/省心/依赖 | 均分 | 理由 | 路径 |
|---|---|---|---|---|---|---|
| 1 | academic-pipeline | 全流程编排 | 5/5/5/5/4 | 4.8 | 研究→写作→诚信检查→审稿→修改的总编排器，人只在关口拍板，最贴合“人只做核心决策” | `Imbad0202__academic-research-skills/academic-research-skills-main/academic-pipeline` |
| 2 | autoresearch | 全流程编排/写代码与跑实验 | 5/4/5/5/4 | 4.6 | 双循环自动研究（内循环跑实验、外循环调方向），适合 agent/harness 类实证论文 | `Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/0-autoresearch-skill` |
| 3 | brainstorming-research-ideas | 选题与idea | 5/5/4/4/5 | 4.6 | CS/AI 选题框架，产出可比较的候选题，供用户拍板 | `Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/21-research-ideation/brainstorming-research-ideas` |
| 4 | creative-thinking-for-research | 卡点：idea 枯竭 | 5/4/3/4/5 | 4.2 | 认知科学式发散方法，idea 卡住时用 | `Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/21-research-ideation/creative-thinking-for-research` |
| 5 | deep-research | 文献检索与综述 | 4/5/5/5/4 | 4.6 | 13-agent 深度调研，8 种模式，含系统综述 | `Imbad0202__academic-research-skills/academic-research-skills-main/deep-research` |
| 6 | literature-review | 文献检索与综述 | 5/4/4/5/4 | 4.4 | OpenAlex 驱动找论文+核验+综合；用户已有 OpenALEX key | `HughYau__AcademicForge/AcademicForge-site-first/skills/claude-science/literature-review` |
| 7 | nature-paper-card | 读论文 | 4/5/3/5/4 | 4.2 | 单篇论文深读卡片，带出处定位 | `Yuan1z0825__nature-skills/nature-skills-main/skills/nature-paper-card` |
| 8 | nature-ref-verifier | 文献检索与综述/审稿自查 | 4/5/3/5/5 | 4.4 | 逐条核验参考文献真实性，防 AI 幻觉引用 | `Yuan1z0825__nature-skills/nature-skills-main/skills/nature-ref-verifier` |
| 9 | experimental-design | 实验设计 | 5/3/3/4/5 | 4.0 | ML 实验的 baseline/消融/对照设计清单（偏短） | `aiming-lab__AutoResearchClaw/AutoResearchClaw-main/researchclaw/skills/builtin/experiment/experimental-design` |
| 10 | evaluating-llms-harness | 写代码与跑实验 | 5/5/3/4/4 | 4.2 | lm-evaluation-harness 用法，harness 方向直接相关 | `Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/11-evaluation/lm-evaluation-harness` |
| 11 | evaluating-code-models | 写代码与跑实验 | 5/4/3/4/4 | 4.0 | 代码模型评测（HumanEval/MBPP 等），agent 编程类论文常用 | `Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/11-evaluation/bigcode-evaluation-harness` |
| 12 | statistical-analysis | 数据分析与画图 | 4/4/4/4/5 | 4.2 | 检验选择、假设检查、效应量，防结果站不住 | `K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/statistical-analysis` |
| 13 | academic-plotting | 数据分析与画图 | 5/4/3/5/3 | 4.0 | 按论文上下文生成 ML 论文图；架构图部分可选 Gemini key | `Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/20-ml-paper-writing/academic-plotting` |
| 14 | scientific-visualization | 数据分析与画图 | 4/5/3/4/5 | 4.2 | matplotlib/seaborn 出版级图表与审图 | `K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/scientific-visualization` |
| 15 | ml-paper-writing | 论文写作（各章节） | 5/5/5/5/5 | 5.0 | 面向 NeurIPS/ICML/ICLR/ACL 的全章节写作，含 LaTeX 模板与 rebuttal 提示 | `Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/20-ml-paper-writing/ml-paper-writing` |
| 16 | systems-paper-writing | 论文写作（系统类） | 4/5/4/4/5 | 4.4 | OSDI/SOSP/NSDI 系统论文写法，工程型 agent 系统论文适用 | `Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/20-ml-paper-writing/systems-paper-writing` |
| 17 | paper-narrative | 论文写作（故事线） | 4/4/3/4/5 | 4.0 | 判断并重塑论文图表讲的故事 | `HughYau__AcademicForge/AcademicForge-site-first/skills/claude-science/paper-narrative` |
| 18 | venue-templates | LaTeX与排版/投稿选刊 | 4/4/4/4/5 | 4.2 | 会议/期刊 LaTeX 模板与格式要求 | `K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/venue-templates` |
| 19 | nature-polishing | 润色与降重 | 3/5/3/5/5 | 4.2 | 中译英与学术精修，保留事实不改数据 | `Yuan1z0825__nature-skills/nature-skills-main/skills/nature-polishing` |
| 20 | academic-paper-reviewer | 审稿模拟与自查 | 5/5/4/5/4 | 4.6 | 5 席位角色分离的模拟审稿 | `Imbad0202__academic-research-skills/academic-research-skills-main/academic-paper-reviewer` |
| 21 | scholar-evaluation | 审稿模拟与自查 | 4/4/3/4/5 | 4.0 | ScholarEval 框架打分，适合投稿前自评 | `K-Dense-AI__scientific-agent-skills/scientific-agent-skills-main/skills/scholar-evaluation` |
| 22 | scientific-critical-thinking | 卡点：实验不出结果/证据不足 | 4/4/3/4/5 | 4.0 | 评估主张与证据质量，排查实验设计漏洞 | `LeonChaoX__qinyan-academic-skills/qinyan-academic-skills-main/skills/04-研究方法与科学思维/scientific-critical-thinking` |
| 23 | nature-response | rebuttal与修改 | 4/4/4/5/5 | 4.4 | 逐条回复审稿意见并定位修改 | `Yuan1z0825__nature-skills/nature-skills-main/skills/nature-response` |
| 24 | ara-research-manager | 科研管理与协作 | 4/4/3/5/5 | 4.2 | 任务结束后自动记录研究溯源（决策、实验、产物） | `Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/22-agent-native-research-artifact/research-manager` |
| 25 | presenting-conference-talks | 投稿后：报告与展示 | 4/4/3/5/4 | 4.0 | 从论文生成 Beamer/PPTX 会议报告 | `Orchestra-Research__AI-Research-SKILLs/AI-Research-SKILLs-main/20-ml-paper-writing/presenting-conference-talks` |

## 依赖与 key
- `literature-review`(AcademicForge)：OPENALEX_API_KEY（用户已有，存加密存储，勿写入文件）。
- `academic-plotting`：画架构示意图时可选 GEMINI_API_KEY；纯数据图不需要。
- `evaluating-*-harness`：需要 GPU/本地模型或 API 模型额度。
- `nature-polishing`/`nature-response` 依赖同包的 `nature-shared`，复制时一起带上。
- 其余均为纯指令型，无 key。

## 刻意没推荐的同类（在备选里）
- K-Dense/qinyan 的 `literature-review`、`research-lookup`：依赖 OpenRouter/Parallel 外发，且前者文档含 curl|bash。
- `qinyan-*` 系列（论文检索/分析/选题）：依赖沁言学术付费 API。
- `academic-paper`（Imbad）：与 ml-paper-writing 功能重叠，ML 会议场景后者更对口；需要中文/期刊长文时再用。
- `nature-writing`/`nature-reviewer`：Nature 期刊取向，不如 ML 会议取向贴合。
- `researchclaw`/AutoResearchClaw：全自动流水线，人难以介入关键决策，作为参考不默认装。