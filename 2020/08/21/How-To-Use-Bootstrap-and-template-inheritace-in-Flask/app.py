from flask import Flask, render_template # render_template for using HTML templates
import random # For creating Random Numbers

app = Flask(__name__) #Create a App

@app.route('/') #  Creating A route
def index():
	# route '/' function
	return render_template('index.html', variable=random.randint(0,100), variable2=random.randint(-10000,10000), list1=['Python','Flask', 'Dynamic', 'HTML']) # you can use any name here like 'abcd.html' but the filename should be same you want to use.

if __name__ == '__main__':
	# for running app
	app.run()
