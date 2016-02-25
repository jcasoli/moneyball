import apiconnect
import httplib, urllib
import datetime
from datetime import date, timedelta
import json

today = datetime.date(2014, 5, 25)
todayString = '%s-%s-%s' % (today.year, today.month, today.day)
conn = apiconnect.Connection()
key = '0deb8f835f264ad99e24cc3622aeb396'

def against_lefties(homeTeam, awayTeam, conn, date):

    firstDayOfSeason = datetime.date(2014, 4, 3)
    currentDate = date
    daysSinceOpener = currentDate - firstDayOfSeason
    daysSinceOpenerInt = daysSinceOpener.days
    dateString = '%s-%s-%s' % (currentDate.year, currentDate.month, currentDate.day)

    currentDate = date
    dayCounter = 0
    hitsAgainstRighty = 0
    while (dayCounter < daysSinceOpenerInt):
        x = game_performance(homeTeam, conn, dateString, 10001319)
        if x!=None:
            hitsAgainstRighty = hitsAgainstRighty+x
        currentDate = currentDate - timedelta(days=1.0)
        dateString = '%s-%s-%s' % (currentDate.year, currentDate.month, currentDate.day)
        dayCounter = dayCounter+1
    print('Hits against Righty: %s') %(hitsAgainstRighty)
def get_batting_order(team, conn, date):
    data = conn.get_projected_player_game_stats_by_date(date)
    #check if team matches, check batting order, input playerID into lineupAray
    jn = json.loads(data)
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
    x=0
    for index2, key2 in enumerate(jn2):
        print 'index2: %s' %(index2)
        while x<len(jn2['Plays']):
             if (jn2['Plays'][x]['HitterID']==playerID):
                print jn2['Plays'][x]['HitterName']
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
    print 'had %s hits against right handers' %(hitsAgainstRighty)
    print 'had %s outs against right handers' %(outsAgainstRighty)
    print 'had %s hits against left handers' %(hitsAgainstLefty)
    print 'had %s outs against left handers' %(outsAgainstLefty)
    return hitsAgainstRighty
if __name__ == "__main__":
    against_lefties("TOR", "SF", conn, today)
