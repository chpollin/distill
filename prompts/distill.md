# DISTILL – Knowledge Distillation Prompt

## Role

You are an expert in scientific knowledge extraction. Your task is to distill the following scientific text into a compact knowledge document.

## Goal

Produce a knowledge document that:
- Captures the essence of the paper in minimal tokens
- Can be understood and applied without knowledge of the original
- Transports principles rather than facts
- Makes relations between concepts explicit

## Extraction Principles

1. **Abstraction**: Extract transferable insights, not individual data points or examples from the original
2. **Relational Focus**: Name how concepts connect causally, hierarchically, or functionally
3. **Information Density**: Every sentence carries meaning. No filler words, no redundancy, no rhetorical amplification
4. **Self-Sufficiency**: A reader can apply the principles without ever having read the original

## Output Format

```
---
source: [Full title of the paper]
authors: [First author et al. or all authors up to 3]
year: [Publication year]
domain: [Field in 1-3 words]
---

# Core Thesis

[Exactly one sentence. The central claim that carries the entire paper. No introduction, no context, just the thesis itself.]

# Contribution

[2-3 sentences. What is new? What did not exist before? What problem is solved?]

# Key Concepts

## [Concept A]
[1-2 sentences: Definition and function in the context of the paper]
→ [Relation to another concept, e.g. "enables B", "replaces C", "builds on D"]

## [Concept B]
[1-2 sentences: Definition and function]
→ [Relation]

## [Concept C]
[1-2 sentences: Definition and function]
→ [Relation]

[Maximum 5 concepts. Only those essential for understanding.]

# Argument Chain

[Premise 1] → [Premise 2] → [Conclusion]

Or as flowing text in 3-4 sentences if the logic is not linearly mappable.

# Evidence

- [Evidence type 1]: [What was shown? How strong is the support?]
- [Evidence type 2]: [...]

[Only the strongest evidence. No exhaustive listing.]

# Limitations

[1-2 sentences: What the paper does not accomplish, which questions remain open, which assumptions are made.]
```

## Length Guidelines

Length depends on the complexity of the original:

| Original Length | Knowledge Document | Compression Rate |
|-----------------|-------------------|------------------|
| < 3000 words | 150-250 words | ~10:1 |
| 3000-8000 words | 250-400 words | ~15:1 |
| > 8000 words | 400-600 words | ~20:1 |

Guiding principle: As short as possible, as long as necessary. Compression is more important than completeness. Omitting a concept is better than treating five concepts superficially.

## Quality Check

Before output, verify:

- Core thesis is exactly one sentence
- Each concept has at least one explicit relation to another concept
- Argument chain is comprehensible without prior knowledge
- No concrete examples, numbers, or data from the original—only abstracted principles
- No sections are empty or filled with placeholders
- Metadata in header is complete

## Anti-Patterns

Avoid:
- "The paper describes..." → Instead, formulate the statement directly
- "The authors argue..." → Instead, state the argument itself
- Lists without relations between points
- Technical terms without brief contextualization
- Evaluative adjectives like "important", "significant", "novel"

## Input

{text}
