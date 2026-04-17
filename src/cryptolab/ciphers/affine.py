import math

NAME = "affine"
DESCRIPTION = "Affine cipher. Each letter x seen as its index in the alphabet (from 0 to 25) is mapped to ax + b mod 26."
ARGS_HELP = "two keys a,b (integers) such that gcd(a,26) = 1 (to ensure that the encryption is invertible)"
ARGS_EXAMPLE = "7 13"

def get_keys(key_a: str, key_b: str):
    a = int(key_a)
    b = int(key_b)
    
    if math.gcd(a,26) != 1:
        raise ValueError("Key 'a' must be coprime with 26")
    return a,b

def encrypt(text: str, key_a: str, key_b: str) -> str:
    a,b = get_keys(key_a, key_b)
    result = []
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result.append(chr((a*(ord(c)-base)+b)%26+base))
        else:
            result.append(c)
    return "".join(result)


def decrypt(text: str, key_a: str, key_b: str) -> str:
    a,b = get_keys(key_a, key_b)
    a_inv = pow(a, -1, 26)
    
    text2 = encrypt(text, 1, -b) # first be shift by -b
    return encrypt(text2, a_inv, 0) # then we multiply by a^(-1)
