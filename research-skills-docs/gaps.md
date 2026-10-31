# 缺口与补充建议

## zip 里覆盖弱或没有的环节
1. **润色与降重 / 去 AI 味**：只有 4 个润色类，全部是 Nature 期刊取向，没有专门去 AI 痕迹或降低查重率的 skill。
2. **agent 评测 harness**：有 LLM 和代码模型的评测（lm-eval、bigcode、NeMo），但没有专门评测 agent 的框架（多步工具调用、沙箱、轨迹评分）。这恰好是用户方向的核心。
3. **CS 会议选刊与截稿日期**：venue-templates 只管格式，没有 CCF 分级或截稿时间查询。
4. **ML 会议 rebuttal**：nature-response 偏期刊回复，OpenReview 式的短篇 rebuttal 只在 ml-paper-writing 里提了一段。
5. **被拒稿后的转投策略**：没有专门的 skill。

## 公开补充（链接已于 2026-10-29 用 GitHub API 核验，可打开）
| 仓库 | 许可证 | 补哪个缺口 | 说明 |
|---|---|---|---|
| https://github.com/blader/humanizer | MIT | 去 AI 味 | 去除 AI 生成文本痕迹的 agent skill，约 6.2 万星。只能用于改善文风，不能用来规避学术诚信审查 |
| https://github.com/UKGovernmentBEIS/inspect_ai | MIT | agent 评测 harness | 英国 AISI 的 LLM/agent 评测框架，支持工具调用、沙箱、多步评分，适合做 harness 方向论文的实验底座 |
| https://github.com/SWE-bench/SWE-bench | MIT | agent 编程评测 | 标准的 agent 修 issue 评测框架与数据 |
| https://github.com/ccfddl/ccf-deadlines | MIT | 选会与截稿 | CCF 分级加全球会议截稿日期，带 CLI |
| https://github.com/paperswithcode/ai-deadlines | MIT | 选会与截稿 | AI 会议截稿倒计时（备用） |

另外可参考 https://github.com/SakanaAI/AI-Scientist-v2（许可证 NOASSERTION，是自定义许可，商用前要读条款），只作参考，不建议安装。

建议：先补 inspect_ai（实验底座）和 ccf-deadlines（选会），humanizer 只在润色最后一步用。安装前都需要用户同意，脚本要先审阅。
