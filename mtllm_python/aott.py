"""AOTT module of MTLLM."""

from typing import Any, Optional

from mtllm.llms.base import BaseLLM
from mtllm.tools.base import Tool


def with_llm(
    llm: BaseLLM,
    method: str,
    tools: Optional[list[Tool]],
    sem_info: dict,
    incl_info: Optional[list] = None,
    *args: list,
    **kwargs: dict,
) -> Any:
    """Calls the LLM with the specified arguments."""
    print(sem_info)
    print(incl_info)
    print(args)
    print(kwargs)
    return "something"
