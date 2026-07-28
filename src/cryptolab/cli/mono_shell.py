import shlex
import json
from pathlib import Path
from cryptolab.utils.text import add_spaces, modify_string
from cryptolab.utils.formatting import clear_screen, print_stacked
from functools import partial
from cryptolab.analysis.ngrams import get_ngrams

class MonoShell:
    def __init__(self, session: MonoSession):
        self.session = session
        self.running = True
        self.visible_ngrams = set()
        self.ngrams_cache = {}
        self.NGRAM_NAMES = {
            1: "Frequencies",
            2: "Bigrams",
            3: "Trigrams",
            4: "Quadgrams",
        }
        self.do_ngrams(1)
        self.status = None
        self.commands = {
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
            "help": self.do_help,
            "quit": self.do_quit,
            "q": self.do_quit,

            "save": self.do_save,
            "load": self.do_load,
        }

    
    # REPL running methods
    def run(self):
        self.display()
    
        while self.running:
            command = input("mono> ").strip()
            self.execute(command)
    
    def execute(self, command: str):
        self.status = None
        if not command:
            self.display()
            return
        
        parts = shlex.split(command)
        
        cmd = parts[0]
        args = parts[1:]
    
        func = self.commands.get(cmd)
        
        if func is None:
            self.status = f"Unknown command: {cmd}."
            self.display()
            return
        try:
            func(*args)
        except TypeError:
            self.status = f"Invalid arguments for '{cmd}'."
        except ValueError as e:
            self.status = str(e)

        self.display()

    def display(self):
        clear_screen()
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
            name = self.NGRAM_NAMES.get(n, f"{n}-grams")
            print(f"{name}: {self.ngrams_cache[n]}")

        if self.status is not None:
            print()
            print(self.status)

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
            self.status = f"Cached {self.NGRAM_NAMES.get(n, f"{n}-grams")}"
            

    # Session commands
    def do_show(self):
        self.status = f"Plaintext: '{self.session.plaintext}'"

    def do_undo(self):
        self.session.undo()
        self.status = "Undo."
    
    def do_redo(self):
        self.session.redo()
        self.status = "Redo."

    def do_help(self):
        raise NotImplementedError("Helper not implemented")    
         
    def do_quit(self):
        self.status = "Goodbye!"
        self.running = False

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
