from flask import Flask, render_template # render_template for using HTML templates

app = Flask(__name__) #Create a App

@app.route('/') #  Creating A route
def index():
	# route '/' function
	return render_template('index.html') # you can use any name here like 'abcd.html' but the filename should be same you want to use.

if __name__ == '__main__':
	# for running app
	app.run()
