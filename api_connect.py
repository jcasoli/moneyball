import httplib, urllib, base64
import sys

active_teams = 'teams'
are_games_in_progress = 'AreAnyGamesInProgress'
box_score = 'BoxScore'
box_scores_by_date = 'BoxScores'
box_scores_by_date_delta = 'BoxScoresDelta'
games_by_date = 'GamesByDate'
get_news = 'News'
get_news_by_date = 'NewsByDate'
get_news_by_player = 'NewsByPlayerID'

class Connection:
    OcpApimSubscriptionKey = '0deb8f835f264ad99e24cc3622aeb396'
    http_loc = 'api.fantasydata.net'
    mlb_path = '/mlb/v2/JSON/'
    conn = None

    def __init__(self):
        try:
            conn = httplib.HTTPSConnection('api.fantasydata.net')
        except Exception as e:
            sys.exit(e)


    def get_active_teams(self):
        try:
            self.conn.request("GET", self.mlb_path + active_teams + "?key=" + Connection.OcpApimSubscriptionKey)
            response = self.conn.getresponse()
            data = response.read()
            return data
        except Exception as e:
            print "warning: could not get active teams"
            return []


    def get_are_games_in_progress(self):
        try:
            self.conn.request("GET", self.mlb_path + are_games_in_progress + "?key=" + Connection.OcpApimSubscriptionKey)
            response = self.conn.getresponse()
            data = response.read()
            return data
        except Exception as e:
            print "warning: could not get active teams"
            return False


    def get_box_score(self, gameid):
        try:
            self.conn.request("GET", self.mlb_path + box_score + "?key=" + Connection.OcpApimSubscriptionKey)
            response = self.conn.getresponse()
            data = response.read()
            return data
        except Exception as e:
            print "warning: could not get active teams"
            return []

    def get_box_scores_by_date(self, date):
        try:
            self.conn.request("GET", self.mlb_path + box_scores_by_date + "/" + date + "?key=" + Connection.OcpApimSubscriptionKey)
            response = self.conn.getresponse()
            data = response.read()
            return data
        except Exception as e:
            print "warning: could not get active teams"
            return []


    def get_box_scores_by_date_delta(self, date, delta):
        try:
            self.conn.request("GET", self.mlb_path + box_scores_by_date + "/" + date + "/" + delta +
                            "?key=" + Connection.OcpApimSubscriptionKey)
            response = self.conn.getresponse()
            data = response.read()
            return data
        except Exception as e:
            print "warning: could not get active teams"
            return []

    def get_games_by_date(self, date):
        try:
            self.conn.request("GET", self.mlb_path + games_by_date + "/" + date +
                            "?key=" + Connection.OcpApimSubscriptionKey)
            response = self.conn.getresponse()
            data = response.read()
            return data
        except Exception as e:
            print "warning: could not get active teams"
            return []

    def get_news(self):
        try:
            self.conn.request("GET", self.mlb_path + get_news +
                            "?key=" + Connection.OcpApimSubscriptionKey)
            response = self.conn.getresponse()
            data = response.read()
            return data
        except Exception as e:
            print "warning: could not get news"
            return []

    def get_news_by_date(self, date):
        try:
            self.conn.request("GET", self.mlb_path + get_news_by_date + "/" + date +
                            "?key=" + Connection.OcpApimSubscriptionKey)
            response = self.conn.getresponse()
            data = response.read()
            return data
        except Exception as e:
            print "warning: could not get news"
            return []

    def get_news_by_player(self, playerid):
        try:
            self.conn.request("GET", self.mlb_path + get_news_by_player + "/" + playerid +
                            "?key=" + Connection.OcpApimSubscriptionKey)
            response = self.conn.getresponse()
            data = response.read()
            return data
        except Exception as e:
            print "warning: could not get news by player"
            return []




    def close_connection(self):
        self.conn.close()
