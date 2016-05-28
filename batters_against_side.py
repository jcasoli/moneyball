from __future__ import division
import apiconnect
import httplib, urllib
import datetime
from datetime import date, timedelta
import json


today = datetime.date(2015, 5, 2)
todayString = '%s-%s-%s' % (today.year, today.month, today.day)
conn = apiconnect.Connection()
key = '0deb8f835f264ad99e24cc3622aeb396'

def against_lefties(homeTeam, awayTeam, conn, date, gameID):

    firstDayOfSeason = datetime.date(2015, 4, 5)
    currentDate = date
    daysSinceOpener = currentDate - firstDayOfSeason
    daysSinceOpenerInt = daysSinceOpener.days
    dateString = '%s-%s-%s' % (currentDate.year, currentDate.month, currentDate.day)

    currentDate = date
    battingOrder = get_batting_order(homeTeam, conn, dateString)
    dayCounter = 0
    hitsAgainstRighty = 0
    ABlistTotal = [0, 0, 0, 0]
    holder = 0
    ABlistTotalTeam = [0, 0, 0, 0]

    while holder < len(battingOrder):
        ABlistTotal = [0, 0, 0, 0]
        dayCounter = 0
        currentDate = date
        averageAgainstRighty = 0
        averageAgainstLefty = 0
        while (dayCounter < daysSinceOpenerInt):
            x = game_performance(homeTeam, conn, dateString, battingOrder[holder])
            if x!=None:
                ABlistTotal[0]=ABlistTotal[0]+x[0]
                ABlistTotal[1]=ABlistTotal[1]+x[1]
                ABlistTotal[2]=ABlistTotal[2]+x[2]
                ABlistTotal[3]=ABlistTotal[3]+x[3]
                ABlistTotalTeam[0]=ABlistTotalTeam[0]+x[0]
                ABlistTotalTeam[1]=ABlistTotalTeam[1]+x[1]
                ABlistTotalTeam[2]=ABlistTotalTeam[2]+x[2]
                ABlistTotalTeam[3]=ABlistTotalTeam[3]+x[3]
            currentDate = currentDate - timedelta(days=1.0)
            dateString = '%s-%s-%s' % (currentDate.year, currentDate.month, currentDate.day)
            dayCounter = dayCounter+1
        if ABlistTotal[0]+ABlistTotal[1]>0:
            averageAgainstRighty = ABlistTotal[0]/(ABlistTotal[0]+ABlistTotal[1])
        if ABlistTotal[2]+ABlistTotal[3]:
            averageAgainstLefty = ABlistTotal[2]/(ABlistTotal[2]+ABlistTotal[3])
        print('Hits against Righty: %s') %ABlistTotal[0]
        print('Batting Against Right: %s') %(averageAgainstRighty)
        print('Batting Against Left: %s') %(averageAgainstLefty)
        holder = holder+1
    teamAverageAgainstRighty = ABlistTotalTeam[0]/(ABlistTotalTeam[0]+ABlistTotalTeam[1])
    teamAverageAgainstLefty = ABlistTotalTeam[2]/(ABlistTotalTeam[2]+ABlistTotalTeam[3])
    print 'Team is batting %s against righties' %(teamAverageAgainstRighty)
    print 'Team is batting %s against lefties' %(teamAverageAgainstLefty)
    print 'Team hits against righty %s' %(ABlistTotalTeam[0])
    print 'Team outs against righty %s' %(ABlistTotalTeam[1])


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

  #  for index, key in enumerate (jn):


def game_performance(team, conn, date, playerID):
    data = conn.get_games_by_date(date)
    jn1 = json.loads(data)
    gameID = 0
    for index, key in enumerate(jn1):
        if (team == jn1[index]['AwayTeam'] or team==jn1[index]['HomeTeam']):
            gameID = jn1[index]['GameID']
            print '%s on date %s' %(gameID, date)
    if (gameID==0):
        return
    data2 = conn.get_play_by_play(gameID)
    jn2 = json.loads(data2)
    outsAgainstRighty = 0
    hitsAgainstRighty = 0
    hitsAgainstLefty = 0
    outsAgainstLefty = 0
    ABlist = []
    print len(ABlist)
    x=0
    for index2, key2 in enumerate(jn2):
        print 'index2: %s' %(index2)
        while x<len(jn2['Plays']):
             if (jn2['Plays'][x]['HitterID']==playerID):
                print jn2['Plays'][x]['HitterName']
                throwHand = jn2['Plays'][x]['PitcherThrowHand']
                print jn2['Game']['HomeTeam']
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
    ABlist.append(hitsAgainstRighty)
    ABlist.append(outsAgainstRighty)
    ABlist.append(hitsAgainstLefty)
    ABlist.append(outsAgainstLefty)
    print 'had %s hits against right handers' %(hitsAgainstRighty)
#    print 'had %s outs against right handers' %(outsAgainstRighty)
#    print 'had %s hits against left handers' %(hitsAgainstLefty)
#    print 'had %s outs against left handers' %(outsAgainstLefty)
    return ABlist

def game_performance(team, conn, date, playerID):
    data = conn.get_games_by_date(date)
    jn1 = json.loads(data)
    gameID = 0
    for index, key in enumerate(jn1):
        if (team == jn1[index]['AwayTeam'] or team==jn1[index]['HomeTeam']):
            gameID = jn1[index]['GameID']
            print '%s on date %s' %(gameID, date)
    if (gameID==0):
        return
    data2 = conn.get_play_by_play(gameID)
    jn2 = json.loads(data2)
    outsAgainstRighty = 0
    hitsAgainstRighty = 0
    hitsAgainstLefty = 0
    outsAgainstLefty = 0
    ABlist = []
    print len(ABlist)
    x=0
    for index2, key2 in enumerate(jn2):
        print 'index2: %s' %(index2)
        while x<len(jn2['Plays']):
             if (jn2['Plays'][x]['HitterID']==playerID):
                print jn2['Plays'][x]['HitterName']
                throwHand = jn2['Plays'][x]['PitcherThrowHand']
                print jn2['Game']['HomeTeam']
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
    ABlist.append(hitsAgainstRighty)
    ABlist.append(outsAgainstRighty)
    ABlist.append(hitsAgainstLefty)
    ABlist.append(outsAgainstLefty)
    print 'had %s hits against right handers' %(hitsAgainstRighty)
#    print 'had %s outs against right handers' %(outsAgainstRighty)
#    print 'had %s hits against left handers' %(hitsAgainstLefty)
#    print 'had %s outs against left handers' %(outsAgainstLefty)
    return ABlist

if __name__ == "__main__":
    against_lefties("TOR", "BOS", conn, today, 17468)
