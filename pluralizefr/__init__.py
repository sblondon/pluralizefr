# -*- coding: utf-8 -*-

"""Pluralize word according French grammar rules

Special cases are based on:
http://fr.wiktionary.org/wiki/Annexe:Pluriels_irr%C3%A9guliers_en_fran%C3%A7ais
"""


def pluralize(word):
    for GRAMMAR_RULE in (_ail_word, _al_word, _au_word, _eil_word, _eu_word, _ou_word, _s_word, _x_word, _z_word,
            _default):
        plural = GRAMMAR_RULE(word)
        if plural:
            return plural



def _ail_word(word):
    if word.endswith("ail"):
        if word == "ail":
            return "aulx"
        elif word in ("bail", "corail", u"émail", "fermail", "soupirail", "travail", "vantail", "ventail", "vitrail"):
            return word[:-3] + "aux"
        return word + "s"

def _al_word(word):
    if word.endswith("al"):
        if word in ("bal", "carnaval", "chacal", "festival", u"récital", u"régal",
            "bancal", "fatal", "fractal", "final", "morfal", "natal", "naval",
            u"aéronaval",
            u"anténatal", u"néonatal", u"périnatal", u"postnatal", u"prénatal",
            "tonal", "atonal", "bitonal", "polytonal",
             "corral", "deal", "goal", "autogoal", "revival", "serial", "spiritual", "trial",
            "caracal", "chacal", "gavial", "gayal", "narval", "quetzal", "rorqual", "serval",
            "metical", "rial", "riyal", "ryal",
            "cantal", "emmental", "emmenthal",
            u"floréal", "germinal", "prairial",
            ):
            return word + "s"
        return word[:-2] + "aux"

def _au_word(word):
    if word.endswith("au"):
        if word in ("berimbau", "donau", "karbau", "landau", "pilau", "sarrau", "unau"):
            return word + "s"
        return word + "x"

def _eil_word(word):
    if word.endswith("eil"):
        return "vieux" if word == "vieil" else word + "s"

def _eu_word(word):
    if word.endswith("eu"):
        return word + "s" if word in ("pneu", "bleu") else word + "x"

def _ou_word(word):
    if word.endswith("ou"):
        return word + "x" if word in ("bijou", "caillou", "chou", "genou", "hibou", "joujou", "pou") else word + "s"

def _s_word(word):
    if word[-1] == "s":
        return word

def _x_word(word):
    if word[-1] == "x":
        return word
        
def _z_word(word):
    if word[-1] == "z":
        return word
 
def _default(word):
    return word + "s"

