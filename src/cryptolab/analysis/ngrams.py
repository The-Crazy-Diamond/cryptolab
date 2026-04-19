from collections import Counter

NAME = "ngrams"
DESCRIPTION = "Display the number of occurences of each ngram in text"
ARGS_HELP = "n (integer): 2 for bigrams, 3 for trigrams, etc... (optional args will be added in an update)"
ARGS_EXAMPLE = "3"


def get_ngrams(
    text: str,
    n: int = 1,
    *,
    ignore_spaces: bool = True,
    normalize_case: bool = True,
    alpha_only: bool = False,
) -> dict:
    if normalize_case:
        text = text.upper()

    # Filtering step (shared logic)
    if ignore_spaces:
        text = "".join(c for c in text if not c.isspace())

    if alpha_only:
        text = "".join(c for c in text if c.isalpha())

    # Edge case
    if n <= 0 or len(text) < n:
        return {}

    # Build n-grams
    ngrams = (text[i:i+n] for i in range(len(text) - n + 1))
    counts = Counter(ngrams)

    return dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))

def analyse(text: str, n: str) -> dict:
    
    return get_ngrams(text,int(n))
