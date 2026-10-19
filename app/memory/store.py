"""存储抽象:先用内存 dict,后续可换 Redis / 数据库"""

_sessions: dict[str, list[dict]] = {}
