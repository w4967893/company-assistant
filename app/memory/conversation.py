"""会话历史:多轮上下文管理"""


def get_history(session_id: str) -> list[dict]:
    """读取一个会话的全部消息"""
    # TODO: 从 store 读取
    raise NotImplementedError


def append_message(session_id: str, role: str, content: str) -> None:
    """追加一条消息到会话"""
    # TODO
    raise NotImplementedError
