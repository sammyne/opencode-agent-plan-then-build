"""
配置管理模块
负责读取环境变量和配置 LLM 参数
"""

import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()


def get_openai_api_key() -> str:
    """
    获取 OpenAI API Key
    从环境变量 OPENAI_API_KEY 读取
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "未找到 OPENAI_API_KEY 环境变量。\n"
            "请在 .env 文件中设置 OPENAI_API_KEY，或在环境中导出该变量。"
        )
    return api_key


def get_model_name() -> str:
    """
    获取使用的模型名称
    从环境变量 MODEL_NAME 读取，默认为 gpt-3.5-turbo
    """
    return os.getenv("MODEL_NAME", "gpt-3.5-turbo")


def get_temperature() -> float:
    """
    获取模型温度参数
    从环境变量 TEMPERATURE 读取，默认为 0.7
    """
    temp = os.getenv("TEMPERATURE")
    if temp is None:
        return 0.7
    try:
        return float(temp)
    except ValueError:
        print(f"警告：TEMPERATURE 值 '{temp}' 无效，使用默认值 0.7")
        return 0.7


def get_max_tokens() -> int:
    """
    获取模型最大 token 数
    从环境变量 MAX_TOKENS 读取，默认为 1024
    """
    max_tok = os.getenv("MAX_TOKENS")
    if max_tok is None:
        return 1024
    try:
        return int(max_tok)
    except ValueError:
        print(f"警告：MAX_TOKENS 值 '{max_tok}' 无效，使用默认值 1024")
        return 1024
