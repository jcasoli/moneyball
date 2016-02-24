import api_connect
import connect
import httplib, urllib
import datetime
from datetime import date, timedelta
import json

today = datetime.date(2015, 5, 25)
todayString = '%s-%s-%s' % (today.year, today.month, today.day)
connection = httplib.HTTPSConnection('api.fantasydata.net')
key = '0deb8f835f264ad99e24cc3622aeb396'


def games_today(conn, date):
    conn = connect.Connection()
    dateString = '%s-%s-%s' % (date.year, date.month, date.day)
    data = conn.get_games_by_date(dateString)
    jn = json.loads(data)
    for index, key in enumerate(jn):
        awayTeam = jn[index]['AwayTeam']
        homeTeam = jn[index]['HomeTeam']
        batting_side(conn, dateString, homeTeam, awayTeam)

def batting_side(conn, date, homeTeam, awayTeam):
    numRightys = 0
    numLeftys = 0
    data = conn.get_projected_player_game_stats_by_date(date)
    jn = json.loads(data)
    pass
if __name__ == "__main__":
    games_today(connection, today)
