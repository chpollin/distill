#!/usr/bin/env python3
"""
Generiere Visualisierungen für Webentwicklungs-Skriptum.

Verwendet die revidierten Strukturtypen:
1. HTML: decomposition (vereinfacht)
2. CSS: contrast (vorher/nachher)
3. JavaScript: sequence (Event-Kette)
"""

import json
import os
from pathlib import Path
from dotenv import load_dotenv

# Lade .env BEVOR andere Module
load_dotenv()

from google import genai
from google.genai import types

# Output-Verzeichnis
OUTPUT_DIR = Path("output/webdev-intro-beginner")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# API Key und Modelle direkt aus Umgebung
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_IMAGE = "gemini-3-pro-image-preview"


def init_client():
    """Initialisiere Gemini Client."""
    return genai.Client(api_key=GEMINI_API_KEY)


def generate_image(client, prompt: str) -> bytes:
    """Generiere Bild via Gemini API."""
    response = client.models.generate_content(
        model=MODEL_IMAGE,
        contents=[prompt],
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
            image_config=types.ImageConfig(
                aspect_ratio="16:9",
                image_size="2K"  # Großes K erforderlich!
            )
        )
    )

    if response is None or not hasattr(response, 'parts') or response.parts is None:
        return None

    for part in response.parts:
        if part.inline_data is not None:
            return part.inline_data.data

    return None


# ============================================================================
# FOLIE 1: HTML - Decomposition (Teil-Ganzes)
# ============================================================================

PROMPT_HTML = """A flat design diagram showing HTML document structure as nested containers, demonstrating part-whole relationships.

COMPOSITION:
- One large outer rounded rectangle in soft blue, representing the <html> document container
- Inside it, TWO distinct sections side by side:
  - LEFT: A smaller compact square in muted teal (representing <head>) - takes about 20% width
  - RIGHT: A larger rectangle in warm coral (representing <body>) - takes about 75% width

- Inside the BODY rectangle, THREE horizontal sections stacked vertically:
  - TOP: A thin horizontal bar in light amber (header area)
  - MIDDLE: A large rectangular area in sage green (main content area) - this is the largest
  - BOTTOM: A thin horizontal bar in dusty rose (footer area)

VISUAL STYLE:
- Modern flat design with solid muted colors
- No gradients, no shadows, no 3D effects
- Clear visual hierarchy through size and nesting
- Thin white gaps between nested elements to show containment
- Clean rounded corners on all rectangles

CRITICAL CONSTRAINTS:
- Absolutely NO text, no labels, no HTML tags, no code
- No icons inside the rectangles
- Only 3 levels of nesting: html > head+body > header+main+footer
- The nesting must be visually obvious through containment
- Pure white background
- 16:9 aspect ratio
"""

CAPTION_HTML = """## HTML: Die Struktur einer Webseite

**Was das Bild zeigt:** Ein HTML-Dokument ist wie eine Schachtel, die andere Schachteln enthält. Die äußerste Schachtel ist das `<html>`-Element – alles andere liegt darin.

**Die zwei Hauptbereiche:**
- **Head** (kleiner Bereich): Enthält unsichtbare Informationen für den Browser – Titel, Metadaten, verlinkte Dateien
- **Body** (großer Bereich): Alles, was der Nutzer sieht

**Im Body:** Drei logische Abschnitte strukturieren den Inhalt:
- **Header:** Logo, Navigation, Einleitung
- **Main:** Der eigentliche Inhalt der Seite
- **Footer:** Impressum, Links, Copyright

**Das Prinzip:** HTML ist Verschachtelung. Elemente enthalten andere Elemente. Diese Hierarchie bestimmt, wie Browser und Screenreader die Seite verstehen.
"""


# ============================================================================
# FOLIE 2: CSS - Contrast (Vorher/Nachher)
# ============================================================================

PROMPT_CSS = """A flat design visualization showing rhetorical contrast between unstyled and styled content, divided into two zones.

COMPOSITION:
The image is divided vertically into two equal halves by a thin light gray line in the center.

LEFT ZONE (Unstyled):
- 4 simple rectangles stacked vertically with equal spacing
- All rectangles are the SAME dull gray color (#9CA3AF)
- All rectangles have the SAME height and width
- Sharp corners, no visual hierarchy
- Boring, monotonous, undifferentiated
- Represents raw HTML without CSS

RIGHT ZONE (Styled):
- The SAME 4 rectangles, but now transformed:
- Rectangle 1: Large, deep purple with rounded corners
- Rectangle 2: Medium, warm coral with slight rounded corners
- Rectangle 3: Wide but short, teal with pill-shaped ends
- Rectangle 4: Small, golden amber, positioned to the right
- VARIED sizes, colors, spacing, and corner radii
- Clear visual hierarchy and rhythm
- Represents HTML with CSS applied

VISUAL STYLE:
- Strictly flat 2D design
- No gradients, no shadows, no 3D effects
- Clean vector-like rendering
- Muted but distinct color palette on the right side

CRITICAL CONSTRAINTS:
- Absolutely NO text, no labels, no CSS code, no curly braces
- The LEFT side must look boring and uniform
- The RIGHT side must look designed and intentional
- Same number of elements on both sides (4 rectangles)
- Pure white background
- 16:9 aspect ratio
"""

CAPTION_CSS = """## CSS: Vom Rohtext zum Design

**Was das Bild zeigt:** Links sehen Sie HTML ohne Styling – vier identische graue Blöcke. Rechts dieselben Elemente mit CSS – plötzlich entsteht visuelle Hierarchie.

**Was CSS verändert:**
- **Farbe:** Jedes Element bekommt eine eigene Identität
- **Größe:** Wichtiges wird größer, Nebensächliches kleiner
- **Abstände:** Weißraum schafft Struktur und Lesbarkeit
- **Form:** Rundungen machen Elemente freundlicher

**Das Prinzip:** CSS trennt Inhalt von Darstellung. Das HTML bleibt gleich – nur das Stylesheet ändert sich. Das ermöglicht:
- Schnelle Design-Änderungen ohne HTML-Anpassung
- Unterschiedliche Styles für verschiedene Geräte
- Konsistentes Aussehen über viele Seiten hinweg

**Merksatz:** HTML sagt *was*, CSS sagt *wie*.
"""


# ============================================================================
# FOLIE 3: JavaScript - Sequence (Event-Kette)
# ============================================================================

PROMPT_JS = """A flat design diagram showing a 4-step event sequence for JavaScript interaction, arranged horizontally.

COMPOSITION:
Four circular icons arranged in a horizontal line from left to right, connected by thin gray arrows between them. Equal spacing between all elements.

STEP 1 (leftmost):
- A simple hand/cursor icon in muted coral
- Represents: User action (click, type, scroll)

STEP 2:
- A lightning bolt or spark icon in warm amber
- Represents: Event fires (the browser notices the action)

STEP 3:
- A gear/cog icon in teal
- Represents: Code executes (JavaScript runs)

STEP 4 (rightmost):
- A rectangle with a small change indicator (like a checkmark or highlight) in sage green
- Represents: Page updates (DOM changes, visible result)

ARROWS:
- Thin gray arrows pointing RIGHT between each step
- Arrows should be simple, single-headed
- Show clear left-to-right flow

VISUAL STYLE:
- Icons should be simple, geometric, flat design
- Each icon in a subtle circular background or container
- Muted, professional color palette
- Clean, minimal, no decorative elements

CRITICAL CONSTRAINTS:
- Absolutely NO text, no labels, no code
- Exactly 4 steps, no more, no fewer
- Clear left-to-right reading direction
- No loops or branches - pure linear sequence
- Pure white background
- 16:9 aspect ratio
"""

CAPTION_JS = """## JavaScript: Von Klick zu Reaktion

**Was das Bild zeigt:** Vier Schritte einer Interaktion – von der Benutzeraktion bis zur sichtbaren Änderung auf der Seite.

**Die Event-Kette:**
1. **User-Aktion:** Der Nutzer klickt, tippt oder scrollt
2. **Event feuert:** Der Browser erkennt die Aktion und erzeugt ein "Event"
3. **Code läuft:** JavaScript-Funktionen reagieren auf das Event
4. **Seite ändert sich:** Das DOM wird aktualisiert – der Nutzer sieht das Ergebnis

**Das Prinzip:** JavaScript macht Webseiten *reaktiv*. Ohne JavaScript ist eine Seite statisch – sie zeigt nur, was im HTML steht. Mit JavaScript kann die Seite auf Eingaben reagieren, Daten laden, Animationen abspielen.

**Beispiel:** Nutzer klickt "Absenden" → Event `click` feuert → JavaScript prüft das Formular → Bei Fehler erscheint eine Meldung, bei Erfolg werden Daten gesendet.

**Merksatz:** JavaScript ist der Vermittler zwischen Nutzer und Seite.
"""


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("=" * 60)
    print("DISTILL: Webentwicklungs-Folien generieren")
    print("=" * 60)

    client = init_client()

    slides = [
        {
            "name": "01_html_structure",
            "title": "HTML: Dokumentstruktur",
            "prompt": PROMPT_HTML,
            "caption": CAPTION_HTML,
            "structure_type": "decomposition"
        },
        {
            "name": "02_css_styling",
            "title": "CSS: Vorher/Nachher",
            "prompt": PROMPT_CSS,
            "caption": CAPTION_CSS,
            "structure_type": "contrast"
        },
        {
            "name": "03_javascript_events",
            "title": "JavaScript: Event-Kette",
            "prompt": PROMPT_JS,
            "caption": CAPTION_JS,
            "structure_type": "sequence"
        }
    ]

    results = []

    for i, slide in enumerate(slides, 1):
        print(f"\n[{i}/3] {slide['title']}")
        print(f"      Strukturtyp: {slide['structure_type']}")
        print(f"      Generiere Bild...")

        image_data = generate_image(client, slide["prompt"])

        if image_data:
            # Speichere Bild
            image_path = OUTPUT_DIR / f"{slide['name']}.png"
            image_path.write_bytes(image_data)
            print(f"      [OK] Bild gespeichert: {image_path}")

            # Speichere Caption
            caption_path = OUTPUT_DIR / f"{slide['name']}.md"
            caption_path.write_text(slide["caption"], encoding="utf-8")
            print(f"      [OK] Text gespeichert: {caption_path}")

            results.append({
                "slide": i,
                "name": slide["name"],
                "title": slide["title"],
                "structure_type": slide["structure_type"],
                "image": str(image_path),
                "caption": str(caption_path),
                "success": True
            })
        else:
            print(f"      [FEHLER] Kein Bild generiert")
            results.append({
                "slide": i,
                "name": slide["name"],
                "success": False
            })

    # Speichere Zusammenfassung
    summary_path = OUTPUT_DIR / "slides_summary.json"
    summary_path.write_text(json.dumps(results, indent=2), encoding="utf-8")

    print("\n" + "=" * 60)
    print("ERGEBNIS:")
    print("=" * 60)

    success_count = sum(1 for r in results if r.get("success"))
    print(f"Erfolgreich: {success_count}/3 Bilder")
    print(f"Output: {OUTPUT_DIR}")
    print(f"Zusammenfassung: {summary_path}")


if __name__ == "__main__":
    main()
