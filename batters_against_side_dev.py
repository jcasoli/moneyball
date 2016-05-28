from __future__ import division
import apiconnect
import httplib, urllib
import datetime
from datetime import date, timedelta
import json


today = datetime.date(2015, 5, 8)
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
    data3 = conn.get_schedules('2015')
    jn3 = json.loads(data3)
    gameIDindex = 0
    gameIDArray=[]
    for index3, key3 in enumerate(jn3):
        if jn3[index3]['GameID'] == gameID:
            gameIDindex = index3
    while gameIDindex>=0:
        if jn3[gameIDindex]['AwayTeam'] == homeTeam or jn3[gameIDindex]['HomeTeam'] == homeTeam:
            currentID = jn3[gameIDindex]['GameID']
            gameIDArray.append(currentID)
            print jn3[gameIDindex]['Day']
        gameIDindex = gameIDindex-1

    while holder < len(battingOrder):
        ABlistTotal = [0, 0, 0, 0]
        dayCounter = 0
        currentDate = date
        averageAgainstRighty = 0
        averageAgainstLefty = 0

        x = game_performance(homeTeam, conn, dateString, battingOrder[holder], gameIDArray)
        if x!=None:
                ABlistTotal[0]=ABlistTotal[0]+x[0]
                ABlistTotal[1]=ABlistTotal[1]+x[1]
                ABlistTotal[2]=ABlistTotal[2]+x[2]
                ABlistTotal[3]=ABlistTotal[3]+x[3]
                ABlistTotalTeam[0]=ABlistTotalTeam[0]+x[0]
                ABlistTotalTeam[1]=ABlistTotalTeam[1]+x[1]
                ABlistTotalTeam[2]=ABlistTotalTeam[2]+x[2]
                ABlistTotalTeam[3]=ABlistTotalTeam[3]+x[3]

        if x[0]+x[1]>0:
            averageAgainstRighty = x[0]/(x[0]+x[1])
        if x[2]+x[3]:
            averageAgainstLefty = x[2]/(x[2]+x[3])
        print('Hits against Righty: %s') %x[0]
        print('Batting Against Right: %s') %(averageAgainstRighty)
        print('Batting Against Left: %s') %(averageAgainstLefty)
        holder = holder+1
    teamAverageAgainstRighty = ABlistTotalTeam[0]/(ABlistTotalTeam[0]+ABlistTotalTeam[1])
    teamAverageAgainstLefty = ABlistTotalTeam[2]/(ABlistTotalTeam[2]+ABlistTotalTeam[3])
    print 'Team had %s hits against righties' %(ABlistTotalTeam[0])
    print 'Team had %s outs against righties' %(ABlistTotalTeam[1])
    print 'Team is batting %s against righties' %(teamAverageAgainstRighty)
    print 'Team is batting %s against lefties' %(teamAverageAgainstLefty)


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


def game_performance(team, conn, date, playerID, gameIDArray):
    totalAB = [0,0,0,0]
    for i, game in enumerate(reversed(gameIDArray)):
        data2 = conn.get_play_by_play(gameIDArray[i])
        jn2 = json.loads(data2)
        outsAgainstRighty = 0
        hitsAgainstRighty = 0
        hitsAgainstLefty = 0
        outsAgainstLefty = 0
        ABlist = []
        print len(ABlist)
        x=0
        for index2, key2 in enumerate(jn2):
            while x<len(jn2['Plays']):
                    if (jn2['Plays'][x]['HitterID']==playerID):
                        print jn2['Plays'][x]['HitterName']
                        print jn2['Game']['HomeTeam']
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
            ABlist.append(hitsAgainstRighty)
            ABlist.append(outsAgainstRighty)
            ABlist.append(hitsAgainstLefty)
            ABlist.append(outsAgainstLefty)
            totalAB[0] = totalAB[0]+hitsAgainstRighty
            totalAB[1] = totalAB[1]+outsAgainstRighty
            totalAB[2] = totalAB[2]+hitsAgainstLefty
            totalAB[3] = totalAB[3]+outsAgainstLefty
     #       print 'had %s hits against right handers' %(hitsAgainstRighty)
     #       print 'had %s outs against right handers' %(outsAgainstRighty)
     #       print 'had %s hits against left handers' %(hitsAgainstLefty)
     #       print 'had %s outs against left handers' %(outsAgainstLefty)
            print 'Hits on day against righty: %s '%hitsAgainstRighty
    return totalAB
if __name__ == "__main__":
    against_lefties("TOR", "BOS", conn, today, 17553)
