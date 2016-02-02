from flask import Flask, request, redirect, url_for
from flask import render_template
import httplib
app = Flask(__name__)



@app.route("/")
def home():
    try:
        conn = httplib.HTTPSConnection('api.fantasydata.net')
        conn.request("GET", "/mlb/v2/JSON/TeamGameStatsByDate/2015-07-07?key=0deb8f835f264ad99e24cc3622aeb396")
        #conn.request("GET", "/mlb/v2/JSON/teams&%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    return data


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials for MONEYBALL.. please try again'
        else:
            return redirect(url_for('home'))
    else:
        return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run(debug=True)