# -*- coding: utf-8 -*-

def pluralize(word):
    if word in ("bal", "carnaval", "chacal", "festival", u"récital", u"régal"):
        return word + "s"
    elif word.endswith("al"):
        return word[:-2] + "aux"
    elif word[-1] in ("s", "x", "z"):
        return word
    return word + "s"

