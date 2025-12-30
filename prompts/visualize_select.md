<role>
You analyze a distilled knowledge document and identify concepts that would benefit most from visual representation. You select the optimal epistemic structure type from a systematic taxonomy of 12 visualization styles.
</role>

<task>
From the provided knowledge document, identify 1-5 concepts that have high didactic and scientific value for visualization. The number should match the document's complexity—simple papers may need only 1-2 images, complex multi-concept papers may need up to 5.

For each concept, determine the most appropriate STRUCTURE TYPE from the taxonomy below. This is critical for generating accurate visualizations.
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
- context: 2-3 sentences explaining what this concept means IN THE PAPER'S TERMS
- relations: array of strings describing how this concept connects to other concepts in the document
- structure_type: one of the 12 types from taxonomy (sequence, quantity, hub, decomposition, transformation, grouping, scale, contrast, stratigraphy, spiral, network, uncertainty)
- structure_type_reasoning: one sentence explaining WHY this type was chosen over similar alternatives
- structure: one of linear-causal, cyclic-causal, juxtaposition, parallel, nested, network (for backwards compatibility)
- visual_type: one of architecture (layered systems), taxonomy (categories), process (flow), contrast (vs comparison), network (connections)
- negative_constraints: array of things that must NOT be shown (e.g., "no temporal sequence", "not nested")
- source_quote: one verbatim quote from the document that defines this concept
- audience: one of novice, intermediate, expert
- style: one of kurzgesagt, isotype, editorial
- justification: one sentence explaining why this concept was selected

Return ONLY the JSON array, no additional text or markdown code blocks.
</output_format>

<structure_type_taxonomy>
Select ONE structure_type from these 12 epistemic visualization styles:

| ID | Type | Shows | Use When |
|----|------|-------|----------|
| sequence | Linear Phase Sequence | Equal-value steps, workflows | Processes with equivalent phases, no transformation |
| quantity | Pictographic Comparison | Proportions, distributions | Comparing amounts across categories |
| hub | Hub Structure | Center with dependent elements | One dominant core with peripheral associations |
| decomposition | Component Breakdown | Parts of a whole | System architecture, what consists of what |
| transformation | Metamorphosis | Qualitative change over time | Learning, development, paradigm shifts |
| grouping | Gestalt Clustering | Categories, similarities | Typologies, classifications, segments |
| scale | Anti-Sublime | Overwhelming quantities | Corpus sizes, making the incomprehensible graspable |
| contrast | Rhetorical Opposition | Dichotomies, before/after | Two states in tension, explicit comparisons |
| stratigraphy | Temporal Layering | Historical epochs, sediment | Accumulated time, phases building on each other |
| spiral | Iterative Cycle | Recurring phases with growth | Agile methods, learning cycles, iterations |
| network | Constellation | Connections without center | Actor networks, citations, relationships |
| uncertainty | Epistemic Blur | Hypotheses, fuzzy boundaries | Uncertain knowledge, overlapping categories |

CRITICAL DISTINCTIONS:
- sequence vs transformation: Equal steps vs. qualitative change (use transformation if output differs fundamentally from input)
- sequence vs spiral: One-time vs. recurring phases
- hub vs network: One dominant center vs. no/multiple centers
- decomposition vs hub: Part-whole vs. associated domains
- grouping vs network: Category membership vs. relationships
- quantity vs scale: Countable proportions vs. overwhelming mass
</structure_type_taxonomy>

<structure_guide>
CRITICAL: Match structure to what the document ACTUALLY says:
- parallel: Elements exist side-by-side without containment (e.g., "Legal Layer AND Bias Management Layer")
- nested: One element contains another (e.g., "Bias Management Layer WITHIN Legal Layer")
- linear-causal: A leads to B leads to C (temporal or causal sequence)
- cyclic-causal: Feedback loop where C influences A
- juxtaposition: Explicit contrast between two approaches (e.g., "criticized vs. proposed")
- network: Multiple interconnected elements without clear hierarchy

DO NOT assume nested structures unless the document explicitly states containment.
DO NOT assume temporal sequences unless the document describes a process over time.
</structure_guide>

<constraints>
- Select concepts that appear explicitly in the document
- The context field must use the paper's own terminology, not generic descriptions
- The relations field must reference OTHER concepts from the same document
- The negative_constraints field must prevent common visualization errors
- Default to "intermediate" audience unless document indicates otherwise
- Default to "kurzgesagt" style for technical content, "editorial" for humanities
- Maximum 5 concepts, minimum 1
</constraints>

<input>
{knowledge_document}
</input>
