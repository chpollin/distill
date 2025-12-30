# INSTRUCTIONS.md – Implementierung

## Technologie

- Python 3.11+
- google-genai SDK
- python-dotenv
- pillow

## Modelle

| Aufgabe | Modell |
|---------|--------|
| Wissensextraktion | gemini-3-flash-preview |
| Bildgenerierung | gemini-3-pro-image-preview |
| Begleittext | gemini-3-flash-preview |

## Dateistruktur

```
distill/
├── data/           # Input
├── knowledge/      # Wissensdokumente
├── output/         # Bilder + Texte
├── distill.py      # Hauptskript
├── prompts.py      # Alle Prompts
├── config.py       # Konfiguration
├── requirements.txt
└── .env
```

## Kernfunktionen

### distill.py

```python
def distill_knowledge(client, text: str) -> str
    # Text → Wissensdokument

def generate_image_prompt(client, concept: str, context: str) -> str
    # Konzept → Bildprompt

def generate_image(client, prompt: str) -> bytes
    # Prompt → Bild

def generate_description(client, concept: str, context: str) -> str
    # Konzept + Kontext → Begleittext
```

### CLI

```bash
python distill.py data/paper.md
python distill.py data/paper.md --visualize
python distill.py data/paper.md --visualize --concept "Name"
```

## Gemini API Aufruf

### Textgenerierung

```python
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[prompt]
)
```

### Bildgenerierung

```python
response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents=[prompt],
    config=types.GenerateContentConfig(
        response_modalities=["Text", "Image"],
        image_config=types.ImageConfig(
            aspect_ratio="16:9",
            image_size="2K"
        )
    )
)
```

## Nächste Schritte

1. Setup ausführen via Claude Code
2. Test-Paper in data/ legen
3. `python distill.py data/paper.md` ausführen
4. Wissensdokument prüfen
5. Destillations-Prompt iterieren
6. Erst dann Visualisierung testen
