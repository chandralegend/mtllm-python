"""Utility functions for the MTLLM."""

import re
from enum import Enum


class Method(Enum):
    """Enum class for the methods used in the MTLLM."""

    Normal = "Normal"
    ChainOfThoughts = "Chain-of-Thoughts"
    BasicReasoning = "Reason"
    ReAct = "ReAct"


def get_semstrings(docstring: str) -> dict:
    """Extracts the semantic information from the docstring."""
    docstring = docstring.strip()

    description_match = re.match(
        r"^(?!Inputs:)(.+?)(?:\n\s*Inputs:|\n\s*Output:)", docstring, re.DOTALL
    )
    description = description_match.group(1).strip() if description_match else ""

    inputs_match = re.search(r"Inputs:(.*?)(?:\n\s*Output:|\Z)", docstring, re.DOTALL)
    inputs_section = inputs_match.group(1).strip() if inputs_match else ""

    inputs = {}
    if inputs_section:
        input_matches = re.finditer(
            r"(\w+):\s*((?:(?!\n\s*\w+:).)*)", inputs_section, re.DOTALL
        )
        for match in input_matches:
            input_name = match.group(1)
            input_desc = re.sub(r"\s+", " ", match.group(2)).strip()
            inputs[input_name] = input_desc

    return_match = re.search(r"Output:(.*)", docstring, re.DOTALL)
    return_value = return_match.group(1).strip() if return_match else ""

    result = {
        "description": description,
        "inputs": inputs,
        "output": return_value,
    }
    return result
