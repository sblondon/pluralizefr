# -*- coding: utf-8 -*-

import unittest

from pluralizefr import pluralize, singularize


class _Test(unittest.TestCase):
    def check(self, single, plural):
        self.assertEqual(pluralize(single), plural)
        self.assertEqual(singularize(plural), single)


class TestDefault(_Test):
    def test_append_an_s_to_a_word(self):
        self.check("fromage", "fromages")
        self.check("jambon", "jambons")


class TestWordEndsWithAl(_Test):
    def test_words_have_aux_plural(self):
        self.check("cheval", "chevaux")
        self.check("animal", "animaux")

    def test_some_nouns_are_special_cases(self):
        self.assertEqual(pluralize("bal"), "bals")
        self.assertEqual(pluralize("carnaval"), "carnavals")
        self.assertEqual(pluralize("chacal"), "chacals")
        self.assertEqual(pluralize("festival"), "festivals")
        self.assertEqual(pluralize(u"récital"), u"récitals")
        self.assertEqual(pluralize(u"régal"), u"régals")

    def test_some_foreign_nouns_are_special_cases(self):
        #english
        self.assertEqual(pluralize("corral"), "corrals")
        self.assertEqual(pluralize("deal"), "deals")
        self.assertEqual(pluralize("goal"), "goals")
        self.assertEqual(pluralize("autogoal"), "autogoals")
        self.assertEqual(pluralize("revival"), "revivals")
        self.assertEqual(pluralize("serial"), "serials")
        self.assertEqual(pluralize("spiritual"), "spirituals")
        self.assertEqual(pluralize("trial"), "trials")

        #animals
        self.assertEqual(pluralize("caracal"), "caracals")
        self.assertEqual(pluralize("chacal"), "chacals")
        self.assertEqual(pluralize("gavial"), "gavials")
        self.assertEqual(pluralize("narval"), "narvals")
        self.assertEqual(pluralize("quetzal"), "quetzals")
        self.assertEqual(pluralize("rorqual"), "rorquals")
        self.assertEqual(pluralize("serval"), "servals")

        #currencies
        self.assertEqual(pluralize("metical"), "meticals")
        self.assertEqual(pluralize("rial"), "rials")
        self.assertEqual(pluralize("riyal"), "riyals")
        self.assertEqual(pluralize("ryal"), "ryals")

    def test_some_words_based_on_proper_nouns_are_special_cases(self):
        self.assertEqual(pluralize("cantal"), "cantals")
        self.assertEqual(pluralize("emmental"), "emmentals")
        self.assertEqual(pluralize("emmenthal"), "emmenthals")

    def test_republican_months_are_special_cases(self):
        self.assertEqual(pluralize(u"floréal"), u"floréals")
        self.assertEqual(pluralize(u"germinal"), u"germinals")
        self.assertEqual(pluralize(u"prairial"), u"prairials")

    def test_some_adjectives_are_special_cases(self):
        self.assertEqual(pluralize("bancal"), "bancals")
        self.assertEqual(pluralize("fatal"), "fatals")
        self.assertEqual(pluralize("fractal"), "fractals")
        self.assertEqual(pluralize("final"), "finals")
        self.assertEqual(pluralize("morfal"), "morfals")
        self.assertEqual(pluralize("natal"), "natals")
        self.assertEqual(pluralize("naval"), "navals")
        self.assertEqual(pluralize(u"aéronaval"), u"aéronavals")

        for PREFIX in (u"anté", u"néo", u"péri" , u"post", u"pré"):
            self.assertEqual(pluralize(PREFIX + u"natal"), PREFIX + u"natals")
        for PREFIX in (u"", u"a", u"bi", u"poly"):
            self.assertEqual(pluralize(PREFIX + u"tonal"), PREFIX + u"tonals")


class TestWordEndsWithOu(unittest.TestCase):
    def test_some_nouns_are_special_cases(self):
        self.assertEqual(pluralize("bijou"), "bijoux")
        self.assertEqual(pluralize("caillou"), "cailloux")
        self.assertEqual(pluralize("chou"), "choux")
        self.assertEqual(pluralize("genou"), "genoux")
        self.assertEqual(pluralize("hibou"), "hiboux")
        self.assertEqual(pluralize("joujou"), "joujoux")
        self.assertEqual(pluralize("pou"), "poux")


class TestUnchangedWord(unittest.TestCase):
    def test_words_finishing_with_s_are_unchanged(self):
        self.assertEqual(pluralize("souris"), "souris")

    def test_words_finishing_with_x_are_unchanged(self):
        self.assertEqual(pluralize(u"époux"), u"époux")

    def test_words_finishing_with_z_are_unchanged(self):
        self.assertEqual(pluralize("nez"), "nez")


class TestWordEndsWithAil(unittest.TestCase):
    def test_words_have_s_plural(self):
        self.assertEqual(pluralize(u"épouvantail"), u"épouvantails")

    def test_some_words_are_special_cases(self):
        self.assertEqual(pluralize("ail"), "aulx")
        self.assertEqual(pluralize("bail"), "baux")
        self.assertEqual(pluralize("corail"), "coraux")
        self.assertEqual(pluralize(u"émail"), u"émaux")
        self.assertEqual(pluralize("fermail"), "fermaux")
        self.assertEqual(pluralize("soupirail"), "soupiraux")
        self.assertEqual(pluralize("travail"), "travaux")
        self.assertEqual(pluralize("vantail"), "vantaux")
        self.assertEqual(pluralize("ventail"), "ventaux")
        self.assertEqual(pluralize("vitrail"), "vitraux")


class TestWordEndsWithAu(unittest.TestCase):
    def test_words_have_aux_plural(self):
        self.assertEqual(pluralize(u"château"), u"châteaux")
        self.assertEqual(pluralize("noyau"), "noyaux")

    def test_some_words_are_special_cases(self):
        self.assertEqual(pluralize("berimbau"), "berimbaus")
        self.assertEqual(pluralize("donau"), "donaus")
        self.assertEqual(pluralize("karbau"), "karbaus")
        self.assertEqual(pluralize("landau"), "landaus")
        self.assertEqual(pluralize("pilau"), "pilaus")
        self.assertEqual(pluralize("sarrau"), "sarraus")
        self.assertEqual(pluralize("unau"), "unaus")


class TestWordEndsWithEil(unittest.TestCase):
    def test_some_words_are_special_cases(self):
        self.assertEqual(pluralize("vieil"), "vieux")


class TestWordEndsWithEu(unittest.TestCase):
    def test_words_have_eux_plural(self):
        self.assertEqual(pluralize("adieu"), "adieux")
        self.assertEqual(pluralize("pieu"), "pieux")

    def test_some_words_are_special_cases(self):
        self.assertEqual(pluralize("bleu"), "bleus")
        self.assertEqual(pluralize(u"émeu"), u"émeus")
        self.assertEqual(pluralize("enfeu"), "enfeus")
        self.assertEqual(pluralize("pneu"), "pneus")
        self.assertEqual(pluralize("rebeu"), "rebeus")



if __name__ == "__main__":
    unittest.main()

