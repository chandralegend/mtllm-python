"""Building blocks for creating the functions, variables and classes for the MTLLM."""

from typing import Any, Callable, Optional, get_type_hints

from mtllm.llms.base import BaseLLM
from mtllm.tools.base import Tool

from mtllm_python.aott import with_llm
from mtllm_python.utils import Method, get_semstrings


class Function:
    """Function that uses the specified method to generate the output."""

    def __init__(
        self,
        fn: Callable,
        llm: BaseLLM,
        incl_info: Optional[list] = None,
        method: str = "Normal",
        tools: Optional[list[Tool]] = None,
        types_needed: Optional[list] = None,
        **kwargs: dict,
    ) -> None:
        """Initializes the Function object."""
        self.fn = fn
        self.llm = llm
        self.incl_info = incl_info
        self.method = method
        self.tools = tools
        self.types_needed = types_needed
        self.kwargs = kwargs

    def _get_semantic_info(self) -> dict:
        """Returns the semantic information of the function."""
        doc_string = self.fn.__doc__
        type_hints = get_type_hints(self.fn)
        sem_info = {
            "description": self.fn.__name__,
            "inputs": [
                {
                    "name": arg,
                    "type": type_hints.get(arg, type(None)).__name__,
                    "semstr": "",
                }
                for arg in self.fn.__code__.co_varnames
            ],
            "output": {
                "type": type_hints.get("return", type(None)).__name__,
                "semstr": "",
            },
        }
        # adding semantic information from docstring
        if doc_string:
            semstrings = get_semstrings(doc_string)
            if semstrings["description"]:
                sem_info["description"] = semstrings["description"]
            if semstrings["inputs"]:
                print(semstrings["inputs"])
                for arg in sem_info["inputs"]:
                    arg["semstr"] = semstrings["inputs"].get(arg["name"], "")
            if semstrings["output"]:
                sem_info["output"]["semstr"] = semstrings["output"]
        return sem_info

    def __call__(self, *args: list, **kwargs: dict) -> Any:
        """Calls the function with the specified arguments."""
        sem_info = self._get_semantic_info()
        return with_llm(
            self.llm, self.method, self.tools, sem_info, self.incl_info, *args, **kwargs
        )

    def _validate_input(self, *args: list, **kwargs: dict) -> bool:
        """Validates the input arguments."""
        pass


class Class:
    """Class that uses the specified method to generate the output."""

    def __init__(
        self,
        cls: Any,
        llm: BaseLLM,
        incl_info: Optional[list] = None,
        method: Method = Method.Normal,
        tools: Optional[list[Tool]] = None,
        types_needed: Optional[list] = None,
        **kwargs: dict,
    ) -> None:
        """Initializes the Class object."""
        self.cls = cls
        self.llm = llm
        self.incl_info = incl_info
        self.method = method
        self.tools = tools
        self.types_needed = types_needed
        self.kwargs = kwargs

    def _get_semantic_info(self) -> dict:
        """Returns the semantic information of the class."""
        doc_string = self.cls.__doc__
        type_hints = get_type_hints(self.cls.__init__)
        sem_info = {
            "description": "",  # replace with the class initialization action
            "inputs": [
                {
                    "name": arg,
                    "type": type_hints.get(arg, type(None)).__name__,
                    "semstr": "",
                }
                for arg in self.cls.__init__.__code__.co_varnames
                if arg != "self"
            ],
            "output": {
                "type": self.cls.__name__,
                "semstr": "",
            },
        }
        # adding semantic information from docstring
        if doc_string:
            semstrings = get_semstrings(doc_string)
            if semstrings["inputs"]:
                for arg in sem_info["inputs"]:
                    arg["semstr"] = semstrings["inputs"].get(arg["name"], "")
            sem_info["output"]["semstr"] = semstrings["description"]
        return sem_info

    def __call__(self, *args: list, **kwargs: dict) -> Any:
        """Calls the class with the specified arguments."""
        sem_info = self._get_semantic_info()
        return with_llm(
            self.llm, self.method, self.tools, sem_info, self.incl_info, *args, **kwargs
        )


class DefinedVariable:
    """DefinedVariable object that contains the structured information of the variable."""

    def __init__(self, var: Any, desc: str) -> None:
        """Initializes the DefinedVariable object."""
        self.value = var
        self.desc = desc
        self.name = self.get_variable_name(var)
        self.type = self.get_type(var)

    def get_type(self, var: Any) -> str:
        """Returns the type of the variable."""
        pass

    def get_variable_name(self, var: Any) -> str:
        """Returns the name of the variable."""
        pass

    def __str__(self) -> str:
        """Returns the string representation of the variable."""
        return f"{self.desc} ({self.get_variable_name}) ({self.get_type}) = {str(self.value)}"

    def get_special_types(self) -> list[str]:
        """Returns the special types used in the variable."""
        pass
