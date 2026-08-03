import unicodedata
import string
import secrets

# Core text normalization and filtering used everywhere:

# clean_text() (remove accents, punctuation, normalize case)
# only_alpha()
# chunk_text()
# alphabet_index() / index_to_char()

def normalize(text: str, upper: bool = True) -> str: # to modify to propose more options and offer flexibility for ciphers and analyse methods
    # 1. Remove accents
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    
    # 2. Remove punctuation and spaces (keep only letters)
    text = ''.join(c for c in text if c.isalpha())
    
    # 3. Optional: uppercase (common for ciphers)
    if upper:
        text = text.upper()
    return text
    
def mono_normalize(text: str) -> str: # provisary version for MonoSession, to get rid of once normalize is improved
    # NOTE: Currently also used for PolySession and VigenereSession
    #1 and 3 yes, 2 no
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    return text.upper()

    
def common_chars(*strings):
    seen = set()
    for s in strings:
        s_set = set(s)
        if seen & s_set:   # intersection not empty → overlap
            return True
        seen |= s_set
    return False

def add_spaces(text):
    new = ''.join(char + ' ' for char in text)
    return new[:-1]

def modify_string(string: str, index: int, char: str):
    """
    Change char in a string at specified index 
    """
    return string[:index] + char + string[index+1:]

def random_string(alphabet: str, length: int) -> str:
    return ''.join(secrets.choice(alphabet) for _ in range(length))
