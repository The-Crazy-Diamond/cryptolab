# Not sure that it is correct after the many changes that occured in the project
from cryptolab.ciphers.caesar import encrypt, decrypt


def test_caesar_encrypt():
    assert encrypt("ABC", 3) == "DEF"


def test_caesar_decrypt():
    assert decrypt("DEF", 3) == "ABC"