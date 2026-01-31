"""
主程序入口
极简 LangChain 聊天机器人 CLI
"""

import sys
from chat import ChatBot


def print_welcome():
    """打印欢迎信息"""
    print("\n" + "=" * 50)
    print("  极简 LangChain 聊天机器人")
    print("=" * 50)
    print("\n输入内容与机器人对话，输入以下命令：")
    print("  /clear - 清空对话历史")
    print("  /count - 查看对话轮数")
    print("  /quit  - 退出程序")
    print("\n" + "-" * 50)


def main():
    """
    主函数
    """
    print_welcome()

    try:
        # 初始化聊天机器人
        chatbot = ChatBot()
        print("\n机器人已就绪，开始对话吧！\n")
    except ValueError as e:
        print(f"\n配置错误: {e}")
        print("\n请确保在 .env 文件中设置了 OPENAI_API_KEY")
        sys.exit(1)
    except Exception as e:
        print(f"\n初始化失败: {e}")
        sys.exit(1)

    # 主循环
    while True:
        try:
            # 获取用户输入
            user_input = input("\n你: ").strip()

            # 处理空输入
            if not user_input:
                continue

            # 处理命令
            if user_input.startswith("/"):
                command = user_input.lower()

                if command == "/quit":
                    print("\n感谢使用，再见！")
                    break

                elif command == "/clear":
                    chatbot.clear_history()

                elif command == "/count":
                    count = chatbot.get_history_count()
                    print(f"\n当前对话轮数: {count}")

                else:
                    print(f"\n未知命令: {user_input}")
                    print("可用命令: /clear, /count, /quit")

                continue

            # 正常对话
            print("\n机器人: ", end="", flush=True)

            try:
                response = chatbot.chat(user_input)
                print(response)

            except Exception as e:
                print(f"\n错误: {e}")

        except KeyboardInterrupt:
            print("\n\n检测到中断信号，正在退出...")
            print("\n感谢使用，再见！")
            break

        except Exception as e:
            print(f"\n发生未知错误: {e}")


if __name__ == "__main__":
    main()
