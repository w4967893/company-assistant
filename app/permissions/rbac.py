"""RBAC 校验逻辑"""


def has_permission(user_roles: list[str], required: str) -> bool:
    """判断角色集合是否拥有某个权限点"""
    # TODO: 角色继承、权限点定义(如 rag:upload / agent:run)
    raise NotImplementedError
