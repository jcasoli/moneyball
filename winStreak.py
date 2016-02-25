import api_connect
import connect
import httplib, urllib
import datetime
from datetime import date, timedelta
import json

today = datetime.date(2014, 5, 5)
todayString = '%s-%s-%s' % (today.year, today.month, today.day)
connection = httplib.HTTPSConnection('api.fantasydata.net')
key = '0deb8f835f264ad99e24cc3622aeb396'


def games_today(conn, date):
    conn = connect.Connection()
#    conn.close_connection()
  #  print date
    dateString = '%s-%s-%s' % (date.year, date.month, date.day)
  #  if (date.month<10 and date.day<10):        Don't think I need all this just leaving it in case
   #      dateString = '%s-0%s-0%s' % (date.year, date.month, date.day)
   # if (date.month<10 and date.day>9):
   #      dateString = '%s-0%s-%s' % (date.year, date.month, date.day)
   # if (date.month>9 and date.day<10):
   #      dateString = '%s-%s-0%s' % (date.year, date.month, date.day)
#    cn = api_connect.Connection()
#    data = cn.get_data("GamesByDate", conn, dateString)
    data = conn.get_games_by_date(dateString)
    jn = json.loads(data)
    for index, key in enumerate(jn):
        awayTeam = jn[index]['AwayTeam']
        homeTeam = jn[index]['HomeTeam']
        win_streak(awayTeam, homeTeam, conn, date)


def win_streak(team_id1, team_id2, conn, date):
    streak1 = 0
    streak2 = 0
    currentDate = date
    dateString = '%s-%s-%s' % (date.year, date.month, date.day)
    if (date.month<10 and date.day<10):
         dateString = '%s-0%s-0%s' % (date.year, date.month, date.day)
    if (date.month<10 and date.day>9):
         dateString = '%s-0%s-%s' % (date.year, date.month, date.day)
    if (date.month>9 and date.day<10):
         dateString = '%s-%s-0%s' % (date.year, date.month, date.day)

#       Check Away Team Streak
    while didWin(team_id1, conn, dateString) == 0 or didWin(team_id1, conn, dateString) == 1:
        x = didWin(team_id1, conn, dateString)
#        print didWin(team_id1, conn, dateString)
#        print x
        if x == 1:
            streak1 = streak1 + 1
        currentDate = currentDate - timedelta(days=1.0)
        dateString = '%s-%s-%s' % (currentDate.year, currentDate.month, currentDate.day)

#       Check Home Team Streak
    currentDate = date
    dateString = '%s-%s-%s' % (currentDate.year, currentDate.month, currentDate.day)
    while didWin(team_id2, conn, dateString) == 0 or didWin(team_id2, conn, dateString) == 1:
        x = didWin(team_id2, conn, dateString)
#        print didWin(team_id1, conn, dateString)
 #       print x
        if x == 1:
  #          print "%s won" %(team_id2)
            streak2 = streak2 + 1
        currentDate = currentDate - timedelta(days=1.0)
        dateString = '%s-%s-%s' % (currentDate.year, currentDate.month, currentDate.day)
    print "%s win streak is at %s, %s win streak is at %s" % (team_id1, streak1, team_id2, streak2)




def didWin(team_id1, conn, date):
 #   cn = api_connect.Connection()
 #   data = cn.get_data("GamesByDate", conn, date)
#    print date
    conn = connect.Connection()
    data = conn.get_games_by_date(date)
    jn = json.loads(data)
    holder = 0
    for dict in jn:
        if dict['AwayTeam'] == team_id1 and dict['AwayTeamRuns'] > dict['HomeTeamRuns']:
       #     print dict['AwayTeamRuns']
   #         print team_id1 + "won + %s +  to  + %s" % (dict['AwayTeamRuns'], dict['HomeTeamRuns'])
            holder =  1
        if dict['AwayTeam'] == team_id1 and dict['AwayTeamRuns'] < dict['HomeTeamRuns']:
   #         print team_id1 + "lost + %s +  to  + %s" % (dict['AwayTeamRuns'], dict['HomeTeamRuns'])
            holder =  2
        if dict['HomeTeam'] == team_id1 and dict['HomeTeamRuns'] < dict['AwayTeamRuns']:
   #         print team_id1 + "lost + %s +  to  + %s" % (dict['HomeTeamRuns'], dict['AwayTeamRuns'])
            holder =  2
        if dict['HomeTeam'] == team_id1 and dict['HomeTeamRuns'] > dict['AwayTeamRuns']:
  #          print team_id1 + "won + %s +  to  + %s" % (dict['HomeTeamRuns'], dict['AwayTeamRuns'])
            holder = 1
#            print "%s won" %(team_id1)
#        else:
 #           print "no games for" + team_id1 + "that day"
 #           holder = 0
    return holder


if __name__ == "__main__":
    games_today(connection, today)
