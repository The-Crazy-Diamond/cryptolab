import warnings

NAME = "morse"
DESCRIPTION = "Encode/decode text using Morse code."
ARGS_HELP = "space symbol used between words (default: '/')"
ARGS_EXAMPLE = ""


def encrypt(text: str, space_symbol: str = '/') -> str:
    text = text.upper()
    morse_dict[' '] = space_symbol
    return ''.join(morse_dict[char] + ' ' for char in text)

def decrypt(text: str, space_symbol: str = '/') -> str:
    reverse_morse_dict[space_symbol] = ' '
    start = 0
    end = 1
    plain = ''
    length = len(text)
    text += ' ' # this padding is necessary for indicating the end of the last scanned piece of text
    while end <= length:
        scan = text[start:end]
        if scan == ' ': # if the scanned text is a space, just ignore it and scan what's next
            start += 1
            end += 1
        elif scan in reverse_morse_dict and text[end] == ' ': 
            plain += reverse_morse_dict[scan]
            start = end + 1
            end = start + 1
        else:
            end += 1
    if (start != length+1) and text[start:end] != ' ':
        warnings.warn('A part of the code was not decrypted: "' + text[start:end]+'"')
    return plain

morse_dict = {
    # Letters
    'A': '.-',       'B': '-...',     'C': '-.-.',     'D': '-..',
    'E': '.',        'F': '..-.',     'G': '--.',      'H': '....',
    'I': '..',       'J': '.---',     'K': '-.-',      'L': '.-..',
    'M': '--',       'N': '-.',       'O': '---',      'P': '.--.',
    'Q': '--.-',     'R': '.-.',      'S': '...',      'T': '-',
    'U': '..-',      'V': '...-',     'W': '.--',      'X': '-..-',
    'Y': '-.--',     'Z': '--..',

    # Numbers
    '0': '-----',    '1': '.----',    '2': '..---',    '3': '...--',
    '4': '....-',    '5': '.....',    '6': '-....',    '7': '--...',
    '8': '---..',    '9': '----.',

    # Punctuation / Symbols
    '.': '.-.-.-',   ',': '--..--',   '?': '..--..',   "'": '.----.',
    '!': '-.-.--',   '/': '-..-.',    '(': '-.--.',    ')': '-.--.-',
    '&': '.-...',    ':': '---...',   ';': '-.-.-.',   '=': '-...-',
    '+': '.-.-.',    '-': '-....-',   '_': '..--.-',   '"': '.-..-.',
    '$': '...-..-',  '@': '.--.-.',

    # Common accented characters
    'À': '.--.-',    'Ä': '.-.-',     'Å': '.--.-',
    'Æ': '.-.-',     'Ç': '-.-..',    'É': '..-..',
    'È': '.-..-',    'Ñ': '--.--',    'Ö': '---.',
    'Ü': '..--',

    # Space / word separator
    ' ': '/',

    # Returns to line
    '\n': '\n',
}

reverse_morse_dict = {v: k for k, v in morse_dict.items()}