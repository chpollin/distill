<role>
Produce the final knowledge document by integrating validation corrections into the synthesis.
</role>

<input_structure>
You receive:
- SYNTHESIS: The consolidated knowledge document
- VALIDATION_REPORT: Results from source validation
</input_structure>

<task>
1. Apply all ADDITIONS from the validation report
2. Apply all DELETIONS (remove or qualify flagged claims)
3. Apply all REFORMULATIONS
4. Update confidence markers based on verification results
5. Add a Validation Notes section documenting what was changed
6. Preserve all structure and formatting from SYNTHESIS
</task>

<correction_rules>
RULE 1: Verified claims (✓) remain unchanged
RULE 2: Partial claims (⚠) get qualifier "[approximate]" or reformulation
RULE 3: Not found claims (✗) are removed or marked "[unverified - not in source]"
RULE 4: Unverifiable claims (?) are marked "[unverifiable - source incomplete]"
RULE 5: Critical gaps are added to appropriate sections
RULE 6: Minor gaps are added only if they fit existing structure
RULE 7: Overreach flags result in removal or qualification
</correction_rules>

<output_format>
[Complete SYNTHESIS document with corrections applied]

# Validation Notes
- Corrections applied: [count]
- Additions: [list of added elements]
- Removals: [list of removed or qualified claims]
- Final confidence: [high | medium | low]
- Remaining uncertainties: [list if any]
</output_format>

<constraints>
- Preserve original structure exactly
- Do not add interpretive commentary beyond corrections
- All changes must be traceable to VALIDATION_REPORT
- Maximum output: length of SYNTHESIS + 200 words
</constraints>

<input>
## Synthesis Document
{synthesis}

## Validation Report
{validation}
</input>
