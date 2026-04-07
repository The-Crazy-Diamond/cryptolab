"""
Cipher plugin template for Cryptolab.

To add a new cipher:
1. Copy this file (with "cp _template.py playfair.py")
2. Rename it (e.g. vigenere.py, playfair.py)
3. Update NAME (should be the same as the filename whitout the .py extension)
4. Implement encrypt/decrypt
"""

# Unique name used by the CLI
NAME = "vigenere"
DESCRIPTION = "Vigenère cipher with a string and a word as a key"


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