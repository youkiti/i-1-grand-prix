"""
Gemini API pricing configuration and cost calculation.
"""
from typing import Dict, Any, Union

# Model pricing in USD per 1M tokens
MODEL_PRICING: Dict[str, Dict[str, Any]] = {
    "gemini-3-pro-preview": {
        "input_per_1m": {"default": 2.00, "over_200k": 4.00},
        "output_per_1m": {"default": 12.00, "over_200k": 18.00},
    },
    "gemini-3-flash-preview": {
        "input_per_1m": 0.50,
        "output_per_1m": 3.00,  # 思考トークン含む
    },
    "gemini-2.5-flash": {
        "input_per_1m": 0.30,
        "output_per_1m": 2.50,
    },
    "gemini-2.5-flash-lite": {
        "input_per_1m": 0.10,
        "output_per_1m": 0.40,
    },
}

# Model name aliases (latest -> versioned)
MODEL_ALIASES: Dict[str, str] = {
    "gemini-flash-latest": "gemini-2.5-flash",
    "gemini-flash-lite-latest": "gemini-2.5-flash-lite",
}


def _get_rate(rate_config: Union[float, Dict[str, float]], tokens: int, threshold: int = 200_000) -> float:
    """Get the applicable rate based on token count."""
    if isinstance(rate_config, dict):
        return rate_config["over_200k"] if tokens > threshold else rate_config["default"]
    return rate_config


def calculate_call_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    """
    Calculate cost for a SINGLE API call.
    
    Tiered pricing (Gemini 3 Pro) is evaluated per-call, not on aggregated totals.
    Input and output thresholds are checked independently.
    """
    resolved_model = MODEL_ALIASES.get(model, model)
    pricing = MODEL_PRICING.get(resolved_model, MODEL_PRICING["gemini-2.5-flash-lite"])
    
    input_rate = _get_rate(pricing["input_per_1m"], input_tokens)
    output_rate = _get_rate(pricing["output_per_1m"], output_tokens)
    
    input_cost = (input_tokens / 1_000_000) * input_rate
    output_cost = (output_tokens / 1_000_000) * output_rate
    
    return input_cost + output_cost
