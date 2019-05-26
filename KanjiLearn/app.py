from flask import Flask, request, render_template
from modules.kanachar import KanaChar
from modules.kanaset import KanaSet, kanaSetUp
from modules.kanjiget import kanjiGetEng, kanjiGetJap
from modules.kanjiset import KanjiSet
from modules.kanjiclass import Kanji
import json
import random


#Variables setUp
testchoice = None                             #Value replaced by needed KanjiSet or KanaSet or str flag for Learn Both Kana game
testinfo = []                                 #User's answers
right = ''                                    #Variable for saving the right answer of current question
score = 0                                     #User's score in the current test
qNum = 0                                      #Number of current question
hiragana = kanaSetUp('hiragana.json', True)   #KanaSet for learning hiragana game
katakana = kanaSetUp('katakana.json', False)  #KanaSet for learning katakana game
tempSearchResult = None                       #Variable for temporary daving of searched Kanji object
toLearn = []                                  #List of str characters in 'To Learn List'
toLearnObjects = []                           #List of Kanji objects for initialization of KanjiSet for learning kanji game

#Application
app = Flask(__name__)

#Home page
@app.route("/")
def home():
    '''
    Function for rendering the template of home page route.
    :return: rendering html template
    '''
    return render_template('home.html')

#Error handling message route
@app.route("/error")
def errorRoute():
    '''
    Function for rendering the template with ERROR handling message.
    :return: rendering html template
    '''
    return render_template("ErrorOccurred.html")

#Basic info page
@app.route("/info", methods=['GET', 'POST'])
def introduction():
    '''
    Function for rendering the basic info page.
    :return: rendering html template
    '''
    return render_template('info.html')

####################

#Search kanji with English or Japanese words
@app.route("/search", methods=['GET', 'POST'])
def kanjiSearch():
    '''
    Function for rendering the template with search options.
    :return: rendering html template
    '''
    return render_template("searchKanji.html")

@app.route("/searchE", methods=['GET', 'POST'])
def kanjiSearchE():
    '''
    Function for rendering the English search option template.
    Also handles the search itself.
    :return: rendering html template
    '''
    global tempSearchResult
    if request.method == 'POST':
        kanjiobj = Kanji(None, None, None, None, None)
        try:
            tosearch = str(request.form['search']).strip()
            kanjiobj = kanjiGetEng(tosearch)
            dikt = kanjiobj.readings
            reads = []
            for k in dikt:
                q = str(dikt[k]).replace("'", "")
                reads.append(k + ':' + q)
            strpart = ', '.join(kanjiobj.parts_of_speech)
            strmeanings = ', '.join(kanjiobj.meanings)
            tempSearchResult = kanjiobj
        except:
            return render_template('ErrorOccurred.html')
        return render_template("searchResult.html", character=kanjiobj.character, meanings=strmeanings,
                           readings=reads, parts_of_speech=strpart,
                           radical=kanjiobj.radical)
    return render_template("searchEng.html")

@app.route("/searchJ", methods=['GET', 'POST'])
def kanjiSearchJ():
    '''
    Function for rendering the Japanese search option template.
    Also handles the search itself.
    :return: rendering html template
    '''
    global tempSearchResult
    if request.method == 'POST':
        kanjiobj = Kanji(None, None, None, None, None)
        try:
            tosearch = str(request.form['search']).strip()
            kanjiobj = kanjiGetJap(tosearch)
            dikt = kanjiobj.readings
            reads = []
            for k in dikt:
                q = str(dikt[k]).replace("'", "")
                reads.append(k + ':' + q)
            strpart = ', '.join(kanjiobj.parts_of_speech)
            strmeanings = ', '.join(kanjiobj.meanings)
            tempSearchResult = kanjiobj
        except:
            return render_template('ErrorOccurred.html')
        return render_template("searchResult.html", character=kanjiobj.character, meanings=strmeanings,
                           readings=reads, parts_of_speech=strpart,
                           radical=kanjiobj.radical)
    return render_template("searchJap.html")

####################

#Learning list viewing and editing
@app.route('/list', methods=["GET", "POST"])
def learnList():
    '''
    Function for handling the Learning List route template
    and list's randomization and new str submits.
    :return: rendering html template
    '''
    global tempSearchResult
    global toLearn
    global toLearnObjects
    if request.method == 'POST':

        if request.form['editlist'] == 'Add to List':
            if tempSearchResult not in toLearnObjects and str(tempSearchResult) not in toLearn:
                toLearn.append(str(tempSearchResult))
                toLearnObjects.append(tempSearchResult)

        elif request.form['editlist'] == 'Randomize':
            toLearn = []
            toLearnObjects = []
            randomCharsFile = open('commonKanji.txt', 'r', encoding='utf-8')
            randomChars = randomCharsFile.readline()
            while len(toLearnObjects) < 10 and len(toLearn) < 10:
                try:
                    char = random.choice(randomChars)
                    if char in toLearn:
                        raise ValueError
                    else:
                        charObj = kanjiGetJap(char)
                        toLearnObjects.append(charObj)
                        toLearn.append(char)
                except:
                    pass

        elif request.form['editlist'] == 'Submit new list':
            toLearn = []
            toLearnObjects = []
            new = request.form['newList']
            for i in new:
                try:
                    if i in toLearn:
                        raise ValueError
                    else:
                        gotkanji = kanjiGetJap(i)
                        toLearnObjects.append(gotkanji)
                        toLearn.append(str(i))
                except:
                    pass
    return render_template("learnList.html", kanjiList="{{  " + "  ||  ".join(toLearn) + "  }}")

####################

#Learn kanji
@app.route("/kanjistart")
def kanji_start():
    '''
    Function for setting up values for kanji test.
    Handles start of the test.
    :return: rendering html template
    '''
    global testchoice
    global testinfo
    global right
    global score
    global qNum
    global toLearnObjects
    testchoice = None
    testinfo = []
    right = ''
    score = 0
    qNum = 0
    testchoice = KanjiSet(toLearnObjects)
    return render_template('startKanji.html', kanjiList="{{  " + "  ||  ".join(toLearn) + "  }}")########################################  ACTUALLY START  ############

####################

#Learn hiragana
@app.route("/hiragana")
def hiraganaHome():
    '''
    Function for route with transitions to hiragana test and table
    :return: rendering html template
    '''
    return render_template('hiragana.html')

@app.route("/hiragana_table")
def hir_table():
    '''
    Function for route with katakana table template
    :return: rendering html template
    '''
    return render_template('hiraganaTable.html')

@app.route("/hstart")
def hir_start():
    '''
    Function for setting up values for hiragana test.
    Handles start of the test.
    :return: rendering html template
    '''
    global testchoice
    global hiragana
    global testinfo
    global right
    global score
    global qNum
    testchoice = None
    testinfo = []
    right = ''
    score = 0
    qNum = 0
    testchoice = hiragana
    return render_template('startHiragana.html')

####################

#Learn katakana
@app.route("/katakana")
def katakanaHome():
    '''
    Function for route with transitions to katakana test and table
    :return: rendering html template
    '''
    return render_template('katakana.html')


@app.route("/katakana_table")
def kat_table():
    '''
    Function for route with katakana table template
    :return: rendering html template
    '''
    return render_template('katakanaTable.html')

@app.route("/kstart")
def kat_start():
    '''
    Function for setting up values for katakana test.
    Handles start of the test.
    :return: rendering html template
    '''
    global testchoice
    global katakana
    global testinfo
    global right
    global score
    global qNum
    testchoice = None
    testinfo = []
    right = ''
    score = 0
    qNum = 0
    testchoice = katakana
    return render_template('startKatakana.html')

####################

#Simultaneous kana learning
@app.route("/twokanas")
def two_kana():
    '''
    Function for rendering template with transitions to hiragana
    and katakana table routes and test with both kana
    :return: rendering html template
    '''
    return render_template('twoKana.html')

@app.route("/twostart")
def twostart():
    '''
    Function for setting up values for both kana test.
    Handles start of the test.
    :return: rendering html template
    '''
    global testchoice
    global testinfo
    global right
    global score
    global qNum
    testchoice = None
    testinfo = []
    right = ''
    score = 0
    qNum = 0
    testchoice = "bothKanaFlag"
    return render_template("startTwoKana.html")

####################

#The tests
@app.route("/learn", methods=['GET', 'POST'])
def learn():
    '''
    Function for handling the learning tests
    :return: rendering html template
    '''
    global testinfo
    global hiragana
    global katakana
    global right
    global score
    global qNum
    global testchoice
    global toLearnObjects

    if isinstance(testchoice, KanaSet):

        if qNum == 10:
            # Processing the answer
            if request.form['submit_button'] == right:
                score += 1
                testinfo.append('{}){} -> ✓'.format(qNum, request.form['submit_button']))
            else:
                score += 0
                testinfo.append('{}){} -> X'.format(qNum, request.form['submit_button']))
            return render_template('result.html', result=score, full=qNum, testinfo=testinfo)

        if request.method == 'GET':
            testinfo = []
            right = ''
            score = 0
            qNum = 0
            # Set up values for test
            qNum += 1
            test = {1: 'What sound does the character {} stand for?',
                    2: 'What character stands for the {} sound?'}
            qtype = random.randint(1, 2)

            # Build question of randomly chosen type
            if qtype == 1:
                toask = testchoice.getRandom()
                ask = test[qtype].format(toask.char)
                right = toask.sound
                options = []
                options.append(right)
                for i in range(3):
                    a = testchoice.getRandom().sound
                    while a == right or a in options:
                        a = testchoice.getRandom().sound
                    options.append(a)
                A = random.choice(options)
                options.remove(A)
                B = random.choice(options)
                options.remove(B)
                C = random.choice(options)
                options.remove(C)
                D = random.choice(options)
                options.remove(D)

            elif qtype == 2:
                toask = testchoice.getRandom()
                ask = test[qtype].format(toask.sound)
                right = toask.char
                options = []
                options.append(right)
                for i in range(3):
                    a = testchoice.getRandom().char
                    while a == right or a in options:
                        a = testchoice.getRandom().char
                    options.append(a)
                A = random.choice(options)
                options.remove(A)
                B = random.choice(options)
                options.remove(B)
                C = random.choice(options)
                options.remove(C)
                D = random.choice(options)
                options.remove(D)

            return render_template('gametest.html', num=qNum, question=ask, answer1=A, answer2=B, answer3=C, answer4=D)

        elif request.method == 'POST':
            #Processing the answer
            if request.form['submit_button'] == right:
                score += 1
                testinfo.append('{}){} -> ✓'.format(qNum, request.form['submit_button']))
            else:
                score += 0
                testinfo.append('{}){} -> X'.format(qNum, request.form['submit_button']))
            # Set up values for test
            qNum += 1
            test = {1: 'What sound does the character {} stand for?',
                    2: 'What character stands for the {} sound?'}
            qtype = random.randint(1, 2)

            # Build question of randomly chosen type
            if qtype == 1:
                toask = testchoice.getRandom()
                ask = test[qtype].format(toask.char)
                right = toask.sound
                options = []
                options.append(right)
                for i in range(3):
                    a = testchoice.getRandom().sound
                    while a == right or a in options:
                        a = testchoice.getRandom().sound
                    options.append(a)
                A = random.choice(options)
                options.remove(A)
                B = random.choice(options)
                options.remove(B)
                C = random.choice(options)
                options.remove(C)
                D = random.choice(options)
                options.remove(D)

            elif qtype == 2:
                toask = testchoice.getRandom()
                ask = test[qtype].format(toask.sound)
                right = toask.char
                options = []
                options.append(right)
                for i in range(3):
                    a = testchoice.getRandom().char
                    while a == right or a in options:
                        a = testchoice.getRandom().char
                    options.append(a)
                A = random.choice(options)
                options.remove(A)
                B = random.choice(options)
                options.remove(B)
                C = random.choice(options)
                options.remove(C)
                D = random.choice(options)
                options.remove(D)

            return render_template('gametest.html', num=qNum, question=ask, answer1=A, answer2=B, answer3=C, answer4=D)


    elif isinstance(testchoice, KanjiSet):

        if len(toLearnObjects) < 8:
            return render_template('tooShort.html', length=len(toLearnObjects))

        if qNum == 10:
            # Processing the answer
            if request.form['submit_button'] == right:
                score += 1
                testinfo.append('{}){} -> ✓'.format(qNum, request.form['submit_button']))
            else:
                score += 0
                testinfo.append('{}){} -> X'.format(qNum, request.form['submit_button']))
            return render_template('result.html', result=score, full=qNum, testinfo=testinfo)

        if request.method == 'GET':
            testinfo = []
            right = ''
            score = 0
            qNum = 0
            # Set up values for test
            qNum += 1
            test = {1: 'What is the one of the meanings of {} kanji?',
                    2: 'What is the kunyomi of {} ?',
                    3: 'What is the onyomi of {} ?',
                    4: 'Do the {} and {} kanji have a common radical?',
                    5: 'Which kanji has the {} radical?',
                    6: 'What is the radical of {} ?'}
            qtype = random.randint(1, 6)

            # Build question of randomly chosen type
            if qtype == 1:
                toask = testchoice.getRandom()
                ask = test[qtype].format(toask.character)
                right = toask.meanings[0]
                options = []
                options.append(right)
                for i in range(3):
                    a = testchoice.getRandom().meanings[0]
                    while a == right or a in options:
                        a = testchoice.getRandom().meanings[0]
                    options.append(a)
                A = random.choice(options)
                options.remove(A)
                B = random.choice(options)
                options.remove(B)
                C = random.choice(options)
                options.remove(C)
                D = random.choice(options)
                options.remove(D)

            elif qtype == 2:
                toask = testchoice.getRandom()
                ask = test[qtype].format(toask.character)
                right = toask.getKunyomi()
                options = []
                options.append(right)
                for i in range(3):
                    a = testchoice.getRandom().getKunyomi()
                    while a == right or a in options:
                        a = testchoice.getRandom().getKunyomi()
                    options.append(a)
                A = random.choice(options)
                options.remove(A)
                B = random.choice(options)
                options.remove(B)
                C = random.choice(options)
                options.remove(C)
                D = random.choice(options)
                options.remove(D)

            elif qtype == 3:
                toask = testchoice.getRandom()
                ask = test[qtype].format(toask.character)
                right = toask.getOnyomi()
                options = []
                options.append(right)
                for i in range(3):
                    a = testchoice.getRandom().getOnyomi()
                    while a == right or a in options:
                        a = testchoice.getRandom().getOnyomi()
                    options.append(a)
                A = random.choice(options)
                options.remove(A)
                B = random.choice(options)
                options.remove(B)
                C = random.choice(options)
                options.remove(C)
                D = random.choice(options)
                options.remove(D)

            elif qtype == 4:
                toask1 = testchoice.getRandom()
                toask2 = testchoice.getRandom()
                ask = test[qtype].format(toask1.character, toask2.character)
                right = toask1.commonRadical(toask2)
                false = not right
                options = []
                options.append(right)
                options.append(false)
                A = random.choice(options)
                options.remove(A)
                B = random.choice(options)
                options.remove(B)
                C = 404
                D = 404

            elif qtype == 5:
                toask = testchoice.getRandom()
                ask = test[qtype].format(toask.radical)
                right = toask.character
                options = []
                options.append(right)
                for i in range(3):
                    a = testchoice.getRandom().character
                    while a == right or a in options:
                        a = testchoice.getRandom().character
                    options.append(a)
                A = random.choice(options)
                options.remove(A)
                B = random.choice(options)
                options.remove(B)
                C = random.choice(options)
                options.remove(C)
                D = random.choice(options)
                options.remove(D)

            elif qtype == 6:
                toask = testchoice.getRandom()
                ask = test[qtype].format(toask.character)
                right = toask.radical
                options = []
                options.append(right)
                for i in range(3):
                    a = testchoice.getRandom().radical
                    while a == right or a in options:
                        a = testchoice.getRandom().radical
                    options.append(a)
                A = random.choice(options)
                options.remove(A)
                B = random.choice(options)
                options.remove(B)
                C = random.choice(options)
                options.remove(C)
                D = random.choice(options)
                options.remove(D)

            return render_template('gametest.html', num=qNum, question=ask, answer1=A, answer2=B, answer3=C, answer4=D)

        elif request.method == 'POST':
            #Processing the answer
            if request.form['submit_button'] == right:
                score += 1
                testinfo.append('{}){} -> ✓'.format(qNum, request.form['submit_button']))
            else:
                score += 0
                testinfo.append('{}){} -> X'.format(qNum, request.form['submit_button']))
            # Set up values for test
            qNum += 1
            test = {1: 'What is the one of the meanings of {} kanji?',
                    2: 'What is the kunyomi of {} ?',
                    3: 'What is the onyomi of {} ?',
                    4: 'Do the {} and {} kanji have a common radical?',
                    5: 'Which kanji has the {} radical?',
                    6: 'What is the radical of {} ?'}
            qtype = random.randint(1, 6)

            # Build question of randomly chosen type
            if qtype == 1:
                toask = testchoice.getRandom()
                ask = test[qtype].format(toask.character)
                right = toask.meanings[0]
                options = []
                options.append(right)
                for i in range(3):
                    a = testchoice.getRandom().meanings[0]
                    while a == right or a in options:
                        a = testchoice.getRandom().meanings[0]
                    options.append(a)
                A = random.choice(options)
                options.remove(A)
                B = random.choice(options)
                options.remove(B)
                C = random.choice(options)
                options.remove(C)
                D = random.choice(options)
                options.remove(D)

            elif qtype == 2:
                toask = testchoice.getRandom()
                ask = test[qtype].format(toask.character)
                right = toask.getKunyomi()
                options = []
                options.append(right)
                for i in range(3):
                    a = testchoice.getRandom().getKunyomi()
                    while a == right or a in options:
                        a = testchoice.getRandom().getKunyomi()
                    options.append(a)
                A = random.choice(options)
                options.remove(A)
                B = random.choice(options)
                options.remove(B)
                C = random.choice(options)
                options.remove(C)
                D = random.choice(options)
                options.remove(D)

            elif qtype == 3:
                toask = testchoice.getRandom()
                ask = test[qtype].format(toask.character)
                right = toask.getOnyomi()
                options = []
                options.append(right)
                for i in range(3):
                    a = testchoice.getRandom().getOnyomi()
                    while a == right or a in options:
                        a = testchoice.getRandom().getOnyomi()
                    options.append(a)
                A = random.choice(options)
                options.remove(A)
                B = random.choice(options)
                options.remove(B)
                C = random.choice(options)
                options.remove(C)
                D = random.choice(options)
                options.remove(D)

            elif qtype == 4:
                toask1 = testchoice.getRandom()
                toask2 = testchoice.getRandom()
                ask = test[qtype].format(toask1.character, toask2.character)
                right = toask1.commonRadical(toask2)
                false = not right
                options = []
                options.append(right)
                options.append(false)
                A = random.choice(options)
                options.remove(A)
                B = random.choice(options)
                options.remove(B)
                C = 404
                D = 404

            elif qtype == 5:
                toask = testchoice.getRandom()
                ask = test[qtype].format(toask.radical)
                right = toask.character
                options = []
                options.append(right)
                for i in range(3):
                    a = testchoice.getRandom().character
                    while a == right or a in options:
                        a = testchoice.getRandom().character
                    options.append(a)
                A = random.choice(options)
                options.remove(A)
                B = random.choice(options)
                options.remove(B)
                C = random.choice(options)
                options.remove(C)
                D = random.choice(options)
                options.remove(D)

            elif qtype == 6:
                toask = testchoice.getRandom()
                ask = test[qtype].format(toask.character)
                right = toask.radical
                options = []
                options.append(right)
                for i in range(3):
                    a = testchoice.getRandom().radical
                    while a == right or a in options:
                        a = testchoice.getRandom().radical
                    options.append(a)
                A = random.choice(options)
                options.remove(A)
                B = random.choice(options)
                options.remove(B)
                C = random.choice(options)
                options.remove(C)
                D = random.choice(options)
                options.remove(D)

            return render_template('gametest.html', num=qNum, question=ask, answer1=A, answer2=B, answer3=C, answer4=D)

    elif isinstance(testchoice, str):

        if qNum == 10:
            # Processing the answer
            if request.form['submit_button'] == right:
                score += 1
                testinfo.append('{}){} -> ✓'.format(qNum, request.form['submit_button']))
            else:
                score += 0
                testinfo.append('{}){} -> X'.format(qNum, request.form['submit_button']))
            return render_template('result.html', result=score, full=qNum, testinfo=testinfo)

        if request.method == 'GET':
            testinfo = []
            right = ''
            score = 0
            qNum = 0
            # Set up values for test
            qNum += 1
            test = {1: 'What sound does the character {} stand for?',
                    2: 'What character stands for the {} sound?',
                    3: 'Which hiragana and katakana characters make the same sound?'}
            qtype = random.randint(1, 3)

            # Build question of randomly chosen type
            if qtype == 1:
                hir_Or_kat = random.choice([hiragana, katakana])
                toask = hir_Or_kat.getRandom()
                ask = test[qtype].format(toask.char)
                right = toask.sound
                options = []
                options.append(right)
                for i in range(3):
                    a = hir_Or_kat.getRandom().sound
                    while a == right or a in options:
                        a = hir_Or_kat.getRandom().sound
                    options.append(a)
                A = random.choice(options)
                options.remove(A)
                B = random.choice(options)
                options.remove(B)
                C = random.choice(options)
                options.remove(C)
                D = random.choice(options)
                options.remove(D)

            elif qtype == 2:
                hir_Or_kat = random.choice([hiragana, katakana])
                toask = hir_Or_kat.getRandom()
                ask = test[qtype].format(toask.sound)
                right = toask.char
                options = []
                options.append(right)
                for i in range(3):
                    a = hir_Or_kat.getRandom().char
                    while a == right or a in options:
                        a = hir_Or_kat.getRandom().char
                    options.append(a)
                A = random.choice(options)
                options.remove(A)
                B = random.choice(options)
                options.remove(B)
                C = random.choice(options)
                options.remove(C)
                D = random.choice(options)
                options.remove(D)

            elif qtype == 3:
                hir = hiragana
                kat = katakana
                toask1 = hir.getRandom()
                toask2 = kat.charBySound(toask1.sound)
                ask = test[qtype]
                right = toask1.char + ' , ' + toask2.char
                options = []
                options.append(right)
                for i in range(3):
                    a = hir.getRandom()
                    b = kat.getRandom()
                    while a.sound == b.sound or a.char + ' , ' + b.char in options:
                        a = hir.getRandom()
                        b = kat.getRandom()
                    theAnswer = a.char + ' , ' + b.char
                    options.append(theAnswer)
                A = random.choice(options)
                options.remove(A)
                B = random.choice(options)
                options.remove(B)
                C = random.choice(options)
                options.remove(C)
                D = random.choice(options)
                options.remove(D)

            return render_template('gametest.html', num=qNum, question=ask, answer1=A, answer2=B, answer3=C, answer4=D)

        elif request.method == 'POST':
            #Processing the answer
            if request.form['submit_button'] == right:
                score += 1
                testinfo.append('{}){} -> ✓'.format(qNum, request.form['submit_button']))
            else:
                score += 0
                testinfo.append('{}){} -> X'.format(qNum, request.form['submit_button']))
            # Set up values for test
            qNum += 1
            test = {1: 'What sound does the character {} stand for?',
                    2: 'What character stands for the {} sound?',
                    3: 'Which hiragana and katakana characters make the same sound?'}
            qtype = random.randint(1, 3)

            # Build question of randomly chosen type
            if qtype == 1:
                hir_Or_kat = random.choice([hiragana, katakana])
                toask = hir_Or_kat.getRandom()
                ask = test[qtype].format(toask.char)
                right = toask.sound
                options = []
                options.append(right)
                for i in range(3):
                    a = hir_Or_kat.getRandom().sound
                    while a == right or a in options:
                        a = hir_Or_kat.getRandom().sound
                    options.append(a)
                A = random.choice(options)
                options.remove(A)
                B = random.choice(options)
                options.remove(B)
                C = random.choice(options)
                options.remove(C)
                D = random.choice(options)
                options.remove(D)

            elif qtype == 2:
                hir_Or_kat = random.choice([hiragana, katakana])
                toask = hir_Or_kat.getRandom()
                ask = test[qtype].format(toask.sound)
                right = toask.char
                options = []
                options.append(right)
                for i in range(3):
                    a = hir_Or_kat.getRandom().char
                    while a == right or a in options:
                        a = hir_Or_kat.getRandom().char
                    options.append(a)
                A = random.choice(options)
                options.remove(A)
                B = random.choice(options)
                options.remove(B)
                C = random.choice(options)
                options.remove(C)
                D = random.choice(options)
                options.remove(D)

            elif qtype == 3:
                hir = hiragana
                kat = katakana
                toask1 = hir.getRandom()
                toask2 = kat.charBySound(toask1.sound)
                ask = test[qtype]
                right = toask1.char + ' , ' + toask2.char
                options = []
                options.append(right)
                for i in range(3):
                    a = hir.getRandom()
                    b = kat.getRandom()
                    while a.sound == b.sound or a.char + ' , ' + b.char in options:
                        a = hir.getRandom()
                        b = kat.getRandom()
                    theAnswer = a.char + ' , ' + b.char
                    options.append(theAnswer)
                A = random.choice(options)
                options.remove(A)
                B = random.choice(options)
                options.remove(B)
                C = random.choice(options)
                options.remove(C)
                D = random.choice(options)
                options.remove(D)

            return render_template('gametest.html', num=qNum, question=ask, answer1=A, answer2=B, answer3=C, answer4=D)


if __name__ == '__main__':
    app.run()
