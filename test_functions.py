from __future__ import division
import apiconnect
import httplib, urllib
import datetime
from datetime import date, timedelta
import json

now = datetime.datetime.now()
today = datetime.date(now.year, now.month, now.day)
todayString = '%s-%s-%s' % (now.year, now.month, now.day)
conn = apiconnect.Connection()
key = '0deb8f835f264ad99e24cc3622aeb396'


def test_win_streak(homeTeam, awayTeam, conn, date):
    streak1 = 0
    streak2 = 0
    currentDate = date
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
    print "%s win streak is at %s, %s win streak is at %s" % (homeTeam, streak1, awayTeam, streak2)
    return "%s win streak is at %s, %s win streak is at %s" % (homeTeam, streak1, awayTeam, streak2)


def test_pitching_today(homeTeam, awayTeam, conn, date,):
    homePitcher = ''
    awayPitcher = ''
    dateString = '%s-%s-%s' % (date.year, date.month, date.day)
    data = conn.get_games_by_date(dateString)
    jn = json.loads(data)
    for dict in jn:
        if dict['HomeTeam'] == homeTeam:
            homePitcherID = dict['HomeTeamProbablePitcherID']
        if dict['AwayTeam'] == awayTeam:
            awayPitcherID = dict['AwayTeamProbablePitcherID']
    data1 = conn.get_player_details_by_player(str(homePitcherID))
    jn1 = json.loads(data1)
    homePitcherHand = ''
    awayPitcherHand = ''

    if jn1['ThrowHand'] == 'R':
        homePitcherHand = 'Right'
    else:
        homePitcherHand = 'Left'
    homePitcher = jn1['LastName']
    data2 = conn.get_player_details_by_player(str(awayPitcherID))
    jn2 = json.loads(data2)
    if jn2['ThrowHand'] == 'R':
        awayPitcherHand = 'Right'
    else:
        awayPitcherHand = 'Left'
    awayPitcher = jn2['LastName']


    print '%s is starting for %s against %s for %s' %(homePitcher, homeTeam, awayPitcher, awayTeam)


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
    print '%s on %s game of road trip' %(awayTeam, length)
    return '%s on %s game of road trip' %(awayTeam, length)


def test_batter_performance(homeTeam, awayTeam, conn, date, gameID):

    firstDayOfSeason = datetime.date(2015, 4, 5)
    currentDate = date
    daysSinceOpener = currentDate - firstDayOfSeason
    daysSinceOpenerInt = daysSinceOpener.days
    dateString = '%s-%s-%s' % (currentDate.year, currentDate.month, currentDate.day)

    currentDate = date
    battingOrder = get_batting_order(homeTeam, conn, dateString)
    battingOrderAway = get_batting_order(awayTeam, conn, dateString)
    data3 = conn.get_schedules('2015')
    jn3 = json.loads(data3)
    gameIDindex = 0
    gameIDArray=[]
    gameIDArrayAway=[]
    for index3, key3 in enumerate(jn3):
        if jn3[index3]['GameID'] == gameID:
            gameIDindex = index3
            gameIDindexAway = gameIDindex
    while gameIDindex>=0:
        if jn3[gameIDindex]['AwayTeam'] == homeTeam or jn3[gameIDindex]['HomeTeam'] == homeTeam:
            currentID = jn3[gameIDindex]['GameID']
            gameIDArray.append(currentID)
#            print jn3[gameIDindex]['Day']
        gameIDindex = gameIDindex-1
    while gameIDindexAway>=0:
        if jn3[gameIDindexAway]['AwayTeam'] == awayTeam or jn3[gameIDindexAway]['HomeTeam'] == awayTeam:
            currentID = jn3[gameIDindexAway]['GameID']
            gameIDArrayAway.append(currentID)
#            print jn3[gameIDindex]['Day']
        gameIDindexAway = gameIDindexAway-1


    x = game_performance(homeTeam, conn, dateString, battingOrder, gameIDArray)
    teamHitsAgainstRight = 0
    teamOutsAgainstRight = 0
    teamHitsAgainstLeft = 0
    teamOutsAgainstLeft = 0
    for i, item in enumerate(x):
        teamHitsAgainstRight = teamHitsAgainstRight + x[i][0]
        teamOutsAgainstRight  = teamOutsAgainstRight + x[i][1]
        teamHitsAgainstLeft = teamHitsAgainstLeft + x[i][2]
        teamOutsAgainstLeft = teamOutsAgainstLeft + x[i][3]
    teamAverageAgainstRight = teamHitsAgainstRight/(teamHitsAgainstRight+teamOutsAgainstRight)
    teamAverageAgainstLeft = teamHitsAgainstLeft/(teamHitsAgainstLeft+teamOutsAgainstLeft)
    print '%s has %s hits against righties and is batting %s' %(homeTeam, teamHitsAgainstRight, teamAverageAgainstRight)
    print '%s has %s hits against lefties and is batting %s' %(homeTeam, teamHitsAgainstLeft, teamAverageAgainstLeft)

    y = game_performance(awayTeam, conn, dateString, battingOrderAway, gameIDArrayAway)
    teamHitsAgainstRight = 0
    teamOutsAgainstRight = 0
    teamHitsAgainstLeft = 0
    teamOutsAgainstLeft = 0
    for i, item in enumerate(x):
        teamHitsAgainstRight = teamHitsAgainstRight + y[i][0]
        teamOutsAgainstRight  = teamOutsAgainstRight + y[i][1]
        teamHitsAgainstLeft = teamHitsAgainstLeft + y[i][2]
        teamOutsAgainstLeft = teamOutsAgainstLeft + y[i][3]
    teamAverageAgainstRight = teamHitsAgainstRight/(teamHitsAgainstRight+teamOutsAgainstRight)
    teamAverageAgainstLeft = teamHitsAgainstLeft/(teamHitsAgainstLeft+teamOutsAgainstLeft)
    print '%s Team has %s hits against righties and is batting %s' %(awayTeam, teamHitsAgainstRight, teamAverageAgainstRight)
    print '%s Team has %s hits against lefties and is batting %s' %(awayTeam, teamHitsAgainstLeft, teamAverageAgainstLeft)

def didWin(team_id1, conn, date):
    data = conn.get_games_by_date(date)
    jn = json.loads(data)
    holder = 0
    print '%s' %(date)
    for dict in jn:
        if dict['AwayTeam'] == team_id1 and dict['AwayTeamRuns'] > dict['HomeTeamRuns']:
            holder =  1
            print 'away team %s won' %(dict['AwayTeam'])
        if dict['AwayTeam'] == team_id1 and dict['AwayTeamRuns'] < dict['HomeTeamRuns']:
            holder =  2
        if dict['HomeTeam'] == team_id1 and dict['HomeTeamRuns'] < dict['AwayTeamRuns']:
            holder =  2
        if dict['HomeTeam'] == team_id1 and dict['HomeTeamRuns'] > dict['AwayTeamRuns']:
            holder = 1
            print 'home team %s won' %(dict['HomeTeam'])
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


def game_performance(team, conn, date, playerIDArray, gameIDArray):
    totalAB = [0,0,0,0]
    outsAgainstRighty = 0
    hitsAgainstRighty = 0
    hitsAgainstLefty = 0
    outsAgainstLefty = 0
    playerABArray = [[0 for x in range(4)] for x in range(9)]
    for i, game in enumerate(reversed(gameIDArray)):
#        print 'LOOPED!!!!'
        data2 = conn.get_play_by_play(gameIDArray[i])
        jn2 = json.loads(data2)
        ABlist = []
#        print len(ABlist)
        for j, player in enumerate(playerIDArray):
            x = 0
            outsAgainstRighty = 0
            hitsAgainstRighty = 0
            hitsAgainstLefty = 0
            outsAgainstLefty = 0
 #           print playerIDArray[j]
            for index2, key2 in enumerate(jn2):
                while x<len(jn2['Plays']):
                     if (jn2['Plays'][x]['HitterID']==playerIDArray[j]):
#                        print jn2['Plays'][x]['HitterName']
                        throwHand = jn2['Plays'][x]['PitcherThrowHand']
                        didOut = jn2['Plays'][x]['Out']
                        didHit = jn2['Plays'][x]['Hit']
                        didStrikeout = jn2['Plays'][x]['Strikeout']
                        if throwHand == 'R':
                            if didHit == True:
                                hitsAgainstRighty = hitsAgainstRighty+1
                            if didOut == True or didStrikeout == True:
                                outsAgainstRighty = outsAgainstRighty +1
                        if throwHand == 'L':
                            if didHit == True:
                                hitsAgainstLefty = hitsAgainstLefty+1
                            if didOut == True or didStrikeout == True:
                                outsAgainstLefty = outsAgainstLefty +1
                     x = x+1
            playerABArray[j][0] = hitsAgainstRighty + playerABArray[j][0]
            playerABArray[j][1] = outsAgainstRighty + playerABArray[j][1]
            playerABArray[j][2] = hitsAgainstLefty + playerABArray[j][2]
            playerABArray[j][3] = outsAgainstLefty + playerABArray[j][3]
            ABlist.append(hitsAgainstRighty)
            ABlist.append(outsAgainstRighty)
            ABlist.append(hitsAgainstLefty)
            ABlist.append(outsAgainstLefty)


     #       print 'had %s hits against right handers' %(hitsAgainstRighty)
     #       print 'had %s outs against right handers' %(outsAgainstRighty)
     #       print 'had %s hits against left handers' %(hitsAgainstLefty)
     #       print 'had %s outs against left handers' %(outsAgainstLefty)
      #  print 'Hits on day against righty: %s '%hitsAgainstRighty
    return playerABArray

def get_batting_order(team, conn, date):
    data = conn.get_player_game_stats_by_date(date)
    jn = json.loads(data)
    length = len(jn)
    battingOrder = [None]*9
    battingOrderName = [None]*9
    x = 0
    while x < length:
        if jn[x]['Team'] == team:
            order = (jn[x]['BattingOrder'])
            if order>0 and order<10:
                order = order-1
                battingOrder[order] = jn[x]['PlayerID']
                battingOrderName[order] = jn[x]['Name']
        x = x+1
    print battingOrderName
    return battingOrder
   #for index, key in enumerate(jn):
       # if jn[index]['Team'] == team:
       #     pass


    pass
if __name__ == "__main__" :
    test_batter_performance("TOR", "BOS", conn, today, 17468)
    test_pitching_today("TOR", "BOS", conn, today)
    test_trip_length("TOR", "BOS", conn, today)
    test_win_streak("TOR", "BOS", conn, today)


