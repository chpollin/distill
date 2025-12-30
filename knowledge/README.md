# DISTILL Wissensvault

Dieses Verzeichnis enthält die Projektdokumentation und Learnings.

## Inhalt

| Datei | Beschreibung |
|-------|--------------|
| [JOURNAL.md](JOURNAL.md) | Chronologische Learnings und Entscheidungen |
| [DISTILL-3P.md](DISTILL-3P.md) | Spezifikation des 3-Perspektiven-Workflows |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Technische Architektur und Datenformate |

## Kernkonzept

Ein Wissensdokument ist destilliertes Wissen. Es speichert Prinzipien, nicht Fakten.

**Qualitätskriterien:**

1. **Transferierbarkeit**: Anwendbar auf unbekannte Situationen
2. **Kompaktheit**: Nur das Notwendige, keine Redundanz
3. **Abrufbarkeit**: Strukturiert für schnellen Zugriff

## Prompt-Varianten

| Variante | Kennzeichen | Empfehlung |
|----------|-------------|------------|
| `distill` | Original Markdown-Stil | Legacy |
| `distill_b` | Kompakter XML-Stil | Schnell |
| `distill_c` | Konzept-Taxonomie + Evidence-Constraints | Gut |
| `distill_3p` | 3-Perspektiven-Synthese | **Empfohlen** |

## Evaluationsergebnis

Basierend auf Tests mit Alvarez_2024_Policy.pdf:

- **distill_3p** zeigt höchste Konsistenz und vollständige Konzept-Taxonomie
- **distill_c** ist schneller Einzelprompt mit guter Qualität
- **distill_b** hat Evidenz-Varianz (gefixt)
- **distill** zeigt Konzept-Varianz zwischen Durchläufen
