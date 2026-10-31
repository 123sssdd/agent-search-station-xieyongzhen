# 决定：轮次锁 6 小时过期

- 状态：已确认（用户 2026-10-29 12:22 回复“确认”，追认 10-28 起执行的规则）
- 内容：开轮前检查 rounds/ 下有无未过期 .lock；没有才写 `rounds/<轮次id>.lock`（owner、开始时间、当前进度），每推进一步更新，结束改名 .done。锁 6 小时无更新即过期；接手方须先 priority:true 告知原 owner。
- 目的：防止 01/02 重复接同一轮；owner 掉线时不至于永久卡死。
- 出处：search-station-workflow/decisions/2026-10-28.md 第 3 条、docs/workflow.md。
