import json
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional


@dataclass
class TokenUsage:
    input_tokens: int
    output_tokens: int
    total_tokens: int


class TokenTracker:
    _instance = None
    _log_path: Optional[Path] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TokenTracker, cls).__new__(cls)
        return cls._instance

    @classmethod
    def initialize(cls, log_path: Path):
        """
        Initialize the global TokenTracker with a log file path.
        """
        cls._log_path = log_path
        # Create directory if it doesn't exist (though cli.py should handle this)
        if hasattr(log_path, "parent"):
            log_path.parent.mkdir(parents=True, exist_ok=True)

    @classmethod
    def track(
        cls,
        pipeline: str,
        step: str,
        model: str,
        usage: TokenUsage,
    ):
        """
        Log token usage to the configured JSONL file.
        """
        if cls._log_path is None:
            # If not initialized, maybe print a warning or just ignore (or print to stdout)
            # For now, let's just ignore to allow running scripts without tracking if needed
            return

        record = {
            "timestamp": datetime.now().isoformat(),
            "pipeline": pipeline,
            "step": step,
            "model": model,
            "input_tokens": usage.input_tokens,
            "output_tokens": usage.output_tokens,
            "total_tokens": usage.total_tokens,
        }

        try:
            with open(cls._log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
        except Exception as e:
            print(f"[Warning] Failed to log token usage: {e}", flush=True)

    @classmethod
    def get_summary(cls, log_path: Optional[Path] = None) -> Dict[str, Dict[str, any]]:
        """
        Aggregate token usage from the log file.
        Returns a dict keyed by 'pipeline / step', with aggregated counts, model, and cost.
        
        Cost is calculated per-call (each log entry) to correctly apply tiered pricing.
        """
        from .pricing import calculate_call_cost
        
        target_path = log_path or cls._log_path
        if target_path is None or not target_path.exists():
            return {}

        summary = {}
        try:
            with open(target_path, "r", encoding="utf-8") as f:
                for line in f:
                    if not line.strip():
                        continue
                    data = json.loads(line)
                    
                    key = f"{data.get('pipeline', 'unknown')} / {data.get('step', 'unknown')}"
                    model = data.get("model", "unknown")
                    input_tokens = data.get("input_tokens", 0)
                    output_tokens = data.get("output_tokens", 0)
                    
                    # Calculate cost for this single call
                    call_cost = calculate_call_cost(model, input_tokens, output_tokens)
                    
                    if key not in summary:
                        summary[key] = {
                            "input_tokens": 0,
                            "output_tokens": 0,
                            "total_tokens": 0,
                            "cost": 0.0,
                            "model": model,
                        }
                    
                    summary[key]["input_tokens"] += input_tokens
                    summary[key]["output_tokens"] += output_tokens
                    summary[key]["total_tokens"] += input_tokens + output_tokens
                    summary[key]["cost"] += call_cost
                    # Keep last seen model for this step (usually same for all calls in a step)
                    summary[key]["model"] = model
                    
        except Exception as e:
            print(f"[Warning] Failed to read token logs from {target_path}: {e}", flush=True)
            return {}

        return summary
