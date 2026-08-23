import cryptolab.ciphers.monoalphabetic as mono
from cryptolab.utils.text import normalize
from itertools import zip_longest

NAME = "polyalphabetic"
DESCRIPTION = "Substitution cipher working like monoalphabetic but using several substitution alphabets used in loop"
ARGS_HELP = "keywords (strings) used to build substitution alphabets: letters are taken once, remaining alphabet is appended automatically"
ARGS_EXAMPLE = "\"CRYPTO\" \"SECRET\" \"PASSWORD\""


def polyalphabetic_core(func, text: str, *keys: str) -> str:
    text = normalize(text, remove_accents = True, only_letters = False, upper = False, remove_line_breaks = True)
    if not keys:
        raise ValueError("At least one key is required")

    n = len(keys)

    # 1. Extract normalized letters only
    letters = [normalize(c,False) for c in text if c.isalpha()]

    # 2. Apply cipher on letters only
    processed = [func(''.join(letters[i::n]), keys[i]) for i in range(n)]

    # 3. Rebuild transformed letters (interleave)
    transformed_letters = ''.join(char for group in zip_longest(*processed, fillvalue='') for char in group)

    # 4. Reinsert into original text
    result = []
    letter_index = 0

    for c in text:
        if c.isalpha():
            result.append(transformed_letters[letter_index])
            letter_index += 1
        else:
            result.append(c)

    result_text = ''.join(result)
    return normalize(result_text, remove_accents = True, only_letters = True, upper = True, remove_line_breaks = True)

def encrypt(text: str, *keys: str) -> str:
    return polyalphabetic_core(mono.encrypt, text, *keys)
 

def decrypt(text: str, *keys: str) -> str:
    return polyalphabetic_core(mono.decrypt, text, *keys).lower()

