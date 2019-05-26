from arrays import ArrayExpanded
import random

class KanjiSet:
    def __init__(self, kanjis=[]):
        '''
        (object, list) -> None
        Initialization.
        '''
        self.theme = None
        self.byRadical = None
        self.size = len(kanjis)

        self._kanjis = ArrayExpanded(len(kanjis))
        for i in range(len(kanjis)):
            self._kanjis[i] = kanjis[i]

    def getRandom(self):
        '''
        Returns a random kanji from the KanjiSet.
        :return: Kanji object
        '''
        indx = random.randint(0, self.size-1)
        return self._kanjis[indx]

    def __getitem__(self, inx):
        '''
        Magic method for getting data from KanjiSet
        by index
        '''
        assert inx >= 0 and inx < len(self), "KanjiSet subscript out of range"
        return self._kanjis[inx]

    def __setitem__(self, inx, val):
        '''
        Magic method for setting a value on chosen index.
        '''
        assert inx >= 0 and inx < len(self), "KanjiSet subscript out of range"
        self._kanjis[inx] = val

    def __len__(self):
        '''
        Magic method that returns the amount of
        kanjis in KanjiSet.
        '''
        return self.size

    def __str__(self):
        res = '{{ '
        for i in range(self.size):
            res += str(self._kanjis[i]) + ', '
        res = res[:-2]
        res += ' }}'
        return res
