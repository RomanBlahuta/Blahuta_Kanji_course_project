#TESTING KANASET ADT
# -*- coding: utf-8 -*-

import json
import unittest
from kanaset import kanaSetUp, KanaSet
from kanachar import KanaChar

class TestKanaSet(unittest.TestCase):
    def setUp(self):
        self.hiragana = kanaSetUp('hiragana.json', True)
        self.katakana = kanaSetUp('katakana.json', False)
        self.someKana = KanaSet([KanaChar('え', 'e', True), KanaChar('メ', 'me', False)])

    def test_init(self):
        self.assertTrue(self.hiragana[0] == KanaChar('あ', 'a', True))
        self.assertTrue(self.katakana[0] == KanaChar('ア', 'a', False))
        self.assertEqual(self.hiragana[2], KanaChar('う', 'u', True))
        self.assertTrue(isinstance(self.hiragana, KanaSet))
        self.assertTrue(isinstance(self.katakana, KanaSet))
        self.assertTrue(isinstance(self.katakana[10], KanaChar))
        self.assertTrue(isinstance(self.hiragana[21], KanaChar))

    def test_charBySound(self):
        self.assertEqual(self.hiragana.charBySound('e'), KanaChar('え', 'e', True))
        self.assertEqual(self.katakana.charBySound('ka'), KanaChar('カ', 'ka', False))
        self.assertEqual(self.hiragana.charBySound('ke'), KanaChar('け', 'ke', True))
        self.assertEqual(self.katakana.charBySound('me'), KanaChar('メ', 'me', False))

    def test_soundByChar(self):
        self.assertEqual(self.hiragana.soundByChar('え'), 'e')
        self.assertEqual(self.katakana.soundByChar('カ'), 'ka')
        self.assertEqual(self.hiragana.soundByChar('け'), 'ke')
        self.assertEqual(self.katakana.soundByChar('メ'), 'me')

    def test_str(self):
        self.assertTrue(str(self.someKana) == "<<'え', 'メ'>>")
