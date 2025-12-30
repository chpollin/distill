# DISTILL-3P+V: Multi-Perspektiven-Extraktion mit Validierung

## Übersicht

DISTILL-3P+V ist ein vierstufiger Workflow zur Wissensextraktion aus wissenschaftlichen Papers. Drei spezialisierte Prompts extrahieren komplementäre Aspekte, ein Synthese-Prompt führt die Ergebnisse zusammen, ein Validierungs-Prompt prüft gegen den Quelltext, und ein Finalisierungs-Prompt integriert die Korrekturen.

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
