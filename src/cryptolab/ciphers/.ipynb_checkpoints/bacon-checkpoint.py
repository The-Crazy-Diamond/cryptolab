NAME = "bacon"
DESCRIPTION = "Bacon's biliteral cipher with string and a bigram as a key"

# Construction of Bacon tables
def bacon_tables(key: str):
    bacon = {}
    reverse_bacon = {}
    counter = 0
    for i in range(24):
        bin_string = str(bin(i+32))[3:]
        bacon_string = ""
        for char in bin_string:
            if char == '0':
                bacon_string += key[0]
            else:
                bacon_string += key[1]
        letter = chr( counter + ord('a'))
        bacon[letter] = bacon_string
        if letter == 'j' or letter == 'v': #i-j and u-v both identified
            counter += 1
        else:
            reverse_bacon[bacon_string] = letter
        counter += 1
    return bacon, reverse_bacon    

def encrypt(text: str, key: str = 'AB') -> str: #default key should be AB and maybe optional parameters regarding spaces
    bacon = bacon_tables(key)[0]
    space = ''
    # if spaces:
    #     space = ' '
    return "".join(bacon[char] + space for char in text.lower())


def decrypt(text: str, key: str = 'AB') -> str:
    reverse_bacon = bacon_tables(key)[1]
    # if spaces:
    #     text = "".join(char for char in text if char != ' ')
    return "".join(reverse_bacon[text[5*i: 5*i+5]] for i in range(len(text)//5) )
