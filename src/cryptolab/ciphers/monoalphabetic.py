import string
from cryptolab.utils.text import normalize 

NAME = "monoalphabetic"
DESCRIPTION = "Substitution cipher using a keyword to generate the substitution alphabet"
ARGS_HELP = "keyword (string) used to build substitution alphabet: letters are taken once, remaining alphabet is appended automatically"
ARGS_EXAMPLE = "CRYPTO"  


def complete_key(key: str) -> str:
    key = normalize(key) + string.ascii_uppercase
    return "".join(dict.fromkeys(key))
    
def encrypt(text: str, key: str) -> str:
    text = normalize(text)
    key = complete_key(key)
    substitution = {}
    for i in range(26):
        substitution[chr(i + ord('a'))] = key[i]
    result = []
    for l in text:
        if l.isalpha():
            c = substitution[l.lower()] if l.isupper() else substitution[l].lower()
            result.append(c)
        else:
            result.append(l)
    cipher = ''.join(result)
    return normalize(cipher, remove_accents = True, only_letters = True, upper= True, remove_line_breaks = True)


def decrypt(text: str, key: str) -> str:
    key = complete_key(key)
    substitution = {}
    for i in range(26):
        substitution[key[i]] = chr(i + ord('a'))
    result = []
    for c in text:
        if c.isalpha():
            l = substitution[c].upper() if c.isupper() else substitution[c.upper()]
            result.append(l)
        else:
            result.append(c)
    return ''.join(result).lower()
