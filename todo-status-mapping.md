# Todos 状态映射（Notion ↔ 本地 todo-management）

- 日期：2026-10-28（Asia/Shanghai）
- Notion 主库：Todos `collection://0312e3e7-3dce-4746-ad2d-6a70076d7c38`（database `78895c6f-2952-43ad-ab9a-17217c75f450`）
- 本地备份：`TODO_DB=/workspace/todos/todo.db`（`todo-management` CLI）
- Notion 为主库；本地永不反向写入 Notion。

## Notion `状态`（原生 status）

| 选项 | 分组 | 本地 status | 本地文本约定 |
|------|------|-------------|--------------|
| 待办 | to_do | pending | 无额外前缀 |
| 待用户决定 | to_do | pending | 文本含「待用户决定」或等价备注 |
| 阻塞 | to_do | pending | 文本含【阻塞】或【延后】 |
| 进行中 | in_progress | in_progress | 无额外前缀 |
| 已完成 | complete | done | 无额外前缀 |
| 已取消 | complete | skipped | 无额外前缀 |

分组约定（schema v1+）：
- to_do：待办、待用户决定、阻塞
- in_progress：进行中
- complete：已完成、已取消

默认选项：待办。

## 「待同步」流程

1. 写 Notion 失败时：仍写本地，文本前缀 `【待同步】` + `todo_id` + 拟写入的 Notion 字段摘要。
2. 下一写周期：`entry list --all`，筛文本含 `【待同步】` 的条目，按摘要重试 Notion。
3. Notion 成功后：去掉 `【待同步】` 前缀（或 `entry edit` 更新为已同步摘要）；本地 status 按上表对齐。
4. 冲突时以 Notion 为准，不把本地改动推回 Notion。

## 延后约定

用户拍板「从待用户决定移除；标延后」时：
- Notion：`状态` → 阻塞；`决策方式` 保持 用户决策；`决策选项/备注` 前置 `【延后 YYYY-MM-DD】…`
- 本地：status 仍为 pending；文本含【延后】与 todo_id
