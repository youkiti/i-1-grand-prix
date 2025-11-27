import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict


def create_run_dir(base: Path) -> Path:
    now = datetime.now()
    day_dir = base / now.strftime("%Y-%m-%d")
    run_dir = day_dir / f"run-{now.strftime('%H%M%S')}"
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "prompts").mkdir(exist_ok=True)
    (run_dir / "outputs").mkdir(exist_ok=True)
    return run_dir


def save_json(path: Path, payload: Dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def save_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")
