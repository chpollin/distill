# DISTILL-3P+V: Multi-Perspektiven-Extraktion mit Validierung und Visualisierung

## Übersicht

DISTILL-3P+V ist ein mehrstufiger Workflow zur Wissensextraktion und -visualisierung aus wissenschaftlichen Papers. Drei spezialisierte Prompts extrahieren komplementäre Aspekte, ein Synthese-Prompt führt die Ergebnisse zusammen, ein Validierungs-Prompt prüft gegen den Quelltext, ein Finalisierungs-Prompt integriert die Korrekturen, und optional generiert eine Visualisierungsstufe didaktisch wertvolle Bilder.

**Designprinzipien**

1. Intentionale Perspektivendifferenz statt zufälliger Varianz
2. Regelbasierte Synthese mit Konfidenzmarkierung
3. Quelltext-Validierung vor Auslieferung
4. Transparente Dokumentation von Unsicherheit

---

## Workflow-Architektur

```
┌─────────────────┐
│   Paper-Input   │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────────────────┐
│            STUFE 1: EXTRAKTION                  │
│                  (parallel)                     │
│  ┌───────────┐ ┌───────────┐ ┌───────────┐     │
│  │ Prompt A  │ │ Prompt B  │ │ Prompt C  │     │
│  │ Argument  │ │ Konzepte  │ │Implikation│     │
│  └─────┬─────┘ └─────┬─────┘ └─────┬─────┘     │
└────────┼─────────────┼─────────────┼───────────┘
         │             │             │
         ▼             ▼             ▼
┌─────────────────────────────────────────────────┐
│            STUFE 2: SYNTHESE                    │
│         Drei Extraktionen -> Ein Dokument       │
│         Merge-Regeln 1-5 anwenden               │
└────────────────────┬────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────┐
│            STUFE 3: VALIDIERUNG                 │
│      Synthese + Quelltext -> Validation Report  │
│      Gaps, Overreach, Corrections identifizieren│
└────────────────────┬────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────┐
│            STUFE 4: FINALISIERUNG               │
│    Synthese + Validation Report -> Finales Dok  │
│    Korrekturen integrieren, Konfidenz anpassen  │
└────────────────────┬────────────────────────────┘
                     │
                     ▼
┌─────────────────────┐
│   Finales DISTILL   │
│      Dokument       │
└─────────┬───────────┘
          │ (optional)
          ▼
┌─────────────────────────────────────────────────┐
│            STUFE 5: VISUALISIERUNG              │
│                  (optional)                     │
│  ┌───────────┐ ┌───────────┐ ┌───────────┐     │
│  │  Select   │→│ Generate  │→│ Describe  │     │
│  │ Concepts  │ │  Images   │ │ Captions  │     │
│  └───────────┘ └───────────┘ └───────────┘     │
└────────────────────┬────────────────────────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │   1-5 Bilder mit    │
          │   Begleittexten     │
          └─────────────────────┘
```

---

## Stufe 1: Extraktion

Drei spezialisierte Prompts extrahieren komplementäre Aspekte desselben Papers. Die Prompts laufen parallel und unabhängig voneinander.

| Prompt | Datei | Fokus | Output |
|--------|-------|-------|--------|
| A | `prompts/distill_3p_a.md` | Logische Struktur | Thesis, Premises, Argument Chain, Evidence, Concessions |
| B | `prompts/distill_3p_b.md` | Terminologie | Criticized/Proposed/Utilized Concepts mit Relationen |
| C | `prompts/distill_3p_c.md` | Praktische Relevanz | Audience, Recommendations, Open Problems, Transfer Domains, Historical Context |

---

## Stufe 2: Synthese

Der Synthese-Prompt (`prompts/distill_3p_synth.md`) führt die drei Extraktionen regelbasiert zusammen.

### Merge-Regeln

| Regel | Beschreibung |
|-------|--------------|
| 1 - Conflict Resolution | Widersprüche mit [A]/[B]/[C] markieren, als "!! contested" flaggen |
| 2 - Confidence Weighting | 2+ Quellen = high confidence; 1 Quelle = "[single-source]" |
| 3 - Completeness | Seltene Items markieren, nicht löschen |
| 4 - Evidence Priority | Konkrete Evidenz überschreibt abstrakte Zusammenfassungen |
| 5 - Structural Integration | Thesis aus A, Konzepte aus B, Implikationen aus C, Evidenz aggregiert |

---

## Stufe 3: Validierung

Der Validierungs-Prompt (`prompts/distill_3p_validate.md`) prüft die Synthese gegen den Originaltext.

### Operationen

1. **Verification**: Claims als ✓ verified / ⚠ partial / ✗ not found / ? unverifiable markieren
2. **Gap Analysis**: Fehlende Informationen identifizieren (Critical vs. Minor Gaps)
3. **Overreach Check**: Überinterpretationen flaggen

### Output: Validation Report

- Verification Results (nach Kategorie)
- Gap Analysis (Critical/Minor)
- Overreach Flags
- Recommended Corrections (Additions/Deletions/Reformulations)
- Revised Confidence Assessment

---

## Stufe 4: Finalisierung

Der Finalisierungs-Prompt (`prompts/distill_3p_finalize.md`) integriert die Validierungsergebnisse.

### Correction Rules

| Status | Aktion |
|--------|--------|
| ✓ verified | Unverändert |
| ⚠ partial | Qualifier "[approximate]" oder Reformulierung |
| ✗ not found | Entfernen oder "[unverified - not in source]" |
| ? unverifiable | "[unverifiable - source incomplete]" |
| Critical Gap | In passende Sektion einfügen |
| Overreach | Entfernen oder qualifizieren |

---

## Qualitätskriterien

### Stufe 1: Einzelextraktionen

| Kriterium | Zielwert |
|-----------|----------|
| Thesis-Präzision (Hauptclaim, nicht Thema) | 100% |
| Konzept-Vollständigkeit (alle 3 Kategorien) | 3/3 |
| Evidenz-Konkretheit (Zahlen/Namen/Cases) | >70% |
| Relationsklarheit (explizite Typen) | 100% |

### Stufe 2: Synthese

| Kriterium | Zielwert |
|-----------|----------|
| Merge-Regel-Einhaltung | 5/5 |
| Konflikt-Dokumentation | 100% |
| Single-Source-Markierung | 100% |

### Stufe 3: Validierung

| Kriterium | Zielwert |
|-----------|----------|
| Verifikationsrate (✓ verified) | >80% |
| Critical Gaps | ≤3 |
| Overreach Flags | <3 |

### Stufe 4: Finalisierung

| Kriterium | Zielwert |
|-----------|----------|
| Korrektur-Integration | 100% |
| Struktur-Erhalt | 100% |
| Traceability (Änderungen dokumentiert) | 100% |

---

## Token-Management

| Stufe | Input | Output |
|-------|-------|--------|
| 1A (Argument) | Paper (5-20k) | ~400 tokens |
| 1B (Konzepte) | Paper (5-20k) | ~400 tokens |
| 1C (Implikationen) | Paper (5-20k) | ~350 tokens |
| 2 (Synthese) | 3 Extraktionen (~1.2k) | ~800 tokens |
| 3 (Validierung) | Synthese + Paper (~6-21k) | ~600 tokens |
| 4 (Finalisierung) | Synthese + Report (~1.4k) | ~1000 tokens |

**Gesamt**: 6 API-Calls pro Paper

---

## Fehlerbehandlung

| Situation | Handling |
|-----------|----------|
| Extraktion unvollständig | Synthese markiert als "[not extracted]" |
| Validierung findet Quelltext-Lücken | Markierung als "? unverifiable" |
| Finalisierung kann Konflikte nicht auflösen | Beide Varianten mit Marker behalten |

---

## Workflow-Varianten

| Variante | Stufen | API-Calls | Use Case |
|----------|--------|-----------|----------|
| DISTILL-3P | 1-2 | 4 | Standard, gute Qualität |
| DISTILL-3P+V-Lite | 1-3 | 5 | Validation Report für manuelle Korrektur |
| DISTILL-3P+V | 1-4 | 6 | Beste Qualität, vollautomatisch |

---

## Stufe 5: Visualisierung (optional)

Die Visualisierungsstufe generiert 1-5 didaktisch wertvolle Bilder aus dem finalen Wissensdokument mit automatischer Qualitätskontrolle.

### Sub-Prompts

| Prompt | Datei | Funktion |
|--------|-------|----------|
| Select | `prompts/visualize_select.md` | Wählt 1-5 Konzepte mit höchstem didaktischen Wert |
| Generate | `prompts/visualize.md` | Generiert Bilder mit Gemini Imagen |
| Analyze | `prompts/visualize_analyze.md` | Prüft epistemische Treue, gibt Verbesserungen |
| Describe | `prompts/visualize_describe.md` | Erstellt strukturierte Begleittexte |

### Refinement-Loop

```
Generate v1 → Analyze → [Fidelity < 4?] → Generate v2 → Describe
                              ↓ nein
                           Describe
```

Pro Bild werden 2-4 API-Calls ausgeführt:
1. Generate v1
2. Analyze (Fidelity Score 1-5)
3. Generate v2 (nur wenn Score < 4)
4. Describe (mit Critical Notes aus Analysis)

### Visualisierungs-Parameter

| Parameter | Werte |
|-----------|-------|
| Function | representational, organizational, interpretational, transformative |
| Structure | linear-causal, cyclic-causal, juxtaposition, dissection, zoom, rotation |
| Audience | novice, intermediate, expert |
| Style | kurzgesagt (technical), isotype (pictograms), editorial (humanities) |
| Colors | Semantische Farbcodes (warm=human, cool=technical) |

### Auswahl-Kriterien

Konzepte werden priorisiert nach:
1. Zentralität (Core Thesis, Key Concepts, Argument Chain)
2. Abstraktheit (Text allein ist unzureichend)
3. Relationalität (verbindet mehrere Elemente)
4. Didaktischem Wert (beschleunigt Verständnis)
5. Nicht trivial visualisierbar

### Strukturelle Constraints

Jedes Konzept wird mit zusätzlichen Kontroll-Feldern spezifiziert:

| Feld | Funktion |
|------|----------|
| `relations` | Explizite Beziehungen aus dem Quelltext |
| `negative_constraints` | Was NICHT visualisiert werden darf |
| `source_quote` | Wörtliches Zitat zur Strukturbestimmung |
| `visual_type` | architecture/taxonomy/process/contrast/network |

**Structure Guide:**

| Struktur | Bedingung |
|----------|-----------|
| parallel | Elemente koexistieren ohne Hierarchie |
| nested | Explizite Enthaltensbeziehung im Quelltext |
| linear-causal | Quelltext beschreibt zeitlichen Prozess |
| cyclic-causal | Feedback-Loop explizit genannt |
| juxtaposition | Vergleich/Kontrast zwischen Elementen |
| network | Wechselseitige Beziehungen |

### Fidelity Scoring (streng)

| Score | Kriterium |
|-------|-----------|
| 5 | Perfekte strukturelle Übereinstimmung, keine Constraint-Verletzungen |
| 4 | Kleinere ästhetische Issues, keine strukturellen Fehler |
| 3 | Ein struktureller Fehler ODER eine Constraint-Verletzung |
| 2 | Mehrere strukturelle Fehler ODER fundamentale Fehldarstellung |
| 1 | Komplett falsche Struktur |

**Regeneration bei Score < 4**

### Output

Alle Dateien eines Papers in einem Ordner:

```
output/final/<paper>/
├── <paper>.md              # Wissensdokument
├── <concept>.png           # Visualisierung
└── <concept>.md            # Begleittext
```

---

## Bekannte Limitationen

1. **Quelltext-Abhängigkeit**: Validierung ist nur so gut wie der verfügbare Quelltext
2. **Kaskadenfehler**: Fehler in Stufe 1 propagieren durch alle Stufen
3. **Survey-Papers**: Workflow ist für argumentative Papers optimiert
4. **Modellspezifität**: Prompts sind für Gemini 3 Flash optimiert (XML-Struktur)
5. **Kosten-Skalierung**: 6 API-Calls pro Paper

---

## Changelog

| Version | Datum | Änderung |
|---------|-------|----------|
| 1.0 | 2024-12-30 | DISTILL-3P Basisversion |
| 2.0 | 2024-12-30 | +V Validierungsstufe, Finalisierung, Historical Context, Qualitätskriterien |
| 2.1 | 2024-12-30 | +Visualisierungsstufe (1-5 Bilder mit Begleittexten) |
| 2.2 | 2024-12-30 | +Refinement-Loop mit Fidelity-Analyse |
| 2.3 | 2024-12-30 | +Strukturelle Constraints: negative_constraints, source_quote, visual_type, structure_guide |
| 3.0 | 2024-12-30 | +Craft Mode: Interaktive Einzelkonzept-Visualisierung mit Sketchpad |

---

## Craft Mode (Alternative zu Stufe 5)

Der Craft-Modus ist eine interaktive Alternative zur automatischen Visualisierung. Er ist für Einzelkonzepte mit präzisen User-Vorstellungen gedacht.

### Workflow

```
User-Input (Konzept + Idee + Referenzbild?)
                    │
                    ▼
┌─────────────────────────────────────────────────┐
│            SKETCHPAD-GENERIERUNG                │
│  User-Idee interpretieren, strukturieren        │
│  Negative Constraints ableiten                  │
│  Generation Prompt Preview erstellen            │
└────────────────────┬────────────────────────────┘
                     │
                     ▼
              [User-Freigabe]
                     │
                     ▼
┌─────────────────────────────────────────────────┐
│            BILDGENERIERUNG                      │
│  Mit Sketchpad-Spezifikation                    │
│  Optional: Referenzbild als Stil-Vorlage        │
└────────────────────┬────────────────────────────┘
                     │
                     ▼
              Bild + Begleittext
```

### CLI-Aufruf

```bash
python distill.py craft "Konzeptname" \
    --context "Beschreibung" \
    --idea "Visualisierungsidee" \
    --ref assets/style.png  # optional
    --auto                  # optional: ohne Freigabe
```

### Sketchpad-Struktur

| Sektion | Inhalt |
|---------|--------|
| User Intent | Zusammenfassung des Ziels |
| Interpretation | Wie die Idee auf das Konzept gemappt wird |
| Open Questions | Klärungsbedarf (falls vorhanden) |
| Visual Specification | Core Elements, Structure, Composition, Style, Colors |
| Negative Constraints | Explizite Verbote |
| Generation Prompt Preview | Finaler Prompt für Gemini |

### Vergleich: visualize vs. craft

| Aspekt | visualize | craft |
|--------|-----------|-------|
| Steuerung | Modell entscheidet | User gibt vor |
| Anzahl | 1-5 automatisch | 1 gezielt |
| Interaktion | Keine | Sketchpad-Freigabe |
| Referenzbilder | Nein | Ja |
| Use Case | Batch, Fremd-Papers | Eigene Arbeiten, Präzision |

### Output

```
output/sketches/<concept>_sketchpad.md
output/craft/<concept>.png
output/craft/<concept>.md
```
