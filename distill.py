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

    # Craft mode (interactive, single concept):
    python distill.py craft "Concept Name" --context "..." --idea "..."
    python distill.py craft "Concept Name" --context "..." --idea "..." --ref assets/style.png
"""

import argparse
import json
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


def save_step(content: str, step_name: str, paper_name: str) -> Path:
    """Speichere Zwischen-Output in steps/ Unterordner."""
    steps_dir = Path(config.PATHS["output"]) / "papers" / paper_name / "steps"
    steps_dir.mkdir(parents=True, exist_ok=True)

    step_path = steps_dir / f"{step_name}.md"
    step_path.write_text(content, encoding="utf-8")
    return step_path


def distill_3p(client, content, is_multimodal: bool = False, paper_name: str = None) -> str:
    """3-Perspektiven-Workflow: A (Argument), B (Konzepte), C (Implikationen) + Synthese."""

    # Stufe 0: Metadaten extrahieren
    print("  [0/4] Extrahiere Metadaten...")
    metadata = extract_metadata(client, content, is_multimodal)
    if paper_name:
        save_step(metadata, "0_metadata", paper_name)

    # Stufe 1: Drei parallele Extraktionen
    print("  [1/4] Extrahiere Argument-Struktur (Prompt A)...")
    extraction_a = distill_knowledge(client, content, "distill_3p_a", is_multimodal)
    if paper_name:
        save_step(extraction_a, "1_extraction_a_argument", paper_name)

    print("  [2/4] Extrahiere Konzept-Landschaft (Prompt B)...")
    extraction_b = distill_knowledge(client, content, "distill_3p_b", is_multimodal)
    if paper_name:
        save_step(extraction_b, "2_extraction_b_concepts", paper_name)

    print("  [3/4] Extrahiere Implikationen (Prompt C)...")
    extraction_c = distill_knowledge(client, content, "distill_3p_c", is_multimodal)
    if paper_name:
        save_step(extraction_c, "3_extraction_c_implications", paper_name)

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
    synthesis = response.text
    if paper_name:
        save_step(synthesis, "4_synthesis", paper_name)

    return synthesis


def distill_3pv(client, content, is_multimodal: bool = False, text_content: str = None, paper_name: str = None) -> str:
    """3-Perspektiven-Workflow mit Validierung: A, B, C + Synthese + Validierung + Finalisierung."""

    # Stufe 0: Metadaten extrahieren
    print("  [0/6] Extrahiere Metadaten...")
    metadata = extract_metadata(client, content, is_multimodal)
    if paper_name:
        save_step(metadata, "0_metadata", paper_name)

    # Stufe 1: Drei parallele Extraktionen
    print("  [1/6] Extrahiere Argument-Struktur (Prompt A)...")
    extraction_a = distill_knowledge(client, content, "distill_3p_a", is_multimodal)
    if paper_name:
        save_step(extraction_a, "1_extraction_a_argument", paper_name)

    print("  [2/6] Extrahiere Konzept-Landschaft (Prompt B)...")
    extraction_b = distill_knowledge(client, content, "distill_3p_b", is_multimodal)
    if paper_name:
        save_step(extraction_b, "2_extraction_b_concepts", paper_name)

    print("  [3/6] Extrahiere Implikationen (Prompt C)...")
    extraction_c = distill_knowledge(client, content, "distill_3p_c", is_multimodal)
    if paper_name:
        save_step(extraction_c, "3_extraction_c_implications", paper_name)

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
    if paper_name:
        save_step(synthesis, "4_synthesis", paper_name)

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
    if paper_name:
        save_step(validation_report, "5_validation", paper_name)

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
    final = response.text
    if paper_name:
        save_step(final, "6_final", paper_name)

    return final


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


def select_visualization_concepts(client, knowledge_document: str) -> list:
    """Waehle 1-5 Konzepte zur Visualisierung aus dem Wissensdokument."""
    prompt_template = load_prompt("visualize_select")
    prompt = prompt_template.format(knowledge_document=knowledge_document)

    response = client.models.generate_content(
        model=config.MODEL_TEXT,
        contents=[prompt]
    )

    # Parse JSON aus Response
    response_text = response.text.strip()
    # Entferne Markdown Code-Blocks falls vorhanden
    if response_text.startswith("```"):
        lines = response_text.split("\n")
        response_text = "\n".join(lines[1:-1])

    try:
        concepts = json.loads(response_text)
        return concepts[:5]  # Maximum 5
    except json.JSONDecodeError:
        print(f"Warnung: Konnte JSON nicht parsen: {response_text[:200]}...")
        return []


def generate_visualization_prompt(spec: dict) -> str:
    """Baue den Bildgenerierungs-Prompt aus der Spezifikation."""
    prompt_template = load_prompt("visualize")

    # Formatiere Relations als String
    relations = spec.get("relations", [])
    relations_str = "\n".join([f"- {r}" for r in relations]) if relations else "None specified"

    # Formatiere Negative Constraints als String
    neg_constraints = spec.get("negative_constraints", [])
    neg_str = "\n".join([f"- {c}" for c in neg_constraints]) if neg_constraints else "None"

    prompt = prompt_template.format(
        concept=spec.get("concept", ""),
        context=spec.get("context", ""),
        relations=relations_str,
        visual_type=spec.get("visual_type", "architecture"),
        structure=spec.get("structure", "parallel"),
        negative_constraints=neg_str,
        audience=spec.get("audience", "intermediate"),
        style=spec.get("style", "kurzgesagt")
    )

    return prompt


def generate_visualization_description(client, spec: dict, analysis: dict = None) -> str:
    """Generiere Begleittext fuer eine Visualisierung."""
    prompt_template = load_prompt("visualize_describe")

    prompt = prompt_template.format(
        concept=spec.get("concept", ""),
        context=spec.get("context", ""),
        function=spec.get("function", "representational"),
        structure=spec.get("structure", "linear-causal"),
        audience=spec.get("audience", "intermediate")
    )

    # Fuege Analysis-Kontext hinzu falls vorhanden
    if analysis and analysis.get("issues"):
        issues_text = "\n".join([f"- {issue}" for issue in analysis.get("issues", [])])
        prompt += f"\n\n## Critical Notes (include in caption)\nThe visualization has these known limitations:\n{issues_text}"

    response = client.models.generate_content(
        model=config.MODEL_TEXT,
        contents=[prompt]
    )

    return response.text


def analyze_visualization(client, image_data: bytes, spec: dict) -> dict:
    """Analysiere generiertes Bild und gib Verbesserungsvorschlaege."""
    prompt_template = load_prompt("visualize_analyze")

    # Formatiere Negative Constraints als String
    neg_constraints = spec.get("negative_constraints", [])
    neg_str = "\n".join([f"- {c}" for c in neg_constraints]) if neg_constraints else "None specified"

    prompt = prompt_template.format(
        image="[See attached image]",
        concept=spec.get("concept", ""),
        context=spec.get("context", ""),
        structure=spec.get("structure", "parallel"),
        negative_constraints=neg_str
    )

    # Sende Bild + Prompt
    image_part = types.Part.from_bytes(data=image_data, mime_type="image/png")

    response = client.models.generate_content(
        model=config.MODEL_TEXT,
        contents=[image_part, prompt]
    )

    # Parse JSON
    response_text = response.text.strip()
    if response_text.startswith("```"):
        lines = response_text.split("\n")
        response_text = "\n".join(lines[1:-1])

    try:
        return json.loads(response_text)
    except json.JSONDecodeError:
        print(f"    Warnung: Konnte Analysis-JSON nicht parsen")
        return {"fidelity_score": 3, "structural_match": False, "constraint_violations": [], "issues": [], "improvements": [], "keep": []}


def generate_refined_visualization_prompt(spec: dict, analysis: dict) -> str:
    """Baue Prompt fuer verbesserte Bildgenerierung mit Analysis-Feedback."""
    base_prompt = generate_visualization_prompt(spec)

    improvements = analysis.get("improvements", [])
    keep = analysis.get("keep", [])

    if improvements or keep:
        base_prompt += "\n\n## CRITICAL REQUIREMENTS"
        if keep:
            base_prompt += "\nPRESERVE these elements:\n" + "\n".join([f"- {k}" for k in keep])
        if improvements:
            base_prompt += "\nAPPLY these corrections:\n" + "\n".join([f"- {imp}" for imp in improvements])

    return base_prompt


def visualize_knowledge(client, knowledge_document: str, source_name: str, refine: bool = True) -> list:
    """Generiere Visualisierungen fuer ein Wissensdokument mit optionalem Refinement."""
    print("\nVisualisierung...")
    print("  Waehle Konzepte zur Visualisierung...")
    concepts = select_visualization_concepts(client, knowledge_document)

    if not concepts:
        print("  Keine Konzepte zur Visualisierung gefunden.")
        return []

    print(f"  {len(concepts)} Konzept(e) ausgewaehlt:")
    for i, spec in enumerate(concepts, 1):
        print(f"    {i}. {spec.get('concept', 'Unbekannt')}")

    results = []
    # Visualisierungen im Paper-Unterordner
    paper_dir = Path(config.PATHS["output"]) / "final" / source_name
    paper_dir.mkdir(parents=True, exist_ok=True)

    for i, spec in enumerate(concepts, 1):
        concept_name = spec.get("concept", f"concept_{i}")
        safe_name = concept_name.replace(" ", "_").replace("/", "-")[:50]

        print(f"\n  Konzept {i}/{len(concepts)}: {concept_name}")

        # Schritt 1: Generiere erstes Bild
        print(f"    [1/4] Generiere Bild v1...")
        image_prompt = generate_visualization_prompt(spec)
        image_data = generate_image(client, image_prompt)

        if not image_data:
            print(f"    Fehler: Kein Bild generiert")
            continue

        analysis = None

        if refine:
            # Schritt 2: Analysiere Bild
            print(f"    [2/4] Analysiere Bild...")
            analysis = analyze_visualization(client, image_data, spec)
            fidelity = analysis.get("fidelity_score", 3)
            print(f"    Fidelity Score: {fidelity}/5")

            if fidelity < 4 and analysis.get("improvements"):
                # Schritt 3: Regeneriere mit Feedback
                print(f"    [3/4] Regeneriere mit {len(analysis.get('improvements', []))} Verbesserungen...")
                refined_prompt = generate_refined_visualization_prompt(spec, analysis)
                refined_image = generate_image(client, refined_prompt)

                if refined_image:
                    image_data = refined_image
                    print(f"    Verbessertes Bild generiert")
                else:
                    print(f"    Warnung: Regenerierung fehlgeschlagen, nutze v1")
            else:
                print(f"    [3/4] Keine Verbesserung noetig (Score >= 4)")

        # Speichere finales Bild
        image_path = paper_dir / f"{safe_name}.png"
        image_path.write_bytes(image_data)
        print(f"    Bild gespeichert: {image_path}")

        # Schritt 4: Generiere Begleittext (mit Analysis-Kontext)
        print(f"    [4/4] Generiere Begleittext...")
        description = generate_visualization_description(client, spec, analysis)

        desc_path = image_path.with_suffix(".md")
        desc_path.write_text(description, encoding="utf-8")
        print(f"    Begleittext gespeichert: {desc_path}")

        results.append({
            "concept": concept_name,
            "image": str(image_path),
            "description": str(desc_path),
            "fidelity_score": analysis.get("fidelity_score") if analysis else None,
            "refined": refine and analysis and analysis.get("fidelity_score", 5) < 4
        })

    return results


def get_next_version(paper_dir: Path, prompt_name: str) -> int:
    """Ermittle nächste Versionsnummer für einen Prompt."""
    existing = list(paper_dir.glob(f"{prompt_name}_v*.md"))
    if not existing:
        return 1
    versions = [int(p.stem.split("_v")[-1]) for p in existing]
    return max(versions) + 1


def save_knowledge(content: str, source_name: str, prompt_name: str = "distill") -> Path:
    """Speichere Wissensdokument. Finale 3pv-Dokumente in Paper-Unterordner."""
    if prompt_name == "distill_3pv":
        # Finale Dokumente in output/final/<paper_name>/
        paper_dir = Path(config.PATHS["output"]) / "final" / source_name
        paper_dir.mkdir(parents=True, exist_ok=True)
        filename = f"{source_name}.md"
        output_path = paper_dir / filename
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


# ============================================================================
# CRAFT MODE - Interactive single-concept visualization
# ============================================================================

def load_image_as_part(path: Path) -> types.Part:
    """Lade Bild als Gemini-Part."""
    image_bytes = path.read_bytes()
    suffix = path.suffix.lower()
    mime_types = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".webp": "image/webp"
    }
    mime_type = mime_types.get(suffix, "image/png")
    return types.Part.from_bytes(data=image_bytes, mime_type=mime_type)


def generate_sketchpad(client, concept: str, context: str, user_idea: str,
                       reference_path: Path = None) -> str:
    """Generiere Sketchpad aus User-Input und optionalem Referenzbild."""
    prompt_template = load_prompt("craft_sketchpad")

    # Beschreibe Referenzbild falls vorhanden
    reference_description = "No reference image provided."
    if reference_path and reference_path.exists():
        reference_description = f"Reference image provided: {reference_path.name}. Analyze the visual style, color palette, and composition approach."

    prompt = prompt_template.format(
        concept=concept,
        context=context,
        user_idea=user_idea,
        reference_description=reference_description
    )

    # Sende mit oder ohne Referenzbild
    if reference_path and reference_path.exists():
        image_part = load_image_as_part(reference_path)
        contents = [image_part, prompt]
    else:
        contents = [prompt]

    response = client.models.generate_content(
        model=config.MODEL_TEXT,
        contents=contents
    )

    return response.text


def parse_sketchpad(sketchpad_content: str) -> dict:
    """Parse Sketchpad-Markdown zurueck in Spezifikation."""
    spec = {
        "concept": "",
        "context": "",
        "structure": "parallel",
        "negative_constraints": [],
        "style": "kurzgesagt",
        "generation_prompt": ""
    }

    lines = sketchpad_content.split("\n")
    current_section = None

    for line in lines:
        line_stripped = line.strip()

        # Extrahiere Konzeptname aus Titel
        if line_stripped.startswith("# Sketchpad:"):
            spec["concept"] = line_stripped.replace("# Sketchpad:", "").strip()

        # Erkenne Sektionen
        elif line_stripped.startswith("### Structure"):
            current_section = "structure"
        elif line_stripped.startswith("## Negative Constraints"):
            current_section = "negative_constraints"
        elif line_stripped.startswith("## Generation Prompt Preview"):
            current_section = "generation_prompt"
        elif line_stripped.startswith("##"):
            current_section = None

        # Parse Inhalte
        elif current_section == "structure" and line_stripped and not line_stripped.startswith("#"):
            # Erste nicht-leere Zeile nach "### Structure"
            for struct_type in ["parallel", "nested", "linear-causal", "cyclic-causal", "juxtaposition", "network"]:
                if struct_type in line_stripped.lower():
                    spec["structure"] = struct_type
                    break
            current_section = None

        elif current_section == "negative_constraints" and line_stripped.startswith("- DO NOT:"):
            constraint = line_stripped.replace("- DO NOT:", "").strip()
            spec["negative_constraints"].append(constraint)

        elif current_section == "generation_prompt":
            spec["generation_prompt"] += line + "\n"

    spec["generation_prompt"] = spec["generation_prompt"].strip()

    return spec


def save_sketchpad(content: str, concept_name: str) -> Path:
    """Speichere Sketchpad in sketches/ Ordner."""
    sketches_dir = Path(config.PATHS["output"]) / "sketches"
    sketches_dir.mkdir(parents=True, exist_ok=True)

    safe_name = concept_name.replace(" ", "_").replace("/", "-")[:50]
    sketchpad_path = sketches_dir / f"{safe_name}_sketchpad.md"
    sketchpad_path.write_text(content, encoding="utf-8")

    return sketchpad_path


def craft_visualization(client, concept: str, context: str, user_idea: str,
                        reference_path: Path = None, auto_approve: bool = False) -> dict:
    """Interaktiver Craft-Workflow fuer einzelne Konzeptvisualisierung."""

    print(f"\n{'='*60}")
    print(f"CRAFT MODE: {concept}")
    print(f"{'='*60}")

    # Schritt 1: Generiere Sketchpad
    print("\n[1/4] Generiere Sketchpad...")
    sketchpad = generate_sketchpad(client, concept, context, user_idea, reference_path)

    # Speichere Sketchpad
    sketchpad_path = save_sketchpad(sketchpad, concept)
    print(f"      Sketchpad gespeichert: {sketchpad_path}")

    # Zeige Sketchpad
    print("\n" + "-"*60)
    print(sketchpad)
    print("-"*60)

    # Schritt 2: Warte auf Freigabe
    if not auto_approve:
        print("\n[2/4] Warte auf Freigabe...")
        print("      Editiere das Sketchpad bei Bedarf: " + str(sketchpad_path))
        response = input("      Fortfahren mit Bildgenerierung? [y/n/e(dit)]: ").strip().lower()

        if response == 'n':
            print("      Abgebrochen.")
            return {"status": "cancelled", "sketchpad": str(sketchpad_path)}
        elif response == 'e':
            print(f"      Bitte editiere: {sketchpad_path}")
            input("      Druecke Enter wenn fertig...")
            # Lade editiertes Sketchpad
            sketchpad = sketchpad_path.read_text(encoding="utf-8")
    else:
        print("\n[2/4] Auto-Approve aktiviert, ueberspringe Freigabe...")

    # Schritt 3: Generiere Bild
    print("\n[3/4] Generiere Bild...")

    # Parse Sketchpad fuer Generation Prompt
    spec = parse_sketchpad(sketchpad)

    # Nutze Generation Prompt Preview aus Sketchpad, oder baue eigenen
    if spec["generation_prompt"]:
        image_prompt = spec["generation_prompt"]
    else:
        # Fallback: Baue Prompt aus Spec
        image_prompt = f"""Create a scientific visualization for: {concept}

Context: {context}

User's vision: {user_idea}

Structure: {spec['structure']}

Style: Clean, minimal, educational illustration similar to Kurzgesagt videos.

DO NOT include any text labels in the image.
"""

    # Falls Referenzbild vorhanden, haenge es an
    if reference_path and reference_path.exists():
        print("      (mit Stil-Referenz)")
        ref_part = load_image_as_part(reference_path)
        full_prompt = f"{image_prompt}\n\nIMPORTANT: Match the visual style, color palette, and aesthetic of the attached reference image."

        response = client.models.generate_content(
            model=config.MODEL_IMAGE,
            contents=[ref_part, full_prompt],
            config=types.GenerateContentConfig(
                response_modalities=["Text", "Image"],
                image_config=types.ImageConfig(
                    aspect_ratio=config.IMAGE_CONFIG["aspect_ratio"],
                    image_size=config.IMAGE_CONFIG["resolution"]
                )
            )
        )
    else:
        response = client.models.generate_content(
            model=config.MODEL_IMAGE,
            contents=[image_prompt],
            config=types.GenerateContentConfig(
                response_modalities=["Text", "Image"],
                image_config=types.ImageConfig(
                    aspect_ratio=config.IMAGE_CONFIG["aspect_ratio"],
                    image_size=config.IMAGE_CONFIG["resolution"]
                )
            )
        )

    # Extrahiere Bild
    image_data = None
    if response is None:
        print("      Fehler: Keine API-Response erhalten")
        return {"status": "error", "sketchpad": str(sketchpad_path)}

    if not hasattr(response, 'parts') or response.parts is None:
        # Versuche Fehlerdetails zu extrahieren
        error_msg = "Unbekannter Fehler"
        if hasattr(response, 'prompt_feedback'):
            error_msg = f"Prompt Feedback: {response.prompt_feedback}"
        elif hasattr(response, 'candidates') and response.candidates:
            candidate = response.candidates[0]
            if hasattr(candidate, 'finish_reason'):
                error_msg = f"Finish Reason: {candidate.finish_reason}"
            if hasattr(candidate, 'safety_ratings'):
                error_msg += f", Safety: {candidate.safety_ratings}"
        print(f"      Fehler: Keine Parts in Response - {error_msg}")
        return {"status": "error", "sketchpad": str(sketchpad_path)}

    for part in response.parts:
        if part.inline_data is not None:
            image_data = part.inline_data.data
            break

    if not image_data:
        print("      Fehler: Kein Bild generiert")
        return {"status": "error", "sketchpad": str(sketchpad_path)}

    # Speichere Bild
    craft_dir = Path(config.PATHS["output"]) / "craft"
    craft_dir.mkdir(parents=True, exist_ok=True)

    safe_name = concept.replace(" ", "_").replace("/", "-")[:50]
    image_path = craft_dir / f"{safe_name}.png"
    image_path.write_bytes(image_data)
    print(f"      Bild gespeichert: {image_path}")

    # Schritt 4: Generiere Begleittext
    print("\n[4/4] Generiere Begleittext...")

    desc_spec = {
        "concept": concept,
        "context": context,
        "function": "representational",
        "structure": spec["structure"],
        "audience": "intermediate"
    }
    description = generate_visualization_description(client, desc_spec)

    desc_path = image_path.with_suffix(".md")
    desc_path.write_text(description, encoding="utf-8")
    print(f"      Begleittext gespeichert: {desc_path}")

    print(f"\n{'='*60}")
    print("CRAFT abgeschlossen!")
    print(f"{'='*60}")

    return {
        "status": "success",
        "sketchpad": str(sketchpad_path),
        "image": str(image_path),
        "description": str(desc_path)
    }


def main():
    # Pruefe ob erstes Argument "craft" ist - dann Craft-Modus
    if len(sys.argv) > 1 and sys.argv[1] == "craft":
        # Craft-Mode Parser
        parser = argparse.ArgumentParser(description="DISTILL Craft Mode")
        parser.add_argument("command", help="craft")
        parser.add_argument("concept", type=str, help="Name des Konzepts")
        parser.add_argument("--context", type=str, required=True, help="Kontext/Beschreibung des Konzepts")
        parser.add_argument("--idea", type=str, required=True, help="Deine Visualisierungsidee")
        parser.add_argument("--ref", type=Path, help="Pfad zu Referenzbild fuer Stil")
        parser.add_argument("--auto", action="store_true", help="Automatisch freigeben ohne Nachfrage")

        args = parser.parse_args()

        print("Initialisiere Gemini Client...")
        client = init_client()

        ref_path = args.ref if args.ref else None
        auto_approve = args.auto

        result = craft_visualization(
            client=client,
            concept=args.concept,
            context=args.context,
            user_idea=args.idea,
            reference_path=ref_path,
            auto_approve=auto_approve
        )

        if result["status"] == "success":
            print(f"\nErgebnis: {result['image']}")
        return

    # Standard Distill-Modus
    parser = argparse.ArgumentParser(description="DISTILL - Wissensextraktion und Visualisierung")
    parser.add_argument("input", type=Path, help="Input-Datei (PDF, Markdown oder Text)")
    parser.add_argument("--prompt", type=str, default="distill", help="Prompt-Name (default: distill)")
    parser.add_argument("--mode", type=str, choices=["multimodal", "text"], default="multimodal",
                        help="PDF-Modus: multimodal (mit Layout/Bildern) oder text (nur extrahierter Text)")
    parser.add_argument("--visualize", action="store_true", help="Automatisch 1-5 Konzepte visualisieren")

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

    source_name = args.input.stem

    # Workflow-Auswahl
    if args.prompt == "distill_3pv":
        print("Starte 3-Perspektiven-Workflow mit Validierung (6 API-Calls)...")
        knowledge = distill_3pv(client, content, is_multimodal=is_multimodal, text_content=text_content, paper_name=source_name)
    elif args.prompt == "distill_3p":
        print("Starte 3-Perspektiven-Workflow (4 API-Calls)...")
        knowledge = distill_3p(client, content, is_multimodal=is_multimodal, paper_name=source_name)
    else:
        print(f"Destilliere Wissen mit Prompt '{args.prompt}'...")
        knowledge = distill_knowledge(client, content, args.prompt, is_multimodal=is_multimodal)
    output_path = save_knowledge(knowledge, source_name, args.prompt)
    print(f"Wissensdokument gespeichert: {output_path}")

    if args.visualize:
        # Neuer automatischer Visualisierungs-Workflow
        results = visualize_knowledge(client, knowledge, source_name)
        if results:
            print(f"\n{len(results)} Visualisierung(en) erstellt.")
        else:
            print("\nKeine Visualisierungen erstellt.")


if __name__ == "__main__":
    main()
