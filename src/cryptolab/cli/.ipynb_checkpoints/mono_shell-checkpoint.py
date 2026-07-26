import shlex
from cryptolab.utils.text import add_spaces, modify_string
from cryptolab.utils.formatting import clear_screen, print_stacked
from functools import partial

class MonoShell:
    def __init__(self, session: MonoSession):
        self.session = session
        self.running = True
        self.visible_ngrams = {1}
        self.status = None
        self.commands = {
            "show": self.do_show,
            "map": self.do_map,
            
            "ngrams": self.do_ngrams,
            "freq": partial(self.do_ngrams, 1),
            "bigrams": partial(self.do_ngrams, 2),
            "trigrams": partial(self.do_ngrams, 3),
            "quadgrams": partial(self.do_ngrams, 4),
            
            "reset": self.do_reset,
            "help": self.do_help,
            "quit": self.do_quit,
        }

    
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

        NGRAM_NAMES = {
            1: "Frequencies",
            2: "Bigrams",
            3: "Trigrams",
            4: "Quadgrams",
        }
        
        for n in sorted(self.visible_ngrams):
            name = NGRAM_NAMES.get(n, f"{n}-grams")
            print(f"{name}: {self.session.ngrams(n)}")

        if self.status is not None:
            print()
            print(self.status)

    def do_show(self):
        self.status = None
    
    def do_map(self, cipher, plain):
        self.session.assign(cipher,plain)
        self.status = f"Mapped {cipher} -> {plain}"

    def do_ngrams(self,n:str):
        n = int(n)
        if n in self.visible_ngrams:
            self.visible_ngrams.remove(n)
        else:
            self.visible_ngrams.add(n)
        self.status = None
            
    def do_reset(self):
        self.session.reset()
        self.status = "Session reset."

    def do_help(self):
        raise NotImplementedError("Helper not implemented")    
         
    def do_quit(self):
        self.status = "Goodbye!"
        self.running = False
    
"""
Richer command set:
map X e
unmap X
swap X Q
undo
redo
freq
ngrams 2
ngrams 3
show
reset
save
save as solved.txt
help
quit

...later:
suggest
score
dictionary
auto
"""
