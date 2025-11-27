from pathlib import Path
from typing import Any, Dict
import jinja2


def load_template(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"テンプレートが見つかりません: {path}")
    return path.read_text(encoding="utf-8")


def render_template(template_text: str, context: Dict[str, Any]) -> str:
    env = jinja2.Environment(autoescape=False)
    template = env.from_string(template_text)
    return template.render(**context)


def load_and_render(path: Path, context: Dict[str, Any]) -> str:
    return render_template(load_template(path), context)
