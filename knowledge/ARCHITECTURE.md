# DISTILL Architektur

## Technologie-Stack

| Komponente | Technologie |
|------------|-------------|
| Runtime | Python 3.11+ |
| API | google-genai SDK |
| PDF-Extraktion | PyMuPDF (fitz) |
| Bildverarbeitung | Pillow |
| Konfiguration | python-dotenv |

## Modelle

| Aufgabe | Modell |
|---------|--------|
| Wissensextraktion | gemini-3-flash-preview |
| Bildgenerierung | gemini-3-pro-image-preview |

## Datenfluss

```
Input (PDF/MD) ──┬── Multimodal ── Gemini (PDF direkt)
                 └── Text ──────── PyMuPDF → Gemini (extrahierter Text)
                          │
                          ▼
                    Wissensdokument
                          │
                          ▼ (optional)
                    Visualisierung
                          │
                    ┌─────┴─────┐
                    ▼           ▼
                  Bild      Begleittext
```

## Datenformate

### Input

| Format | Verarbeitung |
|--------|--------------|
| PDF | Multimodal (default) oder Text-Extraktion |
| Markdown | Direkt als Text |
| Plain Text | Direkt als Text |

### Output: Wissensdokument

```markdown
---
source: [Titel]
authors: [Autoren]
year: [Jahr]
domain: [Domäne]
---

# Core Thesis
[Ein Satz]

# Key Concepts
## [Konzept]
[Definition]
-> [Relation]

# Argument Chain
[Logische Kette]

# Evidence
- [Typ]: [Spezifischer Beleg]

# Limitations
[Methodische/kontextuelle Einschränkungen]
```

### Output: DISTILL-3P

Zusätzliche Felder:
- `confidence: high | medium | low`
- `# Implications` (Audience, Recommendations, Open Problems)
- `# Contested Items`
- `# Synthesis Notes`

### Output: Visualisierung

| Typ | Format | Pfad |
|-----|--------|------|
| Bild | PNG (2K, 16:9) | `output/{paper}_{concept}.png` |
| Begleittext | Markdown | `output/{paper}_{concept}.md` |

## CLI-Interface

```bash
python distill.py <input> [options]

Positional:
  input               PDF, Markdown oder Text-Datei

Options:
  --prompt PROMPT     Prompt-Variante (distill, distill_b, distill_c, distill_3p)
  --mode MODE         PDF-Modus (multimodal, text)
  --visualize         Bild generieren
  --concept CONCEPT   Spezifisches Konzept visualisieren
```

## Kernfunktionen

```python
# Wissensextraktion
distill_knowledge(client, content, prompt_name, is_multimodal) -> str

# 3-Perspektiven-Workflow
distill_3p(client, content, is_multimodal) -> str
  ├── extract_metadata(...)
  ├── distill_knowledge(..., "distill_3p_a", ...)  # Argument
  ├── distill_knowledge(..., "distill_3p_b", ...)  # Konzepte
  ├── distill_knowledge(..., "distill_3p_c", ...)  # Implikationen
  └── synthesize(metadata, a, b, c)

# Visualisierung
generate_image_prompt(client, concept, context) -> str
generate_image(client, prompt) -> bytes
generate_description(client, concept, context) -> str
```

## Qualitätskriterien

### Wissensdokument

| Kriterium | Beschreibung |
|-----------|--------------|
| Kompression | Mindestens Faktor 5 kleiner als Original |
| Transferierbarkeit | Prinzipien statt Beispiele |
| Selbstgenügsamkeit | Ohne Original verständlich |
| Evidenz-Konkretheit | Zahlen, Namen, Cases statt Abstraktion |

### Visualisierung

| Kriterium | Beschreibung |
|-----------|--------------|
| Inhaltliche Korrektheit | Repräsentiert das Konzept |
| Visuelle Klarheit | Übersichtlich und verständlich |
| Stilkonsistenz | Wissenschaftlich angemessen |
