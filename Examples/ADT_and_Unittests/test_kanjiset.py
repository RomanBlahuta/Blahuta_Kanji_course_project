#TESTING KANJISET ADT
import unittest
import random
random.seed(1000)
from kanjiset import KanjiSet
from kanjiclass import Kanji
from kanjiget import kanjiGetJap

class TestKanjiSet(unittest.TestCase):
    def setUp(self):
        self.initlist = []
        kanjistr = '直創缶度関'
        for k in kanjistr:
            kanji = kanjiGetJap(k)
            self.initlist.append(kanji)
        self.kanjis1 = KanjiSet(self.initlist)
        self.kanjis2 = KanjiSet(self.initlist[:2])

    def test_init(self):
        self.assertTrue(isinstance(self.kanjis1, object))
        self.assertTrue(isinstance(self.kanjis2, KanjiSet))
        self.assertTrue(isinstance(self.kanjis1, KanjiSet))
        self.assertTrue(isinstance(self.kanjis2, KanjiSet))
        self.assertTrue(isinstance(self.kanjis1[3], Kanji))
        self.assertTrue(isinstance(self.kanjis2[1], Kanji))
        self.assertEqual(len(self.kanjis1), 5)
        self.assertEqual(len(self.kanjis2), 2)

    def test_values(self):
        value = kanjiGetJap('氷')
        self.assertEqual(str(self.kanjis1[0]), '直')
        self.kanjis1[0] = value
        self.assertEqual(str(self.kanjis1[0]), '氷')
        self.assertTrue(isinstance(self.kanjis1[0], Kanji))
        self.assertEqual(len(self.kanjis1), 5)

    def test_str(self):
        self.assertEqual(str(self.kanjis1), '{{ 直, 創, 缶, 度, 関 }}')
        self.assertEqual(str(self.kanjis2), '{{ 直, 創 }}')

    def test_getRandom(self):
        got = self.kanjis1.getRandom()
        self.assertEqual(str(got), '度')
