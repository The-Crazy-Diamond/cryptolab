from cryptolab.ui.repl.shell import Shell
from cryptolab.analysis.solvers.monoalphabetic.session import MonoSession
from cryptolab.utils.text import add_spaces
from cryptolab.utils.formatting import print_stacked
from cryptolab.analysis.methods.ngrams import get_ngrams, NGRAM_NAMES

import json
from pathlib import Path
from functools import partial

class MonoShell(Shell):

    TITLE = "Monoalphabetic substitution"
    PROMPT = "mono> "
    def __init__(self, session: MonoSession):
        super().__init__()
        self.session = session
        self.visible_ngrams = set()
        self.ngrams_cache = {}
        self.status = "Monoalphabetic session initialized. \n" + self.status
        

    def build_commands(self):
        commands = super().build_commands()
        commands.update({
            "map": self.do_map,
            "unmap": self.do_unmap,
            "swap": self.do_swap,
            "reset": self.do_reset,
            
            "ngrams": self.do_ngrams,
            "frequencies": self.do_frequencies,
            "bigrams": self.do_bigrams,
            "trigrams": self.do_trigrams,
            "quadgrams": self.do_quadgrams,
            
            "show": self.do_show,
            "undo": self.do_undo,
            "redo": self.do_redo,
    
            "save": self.do_save,
            "load": self.do_load,
        })

        return commands

    def build_aliases(self):
        aliases = super().build_aliases()
        aliases.update({
            "m": "map",
            "u": "unmap",
            "s": "swap",
            "r": "reset",
            
            "ng": "ngrams",
            "freq": "frequencies",
        })

        return aliases

    def display_content(self):
        print_stacked(
            add_spaces(self.session.ciphertext),
            add_spaces(self.session.plaintext),
        )
        
        print(
            '\nUnassigned ciphertext characters: ',
              add_spaces(''.join(self.session.cipher_chars_to_assign)),
        )
        print(
            '\nUnassigned plaintext characters: ',
            add_spaces(''.join(self.session.plain_chars_to_assign)),'\n',
        )
        
        for n in sorted(self.visible_ngrams):
            name = NGRAM_NAMES.get(n, f"{n}-grams")
            print(f"{name}: {self.ngrams_cache[n]}")

    # Modifying commands
    def do_map(self, cipher, plain):
        """
        Assign a plaintext letter to a ciphertext letter.
    
        Usage:
            map <cipher> <plain>
    
        Example:
            map X e
        """
        self.session.assign(cipher,plain)
        self.status = f"Mapped {cipher} -> {plain}"

    def do_unmap(self, cipher):
        """
        Unassign the plaintext letter of a ciphertext letter.
    
        Usage:
            unmap <cipher>
    
        Example:
            unmap X
        """
        self.session.unassign(cipher)
        self.status = f"Unassigned {cipher}"

    def do_swap(self, cipher1, cipher2):
        """
        Swap two existing assignments.
    
        Usage:
            swap <cipher1> <cipher2>
    
        Example:
            swap X Y
        """
        self.session.swap(cipher1,cipher2)
        self.status = f"Swapped {cipher1} <-> {cipher2}"
    
    def do_reset(self):
        """
        Reset the session.
    
        Usage:
            reset
        """
        self.session.reset()
        self.status = "Session reset."

    # Analysis commands
    def do_ngrams(self,n:str):
        """
        Toggle the display of n-grams.
    
        Usage:
            ngrams <n>
    
        Example:
            ngrams 2
        """
        n = int(n)

        if n in self.visible_ngrams:
            self.visible_ngrams.remove(n)
        else:
            self.visible_ngrams.add(n)
        self.status = None

        if n not in self.ngrams_cache:
            self.ngrams_cache[n] = get_ngrams(self.session.ciphertext, n)
            self.status = f"Cached {NGRAM_NAMES.get(n, f"{n}-grams")}"
            
    def do_frequencies(self):
        """
        Toggle the display of letter frequencies.
        
        Usage:
            frequencies
        """

        
        self.do_ngrams(1)
    
    def do_bigrams(self):
        """
        Toggle the display of bigrams.
        
        Usage:
            bigrams
        """
        self.do_ngrams(2)
    
    def do_trigrams(self):
        """
        Toggle the display of trigrams.
        
        Usage:
            trigrams
        """
        self.do_ngrams(3)
    
    def do_quadgrams(self):
        """
        Toggle the display of quadgrams.
        
        Usage:
            quadgrams
        """
        self.do_ngrams(4)
            

    # Session commands
    def do_show(self):
        """
        Print the current plaintext state.
    
        Usage:
            show
        """
        self.status = f"Plaintext: '{self.session.plaintext}'"

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
        
    def do_save(self, filename="monoalphabetic.json"):
        """
        Save the session in a JSON file. (By thefault, filename is "monoalphabetic.json".)
    
        Usage:
            save <filename>
    
        Example:
            save my_session.json
        """
        path = Path(filename)
    
        if path.exists():
            answer = input(f"'{filename}' already exists. Overwrite? [y/N] ")
            if answer.lower() not in ("y", "yes"):
                self.status = "Save cancelled."
                return
    
        with path.open("w") as f:
            json.dump(self.session.to_dict(), f, indent=4)
    
        self.status = f"Session saved to '{filename}'."
        
    def do_load(self, filename="monoalphabetic.json"):
        """
        Load the session from a JSON file.
    
        Usage:
            load <filename>
    
        Example:
            load monoalphabetic.json
        """
        path = Path(filename)
    
        if not path.exists():
            raise ValueError(f"'{filename}' does not exist.")
    
        with path.open() as f:
            data = json.load(f)

        if data["analyse_tool"] != "monoalphabetic":
            raise ValueError("Not a monoalphabetic session.")
    
        session = MonoSession(data["ciphertext"])
        session._mapping = data["mapping"]
    
        self.session = session
        self.status = f"Session loaded from '{filename}'."
        
        
    
"""
Commands to add:

[] suggest
[] score
[] dictionary
[] auto
"""
