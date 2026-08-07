import unicodedata
import string
import secrets

def normalize(text: str, remove_accents: bool = True, only_letters: bool = True, upper: bool = True, remove_line_breaks = True) -> str:
    # 1. Remove accents
    if remove_accents:
        text = unicodedata.normalize('NFD', text)
        text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    
    # 2. Remove punctuation and spaces (keep only letters)
    if only_letters:
        text = ''.join(c for c in text if c.isalpha())
    
    # 3. Turn to uppercase (common for ciphers)
    if upper:
        text = text.upper()

    # 4. Remove line breaks
    if remove_line_breaks:
        text = text.replace("\n", "")
        
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

def random_string(alphabet: str, length: int) -> str:
    return ''.join(secrets.choice(alphabet) for _ in range(length))
