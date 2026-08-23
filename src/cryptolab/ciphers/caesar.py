from cryptolab.utils.text import normalize

NAME = "caesar"
DESCRIPTION = "Classic shift cipher (each letter shifted by a fixed amount)"
ARGS_HELP = "shift (integer)"
ARGS_EXAMPLE = "3"


def encrypt(text: str, key: str) -> str:
    text = normalize(text, remove_accents = True, only_letters = False, upper = False, remove_line_breaks = True)
    shift = int(key)
    result = []
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result.append(chr((ord(c)-base+shift)%26+base))
        else:
            result.append(c)
    cipher = "".join(result)
    return normalize(cipher, remove_accents = True, only_letters = True, upper = True, remove_line_breaks = True)


def decrypt(text: str, key: str) -> str:
    return encrypt(text, str(-int(key))).lower()
