"""
对话管理模块
负责管理 LLM 对话和历史记录
"""

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from typing import List
from pydantic import SecretStr

from config import get_openai_api_key, get_model_name, get_temperature


class ChatBot:
    """
    极简聊天机器人类
    """

    def __init__(self):
        """
        初始化聊天机器人
        """
        # 获取配置
        api_key = get_openai_api_key()
        model_name = get_model_name()
        temperature = get_temperature()

        # 初始化 LLM (API Key 需要转换为 SecretStr)
        self.llm = ChatOpenAI(
            api_key=SecretStr(api_key),
            model=model_name,
            temperature=temperature,
        )

        # 对话历史
        self.history: List[BaseMessage] = []

    def chat(self, user_input: str) -> str:
        """
        处理用户输入并返回机器人回复

        Args:
            user_input: 用户输入的文本

        Returns:
            str: 机器人的回复文本
        """
        # 将用户输入添加到历史
        human_message = HumanMessage(content=user_input)
        self.history.append(human_message)

        # 构建消息列表
        messages = self.history.copy()

        # 调用 LLM
        try:
            response = self.llm.invoke(messages)
            ai_message = str(response.content)

            # 将 AI 回复添加到历史
            self.history.append(AIMessage(content=ai_message))

            return ai_message

        except Exception as e:
            # 如果出错，从历史中移除用户消息
            self.history.pop()
            raise Exception(f"调用 LLM 时出错: {str(e)}")

    def clear_history(self):
        """
        清空对话历史
        """
        self.history = []
        print("对话历史已清空")

    def get_history_count(self) -> int:
        """
        获取当前对话轮数
        """
        return len(self.history) // 2  # 每轮对话包含用户和 AI 两条消息
