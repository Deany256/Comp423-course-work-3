import pytest
from email_validation import (
    creating_an_answer,
    is_valid_email,
    extract_user,
    spotting_word,
)


@pytest.mark.parametrize(
    "email,domain,expected",
    [
        ("fred@pop.ac.uk", "pop.ac.uk", True),
        ("fred@pop.ac.uk", "unipop.ac.uk", False),
        ("@pop.ac.uk", "pop.ac.uk", False),
        ("f@pop.ac.uk", "pop.ac.uk", False),
        ("fred.at.ac.uk", "pop.ac.uk", False),
    ],
)
def test_is_valid_email(email, domain, expected):
    assert is_valid_email(email, domain) == expected


@pytest.mark.parametrize(
    "email,expected", [("fred@pop.ac.uk", "fred"), ("freddi@pop.ac.uk", "freddi")]
)
def test_extract_user(email, expected):
    assert extract_user(email) == expected


@pytest.mark.parametrize(
    "user_input,keywords,expected",
    [
        ("hello", ["quit", "exit", "end"], False),
        ("quit", ["quit", "exit", "end"], True),
        ("ending", ["quit", "exit", "end"], False),
        ("hello can we quit now", ["quit", "exit", "end"], True),
    ],
)
def test_spotting_word(user_input, keywords, expected):
    assert spotting_word(user_input, keywords) == expected


@pytest.mark.parametrize(
    "user_input,keywords,responses,expected",
    [("hello", ["quit", "hello"], {"hello": "Hello George"}, "Hello George")],
)
def test_creating_an_answer(user_input, keywords, responses, expected):
    assert creating_an_answer(user_input, keywords, responses) == expected
