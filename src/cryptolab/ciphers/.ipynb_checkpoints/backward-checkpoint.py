NAME = "backward"
DESCRIPTION = "Backward permutation"


def encrypt(text: str, key: str) -> str: #no key is needed
    return ''.join(reversed(text))

def decrypt(text: str, key: str) -> str:
    return encrypt(text, key)