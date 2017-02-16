import numpy as np
import json
import pyperclip

#Definitions

def BinderQuery(variants):
    """
    Helper function that prints a list of search terms as a binder query.
    Parameters:
        Variants: List of words for binder query
    """
    variants = map(lambda x: "'" + x + "'", variants)
    termstring = "name contains (" + ", ".join(variants) + ")"
    print termstring
    return termstring

def edit1(words, distance = 1):
    """
    Returns all words within one edit of input string. "*" denotes
    a wildcard character
    """
    cache = []

    for word in words:
        letters = "*" # set of letters to use for inserts and replacements

        splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
        deletes    = [L + R[1:]               for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]

        if distance:
            replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
            inserts    = [L + c + R               for L, R in splits for c in letters]

        else:
            replaces = []
            inserts    = [L + c + R               for L, R in splits if R and L for c in L[-1] + R[0]]

        cache += list(set(deletes + transposes + replaces + inserts))

    cache = [i for i in cache if len(i) > 2]

    cache_clean = []

    for i in range(len(cache)):
        for z in range(len(cache_clean)):

            if cache[i] in cache_clean[z]:
                cache_clean[z] = cache[i]

            elif cache_clean[z] in cache[i]:
                break
        else:
            cache_clean.append(cache[i])

    return list(set(cache_clean + words))


def below_distance(sim_matrix, distance, chars):
        """
        Generates a dictionary of possible replacements for each key below a specified distance threshold.
        Input chars variable as list in the order that characters are indexed in sim_matrix
        """
        output_ind = {}
        for ind in range(sim_matrix.shape[0]):
            output_ind[ind] = [x for x, dist in zip(range(sim_matrix.shape[0]), sim_matrix[ind]) if dist <= distance]

        output_char = {}
        for indx in output_ind:
            output_char[chars[indx]] = [chars[i] for i in output_ind[indx]]

        return output_char

def WghtdEdit1(words, sim_dict):
    """
    Returns all words within a distance of the input string
    """

    cache = []

    for word in words:

        splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
        deletes    = [L + R[1:]               for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
        replaces   = [L + c + R[1:]           for L, R in splits if R for c in sim_dict[R[0]]]
        inserts    = [L + c + R               for L, R in splits if L and R for c in sim_dict[R[0]] + sim_dict[L[-1]]]

        cache += list(set(deletes + transposes + replaces + inserts))

    cache = [i for i in cache if len(i) > 2] + words

    cache_clean = []

    #removes redundant binder queries
    for i in range(len(cache)):
        for z in range(len(cache_clean)):
            replaced = False

            if cache[i] in cache_clean[z] and not replaced:
                cache_clean[z] = cache[i]
                replaced = True

            elif cache_clean[z] in cache[i]:
                break
        else:
            cache_clean.append(cache[i])
    cache_clean = list(set(cache_clean + words))

    return cache_clean


running = True

while running:
    #load distance matrices
    try:
        distance_arrays = np.load(open("d_arrays.npz"))
        hmn = distance_arrays["hmn_distance"] #/ 0.2
        ocr = distance_arrays["ocr_distance"] #/ 0.2
        euc = distance_arrays["euc_distance"]

    except IOError:
        print "Loading data failed! Make sure the 'd_arrays.npz' file is in the same directory as this script then re-run it."
        quit()

    #indexing order for numpy arrays
    chars = list("qwertyuiopasdfghjklzxcvbnm")
    alp_chars = list("abcdefghijklmnopqrstuvwxyz")


    print "\n"
    words = raw_input("Input words seperated by commas: ")
    #clean input words
    all_words = words.lower().split("|")

    edit_words = map(lambda x: x.strip(), all_words[0].split(","))

    if "|" in words:
        extra_words = map(lambda x: x.strip(), all_words[1].split(","))
    else:
        extra_words = []

    """
    distance = float(distance)
    su_distance = distance * 0.2

    #create simalarity dictionaries
    euc_sim_dict = below_distance(euc, distance, chars)
    hum_sim_dict = below_distance(hmn, su_distance, alp_chars)
    ocr_sim_dict = below_distance(ocr, su_distance, alp_chars)
    """

    print "\nWildcards:"
    print "---"

    output = BinderQuery(edit1(edit_words) + extra_words)
    pyperclip.copy(output)

quit()




