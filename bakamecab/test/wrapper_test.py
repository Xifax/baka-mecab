#!/usr/bin/env python
# encoding: utf-8

import subprocess
import unittest

from bakamecab.cli import Parser


class TestWrapper(unittest.TestCase):
    """Test MeCab cli parser"""

    def setUp(self):
        """Check if MeCab is installed and initialize test attributes"""
        try:
            subprocess.check_output('which mecab', shell=True)
        except:
            self.fail('No MeCab executable available.')

        self.sentence = u'任意のディレクトリ内で'
        self.parser = Parser(self.sentence)

    def test_can_get_words(self):
        """Check if may parse sentence"""
        self.assertEqual(len(self.parser.get_words()), 5)
        self.assertIn('任意', self.parser.get_words())

    def test_can_get_info(self):
        """Check if may get info for every word in a sentence"""
        self.assertEqual(len(self.parser.get_info()), 5)
        self.assertEqual(
            self.parser.get_info().keys(),
            self.parser.get_words()
        )
