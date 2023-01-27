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
            "pssi": {
                "oui": 25,
                "non": 0
            },
            "know": {
                "4": 75,
                "3": 50,
                "2": 25,
                "1": 0,
            }
        }
        score = 0
        for name, value in input.items():
            score += answers[name][value]
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
