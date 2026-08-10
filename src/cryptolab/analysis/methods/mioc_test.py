from cryptolab.utils.text import normalize
from cryptolab.data.indices_of_coincidence import IOC_dict
from cryptolab.analysis.methods.IOC import index_of_coincidence
from cryptolab.analysis.methods.MIOC import mutual_index_of_coincidence
from cryptolab.ciphers.caesar import encrypt as caesar_shift

NAME = "mioc_test"
DESCRIPTION = "This test tries to determine the key used for a Vigenere cipher by analysing with the ciphertext with mutual indices of coincidence. The key length is supposed to be known."
ARGS_HELP = "key_length (int)"
ARGS_EXAMPLE = "6"


def analyse(text: str, key_length = 10): # coincidence_threshold = 0.06
    # Treat input
    text = normalize(text, remove_accents = True, only_letters = True, upper = True, remove_line_breaks = True)
    key_length = int(key_length)
    # coincidence_threshold = float(coincidence_threshold)

    # Compute mutual indices of coincidence table
    # MIOC_table = {}
    # Compute best relative shifts with their associated mutual index of coincidence
    MIOC_scores = {}
    for i in range(key_length):
        for j in range(i+1, key_length):
            text_i = text[i::key_length]
            text_j = text[j::key_length]
            # Compute mutual indices of coincidence for index pair (i,j)
            MIOC ={}
            for shift in range(26):
                MIOC[shift] = mutual_index_of_coincidence(text_i, caesar_shift(text_j,-shift))
            # MIOC_table[(i,j)] = MIOC # might be an overkill, not sure that it would make the UX good
            shift_max = max(MIOC, key=MIOC.get)
            mioc_max = MIOC[shift_max]
            MIOC_scores[(i,j)] = shift_max
            print(f"For pair ({i},{j}), the relative shift {shift_max:2} yields the best mutual index of coincidence {mioc_max}.")

    # Deduce potential keywords (not optimal yet because only consider the shifts relatively to the first letter of the keyword)
    print("\nPotential keywords:")
    potential_keywords = []
    out = ['A']
    for j in range(1,key_length):
        shift = MIOC_scores[(0,j)]
        out.append(chr(ord('A') + shift))
    keyword = "".join(out)
    for shift in range(26):
        shifted_keyword = caesar_shift(keyword,shift)
        potential_keywords.append(shifted_keyword)
        print(shifted_keyword)

    return potential_keywords
            
