# Reference-Guided Paper Polishing

一个面向科研论文的参考论文仿写、结构重构与润色 skill。它把“看项目、读参考论文、模仿写法、重写主稿和图注、核验结果”串成一条可重复执行的证据链，重点防止三类常见错误：

- 为了语言更流畅而改变科学结论；
- 把参考论文的机制、来源或临床验证强度直接迁移到证据不足的新研究；
- 修饰句子之前没有先校正主张层级、数字口径和图注一致性。

## 1. 适用场景

适合：

- 已有科研项目、数据结果、论文草稿和参考论文，需要系统重写；
- 想借鉴优秀论文的研究逻辑、章节结构、语言表达和语义边界；
- 需要同步修改中文稿、英文稿、摘要、Results、Discussion 和图注；
- 需要把项目事实、任务书、参考卡片和修订记录做成可交接文件；
- 稿件存在过度解释、防御性写作、术语漂移或图文口径不一致。

不适合：

- 只改一个单词、标点或纯语法问题；
- 只重绘图片，不处理稿件主张与图注；
- 在没有项目数据或权威结果的情况下代写研究结论；
- 只按“像某篇论文”做逐句改写或复制措辞。

## 2. 调用方式

自动发现已启用。也可以显式调用：

```text
使用 $reference-guided-paper-polishing 审阅这个科研项目。
项目目录：D:\project
当前主稿：D:\project\paper\draft.md
参考论文：D:\project\references
目标：重写中文主稿、英文稿和 Figure 1–5 图注。
```

如果不指定语言或期刊，skill 会采用适合该领域的通用高影响力论文结构，并明确说明这一选择，不虚构期刊格式。

## 3. 输入

最好提供：

- 项目根目录和当前权威稿件；
- 正式结果表、统计输出或验证脚本；
- Figure 文件、现有图注和图件说明；
- 项目交接记录、修改说明和任务记录；
- 希望参考的论文全文、摘要或 DOI；
- 目标语言、目标期刊和允许的改动范围。

如果路径缺失，skill 会先在工作区内寻找合理替代，并记录替代关系。最新修改时间不会被自动视为权威版本。

## 4. 完整流程

### 阶段一：项目证据审阅

确定当前事实，形成：

- 权威文件表；
- 一句话 North Star；
- 中心科学问题；
- 主张—证据架构；
- confirmed / assumed / unresolved 事实；
- Figure、Supplementary 和图注资产清单；
- 主要科学、结构和术语风险。

若核心主张无法由现有证据支持，会先停止润色并报告证据缺口。

### 阶段二：任务文件

将审阅结果转成单独任务书，写明：

- 修改目标；
- 输入版本；
- 允许和禁止的改动；
- 规范术语；
- 必须保持的数字与加和关系；
- 交付物；
- 验收标准；
- 已知阻塞项。

### 阶段三：参考论文分析

优先深读用户提供的论文。需要扩展时，可按 DOI、PMID、PMCID 等联网检索同类研究。每篇论文会提取：

- 研究问题、目的和缺口；
- 研究路线与证据顺序；
- Claim–Evidence Chain；
- 语言姿态和段落功能；
- 作者明确承认的限制；
- 哪些结论能迁移，哪些只因研究设计不同而不能迁移。

### 阶段四：写作机制迁移

建立“目标章节 × 参考机制 × 安全迁移方式 × 不可迁移点”的矩阵。迁移的是段落分工、推理顺序、证据密度和边界位置，不复制句子或独特措辞。

### 阶段五：分层重写

按以下顺序处理：

1. 主张层级与章节任务；
2. Results 证据顺序；
3. 段落逻辑与读者前置知识；
4. 语义边界和动词强度；
5. 防御性写作；
6. 句法、节奏和中文自然化；
7. Figure legend 与主文同步。

### 阶段六：验证与交付

检查：

- 数字、分母、P 值、CI、FDR 和分类总数；
- 引文覆盖与 DOI；
- 术语一致性；
- 图文面板对应；
- 保留下来的必要限制；
- 未被隐藏的机制、来源或临床验证缺口。

交付通常包括版本化主稿、同步图注、修订说明和项目工作文件。

## 5. 输出文件示例

```text
work/
|-- 01_project_evidence_audit.md
|-- 02_reference_style_synthesis.md
|-- 03_task_brief.md
|-- 04_revision_report.md
|-- reference_cards/
|-- expanded_references/
`-- package-check.json
```

主稿和图注应写入新文件，除非用户明确要求原地修改。

## 6. 目录结构

```text
reference-guided-paper-polishing/
|-- SKILL.md
|-- README.md
|-- agents/
|   `-- openai.yaml
|-- references/
|   |-- project-audit-and-task.md
|   |-- reference-analysis-and-transfer.md
|   `-- rewrite-and-validation.md
`-- scripts/
    `-- check_manuscript_package.py
```

### [SKILL.md](SKILL.md)

技能入口和必须遵守的操作契约。

### [references/project-audit-and-task.md](references/project-audit-and-task.md)

项目文件优先级、权威版本判断、Claim–Evidence Map、任务书模板和并行工作边界。

### [references/reference-analysis-and-transfer.md](references/reference-analysis-and-transfer.md)

参考论文卡片、外部扩展、来源等级、语义边界阶梯和写作机制迁移矩阵。

### [references/rewrite-and-validation.md](references/rewrite-and-validation.md)

章节契约、Results 证据顺序、防御性写作边界、图注规范、双语同步和最终验收。

### [scripts/check_manuscript_package.py](scripts/check_manuscript_package.py)

只使用 Python 标准库的确定性检查器，用于验证显式声明的稿件不变量。

## 7. 使用验证脚本

在项目中创建 `package-check.json`：

```json
{
  "files": [
    "paper/manuscript-zh.md",
    "paper/figure-legends.md"
  ],
  "required_phrases": [
    "1,007",
    "980",
    "72.0%"
  ],
  "forbidden_phrases": [
    "913"
  ],
  "reference_count": 31,
  "require_reference_doi": true,
  "citation_range": [1, 31],
  "sums": [
    {"total": 1007, "parts": [980, 27]},
    {"total": 980, "parts": [54, 13, 607, 306]},
    {"total": 107, "parts": [67, 40]}
  ],
  "required_concepts": [
    "cell-type expression association",
    "validation"
  ]
}
```

运行：

```bash
python scripts/check_manuscript_package.py package-check.json
```

也可以从标准输入读取：

```bash
cat package-check.json | python scripts/check_manuscript_package.py -
```

检查器可验证：

- 文件存在且可读；
- 必需与禁用短语；
- Markdown 代码围栏是否成对；
- 参考文献数量和 DOI；
- 正文引用是否覆盖指定范围；
- 各文件的引用覆盖是否一致；
- 显式声明的加和关系；
- 必需术语或边界概念。

检查器不能证明：

- 某条引文确实支持对应句子；
- 统计模型或显著性判断正确；
- 图面视觉上没有重叠或裁切；
- 稿件已经达到目标期刊的投稿要求。

这些仍需人工审计，并可配合 `claim-source-verification`、`citation-verifier`、`nature-statistics` 与 `submission-audit`。

## 8. 与其他 skill 的关系

根据已安装环境，本 skill 会按需协同：

- `paper-workflow`：通用论文任务的链路路由；
- `manuscript-optimizer`：主张架构和章节逻辑；
- `nature-paper-card`：参考论文深度卡片；
- `nature-academic-search`：文献发现和元数据检索；
- `claim-source-verification`：句子和引用来源的对应核验；
- `anti-defensive-writing`：删除防御性表达但保留必要限制；
- `humanizer-zh`：中文自然化；
- `scientific-prose-style`：句级节奏和标点；
- `figure-planner`：面板角色和图注；
- `documents`：需要 DOCX 时执行渲染与版式检查。

这些不是重复步骤。每层负责不同缺陷，前一层没有稳定时不应跳到下一层。

## 9. 核心原则

- 科学正确性优先于逻辑，逻辑优先于信息结构，信息结构优先于润色。
- 相关性不自动升级为因果、来源、装载机制或临床效用。
- 参考论文是写作机制来源，不是结论授权来源。
- 必要限制应保留一次，放在实际约束结论的位置。
- 先修主张和图注，再做句子润色。
- 原稿保留；输出版本化新文件。
- 无法由文字解决的证据缺口，必须报告，不能用更强的措辞填补。

## 10. 质量验证

技能创建时已完成：

- `quick_validate.py`：通过；
- Python 脚本语法检查：通过；
- 使用真实 v21 稿件验证引用、DOI 和数字加和：通过；
- 独立小项目前向测试：通过，未把非配对数据写成来源确认，也未迁移参考论文的术后动态、RT-ddPCR 或诊断验证结论。

## 11. 典型请求模板

```text
使用 $reference-guided-paper-polishing 完成以下任务：

项目目录：...
当前主稿：...
结果与图件说明：...
参考论文：...
目标语言：中文 + 英文图注
目标期刊：暂未确定

请先审阅项目和现行结果，形成项目报告与任务文件；
再阅读参考论文并建立参考卡片和写作迁移矩阵；
然后重构主稿和图注；
最后检查数字、引用、术语和证据边界，并列出仍未解决的事项。
```

## 12. 环境

- 无需额外 Python 包即可运行检查器；
- 建议 Python 3.9 或更高版本；
- 自动发现默认开启；
- 显式名称为 `$reference-guided-paper-polishing`。
