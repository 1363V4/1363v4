from flask import Flask, render_template, request, url_for, flash, session, redirect
from settings import scores, msgs, twins, powers
from random import randint, choice
import os

app = Flask(__name__)
app.secret_key = os.getenv('secret_key')

# HOME
@app.route("/")
def index():
    return render_template('index.html')

#QUIZ V1
@app.route("/quiz/v1")
def quiz_v1():
    return render_template('v1/quiz.html')


@app.route("/quiz/v1/dcp", methods=('GET', 'POST'))
def quiz_questions_v1():
    if request.method == 'POST':
        input = request.form
        _scores = scores['dcp']
        score = 0
        for name, value in input.items():
            score += _scores[name][value]
        score = int(int((4*score)/14)*25)
        _msgs = msgs['dcp']
        msg = _msgs[score]
        return render_template(
            'v1/quiz_results.html',
            score=str(score),
            message=msg
            )
    return render_template('v1/quiz_questions.html')

#QUIZ V2
@app.route("/quiz/v2")
def quiz_v2():
    return render_template('v2/quiz.html')


@app.route("/quiz/v2/dcp", methods=('GET', 'POST'))
def quiz_questions_v2():
    if request.method == 'POST':
        input = request.form
        _scores = scores['dcp']
        score = 0
        for name, value in input.items():
            score += _scores[name][value]
        score = int(int((4*score)/14)*25)
        _msgs = msgs['dcp']
        msg = _msgs[score]
        return render_template(
            'v2/quiz_results.html',
            score=str(score),
            message=msg
            )
    return render_template('v2/quiz_questions.html')

# LRP
@app.route("/lrp", methods=('GET', 'POST'))
def lrp():
    _leg1 = 13
    _leg2 = 63
    if request.method == 'POST':
        _leg1 = randint(1, 105)
        _leg2 = randint(1, 105)
    return render_template('lrp.html', leg1=_leg1, leg2=_leg2)

# JML
@app.route("/jml", methods=('GET', 'POST'))
def jml():
    _win = False
    _etapes = 2
    if request.method == 'GET':
        _ville_d = choice([*twins])
        session['ogd'] = _ville_d
        _villes = twins[_ville_d]
        _temp = choice(twins[_ville_d])
        _ville_a = _ville_d
        while _ville_a == _ville_d:
            _ville_a = choice(twins[_temp])
        session['ville_a'] = _ville_a
        session['tries'] = 0
        session['steps'] = []
    if request.method == 'POST':
        session['tries'] += 1
        _ville_d = request.form['ville']
        session['steps'] += [_ville_d]
        _ville_a = session.get('ville_a', None)
        try:
            _villes = twins[_ville_d]
        except KeyError:
            _villes = ['pas encore fait']
        if _ville_d == _ville_a:
            _win = True
    return render_template(
        'jml.html',
        ville_d=_ville_d,
        ville_a=_ville_a,
        villes=_villes,
        etapes=_etapes,
        tries=session['tries'],
        ogd=session['ogd'],
        steps=session['steps'],
        win=_win)

_powers = [*powers]
# UM
@app.route("/um", methods=('GET', 'POST'))
def um():
    _players = {}
    _power = 0
    if request.method == 'POST':
        _player = request.form['player']
        if _player == 'reset':
            _powers = [*powers]
        elif _powers:
            _power = choice(_powers)
            _powers.remove(_power)
            _players[_player] = _power
        else:
            _power = 'no more powers!'
    return render_template(
        'um.html',
        power=_power,
        players=_players)

