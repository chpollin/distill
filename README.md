# DISTILL

**Document Intelligence for Scientific Text to Illustrated Learning Layouts**

DISTILL destilliert wissenschaftliche Texte in tokeneffiziente Wissensdokumente und generiert daraus Wissensvisualisierungen mit Begleittexten.

## Kernkonzept

Ein Wissensdokument ist destilliertes Wissen. Es speichert Prinzipien, nicht Fakten. Drei Kriterien bestimmen die Qualität:

1. **Transferierbarkeit**: Anwendbar auf unbekannte Situationen
2. **Kompaktheit**: Nur das Notwendige, keine Redundanz
3. **Abrufbarkeit**: Strukturiert für schnellen Zugriff

## Installation

```bash
pip install -r requirements.txt
cp .env.example .env
# GEMINI_API_KEY in .env eintragen
```

## Usage

### Schnellstart

```bash
# Beste Qualität (6 API-Calls, mit Validierung)
python distill.py data/paper.pdf --prompt distill_3pv

# Gute Qualität (4 API-Calls)
python distill.py data/paper.pdf --prompt distill_3p

# Schnell (1 API-Call)
python distill.py data/paper.pdf --prompt distill_c
```

### PDF-Verarbeitung

```bash
# Multimodal (default) - PDF mit Layout/Bildern an Gemini
python distill.py data/paper.pdf

# Text-Modus - nur extrahierter Text
python distill.py data/paper.pdf --mode text
```

### Prompt-Varianten

| Prompt | API-Calls | Beschreibung |
|--------|-----------|--------------|
| `distill_3pv` | 6 | 3P + Validierung + Finalisierung **(empfohlen)** |
| `distill_3p` | 4 | 3-Perspektiven-Synthese |
| `distill_c` | 1 | Konzept-Taxonomie + Evidence-Constraints |
| `distill_b` | 1 | Kompakter XML-Stil |
| `distill` | 1 | Original Markdown-Stil |

### Mit Visualisierung (Batch)

```bash
# Visualisierung aus finalem Wissensdokument
python distill.py output/final/paper.md --visualize

# Kompletter Workflow: Extraktion + Visualisierung
python distill.py data/paper.pdf --prompt distill_3pv --visualize

# Mit Stil-Referenz (siehe assets/styles/)
python distill.py data/paper.pdf --visualize --style kurzgesagt
```

Generiert 1-5 didaktisch wertvolle Bilder mit strukturierten Begleittexten. Die Anzahl wird automatisch an die Komplexität des Papers angepasst.

**Verfügbare Stile:** `kurzgesagt`, `scientific`, `conceptual`, `narrative` (siehe [assets/styles/](assets/styles/))

### Craft Mode (Interaktiv)

```bash
# Einzelkonzept mit eigener Idee visualisieren
python distill.py craft "Konzeptname" \
    --context "Beschreibung des Konzepts" \
    --idea "Deine Visualisierungsidee"

# Mit Stil-Referenzbild
python distill.py craft "Konzeptname" \
    --context "..." --idea "..." \
    --ref assets/style.png

# Automatische Freigabe (ohne Nachfrage)
python distill.py craft "Konzeptname" --context "..." --idea "..." --auto
```

Der Craft-Modus erzeugt ein editierbares Sketchpad vor der Bildgenerierung:
- Interpretation deiner Idee
- Visuelle Spezifikation (Elemente, Struktur, Komposition)
- Negative Constraints (was vermieden wird)
- Generation Prompt Preview

Output:
```
output/final/<paper>/           # Batch-Visualisierung
├── <paper>.md                  # Wissensdokument
├── <concept>.png               # Visualisierung
└── <concept>.md                # Begleittext

output/sketches/                # Craft-Mode
└── <concept>_sketchpad.md      # Editierbares Sketchpad

output/craft/                   # Craft-Mode
├── <concept>.png               # Generiertes Bild
└── <concept>.md                # Begleittext
```

### Output

```
output/papers/<paper_name>/<prompt>_v<n>.md
```

## 12 Epistemische Visualisierungsstile

DISTILL nutzt eine systematische Taxonomie von 12 Strukturtypen zur Visualisierung:

| Typ | Zeigt | Anwendung |
|-----|-------|-----------|
| `sequence` | Gleichwertige Schritte | Workflows, Prozesse |
| `quantity` | Proportionen | Mengenvergleiche |
| `hub` | Zentrum + Peripherie | Kernkonzepte mit Abhängigkeiten |
| `decomposition` | Teil-Ganzes | Systemarchitektur |
| `transformation` | Qualitative Wandlung | Lernprozesse, Entwicklung |
| `grouping` | Kategorien | Typologien, Klassifikationen |
| `scale` | Überwältigende Masse | Korpusgrößen |
| `contrast` | Gegensätze | Vorher/Nachher, Dichotomien |
| `stratigraphy` | Zeitschichten | Historische Epochen |
| `spiral` | Iteration | Agile Zyklen |
| `network` | Verbindungen | Akteurskonstellationen |
| `uncertainty` | Unschärfe | Hypothesen |

Siehe `knowledge/VISUALIZATION-STYLES.md` für vollständige Dokumentation mit Templates und Beispielbildern.

## DISTILL-3P+V Workflow

Der 3-Perspektiven-Workflow mit Validierung ist die hochqualitative Variante:

```
              ┌── Prompt A (Argument) ──┐
PDF ──────────┼── Prompt B (Konzepte) ──┼── Synthese
              └── Prompt C (Implikat.) ─┘
                                            │
                                            ▼
                              Validierung gegen Quelltext
                                            │
                                            ▼
                              Finalisierung mit Korrekturen
                                            │
                                            ▼
                                   Wissensdokument
```

**Features:**
- Konfidenzmarkierung durch Übereinstimmungsprüfung
- Systematische Konzept-Taxonomie (criticized/proposed/utilized)
- Quelltext-Validierung (✓ verified / ⚠ partial / ✗ not found)
- Automatische Korrektur und Gap-Filling
- Konflikt-Dokumentation bei Widersprüchen

Siehe `knowledge/WORKFLOW.md` für Details.

## Projektstruktur

```
distill/
├── distill.py          # Hauptskript
├── config.py           # Konfiguration & API-Setup
├── prompts.py          # Prompt-Loader
├── prompts/            # Prompt-Templates
│   ├── distill*.md           # Extraktions-Prompts
│   ├── distill_3p_*.md       # 3-Perspektiven-Workflow
│   ├── visualize*.md         # Visualisierungs-Pipeline
│   └── structures/           # 12 Strukturtyp-Templates
│       └── transformation.md # Beispiel-Template
├── config/             # Python-Konfiguration
│   └── structure_types.py    # Strukturtyp-Taxonomie
├── assets/
│   ├── styles/               # Stil-Referenzen
│   └── style-references/     # 80+ Beispielbilder (12 Stile)
├── knowledge/          # Wissensvault (Projektdokumentation)
│   ├── WORKFLOW.md           # Kanonische Workflow-Beschreibung
│   ├── ARCHITECTURE.md       # Tech-Stack, CLI
│   ├── JOURNAL.md            # Learnings & Entscheidungen
│   └── VISUALIZATION-STYLES.md # 12-Stile-Handbuch
├── data/               # Input: PDFs (nicht versioniert)
└── output/             # Output: Wissensdokumente (nicht versioniert)
```

## Technologie

| Aufgabe | Modell |
|---------|--------|
| Wissensextraktion | gemini-3-flash-preview |
| Bildgenerierung | gemini-3-pro-image-preview |

## Status

Phase: EXPLORATION
