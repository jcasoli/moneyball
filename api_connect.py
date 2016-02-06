import httplib
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
get_player_details_by_active = 'Players'
get_player_details_by_free_agent = 'FreeAgents'
get_player_details_by_player = 'Player'
get_player_game_stats_by_date = 'PlayerGameStatsByDate'
get_player_game_stats_by_player = 'PlayerGameStatsByPlayer'
get_player_season_stats = 'PlayerSeasonStats'
get_season_stats_by_player = 'PlayerSeasonStatsByPlayer'
get_player_season_stats_by_team = 'PlayerSeasonStatsByTeam'
get_players_by_team = 'Players'
get_projected_player_game_stats_by_date = 'PlayerGameProjectionStatsByDate'
get_projected_player_game_stats_by_player = 'PlayerGameProjectionStatsByPlayer'
get_schedules = 'Games'
get_stadiums = 'Stadiums'
get_team_game_stats_by_date = 'TeamGameStatsByDate'
get_team_season_stats = 'TeamSeasonStats'

class Connection:
    OcpApimSubscriptionKey = '0deb8f835f264ad99e24cc3622aeb396'
    http_loc = 'api.fantasydata.net'
    mlb_path = '/mlb/v2/JSON/'
    conn = None

    def __init__(self):
        try:
            self.conn = httplib.HTTPSConnection('api.fantasydata.net')
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


    def get_player_details_by_active(self):
        try:
            self.conn.request("GET", self.mlb_path + get_player_details_by_active +
                            "?key=" + Connection.OcpApimSubscriptionKey)
            response = self.conn.getresponse()
            data = response.read()
            return data
        except Exception as e:
            print "warning: could not get news by player"
            return []

    def get_player_details_by_free_agents(self):
        try:
            self.conn.request("GET", self.mlb_path + get_player_details_by_free_agent +
                            "?key=" + Connection.OcpApimSubscriptionKey)
            response = self.conn.getresponse()
            data = response.read()
            return data
        except Exception as e:
            print "warning: could not get news by player"
            return []


    def get_player_details_by_player(self, playerid):
        try:
            self.conn.request("GET", self.mlb_path + get_player_details_by_player + "/" + playerid +
                            "?key=" + Connection.OcpApimSubscriptionKey)
            response = self.conn.getresponse()
            data = response.read()
            return data
        except Exception as e:
            print "warning: could not get news by player"
            return []


    def get_player_game_stats_by_date(self, date):
        try:
            self.conn.request("GET", self.mlb_path + get_player_game_stats_by_date + "/" + date +
                            "?key=" + Connection.OcpApimSubscriptionKey)
            response = self.conn.getresponse()
            data = response.read()
            return data
        except Exception as e:
            print "warning: could not get player game stats by date"
            return []

    def get_player_game_stats_by_player(self, date, playerid):
        try:
            self.conn.request("GET", self.mlb_path + get_player_game_stats_by_player + "/" + date + "/" + playerid +
                            "?key=" + Connection.OcpApimSubscriptionKey)
            response = self.conn.getresponse()
            data = response.read()
            return data
        except Exception as e:
            print "warning: could not get player game stats by date"
            return []

    def get_player_season_stats(self):
        try:
            self.conn.request("GET", self.mlb_path + get_player_season_stats +
                            "?key=" + Connection.OcpApimSubscriptionKey)
            response = self.conn.getresponse()
            data = response.read()
            return data
        except Exception as e:
            print "warning: could not get player game stats by date"
            return []


    def get_season_stats_by_player(self, season, playerid):
        try:
            self.conn.request("GET", self.mlb_path + get_season_stats_by_player + "/" + season + "/" + playerid +
                            "?key=" + Connection.OcpApimSubscriptionKey)
            response = self.conn.getresponse()
            data = response.read()
            return data
        except Exception as e:
            print "warning: could not get player game stats by date"
            return []

    def get_player_season_stats_by_team(self, season, team):
        try:
            self.conn.request("GET", self.mlb_path + get_player_season_stats_by_team + "/" + season + "/" + team +
                            "?key=" + Connection.OcpApimSubscriptionKey)
            response = self.conn.getresponse()
            data = response.read()
            return data
        except Exception as e:
            print "warning: could not get player game stats by date"
            return []


    def get_players_by_team(self, team):
        try:
            self.conn.request("GET", self.mlb_path + get_players_by_team + "/" + team +
                            "?key=" + Connection.OcpApimSubscriptionKey)
            response = self.conn.getresponse()
            data = response.read()
            return data
        except Exception as e:
            print "warning: could not get player game stats by date"
            return []

    def get_projected_player_game_stats_by_date(self, date):
        try:

            response = self.conn.getresponse()
            data = response.read()
            return data
        except Exception as e:
            print "warning: could not get player game stats by date"
            return []

    def get_projected_player_game_stats_by_player(self, date, playerid):
        try:
            return self._get_data(get_projected_player_game_stats_by_player, [date, playerid])
        except Exception as e:
            print "warning: could not get player game stats by date"
            return []

    def get_schedules(self, season):
        try:
            return self._get_data(get_schedules, [season])
        except Exception as e:
            print "warning: could not get player game stats by date"
            return []

    def get_stadiums(self):
        try:
            return self._get_data(get_stadiums)
        except Exception as e:
            print "warning: could not get player game stats by date"
            return []

    def get_team_game_stats_by_date(self, date):
        try:
            return self._get_data(get_team_game_stats_by_date, [date])
        except Exception as e:
            print "warning: could not get player game stats by date"
            return []

    def get_team_season_stats(self, season):
        try:
            return self._get_data(get_team_season_stats, [season])
        except Exception as e:
            print "warning: could not get player game stats by date"
            return []

    def _get_data(self, request_type, params=[]):
        request_url = self._create_request_url(request_type, params)
        self.conn.request("GET", request_url)
        response = self.conn.getresponse()
        data = response.read()
        return data

    def _create_request_url(self, request, parameters):
        base = self.mlb_path + request
        if len(parameters) > 0:
            url = base + "/" + "/".join(parameters)
        return url


    def close_connection(self):
        self.conn.close()
