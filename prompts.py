from pathlib import Path

PROMPTS_DIR = Path(__file__).parent / "prompts"


def load_prompt(name: str) -> str:
    """Lade Prompt aus Markdown-Datei."""
    return (PROMPTS_DIR / f"{name}.md").read_text(encoding="utf-8")
