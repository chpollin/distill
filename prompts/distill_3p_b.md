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
- Relation: [type] -> [target concept]

## Proposed Concepts
### [Concept Name]
- Definition: [from paper]
- Relation: [type] -> [target concept]

## Utilized Concepts
### [Concept Name]
- Definition: [from paper]
- Relation: [type] -> [target concept]
</output_format>

<input>
{text}
</input>
