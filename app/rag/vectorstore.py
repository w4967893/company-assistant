"""向量库抽象:先做内存实现,后续可替换 Milvus / PGVector"""


def save(chunks: list[str], vectors: list[list[float]]) -> None:
    """文本块连同向量入库"""
    # TODO
    raise NotImplementedError


def search(vector: list[float], top_k: int = 5) -> list[str]:
    """按相似度检索 top_k 个文本块"""
    # TODO
    raise NotImplementedError
