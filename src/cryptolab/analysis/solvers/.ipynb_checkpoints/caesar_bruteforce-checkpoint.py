from cryptolab.ciphers.caesar import decrypt

NAME = "caesar_bruteforce"
DESCRIPTION = "Decrypt a caesar ciphertext by exhausting all possible keys."
ARGS_HELP = None
ARGS_EXAMPLE = ""

def solve(text: str):
    for key in range(26):
        print(f"Key = {key:2} : {decrypt(text, key)}")
