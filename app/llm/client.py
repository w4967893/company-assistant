"""统一的大模型调用入口"""

from openai import OpenAI

from app.core.config import get_settings

_settings = get_settings()

_client = OpenAI(
    api_key=_settings.deepseek_api_key,
    base_url=_settings.llm_base_url,
)


def call_mml(messages: list, model: str | None = None, **kwargs) -> str:
    """调用 DeepSeek 大模型进行一轮对话

    messages 为 OpenAI 格式 [{"role": ..., "content": ...}, ...];
    kwargs 可透传 temperature 等参数。
    """
    response = _client.chat.completions.create(
        model=model or _settings.llm_model,
        messages=messages,
        **kwargs,
    )
    return response.choices[0].message.content
