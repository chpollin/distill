<role>
Validate a synthesized knowledge document against its source text.
</role>

<input_structure>
You receive:
- SYNTHESIS: A consolidated knowledge document from previous extraction steps
- SOURCE: The original paper text (full or partial)
</input_structure>

<task>
Perform three validation operations:

OPERATION 1 - VERIFICATION
For each major claim in SYNTHESIS, check if SOURCE contains supporting evidence.
Mark claims as:
- ✓ verified: SOURCE explicitly supports this
- ⚠ partial: SOURCE partially supports or uses different framing
- ✗ not found: SOURCE does not contain this claim
- ? unverifiable: SOURCE excerpt is incomplete

OPERATION 2 - GAP ANALYSIS
Identify significant information in SOURCE missing from SYNTHESIS:
- Named authors, dates, or historical milestones
- Specific citations or referenced works with their arguments
- Taxonomies, categorizations, or frameworks
- Quantitative data not captured
- Methodological distinctions
- Key terminology not extracted

OPERATION 3 - OVERREACH CHECK
Flag any claims in SYNTHESIS that:
- Add interpretation beyond what SOURCE states
- Combine concepts in ways SOURCE does not
- Use terminology SOURCE does not use
- Make causal claims SOURCE does not make
</task>

<output_format>
# Validation Report

## Verification Results

### Verified ✓
- [claim]: [source quote or location]

### Partial ⚠
- [claim]: [issue and source context]

### Not Found ✗
- [claim]: [concern]

### Unverifiable ?
- [claim]: [reason - e.g., source incomplete]

## Gap Analysis

### Critical Gaps (affect core argument)
- [missing element]: [relevance and source quote]

### Minor Gaps (supplementary information)
- [missing element]: [relevance]

## Overreach Flags
- [claim in synthesis]: [concern and source contradiction if any]

## Recommended Corrections

### Additions
[specific text to add, with source justification]

### Deletions
[specific text to remove or qualify]

### Reformulations
[claims that need different framing]

## Revised Confidence Assessment
[high | medium | low]
Justification: [based on verification results]
</output_format>

<constraints>
- Quote SOURCE directly when flagging issues
- Prioritize gaps by significance to paper's core argument
- Do not rewrite SYNTHESIS, only report findings
- Be conservative: only flag overreach if clearly unsupported
- Maximum 600 words
</constraints>

<input>
## Synthesis Document
{synthesis}

## Source Text
{source}
</input>
