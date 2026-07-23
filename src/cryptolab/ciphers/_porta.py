from cryptolab.utils.text import normalize
from itertools import zip_longest

NAME = "porta(in_progress)"
DESCRIPTION = "Giambatista della Porta's polyalphabetic cipher"
ARGS_HELP = "keyword"
ARGS_EXAMPLE = "\"PASSVORD\""

substitutions = {
 'AB': 'ABCDEFGHILMNOPQRSTVXYZ',
 'CD': 'ANBOCPDQERFSGTHVIXLYMZ',
 'EF': 'AIRBLSCMTDNVEOXFPYGQZH',
 'GH': 'AYCVESGQIOMZBXDTFRHPLN',
 'IL': 'ACEGIMOQSVYBDFHLNPRTXZ',
 'MN': 'ABSCDTEFVGHILXM NYOPZQR',
 'OP': 'ABCLDEFMGHIPRNYSOQXTVZ',
 'QR': 'ABCSDEFTVGHILMXNOPYZQR',
 'ST': 'ZABCDEFGHILMNOPQRSTVXY',
 'VX': 'YZABCDEFGHILMNOPQRSTVX',
 'YZ': 'XYZABCDEFGHILMNOPQRSTV'  
}

def encrypt(text: str, key: str) -> str:
    if not key:
        raise ValueError("At least one key is required")

    # 1. Extract normalized letters only
    letters = [normalize(c,False) for c in text if c.isalpha()]

    # 2. Apply cipher on letters only
    processed = [func(''.join(letters[i::n]), keys[i]) for i in range(n)]

    # 3. Rebuild transformed letters (interleave)
    transformed_letters = ''.join(char for group in zip_longest(*processed, fillvalue='') for char in group)

    # 4. Reinsert into original text
    result = []
    letter_index = 0

    for c in text:
        if c.isalpha():
            result.append(transformed_letters[letter_index])
            letter_index += 1
        else:
            result.append(c)

    return ''.join(result)


def decrypt(text: str, key: str) -> str:
    return 
