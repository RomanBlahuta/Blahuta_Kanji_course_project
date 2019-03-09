import requests

def kanji_get_J(url):
    '''
    str -> None
    Writes json info about kanji from Jisho.org into the file
    '''
    f = open('kanji.json', 'w', encoding='utf-8')
    page = requests.get(url).content.decode('utf-8')
    f.write(str(page))


kanji_get('https://jisho.org/api/v1/search/words?keyword=ice')
