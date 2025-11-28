"""
モデルプロバイダーの抽象化レイヤー

Gemini と OpenRouter (Grok) を統一インターフェースで扱う。
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional
import os

from google import genai
from openai import OpenAI


@dataclass
class ModelConfig:
    """モデル呼び出しの設定"""
    model: str
    temperature: float = 0.3
    max_output_tokens: int = 64000
    top_p: float = 0.95
    top_k: int = 40


class ModelProvider(ABC):
    """モデルプロバイダーの基底クラス"""

    @abstractmethod
    def generate(self, prompt: str, config: ModelConfig) -> str:
        """プロンプトに対する応答を生成"""
        pass


class GeminiProvider(ModelProvider):
    """Google Gemini プロバイダー (google-genai)"""

    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)

    def generate(self, prompt: str, config: ModelConfig) -> str:
        response = self.client.models.generate_content(
            model=config.model,
            contents=prompt,
            generation_config={
                "temperature": config.temperature,
                "max_output_tokens": config.max_output_tokens,
                "top_p": config.top_p,
                "top_k": config.top_k,
            },
        )
        return response.text


class OpenRouterProvider(ModelProvider):
    """OpenRouter プロバイダー (Grok など)"""

    def __init__(self, api_key: str):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
        )

    def generate(self, prompt: str, config: ModelConfig) -> str:
        completion = self.client.chat.completions.create(
            model=config.model,
            temperature=config.temperature,
            max_tokens=config.max_output_tokens,
            top_p=config.top_p,
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
        return completion.choices[0].message.content


def create_provider(model_name: str, api_key: Optional[str] = None) -> ModelProvider:
    """
    モデル名から適切なプロバイダーを作成

    Args:
        model_name: モデル名 (例: "gemini-flash-lite-latest", "x-ai/grok-4.1-fast:free")
        api_key: APIキー（省略時は環境変数から取得）

    Returns:
        ModelProvider インスタンス
    """
    # OpenRouter のモデル名には "/" が含まれる
    if "/" in model_name:
        key = api_key or os.environ.get("OPENROUTER_API_KEY")
        if not key:
            raise ValueError("OPENROUTER_API_KEY が設定されていません")
        return OpenRouterProvider(key)
    else:
        # Gemini
        key = api_key or os.environ.get("GOOGLE_API_KEY")
        if not key:
            raise ValueError("GOOGLE_API_KEY が設定されていません")
        return GeminiProvider(key)
