from flask import Flask, render_template, request, url_for, flash
from settings import scores, msgs


app = Flask(__name__)

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
    _leg1 = "?"
    _leg2 = "?"
    if request.method == 'POST':
        _leg1 = "pif"
        _leg2 = "pouf"
    return render_template('lrp.html', leg1=_leg1, leg2=_leg2)
