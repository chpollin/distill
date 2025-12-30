# DISTILL Journal

Chronologische Dokumentation von Erkenntnissen, Entscheidungen und Learnings.

---

## 2024-12-30

### Repository-Setup

**Entscheidung: Datei-Struktur für Git**

Committet:
- Source: `distill.py`, `config.py`, `prompts.py`
- Prompts: `prompts/*.md` (5 Templates)
- Docs: `README.md`, `knowledge/meta/*.md`
- Config: `.gitignore`, `.env.example`, `requirements.txt`

Ignoriert:
- `.env` (API-Key)
- `__pycache__/` (generiert)
- `data/` (Input-Testdaten)
- `knowledge/papers/` (generierte Outputs)
- `output/` (generierte Bilder)

**Begründung:** Source und Prompts sind versionierungsrelevant. Testdaten und Outputs sind reproduzierbar und enthalten keine Logik.

---

### Learnings

**L1: .env.example gehört ins Repo**

Fehler in initialer `.gitignore`: `.env.example` war ignoriert. Diese Datei ist das sichere Template für andere Entwickler und muss committet werden. Nur `.env` (mit echten Keys) wird ignoriert.

**L2: Prompt-Templates als separate Dateien**

Architekturentscheidung: Prompts liegen in `prompts/*.md`, nicht inline im Code. Vorteile:
- Editierbar ohne Code-Änderung
- Versionierbar
- Mehrere Varianten testbar (distill.md, distill_a.md, distill_b.md)

**L3: Versionierte Outputs**

Output-Pfad: `knowledge/papers/<paper_name>/distill_v<n>.md`

Das `_v<n>` Suffix ermöglicht iterative Verbesserung ohne Überschreiben. Vergleich zwischen Versionen möglich.

**L4: Gemini-Modelle (Stand 12/2024)**

| Aufgabe | Modell |
|---------|--------|
| Text | gemini-3-flash-preview |
| Bild | gemini-3-pro-image-preview |

Preview-Modelle für experimentelle Features. Bildgenerierung erfordert Pro-Variante.

---

### PDF-Verarbeitung

**Entscheidung: Zwei Modi für PDF-Input**

| Modus | Flag | Beschreibung |
|-------|------|--------------|
| Multimodal | `--mode multimodal` (default) | PDF direkt an Gemini, erhält Layout/Bilder |
| Text | `--mode text` | PyMuPDF-Extraktion, nur Text |

**Begründung:** Multimodal erhält mehr Kontext (Tabellen, Abbildungen), Text ist kompakter und potentiell günstiger. Beide haben Anwendungsfälle.

---

### Prompt-Evaluation (Alvarez_2024_Policy.pdf)

**Getestete Varianten:**

| Variante | Kennzeichen | Qualität |
|----------|-------------|----------|
| `distill` | Original Markdown | Moderate Konsistenz, Konzept-Varianz |
| `distill_b` | XML-Struktur | Hohe Thesis-Stabilität, Evidenz-Varianz |
| `distill_c` | Mit Taxonomie + Evidence-Constraints | Hohe Konsistenz, konkrete Evidenz |
| `distill_3p` | 3-Perspektiven-Synthese | Höchste Konsistenz, vollständige Taxonomie |

**L5: Evidenz-Konkretheit erfordert explizite Constraints**

Ohne Anweisung "include specific quantities, named datasets" weicht Gemini auf Abstraktion aus. Prompts mit expliziten Evidenz-Anforderungen (distill_c, distill_3p) zeigen konsistent konkrete Belege.

**L6: Konzept-Taxonomie stabilisiert Extraktion**

Die Dreiteilung `criticized/proposed/utilized` erzwingt systematische Abdeckung. Ohne Taxonomie variiert die Konzeptauswahl zwischen Durchläufen.

**L7: Multi-Perspektiven-Synthese kompensiert Einzelfehler**

DISTILL-3P nutzt drei spezialisierte Prompts (Argument, Konzepte, Implikationen) mit regelbasierter Synthese. Vorteile:
- Konfidenzmarkierung durch Übereinstimmungsprüfung
- Source-Marker für Einzelbelege
- Conflict-Dokumentation bei Widersprüchen

**L8: Metadaten separat extrahieren**

Bug in 3P v1: Synthese-Prompt inferierte falsche Metadaten aus Extraktionen. Fix: Metadaten als separater Extraktionsschritt vor der Synthese.

---

### Prompt-Fixes angewendet

**E1: Metadaten-Fix für DISTILL-3P**

Synthese-Prompt erhält jetzt explizites `{metadata}` Feld. Metadaten werden in Stufe 0 separat extrahiert.

**E2: Evidenz-Constraint für distill_b**

Regel ergänzt: "Minimum 2 evidence items. Must include specific numbers, names, or case studies."

---

### DISTILL-3P+V Implementierung

**Entscheidung: Validierungsstufe hinzugefügt**

Der 3P-Workflow wurde um zwei Stufen erweitert:
- Stufe 3: Validierung gegen Quelltext
- Stufe 4: Finalisierung mit Korrekturen

Neue Prompts: `distill_3p_validate.md`, `distill_3p_finalize.md`

**L9: Validierung entfernt Halluzinationen**

Im Test mit Alvarez_2024_Policy.pdf wurden 11-14 Korrekturen pro Durchlauf angewendet. Typische Entfernungen:
- Unverifiable Statistiken (z.B. "21% XAI statistic")
- Fehlzuschreibungen (z.B. "Ground truth myth")
- Überinterpretationen in Argument Chain

**L10: Konfidenz-Abstufung ist informativ**

"Medium confidence" mit Begründung ist nützlicher als "high" ohne Begründung. Der Workflow stuft automatisch herab, wenn Quelltext-Ausschnitt unvollständig.

**L11: Traceability durch Validation Notes**

Jede Änderung wird dokumentiert:
- Corrections applied: [Anzahl]
- Additions: [Liste]
- Removals: [Liste]
- Remaining uncertainties: [Liste]

**L12: Finale Dokumente in separatem Ordner**

Output-Pfad für `distill_3pv`: `output/final/<paper_name>.md`

Keine Versionierung, da validierte Dokumente als kanonisch gelten. Erleichtert das Auffinden fertiger Extrakte.

---

### Workflow-Vergleich (Final)

| Kriterium | distill | distill_b | distill_c | distill_3p | distill_3pv |
|-----------|---------|-----------|-----------|------------|-------------|
| API-Calls | 1 | 1 | 1 | 4 | 6 |
| Konzept-Taxonomie | Nein | Nein | Ja | Ja | Ja |
| Evidenz-Verifizierung | Nein | Nein | Nein | Nein | Ja |
| Konfidenz-Begründung | Nein | Nein | Nein | Ja | Ja |
| Traceability | Nein | Nein | Nein | Nein | Ja |

**Empfehlung**: `distill_3pv` für finale Extrakte, `distill_c` für schnelle Einzeldurchläufe.
