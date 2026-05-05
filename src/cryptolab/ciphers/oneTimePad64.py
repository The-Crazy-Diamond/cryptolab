import unicodedata
from cryptolab.utils.text import random_string

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

def normalize64(text: str) -> str: # filter text by remove accent and keeping only base64 characters (A-Z,a-z,0-9,+,/)
    # 1. Remove accents
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    
    # 2. Remove punctuation and spaces (keep only letters)
    text = ''.join(c for c in text if c in BASE64_ALPHABET)
    return text

def random_key(length: int) -> str:
    return random_string(BASE64_ALPHABET,length)

def xor64(s1:str, s2:str) -> str:
    if len(s1) != len(s2):
         raise ValueError("Strings must have same length")
    xor_indices = [b64_index(x) ^ b64_index(y) for x, y in zip(s1, s2)]
    return ''.join(b64_char(i) for i in xor_indices)
     
def common_crypt(text: str, key: str, propose_key: bool = True) -> str:
    if key != normalize64(key):
        raise ValueError("Key must contain only base64 characters (A-Z,a-z,0-9,+,/)")
    text = normalize64(text)
    l_text, l_key = len(text), len(key)
    if propose_key:
        if l_key == 0:
            key = random_key(l_text)
            print("No given key. Random key used :",key)
        elif l_key > l_text:
            key = key[0:l_text]
            print("Too long key. Truncated key used :",key)
        elif l_key < l_text:
            key = key + random_key(l_text - l_key)
            print("Too short key. Randomly completed key used :",key)
    else:
        if l_text != l_key:
            raise ValueError("Key and normalized text must have same length")
    return xor64(text,key)

def encrypt(text: str, key: str = '') -> str:
    return common_crypt(text,key)


def decrypt(text: str, key: str) -> str:
    return common_crypt(text,key,False)
