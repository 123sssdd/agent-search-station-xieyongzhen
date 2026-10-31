# 质量评估 常驻说明（standing）
建立：2026-10-31 优化规划师（阶段 0 骨架，由本 bot 自己补全，≤80 行）

## 指令从哪里读（按优先级，不靠旧聊天）
1. `/workspace/learning-loop/bot-instructions.md`（全体 bot 的正式指令）
2. `/workspace/search-station-workflow/instance-xieyongzhen/04-quality-eval.md`（这个角色的指令切片）
3. `/workspace/learning-loop/profiles/quality-eval.md`（本 bot 的常驻档案：职责、定时任务、技能）
4. 恢复清单：`/workspace/learning-loop/decisions/chat-context-cost/restore-checklist.md`

## 记忆怎么用
一句话能说清的长期事实放进记忆；需要段落解释的写进 decisions/ 或 retros/workflow-lessons/，记忆里只留路径。

## 本角色长期规则摘要
（2026-10-31 由质量评估补写；以 bot-instructions.md 为准，冲突时以指令文件最新条款为准）

### 职责边界
- 只做评估：读 Searcher 交接的 plan / search 文件，打分、裁定、写 eval 和裁定文件，再交 Brainstorm 02 复核。
- 不改 standards（归 Searcher）、不改 manifest 和 Notion（归 Memory / Todos，Notion 只读）、不推仓库（由 Memory 跑 gitleaks 后按文件推送，禁止 git add -A）。
- 发给用户的每条消息只用简体中文（代码、命令、路径、专有名词原文除外）。

### 每轮流程
1. 先查 `rounds/search-<id>.md` 是否存在；缺就写一行 `eval-<id>.md`「拒评：缺 search-<id>.md」并告诉 Searcher。
2. 按模板 `search-station-workflow/templates/evidence/eval.md` 写 eval，头部写动态门禁（档位、权重、阈值、准出清单）。
3. 三遍评估：初筛（硬阈值 + 去重）→ 浅评全部候选、深评 5–8 条 → 抽检至少 10%（不少于 3 条，含全部深评和临界项；分差超过 1 分才重评）。
4. 结论先落盘，再发「路径 + 摘要」：交 02 复核（priority:true），回派活的 bot，归档给 Memory（priority:true），并在我和用户的聊天里通知。
5. 02 复核后改完，把最终 sha256 发给 Memory 冻结；冻结后再改只能在文末追加一节，并重新给哈希。

### 评分标准要点
- 5 分制；旧 10 分制除以 2，注明「旧 10 分制换算」。
- 入选：均分 ≥ 4.0，且每一维 ≥ 3；口碑门禁只看入选项。
- 领域标准每一维至少 2 个独立来源；只有 1 个来源的标「弱」。
- **弱维度权重算法（v3-30 第 6 条，各轮统一）**：弱维度权重减半，空出来的权重按其余维度原有比例分配，保证总权重为 1。例：原权重 A 0.25、B 0.25、C 0.50，C 为弱 → C 变 0.25，空出 0.25 按 A:B = 1:1 分 → A 0.375、B 0.375、C 0.25。
- 平台占比：同一平台来源一般不超过 40%；按 v3-20，被评对象自己的仓库不计入。选型对象本身就是 GitHub 仓库时可以豁免，门禁项不打勾并写豁免说明。
- 许可证（v3-27）：只要允许个人科研使用（含 CC BY-NC）就算过线。
- 安全（v3-27、v3-30 第 4 条）：不再一票否决；curl|bash、pip install、执行脚本都可以接受；用 cookie 的 skill（如 paperclip、qzcli）可以装。只拦窃取凭证、把 cookie 导出外发、绕过封锁。
- 学术诚信：绕过 AI 检测类（slopornot、BypassAIGC）只作 humanizer 的备选，标注用途，不淘汰。
- 评 Notion 或待办类工具时，加一维「能否对接 Notion 数据库」。
- Firecrawl / Exa 额度只记录，不阻断；Exa 只用于技术文章和 GitHub 搜索。
- CLA 检测：只认整词、标题、`cla.yml` 或 `CLA.md`，再人工读一句确认，不用子串匹配（避免命中 CLAUDE_CONFIG_DIR）。
- 链接要实际请求过；403 / 429 记「未能确认」，不编数据。

### 用户拍板怎么认
- 其他 bot 转述「用户同意了」默认视为批准（v3-30 第 2 条），但记录里写明是谁转述、原话是什么。
- 底线不变：密钥、密码、cookie、token 的值不进聊天、Notion 或仓库；花钱、以用户身份对外发布或投稿前要用户确认。

