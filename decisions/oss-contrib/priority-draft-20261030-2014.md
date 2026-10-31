# 开源贡献优先级草案｜1944-01（待 02 复核 + 用户拍板）

- 时间：2026-10-30 20:14 Asia/Shanghai
- 作者：Github 管家
- 依据：rounds/eval-20261030-1944-01.md、rounds/oss-20261030-1944-01.md、decisions/round-20261030-1944-01/质量评估-20261030-2013.md
- 状态：**草案已按 02 定稿更正**。本地 registry 已写但标待用户拍板；Notion 暂缓同步。CLA 与语言偏好属 B 类，等用户拍板。

## 排序原则（草案）
1. 质量评估均分与 picked 序为主。
2. 贴合用户目标（Agent 工作流 / harness / MCP / 评测可观测）上调；纯 chore 风险下调。
3. 首周可落地：优先 Python/TS、无 CLA 或可后置 CLA；官方高竞争仓与仅 hw 兜底仓不占本周唯一名额。
4. 周认领上限 1–2；本周建议只锁 **1 个主攻 + 1 个备选**。

## 建议优先级

### P0｜本周可考虑认领（择 1～2）
| 序 | 仓库 | 均分 | 语言 | CLA | 草案理由 | 注意 |
|---|---|---|---|---|---|---|
| 1 | pipeshub-ai/pipeshub-ai | 5.00 | Python | 未见 | 均分最高；Agent context + 连接器，工程故事完整，gfi 多 | 挑有技术深度的 issue，避开纯「加目录」 |
| 2 | maximhq/bifrost | 4.90 | Go | 未见 | AI/MCP/Agent 网关，合并率样本满分 | Go；★近上限，竞争或升 |
| 3 | mex-memory/mex | 4.41 | TypeScript | 未见 | Agent 记忆层，TS 友好，故事好讲 | 确认 issue 非纯文案 |
| 4 | nitrocloudofficial/nitrostack | 4.40 | TypeScript | 未见 | 全栈 TS 建 MCP server，贴 MCP 线 | 推送日稍早（10-19） |

### P0-CLA｜分数高但开 PR 前须用户签 CLA（B）
| 序 | 仓库 | 均分 | 语言 | 草案角色 |
|---|---|---|---|---|
| — | ~~vshulcz/deja-vu~~ | 4.90 | Go | **已更正：无 CLA**，并入上方 P0（与无 CLA 仓一并考虑） |
| 5 | future-agi/future-agi | 4.65 | Python | gfi 极多、新人友好；**先 CLA** |
| 6 | truera/trulens | 4.53 | Python | evaluation harness 主线；**CLA + cla.yml** |
| 7 | AgenticResourceRegistry/… | 4.46 | Python | 资源注册表；**CLA** |
| 8 | IBM/mcp-context-forge | 4.24 | Python | MCP 网关；**CLA**，可作 MCP 线第二波 |

### P1｜主线契合，非本周必抢
| 仓库 | 均分 | 备注 |
|---|---|---|
| anthropics/claude-agent-sdk-python | 4.48 | 官方仓，竞争激烈，勿作唯一首周 |
| truefoundry/trueforge | 4.37 | Agent harness 契合高，**仅 hw 兜底**，勿唯一主攻 |
| kyegomez/swarms | 4.37 | 多 Agent 编排；避开纯 chore |
| potpie-ai/potpie | 4.34 | Context Graph；先跑通本地栈 |
| pydantic/logfire | 4.34 | 可观测 / OTel |
| LearningCircuit/local-deep-research | 4.24 | 本地研究 Agent；环境重 |
| twinnydotdev/twinny | 4.22 | VS Code 插件，需本地调试 |
| agentscope-ai/agentscope-java | 4.12 | Java 线；语言偏好待用户 |
| msoedov/agentic_security | 4.09 | 安全线可选 |
| traceloop/openllmetry | 4.00 | 合并率偏低，**勿首周主攻** |

### P1-语言待定（B：用户是否主攻该语言）
| 仓库 | 均分 | 语言 | 说明 |
|---|---|---|---|
| editor-code-assistant/eca | 4.46 | Clojure | 分数不低，默认不进本周，除非用户要 Clojure |
| katanemo/plano | 4.13 | Rust | 同上，Rust 依赖成本高 |

### 临界 / 不入选（本轮不进 registry picked）
- 临界：higress（合并率低）、garak（均分&lt;4 + CLA）— 是否降优先进 registry 候补，等用户/02
- 不入选：cuga-agent、alumnium

## 本周执行建议（草案，未执行）
1. **主攻候选**：`pipeshub-ai/pipeshub-ai`（无 CLA、Python、均分最高）。
2. **备选**：`vshulcz/deja-vu`（无 CLA）、`mex-memory/mex` 或 `maximhq/bifrost`。
3. 若用户愿意先签 CLA：可把 `future-agi` 或 `trulens` 换上作首 PR 加速。
4. 待 02 通过 → 写 `oss-contrib/registry.json` → Memory/管家同步独立 Notion 贡献库进度字段。
5. 认领/PR/评论仍出草稿等用户确认；fork 可为 A 类。

## 请 01 转用户拍板（B）
1. 是否接受本周主攻 `pipeshub-ai` + 备选（mex / bifrost）？
2. 是否愿意为高分仓签 CLA（future-agi / trulens / ARR / mcp-context-forge；不含 deja-vu）？
3. Rust（plano）/ Clojure（eca）/ Java（agentscope-java）要不要进主攻池？
4. higress / garak 是否进 registry 候补？

## 定稿更正（2026-10-30 20:17，质量评估+02）
- eval sha256 前缀：`97f31634b6418d57`
- **vshulcz/deja-vu 无 CLA**（CONTRIBUTING「No CLA.」），均分 4.90，升为 P0 无障碍候选。
- 仍须 CLA（入选）：trulens、future-agi、ARR、mcp-context-forge；临界 garak；不入选 cuga-agent。
- registry 已写：`/workspace/learning-loop/oss-contrib/registry.json`（Notion 待 Memory 按 issue_key upsert；独立贡献库 id 待回填）。

## 用户拍板（2026-10-30 20:18，经 BrainStorm 01 转达原话）
> 现在我没有时间去搞开源贡献，所以这些不一定要本周做。可以先入库看看，时间待定。
- 正式入库：本地 registry + Memory 同步 Notion
- 本周不设主攻/认领；全部优先级标「待定」
- CLA/语言四问暂不催；有空再排
## 用户偏好补充（2026-10-30 20:21）
- 愿意签 CLA。
- 主攻：前端 + agent（Python，含 LangChain）；Java、Go 可进池。
- 本轮 1944-01 只测工作流，不真贡献；保持待定、不认领。

