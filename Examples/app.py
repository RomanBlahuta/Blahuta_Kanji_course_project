from flask import Flask, request, render_template
from modules.kanachar import KanaChar
from modules.kanaset import KanaSet, kanaSetUp
#from modules.kanjiset import KanjiSet
from modules.kanjiclass import Kanji
import json
import random


#Variables setUp
testinfo = []
right = ''
score = 0
qNum = 0
hiragana = kanaSetUp('hiragana.json', True)
katakana = kanaSetUp('katakana.json', False)

#Application
app = Flask(__name__)

#Home page
@app.route("/")
def home():
    return render_template('home.html')


#Basic info page
@app.route("/info", methods=['GET', 'POST'])
def introduction():
    return render_template('info.html')

####################

#Learn hiragana game
@app.route("/hiragana")
def hiraganaHome():
    return render_template('hiragana.html')

@app.route("/hiragana_table")
def hir_table():
    return render_template('hiraganaTable.html')

@app.route("/hlearn", methods=['GET', 'POST'])
def hiragana_learn():
    global testinfo
    global right
    global score
    global qNum
    global hiragana

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
            toask = hiragana.getRandom()
            ask = test[qtype].format(toask.char)
            right = toask.sound
            options = []
            options.append(right)
            for i in range(3):
                a = hiragana.getRandom().sound
                while a == right:
                    a = hiragana.getRandom().sound
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
            toask = hiragana.getRandom()
            ask = test[qtype].format(toask.sound)
            right = toask.char
            options = []
            options.append(right)
            for i in range(3):
                a = hiragana.getRandom().char
                while a == right:
                    a = hiragana.getRandom().char
                options.append(a)
            A = random.choice(options)
            options.remove(A)
            B = random.choice(options)
            options.remove(B)
            C = random.choice(options)
            options.remove(C)
            D = random.choice(options)
            options.remove(D)

        return render_template('hiraganatest.html', num=qNum, question=ask, answer1=A, answer2=B, answer3=C, answer4=D)
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
            toask = hiragana.getRandom()
            ask = test[qtype].format(toask.char)
            right = toask.sound
            options = []
            options.append(right)
            for i in range(3):
                a = hiragana.getRandom().sound
                while a == right:
                    a = hiragana.getRandom().sound
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
            toask = hiragana.getRandom()
            ask = test[qtype].format(toask.sound)
            right = toask.char
            options = []
            options.append(right)
            for i in range(3):
                a = hiragana.getRandom().char
                while a == right:
                    a = hiragana.getRandom().char
                options.append(a)
            A = random.choice(options)
            options.remove(A)
            B = random.choice(options)
            options.remove(B)
            C = random.choice(options)
            options.remove(C)
            D = random.choice(options)
            options.remove(D)

        return render_template('hiraganatest.html', num=qNum, question=ask, answer1=A, answer2=B, answer3=C, answer4=D)

####################

#Learn katakana game
@app.route("/katakana")
def katakanaHome():
    return render_template('katakana.html')


@app.route("/katakana_table")
def kat_table():
    return render_template('katakanaTable.html')

@app.route("/klearn", methods=['GET', 'POST'])
def katakana_learn():
    global testinfo
    global right
    global score
    global qNum
    global katakana

    if qNum == 10:
        # Processing the answer
        if request.form['submit_button1'] == right:
            score += 1
            testinfo.append('{}){} -> ✓'.format(qNum, request.form['submit_button1']))
        else:
            score += 0
            testinfo.append('{}){} -> X'.format(qNum, request.form['submit_button1']))
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
            toask = katakana.getRandom()
            ask = test[qtype].format(toask.char)
            right = toask.sound
            options = []
            options.append(right)
            for i in range(3):
                a = katakana.getRandom().sound
                while a == right:
                    a = katakana.getRandom().sound
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
            toask = katakana.getRandom()
            ask = test[qtype].format(toask.sound)
            right = toask.char
            options = []
            options.append(right)
            for i in range(3):
                a = katakana.getRandom().char
                while a == right:
                    a = katakana.getRandom().char
                options.append(a)
            A = random.choice(options)
            options.remove(A)
            B = random.choice(options)
            options.remove(B)
            C = random.choice(options)
            options.remove(C)
            D = random.choice(options)
            options.remove(D)

        return render_template('katakanatest.html', num=qNum, question=ask, answer1=A, answer2=B, answer3=C, answer4=D)
    elif request.method == 'POST':
        #Processing the answer
        if request.form['submit_button1'] == right:
            score += 1
            testinfo.append('{}){} -> ✓'.format(qNum, request.form['submit_button1']))
        else:
            score += 0
            testinfo.append('{}){} -> X'.format(qNum, request.form['submit_button1']))
        # Set up values for test
        qNum += 1
        test = {1: 'What sound does the character {} stand for?',
                2: 'What character stands for the {} sound?'}
        qtype = random.randint(1, 2)

        # Build question of randomly chosen type
        if qtype == 1:
            toask = katakana.getRandom()
            ask = test[qtype].format(toask.char)
            right = toask.sound
            options = []
            options.append(right)
            for i in range(3):
                a = katakana.getRandom().sound
                while a == right:
                    a = katakana.getRandom().sound
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
            toask = katakana.getRandom()
            ask = test[qtype].format(toask.sound)
            right = toask.char
            options = []
            options.append(right)
            for i in range(3):
                a = katakana.getRandom().char
                while a == right:
                    a = katakana.getRandom().char
                options.append(a)
            A = random.choice(options)
            options.remove(A)
            B = random.choice(options)
            options.remove(B)
            C = random.choice(options)
            options.remove(C)
            D = random.choice(options)
            options.remove(D)

        return render_template('katakanatest.html', num=qNum, question=ask, answer1=A, answer2=B, answer3=C, answer4=D)

####################

'''
#Simultaneous hiragana and katakana learning game
@app.route("/kanas")
def kanas_learn():
    pass


#Kanji search
@app.route("/kanji#search")
def kanji_search():
    pass


#Learn Kanji game
@app.route("/kanji#learn")
def kanjiGame():
    pass

'''
if __name__ == '__main__':
    app.run()
