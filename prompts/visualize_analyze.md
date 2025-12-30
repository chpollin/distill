<role>
Analyze a scientific visualization for epistemic fidelity and suggest specific improvements.
</role>

<input>
## Image
{image}

## Source Concept
{concept}

## Context
{context}

## Intended Parameters
- Function: {function}
- Structure: {structure}
- Audience: {audience}
</input>

<task>
Perform three analytical operations and generate actionable feedback.

OPERATION 1 - STRUCTURAL CHECK
Verify the visualization matches the intended structure:
- Does the layout match the specified structure type?
- Is the reading direction clear?
- Are the key elements properly emphasized?

OPERATION 2 - EPISTEMIC ALIGNMENT
Compare visualization to source concept:
- Fidelity: Does the image accurately represent the concept?
- Additions: Does the image suggest relationships not in the source?
- Omissions: Does the image hide aspects present in the source?
- Distortions: Does the visual framing change the concept's meaning?

OPERATION 3 - IMPROVEMENT RECOMMENDATIONS
Generate specific, actionable corrections:
- What should be added to improve accuracy?
- What should be removed or de-emphasized?
- What visual metaphors should be changed?
</task>

<output_format>
Return a JSON object with these fields:
- fidelity_score: number 1-5 (5 = perfect match, 1 = major distortions)
- issues: array of strings describing problems found
- improvements: array of specific changes to make in regeneration
- keep: array of elements that work well and should be preserved

Return ONLY the JSON object, no additional text or markdown code blocks.
</output_format>

<constraints>
- Be specific: "add arrow from A to B" not "improve flow"
- Focus on epistemic accuracy, not aesthetic preferences
- Maximum 5 issues and 5 improvements
- If fidelity_score >= 4, improvements array can be empty
</constraints>
