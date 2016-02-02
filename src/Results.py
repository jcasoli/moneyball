
import json
import httplib, urllib
from datetime import datetime
now = datetime.now()
today = '%s-%s-%s' % (now.year, now.month, now.day)
connection = httplib.HTTPSConnection('api.fantasydata.net')
key = '0deb8f835f264ad99e24cc3622aeb396'
def games_today(conn, date):
        conn.request("GET", "/mlb/v2/JSON/GamesByDate/%skey=0deb8f835f264ad99e24cc3622aeb396")(today)
        print('made it')
        #conn.request("GET", "/mlb/v2/JSON/teams&%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        jn = json.loads(data)
def win_streak(team_id1, team_id2, conn, date):
        pass

def team1_streak(team_id1, connection, date):
        pass

if __name__ == "__main__":
    win_streak(5, 5, connection, today)