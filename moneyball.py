from flask import Flask, request, redirect, url_for
from flask import render_template

import forms
import testfactors

import datetime

app = Flask(__name__)
app.secret_key = "moneyball"

@app.route("/")
def home():
    return redirect(url_for('login'))

@app.route("/welcome", methods=['GET', 'POST'])
def welcome():
    global result
    test = testfactors.Test()
    result = test.run(datetime.datetime.now())
    form = forms.DateForm()
    if form.validate_on_submit():
        date = form.dt.data
        result = test.run(date)
        return render_template('welcome.html', result=result, form=form)
    return render_template('welcome.html', result=result, form=form)

@app.route("/results")
def results():
    gameid = request.args.get('gameid').encode('ascii', 'ignore')
    game = [match for match in result if str(match['GameID'])==gameid]
    return render_template('results.html', game=game[0])


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
    global result
    app.run(debug=True)