import itertools
import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    all_words = _get_permutations_draw(draw)
    valid_words = [word for word in all_words if word in dictionary]
    return valid_words
    pass

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    all_words = []

    for i in range(2, len(draw)):
        for word in itertools.permutations(draw, i):
            all_words.append("".join(word).lower())
    return all_words
    pass

draw1 = 'T, I, I, G, T, T, L'.split(", ")
print(draw1)
print(get_possible_dict_words(draw1))