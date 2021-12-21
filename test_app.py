import pytest
from app import is_valid_email, random_string


# def test_random_string():

#     l = ["hi", "my", "name"]
#     expected = "my"
#     result = random_string(l)

#     assert result == expected

testdata = [
    ("fred@pop.ac.uk", "pop.ac.uk", True),
    ("fred@pop.ac.uk", "unipop.ac.uk", False),
    ("@pop.ac.uk", "pop.ac.uk", False),
    ("f@pop.ac.uk", "pop.ac.uk", False),
    ("fred.at.ac.uk", "pop.ac.uk", False),
]


@pytest.mark.parametrize("email,domain,expected", testdata)
def test_is_valid_email(email, domain, expected):
    assert is_valid_email(email, domain) == expected
