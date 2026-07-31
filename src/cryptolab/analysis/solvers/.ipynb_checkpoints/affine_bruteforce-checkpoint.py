from cryptolab.ciphers.affine import decrypt

NAME = "affine_bruteforce"
DESCRIPTION = "Decrypt an affine ciphertext by exhausting all possible keys, with an optional likely word"
ARGS_HELP = None
ARGS_EXAMPLE = ""

def solve(text: str, guess: str = ''):
    for key_a in range(26):
        for key_b in range(26):
            try:
                plaintext = decrypt(text, key_a,key_b)
                if guess in plaintext:
                    print(f"Key pair = ({key_a:2},{key_b:2}) : {plaintext}")
            except ValueError:
                pass
