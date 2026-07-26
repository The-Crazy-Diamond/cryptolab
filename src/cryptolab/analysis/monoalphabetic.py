from cryptolab.analysis.ngrams import get_ngrams
from cryptolab.analysis.frequency import get_frequencies
from cryptolab.utils.alphabet import ALPHABET, alphabet
import string

from cryptolab.cli.mono_shell import MonoShell

NAME = "monoalphabetic"
DESCRIPTION = "Tool designed to progressively assign letters assuming that the ciphertext is an encryption using a monoalphabetic substitution"
ARGS_HELP = None
ARGS_EXAMPLE = ""

def analyse(text: str):
    session = MonoSession(text)
    shell = MonoShell(session)
    shell.run()

def initial_mapping() -> dict[str, str]:
    """Return the default substitution mapping.

    Spaces, newlines and punctuation map to themselves.
    Letters are initially unmapped.
    """
    return {c: c for c in " \n" + string.punctuation}

class MonoSession:
    """
    MonoSession is essentially defined by a ciphertext (in uppercases) and a plaintext (in lowercases) progressively determined through a substitution mapping
    """
    
    def __init__(self, ciphertext: str) -> None:
        
        self.ciphertext = ciphertext.upper()
        self.mapping = initial_mapping()   

    @property
    def length(self)-> int:
        return len(self.ciphertext)
            
    @property
    def plaintext(self)-> str:
        return "".join(self.mapping.get(c, '_') for c in self.ciphertext)

    @property
    def cipher_chars_to_assign(self)-> str:
        return ''.join(c for c in ALPHABET if c not in self.mapping.keys())

    @property
    def plain_chars_to_assign(self) -> str:
        return ''.join(c for c in alphabet if c not in self.mapping.values())

    def frequencies(self)-> dict: #not useful since frequencies == ngrams(1)
        return get_frequencies(self.ciphertext)

    def ngrams(self,n: int) :
        return get_ngrams(self.ciphertext, n)
    
    def assign(self, cipher: str, plain: str):
        cipher = cipher.upper()
        plain = plain.lower()
        

        for c, p in self.mapping.items():
            if p == plain and c != cipher:
                raise ValueError(f"'{plain}' is already assigned to '{c}'.")
                
        self.mapping[cipher] = plain

    def reset(self) -> None:
        self.mapping = initial_mapping() 