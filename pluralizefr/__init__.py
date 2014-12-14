# -*- coding: utf-8 -*-

def pluralize(word):
    if word in ("bal", "carnaval", "chacal", "festival", u"récital", u"régal",
            "bancal", "fatal", "final", "natal", "naval"):
        return word + "s"
    elif word in ("bail", "corail", u"émail", "fermail", "soupirail", "travail", "vantail", "ventail", "vitrail"):
        return word[:-3] + "aux"
    elif word in ("pneu", "bleu"):
        return word + "s"
    elif word.endswith("au") or word.endswith("eu"):
        return word + "x"
    elif word.endswith("al"):
        return word[:-2] + "aux"
    elif word[-1] in ("s", "x", "z"):
        return word
    return word + "s"

