# Plan: oss-contrib Notion upsert (23)

## Goal
按用户 20:18「可先入库看看」把 registry.json 23 条按 issue_key 单向 upsert 到开源项目贡献管理库；先补 schema（待定/候补/Clojure），记 Decisions，不回写 registry、不推 git。

## Phases

### Phase 1: Schema precheck + Decisions + ALTER
**Status:** complete
- 缺口：优先级+待定；状态+候补；语言+Clojure
- dec 编号：无 dec-20261030-*，用 **dec-20261030-01**（今日首条；父指令备选 29-11，按日期规范用 30-01）
- 轮次 20261030-1944-01 不在轮次库 → 不建轮次行，备注写 round_id

### Phase 2: Upsert 23 rows
**Status:** complete
- 库当前 0 行；全新建
- ≤3/s；类型/负责人/PR 空；进度字段待定/候选|候补

### Phase 3: Spot-check + report
**Status:** complete
- 回读 ≥5 条含 2 候补
- 回 Github 管家 + SendToUser 中文收据

## Next Step
完成：新建23/更新0/失败0；dec-20261030-01；schema+待定+候补+Clojure。
