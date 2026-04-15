NAME = "vigenere"
DESCRIPTION = "Classical Vigenère cipher. Polyalphabetic cipher using a repeating keyword"
ARGS_HELP = "keyword (string)"
ARGS_EXAMPLE = "KEY"

# Remark: Vigenere is a special case of polyalphabetic. Code could be refactored.


def encrypt(text: str, key: str) -> str:
    shifts = [ord(c) - ord('A') for c in key.upper()]
    l = len(key)
    index = 0
    result = []
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result.append(chr((ord(c)-base+shifts[index])%26+base))
            index = (index + 1) % l
        else:
            result.append(c)
    return "".join(result)


def decrypt(text: str, key: str) -> str:
    reverse_key = "".join([chr( 26 - (ord(c) - ord('A')) + ord('A')) for c in key.upper()])
    return encrypt(text,reverse_key)
