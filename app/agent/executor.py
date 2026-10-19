"""Agent 主循环:规划 → 调用工具 → 观察结果 → 循环"""


def run_agent(task: str) -> str:
    """执行一个 Agent 任务,返回最终结果"""
    # TODO: 调 planner 拆解任务
    # TODO: 循环调用 LLM 决定下一步动作(工具调用或给出答案)
    # TODO: 执行工具并把结果回填到上下文
    raise NotImplementedError
