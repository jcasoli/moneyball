from flask import Flask, request, redirect, url_for
from flask import render_template
import api_connect
app = Flask(__name__)



@app.route("/")
def home():
    conn = api_connect.Connection.get_connection()



# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Invalid credentials for MONEYBALL.. please try again'
#         else:
#             return redirect(url_for('home'))
#     else:
#         return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run(debug=True)