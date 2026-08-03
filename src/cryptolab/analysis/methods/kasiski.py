from cryptolab.utils.text import normalize
from cryptolab.utils.formatting import print_banner

NAME = "kasiski"
DESCRIPTION = "Kasiski's test tries to determine the length of the keyword used for a polyalphabetic substitution cipher by looking repetitions of n-grams."
ARGS_HELP = "n-grams size (int, default = 3), key_length_bound (int, default = 10), score_margin (int, default = 5)"
ARGS_EXAMPLE = "3"


def analyse(text: str, n: int = 3, key_length_bound = 10, score_margin = 5):
    # Treat input
    text = normalize(text)
    key_length_bound = int(key_length_bound)
    score_margin = int(score_margin)

    # Compute distances between repeated n-grams
    occurrences = ngrams_distances(text, n)

    # Flatten the list of distances
    differences = [
        distance
        for distances in occurrences.values()
        for distance in distances
    ]

    # Display scores of the candidate key lengths
    print(f"Score of each candidate key length (between 2 and {key_length_bound})\n")
    scores = key_length_scores(differences, key_length_bound)
    for candidate, score in scores.items():
        print(f"{candidate:2}: {score:3} %")

    # Compute the top_candidate candidate key lengths
    ## Get the highest scores candidates
    best_score = max(scores.values())
    threshold = best_score - score_margin
    
    top_candidates = [candidate for candidate, score in scores.items() if score >= threshold]

    print(f"\nBest score is {best_score} %. Candidates close to best with a margin of {score_margin} % are: {top_candidates}")

    ## If candidate is lonely, it is the top_candidate one
    if len(top_candidates) == 1:
        top_candidate = top_candidates[0]
        print(f"\nBest candidate key length found with a significant highest score: {top_candidate}")
        return top_candidate

    ## Test if one candidate is divisible by all others
    largest_candidate = top_candidates[-1]
    
    if all(largest_candidate % candidate == 0 for candidate in top_candidates):
        print(f"\nBest candidate key length found (common multiple of the best candidates): {largest_candidate}")
        return largest_candidate

    ## No more tests available
    print(f"\nCannot identify best candidate key length among {top_candidates}.")
    return top_candidates

def find_occurrence_indices(string, substring):
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
    
    # Option 1: All occurences
    for i in range(count):
        for j in range(i,count):
            diff = occurrences[j] - occurrences[i]      
            if diff != 0:
                differences.append(diff)
                
    # Option 2: Consecutive occurences
    # for i in range(count-1):
    #     diff = occurrences[i+1] - occurrences[i]      
    #     if diff != 0:
    #         differences.append(diff)
    
    return differences


def ngrams_distances(string, n):
    """
    Return the distances between every pair of occurrence indices of every n-gram in `string`.
    """
    occurrences = {}
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        diff_occurrences = occurrence_distances(find_occurrence_indices(string, substring))
        if diff_occurrences:
            occurrences[substring] = diff_occurrences
    return occurrences
    # Example: {'IPD': [95, 360, 395, 485, 560, 265, 300, 390, 465, 35, 125, 200, 90, 165, 75], 'PDR': [95, 560, 465], 'ECM': [245], 'TWM': [125, 160, 285, 35, 160, 125], 'WMQ': [35, 655, 620], 'MQH': [705], 'VTZ': [60], 'QHT': [620], 'XDZ': [530], 'NTK': [295], 'MQD': [620], 'ACL': [655], 'LAD': [515], 'RDC': [115], 'ICO': [30, 135, 295, 105, 265, 160], 'HMG': [155], 'MGI': [300], 'GIP': [300], 'OJV': [255], 'JVC': [255], 'TLV': [210], 'LVH': [210], 'VHT': [210], 'HTW': [210], 'BGD': [465], 'HQD': [45], 'IMS': [195], 'DDD': [458], 'BNE': [595], 'OKE': [515], 'QMF': [6, 131, 125], 'MFT': [125], 'FTW': [125], 'CSH': [391], 'HNT': [545], 'SGE': [20, 235, 450, 465, 215, 430, 445, 215, 230, 15], 'ERW': [435, 455, 20], 'RWL': [435], 'WLD': [305], 'ETB': [390], 'HFH': [340], 'GZN': [128], 'ZNV': [128], 'MCR': [230], 'CRT': [136], 'HKL': [260], 'TWK': [111], 'MSS': [110], 'ADR': [186], 'ZSI': [186, 320, 134], 'ZNI': [93], 'ZDR': [260], 'LWQ': [30], 'WQJ': [30], 'WMU': [220], 'UEG': [170], 'SHT': [40], 'DVD': [5], 'GER': [15]}


def key_length_scores(differences: list[int], key_length_bound: int) -> dict[int, int]:
    """
    Compute a score for each candidate key length.

    For every candidate key length between 2 and `key_length_bound`, the score
    is the percentage of occurrence distances in `differences` that are divisible
    by the candidate. Scores are normalized so that their sum is 100.
    """
    scores = {}
    total = 0

    # Scoring in absolute value
    for n in range(2, key_length_bound + 1):
        score = sum(diff % n == 0 for diff in differences)
        scores[n] = score
        total += score

    if total == 0:
        return scores
    # Make the scores relative to the total       
    for n, score in scores.items():
        scores[n] = round(scores[n] * 100 / total) # scores are expressed in percent

    return scores
    