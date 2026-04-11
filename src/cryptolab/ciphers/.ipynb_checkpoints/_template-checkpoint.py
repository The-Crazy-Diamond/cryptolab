"""
Cipher plugin template for Cryptolab.

To add a new cipher:
1. Copy this file (with "cp _template.py playfair.py")
2. Rename it (e.g. vigenere.py, playfair.py)
3. Update NAME (should be the same as the filename)
4. Implement encrypt/decrypt
"""

# Unique name used by the CLI
NAME = "_cipher_name"
DESCRIPTION = "_brief description of what is this cipher"


def encrypt(text: str, *args: str) -> str:
    """
    Encrypt the given text using the provided arguments (key(s) and parameters).

    Args:
        text: The plaintext input
        args: Cipher key and/or parameters (format depends on cipher)

    Returns:
        Encrypted text (ciphertext)
    """
    raise NotImplementedError("Encrypt function not implemented")


def decrypt(text: str, *args: str) -> str:
    """
    Decrypt the given text using the provided arguments (key(s) and parameters).

    Args:
        text: The ciphertext input
        args: Cipher key and/or parameters (format depends on cipher)
    Returns:
        Decrypted text (plaintext)
    """
    raise NotImplementedError("Decrypt function not implemented")