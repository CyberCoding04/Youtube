from flask import Flask, render_template, request, redirect, session # it will redirect to the given url # we have to import this for handling request Method # render_template for using HTML templates
import random # For creating Random Numbers

app = Flask(__name__) #Create a App
app.config['SECRET_KEY'] = 'secret' #any key you want.

@app.route('/') #  Creating A route
def index():
	# route '/' function
	return render_template('index.html', variable=random.randint(0,100), variable2=random.randint(-10000,10000), list1=['Python','Flask', 'Dynamic', 'HTML']) # you can use any name here like 'abcd.html' but the filename should be same you want to use.

@app.route('/second', methods=["POST", "GET"]) # it will only allow POST Methods.
def second():
	if request.method == "POST":
		name = request.form.get('name') # request.form is for post methods and is a dictionary
		session['user_id'] = name
		return render_template('second.html', name=name) # lets Send the name data to the second.html file.
		# request.method is the way to get the method that the page is opened
	else:
		#return redirect('/') # we have to import redirect from flask module
		return redirect('/')

@app.route('/logout')
def logout():
	if 'user_id' in session:
		session.pop('user_id', None)
		return redirect('/')
		# If user is logged in logout user and redirect to '/' page
	else:
		return '/' # if not logged in display '/'

if __name__ == '__main__':
	# for running app
	app.run()
