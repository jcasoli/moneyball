
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
    dateString = '%s-%s-%s' % (date.year, date.month, date.day)
    data = conn.get_games_by_date(dateString)
    jn = json.loads(data)
    for index, key in enumerate(jn):
        awayTeam = jn[index]['AwayTeam']
        homeTeam = jn[index]['HomeTeam']
        pitching_today(conn, dateString, homeTeam, awayTeam)

def pitching_today(conn, date, homeTeam, awayTeam):
    homePitcher = ''
    awayPitcher = ''
    data = conn.get_games_by_date(date)
    jn = json.loads(data)
    for dict in jn:
        if dict['HomeTeam'] == homeTeam:
            homePitcherID = dict['HomeTeamProbablePitcherID']
        if dict['AwayTeam'] == awayTeam:
            awayPitcherID = dict['AwayTeamProbablePitcherID']
    data1 = conn.get_player_details_by_player(homePitcherID)
    jn2 = json.loads(data1)
    homePitcherHand = ''
    awayPitcherHand = ''

    for dict2 in jn2:
        if dict['ThrowHand']=='R':
            homePitcherHand = 'Right'
        else:
            homePitcherHand = 'Left'
        homePitcher = dict['LastName']
        data1 = conn.get_player_details_by_player(homePitcherID)
    jn2 = json.loads(data1)
    for dict2 in jn2:
        if dict['ThrowHand']=='R':
            awayPitcherHand = 'Right'
        else:
            awayPitcherHand = 'Left'
        awayPitcher = dict['LastName']

    print '%s is starting for %s against %s for %s' %(homePitcher, homeTeam, awayPitcher, awayTeam)

if __name__ == "__main__":
    games_today(connection, today)


