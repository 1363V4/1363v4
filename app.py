from flask import Flask, render_template, request, url_for, flash


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
	
@app.route("/app_1", methods=('GET', 'POST'))
def app_1():
	output = "_"
	if request.method == 'POST':
		input = request.form['input']
		answers = {
			'Sopra': "Steria",
			'Eva': "BSSI !",
		}
		try:
			output = answers[input]
		except:
			output = "Bad input."
		output = "yes"
		return render_template('app_1.html', output=output)
		
	return render_template('app_1.html', output=output)
	