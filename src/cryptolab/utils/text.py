import unicodedata
import string

# Core text normalization and filtering used everywhere:

# clean_text() (remove accents, punctuation, normalize case)
# only_alpha()
# chunk_text()
# alphabet_index() / index_to_char()

def normalize(text: str, upper: bool = True) -> str:
    # 1. Remove accents
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    
    # 2. Remove punctuation and spaces (keep only letters)
    text = ''.join(c for c in text if c.isalpha())
    
    # 3. Optional: uppercase (common for ciphers)
    if upper:
        text = text.upper()
    return text
    
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

