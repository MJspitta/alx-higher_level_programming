#!/usr/bin/python3
def best_score(a_dictionary):
    best = 0
    if a_dictionary is None:
        return None
    for score in a_dictionary.values():
        if score > best:
            best = score
    for key, val in a_dictionary.items():
        if best == val:
            return key
