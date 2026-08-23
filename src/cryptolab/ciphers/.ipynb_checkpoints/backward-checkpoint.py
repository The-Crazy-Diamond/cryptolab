from cryptolab.utils.text import normalize

NAME = "backward"
DESCRIPTION = "Reverse the input text"
ARGS_HELP = None
ARGS_EXAMPLE = ""


def encrypt(text: str) -> str:
    cipher = ''.join(reversed(text))
    return normalize(cipher, remove_accents = True, only_letters = True, upper = True, remove_line_breaks = True)

def decrypt(text: str) -> str:
    return encrypt(text).lower()
