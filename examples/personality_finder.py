from mtllm.llms import Anthropic
from enum import Enum
from mtllm_python import DefinedVariable, ChainofThoughts

llm = Anthropic(model_name="claude-3-sonnet-20240229")


class Personality(Enum):
    """
    Description: Personality of the Person
    Args:
        INTROVERT: Person who is shy and reticent
        EXTROVERT: Person who is outgoing and socially confident
    """

    INTROVERT = "Introvert"
    EXTROVERT = "Extrovert"


class Person:
    """
    Description: Person
    Args:
        full_name (str): Fullname of the Person
        yod (int): Year of Death
        personality (Personality): Personality of the Person
    """

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
    Description: Get Person Information
    Args:
        name (str): Name of the Person
    Returns:
        (Person): Person
    """
    pass


get_person_info = ChainofThoughts(
    fn=get_person_info, llm=llm, incl_info=(personality_examples)
)


person_obj = get_person_info("Martin Luther King Jr.").result
print(
    f"{person_obj.full_name} was a {person_obj.personality.value} person who died in {person_obj.yod}"
)
