"""检索:向量召回 + 重排"""


def retrieve(query: str, top_k: int = 5) -> list[str]:
    """检索与问题最相关的文本块"""
    # TODO: embed(query) → vectorstore.search → 重排
    raise NotImplementedError
