# -*- coding: utf-8 -*-
# By @nogagmx
from flask import Flask, render_template,render_template_string, request
app = Flask(__name__)
@app.route("/")
def index():
	return render_template('index.html')

@app.route("/register")
def process():
	blacklist = ["__class__", "__","."]
	name = request.args.get('name')
	for bad_string in blacklist:
	if bad_string in name:
		err_temp = '<!DOCTYPE html><html><body><h2>Intento de hackeo detectado por el uso de: %s </h2></body></html>' % bad_string
		return render_template_string(err_temp)

	template = '<!DOCTYPE html><html><body><h2>Bienvenido %s! </h2></body></html>' % name
	return render_template_string(template)

if __name__ == "__main__":
	app.run(host= '0.0.0.0')
