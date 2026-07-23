import shlex
from cryptolab.utils.text import add_spaces, modify_string
from cryptolab.utils.formatting import clear_screen, print_stacked

class MonoShell:
    def __init__(self, session: MonoalphabeticSession):
        self.session = session
        self.running = True
        self.ngrams_to_show = {1}
        self.commands = {
            "show": self.do_show,
            "map": self.do_map,
            "freq": self.do_freq,
            "ngrams": self.do_ngrams,
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
        if not command:
            self.display()
            return
    
        
        parts = shlex.split(command)
        cmd = parts[0]
        args = parts[1:]
    
        func = self.commands.get(cmd)
    
        if func is None:
            print(f"Unknown command: {cmd}.")
            return
    
        try:
            func(*args)
        except TypeError:
            print(f"Invalid arguments for '{cmd}'.")
        self.display()

    def display(self):
        clear_screen()
        print_stacked(add_spaces(self.session.ciphertext), add_spaces(self.session.plaintext))
        print('\nUnassigned ciphertext characters: ', add_spaces(''.join(self.session.cipher_chars_to_map)))
        print('\nUnassigned plaintext characters: ',add_spaces(''.join(self.session.plain_chars_to_map)),'\n')
        for n in self.ngrams_to_show:
            if n == 1:
                ngram_name = 'Frequencies'
            elif n == 2:
                ngram_name = 'Bigrams'
            elif n == 3:
                ngram_name = 'Trigrams'
            elif n == 4:
                ngram_name = 'Quadgrams'
            else:
                ngram_name = str(n)+'-grams'
            print(ngram_name+': ', self.session.ngrams(n)) 

    

    def do_show(self):
        # do nothing because the method execute will call display
        self.running = True
    
    def do_map(self, cipher, plain):
        self.session.map(cipher,plain)
        
    def do_freq(self):
        self.do_ngrams(1)

    def do_ngrams(self,n):
        if n in self.ngrams_to_show:
            self.ngrams_to_show.remove(n)
        else:
            self.ngrams_to_show.add(n)
            
    def do_reset(self):
        self.session.reset()

    def do_help(self):
        clear_screen()
        print('Type two characters to make a substitution, e.g. \'Rg\' will map every \'R\' with \'g\'.')
        print('Type \'ngram\' INT to (un)show ngram with n = INT')
        print('Type \'reset\' to reset the solving.')
        print('Type \'quit\' to quit.')
        input('Type enter to continue.')
        
         
    def do_quit(self):
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