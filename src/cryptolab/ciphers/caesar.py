NAME = "caesar"
DESCRIPTION = "Classic shift cipher (each letter shifted by a fixed amount)"
ARGS_HELP = "shift (integer, e.g. 3)"


def encrypt(text: str, key: str) -> str:
    shift = int(key)
    result = []
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result.append(chr((ord(c)-base+shift)%26+base))
        else:
            result.append(c)
    return "".join(result)


def decrypt(text: str, key: str) -> str:
    return encrypt(text, str(-int(key)))