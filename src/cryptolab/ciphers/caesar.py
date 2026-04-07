NAME = "caesar"
DESCRIPTION = "Caesar cipher with a string and an integer as a key"

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