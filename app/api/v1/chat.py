"""对话接口"""

from fastapi import APIRouter

router = APIRouter()


@router.post("")
def chat(message: str) -> dict:
    """对话:读取会话历史 → 调用 LLM → 写回历史"""
    # TODO: 接入 app.memory.conversation 读取/写入历史
    # TODO: 可选接入 app.rag.retriever 注入相关文档片段
    # TODO: 调用 app.llm.client.call_mml 生成回复
    return {"reply": ""}
