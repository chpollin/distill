# REQUIREMENTS.md – Anforderungen

## Funktionale Anforderungen

### Must-Have (MVP)

| ID | Anforderung |
|----|-------------|
| R1 | System liest Markdown/Text-Dateien |
| R2 | System erzeugt Wissensdokument nach Schema |
| R3 | System generiert Bildprompt aus Konzept |
| R4 | System erzeugt Bild via Gemini API |
| R5 | System speichert Outputs strukturiert |

### Should-Have

| ID | Anforderung |
|----|-------------|
| R6 | System generiert Begleittext zum Bild |
| R7 | Nutzer kann Konzept interaktiv wählen |
| R8 | Zwischenergebnisse werden geloggt |

### Later

| ID | Anforderung |
|----|-------------|
| R9 | PDF-Import |
| R10 | Automatische Bildevaluation |
| R11 | Iterative Prompt-Verfeinerung |

## Nicht-funktionale Anforderungen

| ID | Anforderung |
|----|-------------|
| NR1 | API-Key über Umgebungsvariable |
| NR2 | Fehlerbehandlung bei API-Ausfällen |
| NR3 | Wissensdokument mindestens Faktor 5 kompakter als Input |

## Evaluationskriterien Bild

Manuelle Prüfung nach Generierung:

1. **Inhaltliche Korrektheit**: Repräsentiert das Konzept?
2. **Visuelle Klarheit**: Übersichtlich und verständlich?
3. **Stilkonsistenz**: Wissenschaftlich angemessen?
4. **Textlesbarkeit**: Falls Text im Bild, korrekt und lesbar?

Automatisierte Evaluation ist explizit nicht Teil des MVP.
