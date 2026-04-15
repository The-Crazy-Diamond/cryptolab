import cryptolab.ciphers.monoalphabetic as mono
from cryptolab.utils.text import normalize
from itertools import zip_longest

NAME = "polyalphabetic"
DESCRIPTION = "Substitution cipher working like monoalphabetic but using several substitution alphabets used in loop"
ARGS_HELP = "keywords (strings used to build substitution alphabets: letters are taked once, remaining alphabet is appended automatically)"
ARGS_EXAMPLE = "\"CRYPTO\" \"SECRET\" \"PASSWORD\""


def polyalphabetic_common(func, text: str, *keys: str) -> str:
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

    return ''.join(result)

def encrypt(text: str, *keys: str) -> str:
    return polyalphabetic_common(mono.encrypt, text, *keys)
 

def decrypt(text: str, *keys: str) -> str:
    return polyalphabetic_common(mono.decrypt, text, *keys)

