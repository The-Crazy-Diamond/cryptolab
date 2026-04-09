NAME = "backward"
DESCRIPTION = "Backward permutation"


def encrypt(text: str) -> str:
    return ''.join(reversed(text))

def decrypt(text: str) -> str:
    return encrypt(text)