from cryptolab.utils.alphabet import ALPHABET, alphabet
from cryptolab.utils.text import normalize
from cryptolab.analysis.solvers.monoalphabetic.session import MonoSession
import string
                    
class PolySession:
    """
    PolySession is essentially defined by a ciphertext (in uppercases) and a plaintext (in lowercases) progressively determined through substitution mappings after finding the key length. 
    """
    TOOL = "polyalphabetic"
    def __init__(self, ciphertext: str) -> None:
        self._ciphertext = normalize(ciphertext, remove_accents = True, only_letters = False, upper = True)
        self._key_length = None
        self._mono_sessions = {}
        # self.history = []
        # self.future = []
        
    # Getters    
    @property
    def ciphertext(self):
        return self._ciphertext
        
    @property
    def key_length(self)-> int:
        if self.key_length_defined:
            return self._key_length
        else:
            return None

    @property
    def mono_sessions(self)-> int:
        return self._mono_sessions.copy()

    # Other properties
    @property
    def length(self)-> int:
        return len(self._ciphertext)
            
    @property
    def plaintext(self):
        if self.key_length_defined:
            out = []
            for index in range(self.length):
                out.append(self._mono_sessions[index % self._key_length].get_plain_char(self._ciphertext[index]))
            return "".join(out)
        else:
            return MonoSession(self._ciphertext).plaintext
            
    @property
    def key_length_defined(self):
        return self._key_length != None
        
    def key_length_check(self):
        if not self.key_length_defined:
            raise ValueError(f"Key's length is not defined. Cannot perform operation.")

    # Key length setting method
    def set_key_length(self, key_length: int):
        self._key_length = key_length
        pure_ciphertext = normalize(self._ciphertext, remove_accents = True, only_letters = True, upper = True)
        for k in range(key_length):
            self._mono_sessions[k] = MonoSession(pure_ciphertext[k::key_length])


    # Modifying methods
    def assign(self, cipher: str, plain: str, key_index: int):
        self.key_length_check()
        self._mono_sessions[key_index].assign(cipher, plain)
        
        # # 1. Validate
        # cipher = cipher.upper()
        # plain = plain.lower()
        # # 2. Save current state        
        # self.checkpoint()
        # # 3. Modify state
        # self._mapping[cipher] = plain

    def unassign(self, cipher: str, key_index: int):
        self.key_length_check()
        self._mono_sessions[key_index].unassign(cipher)
        
        # # 1. Validate
        # cipher = cipher.upper() 
        # if (cipher not in ALPHABET) or len(cipher) > 1:
        #     raise ValueError(f"'{cipher}' is not in A-Z.")
        # if cipher not in self._mapping:
        #     raise ValueError(f"'{cipher}' is not assigned yet.")
        # # 2. Save current state    
        # self.checkpoint()
        # # 3. Modify state
        # self._mapping.pop(cipher)

    def swap(self, cipher1: str, cipher2: str, key_index: int):
        self.key_length_check()
        self._mono_sessions[key_index].swap(cipher1, cipher2)

        
        # # 1. Validate
        # cipher1 = cipher1.upper()
        # cipher2 = cipher2.upper()
        # for cipher in [cipher1,cipher2]:
        #     if (cipher not in ALPHABET) or len(cipher) > 1:
        #         raise ValueError(f"'{cipher}' is not in A-Z.")
        #     if cipher not in self._mapping:
        #         raise ValueError(f"'{cipher}' is not assigned yet.")
        # # 2. Save current state
        # self.checkpoint()
        # # 3. Modify state
        # self._mapping[cipher1], self._mapping[cipher2] = (
        #     self._mapping[cipher2],
        #     self._mapping[cipher1],
        # )                
        
    def reset(self) -> None:
        self._key_length = None
        self._mono_sessions = {}
    #     # 1. Validate
    #     # nothing to do
    #     # 2. Save current state
    #     self.checkpoint()
    #     # 3. Modify state
    #     self._mapping = initial_mapping()

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


