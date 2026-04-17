from cryptolab.utils.text import normalize

NAME = "transposition"
DESCRIPTION = "Transposition cipher writing the text by rows in a table, rearringing the columns and reading the text by columns"
ARGS_HELP = "keyword (string) used to rearrange the order of the columns and a mode (\"normalized\" or \"all\") for encryption: the order is determined by sorting the characters of the keyword in alphabetical order; the columns are then rearranged to match this sorted order. The mode allows to choose if the text should be normalized before encryption (default) or if all characters should be considered."
ARGS_EXAMPLE = "KEYWORD all"

"""
Features ideas:
- Add a mode option: "write by rows/columns read by rows/columns" see https://www.dcode.fr/transposition-cipher
- Add another mode option to deal with spaces in text or key (not essential)
- Deal case of common letters in keyword differently ?
"""
valid_modes = ["normalized","all"]

def check_key(key: str) -> str:
    key = normalize(key)
    if len(set(key)) < len(key):
        raise ValueError("Keyword must contain distinct letters.")
    else:
        return key

def encrypt(text: str, key: str, mode: str = "normalized") -> str:
    key = check_key(key)
    if mode not in valid_modes: 
         raise ValueError("Invalid mode. Must be in " + str(valid_modes))
    if mode == "normalized":
        text = normalize(text)

    l = len(key)
    columns = [text[i::l] for i in range(l)]
    return ''.join(columns[i] for i in sorted(range(l), key=lambda i: key[i]))

    # My original code was this:
    # columns = {}
    # l = len(key)
    # for i in range(l):
    #     columns[key[i]] = text[i::l]
    # return ''.join([columns[c] for c in sorted(key)])

def decrypt(cipher: str, key: str) -> str:
    """
    This function was implemented by an AI. I wanted to try. :-)
    """
    key = check_key(key)
    l = len(key)
    n = len(cipher)

    # Step 1: get sorted column indices (same as encryption)
    sorted_indices = sorted(range(l), key=lambda i: key[i])

    # Step 2: determine column lengths
    base_len = n // l
    extra = n % l  # first 'extra' columns are longer

    col_lengths = [base_len + (i < extra) for i in range(l)]

    # Step 3: assign slices from cipher to correct columns
    columns = [None] * l
    pos = 0
    for idx in sorted_indices:
        length = col_lengths[idx]
        columns[idx] = cipher[pos:pos + length]
        pos += length

    # Step 4: rebuild original text row-wise
    result = []
    for i in range(max(col_lengths)):
        for col in columns:
            if i < len(col):
                result.append(col[i])

    return ''.join(result)
