"""RAG 文档接口"""

from fastapi import APIRouter

router = APIRouter()


@router.post("")
def upload_document(filename: str) -> dict:
    """上传文档进入 RAG 流程:解析 → 切片 → 向量化 → 入库"""
    # TODO: 调用 app.rag.ingest
    return {"status": "ok"}


@router.get("/search")
def search(q: str) -> dict:
    """检索与问题相关的文档片段"""
    # TODO: 调用 app.rag.retriever
    return {"chunks": []}
