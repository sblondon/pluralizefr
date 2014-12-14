# -*- coding: utf-8 -*-

def pluralize(word):
    if word.endswith("al"):
        return word[:-2] + "aux"
    elif word.endswith("s") or word.endswith("z"):
        return word
    return word + "s"

