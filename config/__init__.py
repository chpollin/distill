"""
DISTILL Configuration Module

Contains:
- structure_types: Taxonomie der 12 epistemischen Visualisierungsstile
"""

from .structure_types import (
    STRUCTURE_TYPES,
    get_structure_type,
    get_all_types,
    get_type_by_number,
    get_distinction_criteria,
    suggest_negative_constraints
)

__all__ = [
    "STRUCTURE_TYPES",
    "get_structure_type",
    "get_all_types",
    "get_type_by_number",
    "get_distinction_criteria",
    "suggest_negative_constraints"
]
