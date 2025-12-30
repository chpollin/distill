#!/usr/bin/env python3
"""
DISTILL - Document Intelligence for Scientific Text to Illustrated Learning Layouts

Usage:
    python distill.py data/paper.md
    python distill.py data/paper.md --visualize
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime

from google import genai
from google.genai import types

import config
from prompts import load_prompt


def init_client():
    """Initialisiere Gemini Client."""
    return genai.Client(api_key=config.GEMINI_API_KEY)


def load_text(path: Path) -> str:
    """Lade Text aus Datei."""
    return path.read_text(encoding="utf-8")


def distill_knowledge(client, text: str, prompt_name: str = "distill") -> str:
    """Destilliere Text zu Wissensdokument."""
    prompt = load_prompt(prompt_name).format(text=text)

    response = client.models.generate_content(
        model=config.MODEL_TEXT,
        contents=[prompt]
    )

    return response.text


def generate_image_prompt(client, concept: str, context: str) -> str:
    """Generiere Bildprompt aus Konzept."""
    prompt = load_prompt("image_prompt").format(concept=concept, context=context)

    response = client.models.generate_content(
        model=config.MODEL_TEXT,
        contents=[prompt]
    )

    return response.text


def generate_image(client, prompt: str) -> bytes:
    """Generiere Bild via Gemini API."""
    response = client.models.generate_content(
        model=config.MODEL_IMAGE,
        contents=[prompt],
        config=types.GenerateContentConfig(
            response_modalities=["Text", "Image"],
            image_config=types.ImageConfig(
                aspect_ratio=config.IMAGE_CONFIG["aspect_ratio"],
                image_size=config.IMAGE_CONFIG["resolution"]
            )
        )
    )

    for part in response.parts:
        if part.inline_data is not None:
            return part.inline_data.data

    return None


def generate_description(client, concept: str, context: str) -> str:
    """Generiere Begleittext."""
    prompt = load_prompt("description").format(concept=concept, context=context)

    response = client.models.generate_content(
        model=config.MODEL_TEXT,
        contents=[prompt]
    )

    return response.text


def get_next_version(paper_dir: Path, prompt_name: str) -> int:
    """Ermittle nächste Versionsnummer für einen Prompt."""
    existing = list(paper_dir.glob(f"{prompt_name}_v*.md"))
    if not existing:
        return 1
    versions = [int(p.stem.split("_v")[-1]) for p in existing]
    return max(versions) + 1


def save_knowledge(content: str, source_name: str, prompt_name: str = "distill") -> Path:
    """Speichere Wissensdokument in Paper-Unterordner."""
    paper_dir = Path(config.PATHS["knowledge"]) / "papers" / source_name
    paper_dir.mkdir(parents=True, exist_ok=True)

    version = get_next_version(paper_dir, prompt_name)
    filename = f"{prompt_name}_v{version}.md"
    output_path = paper_dir / filename

    output_path.write_text(content, encoding="utf-8")
    return output_path


def save_image(image_data: bytes, name: str) -> Path:
    """Speichere Bild."""
    output_dir = Path(config.PATHS["output"])
    output_dir.mkdir(exist_ok=True)

    output_path = output_dir / f"{name}.png"
    output_path.write_bytes(image_data)
    return output_path


def main():
    parser = argparse.ArgumentParser(description="DISTILL - Wissensextraktion und Visualisierung")
    parser.add_argument("input", type=Path, help="Input-Datei (Markdown oder Text)")
    parser.add_argument("--prompt", type=str, default="distill", help="Prompt-Name (default: distill)")
    parser.add_argument("--visualize", action="store_true", help="Auch Visualisierung generieren")
    parser.add_argument("--concept", type=str, help="Spezifisches Konzept visualisieren")

    args = parser.parse_args()

    if not args.input.exists():
        print(f"Fehler: {args.input} nicht gefunden")
        sys.exit(1)

    print(f"Lade: {args.input}")
    text = load_text(args.input)

    print("Initialisiere Gemini Client...")
    client = init_client()

    print(f"Destilliere Wissen mit Prompt '{args.prompt}'...")
    knowledge = distill_knowledge(client, text, args.prompt)

    source_name = args.input.stem
    output_path = save_knowledge(knowledge, source_name, args.prompt)
    print(f"Wissensdokument gespeichert: {output_path}")

    if args.visualize:
        concept = args.concept or input("Welches Konzept visualisieren? ")

        print("Generiere Bildprompt...")
        image_prompt = generate_image_prompt(client, concept, knowledge)
        print(f"Prompt: {image_prompt[:200]}...")

        print("Generiere Bild...")
        image_data = generate_image(client, image_prompt)

        if image_data:
            image_path = save_image(image_data, f"{source_name}_{concept.replace(' ', '_')}")
            print(f"Bild gespeichert: {image_path}")

            print("Generiere Begleittext...")
            description = generate_description(client, concept, knowledge)

            desc_path = image_path.with_suffix(".md")
            desc_path.write_text(description, encoding="utf-8")
            print(f"Begleittext gespeichert: {desc_path}")
        else:
            print("Fehler: Kein Bild generiert")


if __name__ == "__main__":
    main()
