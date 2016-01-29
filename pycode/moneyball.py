from flask import Flask
import httplib, urllib, base64
import json
app = Flask(__name__)



@app.route("/")
def hello():
    print("Hello World!")
    ########### Python 2.7 #############
    headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '0deb8f835f264ad99e24cc3622aeb396',
    }

    params = urllib.urlencode({
    })

    try:
        conn = httplib.HTTPSConnection('api.fantasydata.net')
        conn.request("GET", "/mlb/v2/JSON/teams?key=0deb8f835f264ad99e24cc3622aeb396")
        print('made it')
        #conn.request("GET", "/mlb/v2/JSON/teams&%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data
    except Exception as e:
        print("Fuck")
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

if __name__ == "__main__":
    app.run()