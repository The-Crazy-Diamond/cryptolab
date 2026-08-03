from cryptolab.utils.text import normalize
from cryptolab.data.indices_of_coincidence import IOC_dict
from cryptolab.analysis.methods.IOC import index_of_coincidence
from cryptolab.analysis.methods.MIOC import mutual_index_of_coincidence

NAME = "coincidence_test"
DESCRIPTION = "Coincidence test tries to determine the length of the keyword used for a Vigenere cipher by using the index of coincidence method."
ARGS_HELP = "key_length_bound (int, default = 10)"
ARGS_EXAMPLE = "7"


def analyse(text: str, key_length_bound = 10, coincidence_threshold = 0.06):
    # Treat input
    text = normalize(text)
    key_length_bound = int(key_length_bound)
    coincidence_threshold = float(coincidence_threshold)

    # Compute average indices of coincidence for every candidate key length
    IOC = {}
    for k in range(1,key_length_bound + 1):
        subtexts = [("".join(text[i] for i in range(len(text)) if i % k == j)) for j in range(k)]
        IOC[k] = round(sum([index_of_coincidence(subtext) for subtext in subtexts]) / k, 4)

    # Display average IOC of the candidate key lengths
    print(f"Average index of coincidence of each candidate key length (between 1 and {key_length_bound})\n")
    for candidate, ioc in IOC.items():
        print(f"{candidate:2}: {ioc}")

    # Compute the top_candidate candidate key lengths
    ## Get the highest scores candidates
    top_candidates = [candidate for candidate, ioc in IOC.items() if ioc >= coincidence_threshold]

    print(f"\nCandidates with satisfying average index of coincidence (> {coincidence_threshold}) are: {top_candidates}")

    ## If candidate is lonely, it is the top_candidate one
    if len(top_candidates) == 1:
        top_candidate = top_candidates[0]
        print(f"\nBest candidate key length found with a significant highest index of coincidence: {top_candidate} (ioc = {IOC[top_candidate]})")
        return top_candidate

    ## Test if the lowest candidate divides all others
    lowest_candidate = top_candidates[0]
    
    if all(candidate % lowest_candidate == 0 for candidate in top_candidates):
        print(f"\nBest candidate key length found (divider of the best candidates): {lowest_candidate} (ioc = {IOC[lowest_candidate]})")
        return lowest_candidate
    ## No more tests available
    print(f"\nCannot identify best candidate key length among {top_candidates}.")
    return top_candidates
