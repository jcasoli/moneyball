from flask import Flask, request, redirect, url_for
from flask import render_template

import testfactors

app = Flask(__name__)
app.secret_key = "moneyball"


@app.route("/")
def home():
    return "Hello World"

@app.route("/welcome")
def welcome():
    test = testfactors.Test()

    return render_template('welcome.html', results=results)



#route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('welcome'))
    return render_template('login.html', error=error)


if __name__ == "__main__":
    app.run(debug=True)