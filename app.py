from flask import Flask, render_template, request
import codecs
from random import randint

with codecs.open('word_rus.txt', encoding='utf-8') as file:
    words = [row.strip() for row in file]
app = Flask(__name__)
@app.route("/")
def hello():
    global res1
    global res2
    global player
    global i
    global t
    res1 = 0
    res2 = 0
    i = randint(0,len(words))
    player = '1 player'
    return render_template('main.html', res1 = 0, res2 = 0, words = words, i = i, t = 20, player = player)
@app.route("/word", methods = ['GET', 'POST'])
def word():
    global res1
    global res2
    global player
    global i
    global t
    i = randint(0,len(words))
    if request.method == 'POST':
        t = request.form['time']
        if player == '1 player' and t != '':
            res1 += 1
        elif player == '2 player' and t != '':
            res2 += 1
        elif t == '' and player == '1 player':
            player = '2 player'
            t = 20
        elif t == '' and player == '2 player':
            player = '1 player'
            t = 20
    return render_template('main.html', res1 = res1, res2 = res2 ,words = words, i = i, t = t, player = player)
if __name__ == "__main__":
    app.run()
