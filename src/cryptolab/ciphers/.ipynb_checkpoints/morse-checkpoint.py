import warnings

NAME = "morse"
DESCRIPTION = "Encode/decode text using Morse code."
ARGS_HELP = "space symbol used between words (default: '/')"
ARGS_EXAMPLE = ""


def encrypt(text: str, space_symbol: str = '/') -> str:
    morse_coding[' '] = space_symbol
    return ''.join(morse_coding[char.upper()] + ' ' for char in text)

def decrypt(text: str, space_symbol: str = '/') -> str:
    morse_decoding[space_symbol] = ' '
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
        elif scan in morse_decoding and text[end] == ' ': 
            plain += morse_decoding[scan]
            start = end + 1
            end = start + 1
        else:
            end += 1
    if (start != length+1) and text[start:end] != ' ':
        warnings.warn('A part of the code was not decrypted: "' + text[start:end]+'"')
    return plain

morse_coding = {
 'A': '.-',
 'B': '-...',
 'C': '-.-.',
 'D': '-..',
 'E': '.',
 'F': '..-.',
 'G': '--.',
 'H': '....',
 'I': '..',
 'J': '.---',
 'K': '-.-',
 'L': '.-..',
 'M': '--',
 'N': '-.',
 'O': '---',
 'P': '.--.',
 'Q': '--.-',
 'R': '.-.',
 'S': '...',
 'T': '-',
 'U': '..-',
 'V': '...-',
 'W': '.--',
 'X': '-..-',
 'Y': '-.--',
 'Z': '--..',
 '0': '-----',
 '.': '.-.-.-',
 ',': '--..--',
 '?': '..--..',
 "'": '.----.',
 '!': '-.-.--',
 '/': '-..-.',
 '(': '-.--.',
 ')': '-.--.-',
 '&': '.-...',
 ':': '---...',
 ';': '-.-.-.',
 '=': '-...-',
 '+': '.-.-.',
 '-': '-....-',
 '_': '..--.-',
 '"': '.-..-.',
 '$': '...-..-',
 '@': '.--.-.',
 '1': '.----',
 '2': '..---',
 '3': '...--',
 '4': '....-',
 '5': '.....',
 '6': '-....',
 '7': '--...',
 '8': '---..',
 '9': '----.'
}


morse_decoding = {
'.-': 'A',
 '-...': 'B',
 '-.-.': 'C',
 '-..': 'D',
 '.': 'E',
 '..-.': 'F',
 '--.': 'G',
 '....': 'H',
 '..': 'I',
 '.---': 'J',
 '-.-': 'K',
 '.-..': 'L',
 '--': 'M',
 '-.': 'N',
 '---': 'O',
 '.--.': 'P',
 '--.-': 'Q',
 '.-.': 'R',
 '...': 'S',
 '-': 'T',
 '..-': 'U',
 '...-': 'V',
 '.--': 'W',
 '-..-': 'X',
 '-.--': 'Y',
 '--..': 'Z',
 '-----': '0',
 '.-.-.-': '.',
 '--..--': ',',
 '..--..': '?',
 '.----.': "'",
 '-.-.--': '!',
 '-..-.': '/',
 '-.--.': '(',
 '-.--.-': ')',
 '.-...': '&',
 '---...': ':',
 '-.-.-.': ';',
 '-...-': '=',
 '.-.-.': '+',
 '-....-': '-',
 '..--.-': '_',
 '.-..-.': '"',
 '...-..-': '$',
 '.--.-.': '@',
 '.----': '1',
 '..---': '2',
 '...--': '3',
 '....-': '4',
 '.....': '5',
 '-....': '6',
 '--...': '7',
 '---..': '8',
 '----.': '9'
}

# tables generated with :

# def morse_tables():
#     morse_coding = {}
#     morse_decoding = {}
    
#     # setting the letters
#     morse_letters = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
    
#     for i in range(26):
#         char,seq = chr(i + ord('A')), morse_letters[i]
#         morse_coding[char] = seq
#         morse_decoding[seq] = char
    
#     # setting the numbers
#     morse_numbers = ['-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']
#     for i in range(10):
#         seq = morse_numbers[i]
#         morse_coding[str(i)] = seq
#         morse_decoding[seq] = str(i)
    
#     # setting special characters
    
#         special = '.,?\'!/()&:;=+-_"$@'
#         morse_special = ['.-.-.-','--..--','..--..','.----.','-.-.--','-..-.','-.--.','-.--.-','.-...','---...','-.-.-.','-...-','.-.-.','-....-','..--.-','.-..-.','...-..-','.--.-.']
#         for i in range(len(special)):
#             char,seq = special[i],morse_special[i]
#             morse_coding[char] = seq
#             morse_decoding[seq] = char

#     return morse_coding, morse_decoding
