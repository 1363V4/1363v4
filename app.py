from flask import Flask, render_template, request, url_for, flash


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
	
@app.route("/app_1", methods=('GET', 'POST'))
def app_1():
	if request.method == 'POST':
		...
		
	return render_template('app_1.html')
	