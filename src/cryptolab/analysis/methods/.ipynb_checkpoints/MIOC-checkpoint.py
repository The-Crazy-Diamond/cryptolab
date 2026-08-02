from cryptolab.utils.text import normalize

NAME = "MIOC"
DESCRIPTION = "Compute the mutual index of coincidence of a text with another text."
ARGS_HELP = "text2"
ARGS_EXAMPLE = "file02.txt"


def analyse(text: str, other_text: str):
    return mutual_index_of_coincidence(text, other_text)

def mutual_index_of_coincidence(string1, string2):
    """
    Compute the mutual index of coincidence of ´string1´ and ´string2´.
    
    MI_C(x) = (\sum_{i=0}^25 (f_i * f_i')) / (n * n')"
    """
    string1 = normalize(string1)
    string2 = normalize(string2)
    n1 = len(string1)
    n2 = len(string2)
    sum = 0.0
    for i in range(26):
        frequency1 = string1.count(chr(i + ord('A')))
        frequency2 = string2.count(chr(i + ord('A')))
        sum += frequency1 * frequency2
    return sum / (n1*n2)