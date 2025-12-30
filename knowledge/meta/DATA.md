# DATA.md – Datenformate

## Eingabe

### Paper (Markdown oder Plain Text)

- Format: `.md` oder `.txt`
- Speicherort: `data/`
- Inhalt: Wissenschaftlicher Text, manuell aus PDF extrahiert oder direkt als Markdown verfügbar

## Zwischenformat

### Wissensdokument

Tokeneffiziente Repräsentation des Paper-Inhalts. Speicherort: `knowledge/`

```markdown
---
source: [Titel des Papers]
authors: [Autorenliste]
year: [Jahr]
---

# Kernthese

[Ein Satz: Die zentrale Aussage des Papers]

# Schlüsselkonzepte

## [Konzept 1]
[1-2 Sätze: Definition und Relation zu anderen Konzepten]

## [Konzept 2]
[...]

# Argumentationsstruktur

[Kompakt: Prämissen → Schlussfolgerungen]

# Visualisierbare Elemente

- [Element]: [Warum und wie visualisierbar]
- [...]
```

## Ausgabe

### Bild

- Format: PNG
- Auflösung: 2K (default) oder 4K
- Aspect Ratio: 16:9 (default) oder 1:1
- Speicherort: `output/`
- Naming: `{paper}_{konzept}.png`

### Begleittext

- Format: Markdown
- Speicherort: `output/`
- Naming: `{paper}_{konzept}.md`

Struktur:
```markdown
[Absatz 1: Was zeigt das Bild?]

[Absatz 2: Bezug zum Paper]

[Absatz 3: Kernaussage der Visualisierung]
```

## Qualitätskriterien Wissensdokument

| Kriterium | Beschreibung |
|-----------|--------------|
| Kompression | Mindestens Faktor 5 kleiner als Original |
| Transferierbarkeit | Prinzipien statt Beispiele |
| Selbstgenügsamkeit | Ohne Original verständlich |
| Visualisierbarkeit | Mindestens 2-3 konkrete Elemente identifiziert |
