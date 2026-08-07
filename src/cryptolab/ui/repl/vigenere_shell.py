from cryptolab.ui.repl.poly_shell import PolyShell
from cryptolab.analysis.solvers.vigenere.session import VigenereSession
from cryptolab.utils.text import add_spaces
from cryptolab.utils.formatting import print_stacked
from cryptolab.analysis.methods.frequency import get_frequencies
from cryptolab.analysis.methods.kasiski import analyse as kasiski_test
from cryptolab.analysis.methods.coincidence_test import analyse as ioc_test
import json
from pathlib import Path

class VigenereShell(PolyShell):

    TITLE = "Vigenere cipher"
    PROMPT = "vigenere> "
    
    def __init__(self, session: VigenereSession):
        super().__init__(session)
        self.status = "Vigenere session initialized. \n" + self.status
        

    def build_commands(self):
        commands = super().build_commands()
        
        # Remove commands that don't apply
        commands.pop("swap", None)
    
        # Add Vigenère-specific commands
        commands.update({
            "shift": self.do_shift,
            "key": self.do_key,
        })
            
        return commands

    def build_aliases(self):
        aliases = super().build_aliases()
        
        # Remove aliases that don't apply
        aliases.pop("s", None)
    
        # Add Vigenère-specific aliases
        aliases.update({
            "s": "shift",
            "k": "key",
        })

        return aliases

    def display_key_state(self):
        super().display_key_state()
        key = self.session.key
        if key is None:
            key = "undefined"
        print(f"Key = {key}")

    # Modifying commands
    def do_shift(self, shift, key_index = None):
        """
        Assign a shift at every index that are congruent to a key index modulo the key's length.
    
        Usage:
            map <shift> <key_index>
    
        Example:
            map 17 2
        """
        key_index = self.treat_index(key_index)
        shift = int(shift) % 26
        self.session.assign_shift(shift, key_index)
        self.status = f"Set shift to {shift} at indices {key_index} mod {self.session.key_length}"

        
    def do_map(self, cipher, plain, key_index = None):
        """
        Assign a plaintext letter to a ciphertext letter at every index that are congruent to a key index modulo the key's length. The shift will be applied in consequence.
    
        Usage:
            map <cipher> <plain> <key_index>
    
        Example:
            map X e 2
        """
        key_index = self.treat_index(key_index)
        self.session.assign(cipher, plain, key_index)
        self.status = f"Mapped {cipher} -> {plain} at indices {key_index} mod {self.session.key_length}"

    def do_unmap(self, key_index = None):
        """
        Unassign the plaintext letter at every index that are congruent to a key index modulo the key's length.
    
        Usage:
            unmap <key_index>
    
        Example:
            unmap 3
        """
        key_index = self.treat_index(key_index)
        self.session.unassign(key_index)
        self.status = f"Letters unassigned at indices {key_index} mod {self.session.key_length}"
        
    def do_key(self, keyword):
        """
        Set the key of the Vigenere cipher.

        Usage:
            key <keyword>

        Example:
            key CRYPTO
        """
        raise NotImplementedError

    def _cache_frequencies(self, key_index):
        """Ensure frequencies for one key index are cached."""
        if key_index not in self.frequencies_cache:
            subcipher = ("".join([c for c in self.session.ciphertext]))[key_index::self.session.key_length]
            self.frequencies_cache[key_index] = get_frequencies(subcipher)
            return True
        return False
    
    def do_undo(self):
        """
        Undo last command.
    
        Usage:
            undo
        """
        self.session.undo()
        self.status = "Undo."
    
    def do_redo(self):
        """
        Redo previous undone command.
    
        Usage:
            redo
        """
        self.session.redo()
        self.status = "Redo."

    # Saving/loading commands
        
    def do_save(self, filename="polyalphabetic.json"):
        """
        Save the session in a JSON file. (By thefault, filename is "polyalphabetic.json".)
    
        Usage:
            save <filename>
    
        Example:
            save my_session.json
        """
        raise NotImplementedError
        # path = Path(filename)
    
        # if path.exists():
        #     answer = input(f"'{filename}' already exists. Overwrite? [y/N] ")
        #     if answer.lower() not in ("y", "yes"):
        #         self.status = "Save cancelled."
        #         return
    
        # with path.open("w") as f:
        #     json.dump(self.session.to_dict(), f, indent=4)
    
        # self.status = f"Session saved to '{filename}'."
        
    def do_load(self, filename="polyalphabetic.json"):
        """
        Load the session from a JSON file.
    
        Usage:
            load <filename>
    
        Example:
            load polyalphabetic.json
        """
        raise NotImplementedError
        # path = Path(filename)
    
        # if not path.exists():
        #     raise ValueError(f"'{filename}' does not exist.")
    
        # with path.open() as f:
        #     data = json.load(f)

        # if data["analyse_tool"] != "polyalphabetic":
        #     raise ValueError("Not a polyalphabetic session.")
    
        # session = MonoSession(data["ciphertext"])
        # session._mapping = data["mapping"]
    
        # self.session = session
        # self.status = f"Session loaded from '{filename}'."
        
        
    
"""
Commands to add:

[] suggest
[] score
[] dictionary
[] auto
"""
