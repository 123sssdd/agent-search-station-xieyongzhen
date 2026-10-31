# 领域标准：research-skills-selection（科研全流程 agent skills / 工具仓库选型；缓存 30 天）
- 建立：Searcher，2026-10-29 13:53 (UTC+8)，轮次 20261029-1345-01；有效至 2026-11-28。预搜约 4 分钟（curl 核验来源状态码，未用 Firecrawl）。

| # | 维度 | 定义 | 权重 | 阈值 | 来源1 | 来源2 | 强/弱 |
|---|---|---|---|---|---|---|---|
| 1 | 环节契合度 | 覆盖科研流程中的明确环节，且贴合工程 / agent / harness / LLM 评测方向 | 0.25→0.125（弱，减半） | 3=覆盖 ≥1 个目标环节 | 用户画像（本轮任务书） | 仅单源 | 弱 |
| 2 | 许可证可修改 | 允许个人科研使用即通过（含 CC BY-NC）；仅无许可证且禁止使用时不通过 | 0（v3-27） | 准入条件（不计分） | https://choosealicense.com/licenses/（200） | https://opensource.org/licenses（200） | 强 |
| 3 | 维护活跃度 | 近 90 天有推送、未归档 | 0.15 | 3=180 天内推送 | https://github.com/ossf/scorecard/blob/main/docs/checks.md（200，Maintained） | https://www.chaoss.community/kb/metrics-model-starter-project-health/（403，未能确认） | 强（来源2 未能确认） |
| 4 | 安全性 | 大部分 skills 视为安全，可在 box 执行脚本；只拦窃取凭证、导出 cookie 外发等恶意行为 | 0.05（v3-27） | 不再一票否决；恶意行为才排除，可疑项单列备注 | https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/（200） | https://owasp.org/www-project-top-10-for-large-language-model-applications/（200） | 强 |
| 5 | Skill 结构质量 | SKILL.md 有清晰 name/description、触发条件、渐进披露 | 0.15 | 3=符合规范 | https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/best-practices（200） | https://agentskills.io/specification（200） | 强 |
| 6 | 依赖成本 | 需要的 key、付费 API、GPU、安装量 | 0.05→0.025（弱，减半） | 不设下限 | https://docs.github.com/en/code-security/dependabot（200） | 仅单源 | 弱 |
注：本轮权重以「变更」节最新一条为准（14:06 起改用方案 A），前一版 0.15 重分配已作废。
## 变更
- 2026-10-29：建立。
- 2026-10-29 14:05：按 02 复核意见改正空出权重 0.1375→0.15，并写入重分配结果。
- 2026-10-29 14:06：01 于 14:04 拍板，1345-01 改用 02 的方案 A（decisions/round-20261029-1345-01/02-1403.md）：D1 契合 0.40 / D2 许可 0.05 / D3 维护 0.15 / D4 安全 0.10 / D5 结构 0.25 / D6 依赖 0.05；D2、D4 仍作硬门槛。14:05 写入的 D2/D4 0.2429、D3/D5 0.1821 作废。
- 2026-10-29 14:20：按 v3-27，采用优化规划师的建议（decisions/v3-27/优化规划师-20261029-1418.md），01 已确认：D1 契合 0.45 / D2 许可 0（只作门槛，允许个人科研使用即通过） / D3 维护 0.15 / D4 安全 0.05 / D5 结构 0.30 / D6 依赖 0.05，合计 1.00。14:06 的方案 A 作废。
- 2026-10-29 14:21：按 v3-27 改第 7、9 行。许可证：允许个人科研使用（含 CC BY-NC）即通过，不再作硬门槛。安全：不再一票否决，只排除窃取凭证、导出 cookie 外发这类恶意行为。表中权重同步为 14:20 版。
