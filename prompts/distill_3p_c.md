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
{text}
</input>
