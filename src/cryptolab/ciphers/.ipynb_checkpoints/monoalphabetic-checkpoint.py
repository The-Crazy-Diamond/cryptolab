import string

NAME = "monoalphabetic"
DESCRIPTION = "Monoalphabetic substitution with a string and a key word."

def complete_key(key: str) -> str:
    key = key.upper() + string.ascii_uppercase
    return "".join(dict.fromkeys(key))
    
def encrypt(text: str, key: str) -> str:
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
    return ''.join(result)


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
    return ''.join(result)
