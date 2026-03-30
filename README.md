# Design Buff

`Design Buff` 不是一个“审美打分器”，而是一个面向业务与体验的设计评审 Skill。它会基于 Figma、截图、页面结构和补充材料，快速重建设计背后的上下文：这是哪个场景、服务谁、要完成什么业务目标、处在产品链路的哪个位置。它看的不是一张静态图，而是一条真实会发生的用户路径。

它最核心的能力，是把设计从“页面视角”拉回到“决策视角”。用户来到一个界面，不是在欣赏，而是在判断：我要不要点、我懂没懂、我信不信、出错怎么办。Design Buff 会系统检查这些关键问题，把模糊的“感觉不太对”翻译成明确的结构问题、认知问题和信任问题。设计不是把信息摆上去，而是替用户减少一次猜测。

这个 Skill 的输出，代表的是一个从业 10 年的体验设计 TL 在设计审核里会重点盯住的问题。它的目标不是替代设计师判断，而是帮设计师更早发现阻力、更早修正结构，把自己 buff 起来。

## 核心价值

### 1. Skill 构建理念

Design Buff 会先补齐设计背景，再进入评审。它会优先确认这条方案服务的是谁、用户为什么会来到这里、他们带着什么预期、页面在整条任务链里承担什么责任。这样做的原因很简单：真正会影响结果的设计问题，往往不在视觉表面，而在任务判断、信息组织和信任建立上。

它评审的重点，不是“页面看起来是否完整”，而是“用户是否能自然地走下去”。当一个方案让用户多猜一步、多想一步、多担心一步，Design Buff 会把这种隐形阻力具体指出来。

### 2. Killer Feature：三流一致性

Design Buff 特别强调一个很少被认真检查、但对转化极关键的能力：三流一致性。这里的“三流”指的是：

- `旅程流`: 用户在整个任务里走到哪一步，整条大链路是否成立
- `操作流`: 当前这一步到底让用户做什么，动作是否清楚、反馈是否连续
- `心智流`: 用户此刻是安心、犹豫、怀疑，还是已经准备放弃

很多方案单看页面本身并没有明显错误，但这三条流一旦脱节，用户就会出现“看得懂，却不敢点；能点下去，却不知道后面会怎样”的状态。Design Buff 会把这些断裂点提前找出来，指出到底是旅程断了、操作断了，还是信任断了。

### 3. 差异性

和常见设计辅助 Skill 相比，Design Buff 不是“更会挑问题”，而是“更会判断问题为什么会发生”。没有约束的大模型做设计审查，往往停在表现层，例如“按钮不够突出”“文案有点长”“视觉不够统一”。Design Buff 会继续追问：为什么按钮必须突出？用户此刻最怕什么？这段文案是在解释规则，还是在增加决策负担？这一步是主任务，还是把营销、法务、确认、跳转全压在了同一个节点上？

它不会只判断界面是否“完整”，而是会从场景匹配、认知与操作成本、用户心智与习惯、价值承接、基础体验这五个维度去综合论证逻辑是否成立。

### 4. 有效性：证据优先

Design Buff 坚持“证据优先”的工作方式。能从 Figma 结构里确认的，就不让模型自由脑补；能从截图验证的，就不只凭文案推断；能明确说明的就明确说明，不能确认的就标记边界。它会区分 `confirmed`、`visible`、`inferred`、`unknown`，避免把猜测说成结论。

好的评审不是声音大，而是依据硬。不是“我觉得这里不舒服”，而是“这里为什么会让用户停住”。

### 5. 双通道：人机分账

Design Buff 从一开始就把“给机器用的内容”和“给人看的内容”分开处理。底层生成的结构化字段，主要服务于 Agent 之间的衔接和 A2A 场景的链接，方便后续复跑、追踪、比对和继续处理；这部分重点是稳定、可解析、可传递。

而给人看的部分，则放弃了用对话框去承载整份评审，而是直接生成带完整排版的 `report.html`。打开文件就能看到本轮审核结果，阅读顺序、信息层级和版式表达都做过一轮基于人因工程和产品体验的优化，目标不是把字段堆出来，而是让设计师、产品和业务能更快读懂问题、判断优先级并推进修改。

## 一句话总结

好设计不是把界面做满，而是把阻力做少；不是让用户惊叹，而是让用户自然地走下去。Design Buff 的价值，不在于回答“这张图好不好”，而在于更关键地追问一句：

**用户会不会走，为什么会走，走到哪里会停下。**

这才是设计真正该被评审的地方。

## 这个 Skill 会产出什么

Design Buff 会输出一套人机分账、各司其职的评审结果：

- 面向设计团队阅读的 `report.html`
- 面向机器持久化与复跑的 `review-state.json`

仓库里的 `README.md` 只是 GitHub 入口说明。真正的运行合同和流程约束，以 `SKILL.md` 以及 `references/` 下的文件为准。

## 跨平台适配

除了 Codex 原生 Skill 形态，这个仓库现在还提供了面向主流 Agent CLI / IDE 的轻量适配层，目标是让同一套评审方法可以落到不同运行时，而不是为每个平台重新写一份漂移 prompt。

当前支持:

- `Codex`: 直接使用原生 `SKILL.md`
- `Claude Code`: 通过 `CLAUDE.md` 和 `.claude/commands/`
- `Cursor IDE`: 通过 `.cursor/rules/*.mdc`
- `Cursor CLI` 与其他兼容 Agent: 通过项目根目录 `AGENTS.md`

适配相关文件位于 `adapters/`，安装脚本位于 `scripts/install_adapter.py`。详细说明见 `adapters/README.md`。

## 适合用来审什么

- 带业务目标的转化流程
- 多步骤表单、开通、绑定、授权、支付、注册、升级等关键路径
- 需要从 Figma、截图或文档中重建设计意图的方案
- 页面本身看起来“没大错”，但总觉得路径不顺、信任不稳、转化会掉的设计

## 生效合同

更新、分发或二次改造这个 Skill 时，以下文件是当前有效合同：

- `SKILL.md`
- `agents/openai.yaml`
- `references/input-standard.md`
- `references/figma-high-precision.md`
- `references/review-playbook.md`
- `references/report-contract.md`
- `references/review-state-schema.md`

## 仓库结构

```text
.
├── SKILL.md
├── README.md
├── LICENSE
├── .gitignore
├── adapters/
├── agents/
├── references/
├── scripts/
└── templates/
```

## 安装方式

1. 把整个文件夹复制到你的 Codex skills 目录，并命名为 `design-buff`。
2. 运行时保持 Skill 包本身只读，不要把评审产物写回这个仓库。
3. 使用时从被评审项目的根目录发起，而不是从 Skill 仓库内部运行。

### 安装到 Claude Code / Cursor

如果你想把 Design Buff 装到其他 Agent CLI 或 IDE，可直接运行:

```bash
python3 scripts/install_adapter.py claude-code --scope project --target /path/to/project
python3 scripts/install_adapter.py claude-code --scope user
python3 scripts/install_adapter.py cursor --target /path/to/project
python3 scripts/install_adapter.py generic-agents --target /path/to/project
```

这四条命令分别对应:

- 给某个项目安装 Claude Code 版本
- 给当前用户安装 Claude Code 版本
- 给某个项目安装 Cursor IDE 规则
- 给某个项目安装通用 `AGENTS.md` 入口

## 运行产物

正常使用时，Design Buff 不会把产物写进自己的仓库，而是写到被评审项目里：

- 可见产物: `design-buff-reviews/<review-slug>/`
- 临时状态: `.design-buff/<review-slug>/`

这两个目录都属于被评审项目，不属于 Skill 包本身。

## 技术依赖

- 支持 Skill 加载的 Codex 运行环境
- Figma MCP
- Python 3.9+，用于随仓库提供的辅助脚本

没有 Figma MCP 时，Skill 仍可运行，但会退化为截图和文档评审路径，精度会低一些。

## License

MIT，见 `LICENSE`。
