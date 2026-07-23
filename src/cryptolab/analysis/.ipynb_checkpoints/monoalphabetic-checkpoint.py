from cryptolab.analysis.ngrams import get_ngrams
from cryptolab.analysis.frequency import get_frequencies
from cryptolab.utils.alphabet import ALPHABET, alphabet
import string

from cryptolab.cli.mono_shell import MonoShell

NAME = "monoalphabetic"
DESCRIPTION = "Tool designed to progressively map letters assuming that the ciphertext is an encryption using a monoalphabetic substitution"
ARGS_HELP = None
ARGS_EXAMPLE = ""

def analyse(text: str):
    session = MonoalphabeticSession(text)
    shell = MonoShell(session)
    shell.run()

INITIAL_MAPPING = {c:c  for c in ' ' + string.punctuation +'\n'} # space and punctuation char maps to themselves

class MonoalphabeticSession:
    """
    MonoalphabeticSession is essentially defined by a ciphertext (in uppercases) and a plaintext (in lowercases) progressively determined through a substitution mapping
    """
    
    def __init__(self, ciphertext: str) -> None:
        
        self.ciphertext = ciphertext.upper()
        self.mapping = INITIAL_MAPPING # {'A': 'e', ...}            

    @property
    def length(self)-> int:
        return len(self.ciphertext)
            
    @property
    def plaintext(self)-> str:
        return "".join(self.mapping.get(c, '_') for c in self.ciphertext)

    @property
    def cipher_chars_to_map(self)-> str:
        return ''.join(c for c in ALPHABET if c not in self.mapping.keys())

    @property
    def plain_chars_to_map(self) -> str:
        return ''.join(c for c in alphabet if c not in self.mapping.values())

    def frequencies(self)-> dict:
        return get_frequencies(self.ciphertext)

    def ngrams(self,n: int) :
        return get_ngrams(self.ciphertext, n)
    
    def map(self, c, p) -> None:
        self.mapping[c] = p

    def reset(self) -> None: # to refactor
        self.ciphertext = ciphertext.upper()
        self.mapping = INITIAL_MAPPING # {'A': 'e', ...}  
