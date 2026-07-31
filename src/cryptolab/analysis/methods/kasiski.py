from cryptolab.utils.text import normalize

NAME = "kasiski"
DESCRIPTION = "Kasiski's test tries to determine the length of the keyword used for a polyalphabetic substitution cipher."
ARGS_HELP = "n-grams size (int), default = 3"
ARGS_EXAMPLE = "3"


def analyse(text: str, n: int = 3):
    text = normalize(text)
    occurrences = ngrams_distances(text, n)

    differences = [
        distance
        for distances in occurrences.values()
        for distance in distances
    ]
    return key_length_scores(differences)

def find_occurrence_indices(string,substring):
    """
    Return the starting indices of every occurrence of `substring` in `string`.
    """
    return [index for index in range(len(string)) if string.startswith(substring, index)] 


def occurrence_distances(occurrences):
    """
    Return the distances between every pair of occurrence indices.
    """
    differences = []
    count = len(occurrences)
    for i in range(count):
        for j in range(i,count):
            diff = occurrences[j] - occurrences[i]      
            if diff != 0:
                differences.append(diff)
    return differences


def ngrams_distances(string, n):
    #lists the indices of occurrences of a substring of length n
    occurrences = {}
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        diff_occurrences = occurrence_distances(find_occurrence_indices(string, substring))
        if diff_occurrences:
            occurrences[substring] = diff_occurrences
    return occurrences

def key_length_scores(differences: list, bound = 15):
    scores = {}
    for n in range(2,bound + 1):
        score = 0
        for diff in differences:
            if diff % n == 0:
                score += 1
        scores[n] = score
    print(f"Key length scores (up to {bound})")
    return scores