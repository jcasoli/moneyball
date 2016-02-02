import httplib, urllib, base64


class Connection:
    OcpApimSubscriptionKey = '0deb8f835f264ad99e24cc3622aeb396'
    http_loc = 'api.fantasydata.net'
    mlb_path = '/mlb/v2/JSON/'


    def get_connection(self):
    ########### Python 2.7 #############
        try:
            conn = httplib.HTTPSConnection('api.fantasydata.net')
            return conn
        except Exception as e:
            print("Could not create connection.. here is error: {}".format(e))

    def get_data(self, field, date, conn):
        conn.request("GET", Connection.mlb_path + field + "?key=" + Connection.OcpApimSubscriptionKey)
        response = conn.getresponse()
        data = response.read()
        return data
