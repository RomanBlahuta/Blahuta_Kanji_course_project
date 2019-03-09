class Kanji:
    def __init__(self, character, meanings, readings, parts_of_speech, radicals, related_words):
        '''
        (object, str, list, dict, list, list, dict) -> None
        Initializes the class with info about hieroglyph. Approximate data examples:
        character = "水"
        meanings = ["water"]
        readings = {"onyomi": "スイ", "kunyomi": "みず"}
        parts_of_speech = ["Noun"]
        radicals = ["水"]
        related_words = {"水分": ["water", "liquid", "fluid", "moisture", "humidity", "sap", "juice"], ...}
        '''
        self.character = character
        self.meanings = meanings
        self.readings = readings
        self.parts_of_speech = parts_of_speech
        self.radicals = radicals
        self.related_words = related_words
