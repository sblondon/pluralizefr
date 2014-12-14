# -*- coding: utf-8 -*-

import unittest

from pluralizefr import pluralize


class TestPluralize(unittest.TestCase):
    def test_by_default_append_an_s_to_a_word(self):
        self.assertEqual(pluralize('fromage'), 'fromages')
        self.assertEqual(pluralize('jambon'), 'jambons')


if __name__ == '__main__':
    unittest.main()
