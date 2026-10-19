"""Agent 工具注册表

每个工具一个文件,统一提供 name / description / execute;
TODO: 实现 Tool 基类与注册、发现机制
"""

TOOLS: dict = {}
