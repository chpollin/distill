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
                 └── Text ──────── PyMuPDF -> Gemini (extrahierter Text)
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

Für den detaillierten Workflow siehe [[WORKFLOW]].

## Datenformate

### Input

| Format | Verarbeitung |
|--------|--------------|
| PDF | Multimodal (default) oder Text-Extraktion |
| Markdown | Direkt als Text |
| Plain Text | Direkt als Text |

### Output: Wissensdokument

Basis-Format (alle Prompt-Varianten):

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

### Output: DISTILL-3P / DISTILL-3P+V

Zusätzliche Felder:
- `confidence: high | medium | low`
- `# Implications` (Audience, Recommendations, Open Problems, Transfer Domains)
- `# Historical Context`
- `# Contested Items`
- `# Synthesis Notes`
- `# Validation Notes` (nur 3P+V)

### Output: Visualisierung

| Typ | Format | Pfad |
|-----|--------|------|
| Bild | PNG (2K, 16:9) | `output/{paper}_{concept}.png` |
| Begleittext | Markdown | `output/{paper}_{concept}.md` |

## CLI-Interface

```bash
# Wissensextraktion
python distill.py <input> [options]

Positional:
  input               PDF, Markdown oder Text-Datei

Options:
  --prompt PROMPT     Prompt-Variante (distill, distill_b, distill_c, distill_3p, distill_3pv)
  --mode MODE         PDF-Modus (multimodal, text)
  --visualize         Batch-Visualisierung (1-5 Bilder)
  --style STYLE       Stil-Referenz aus assets/styles/ (kurzgesagt, scientific, conceptual, narrative)

# Craft Mode (Einzelvisualisierung)
python distill.py craft <concept> --context "..." --idea "..." [--ref <image>] [--auto]
```

## Projektstruktur

```
distill/
├── distill.py          # Hauptanwendung
├── config.py           # Konfiguration (Modelle, Pfade)
├── prompts.py          # Prompt-Loader
├── prompts/            # Prompt-Templates
│   ├── distill.md
│   ├── distill_b.md
│   ├── distill_c.md
│   ├── distill_3p_a.md
│   ├── distill_3p_b.md
│   ├── distill_3p_c.md
│   ├── distill_3p_synth.md
│   ├── distill_3p_validate.md
│   ├── distill_3p_finalize.md
│   ├── visualize.md
│   ├── visualize_select.md
│   ├── visualize_analyze.md
│   ├── visualize_describe.md
│   └── craft_sketchpad.md      # Craft-Mode Sketchpad
├── assets/
│   └── styles/         # Stil-Referenzbilder
│       ├── kurzgesagt.png
│       ├── scientific.png
│       ├── conceptual.png
│       └── narrative.png
├── knowledge/          # Projektdokumentation (dieser Vault)
├── data/               # Input-Dateien (nicht versioniert)
└── output/             # Generierte Outputs (nicht versioniert)
    ├── final/          # Batch-Visualisierungen
    ├── sketches/       # Craft-Mode Sketchpads
    └── craft/          # Craft-Mode Bilder
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
| Strukturelle Treue | Struktur entspricht Quelltext (parallel ≠ sequenziell) |
| Constraint-Einhaltung | Keine Verletzung der negative_constraints |
| Inhaltliche Korrektheit | Repräsentiert das Konzept |
| Visuelle Klarheit | Übersichtlich und verständlich |
| Stilkonsistenz | Wissenschaftlich angemessen |

**Fidelity-Scoring:** Score < 4 triggert Regeneration. Strukturelle Fehler wiegen schwerer als ästhetische.
