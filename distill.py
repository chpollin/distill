#!/usr/bin/env python3
"""
DISTILL - Document Intelligence for Scientific Text to Illustrated Learning Layouts

Usage:
    python distill.py data/paper.pdf                    # PDF multimodal (default)
    python distill.py data/paper.pdf --mode text       # PDF mit Textextraktion
    python distill.py data/paper.pdf --mode multimodal # PDF multimodal (explizit)
    python distill.py data/paper.md                     # Markdown/Text
    python distill.py data/paper.pdf --visualize       # Mit Visualisierung
    python distill.py data/paper.pdf --prompt distill_3p   # 3-Perspektiven-Workflow
    python distill.py data/paper.pdf --prompt distill_3pv  # 3P + Validierung (beste Qualitaet)
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime

import fitz  # PyMuPDF
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


def load_pdf_multimodal(path: Path) -> types.Part:
    """Lade PDF als Gemini-Part (multimodal)."""
    pdf_bytes = path.read_bytes()
    return types.Part.from_bytes(data=pdf_bytes, mime_type="application/pdf")


def extract_pdf_text(path: Path) -> str:
    """Extrahiere Text aus PDF via PyMuPDF."""
    doc = fitz.open(path)
    text_parts = []
    for page in doc:
        text_parts.append(page.get_text())
    doc.close()
    return "\n\n".join(text_parts)


def distill_knowledge(client, content, prompt_name: str = "distill", is_multimodal: bool = False) -> str:
    """Destilliere Text oder PDF zu Wissensdokument."""
    prompt_template = load_prompt(prompt_name)

    if is_multimodal:
        # Multimodal: PDF als separater Part
        prompt_text = prompt_template.replace("{text}", "[See attached PDF]")
        contents = [content, prompt_text]
    else:
        # Text: Prompt mit eingebettetem Text
        prompt_text = prompt_template.format(text=content)
        contents = [prompt_text]

    response = client.models.generate_content(
        model=config.MODEL_TEXT,
        contents=contents
    )

    return response.text


def extract_metadata(client, content, is_multimodal: bool = False) -> str:
    """Extrahiere Metadaten (Titel, Autoren, Jahr) aus dem Paper."""
    metadata_prompt = """Extract the following metadata from this scientific paper:
- Title: [exact full title]
- Authors: [all authors, or "First Author et al." if more than 3]
- Year: [publication year]

Return ONLY these three lines, nothing else."""

    if is_multimodal:
        contents = [content, metadata_prompt]
    else:
        contents = [f"{metadata_prompt}\n\n{content[:5000]}"]  # First 5000 chars for metadata

    response = client.models.generate_content(
        model=config.MODEL_TEXT,
        contents=contents
    )
    return response.text


def distill_3p(client, content, is_multimodal: bool = False) -> str:
    """3-Perspektiven-Workflow: A (Argument), B (Konzepte), C (Implikationen) + Synthese."""

    # Stufe 0: Metadaten extrahieren
    print("  [0/4] Extrahiere Metadaten...")
    metadata = extract_metadata(client, content, is_multimodal)

    # Stufe 1: Drei parallele Extraktionen
    print("  [1/4] Extrahiere Argument-Struktur (Prompt A)...")
    extraction_a = distill_knowledge(client, content, "distill_3p_a", is_multimodal)

    print("  [2/4] Extrahiere Konzept-Landschaft (Prompt B)...")
    extraction_b = distill_knowledge(client, content, "distill_3p_b", is_multimodal)

    print("  [3/4] Extrahiere Implikationen (Prompt C)...")
    extraction_c = distill_knowledge(client, content, "distill_3p_c", is_multimodal)

    # Stufe 2: Synthese
    print("  [4/4] Synthese der drei Perspektiven...")
    synth_template = load_prompt("distill_3p_synth")
    synth_prompt = synth_template.format(
        metadata=metadata,
        extraction_a=extraction_a,
        extraction_b=extraction_b,
        extraction_c=extraction_c
    )

    response = client.models.generate_content(
        model=config.MODEL_TEXT,
        contents=[synth_prompt]
    )

    return response.text


def distill_3pv(client, content, is_multimodal: bool = False, text_content: str = None) -> str:
    """3-Perspektiven-Workflow mit Validierung: A, B, C + Synthese + Validierung + Finalisierung."""

    # Stufe 0: Metadaten extrahieren
    print("  [0/6] Extrahiere Metadaten...")
    metadata = extract_metadata(client, content, is_multimodal)

    # Stufe 1: Drei parallele Extraktionen
    print("  [1/6] Extrahiere Argument-Struktur (Prompt A)...")
    extraction_a = distill_knowledge(client, content, "distill_3p_a", is_multimodal)

    print("  [2/6] Extrahiere Konzept-Landschaft (Prompt B)...")
    extraction_b = distill_knowledge(client, content, "distill_3p_b", is_multimodal)

    print("  [3/6] Extrahiere Implikationen (Prompt C)...")
    extraction_c = distill_knowledge(client, content, "distill_3p_c", is_multimodal)

    # Stufe 2: Synthese
    print("  [4/6] Synthese der drei Perspektiven...")
    synth_template = load_prompt("distill_3p_synth")
    synth_prompt = synth_template.format(
        metadata=metadata,
        extraction_a=extraction_a,
        extraction_b=extraction_b,
        extraction_c=extraction_c
    )

    response = client.models.generate_content(
        model=config.MODEL_TEXT,
        contents=[synth_prompt]
    )
    synthesis = response.text

    # Stufe 3: Validierung gegen Quelltext
    print("  [5/6] Validiere gegen Quelltext...")
    validate_template = load_prompt("distill_3p_validate")

    # Fuer Validierung brauchen wir Text, nicht PDF-Bytes
    source_text = text_content if text_content else "[Source text not available for validation]"

    validate_prompt = validate_template.format(
        synthesis=synthesis,
        source=source_text[:30000]  # Limit to 30k chars
    )

    response = client.models.generate_content(
        model=config.MODEL_TEXT,
        contents=[validate_prompt]
    )
    validation_report = response.text

    # Stufe 4: Finalisierung
    print("  [6/6] Finalisiere mit Korrekturen...")
    finalize_template = load_prompt("distill_3p_finalize")
    finalize_prompt = finalize_template.format(
        synthesis=synthesis,
        validation=validation_report
    )

    response = client.models.generate_content(
        model=config.MODEL_TEXT,
        contents=[finalize_prompt]
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
    """Speichere Wissensdokument. Finale 3pv-Dokumente in separatem Ordner."""
    if prompt_name == "distill_3pv":
        # Finale Dokumente direkt in output/final/
        final_dir = Path(config.PATHS["output"]) / "final"
        final_dir.mkdir(parents=True, exist_ok=True)
        filename = f"{source_name}.md"
        output_path = final_dir / filename
    else:
        # Andere Varianten in Paper-Unterordner mit Versionierung
        paper_dir = Path(config.PATHS["output"]) / "papers" / source_name
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
    parser.add_argument("input", type=Path, help="Input-Datei (PDF, Markdown oder Text)")
    parser.add_argument("--prompt", type=str, default="distill", help="Prompt-Name (default: distill)")
    parser.add_argument("--mode", type=str, choices=["multimodal", "text"], default="multimodal",
                        help="PDF-Modus: multimodal (mit Layout/Bildern) oder text (nur extrahierter Text)")
    parser.add_argument("--visualize", action="store_true", help="Auch Visualisierung generieren")
    parser.add_argument("--concept", type=str, help="Spezifisches Konzept visualisieren")

    args = parser.parse_args()

    if not args.input.exists():
        print(f"Fehler: {args.input} nicht gefunden")
        sys.exit(1)

    is_pdf = args.input.suffix.lower() == ".pdf"
    is_multimodal = is_pdf and args.mode == "multimodal"

    # Lade Content
    text_content = None  # Fuer Validierung bei 3pv
    if is_pdf:
        if args.mode == "multimodal":
            print(f"Lade: {args.input} (PDF multimodal)")
            content = load_pdf_multimodal(args.input)
            # Fuer 3pv brauchen wir auch den Text fuer Validierung
            if args.prompt == "distill_3pv":
                text_content = extract_pdf_text(args.input)
        else:
            print(f"Lade: {args.input} (PDF -> Textextraktion)")
            content = extract_pdf_text(args.input)
            text_content = content
            print(f"Extrahiert: {len(content)} Zeichen")
    else:
        print(f"Lade: {args.input} (Text)")
        content = load_text(args.input)
        text_content = content

    print("Initialisiere Gemini Client...")
    client = init_client()

    # Workflow-Auswahl
    if args.prompt == "distill_3pv":
        print("Starte 3-Perspektiven-Workflow mit Validierung (6 API-Calls)...")
        knowledge = distill_3pv(client, content, is_multimodal=is_multimodal, text_content=text_content)
    elif args.prompt == "distill_3p":
        print("Starte 3-Perspektiven-Workflow (4 API-Calls)...")
        knowledge = distill_3p(client, content, is_multimodal=is_multimodal)
    else:
        print(f"Destilliere Wissen mit Prompt '{args.prompt}'...")
        knowledge = distill_knowledge(client, content, args.prompt, is_multimodal=is_multimodal)

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
