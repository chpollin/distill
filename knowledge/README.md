# DISTILL Wissensvault

Projektdokumentation für DISTILL - Document Intelligence for Scientific Text.

## Dokumente

| Dokument | Beschreibung |
|----------|--------------|
| [[WORKFLOW]] | Kanonische Workflow-Beschreibung (DISTILL-3P+V) |
| [[ARCHITECTURE]] | Tech-Stack, CLI, Datenformate |
| [[JOURNAL]] | Chronologische Learnings und Entscheidungen |

## Kernkonzept

Ein **Wissensdokument** ist destilliertes Wissen. Es speichert Prinzipien, nicht Fakten.

**Qualitätskriterien:**
1. **Transferierbarkeit** - Anwendbar auf unbekannte Situationen
2. **Kompaktheit** - Nur das Notwendige, keine Redundanz
3. **Abrufbarkeit** - Strukturiert für schnellen Zugriff

## Prompt-Varianten

| Variante | Kennzeichen | Empfehlung |
|----------|-------------|------------|
| `distill` | Original Markdown-Stil | Legacy |
| `distill_b` | Kompakter XML-Stil | Schnell |
| `distill_c` | Konzept-Taxonomie + Evidence-Constraints | Gut |
| `distill_3p` | 3-Perspektiven-Synthese | Empfohlen |
| `distill_3pv` | 3P + Validierung + Finalisierung | **Beste Qualität** |

Siehe [[WORKFLOW]] für Details zu DISTILL-3P+V.

## Evaluationsergebnis

Basierend auf Tests mit Alvarez_2024_Policy.pdf (siehe [[JOURNAL#Prompt-Evaluation]]):

- **distill_3p/3pv** zeigt höchste Konsistenz und vollständige Konzept-Taxonomie
- **distill_c** ist schneller Einzelprompt mit guter Qualität
- **distill_b** hat Evidenz-Varianz (gefixt mit E2)
- **distill** zeigt Konzept-Varianz zwischen Durchläufen

## Schnellstart

```bash
# Beste Qualität (6 API-Calls)
python distill.py paper.pdf --prompt distill_3pv

# Gute Qualität (4 API-Calls)
python distill.py paper.pdf --prompt distill_3p

# Schnell (1 API-Call)
python distill.py paper.pdf --prompt distill_c
```
