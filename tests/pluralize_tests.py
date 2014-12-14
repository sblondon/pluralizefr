# -*- coding: utf-8 -*-

import unittest

from pluralizefr import pluralize


class TestPluralize(unittest.TestCase):
    def test_by_default_append_an_s_to_a_word(self):
        self.assertEqual(pluralize('fromage'), 'fromages')
        self.assertEqual(pluralize('jambon'), 'jambons')

    def test_word_finishing_with_al_have_aux_plural(self):
        self.assertEqual(pluralize('cheval'), 'chevaux')
        self.assertEqual(pluralize('animal'), 'animaux')

    def test_some_nouns_finishing_with_al_are_special_cases(self):
        self.assertEqual(pluralize('bal'), 'bals')
        self.assertEqual(pluralize('carnaval'), 'carnavals')
        self.assertEqual(pluralize('chacal'), 'chacals')
        self.assertEqual(pluralize('festival'), 'festivals')
        self.assertEqual(pluralize(u'récital'), u'récitals')
        self.assertEqual(pluralize(u'régal'), u'régals')

    def test_word_finishing_with_s_are_unchanged(self):
        self.assertEqual(pluralize('souris'), 'souris')

    def test_word_finishing_with_x_are_unchanged(self):
        self.assertEqual(pluralize(u'époux'), u'époux')

    def test_word_finishing_with_z_are_unchanged(self):
        self.assertEqual(pluralize('nez'), 'nez')

    def test_word_finishing_with_ail_have_s_plural(self):
        self.assertEqual(pluralize(u'épouvantail'), u'épouvantails')
    
    def test_some_words_finishing_with_ail_are_special_cases(self):
        self.assertEqual(pluralize('bail'), 'baux')
        self.assertEqual(pluralize('corail'), 'coraux')
        self.assertEqual(pluralize(u'émail'), u'émaux')
        self.assertEqual(pluralize('fermail'), 'fermaux')
        self.assertEqual(pluralize('soupirail'), 'soupiraux')
        self.assertEqual(pluralize('travail'), 'travaux')
        self.assertEqual(pluralize('vantail'), 'vantaux')
        self.assertEqual(pluralize('ventail'), 'ventaux')
        self.assertEqual(pluralize('vitrail'), 'vitraux')

    def test_word_finishing_with_au_have_aux_plural(self):
        self.assertEqual(pluralize(u'château'), u'châteaux')
        self.assertEqual(pluralize('noyau'), 'noyaux')
    
    def test_word_finishing_with_eu_have_eux_plural(self):
        self.assertEqual(pluralize("feu"), "feux")
        self.assertEqual(pluralize("pieu"), "pieux")

    def test_some_words_finishing_with_eu_are_special_cases(self):
        self.assertEqual(pluralize("pneu"), "pneus")
        self.assertEqual(pluralize("bleu"), "bleus")
 
 


if __name__ == '__main__':
    unittest.main()

