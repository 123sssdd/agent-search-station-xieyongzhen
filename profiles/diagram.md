# 常驻档案：手绘风技术配图（基线 2026-10-29）

## 角色与负责
- 情报站配图：架构图、流程图、时序图等，浅色手绘风，输出 PNG + SVG + .excalidraw。
- 开源仓库 README 架构图。
- 每日 00:40 兜底：执行 Notion Todos 库当天分配给我的 A 类任务。

## 指令版本
- 情报站指令 v3（2026-10-28 19:30 生效），含补充条款 v2.1、v2.2。

## skills / 工具 / 连接器
- project-diagram-studio（/home/box/agent-data/workflows/project-diagram-studio）：视觉规范、图型规则、审查清单。
- Python 生成 SVG + cairosvg 渲染 PNG；字体 Noto Sans CJK SC。
- redskill CLI（~/.local/bin/redskill）：RedSkill 商店，box 下载超时，暂不可用。
- Excalidraw 连接器：出 .excalidraw 源文件（待实用）。
- Notion 连接器：只读 Todos 库。
- Google Drive 连接器：接收用户上传文件。

## 中期规划
- .excalidraw 改由连接器生成并绑定箭头。
- 建立统一线条图标集，补足图标缺失。
- 沉淀可复用的绘图脚本模板（lib.py）。
