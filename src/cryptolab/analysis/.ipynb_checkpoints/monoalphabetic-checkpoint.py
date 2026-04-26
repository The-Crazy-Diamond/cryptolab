from cryptolab.analysis.ngrams import get_ngrams
from cryptolab.analysis.frequency import get_frequencies
from cryptolab.utils.alphabet import ALPHABET, alphabet
from cryptolab.utils.text import add_spaces, modify_string
from cryptolab.utils.formatting import clear_screen, print_stacked
from cryptolab.utils.collections import toggle_number
import string

NAME = "monoalphabetic"
DESCRIPTION = "Tool designed to progressively substitute letters assuming that the ciphertext is an encryption using a monoalphabetic substitution"
ARGS_HELP = None
ARGS_EXAMPLE = ""


def analyse(text: str):
    mono = MonoalphabeticSubstititionDecoder(text)
    solve(mono)

INITIAL_MAPPING = {c:c  for c in ' ' + string.punctuation +'\n'} # space and punctuation char maps to themselves

class MonoalphabeticSubstititionDecoder:
    """
    MonoalphabeticSubstititionDecoder is essentially defined by a ciphertext (in uppercases) and a plaintext (in lowercases) progressively determined through a substitution mapping
    """
    
    
    def __init__(self, ciphertext: str) -> None:
        
        self.ciphertext = ciphertext.upper()
        self.mapping = INITIAL_MAPPING # {'A': 'e', ...}            
        
    def __str__(self) -> str:
        raise NotImplementedError

    @property
    def length(self)-> int:
        return len(self.ciphertext)
            
    @property
    def plaintext(self)-> str:
        return "".join(self.mapping.get(c, '_') for c in self.ciphertext)

    @property
    def cipher_chars_to_substitute(self)-> str:
        return ''.join(c for c in ALPHABET if c not in self.mapping.keys())

    @property
    def plain_chars_to_substitute(self) -> str:
        return ''.join(c for c in alphabet if c not in self.mapping.values())

    def frequencies(self)-> dict:
        return get_frequencies(self.ciphertext)

    def ngrams(self,n: int) :
        return get_ngrams(self.ciphertext, n)
    
    def substitute(self, c, p) -> None:
        self.mapping[c] = p

    def reset(self) -> None: # to refactor
        self.ciphertext = ciphertext.upper()
        self.mapping = INITIAL_MAPPING # {'A': 'e', ...}  

def mono_display(mono: MonoalphabeticSubstititionDecoder, ngrams_to_show = [1]) -> None:
    clear_screen()
    print_stacked(add_spaces(mono.ciphertext), add_spaces(mono.plaintext))
    print('\nUnassigned ciphertext characters: ', add_spaces(''.join(mono.cipher_chars_to_substitute)))
    print('\nUnassigned plaintext characters: ',add_spaces(''.join(mono.plain_chars_to_substitute)),'\n')
    for n in sorted(ngrams_to_show):
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
        print(ngram_name+': ', mono.ngrams(n))   
            
def solve(mono: MonoalphabeticSubstititionDecoder) -> None:
    # INITIAL STATE
    ngrams_to_show = [1]
    mono_display(mono,ngrams_to_show)
    should_continue = True
    while should_continue:
        command = input('Enter command:\n')
        if len(command) > 0:
            if command == 'help':
                clear_screen()
                print('Type two characters to make a substitution, e.g. \'Rg\' will substitute every \'R\' with \'g\'.')
                print('Type \'ngram\' INT to (un)show ngram with n = INT')
                print('Type \'reset\' to reset the solving.')
                print('Type \'quit\' to quit.')
                input('Type enter to continue.')
                mono_display(mono,ngrams_to_show)
            elif command in ['quit','exit']:
                should_continue = False
            elif command == 'reset':
                mono.reset()
                mono_display(mono,ngrams_to_show)
            elif command in ['freq','frequency']:
                ngrams_to_show = toggle_number(ngrams_to_show,1)
                mono_display(mono,ngrams_to_show)
            elif command == 'bigrams':
                ngrams_to_show = toggle_number(ngrams_to_show,2)
                mono_display(mono,ngrams_to_show)
            elif command == 'trigrams':
                ngrams_to_show = toggle_number(ngrams_to_show,3)
                mono_display(mono,ngrams_to_show)
            elif command == 'quadgrams':
                ngrams_to_show = toggle_number(ngrams_to_show,4)
                mono_display(mono,ngrams_to_show)
            elif command[0].isdigit() and command[1:] == 'grams':
                n = int(command[0])
                ngrams_to_show = toggle_number(ngrams_to_show,n)
                mono_display(mono,ngrams_to_show)
            elif len(command) == 2:
                c, p = command[0],command[1]
                if (c in ALPHABET) and (p in alphabet or p == '_'): # ensures that letters are substituted only by letters anc vice versa or eventually by '_'
                    mono.substitute(c,p)
                    mono_display(mono,ngrams_to_show)
                else:
                    print('Unvalid substitution')
                    mono_display(mono,ngrams_to_show)
            elif command in ['print plaintext','print']:
                clear_screen()
                print(mono.plaintext)
            elif command == '':
               mono_display(mono,ngrams_to_show) 
            else:
                print('Unvalid command. Try again or type \'help\'.')

    
