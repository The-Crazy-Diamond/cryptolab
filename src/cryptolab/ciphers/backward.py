NAME = "backward"
DESCRIPTION = "Reverse the input text"
ARGS_HELP = None
ARGS_EXAMPLE = ""


def encrypt(text: str) -> str:
    return ''.join(reversed(text))

def decrypt(text: str) -> str:
    return encrypt(text)
