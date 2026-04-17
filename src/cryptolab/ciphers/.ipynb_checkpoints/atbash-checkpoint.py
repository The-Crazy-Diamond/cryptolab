from cryptolab.ciphers import affine as aff

NAME = "atbash"
DESCRIPTION = "Substitution cipher mapping the alphabet to itself in reverse order. It is a special case of affine cipher with a = b = -1"
ARGS_HELP = None
ARGS_EXAMPLE = ""

#shift: str
def encrypt(text: str) -> str:
    return aff.encrypt(text,-1,-1)


def decrypt(text: str) -> str:
    return encrypt(text)
