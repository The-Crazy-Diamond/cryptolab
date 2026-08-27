from cryptolab.utils.alphabet import ALPHABET, alphabet
from cryptolab.utils.text import normalize

import string
    
class Session:
    """
    Session provides the general framework to solve a ciphertext.
    It is defined by a ciphertext (normalized in uppercases and with accents removed) as well as generic properties. 
    """
    TOOL = "undefined"
    def __init__(self, ciphertext: str) -> None:
        self._ciphertext = normalize(ciphertext, remove_accents = True, only_letters = False, upper = True, remove_line_breaks = True) 

        # See later if history and future can be refactored
        # self.history = []
        # self.future = []

    # Getters
    @property
    def ciphertext(self):
        return self._ciphertext    

    # Other properties
    @property
    def length(self)-> int:
        return len(self._ciphertext)

    def compute_plaintext(self) -> str:
        return "???" #Should raise an error "Plaintext cannot be computed for general Session"
        
    @property
    def plaintext(self):
        return self.compute_plaintext()
        
    def reset(self) -> None:
        raise NotImplementedError

    def validate_cipher_char(self, cipher: str):
        cipher = cipher.upper()
        if (cipher not in ALPHABET) or len(cipher) > 1:
            raise ValueError(f"'{cipher}' is not in A-Z.")
        return cipher

    def validate_plain_char(self, plain: str):
        plain = plain.lower()
        if (plain not in alphabet) or len(plain) > 1:
            raise ValueError(f"'{plain}' is not in a-z.")
        return plain

# For the next lines, I need to see if I have a general way of doing things first
    # #Undo/redo methods
    # def checkpoint(self):
    #     self.history.append(self.mapping) # Remember that self.mapping is a property so it already returns a fresh copy
    #     self.future.clear()

    # def undo(self):
    #     if not self.history:
    #         raise ValueError("Nothing to undo.")
    
    #     self.future.append(self.mapping) # same remark as above
    #     self._mapping = self.history.pop()

    # def redo(self):
    #     if not self.future:
    #         raise ValueError("Nothing to redo.")

    #     self.history.append(self.mapping) # same remark as above
    #     self._mapping = self.future.pop()

    # # Save/load methods

    # def to_dict(self):
    #     return {
    #         "analyse_tool": self.TOOL, #metadata
    #         "ciphertext": self._ciphertext,
    #         "mapping": self.mapping,
    #     }