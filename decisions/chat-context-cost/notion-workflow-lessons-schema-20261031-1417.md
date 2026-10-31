# Notion「工作流经验」库 schema 快照（v1）
- 建库：Memory，2026-10-31（UTC+8）；Decisions：dec-20261031-01（用户 14:13「建」，经 BrainStorm 01 转达）
- 规格：decisions/chat-context-cost/notion-workflow-lessons-spec.md；本地条目模板：retros/workflow-lessons/_template.md
- 父页：学习中枢 hub（407d7661-1323-8190-86f1-f6c35f72ab7f）
- 数据库：https://app.notion.com/p/62e1bfcea7354821834a265ae5e9b0ff
- data source：collection://4ecf0b16-0b29-4a6e-acd5-74d30dc90e2f
- 库描述含 schema v1 说明、写入方（Memory 主写；通义千问、豆包工作助理也可写入——用户 2026-10-31 14:30 原话「千问豆包也可以」，经 BrainStorm 01 转达；14:3x 已更新 Notion 库描述与 dec-20261031-01）和白话写作规范。
- 条目：0（未写示例）

## 字段（17，回读核对一致）
| 字段 | 类型 | 选项 / 说明 |
|---|---|---|
| 标题 | title | |
| 经验编号 | text | exp-YYYYMMDD-序号 |
| 类型 | select | 踩坑 / 原则 / 设计模式 / 约定其他 |
| 场景/症状 | text | 踩坑必填 |
| 原因 | text | 踩坑必填 |
| 解法 | text | 踩坑必填 |
| 表述 | text | 原则类必填 |
| 适用边界 | text | 原则类必填 |
| 反例 | text | |
| 相关路径 | text | |
| 是否仍有效 | select | 有效 / 已过时 / 待复核 |
| 日期 | date | |
| 涉及 bot | multi_select | 01、02、Searcher、质量评估、Memory、优化规划师、Todos、Github 管家、配图、科研大师 |
| 标签 | multi_select | 安全审查、搜索噪音、额度、Notion、仓库、登录、上下文 |
| 关联 Decision | relation（单向）| → Decisions collection://dac471bb-bd60-4ae3-8ba1-b5a75a1994dd |
| 本地文件 | text | |
| 状态 | status | 草稿（to_do，默认）/ 已发布（in_progress）/ 废止（complete） |

## 视图（5 + 默认 Default view）
1. 仍有效：是否仍有效 = 有效，按日期倒序
2. 按类型：按类型分组（显示空组），按日期倒序
3. 按涉及 bot：按涉及 bot 分组，按日期倒序
4. 按标签：按标签分组，按日期倒序
5. 本周新增：日期 ≥ 一周前（MCP 不支持「本周」相对值，改用滚动 7 天；需要严格自然周可在 Notion 界面改成 This week）

## 偏差
- 「必填」Notion 无法强制，只写在字段描述里。
- 状态「已发布」放在 in_progress 组（Notion status 只有三组）。
- 规格写「Memory 独写」，本次按 01 转达写成「Memory 主写，千问/豆包可补草稿」。
