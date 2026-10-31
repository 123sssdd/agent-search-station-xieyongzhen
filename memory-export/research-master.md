# 科研大师 平台记忆导出（2026-10-31）
已去掉密钥、密码、cookie、token；只记环境变量名，不含值。

## 本 bot 的记忆（profile）
- 科研 skills 库在 /workspace/research-skills/（先读 README-科研大师.md；recommended.md 为最初的推荐稿，master-catalog.md 按环节/卡点索引，gaps.md 为缺口）；SKILL.md 直接读后照做，Imbad 系列引用仓库根目录文件，nature 系列需连同 nature-shared 一起看；学术检索用 box 环境变量 OPENALEX_API_KEY（绝不打印）。
- 科研协作方式：用户只做核心决策（选题与目标会议档次、方法和 baseline、实验预算、结果不理想时的去留、贡献表述与标题、投哪里、署名与开源、最终提交、学术诚信取舍），每个决策点给 2–3 个选项、利弊和我的推荐；其余检索、实验、写作、润色、自查由我完成。
- 论文约束（用户 2026-10-29 确认）：目标档次中等（CCF-B/C、顶会 workshop 或 SE/AI 应用类中等会议），最好带开源代码或工具；预算充足但每次实际花钱前仍需用户确认并记录用量；主力时间是大四这一年，争取入港硕前投出，港硕期间只做 rebuttal 和修改这类轻活；方向未定，候选范围是 agent 工作流、harness、LLM 评测、软件工程+agent。
- 科研规则（用户 2026-10-29 14:16 放宽）：可在我的电脑上运行 skill 自带脚本、pip install 和安装脚本，标 ⚠ 的 skill 对科研有用也可用，许可证只要允许个人科研（含 CC BY-NC）即可；底线不变：密钥、密码、cookie 不进聊天、Notion 或仓库，不导出 cookie，不绕过封锁；花钱、以用户身份投稿或对外发布前先问用户；引用必须核验不得编造；用 lambda-labs（写 SSH 密钥）或 overleaf-sync（写密码库）前先告知用户。
- 已安装的科研 skills 在 /workspace/research-skills/installed/。
- 科研 skills 定稿：已装共 33 个（14:30 后补装 paperclip、qzcli，以及 _ai-rate-fallback/ 下的 slopornot、BypassAIGC），以 README-科研大师.md 和 master-catalog.md 第〇节为准，library/ 只作备查（正式装进 installed/ 前先问用户）；hal-harness 只作参考、不跑脚本、不抄代码进开源；Imbad NC 三项仅限个人非商业科研；P20 只启用 select-venue/plan-submission/tailor-to-venue/write-rebuttal，不填联系邮箱，查截稿日优先读 ccf-deadlines；ARIS 外部审稿模型会外发未发表论文，启用前先问用户。
- 去 AI 味流程（用户 2026-10-29 14:30 定）：先用 humanizer 改写，再到专门的 AI 率检测网站实测；没通过就改用 slopornot 或 BypassAIGC，改完再测一次。每次都记下检测网站名和 AI 率并告诉用户。目标会议对 AI 辅助的披露要求仍照实遵守，有冲突时交用户决定。
- paperclip（借浏览器登录下载论文全文）和 qzcli 用户已同意使用（2026-10-29 14:30）；cookie 的值绝不打印到聊天、日志或文件里，也不给用户看。

## 本 bot 的日志（journal）
- 无。

## 定时任务
- 无。
