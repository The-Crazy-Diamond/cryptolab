from cryptolab.analysis.ngrams import get_ngrams
from cryptolab.analysis.frequency import get_frequencies
from cryptolab.utils.alphabet import ALPHABET, alphabet
from cryptolab.utils.text import add_spaces, modify_string
from cryptolab.utils.formatting import clear_screen, print_stacked
import string

NAME = "monoalphabetic"
DESCRIPTION = "Tool designed to progressively replace letters assuming that the ciphertext is an encryption using a monoalphabetic substitution"
ARGS_HELP = None
ARGS_EXAMPLE = ""


def analyse(text: str):
    problem = MonoalphabeticSubstititionDecoder(text)
    problem.solve()


class MonoalphabeticSubstititionDecoder:
    """
    MonoalphabeticSubstititionDecoder is defined by...
    - a ciphertext (in uppercases)
    - a plaintext (in lowercases) to be progressively determined
    """
    
# Ideas to improve:
# - replace plaintext by plaintexts, an array of possible plaintexts to work on different guesses in paraellel
# - add a dict that memorizes replacement map
# - create cancel command
# - make an automatic solving
    
    def __init__(self, ciphertext: str) -> None:
        self.ciphertext = ciphertext
        self.length = len(ciphertext)
        self.plaintext = '-' * self.length
        self.frequencies = get_frequencies(self.ciphertext)
        self.bigrams = get_ngrams(self.ciphertext,2)
        self.trigrams = get_ngrams(self.ciphertext,3)
        self.cipher_to_replace = self.get_cipher_to_replace()
        self.plain_to_replace = alphabet
        self.display_options = [True,False,False]
        
    def __str__(self) -> str:
        raise NotImplementedError

    def display(self) -> None:
        clear_screen()
        print_stacked(add_spaces(self.ciphertext), add_spaces(self.plaintext))
        print('\nCharacters in ciphertext to replace: ', add_spaces(''.join(self.cipher_to_replace)))
        print('Characters in plaintext to replace: ',add_spaces(''.join(self.plain_to_replace)),'\n')
        if self.display_options[0]:
            print('Frequencies: ',self.frequencies,'\n')
        if self.display_options[1]:
            print('Bigrams: ',self.bigrams,'\n')
        if self.display_options[2]:
            print('Trigrams: ',self.trigrams,'\n')

    def get_cipher_to_replace(self) -> list:
        return sorted(list(set([self.ciphertext[i] for i in range(self.length) if self.plaintext[i] == '-'])))

    def get_plain_to_replace(self) -> list:
        return [c for c in alphabet if c not in self.plaintext]
                
    def replace(self, cipherchar, plainchar) -> None:
        for i in range(self.length):
            if self.ciphertext[i] == cipherchar:
                self.plaintext = modify_string(self.plaintext,i,plainchar)
                self.cipher_to_replace = self.get_cipher_to_replace()
                self.plain_to_replace = self.get_plain_to_replace()

    def replace_punctuation(self) -> None:
        # replaces every punctuation symbol and space by itself
        for c in string.punctuation:
            self.replace(c,c)
            
    def replace_spaces(self) -> None:
        self.replace(' ',' ')

    def reset(self) -> None:
        self.plaintext = '-' * self.length
        self.cipher_to_replace = self.get_cipher_to_replace()
        self.plain_to_replace = alphabet
        self.display()
            
    def solve(self) -> None:
        # INITIAL STATE
        self.display()
          
        should_continue = True
        while should_continue:
            command = input('Enter command:\n')
            if command == 'help':
                clear_screen()
                print('Type two characters to make a substitution, e.g. \'Rg\' will substitute every \'R\' with \'g\'.')
                print('Type \'spaces\' or \'punct\' to substitute spaces or punctuations respectively.')
                print('Type \'frequencies\',\'bigrams\' or \'trigrams\' to (un)show the respective countings in the ciphertext.')
                print('Type \'reset\' to reset the solving.')
                print('Type \'quit\' to quit.')
                input('Type enter to continue.')
                self.display()
            elif command == 'quit':
                should_continue = False
            elif command == 'reset':
                self.reset()
            elif command in ['replace spaces','spaces']:
                self.replace_spaces()
                self.display()
            elif command in ['replace punctuation','punct','punctuation']:
                self.replace_punctuation()
                self.display()
            elif command in ['frequencies','freq']:
                self.display_options[0] = not self.display_options[0]
                self.display()
            elif command == 'bigrams':
                self.display_options[1] = not self.display_options[1]
                self.display()
            elif command == 'trigrams':
                self.display_options[2] = not self.display_options[2]
                self.display()
            elif len(command) == 2:
                cipher_char, plain_char = command[0],command[1]
                if (cipher_char in ALPHABET) == (plain_char in alphabet) or plain_char == '-': # ensures that letters are replaced only by letters anc vice versa or eventually by '-'
                    if (plain_char in alphabet) and (plain_char not in self.plain_to_replace):
                        self.display()
                        i = self.plaintext.index(plain_char)
                        print(plain_char, 'is already assigned to \'' + self.ciphertext[i]+ '\'.')
                    else:
                        self.replace(cipher_char, plain_char)
                        self.display()
                else:
                    self.display()
                    print('Unvalid replacement. Try again.')
            elif command in ['print plaintext','print']:
                print(self.plaintext)
            else:
                print('Unvalid command. Try again or type \'help\'.')
        