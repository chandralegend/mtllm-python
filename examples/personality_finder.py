from mtllm.llms import OpenAI
from enum import Enum
from mtllm_python import DefinedVariable, Method, Function, Class

llm = OpenAI()


class Personality(Enum):
    """Personality of a Person."""

    INTROVERT = "Introvert"
    EXTROVERT = "Extrovert"


class Person:
    def __init__(self, full_name: str, yod: int, personality: Personality):
        self.full_name = full_name
        self.yod = yod
        self.personality = personality


personality_examples = {
    "Albert Einstein": Personality.INTROVERT,
    "Barack Obama": Personality.EXTROVERT,
}
personality_examples = DefinedVariable(
    personality_examples, "Personality Information of Famous People"
)


def get_person_info(name: str) -> Person:
    """
    Get Person Information
    Inputs:
        name: Name of the Person
    Output: Person Object
    """
    pass


get_person_info = Function(
    get_person_info,
    llm,
    [personality_examples],
    Method.ChainOfThoughts,
    types_needed=[Person, Personality],
)
person_obj = get_person_info("Martin Luther King Jr.")
print(person_obj)

_Person = Class(Person, llm)
person_obj = _Person("Mahatma Gandhi")
print(person_obj)
