from cryptolab.analysis.ngrams import get_ngrams

NAME = "frequency"
DESCRIPTION = "Display the number of occurences of each character in text"
ARGS_HELP = "(optional args will be added in an update)"
ARGS_EXAMPLE = ""


def get_frequencies(text: str, **kwargs) -> dict:
    return get_ngrams(text, n=1, **kwargs)
    
def analyse(text: str) -> dict:
    return get_frequencies(text)