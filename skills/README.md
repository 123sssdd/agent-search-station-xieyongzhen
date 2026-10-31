# Skills 备份
`user-workflows/` 是用户自建 skill（原位置 /home/box/agent-data/workflows/），恢复时用 UpdateSkill 逐个写回。
Cursor 内置 skill 和已装插件 skill 无需备份，重装插件即可。已排除 >10MB 文件、压缩包、node_modules、.venv。
