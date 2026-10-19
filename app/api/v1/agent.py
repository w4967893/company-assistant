"""Agent 任务接口"""

from fastapi import APIRouter

router = APIRouter()


@router.post("")
def run(task: str) -> dict:
    """执行一个 Agent 任务"""
    # TODO: 调用 app.agent.executor.run_agent
    return {"result": ""}
