<role>
Analyze a scientific visualization for epistemic fidelity and structural accuracy. Be STRICT—a visualization that misrepresents the source structure is fundamentally flawed regardless of aesthetics.
</role>

<input>
## Image
{image}

## Source Concept
{concept}

## Context (what the source document says)
{context}

## Intended Structure
{structure}

## Negative Constraints (what should NOT appear)
{negative_constraints}
</input>

<task>
Perform four analytical operations and generate actionable feedback.

OPERATION 1 - STRUCTURAL ACCURACY (most important)
Check if the visualization matches the SOURCE DOCUMENT's actual structure:
- If source describes PARALLEL elements: Are they shown side-by-side with equal weight?
- If source describes NESTED elements: Is containment correctly shown?
- If source describes a PROCESS: Are temporal stages accurately represented?
- If source describes CONTRAST: Are the two sides clearly distinguished?

CRITICAL ERRORS (automatic score <= 2):
- Showing parallel elements as nested
- Adding temporal stages to non-process concepts
- Showing architectural layers as developmental phases
- Inventing containment relationships not in the source

OPERATION 2 - NEGATIVE CONSTRAINT VIOLATIONS
Check if any negative constraints were violated:
- Are there elements that were explicitly forbidden?
- Did the visualization add "Stage 1, Stage 2" to a non-process?
- Did it nest elements that should be parallel?

OPERATION 3 - EPISTEMIC ALIGNMENT
- Additions: Does the image suggest relationships not in the source?
- Omissions: Does the image hide aspects present in the source?
- Distortions: Does the visual framing change the concept's meaning?

OPERATION 4 - IMPROVEMENT RECOMMENDATIONS
Generate specific, actionable corrections:
- What structural changes are needed?
- What elements should be removed?
- What relationships should be corrected?
</task>

<scoring_rubric>
FIDELITY SCORE (be strict):
- 5: Perfect structural match, no constraint violations, accurate representation
- 4: Minor issues (aesthetic, not structural), no fundamental errors
- 3: One structural error OR one constraint violation, but fixable
- 2: Multiple structural errors OR fundamental misrepresentation
- 1: Completely wrong structure (e.g., parallel shown as nested, architecture shown as process)

EXAMPLES OF SCORE 1-2:
- "NoBIAS Architecture has Legal Layer AND Bias Management Layer" shown as "Stage 1 → Stage 2 → Stage 3" = SCORE 1
- "Three types of bias (parallel)" shown as "nested containers" = SCORE 2
- Adding developmental phases to a static architecture = SCORE 2
</scoring_rubric>

<output_format>
Return a JSON object with these fields:
- fidelity_score: number 1-5 (use the rubric strictly)
- structural_match: boolean (does the structure match the source?)
- constraint_violations: array of strings (which negative constraints were violated)
- issues: array of strings describing problems found
- improvements: array of specific changes to make in regeneration
- keep: array of elements that work well and should be preserved

Return ONLY the JSON object, no additional text or markdown code blocks.
</output_format>

<constraints>
- Be STRICT with scoring—structural errors are fundamental flaws
- Be specific: "change from nested to side-by-side layout" not "improve structure"
- If structural_match is false, fidelity_score must be <= 3
- If any constraint_violations exist, fidelity_score must be <= 3
- Maximum 5 issues and 5 improvements
</constraints>
