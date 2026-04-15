import random
import cryptolab.ciphers.morse as morse
from cryptolab.utils.text import common_chars
NAME = "pollux"
DESCRIPTION = "Pollux cipher first encodes the text using Morse code, then the 3 Morse symbols (Dot, Dash and Space) are substituted with alphanumeric characters via a predefined correspondence table. The algorithm substitutes a Morse symbol with a random character in the correspondance table."
ARGS_HELP = "three distinct keys (string) containing characters which randomly replace dots, dashes and spaces, respectively, after Morse encoding"
ARGS_EXAMPLE = "\"0378AEFMOPQXYZ\" \"145BCGJNRTW\" \"269DHIKLSUV\""


def pollux_keys(text: str, *args: str) -> dict:
    if len(args) != 3:
        raise ValueError("Three keys are required : one for dots, one for dashes and one for spaces")
    if common_chars(*args):
        raise ValueError("Keys must be disjoint")
    keys = {}
    keys['.'] = [c for c in args[0]]
    keys['-'] = [c for c in args[1]]
    keys[' '] = [c for c in args[2]]
    
    return keys

def encrypt(text: str, *args: str) -> str:
    keys = pollux_keys(text, *args)
    
    result = [str(random.choice(keys[c])) for c in morse.encrypt(text) if c != '/'] # Spaces in original text are first encoded into '/' and then ignored in this line.
# It follows that this implementation of pollux does not allow to have spaces in ciphertext. In some sense it is ok as keeping spaces in ciphertexts is less secure.
    return ''.join(result)


def decrypt(text: str, *args: str) -> str:
    keys = pollux_keys(text, *args)
    reverse_keys = {}
    for key in keys['.']:
        reverse_keys[str(key)] = '.'
    for key in keys['-']:
        reverse_keys[str(key)] = '-'
    for key in keys[' ']:
        reverse_keys[str(key)] = ' '
        
    return morse.decrypt(''.join(reverse_keys[c] for c in text))