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

    def test_words_have_eaux(self):
        self.check("bateau", "bateaux")
        self.check("moineau", "moineaux")

    def test_some_nouns_are_special_cases(self):
        self.assertEqual(pluralize("bal"), "bals")
        self.assertEqual(pluralize("carnaval"), "carnavals")
        self.assertEqual(pluralize("chacal"), "chacals")
        self.assertEqual(pluralize("festival"), "festivals")
        self.assertEqual(pluralize("récital"), "récitals")
        self.assertEqual(pluralize("régal"), "régals")

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
        self.assertEqual(pluralize("floréal"), "floréals")
        self.assertEqual(pluralize("germinal"), "germinals")
        self.assertEqual(pluralize("prairial"), "prairials")

    def test_some_adjectives_are_special_cases(self):
        self.assertEqual(pluralize("bancal"), "bancals")
        self.assertEqual(pluralize("fatal"), "fatals")
        self.assertEqual(pluralize("fractal"), "fractals")
        self.assertEqual(pluralize("final"), "finals")
        self.assertEqual(pluralize("morfal"), "morfals")
        self.assertEqual(pluralize("natal"), "natals")
        self.assertEqual(pluralize("naval"), "navals")
        self.assertEqual(pluralize("aéronaval"), "aéronavals")

        for PREFIX in ("anté", "néo", "péri" , "post", "pré"):
            self.assertEqual(pluralize(PREFIX + "natal"), PREFIX + "natals")
        for PREFIX in ("", "a", "bi", "poly"):
            self.assertEqual(pluralize(PREFIX + "tonal"), PREFIX + "tonals")


class TestWordEndsWithOu(_Test):
    def test_default(self):
        self.check("fou", "fous")

    def test_some_nouns_are_special_cases(self):
        self.check("bijou", "bijoux")
        self.check("caillou", "cailloux")
        self.check("chou", "choux")
        self.check("genou", "genoux")
        self.check("hibou", "hiboux")
        self.check("joujou", "joujoux")
        self.check("pou", "poux")


class TestUnchangedWord(_Test):
    def test_words_finishing_with_s_are_unchanged(self):
        self.check("souris", "souris")

    def test_words_finishing_with_x_are_unchanged(self):
        self.check("époux", "époux")

    def test_words_finishing_with_z_are_unchanged(self):
        self.check("nez", "nez")


class TestWordEndsWithAil(_Test):
    def test_words_have_s_plural(self):
        self.check("épouvantail", "épouvantails")

    def test_some_words_are_special_cases(self):
        self.check("ail", "aulx")
        self.check("bail", "baux")
        self.check("corail", "coraux")
        self.check("émail", "émaux")
        self.check("fermail", "fermaux")
        self.check("soupirail", "soupiraux")
        self.check("travail", "travaux")
        self.check("vantail", "vantaux")
        self.check("ventail", "ventaux")
        self.check("vitrail", "vitraux")


class TestWordEndsWithAu(_Test):
    def test_words_have_aux_plural(self):
        self.assertEqual(pluralize("château"), "châteaux")
        self.assertEqual(pluralize("noyau"), "noyaux")

    def test_some_words_are_special_cases(self):
        self.check("berimbau", "berimbaus")
        self.check("donau", "donaus")
        self.check("karbau", "karbaus")
        self.check("landau", "landaus")
        self.check("pilau", "pilaus")
        self.check("sarrau", "sarraus")
        self.check("unau", "unaus")


class TestWordEndsWithEil(_Test):
    def test_default(self):
        self.check("orteil", "orteils")

    def test_some_words_are_special_cases(self):
        self.check("vieil", "vieux")


class TestWordEndsWithEu(_Test):
    def test_words_have_eux_plural(self):
        self.check("adieu", "adieux")
        self.check("pieu", "pieux")

    def test_some_words_are_special_cases(self):
        self.check("bleu", "bleus")
        self.check("émeu", "émeus")
        self.check("enfeu", "enfeus")
        self.check("pneu", "pneus")
        self.check("rebeu", "rebeus")


class TestWordStartWithGrand(_Test):
    def test_default(self):
        self.check("grand-mère", "grand-mères")

    def test_masculine(self):
        self.check("grand-père", "grands-pères")
        self.check("grand-parent", "grands-parents")


if __name__ == "__main__":
    unittest.main()
