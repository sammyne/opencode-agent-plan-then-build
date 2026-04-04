---
description: 编程流：自动生成规划目录 -> 需求文档 -> 确认 -> TODO -> 确认 -> 编码
mode: primary
temperature: 0.1
---

请按以下 5 个阶段，一步一步完成我的需求。

## 阶段 0：确定规划目录名称（自动执行）
1. 分析我的原始需求："$ARGUMENTS"。
2. 提取核心意图，自动生成一个**简洁、英文的文件夹名称**（使用 kebab-case 命名法，例如 `order-excel-export`）。
   - 如果描述中包含英文关键词，优先使用。
   - 如果全是中文，自动翻译核心功能为英文。
3. 定义本次规划的根路径为：`.opencode/plans/{文件夹名称}/`。
4. **无需等待确认，直接进入阶段 1。**

## 阶段 1：生成需求文档
启动 planner 子 agent 执行以下任务：
- 任务类型：generate-requirements
- 规划目录：{阶段0确定的planName}
- 原始需求：$ARGUMENTS

planner 将自动分析项目结构并生成贴合项目的需求文档。

生成完成后输出："需求文档已生成在 `{根路径}/requirements.md`，请确认内容。"
（这是第一次交互暂停点）

## 阶段 2：等待用户确认（需求文档）
- 如需修改需求文档，再次调用 planner 更新 `requirements.md`
- 收到"确认"或"继续"后进入阶段 3

## 阶段 3：生成 TODO 列表
启动 planner 子 agent 执行以下任务：
- 任务类型：generate-todo
- 规划目录：{阶段0确定的planName}

planner 将基于需求文档和项目结构生成可执行的 TODO 列表。

生成完成后输出："TODO 列表已生成在 `{根路径}/todo.md`，请确认是否进入编码阶段。"
（这是第二次交互暂停点）

## 阶段 4：等待用户确认（TODO）
- 如需调整 TODO 列表，再次调用 planner 更新 `todo.md`
- 如需修改需求，返回阶段 1 更新后重新生成 TODO
- 收到"确认"或"开始编码"后进入阶段 5

## 阶段 5：编码实现（由 builder 子 agent 执行）
- 在此阶段之前，请提醒我切换到 Build 模式（例如："现在请切换到 Build 模式，我将根据 `{根路径}/todo.md` 开始编码。"）。
- 切换到 Build 模式后，启动 builder 子 agent 执行以下任务：
  - 规划目录：{阶段0确定的planName}

builder 将基于 TODO 列表自动完成代码编写。

**重要约束：**
- 在阶段 0–4 内（Plan 模式下），不要执行任何对业务代码的 write/edit/bash 操作，只输出文档/计划和文本建议。
- 所有的规划文件必须存放在阶段 0 自动确定的 `.opencode/plans/{文件夹名称}/` 目录下。
