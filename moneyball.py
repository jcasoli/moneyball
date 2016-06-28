from flask import Flask, request, redirect, url_for, session
from flask import render_template, flash
from functools import wraps
from apscheduler.schedulers.background import BackgroundScheduler

import testfactors

import datetime

app = Flask(__name__)
app.secret_key = "moneyball"

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('login'))
        return wrap

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

    #TODO make result a dictionary by using gameid's as keys
    result = test.run(datetime.datetime.now().date())

    pass


@app.route("/")
def home():
    """
    Redirects to login page, people must login before they can see data
    :return: a redirect to login page
    """

    return redirect(url_for('login'))


@app.route("/welcome")
@login_required
def welcome():
    """
    renders page that shows listing of games and results, using the latest version of result.
    :return: welcome.html
    """

    return render_template('welcome.html', result=result)


@app.route("/results")
@login_required
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

    #TODO: make sure user has been authenticated before they get to see any other pages
    error = None
    if request.method == 'POST':

        # Check for correct login information
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            # Create a user session so we can password protect other endpoints
            session['logged_in'] = True
            flash('You were just logged in!')

            # Valid credentials, go to welcome
            return redirect(url_for('welcome'))

    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    """
    Logs the user out
    :return: A redirect to login page
    """

    # End the users session
    session.pop('logged_in', None)
    flash('You were just logged out!')

    # Send user back to login page
    return redirect(url_for('login'))

if __name__ == "__main__":
    global result
    result = []
    scheduler = BackgroundScheduler()
    scheduler.add_job(process, 'interval', seconds=2)
    scheduler.start()
    try:
        app.run(debug=True)
    except Exception as e:
        scheduler.shutdown()