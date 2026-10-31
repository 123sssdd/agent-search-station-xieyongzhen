# 优化规划师 平台记忆导出（脱敏）
导出：2026-10-31 15:00。只导出要点，不含密钥、密码、cookie、token、邮箱。

## 关于用户（共享记忆要点）
- 用户是谢永镇，浙江工业大学软件工程本科，在申请港大 MSc(CompSc)；目标是 AI 全栈 / AI Agent 工程师。
- 科研目标：港硕期间借 AI 发一篇中等水平论文，方向偏工程和 agent 工作流，由科研大师 bot 负责。
- 开源贡献：愿意签 CLA；主攻前端和 Python agent，Java、Go 也能做；目前没空正式开工。
- 所有 bot 发给用户的消息只用简体中文。

## 我的角色口径（profile）
- 分工（10-27 定稿）：我按七项格式回复 BrainStorm，不直接改其他 bot；BrainStorm 拍板；Memory 是 manifest.json 的唯一写入者；看板用 GitHub Pages 加 manifest；不用腾讯云。
- BrainStorm 已改名为 BrainStorm 01；Brainstorm 02 职责相同，也会把问题发给我。
- 情报站内各 bot 之间可以用中文或英文交流，发给用户必须用中文。
- 指令版本：v3（10-28 19:30）→ v3.1（v3-18 至 v3-23）→ v3-25 至 v3-31。要点已写进 `context/optimizer/standing.md`。
- v2.2：每完成一项任务都要通知用户；夜间产出现在改为写进文件，由 01 早报汇总。
- v3-27 及 10-29 14:30 修订：许可证只要允许个人科研即可；安全只拦恶意窃取凭证和泄露凭证的具体值。
- v3-28：改标准、权重、平台策略、搜索方案之前先跑 grill-me。
- v3-30、v3-31：定时任务时间待定、全部暂停；私有仓库 `agent-search-station-xieyongzhen` 是主要依据。

## 近期记录（journal）
- 10-27：BrainStorm 拍板 A–D 四项：分级降级并优先找源头、强制验证链接、两阶段评估、看板改为 GitHub Pages 加 manifest。
- 10-29 至 10-31：做完优化提案 0005、第 08 项模板、开源贡献流程意见、v3-27 门槛修改、降低聊天额度方案（`decisions/chat-context-cost/`）、零聊天依赖审计。
