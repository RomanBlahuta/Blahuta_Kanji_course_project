class KanaChar:
    '''Class for representation of hiragana and katakana characters
    with their sounds, characters and kana values.'''
    def __init__(self, char, sound, kana):
        '''
        Initializes KanaChar object.
        :param char: str - japanese kana character
        :param sound: str - latin character sound
        :param kana: bool (True - hiragana, False - katakana)
        '''
        self.char = char
        self.sound = sound
        self.kana = kana

    def consonant(self):
        '''
        Returns the consonant of the character sound.
        Example: gets 'ka' -> returns 'k'
        :return: str
        '''
        res = ''
        for i in self.sound:
            if i not in 'eyuioa':
                res += i
        return res

    def vowel(self):
        '''
        Returns vowel of the character sound.
        Example: gets 'ka' -> returns 'a'
        :return: str
        '''
        res = ''
        for i in self.sound:
            if i in 'eyuioa':
                res += i
        return res

    def __add__(self, other):
        '''
        Magic method for '+' operator.
        Merges characters and sounds of two kana characters.
        :param other: KanaChar
        :return: KanaChar
        '''
        if self.kana == other.kana:
            result = KanaChar(str(self.char+other.char), str(self.sound+other.sound), self.kana)
            return result
        else:
            return NotImplemented

    def __eq__(self, other):
        '''
        Magic method for '==' operator.
        If all parameters are equal then
        two KanaChar objects are equal too.
        :param other: KanaChar
        :return: bool
        '''
        if self.char == other.char and self.sound == other.sound and self.kana == other.kana:
            return True
        else:
            return False

    def __str__(self):
        '''
        Represents object as str by returning KanaChar's char parameter.
        :return: str
        '''
        return self.char
