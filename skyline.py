from flask import Flask, render_template, request
from foodie import send_file


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		email = request.form["email"]
		name = request.form["name"]
		place = request.form["place"]
		greet = "name:{} email:{} place:{}".format(name,email,place)
		send_file("food", email)
		return  greet

	return render_template('index.html')



if __name__ == "__main__":
	app.run()
