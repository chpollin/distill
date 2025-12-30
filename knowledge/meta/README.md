# DISTILL

**Document Intelligence for Scientific Text to Illustrated Learning Layouts**

## Was DISTILL macht

DISTILL destilliert wissenschaftliche Texte in tokeneffiziente Wissensdokumente und generiert daraus Wissensvisualisierungen mit Begleittexten.

Input: Paper als Markdown oder Plain Text
Output: Wissensdokument + Bilder + Begleittexte

## Kernkonzept

Ein Wissensdokument ist destilliertes Wissen. Es speichert Prinzipien, nicht Fakten. Drei Kriterien bestimmen die Qualität:

1. **Transferierbarkeit**: Anwendbar auf unbekannte Situationen
2. **Kompaktheit**: Nur das Notwendige, keine Redundanz
3. **Abrufbarkeit**: Strukturiert für schnellen Zugriff

## Technologie

| Aufgabe | Modell |
|---------|--------|
| Textextraktion | gemini-3-flash-preview |
| Bildgenerierung | gemini-3-pro-image-preview |

## Projektstruktur

```
distill/
├── data/           # Input: Paper als .md oder .txt
├── knowledge/      # Output: Wissensdokumente
├── output/         # Output: Bilder + Begleittexte
├── distill.py      # Hauptskript
├── prompts.py      # Zentrale Prompts
└── config.py       # Konfiguration
```

## Usage

```bash
# Nur Wissensextraktion
python distill.py data/paper.md

# Mit Visualisierung
python distill.py data/paper.md --visualize

# Spezifisches Konzept
python distill.py data/paper.md --visualize --concept "Self-Attention"
```

## Status

Phase: EXPLORATION
Nächster Schritt: Test mit realem Paper
