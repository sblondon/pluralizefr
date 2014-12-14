# -*- coding: utf-8 -*-

def pluralize(word):
    if word.endswith("al"):
        return word[:-2] + "aux"
    return word + "s"

