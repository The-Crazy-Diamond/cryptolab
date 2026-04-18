import unicodedata

NAME = "oneTimePad64"
DESCRIPTION = "One-time pad cipher (version for strings written in base64 characters)"
ARGS_HELP = "optional key (string) with same length as normalized text"
ARGS_EXAMPLE = "De69/S3k+rT"

"""
The goal of this cipher is to have a first approach of OTP but keeping it simple by resticting to base64 characters (A-Z,a-z,0-9,+,/)
Features ideas:
- Add option to generate random key
"""

###  The following could be moved to a utils file that could be name mybase64
BASE64_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
BASE64_MAP = {c: i for i, c in enumerate(BASE64_ALPHABET)}

def b64_index(c: str) -> int:
    if c == '=':
        raise ValueError("Padding '=' has no index")
    try:
        return BASE64_MAP[c]
    except KeyError:
        raise ValueError(f"Invalid Base64 character: {c}")

def b64_char(i: int) -> str:
    if not (0 <= i < 64):
        raise ValueError("Index must be in range 0–63")
    return BASE64_ALPHABET[i]

def xor64(s1:str, s2:str) -> str:
    if len(s1) != len(s2):
         raise ValueError("Strings must have same length")
    xor_indices = [b64_index(x) ^ b64_index(y) for x, y in zip(s1, s2)]
    return ''.join(b64_char(i) for i in xor_indices)

def normalize64(text: str) -> str: # filter text by remove accent and keeping only base64 characters (A-Z,a-z,0-9,+,/)
    # 1. Remove accents
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    
    # 2. Remove punctuation and spaces (keep only letters)
    text = ''.join(c for c in text if c in BASE64_ALPHABET)
    
    return text
###

def encrypt(text: str, key: str) -> str:
    if key != normalize64(key):
        raise ValueError("Key must contain only base64 characters (A-Z,a-z,0-9,+,/)")
    text = normalize64(text)
    if len(text) != len(key):
        raise ValueError("Key and normalized text must have same length")
    return xor64(text,key)


def decrypt(text: str, key: str) -> str:
    return encrypt(text,key)
