class Kanji:
    '''Class for representation of a kanji character with all its information
    like the character itself, meanings, readings, which part of speech it is, its radicals.'''
    def __init__(self, character, meanings, readings, parts_of_speech, radical):
        '''
        (object, str, list, dict, list, str, dict) -> None
        Initializes the class with info about hieroglyph. Approximate data examples:
        character = "水"
        meanings = ["water"]
        readings = {'onyomi': {'romaji': 'sui', 'katakana': 'スイ'}, 'kunyomi': {'romaji': 'mizu', 'hiragana': 'みず'}}
        parts_of_speech = ["Noun"]
        radical = "水"
        '''
        self.character = character
        self.meanings = meanings
        self.readings = readings
        self.parts_of_speech = parts_of_speech
        self.radical = radical

    def commonRadical(self, other):
        '''
        Tests if two Kanji objects have the same radical
        and returns corresponing bool value.
        :param other: Kanji
        :return: bool
        '''
        if self.radical == other.radical:
            return True
        else:
            return False

    def getKunyomi(self):
        '''
        Returns hiragana symbols of kunyomi reading of the kanji.
        :return: str
        '''
        return self.readings['kunyomi']['hiragana']

    def getOnyomi(self):
        '''
        Returns katakana symbols of onyomi reading of the kanji.
        :return: str
        '''
        return self.readings['onyomi']['katakana']

    def commonSpeechPart(self, other):
        '''
        Tests if two radicals are the same part of speech
        and gives corresponding bool value.
        :param other: Kanji
        :return: bool
        '''
        if self.parts_of_speech == other.parts_of_speech:
            return True
        else:
            return False


    def __str__(self):
        '''
        Represents the object as str by returning
        the objects character parameter
        :return: str
        '''
        return self.character
