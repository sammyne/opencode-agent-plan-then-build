# 先规划后编码的 OpenCode Agent

此项目用 .opencode/agents/plan-then-build.md 文件自定义了一个 OpenCode Agent，用于实现以下分阶段编程工作流

```
自动生成规划目录 -> 需求文档 -> 确认 -> TODO -> 确认 -> 编码
```

## 快速开始

1. 将 .opencode 目录拷贝到你的项目根目录；
2. 在 opencode 的 TUI 界面，切换到 plan-then-build agent；
3. 输入以下提示词
    ```
    用 langchain 实现一个极简聊天机器人
    ```

即可开始分阶段编码流程，产出
- .opencode/plangs/langchain-chatbot 下的需求文档和待办清单；
- python 项目 langchain-chatbot（如需将代码生成在根目录，最后补一个移动代码的指令即可）

## 参考文献
- https://opencode.ai/docs/agents/
