import random
import json
from kanachar import KanaChar
from arrays import ArrayExpanded

class KanaSet:
    '''Data structure based on ArrayExpanded data structure.
    Is used for work with KanaChar objects and their storage'''
    def __init__(self, chars):
        '''
        Initializes the KanaSet object.
        :param chars: list of KanaChar objects
        '''
        self.kana = ArrayExpanded(len(chars))

        for i in range(len(chars)):
            self.kana.insert(i, chars[i])


    def sameConsonant(self, cons):
        '''
        Returns all KanaChars with corresponding consonant.
        :param cons: str
        :return: list
        '''
        result = list()

        for i in range(len(self)):
            excon = self.kana[i].consonant()
            if self.kana[i].sound == 'ji':
                excon = 'd'
            elif self.kana[i].sound == 'chi':
                excon = 't'
            elif self.kana[i].sound == 'tsu':
                excon = 't'
            elif self.kana[i].sound == 'fu':
                excon = 'h'
            elif self.kana[i].sound == 'shi':
                excon = 's'
            if excon == cons:
                result.append(str(self.kana[i]))

        return result

    def sameVowel(self, vow):
        '''
        Returns all KanaChars with corresponding vowel.
        :param vow: str
        :return: list
        '''
        result = list()

        for i in range(len(self)):
            if self.kana[i].vowel() == vow:
                result.append(str(self.kana[i]))

        return result

    def charBySound(self, snd):
        '''
        Returns a KanaChar with corresponding sound value.
        :param sound: str
        :return:KanaChar
        '''
        for i in range(self.itemCount()):
            if self.kana[i].sound == snd:
                return self.kana[i]

    def soundByChar(self, chr):
        '''
        Returns a sound value of KanaChar with corresponding character value.
        :param chr: str
        :return: str
        '''
        for i in range(self.itemCount()):
            if self.kana[i].char == chr:
                return self.kana[i].sound

    def getRandom(self):
        '''
        Returns a random character from the KanaSet.
        :return: KanaChar
        '''
        indx = random.randint(0, self.itemCount()-1)
        return self.kana[indx]


    def itemCount(self):
        '''
        Returns the amount of items, not the actual length.
        :return: int
        '''
        return self.kana.size()

    def __len__(self):
        '''
        Magic method for len() operation.
        :return: int
        '''
        return len(self.kana)

    def __getitem__(self, index):
        '''
        Subscript operator for access at index.
        Precondition: 0 <= index < size()
        '''
        return self.kana[index]

    def __str__(self):
        '''
        Represents object as str.
        :return: str
        '''
        res = '<<'

        for i in range(self.itemCount()):
            res += "'" + str(self.kana[i]) + "', "

        res = res[:-2]
        res += '>>'
        return res

    def __add__(self, other):
        '''
        Magic method for '+' operator.

        Adds two KanaSet objects by creating
        a new KanaSet with the elements
        of the first KanaSet but extended
        with the elements of the second KanaSet.

        :param other: KanaSet object
        :return:
        '''
        initresult = []

        for i in range(self.itemCount()):
            initresult.append(self.kana[i])

        for j in range(other.itemCount()):
            initresult.append(other.kana[j])

        result = KanaSet(initresult)
        return result


def kanaSetUp(file, kanabool):
    '''
    Sets up a KanaSet structure with data
    from a json file as KanaChar objects.
    Works with jsin files structured like
    hiragana.json and katakana.json
    :param file: str
    :param kanabool: bool(True - hiragana, False - katakana)
    :return: KanaSet
    '''
    chars = []
    kanafile = open(file, 'r', encoding='utf-8')
    kana = json.load(kanafile)

    for char in kana['alphabet']:
        chars.append(KanaChar(char['character'], char['romanization'], kanabool))

    kanafile.close()
    return KanaSet(chars)
