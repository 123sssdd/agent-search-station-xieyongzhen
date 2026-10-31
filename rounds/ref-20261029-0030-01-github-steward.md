# 【未经评估，仅供参考】Github 管家 · 开源贡献调研半成品（2026-10-29 00:30，北京时间）
> 00:32/00:33 按用户要求中止，未补搜。数据来自 gh 只读查询，star 等为 00:30 前后实时值；指标不完整。

## 方法（已试用）
- 仓库初筛：`gh api -X GET search/repositories -f q='topic:<ai-agents|llm|agents|rag|mcp|llmops> stars:1000..10000 good-first-issues:>=3 pushed:>2026-10-15 archived:false' -f sort=stars`
- issue 计数：search/issues，`repo:X is:issue is:open label:"good first issue" [no:assignee]`；`label:"help wanted" no:assignee`
- 合并活跃度：`is:pr is:merged merged:>日期` 与 `is:pr is:closed is:unmerged` 计数；`gh pr list --state merged --json createdAt,mergedAt` 算合并中位时长；issue 首次非作者非 bot 评论时间 → 维护者首响中位数。
- 坑：search API 约 30 次/分钟，并发会限流；`gh api --jq` 不支持 `--arg`，需管道给 jq。脚本草稿：/workspace/learning-loop/oss/metrics.sh（已标作废）。
- 未及调研：goodfirstissue.dev、up-for-grabs、OSS Insight。

## 初筛命中仓库（search 返回，满足 1k–10k star、≥3 个 good first issue、10/15 后有推送）
重点 16 个（00:30 实测，含开放 good first issue 数 gfi、其中未指派数）：
| 仓库 | star | 语言 | 最近推送(UTC) | gfi | gfi 未指派 |
|---|---|---|---|---|---|
| apache/seatunnel | 9767 | Java | 10-28 | 23 | 未测 |
| iflytek/astron-agent | 8940 | Java | 10-28 | 3 | 1 |
| flyteorg/flyte | 7784 | Go | 10-28 | 17 | 未测 |
| traceloop/openllmetry | 7513 | Python | 10-19 | 7 | 未测 |
| apache/hertzbeat | 7446 | Java | 10-28 | 29 | 未测 |
| NVIDIA-NeMo/Guardrails | 7386 | Python | 10-28 | 3 | 0 |
| enricoros/big-AGI | 7157 | TypeScript | 10-28 | 4 | 4 |
| agentscope-ai/agentscope-java | 6161 | Java | 10-28 | 6 | 未测 |
| IBM/mcp-context-forge | 4712 | Python | 10-28 | 4 | 4 |
| jupyterlab/jupyter-ai | 4427 | Python | 10-27 | 6 | 未测 |
| truera/trulens | 3616 | Python | 10-28 | 5 | 5 |
| lmnr-ai/lmnr | 3459 | TypeScript | 10-28 | 3 | 未测 |
| containers/ramalama | 3093 | Python | 10-26 | 7 | 4 |
| apache/burr | 2584 | Python | 10-28 | 6 | 未测 |
| mcpjungle/MCPJungle | 1312 | Go | 10-26 | 16 | 未测 |
| Arize-ai/openinference | 1294 | Python | 10-28 | 5 | 未测 |
help wanted、PR 合并数、合并时长、首响时长：因限流未取得。具体 issue 链接：未取。

其余命中（仅 star/语言，未核验质量）：MakazhanAlpamys/Soup 9755 Py；modem-dev/hunk 9705 TS；pacifio/atlas 9555 TS；HarnessMD/munder-difflin 9155 TS；superradcompany/microsandbox 8840 Rust；repowise-dev/repowise 8023 Py；kyegomez/swarms 7309 Py；vespa-engine/vespa 7152 Java；katanemo/plano 7100 Rust；FailproofAI/failproofai 6953 TS；GreptimeTeam/greptimedb 6769 Rust；apache/maka 5921 TS；potpie-ai/potpie 5774 Py；maziyarpanahi/openmed 5720 Py；Blaizzy/mlx-vlm 5686 Py；TabularisDB/tabularis 5320 TS；InternLM/xtuner 5219 Py；aipotheosis-labs/aci 4925 Py；rivet-dev/agentos 4833 Rust；memgraph/memgraph 4634 C++；gradio-app/fastrtc 4634 JS；Observal/Observal 4533 Py；deepflowio/deepflow 4309 Go；pipeshub-ai/pipeshub-ai 3864 Py；SciSharp/LLamaSharp 3818 C#；twinnydotdev/twinny 3684 TS；taylorwilsdon/google_workspace_mcp 3429 Py；silexlabs/Silex 3023 TS；Vexa-ai/vexa 2924 Py；trustgraph-ai/trustgraph 2845 Py；apache/hamilton 2618；Nano-Collective/nanocoder 2539 TS；sierra-research/tau2-bench 2350 Py；kubeflow/trainer 2264 Go；future-agi/future-agi 2213 Py；ovg-project/kvcached 2015 Py；generative-computing/mellea 1841 Py；NVIDIA-NeMo/Curator 1831 Py；bespokelabsai/curator 1756 Py；openchoreo/openchoreo 1716 Go；amd/gaia 1599 Py；Azure/data-api-builder 1534 C#；KusionStack/kusion 1325 Go；stackql/stackql 1069 Go；cuga-project/cuga-agent 1054 Py；bytechefhq/bytechef 1050 Java（另有若干营销/列表型仓库未列）。

## 工具现状
见 /workspace/learning-loop/profiles/github-steward.md（gh CLI 只读、user-GitHub-xai 99 工具、cursor-origin 32 工具、cursor-github 未授权）。
