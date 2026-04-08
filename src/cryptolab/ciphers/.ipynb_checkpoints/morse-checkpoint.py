NAME = "morse"
DESCRIPTION = "Morse code."


def morse_tables(key: str):
    morse_coding = {}
    morse_decoding = {}
    
    # setting the letters
    morse_letters = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
    
    for i in range(26):
        char,seq = chr(i + ord('A')), morse_letters[i]
        morse_coding[char] = seq
        morse_decoding[seq] = char
    
    # setting the numbers
    morse_numbers = ['-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']
    for i in range(10):
        seq = morse_numbers[i]
        morse_coding[str(i)] = seq
        morse_decoding[seq] = str(i)
    
    # setting special characters
    
        special = '.,?\'!/()&:;=+-_"$@'
        morse_special = ['.-.-.-','--..--','..--..','.----.','-.-.--','-..-.','-.--.','-.--.-','.-...','---...','-.-.-.','-...-','.-.-.','-....-','..--.-','.-..-.','...-..-','.--.-.']
        for i in range(len(special)):
            char,seq = special[i],morse_special[i]
            morse_coding[char] = seq
            morse_decoding[seq] = char

    return morse_coding, morse_decoding

def encrypt(text: str, key: str) -> str:
    morse_coding = morse_tables(key)[0]
    space = '   ' #by default the separation between words is made of 3 spaces
    morse_coding[' '] = space
    return ''.join(morse_coding[char.upper()] + ' ' for char in text)

def decrypt(text: str, key: str) -> str:
    morse_decoding = morse_tables(key)[1]
    space = '   ' #by default the separation between words is made of 3 spaces
    morse_decoding[space] = ' '
    start = 0
    end = 1
    text = ''
    length = len(code)
    code += ' '
    while end <= length:
        seq = code[start:end]           
        if seq in morse_decoding and code[end] == ' ':
            text += morse_decoding[seq]
            start = end + 1
            end = start + 1
        else:
            end += 1
        
    return text