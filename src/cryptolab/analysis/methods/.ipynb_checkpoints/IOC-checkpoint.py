from cryptolab.utils.text import normalize

NAME = "IOC"
DESCRIPTION = "Compute the index of coincidence of a text."
ARGS_HELP = None
ARGS_EXAMPLE = ""


def analyse(text: str):
    return index_of_coincidence(text)

def index_of_coincidence(string: str):
    """
    Compute the index of coincidence of ´string´.
    
    I_C(x) = (sum_{i=0}^25 f_i (f_i - 1)) / (n(n+1))"
    """
    string = normalize(string)
    n = len(string)
    sum = 0.0
    for i in range(26):
        frequency = string.count(chr(i + ord('A')))
        sum += frequency * (frequency - 1)
    return round(sum / (n*(n-1)),4)