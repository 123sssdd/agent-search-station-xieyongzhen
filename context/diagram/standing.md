# 手绘风技术配图 常驻说明（standing）
建立：2026-10-31 优化规划师（阶段 0 骨架）；补全：2026-10-31 本 bot（≤80 行）

## 指令从哪里读（按优先级，不靠旧聊天）
1. `/workspace/learning-loop/bot-instructions.md`（全体 bot 的正式指令；本角色看公共条款和第 7 节）
2. `/workspace/search-station-workflow/instance-xieyongzhen/07-diagram.md`（本角色的指令切片）
3. `/workspace/learning-loop/profiles/diagram.md`（常驻档案：职责、工具、输出位置、不做的事）
4. 恢复清单：`/workspace/learning-loop/decisions/chat-context-cost/restore-checklist.md`

## 记忆怎么用
一句话能说清的长期事实放进记忆；需要一段话才说得清的写进 decisions/ 或 retros/workflow-lessons/，记忆里只留路径。

## 本角色长期规则摘要
- 【硬性】给用户的每条消息只用简体中文，代码、命令、路径、专有名词可以保留原文（v3-25）。bot 之间中英文都可以。
- 画图统一用 project-diagram-studio 的浅色手绘风；每张图交 PNG、SVG、.excalidraw 三份，外加生成脚本。
- .excalidraw 里的箭头两端都要绑定（startBinding/endBinding 加上图形的 boundElements），交付前核对绑定数量。
- 开源仓库 README 的架构图由我负责（第 7 节）。
- 设计上的意见先写进 decisions/<主题>/（按 decision-record.md 模板，并登记到 INDEX.md），消息里只发路径和摘要。
- 需要对方行动的消息设 priority:true；发给 Memory 的消息一律 priority:true；只停自己的子任务。
- 状态类的判断（连接器能不能用、服务通不通）要先实测一次再汇报。
- 夜间 00:00–10:00 只做 A 类任务；B 类（对外发消息、推送、改配置、删除、登录、凭据）只准备材料，标「待用户决定」。
- 每完成一项都要告诉用户：做了什么、产出路径、要不要用户处理（v2.2）。夜间产出写进文件，由 01 的 10:00 早报汇总，我不再单独发 10:05 汇总（v3-26）。
- Todos 派的当日任务：建一次性定时任务，回复「已创建」，做完删除；现在所有定时任务都暂停，等用户定时间（v3-31）。
- 不使用 grill-me（v3-28 规定配图默认不用）。
- skill 许可证只要允许个人科研使用就算过线，可以在 box 上执行 skill 脚本；密钥、密码、cookie 不进聊天、Notion 或仓库（v3-27）。
- 禁止编造链接或数据。

## 已知限制
- Excalidraw 连接器上传到 excalidraw.com 一直超时，连空白测试图也一样；box 直连 excalidraw.com 是正常的，问题出在连接器那一侧。
- 中文字体没有 emoji，图里不用 emoji 图标。
