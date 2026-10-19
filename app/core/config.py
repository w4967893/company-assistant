"""全局配置:从 .env 读取"""

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # api/


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env", env_file_encoding="utf-8"
    )

    app_name: str = "公司 AI 助手"
    debug: bool = False

    # 大模型(字段名对应 .env 里的 DEEPSEEK_API_KEY)
    deepseek_api_key: str = ""
    llm_base_url: str = "https://api.deepseek.com"
    llm_model: str = "deepseek-chat"

    # TODO: RAG 向量库、Memory 存储、权限等配置按需补充


@lru_cache
def get_settings() -> Settings:
    return Settings()
