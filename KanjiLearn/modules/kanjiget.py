from modules.kanjiclass import Kanji
import requests
import json
import urllib.parse

def kanjiGet_KA(url):
    '''
    Helping function.
    Gets an API link for request.
    Returns json info about kanji from Kanji Alive app database.
    :param url: str
    :return: dict
    '''
    page = requests.get(url, headers={
    "X-RapidAPI-Key": "3e4cc8eef5mshdf4d5f67002f09fp1b204fjsn9c8ca32999aa"}).content.decode('utf-8')
    res = json.loads(page)
    return res


def kanjiGet_J(url):
    '''
    Helping function.
    Gets an API link for request.
    Returns json info about kanji from Jisho.org API.
    :param url: str
    :return: dict
    '''
    page = requests.get(url).content.decode('utf-8')
    res = json.loads(page)
    return res


def kanjiGetJap(kanji):
    '''
    Gets a kanji character as an argument.
    Constructs a Kanji object based on data gathered
    from Kanji Alive API and Jisho.org API.
    :param kanji: str
    :return: Kanji
    '''
    #Getting hieroglyph's details based on the character
    ka = kanjiGet_KA("https://kanjialive-api.p.rapidapi.com/api/public/kanji/" + urllib.parse.quote(kanji))
    #If kanji not found
    if str(ka) == "{'error': 'No kanji found.'}":
        raise ValueError
    jsh = kanjiGet_J('https://jisho.org/api/v1/search/words?keyword=' + str(kanji))
    #If kanji not found
    if str(jsh) == "{'meta': {'status': 200}, 'data': []}":
        raise ValueError

    #Setting up values
    character = ka['kanji']['character']
    meanings = ka['kanji']['meaning']['english'].split(',')

    readings = {'onyomi': None, 'kunyomi': None}
    readings['onyomi'] = ka['kanji']['onyomi']
    readings['kunyomi'] = ka['kanji']['kunyomi']

    parts_of_speech = jsh['data'][0]['senses'][0]['parts_of_speech']
    radical = ka['radical']['character']

    #Creating the object to return
    result = Kanji(character, meanings, readings, parts_of_speech, radical)
    return result




def kanjiGetEng(word):
    '''
    Gets an English word as an argument.
    Constructs a Kanji object based on data gathered
    from Kanji Alive API and Jisho.org API.
    :param kanji: str
    :return: Kanji
    '''
    #Requesting for hieroglyph character by English meaning
    getcharfrom = kanjiGet_KA('https://kanjialive-api.p.rapidapi.com/api/public/search/advanced/?kem=' + str(word))
    #If kanji not found
    if str(getcharfrom) == '[]':
        raise ValueError
    searchKanji = getcharfrom[0]['kanji']['character']

    #Getting hieroglyph's details based on the character
    ka = kanjiGet_KA("https://kanjialive-api.p.rapidapi.com/api/public/kanji/" + urllib.parse.quote(searchKanji))
    #If kanji not found
    if str(ka) == "{'error': 'No kanji found.'}":
        raise ValueError
    jsh = kanjiGet_J('https://jisho.org/api/v1/search/words?keyword=' + str(searchKanji))
    #If kanji not found
    if str(jsh) == "{'meta': {'status': 200}, 'data': []}":
        raise ValueError

    #Setting up values
    character = ka['kanji']['character']
    meanings = ka['kanji']['meaning']['english'].split(',')

    readings = {'onyomi': None, 'kunyomi': None}
    readings['onyomi'] = ka['kanji']['onyomi']
    readings['kunyomi'] = ka['kanji']['kunyomi']

    parts_of_speech = jsh['data'][0]['senses'][0]['parts_of_speech']
    radical = ka['radical']['character']

    #Creating the object to return
    result = Kanji(character, meanings, readings, parts_of_speech, radical)
    return result
