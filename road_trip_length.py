
import apiconnect
import httplib, urllib
import datetime
from datetime import date, timedelta
import json

today = datetime.date(2014, 5, 25)
todayString = '%s-%s-%s' % (today.year, today.month, today.day)
connection = httplib.HTTPSConnection('api.fantasydata.net')
key = '0deb8f835f264ad99e24cc3622aeb396'


def games_today(conn, date):
    conn = apiconnect.Connection()
    currentDate = date
    dateString = '%s-%s-%s' % (currentDate.year, currentDate.month, currentDate.day)
    data = conn.get_games_by_date(dateString)
    jn = json.loads(data)
    length = 0
    for index, key in enumerate(jn):
        length = 0
        awayTeam = jn[index]['AwayTeam']
        currentDate = date
        dateString = '%s-%s-%s' % (currentDate.year, currentDate.month, currentDate.day)
        x = isAway(conn, dateString, awayTeam)
        while x < 2:
            if x == 1:
                length = length + 1
            currentDate = currentDate - timedelta(days=1.0)
            dateString = '%s-%s-%s' % (currentDate.year, currentDate.month, currentDate.day)
            x = isAway(conn, dateString, awayTeam)
        print '%s on %s game of road trip' %(awayTeam, length)


def isAway(conn, date, team):
    holder = 0
    data = conn.get_team_game_stats_by_date(date)
    length = 1
    jn = json.loads(data)
    for dict in jn:
        if dict['Team'] == team:
            if dict['HomeOrAway'] == 'HOME':
                holder = 2
            if dict['HomeOrAway'] == 'AWAY':
                holder = 1
    return holder





if __name__ == "__main__":
    games_today(connection, today)