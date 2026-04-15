"""
Cipher plugin template for Cryptolab.

To add a new cipher:
1. Copy this file (with "cp _template.py your_cipher.py")
2. Rename it (e.g. vigenere.py, playfair.py)
3. Update attributes
4. Implement encrypt/decrypt
"""

NAME = "your_cipher_name" # e.g."caesar"
DESCRIPTION = "brief description of what is this cipher" # e.g."Classic shift cipher (each letter shifted by a fixed amount)"
ARGS_HELP = "list of required arguments: name (type)" # e.g."shift (integer)"
ARGS_EXAMPLE = "example" # e.g."3"


def encrypt(text: str, *args: str) -> str:
    raise NotImplementedError("Encrypt function not implemented")


def decrypt(text: str, *args: str) -> str:
    raise NotImplementedError("Decrypt function not implemented")
