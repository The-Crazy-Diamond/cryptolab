from cryptolab.utils.alphabet import ALPHABET, alphabet
from cryptolab.utils.text import normalize
from cryptolab.analysis.solvers.session import Session

import string


def initial_mapping() -> dict[str, str]:
    """
    Return the default substitution mapping.
    """
    return {}
    # return {c: c for c in " \n" + string.punctuation}

    
class MonoSession(Session):
    """
    Tool to decipher a monoalphabetic ciphertext by determining progressively the mapping.
    """
    TOOL = "monoalphabetic"
    def __init__(self, ciphertext: str) -> None:
        super().__init__(ciphertext)
        self._mapping = initial_mapping()
        self.history = []
        self.future = []

    # Getters
        
    @property
    def mapping(self):
        return self._mapping.copy()

    # Other properties
            
    def get_plain_char(self, c):
        if c in self._mapping:
            return self._mapping[c]
        elif c in ALPHABET:
            return "_"
        else:
            return c
        
    def compute_plaintext(self) -> str:
        # return "".join(self._mapping.get(c, '_') for c in self._ciphertext)
        out = []
    
        for c in self._ciphertext:
            out.append(self.get_plain_char(c))
    
        return "".join(out)

    @property
    def cipher_chars_to_assign(self)-> str:
        return ''.join(c for c in ALPHABET if (c in self._ciphertext) and (c not in self._mapping.keys()))

    @property
    def plain_chars_to_assign(self) -> str:
        return ''.join(c for c in alphabet if c not in self._mapping.values())

     
    # Modifying methods
    def assign(self, cipher: str, plain: str):
        # 1. Validate
        cipher = self.validate_cipher_char(cipher)
        plain = self.validate_plain_char(plain)   
        
        for c, p in self._mapping.items():
            if p == plain and c != cipher:
                raise ValueError(f"'{plain}' is already assigned to '{c}'.")
        # 2. Save current state        
        self.checkpoint()
        # 3. Modify state
        self._mapping[cipher] = plain

    def unassign(self, cipher: str):
        # 1. Validate
        cipher = self.validate_cipher_char(cipher)
        if cipher not in self._mapping:
            raise ValueError(f"'{cipher}' is not assigned yet.")
        # 2. Save current state    
        self.checkpoint()
        # 3. Modify state
        self._mapping.pop(cipher)

    def swap(self, cipher1: str, cipher2: str):
        # 1. Validate
        cipher1 = cipher1.upper()
        cipher2 = cipher2.upper()
        for cipher in [cipher1,cipher2]:
            cipher = self.validate_cipher_char(cipher)
            if cipher not in self._mapping:
                raise ValueError(f"'{cipher}' is not assigned yet.")
        # 2. Save current state
        self.checkpoint()
        # 3. Modify state
        self._mapping[cipher1], self._mapping[cipher2] = (
            self._mapping[cipher2],
            self._mapping[cipher1],
        )                
        
    def reset(self) -> None:
        # 1. Validate
        # nothing to do
        # 2. Save current state
        self.checkpoint()
        # 3. Modify state
        self._mapping = initial_mapping()

    #Undo/redo methods
    def checkpoint(self):
        self.history.append(self.mapping) # Remember that self.mapping is a property so it already returns a fresh copy
        self.future.clear()

    def undo(self):
        if not self.history:
            raise ValueError("Nothing to undo.")
    
        self.future.append(self.mapping) # same remark as above
        self._mapping = self.history.pop()

    def redo(self):
        if not self.future:
            raise ValueError("Nothing to redo.")

        self.history.append(self.mapping) # same remark as above
        self._mapping = self.future.pop()

    # Save/load methods

    def to_dict(self):
        return {
            "analyse_tool": self.TOOL, #metadata
            "ciphertext": self._ciphertext,
            "mapping": self.mapping,
        }