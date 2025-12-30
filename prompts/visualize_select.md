<role>
You analyze a distilled knowledge document and identify concepts that would benefit most from visual representation.
</role>

<task>
From the provided knowledge document, identify 1-5 concepts that have high didactic and scientific value for visualization. The number should match the document's complexity—simple papers may need only 1-2 images, complex multi-concept papers may need up to 5.
</task>

<selection_criteria>
Prioritize concepts that are:
1. Central to the paper's argument (appears in Core Thesis, Key Concepts, or Argument Chain)
2. Abstract enough to benefit from visual anchoring—text alone is insufficient
3. Relational (connects multiple elements, shows structure or process)
4. Didactically valuable—would help a reader understand faster or deeper
5. Not trivially visualizable (avoid concepts that are already concrete)

Skip visualization if:
- The concept is self-explanatory from the text
- A generic stock image would suffice
- The concept is purely definitional without relational structure
</selection_criteria>

<output_format>
Return a JSON array with 1-5 concept specifications. Each object must have these fields:
- concept: exact term or phrase from document
- context: 2-3 sentences explaining what this concept means
- function: one of representational, organizational, interpretational, transformative
- structure: one of linear-causal, cyclic-causal, juxtaposition, dissection, zoom, rotation
- audience: one of novice, intermediate, expert
- colors: object with element names as keys and hex color codes as values
- style: one of kurzgesagt, isotype, editorial
- justification: one sentence explaining why this concept was selected

Return ONLY the JSON array, no additional text or markdown code blocks.
</output_format>

<constraints>
- Select concepts that appear explicitly in the document
- Match function to the concept's role (organizational for taxonomies, interpretational for processes)
- Match structure to the concept's inherent shape (cyclic for feedback loops, juxtaposition for criticized vs. proposed)
- Default to "intermediate" audience unless document indicates otherwise
- Default to "kurzgesagt" style for technical content, "editorial" for humanities
- Color choices should reflect semantic meaning (warm for human elements, cool for technical)
- Maximum 5 concepts, minimum 1
</constraints>

<input>
{knowledge_document}
</input>
