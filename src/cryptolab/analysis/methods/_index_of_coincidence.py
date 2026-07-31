NAME = "indexOfCoincidence"
DESCRIPTION = "brief description of what is this method"
ARGS_HELP = "list of required arguments: name (type) (write None if no argument is required)"
ARGS_EXAMPLE = "example (write \"\" if no argument is required)"


def analyse(text: str, *args: str):
    raise NotImplementedError("Method function not implemented")


"""
CODE TO RECYCLE:

def index_of_coincidence(string):
    string = string.upper()
    n = len(string)
    sum = 0.0
    for i in range(26):
        frequency = string.count(chr(i + ord('A')))
        sum += frequency * (frequency -1)
    return sum / (n*(n-1))
    
def modular(number,modulo):
    result = number % modulo
    if result < 0:
        result += modulo
    return result

def shift(string,key):
    string = string.upper()
    # the returned shifted string is in uppercase
    return "".join(chr( modular((ord(letter)-ord('A')) + key, 26) + ord('A')) for letter in string)
    

def test_coincidence(cipher,key_length):
    # first split the cipher into supcipher according to the supposed key_length. Each of this cipher should simply be a shift
    subciphers = [("".join(cipher[i] for i in range(len(cipher)) if i % key_length == j)) for j in range(key_length)] #this should be more a general function
    # we compute the mean of the coincidence of each of this subcipher. If key_length was a good guess, the value should be close to 0.065 (see p.83)
    sum = 0.0
    for subcipher in subciphers:
        sum += index_of_coincidence(subcipher)
    sum /= key_length
    print(sum)

def mutual_index_of_coincidence(string1, string2):
    string1 = string1.upper()
    string2 = string2.upper()
    n1 = len(string1)
    n2 = len(string2)
    sum = 0.0
    for i in range(26):
        frequency1 = string1.count(chr(i + ord('A')))
        frequency2 = string2.count(chr(i + ord('A')))
        sum += frequency1 * frequency2
    return sum / (n1*n2)

def vigenere_get_system(cipher,key_length, trust_threshold = 0.05):
    # yields system as in p.86 ... to improve
    subciphers = [("".join(cipher[i] for i in range(len(cipher)) if i % key_length == j)) for j in range(key_length)]
    for j in range(key_length):
        for i in range(j):
            for g in range(26):
                MI = mutual_index_of_coincidence(subciphers[i],shift(subciphers[j],g))
                if MI > trust_threshold:
                    print("k_" + str(i) + " - " + "k_" + str(j)+ " = " + str(g) + "   (MI = " + str(MI) + ")")

"""