from typing import List
from random import choice, randint


def random_string(l: List[str]) -> str:
    """Function that when passed a non-empty list of strings returns a random string from the list.

    Args:
        l (List[str]): None empty list of strings.

    Returns:
        str: Random string from l.
    """
    return choice(l)


def is_valid_email(email: str, domain: str) -> bool:
    """Checks if a given string could plausibly be an email address at a particular domain.

    Args:
        email (str): Any string.
        domain (str): Email domain after the "@".

    Returns:
        bool: representing whether string is valid email for domain.
    """
    # The address must contain exactly one @ character
    if email.count("@") != 1:
        return False

    # The @ character must have at least two characters before it
    if email.index("@") < 2:
        return False

    # The characters after the @ character must be the domain (the other parameter), and nothing else.
    # NOTE safe to assume list will be of length 2
    if email.split("@")[1] != domain:
        return False

    return True


# NOTE safe to assume username can be extracted
def extract_user(email: str) -> str:
    """Takes an email address and returns the left-hand part of it.

    Args:
        email (str): Any string.

    Returns:
        str: String containing hypothetical name.
    """
    return email.split("@")[0]


def spotting_word(user_input: str, keywords: List[str]) -> bool:
    """Checks input string for key words and end program if detected.

    Args:
        user_input (str): Non-empty string.

    Returns:
        bool: Returns True to quit the program.
    """
    if set(keywords) & set(user_input.split()):
        return True
    else:
        return False

    # return any(x in user_input for x in keywords)


def creating_an_answer(user_input: str, keywords: List[str], responses: dict) -> str:
    """assuming this function comes after the spotting_word function

    Args:
        user_input (str): Non-empty string.
        keywords (List[str]): list of words to search for
        responses (dict): dictionary of responses to words within keywords list

    Returns:
        str: Returns a string
    """
    keywords = set(keywords)
    user_input = set(user_input.split())
    return responses[(user_input & keywords).pop()]


def select_random_number(minimum: int, maximum: int) -> bool:
    """Selects random number within range and return True if selected number matches minimum

    Args:
        minimum (int): Minimum number for range
        maximum (int): Maximum number for range

    Returns:
        bool: returns True if random number matches minimum
    """
    if randint(minimum, maximum) == minimum:
        return True
    else:
        return False
