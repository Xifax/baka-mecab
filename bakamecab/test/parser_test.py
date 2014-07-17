#!/usr/bin/env python
# encoding: utf-8

import subprocess
import unittest

from bakamecab.cli import Parser


class TestParser(unittest.TestCase):
    """Test mecab cli parser"""

    def setUp(self):
        """Check if MeCab is installed and initialize test attributes"""
        try:
            subprocess.check_output('which mecab', shell=True)
        except:
            self.fail('No MeCab executable available.')

        self.sentence = u'任意のディレクトリ内で'

    def test_can_parse_mecab_stdout(self):
        """Check if may call MeCab and parse its output"""
        parser = Parser(self.sentence)
        self.assertIsInstance(parser.mecab(), Parser)
        self.assertTrue(parser.words)
        self.assertTrue(parser.info)
