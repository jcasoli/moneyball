import httplib, urllib, base64


def pull_data():
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
        #conn.request("GET", "/mlb/v2/JSON/teams&%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
