from cryptolab.ui.repl.shell import Shell
from cryptolab.utils.text import add_spaces
from cryptolab.utils.formatting import print_stacked
from cryptolab.analysis.ngrams import get_ngrams, NGRAM_NAMES

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
        self.do_ngrams(1)
        self.status = "Monoalphabetic session initialized."
        

    def build_commands(self):
        commands = super().build_commands()
        commands.update({
            "map": self.do_map,
            "m": self.do_map,
            "unmap": self.do_unmap,
            "u": self.do_unmap,
            "swap": self.do_swap,
            "s": self.do_swap,
            "reset": self.do_reset,
            "r": self.do_reset,
            
            "ngrams": self.do_ngrams,
            "ng": self.do_ngrams,
            "frequencies": partial(self.do_ngrams, 1),
            "freq": partial(self.do_ngrams, 1),
            "bigrams": partial(self.do_ngrams, 2),
            "trigrams": partial(self.do_ngrams, 3),
            "quadgrams": partial(self.do_ngrams, 4),
            
            "show": self.do_show,
            "undo": self.do_undo,
            "redo": self.do_redo,
            # "help": self.do_help, # to implement in Shell ?
    
            "save": self.do_save,
            "load": self.do_load,
        })

        return commands

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
        self.session.assign(cipher,plain)
        self.status = f"Mapped {cipher} -> {plain}"

    def do_unmap(self, cipher):
        self.session.unassign(cipher)
        self.status = f"Unassigned {cipher}"

    def do_swap(self, cipher1, cipher2):
        self.session.swap(cipher1,cipher2)
        self.status = f"Swapped {cipher1} <-> {cipher2}"
    
    def do_reset(self):
        self.session.reset()
        self.status = "Session reset."

    # Analysis commands
    def do_ngrams(self,n:str):
        n = int(n)

        if n in self.visible_ngrams:
            self.visible_ngrams.remove(n)
        else:
            self.visible_ngrams.add(n)
        self.status = None

        if n not in self.ngrams_cache:
            self.ngrams_cache[n] = get_ngrams(self.session.ciphertext, n)
            self.status = f"Cached {NGRAM_NAMES.get(n, f"{n}-grams")}"
            

    # Session commands
    def do_show(self):
        self.status = f"Plaintext: '{self.session.plaintext}'"

    def do_undo(self):
        self.session.undo()
        self.status = "Undo."
    
    def do_redo(self):
        self.session.redo()
        self.status = "Redo."

    # Saving/loading commands
        
    def do_save(self, filename="monoalphabetic.json"):
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
Richer command set:
[x] map X e
[x] unmap X
[X] swap X Q
[X] undo
[X] redo
[x] freq
[x] ngrams n
[x] show
[x] reset
[] save
[] save as solved.txt
[] help
[x] quit

...later:
[] suggest
[] score
[] dictionary
[] auto
"""
