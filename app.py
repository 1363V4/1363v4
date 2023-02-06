from flask import Flask, render_template, request, url_for, flash


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/quiz")
def quiz():
    return render_template('quiz.html')


@app.route("/quiz/v1", methods=('GET', 'POST'))
def quiz_questions():
    if request.method == 'POST':
        input = request.form
        answers = {
            "dcp1": {
                "r11": 2,
                "r12": 1,
                "r13": 0,
            },
            "dcp2": {
                "r21": 2,
                "r22": 1,
                "r23": 0,
            },
            "dcp3": {
                "r31": 2,
                "r32": 1,
                "r33": 0,
            },
            "dcp4": {
                "r41": 2,
                "r42": 1,
                "r43": 0,
            },
            "dcp5": {
                "r51": 2,
                "r52": 1,
                "r53": 0,
            },
            "dcp6": {
                "r61": 2,
                "r62": 1,
                "r63": 0,
            },
            "dcp7": {
                "r71": 2,
                "r72": 1,
                "r73": 0,
            },
        }
        score = 0
        for name, value in input.items():
            score += answers[name][value]
        score = int(int((4*score)/14)*25)
        msgs = {
            100: "Très bien",
            75: "Bien",
            50: "Correct",
            25: "Pas top",
            0: "Faut consulter",
        }
        msg = msgs[score]
        return render_template(
            'quiz_results.html',
            score=str(score),
            message=msg
            )
    return render_template('quiz_questions.html')
