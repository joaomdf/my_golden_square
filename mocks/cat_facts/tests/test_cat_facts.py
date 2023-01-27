from unittest.mock import Mock
from lib.cat_facts import *


def test_cat_facts():
    mock_requester = Mock()
    mock_response = Mock()
    mock_requester.get.return_value = mock_response
    mock_response.json.return_value = {
        "fact":"A group of cats is called a \u201cclowder.\u201d",
        "length":38
        }
    cat_facts = CatFacts(mock_requester)
    assert cat_facts.provide() == "Cat fact: A group of cats is called a \u201cclowder.\u201d"
