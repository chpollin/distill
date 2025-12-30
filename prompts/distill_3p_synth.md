<role>
Synthesize three specialized extractions into one coherent knowledge document.
</role>

<input_structure>
You receive:
1. PAPER_METADATA: The exact title, authors, and year from the original paper
2. Three extractions from the same paper:
   - EXTRACTION_A: Argument structure (thesis, premises, evidence)
   - EXTRACTION_B: Concept landscape (criticized, proposed, utilized)
   - EXTRACTION_C: Practical implications (audience, recommendations, open problems)

CRITICAL: Use the provided PAPER_METADATA verbatim for the output header. Do not infer or guess metadata from the extractions.
</input_structure>

<merge_rules>
RULE 1 - CONFLICT RESOLUTION:
If extractions contain contradictory statements, include both with source markers [A], [B], or [C] and flag as "!! contested".

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
- Relation: [type] -> [target]

## Proposed
### [name]
- Definition: [from B]
- Role in Argument: [from A if available]
- Relation: [type] -> [target]

## Utilized
### [name]
- Definition: [from B]
- Role in Argument: [from A if available]
- Relation: [type] -> [target]

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
[list any conflicts found with [A], [B], [C] markers, or "None" if no conflicts]

# Synthesis Notes
[optional: observations about extraction quality or gaps]
</output_format>

<input>
## Paper Metadata
{metadata}

## Extraction A (Argument)
{extraction_a}

## Extraction B (Concepts)
{extraction_b}

## Extraction C (Implications)
{extraction_c}
</input>
