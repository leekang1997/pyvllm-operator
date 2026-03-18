from typing import Iterable, Optional

from openai import OpenAI

from .config import VLLMConfig


class OpenAICompatClient:
    def __init__(self, config: VLLMConfig):
        self.config = config
        self._client = OpenAI(base_url=config.base_url, api_key=config.api_key)

    def chat(
        self,
        prompt: str,
        *,
        history: Optional[Iterable[str]] = None,
        model: Optional[str] = None,
        temperature: float = 0.0,
    ) -> str:
        messages = [{"role": "user", "content": message} for message in (history or [])]
        messages.append({"role": "user", "content": prompt})
        response = self._client.chat.completions.create(
            model=model or self.config.served_model_name,
            messages=messages,
            temperature=temperature,
        )
        return response.choices[0].message.content or ""
