from flask import Flask, request, redirect, url_for
from flask import render_template
from apscheduler.schedulers.background import BackgroundScheduler

import testfactors

import datetime

app = Flask(__name__)
app.secret_key = "moneyball"


def process():
    """
    This function is scheduled to run every night at 2am. It is scheduled by an apscheduler
    :return: Updates the current value of result, which is the results of an analysis using api data
    """
    # This method needs to be able to update the current analysis
    global result
    # Get instance of test class
    test = testfactors.Test()
    # Run analysis for all games on the current date
    result = test.run(datetime.datetime(2015, 8, 19))


@app.route("/")
def home():
    """
    Redirects to login page, people must login before they can see data
    :return: a redirect to login page
    """

    return redirect(url_for('login'))


@app.route("/welcome")
def welcome():
    """
    renders page that shows listing of games and results, using the latest version of result.
    :return: welcome.html
    """

    return render_template('welcome.html', result=result)


@app.route("/results")
def results():
    """
    After a user has selected which game they are interested in seeing more about, they are redirected
    to this page, which shows the data behind the heatrating
    :return: results.html
    """

    # Get gameid from url parameter 'gameid'
    gameid = request.args.get('gameid').encode('ascii', 'ignore')

    # Get dictionary corresponding to the game that was clicked
    game = [match for match in result if str(match['GameID'])==gameid]

    return render_template('results.html', game=game[0])


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    The login page logic
    :return: welcome.html or login.html if failed login
    """
    error = None
    if request.method == 'POST':

        # Check for correct login information
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            # Valid credentials, go to welcome
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