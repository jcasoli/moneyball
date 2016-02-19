
import apiconnect
import httplib, urllib
import datetime
from datetime import date, timedelta
import json

today = datetime.date(2015, 5, 25)
todayString = '%s-%s-%s' % (today.year, today.month, today.day)
conn = apiconnect.Connection()
key = '0deb8f835f264ad99e24cc3622aeb396'

def test_win_streak(homeTeam, awayTeam, conn, date):
    streak1 = 0
    streak2 = 0
    currentDate = date
    dateString = '%s-%s-%s' % (date.year, date.month, date.day)
    if (date.month<10 and date.day<10):
         dateString = '%s-0%s-0%s' % (date.year, date.month, date.day)
    if (date.month<10 and date.day>9):
         dateString = '%s-0%s-%s' % (date.year, date.month, date.day)
    if (date.month>9 and date.day<10):
         dateString = '%s-%s-%s' % (date.year, date.month, date.day)

#       Check Away Team Streak
    x = didWin(homeTeam, conn, dateString)
    while (x<2):
        if x == 1:
            streak1 = streak1 + 1
        currentDate = currentDate - timedelta(days=1.0)
        dateString = '%s-%s-%s' % (currentDate.year, currentDate.month, currentDate.day)
        x = didWin(homeTeam, conn, dateString)
    currentDate = date
    dateString = '%s-%s-%s' % (currentDate.year, currentDate.month, currentDate.day)
    x = didWin(awayTeam, conn, dateString)
    while (x<2):
        if x == 1:
            streak2 = streak2 + 1
        currentDate = currentDate - timedelta(days=1.0)
        dateString = '%s-%s-%s' % (currentDate.year, currentDate.month, currentDate.day)
        x = didWin(awayTeam, conn, dateString)
    return "%s win streak is at %s, %s win streak is at %s" % (homeTeam, streak1, awayTeam, streak2)

def test_pitching_today(homeTeam, awayTeam, conn, date,):
    homePitcher = ''
    awayPitcher = ''
    dateString = '%s-%s-%s' % (date.year, date.month, date.day)
    data = conn.get_games_by_date(dateString)
    jn = json.loads(data)
    for dict in jn:
        if dict['HomeTeam'] == homeTeam:
            homePitcher = dict['HomeTeamProbablePitcherID']
        if dict['AwayTeam'] == awayTeam:
            awayPitcher = dict['AwayTeamProbablePitcherID']
    return '%s is starting for %s against %s for %s' %(homePitcher, homeTeam, awayPitcher, awayTeam)

def test_trip_length(homeTeam, awayTeam, conn, date):
    currentDate = date
    dateString = '%s-%s-%s' % (currentDate.year, currentDate.month, currentDate.day)
    data = conn.get_games_by_date(dateString)
    jn = json.loads(data)
    length = 0
    currentDate = date
    dateString = '%s-%s-%s' % (currentDate.year, currentDate.month, currentDate.day)
    x = isAway(conn, dateString, awayTeam)
    while x < 2:
        if x == 1:
            length = length + 1
        currentDate = currentDate - timedelta(days=1.0)
        dateString = '%s-%s-%s' % (currentDate.year, currentDate.month, currentDate.day)
        x = isAway(conn, dateString, awayTeam)
    return '%s on %s game of road trip' %(awayTeam, length)

def didWin(team_id1, conn, date):
    data = conn.get_games_by_date(date)
    jn = json.loads(data)
    holder = 0
    for dict in jn:
        if dict['AwayTeam'] == team_id1 and dict['AwayTeamRuns'] > dict['HomeTeamRuns']:
            holder =  1
        if dict['AwayTeam'] == team_id1 and dict['AwayTeamRuns'] < dict['HomeTeamRuns']:
            holder =  2
        if dict['HomeTeam'] == team_id1 and dict['HomeTeamRuns'] < dict['AwayTeamRuns']:
            holder =  2
        if dict['HomeTeam'] == team_id1 and dict['HomeTeamRuns'] > dict['AwayTeamRuns']:
            holder = 1
    return holder

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

if __name__ == "__main__" :

    test_pitching_today("HOU", "TOR", conn, today)
    test_trip_length("HOU", "TOR", conn, today)
    test_win_streak("HOU", "TOR", conn, today)

