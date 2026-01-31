# LangChain Chatbot

极简的 LangChain 聊天机器人示例项目。

## 功能特点

- 🤖 基于 LangChain 框架
- 💬 支持多轮对话
- 📝 对话历史管理
- ⚙️ 灵活的配置选项
- 🖥️ 简单的命令行界面

## 快速开始

### 1. 克隆项目

```bash
cd langchain-chatbot
```

### 2. 创建虚拟环境

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
.\venv\Scripts\activate   # Windows
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 配置环境变量

复制 `.env.example` 为 `.env` 并填入你的 API Key：

```bash
cp .env.example .env
```

编辑 `.env` 文件：

```env
OPENAI_API_KEY=your_api_key_here
```

### 5. 运行程序

```bash
python main.py
```

## 使用说明

- 直接输入内容与机器人对话
- 输入 `/clear` 清空对话历史
- 输入 `/count` 查看对话轮数
- 输入 `/quit` 退出程序

## 配置选项

在 `.env` 文件中可以配置以下参数：

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `OPENAI_API_KEY` | OpenAI API Key | 必需 |
| `MODEL_NAME` | 使用的模型名称 | gpt-3.5-turbo |
| `TEMPERATURE` | 温度参数 (0.0-2.0) | 0.7 |
| `MAX_TOKENS` | 最大输出 token 数 | 1024 |

## 项目结构

```
langchain-chatbot/
├── config.py          # 配置管理模块
├── chat.py            # 对话管理模块
├── main.py            # 主程序入口
├── requirements.txt   # 依赖列表
├── .env.example       # 环境变量模板
└── README.md          # 项目说明
```

## 依赖

- langchain >= 0.2.0
- langchain-openai >= 0.1.0
- python-dotenv >= 1.0.0

## 许可证

MIT License
