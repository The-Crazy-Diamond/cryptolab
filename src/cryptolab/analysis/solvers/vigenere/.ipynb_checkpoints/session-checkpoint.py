from cryptolab.utils.alphabet import ALPHABET, alphabet
from cryptolab.utils.text import normalize
from cryptolab.analysis.solvers.polyalphabetic.session import PolySession
from cryptolab.analysis.solvers.monoalphabetic.session import MonoSession
                    
class VigenereSession(PolySession):
    """
    VigenereSession is essentially defined by a ciphertext (in uppercases) and a plaintext (in lowercases) progressively determined through substitution mappings after finding the key length. 
    """
    TOOL = "vigenere"
        
    def __init__(self, ciphertext: str) -> None:
        super().__init__(ciphertext)
        # self.history = []
        # self.future = []
        
    def _init_key_state(self):
        self._shifts = {}
        
    # Getters    
    def get_mono_session(self, key_index):
        raise NotImplementedError(
            "VigenereSession uses shifts instead of monoalphabetic sessions."
        )
        
    def get_shift(self, key_index):
        return self._shifts[key_index]

    
    @property
    def plaintext(self):
        out = []
        letter_index = 0
    
        for c in self._ciphertext:
            if c.isalpha():
                if self.key_length_defined:
                    shift = self._shifts[letter_index % self.key_length]
                    if shift is None:
                        out.append('_')
                    else:
                        # Work the shift with alphabet indices
                        index = ord(c) - ord('A')
                        new_index = (index - shift) % 26
                        out.append( chr(ord('a') + new_index) ) # using decrypt from ciphers.caesar would be an idea
                else:
                    out.append('_')
                letter_index += 1
            else:
                out.append(c)
        return "".join(out)

    @property
    def key(self):
        if self.key_length_defined:
            out = []
            for shift in self._shifts.values():
                if shift is not None:
                    out.append(chr(ord('A') + shift))
                else:
                    out.append('?')
            return "".join(out)
        else:
            return None
    
    # Setters
    def set_key_state(self, key_length: int):
        for i in range(key_length):
            self._shifts[i] = None

    # Modifying methods
    def assign_shift(self, shift: int, key_index: int):
        shift = shift % 26
        self._shifts[key_index] = shift
        
    def assign(self, cipher: str, plain: str, key_index: int):
        self.key_length_check()
        
        # 1. Validate
        cipher = cipher.upper()
        plain = plain.lower()

        if (cipher not in ALPHABET) or len(cipher) > 1:
            raise ValueError(f"'{cipher}' is not in A-Z.")
        
        if (plain not in alphabet) or len(plain) > 1:
            raise ValueError(f"'{plain}' is not in a-z.")
    
        # 2. Save current state        
        # self.checkpoint()
        
        # 3. Modify state
        shift_start = ord(plain) - ord('a')
        shift_end = ord(cipher) - ord('A')
        self.assign_shift(shift_end - shift_start, key_index)        
        

    def unassign(self, key_index: int):
        self.key_length_check()

        # 1. Validate
        # nothing to do
        # 2. Save current state    
        # self.checkpoint()
        
        # 3. Modify state
        self,_shifts[key_index] = None

    def swap(self, *args, **kwargs):
        raise NotImplementedError(
            "swap() is not supported for VigenereSession."
        )

    def reset_key_state(self):
        self._shifts = {}
    
    # #Undo/redo methods
    def checkpoint(self):
        raise NotImplementedError('Checkpoint not implemented.')
    #     self.history.append(self.mapping) # Remember that self.mapping is a property so it already returns a fresh copy
    #     self.future.clear()

    def undo(self):
        raise NotImplementedError(('Undo not implemented.'))
    #     if not self.history:
    #         raise ValueError("Nothing to undo.")
    
    #     self.future.append(self.mapping) # same remark as above
    #     self._mapping = self.history.pop()

    def redo(self):
        raise NotImplementedError('Redo not implemented.')
    #     if not self.future:
    #         raise ValueError("Nothing to redo.")

    #     self.history.append(self.mapping) # same remark as above
    #     self._mapping = self.future.pop()

    # # Save/load methods

    def to_dict(self):
        raise NotImplementedError('Function not implemented.')
    #     return {
    #         "analyse_tool": self.TOOL, #metadata
    #         "ciphertext": self._ciphertext,
    #         "mapping": self.mapping,
    #     }


