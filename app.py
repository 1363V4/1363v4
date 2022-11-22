from flask import Flask, render_template, request, url_for, flash


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
	
@app.route("/app_1", methods=('GET', 'POST'))
def app_1():
	flash("fuck")
	if request.method == 'POST':
		input = request.form['input']
		answers = {
			'Sopra': "Steria",
			'Eva': "BSSI !",
		}
		try:
			msg = answers[input]
		except:
			msg = "Bad input."
		flash(msg)
		
	return render_template('app_1.html')
	