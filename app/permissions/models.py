"""用户 / 角色 / 权限数据模型"""

from dataclasses import dataclass, field


@dataclass
class User:
    id: int
    name: str
    roles: list[str] = field(default_factory=list)


@dataclass
class Role:
    name: str
    permissions: list[str] = field(default_factory=list)
