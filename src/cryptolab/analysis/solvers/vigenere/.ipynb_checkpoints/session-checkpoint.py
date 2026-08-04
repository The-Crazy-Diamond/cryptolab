from cryptolab.utils.alphabet import ALPHABET, alphabet
from cryptolab.utils.text import normalize
from cryptolab.analysis.solvers.polyalphabetic.session import PolySession

import string


def initial_mapping() -> dict[str, str]:
    """
    Return the default substitution mapping.
    """
    return {}
    # return {c: c for c in " \n" + string.punctuation}

def vigenere_get_system(cipher,key_length, coincidence_threshold = 0.05):
    # yields system as in p.86 ... to improve
    subciphers = [("".join(cipher[i] for i in range(len(cipher)) if i % key_length == j)) for j in range(key_length)]
    for j in range(key_length):
        for i in range(j):
            for g in range(26):
                MI = mutual_index_of_coincidence(subciphers[i],shift(subciphers[j],g))
                if MI > coincidence_threshold:
                    print("k_" + str(i) + " - " + "k_" + str(j)+ " = " + str(g) + "   (MI = " + str(MI) + ")")

                    
class VigenereSession(PolySession):
    """
    MonoSession is essentially defined by a ciphertext (in uppercases) and a plaintext (in lowercases) progressively determined through a substitution mapping
    """
    TOOL = "monoalphabetic"
    def __init__(self, ciphertext: str) -> None:
        
        self.ciphertext = normalize(ciphertext, remove_accents = True, only_letters = False, upper = True) 
        self._mapping = initial_mapping()
        self.history = []
        self.future = []
        
    @property
    def mapping(self):
        return self._mapping.copy()
    
    @property
    def length(self)-> int:
        return len(self.ciphertext)
            
    
    @property
    def plaintext(self):
        # return "".join(self._mapping.get(c, '_') for c in self.ciphertext)
        out = []
    
        for c in self.ciphertext:
            if c in self._mapping:
                out.append(self._mapping[c])
            elif c in ALPHABET:
                out.append("_")
            else:
                out.append(c)
    
        return "".join(out)

    @property
    def cipher_chars_to_assign(self)-> str:
        return ''.join(c for c in ALPHABET if c not in self._mapping.keys())

    @property
    def plain_chars_to_assign(self) -> str:
        return ''.join(c for c in alphabet if c not in self._mapping.values())

    # Modifying methods
    def assign(self, cipher: str, plain: str):
        # 1. Validate
        cipher = cipher.upper()
        plain = plain.lower()

        if (cipher not in ALPHABET) or len(cipher) > 1:
            raise ValueError(f"'{cipher}' is not in A-Z.")
        
        if (plain not in alphabet) or len(plain) > 1:
            raise ValueError(f"'{plain}' is not in a-z.")
    
        for c, p in self._mapping.items():
            if p == plain and c != cipher:
                raise ValueError(f"'{plain}' is already assigned to '{c}'.")
        # 2. Save current state        
        self.checkpoint()
        # 3. Modify state
        self._mapping[cipher] = plain

    def unassign(self, cipher: str):
        # 1. Validate
        cipher = cipher.upper() 
        if (cipher not in ALPHABET) or len(cipher) > 1:
            raise ValueError(f"'{cipher}' is not in A-Z.")
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
            if (cipher not in ALPHABET) or len(cipher) > 1:
                raise ValueError(f"'{cipher}' is not in A-Z.")
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
            "ciphertext": self.ciphertext,
            "mapping": self.mapping,
        }


