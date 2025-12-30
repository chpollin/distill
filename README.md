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

### Nur Wissensextraktion

```bash
python distill.py data/paper.md
```

Output: `knowledge/papers/<paper_name>/distill_v<n>.md`

### Mit Visualisierung

```bash
python distill.py data/paper.md --visualize
```

Fragt interaktiv nach dem zu visualisierenden Konzept.

### Spezifisches Konzept

```bash
python distill.py data/paper.md --visualize --concept "Self-Attention"
```

Output: `output/<concept>.png` + `output/<concept>.md`

## Projektstruktur

```
distill/
├── distill.py      # Hauptskript
├── config.py       # Konfiguration & API-Setup
├── prompts.py      # Prompt-Loader
├── prompts/        # Prompt-Templates für Gemini
├── data/           # Input: Paper als .md oder .txt
├── knowledge/      # Output: Wissensdokumente
└── output/         # Output: Bilder + Begleittexte
```

## Technologie

| Aufgabe | Modell |
|---------|--------|
| Textextraktion | gemini-3-flash-preview |
| Bildgenerierung | gemini-3-pro-image-preview |

## Status

Phase: EXPLORATION
