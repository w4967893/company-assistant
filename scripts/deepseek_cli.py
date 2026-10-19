"""DeepSeek 命令行对话(原根目录 main.py 迁移而来)

运行:python scripts/deepseek_cli.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.llm.client import call_mml


def main():
    print("DeepSeek 命令行对话(输入 q 退出)")
    # 保留历史消息,让模型记住上下文
    history = [{"role": "system", "content": "你是一个乐于助人的助手。"}]

    while True:
        try:
            user_input = input("\n你: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not user_input or user_input.lower() in ("q", "quit", "exit"):
            break

        history.append({"role": "user", "content": user_input})
        reply = call_mml(history)
        history.append({"role": "assistant", "content": reply})
        print(f"DeepSeek: {reply}")


if __name__ == "__main__":
    main()
