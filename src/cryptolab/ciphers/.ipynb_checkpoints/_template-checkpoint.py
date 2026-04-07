"""
Cipher plugin template for Cryptolab.

To add a new cipher:
1. Copy this file (with "cp _template.py playfair.py")
2. Rename it (e.g. vigenere.py, playfair.py)
3. Update NAME (should be the same as the filename whitout the .py extension)
4. Implement encrypt/decrypt
"""

# Unique name used by the CLI
NAME = "_cipher_name"
DESCRIPTION = "brief description of what is this cipher"


def encrypt(text: str, key: str) -> str:
    """
    Encrypt the given text using the provided key.

    Args:
        text: The plaintext input
        key: Cipher key (format depends on cipher)

    Returns:
        Encrypted text (ciphertext)
    """
    raise NotImplementedError("Encrypt function not implemented")


def decrypt(text: str, key: str) -> str:
    """
    Decrypt the given text using the provided key.

    Args:
        text: The ciphertext input
        key: Cipher key (format depends on cipher)

    Returns:
        Decrypted text (plaintext)
    """
    raise NotImplementedError("Decrypt function not implemented")