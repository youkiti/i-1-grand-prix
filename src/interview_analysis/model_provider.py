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
            config={
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
        try:
            completion = self.client.chat.completions.create(
                model=config.model,
                temperature=config.temperature,
                max_tokens=config.max_output_tokens,
                top_p=config.top_p,
                messages=[
                    {"role": "user", "content": prompt}
                ],
            )
            if not completion or not completion.choices:
                print(f"[Error] Invalid completion response: {completion}", flush=True)
                return ""
            
            return completion.choices[0].message.content or ""
        except Exception as e:
            print(f"[Error] OpenRouter API call failed: {e}", flush=True)
            return ""


def create_provider(model_name: str, api_key: Optional[str] = None) -> ModelProvider:
    """
    モデル名から適切なプロバイダーを作成

    プレフィックスでプロバイダーを指定:
      - gemini:model_name → Gemini (例: gemini:gemini-2.0-flash-lite)
      - openrouter:model_name → OpenRouter (例: openrouter:x-ai/grok-4.1-fast:free)
      - プレフィックスなし → Gemini (後方互換性)

    Args:
        model_name: モデル名
        api_key: APIキー（省略時は環境変数から取得）

    Returns:
        ModelProvider インスタンス
    """
    # プレフィックスで判定
    if model_name.startswith("openrouter:"):
        # OpenRouter
        actual_model = model_name[len("openrouter:"):]
        key = api_key or os.environ.get("OPENROUTER_API_KEY")
        if not key:
            raise ValueError("OPENROUTER_API_KEY が設定されていません")
        # 実際のモデル名を設定するためにModelConfigを返す前にmodel_nameを書き換える
        return OpenRouterProvider(key), actual_model
    else:
        # Gemini (gemini: プレフィックスあり or なし)
        actual_model = model_name[len("gemini:"):] if model_name.startswith("gemini:") else model_name
        key = api_key or os.environ.get("GOOGLE_API_KEY")
        if not key:
            raise ValueError("GOOGLE_API_KEY が設定されていません")
        return GeminiProvider(key), actual_model
