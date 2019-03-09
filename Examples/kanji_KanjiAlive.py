import requests

def kanji_get_KA(url):
    '''
    str -> None
    Writes json info about kanji from Kanji Alive app database into the file
    '''
    f = open('kanjsi.json', 'w', encoding='utf-8')
    page = requests.get(url, headers={
    "X-RapidAPI-Key": "3e4cc8eef5mshdf4d5f67002f09fp1b204fjsn9c8ca32999aa"}).content.decode('utf-8')
    f.write(str(page))
    print(page)


kanji_get("https://kanjialive-api.p.rapidapi.com/api/public/search/advanced/?kanji=%E8%A6%AA")
