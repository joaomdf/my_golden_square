from lib.check_codeword import *

def test_response_to_correct_codeword():
    response = check_codeword("horse")
    assert response == "Correct! Come in."

def test_response_to_matching_starting_and_ending_letters():
    response = check_codeword("hide")
    assert response == "Close, but nope."

def test_response_to_wrong_codeword():
    response = check_codeword("swordfish")
    assert response == "WRONG!"