from flask import Flask, request, redirect, url_for
from flask import render_template
from apscheduler.schedulers.background import BackgroundScheduler

import testfactors

import datetime

app = Flask(__name__)
app.secret_key = "moneyball"


def process():
    # This method needs to be able to update the current analysis
    global result
    # Get instance of test class
    test = testfactors.Test()
    # Run analysis for all games on the current date
    result = test.run(datetime.datetime(2015, 8, 19))


# home route that immediately redirects to the login page
@app.route("/")
def home():
    # Go directly to login page
    return redirect(url_for('login'))

# route that displays all the games on a given night
@app.route("/welcome")
def welcome():
    # Render webpage with result (the latest version of result)
    return render_template('welcome.html', result=result)


# route for dislplaying the results of an analysis
@app.route("/results")
def results():
    # Get gameid from url parameter 'gameid'
    gameid = request.args.get('gameid').encode('ascii', 'ignore')
    # Get dictionary corresponding to the game that was clicked
    game = [match for match in result if str(match['GameID'])==gameid]
    # Display the webpage
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
    result = []
    scheduler = BackgroundScheduler()
    scheduler.add_job(process, 'interval', seconds=1)
    scheduler.start()
    try:
        app.run(debug=True)
    except Exception as e:
        scheduler.shutdown()