#Important!
#Files hiragana.json and katakana.json are required

import json

def kana_char(kana_file, sound):
    '''
    (str, str) -> str
    Works with file hiragana.json and gathers hiragana characters.
    '''
    file = open(kana_file, 'r', encoding='utf-8')
    inf = json.load(file)
    allchars = inf["alphabet"]
    for hrgn in allchars:
        if hrgn["romanization"] == sound:
            return hrgn["character"]


def pair_chars(sound):
    '''
    str -> list
    Learning Hiragana and Katakana at the same time is easier!
    This function returns Hiragana and Katakana characters for the same sound.
    '''
    hir_char = kana_char("hiragana.json", sound)
    kat_char = kana_char("katakana.json", sound)
    result = []
    result.append(hir_char)
    result.append(kat_char)
    return result

class Sound:
    def __init__(self, sound, hiragana, katakana):
        '''
        (object, str, str, str) -> None
        Initializes the class
        '''
        self.sound = sound
        self.hiragana = hiragana
        self.katakana = katakana

print(kana_char("hiragana.json", "hi"))
print(pair_chars("sa"))
