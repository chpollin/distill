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

### PDF-Verarbeitung

```bash
# Multimodal (default) - PDF mit Layout/Bildern an Gemini
python distill.py data/paper.pdf

# Text-Modus - nur extrahierter Text
python distill.py data/paper.pdf --mode text
```

### Prompt-Varianten

| Prompt | Beschreibung | Befehl |
|--------|--------------|--------|
| `distill` | Original Markdown-Stil | `--prompt distill` |
| `distill_b` | Kompakter XML-Stil | `--prompt distill_b` |
| `distill_c` | Mit Konzept-Taxonomie + Evidence-Constraints | `--prompt distill_c` |
| `distill_3p` | 3-Perspektiven-Synthese (empfohlen) | `--prompt distill_3p` |

```bash
# Empfohlen: 3-Perspektiven-Workflow
python distill.py data/paper.pdf --prompt distill_3p

# Schneller Einzelprompt
python distill.py data/paper.pdf --prompt distill_c
```

### Mit Visualisierung

```bash
python distill.py data/paper.pdf --visualize
python distill.py data/paper.pdf --visualize --concept "Causal Fairness"
```

### Output

```
output/papers/<paper_name>/<prompt>_v<n>.md
```

## Projektstruktur

```
distill/
├── distill.py      # Hauptskript
├── config.py       # Konfiguration & API-Setup
├── prompts.py      # Prompt-Loader
├── prompts/        # Prompt-Templates
│   ├── distill.md
│   ├── distill_b.md
│   ├── distill_c.md
│   ├── distill_3p_a.md   # Argument-Extraktion
│   ├── distill_3p_b.md   # Konzept-Extraktion
│   ├── distill_3p_c.md   # Implikations-Extraktion
│   └── distill_3p_synth.md
├── knowledge/      # Wissensvault (Projektdokumentation)
├── data/           # Input: PDFs
└── output/         # Output: Wissensdokumente, Bilder
```

## DISTILL-3P Workflow

Der 3-Perspektiven-Workflow extrahiert drei komplementäre Aspekte und synthetisiert sie regelbasiert:

```
PDF ──┬── Prompt A (Argument) ──┐
      ├── Prompt B (Konzepte) ──┼── Synthese ── Wissensdokument
      └── Prompt C (Implikat.) ─┘
```

Vorteile:
- Konfidenzmarkierung durch Übereinstimmungsprüfung
- Systematische Konzept-Taxonomie (criticized/proposed/utilized)
- Konflikt-Dokumentation bei Widersprüchen

## Technologie

| Aufgabe | Modell |
|---------|--------|
| Textextraktion | gemini-3-flash-preview |
| Bildgenerierung | gemini-3-pro-image-preview |

## Status

Phase: EXPLORATION
