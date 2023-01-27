from lib.greet import *

def test_if_prints_Joao_in_greeting():
    greeting = greet("Joao")
    assert greeting == "Hello, Joao!"