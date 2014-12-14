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



if __name__ == '__main__':
    unittest.main()

