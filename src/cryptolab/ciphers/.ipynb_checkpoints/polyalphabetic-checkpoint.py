import cryptolab.ciphers.monoalphabetic as mono
from itertools import zip_longest

NAME = "polyalphabetic"
DESCRIPTION = "Substitution cipher working like monoalphabetic but using several substitution alphabets used in loop"
ARGS_HELP = "keywords (strings used to build substitution alphabets: letters are taked once, remaining alphabet is appended automatically)"
ARGS_EXAMPLE = "\"CRYPTO\" \"SECRET\" \"PASSWORD\""

def polyalphabetic_common(func, text: str, *keys: str) -> str:
    if not keys:
        raise ValueError("At least one key is required")
    
    n = len(keys)
    results = [func(text[i::n],keys[i]) for i in range(n)]
    
    return ''.join(char for group in zip_longest(*results, fillvalue='') for char in group)


def encrypt(text: str, *keys: str) -> str:
    return polyalphabetic_common(mono.encrypt, text, *keys)
 

def decrypt(text: str, *keys: str) -> str:
    return polyalphabetic_common(mono.decrypt, text, *keys)

