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
├── generate_webdev_slides.py  # Standalone Slide-Generator
├── prompts/            # Prompt-Templates
│   ├── distill*.md           # Extraktions-Prompts
│   ├── distill_3p_*.md       # 3-Perspektiven-Workflow
│   ├── visualize*.md         # Visualisierungs-Pipeline
│   ├── craft_sketchpad.md    # Craft-Mode Sketchpad
│   └── structures/           # 12 Strukturtyp-Templates
│       └── transformation.md # Proof-of-Concept Template
├── config/             # Python-Konfiguration
│   └── structure_types.py    # Strukturtyp-Taxonomie (12 Typen)
├── assets/
│   ├── styles/               # Stil-Referenzen (4 Stile)
│   └── style-references/     # 80+ Beispielbilder (12 Ordner)
│       ├── stil-01-sequenz/
│       ├── stil-02-quantität/
│       ├── ...
│       └── stil-12-unschärfe/
├── knowledge/          # Projektdokumentation (dieser Vault)
│   ├── WORKFLOW.md
│   ├── ARCHITECTURE.md
│   ├── JOURNAL.md
│   └── VISUALIZATION-STYLES.md  # 12-Stile-Handbuch
├── data/               # Input-Dateien (nicht versioniert)
└── output/             # Generierte Outputs (nicht versioniert)
    ├── final/          # Batch-Visualisierungen
    ├── papers/         # Wissensdokumente
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

## 12 Epistemische Strukturtypen

Die Visualisierungspipeline nutzt eine systematische Taxonomie von 12 Strukturtypen:

| Nr | Typ | Zeigt | Beispiel |
|----|-----|-------|----------|
| 1 | `sequence` | Gleichwertige Schritte | Workflows, Prozesse |
| 2 | `quantity` | Proportionen | Mengenvergleiche |
| 3 | `hub` | Zentrum + Peripherie | Kernkonzepte |
| 4 | `decomposition` | Teil-Ganzes | Systemarchitektur |
| 5 | `transformation` | Qualitative Wandlung | Lernprozesse |
| 6 | `grouping` | Kategorien | Typologien |
| 7 | `scale` | Masse fassbar | Korpusgrößen |
| 8 | `contrast` | Gegensätze | Vorher/Nachher |
| 9 | `stratigraphy` | Zeitschichten | Epochen |
| 10 | `spiral` | Iteration | Agile Zyklen |
| 11 | `network` | Verbindungen | Akteursnetzwerke |
| 12 | `uncertainty` | Unschärfe | Hypothesen |

Siehe [[VISUALIZATION-STYLES]] für Details zu jedem Typ mit Template-Prompts und Beispielbildern.

## Standalone-Skripte

### generate_webdev_slides.py

Generiert Folien für Tutorials mit direkten Prompts:

```bash
python generate_webdev_slides.py
```

Output: `output/webdev-intro-beginner/` mit PNG-Bildern und Markdown-Captions.
