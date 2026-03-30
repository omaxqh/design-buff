# 跨平台适配

`design-buff` 的核心方法仍以仓库里的 `SKILL.md` 和 `references/` 为准，但主流 Agent 运行时接入方式不同，所以仓库里额外提供了一层轻量适配。

当前适配目标:

- `Codex`: 直接使用原生 Skill
- `Claude Code`: 使用 `CLAUDE.md` 和 `.claude/commands/`
- `Cursor IDE`: 使用 `.cursor/rules/*.mdc`
- `Cursor CLI` 与其他兼容 Agent: 使用项目根目录 `AGENTS.md`

这层适配遵循两个原则:

1. 核心方法只保留一套，避免多份 prompt 漂移
2. 平台差异只处理入口和载体，不改 Design Buff 的评审标准

## 安装脚本

仓库提供一个安装脚本，把精简后的可移植指令写入目标项目:

```bash
python3 scripts/install_adapter.py claude-code --scope project --target /path/to/project
python3 scripts/install_adapter.py claude-code --scope user
python3 scripts/install_adapter.py cursor --target /path/to/project
python3 scripts/install_adapter.py generic-agents --target /path/to/project
```

安装策略:

- `claude-code`
  - 项目级: 写入 `<project>/.claude/CLAUDE.md`
  - 用户级: 写入 `~/.claude/CLAUDE.md`
  - 同时生成自定义命令 `.claude/commands/design-buff-review.md`
- `cursor`
  - 写入 `<project>/.cursor/rules/design-buff-review.mdc`
- `generic-agents`
  - 写入 `<project>/AGENTS.md`

脚本会使用带标记的托管区块更新 `CLAUDE.md` 或 `AGENTS.md`，不会粗暴覆盖整个文件。专用命令文件和规则文件则直接以 `design-buff-review` 这个固定文件名写入。

## 使用建议

### Claude Code

- 安装项目级适配后，直接在项目里使用 `/design-buff-review`
- 如果团队已经有自己的 `CLAUDE.md`，脚本会把 Design Buff 追加成一个托管区块
- 需要持久化使用时，优先把项目级适配文件提交到仓库

### Cursor IDE

- 安装后，`design-buff-review.mdc` 会作为一个 `Agent Requested` 规则存在于 `.cursor/rules/`
- 在设计评审、Figma、截图、转化流程诊断这类请求里，Cursor Agent 可以自动调用这条规则
- 如果你想让 Cursor CLI 也稳定读取同一套入口，可以额外安装 `generic-agents`

### 通用 CLI / IDE

- 对于会读取项目根目录 `AGENTS.md` 的工具，安装 `generic-agents` 即可
- 如果工具本身支持更强的规则系统，再叠加对应平台适配会更稳

## 官方依据

这层适配基于当前官方文档:

- Claude Code 通过 `CLAUDE.md` 提供持久指令，通过 `.claude/commands/` 提供自定义 slash commands，并支持 `.claude/rules/` 规则拆分
- Cursor 通过 `.cursor/rules/*.mdc` 提供项目规则；Cursor CLI 还会读取项目根目录的 `AGENTS.md` 和 `CLAUDE.md`

参考:

- [Claude Code: How Claude remembers your project](https://code.claude.com/docs/en/memory)
- [Claude Code: Slash commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands)
- [Cursor: Rules](https://docs.cursor.com/context/rules)
- [Cursor: Using CLI](https://docs.cursor.com/en/cli/using)
