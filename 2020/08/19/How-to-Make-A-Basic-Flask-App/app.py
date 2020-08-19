from flask import Flask # import flask Class from Flask Module

app = Flask(__name__) #Create a Flask app

@app.route('/') # create a Route for app.
def index():
	# Create a function for the route.
	return "Hello World" # we have to use return keyword to display the content for the route

if __name__ == '__main__':
	# If statement for that This File is Imported from another file or directly run from console.
	# if it is directly run it will automatically run the app. If is imported the in the main file we have to run it manually
	app.run()
