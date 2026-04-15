import unicodedata
import string

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
