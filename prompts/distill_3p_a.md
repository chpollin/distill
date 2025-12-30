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
1. [step] ->
2. [step] ->
3. [conclusion]

## Evidence
- [type]: [specific content]
...

## Concessions
- [limitation or counterargument]
...
</output_format>

<input>
{text}
</input>
