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
        
        # tracks and adds whitespace char at the end of words
        if word[-1] == " ":
            trailing = (" ")
            word = word.strip()
        else:
            trailing = ("")

        letters = "*" # specific Binder 2.0 wildcard char for inserts and replacements

        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [L + R[1:] + trailing for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] + trailing for L, R in splits if len(R)>1]

        if distance:
            replaces = [L + c + R[1:] + trailing for L, R in splits if R for c in letters]
            inserts = [L + c + R + trailing for L, R in splits for c in letters]

        else:
            replaces = []
            inserts = [L + c + R + trailing for L, R in splits if R and L for c in L[-1] + R[0]]

        cache += list(set(deletes + transposes + replaces + inserts))

    # process and clean up the list of variants

    cache = [i for i in cache if len(i) > 2]

    cache_clean = []

    for i in range(len(cache)):
        for z in range(len(cache_clean)):

            if cache[i] in cache_clean[z]:
                cache_clean[z] = cache[i]
        else:
            cache_clean.append(cache[i])

    return list(set(cache_clean + words))


running = True

while running:

    print "\n"
    words = raw_input("Input words seperated by commas: ")
    
    #clean input words
    
    all_words = words.lower().split("|")

    edit_words = map(lambda x: x.lstrip(), all_words[0].split(","))

    if "|" in words:
        extra_words = map(lambda x: x.lstrip(), all_words[1].split(","))
    else:
        extra_words = []

    print "\nWildcards:"
    print "---"

    output = BinderQuery(edit1(edit_words) + extra_words)
    pyperclip.copy(output)

quit()
