"""
Cipher plugin template for Cryptolab.

To add a new cipher:
1. Copy this file (with "cp _template.py your_cipher.py")
2. Rename it (e.g. vigenere.py, playfair.py)
3. Update attributes
4. Implement encrypt/decrypt
"""

NAME = "your_cipher_name"
DESCRIPTION = "brief description of what is this cipher"
ARGS_HELP = "list of required arguments: name (type)"
ARGS_EXAMPLE = "example"

# As an example:
# NAME = "caesar"
# DESCRIPTION = "Classic shift cipher (each letter shifted by a fixed amount)"
# ARGS_HELP = "shift (integer)"
# ARGS_EXAMPLE = "3"


def encrypt(text: str, *args: str) -> str:
    raise NotImplementedError("Encrypt function not implemented")


def decrypt(text: str, *args: str) -> str:
    raise NotImplementedError("Decrypt function not implemented")
