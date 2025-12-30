# DISTILL-3P: Multi-Perspektiven-Extraktion für wissenschaftliche Texte

## Übersicht

DISTILL-3P ist ein dreistufiger Workflow zur Wissensextraktion aus wissenschaftlichen Papers. Drei spezialisierte Prompts extrahieren komplementäre Aspekte, ein Synthese-Prompt führt die Ergebnisse regelbasiert zusammen.

**Designprinzip**: Intentionale Perspektivendifferenz statt zufälliger Varianz. Jeder Prompt hat einen definierten Fokus, der blinde Flecken der anderen kompensiert.

---

## Stufe 1: Drei Extraktionsprompts

### Prompt A: Argument-Extraktion

```xml
<role>
Extract the logical structure of a scientific paper.
</role>

<task>
Analyze the paper and extract:
1. THESIS: The central claim in one sentence
2. PREMISES: Assumptions the argument builds on (max 5)
3. ARGUMENT_CHAIN: Numbered inference steps from premises to conclusion
4. EVIDENCE: Concrete support (statistics, case studies, citations with numbers)
5. CONCESSIONS: Limitations or counterarguments the paper acknowledges
</task>

<constraints>
- EVIDENCE must include specific quantities, named datasets, or cited cases
- Reject abstract summaries like "synthesis of literature"
- ARGUMENT_CHAIN steps must be logically connected with explicit transitions
- Maximum 300 words total
</constraints>

<output_format>
## Thesis
[single sentence]

## Premises
- [premise 1]
- [premise 2]
...

## Argument Chain
1. [step] →
2. [step] →
3. [conclusion]

## Evidence
- [type]: [specific content]
...

## Concessions
- [limitation or counterargument]
...
</output_format>

<input>
{{PAPER_TEXT}}
</input>
```

---

### Prompt B: Konzept-Extraktion

```xml
<role>
Map the terminological landscape of a scientific paper.
</role>

<task>
Identify and categorize concepts into three classes:
1. CRITICIZED: Paradigms, approaches, or terms the paper rejects or problematizes
2. PROPOSED: New terms, frameworks, or models the paper introduces
3. UTILIZED: Established concepts the paper uses as analytical tools

For each concept provide:
- Name (exact term from paper)
- Definition (as given or implied in paper)
- Relations (how it connects to other concepts: replaces, enables, conflicts with, requires)
</task>

<constraints>
- Extract at least one concept per category
- Definitions must come from the paper, not external knowledge
- Relations must use explicit type: replaces | enables | conflicts_with | requires | extends
- Maximum 5 concepts total, prioritize by centrality to argument
</constraints>

<output_format>
## Criticized Concepts
### [Concept Name]
- Definition: [from paper]
- Relation: [type] → [target concept]

## Proposed Concepts
### [Concept Name]
- Definition: [from paper]
- Relation: [type] → [target concept]

## Utilized Concepts
### [Concept Name]
- Definition: [from paper]
- Relation: [type] → [target concept]
</output_format>

<input>
{{PAPER_TEXT}}
</input>
```

---

### Prompt C: Implikations-Extraktion

```xml
<role>
Extract the practical relevance and implications of a scientific paper.
</role>

<task>
Analyze the paper for:
1. AUDIENCE: Who is this written for? (researchers, practitioners, policymakers, specific disciplines)
2. RECOMMENDATIONS: What should readers do differently? (max 5 actionable items)
3. OPEN_PROBLEMS: What does the paper mark as unresolved? (max 3)
4. TRANSFER_DOMAINS: Where else could these insights apply?
</task>

<constraints>
- RECOMMENDATIONS must be actionable, not descriptive
- OPEN_PROBLEMS must be explicitly stated in the paper, not inferred gaps
- TRANSFER_DOMAINS require justification in one sentence
- Maximum 250 words total
</constraints>

<output_format>
## Audience
[primary and secondary audiences]

## Recommendations
1. [actionable recommendation]
2. [actionable recommendation]
...

## Open Problems
- [problem as stated in paper]
...

## Transfer Domains
- [domain]: [one-sentence justification]
...
</output_format>

<input>
{{PAPER_TEXT}}
</input>
```

---

## Stufe 2: Synthese-Prompt

```xml
<role>
Synthesize three specialized extractions into one coherent knowledge document.
</role>

<input_structure>
You receive three extractions from the same paper:
- EXTRACTION_A: Argument structure (thesis, premises, evidence)
- EXTRACTION_B: Concept landscape (criticized, proposed, utilized)
- EXTRACTION_C: Practical implications (audience, recommendations, open problems)
</input_structure>

<merge_rules>
RULE 1 - CONFLICT RESOLUTION:
If extractions contain contradictory statements, include both with source markers [A], [B], or [C] and flag as "⚠ contested".

RULE 2 - CONFIDENCE WEIGHTING:
- Statements appearing in 2+ extractions: high confidence (no marker)
- Statements from single extraction: mark as "[single-source]"

RULE 3 - COMPLETENESS:
Never discard concepts or arguments because they appear rarely. Mark rare items, do not delete them.

RULE 4 - EVIDENCE PRIORITY:
Concrete evidence (numbers, names, cases) overrides abstract summaries. Always preserve specifics.

RULE 5 - STRUCTURAL INTEGRATION:
- Thesis comes from A
- Key Concepts come from B, enriched with argument context from A
- Implications come from C
- Evidence aggregates from all three
</merge_rules>

<output_format>
---
source: [paper title]
authors: [author list]
year: [year]
domain: [from extractions]
confidence: [high | medium | low based on extraction agreement]
---

# Core Thesis
[from Extraction A]

# Key Concepts

## Criticized
### [name]
- Definition: [from B]
- Role in Argument: [from A if available]
- Relation: [type] → [target]

## Proposed
### [name]
- Definition: [from B]
- Role in Argument: [from A if available]
- Relation: [type] → [target]

## Utilized
### [name]
- Definition: [from B]
- Role in Argument: [from A if available]
- Relation: [type] → [target]

# Argument Chain
[numbered steps from A, with confidence markers]

# Evidence
- [type]: [content] [source marker if single-source]
...

# Implications
- Audience: [from C]
- Recommendations: [from C]
- Open Problems: [from C]
- Transfer Domains: [from C]

# Contested Items
[list any conflicts found with [A], [B], [C] markers]

# Synthesis Notes
[optional: observations about extraction quality or gaps]
</output_format>

<input>
## Extraction A (Argument)
{{EXTRACTION_A}}

## Extraction B (Concepts)
{{EXTRACTION_B}}

## Extraction C (Implications)
{{EXTRACTION_C}}
</input>
```

---

## Workflow-Ablauf

```
┌─────────────┐
│ Paper-Input │
└──────┬──────┘
       │
       ▼
┌──────────────────────────────────────────┐
│           Stufe 1: Parallel              │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐    │
│  │Prompt A │ │Prompt B │ │Prompt C │    │
│  │Argument │ │Konzepte │ │Implikat.│    │
│  └────┬────┘ └────┬────┘ └────┬────┘    │
└───────┼───────────┼───────────┼─────────┘
        │           │           │
        ▼           ▼           ▼
┌──────────────────────────────────────────┐
│         Stufe 2: Synthese                │
│  ┌────────────────────────────────────┐  │
│  │   Merge nach Regeln 1-5            │  │
│  │   → Konfidenzmarkierung            │  │
│  │   → Konfliktdokumentation          │  │
│  └────────────────────────────────────┘  │
└──────────────────────────────────────────┘
        │
        ▼
┌─────────────────┐
│ Finales DISTILL │
│   Dokument      │
└─────────────────┘
```

---

## Qualitätskriterien für Evaluation

| Kriterium | Messung | Zielwert |
|-----------|---------|----------|
| Thesis-Konsistenz | Semantische Übereinstimmung A↔Synthese | >95% |
| Konzept-Vollständigkeit | Kategorien criticized/proposed/utilized belegt | 3/3 |
| Evidenz-Konkretheit | Anteil Evidenz mit Zahlen/Namen/Cases | >70% |
| Konflikt-Transparenz | Alle Widersprüche dokumentiert | 100% |
| Implikations-Actionability | Empfehlungen sind handlungsorientiert | >80% |

---

## Erweiterungsmöglichkeiten

**Prompt D: Methodik-Kritik**
Fokus auf Forschungsdesign, Validität, Reproduzierbarkeit. Sinnvoll für empirische Papers.

**Prompt E: Historische Einordnung**
Fokus auf Vorläufer, Paradigmenwechsel, Schulenbildung. Sinnvoll für theoretische Papers.

**Prompt F: Interdisziplinäre Brücken**
Fokus auf Anschlussfähigkeit zu anderen Disziplinen. Sinnvoll für Survey-Papers.

---

## Bekannte Limitationen

1. **Synthese-Prompt als Fehlerquelle**: Der Merge-Schritt kann selbst Fehler einführen. Manuelle Stichproben empfohlen.

2. **Lange Papers**: Bei >20 Seiten sollte vorgelagerte Segmentierung erfolgen, mit je einem Durchlauf pro Hauptabschnitt.

3. **Konsens ≠ Korrektheit**: Wenn alle drei Prompts denselben Fehler machen, verstärkt die Synthese ihn. Domänenexpertise bleibt notwendig.

4. **Modellspezifität**: Prompts sind für Gemini 3 Flash optimiert (XML-Struktur, Constraints am Ende). Andere Modelle erfordern Anpassung.

---

## Changelog

| Version | Datum | Änderung |
|---------|-------|----------|
| 1.0 | 2025-12-30 | Initiale Version basierend auf Evaluationsergebnissen NoBIAS-Paper |