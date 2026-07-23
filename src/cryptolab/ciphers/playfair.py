from cryptolab.utils.text import normalize
import string

NAME = "playfair"
DESCRIPTION = "Encode/decode text using Playfair cipher which substitute bigrams using a grid."
ARGS_HELP = "key (string) to generate the substitution 5x5 grid, letter omitted in the grid (default: 'J') and letter to complete bigrams (default: 'X')"
ARGS_EXAMPLE = "KEYWORD"

# Warning no double letters

class PlayfairGrid:
    """
    5x5 grid used to perform Playfair cipher
    """
    
    def __init__(self, key: str, omitted_char: str,show_key: bool = True) -> None:
        if len(omitted_char) != 1:
            raise ValueError("Omitted letter must be a unique character")
        key = normalize(key) + string.ascii_uppercase
        self.grid =  "".join(dict.fromkeys(key)).replace(omitted_char, '')
        # to remove after testing
        if len(self.grid) != 25:
            print("Something went wrong.")
        if show_key:
            for i in range(5):
                line = "".join( self.grid[i*5+ j] + ' ' for j in range(5))
                print(line[:-1]) # we must remove the last space

    def get_coord(self, char):
        n = self.grid.index(char)
        col = n % 5
        row = (n - col)//5
        return row, col

    def get_char(self, row, col):
        return self.grid[5*row + col]

    def encode_pair(self,x,y):
        row_x,col_x = self.get_coord(x)
        row_y,col_y = self.get_coord(y)
        # Case 1: same line -> shift by 1 to the right
        if row_x == row_y:
            col_x = (col_x + 1) % 5
            col_y = (col_y + 1) % 5    
        # Case 2: same column -> shift by 1 below
        elif col_x == col_y:
            row_x = (row_x + 1) % 5
            row_y = (row_y + 1) % 5  
        # Case 3: swap the column coordinates
        else:
            tmp = col_x
            col_x = col_y
            col_y = tmp
        return self.get_char(row_x,col_x)+self.get_char(row_y,col_y)
    
    def decode_pair(self,x,y):
        row_x,col_x = self.get_coord(x)
        row_y,col_y = self.get_coord(y)
        # Case 1: same line -> shift by 1 to the left
        if row_x == row_y:
            col_x = (col_x - 1) % 5
            col_y = (col_y - 1) % 5    
        # Case 2: same column -> shift by 1 above
        elif col_x == col_y:
            row_x = (row_x - 1) % 5
            row_y = (row_y - 1) % 5  
        # Case 3: swap the column coordinates
        else:
            tmp = col_x
            col_x = col_y
            col_y = tmp
        return self.get_char(row_x,col_x)+self.get_char(row_y,col_y)

def playfair_normalize(text,completion_char) -> str:
    text = text.upper()
    plain = text[0]
    for char in text[1:]:
        if plain[-1] == char:
            plain += completion_char
        plain += char
    if len(plain) % 2 != 0:
        plain += completion_char
    return plain
    
def encrypt(text: str, key: str, ommited_char: str = 'J', completion_char: str = 'X') -> str:
    text = playfair_normalize(text,completion_char)
    grid = PlayfairGrid(key, ommited_char)
    return ''.join(grid.encode_pair(text[2*n],text[2*n+1]) for n in range(len(text) // 2))


def decrypt(text: str, key: str, ommited_char: str = 'J', completion_char: str = 'X') -> str:
    text = playfair_normalize(text,completion_char)
    grid = PlayfairGrid(key, ommited_char)
    return ''.join(grid.decode_pair(text[2*n],text[2*n+1]) for n in range(len(text) // 2))

# def playfair_decode(cipher,key,display_table = False):
#     cipher = cipher.upper()
#     table = playfair_table(key,display_table)
#     plain = ''.join(decode_pair(cipher[2*n],cipher[2*n+1],table) for n in range(len(cipher) // 2))
#     # eventually add a funciton that erase 'X'
#     print(plain)
#     return plain
"""
mycipher = ME MH IV KB MG DC UM YM LP UP UX CU CM CQ MU EU NB PB PU MU OH UM UM BE LJ CD PU
  cipher = ME MH IV KB MG DC UM YM LP MU SI MC DC VM UE HC BP PB PU MU OH UM UM BE LJ CD PU
decipher = ET RE LI BR EC EN ES TP AS SE UL EM EN TS ED EB AR YX AR ES DS XE SE RC UC GA XO EU
"""