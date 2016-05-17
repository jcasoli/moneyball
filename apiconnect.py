import httplib
import sys

get_active_teams = 'teams'
get_are_games_in_progress = 'AreAnyGamesInProgress'
get_box_score = 'BoxScore'
get_box_scores_by_date = 'BoxScores'
get_box_scores_by_date_delta = 'BoxScoresDelta'
get_games_by_date = 'GamesByDate'
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
get_play_by_play = 'PlayByPlay'

class Connection:
    """
    This class handles all interfacing with fantasydata.com
    """
    OcpApimSubscriptionKey = '0deb8f835f264ad99e24cc3622aeb396'
    OcpApimSubscriptionKey2 = '826b7999d438456cb2f53cef2772513e'
    http_loc = 'api.fantasydata.net'
    mlb_path = '/mlb/v2/JSON/'

    def __init__(self):
        """
        Contstructor for api connection class (fantasydata.com)
        :return: Instance of Connection
        """
        try:
            self.conn = httplib.HTTPSConnection('api.fantasydata.net')
        except Exception as e:
            sys.exit(e)


    def get_active_teams(self):
        try:
            return self._get_data(get_active_teams)
        except Exception as e:
            print "warning: could not get active teams"
            return None


    def get_are_games_in_progress(self):
        try:
            return self._get_data(get_are_games_in_progress)
        except Exception as e:
            print "warning: could not get are games in progress"
            return None


    def get_box_score(self, gameid):
        try:
            return self._get_data(get_box_score, [gameid])
        except Exception as e:
            print "warning: could not get box score"
            return None

    def get_box_scores_by_date(self, date):
        try:
            return self._get_data(get_box_scores_by_date, [date])
        except Exception as e:
            print "warning: could not get box scores by date"
            return None

    def get_box_scores_by_date_delta(self, date, delta):
        try:
            return self._get_data(get_box_scores_by_date_delta, [date, delta])
        except Exception as e:
            print "warning: could not get box scores by date delta"
            return None

    def get_games_by_date(self, date):
        try:
            return self._get_data(get_games_by_date, [date])
        except Exception as e:
            print "warning: could not get games by date"
            return None

    def get_news(self):
        try:
            return self._get_data(get_news)
        except Exception as e:
            print "warning: could not get news"
            return None

    def get_news_by_date(self, date):
        try:
            return self._get_data(get_news_by_date, [date])
        except Exception as e:
            print "warning: could not get news by date"
            return None

    def get_news_by_player(self, playerid):
        try:
            return self._get_data(get_news_by_player, [playerid])
        except Exception as e:
            print "warning: could not get news by player"
            return None

    def get_player_details_by_active(self):
        try:
            return self._get_data(get_player_details_by_active)
        except Exception as e:
            print "warning: could not get player details by active"
            return None

    def get_player_details_by_free_agents(self):
        try:
            return self._get_data(get_player_details_by_free_agent)
        except Exception as e:
            print "warning: could not get player details by free agents"
            return None


    def get_player_details_by_player(self, playerid):
        try:
            return self._get_data(get_player_details_by_player, [playerid])
        except Exception as e:
            print "warning: could not player details by player"
            return None


    def get_player_game_stats_by_date(self, date):
        try:
            return self._get_data(get_player_game_stats_by_date, [date])
        except Exception as e:
            print "warning: could not get player game stats by date"
            return None

    def get_player_game_stats_by_player(self, date, playerid):
        try:
            return self._get_data(get_player_game_stats_by_player, [date, playerid])
        except Exception as e:
            print "warning: could not get player game stats by date"
            return None

    def get_player_season_stats(self):
        try:
            return self._get_data(get_player_season_stats)
        except Exception as e:
            print "warning: could not get player game stats by date"
            return None


    def get_season_stats_by_player(self, season, playerid):
        try:
            return self._get_data(get_season_stats_by_player, [season, str(playerid)])
        except Exception as e:
            print "warning: could not get season stats by player"
            return None

    def get_player_season_stats_by_team(self, season, team):
        try:
            return self._get_data(get_player_season_stats_by_team, [season, team])
        except Exception as e:
            print "warning: could not get player season stats by team"
            return None


    def get_players_by_team(self, team):
        try:
            return self._get_data(get_players_by_team, [team])
        except Exception as e:
            print "warning: could not get players by team"
            return None

    def get_projected_player_game_stats_by_date(self, date):
        try:
            return self._get_data(get_projected_player_game_stats_by_date, [date])
        except Exception as e:
            print "warning: could not get projected player game stats by date"
            return None

    def get_projected_player_game_stats_by_player(self, date, playerid):
        try:
            return self._get_data(get_projected_player_game_stats_by_player, [date, str(playerid)])
        except Exception as e:
            print "warning: could not get player game stats by player"
            return None

    def get_schedules(self, season):
        try:
            return self._get_data(get_schedules, [season])
        except Exception as e:
            print "warning: could not get schedules"
            return None

    def get_stadiums(self):
        try:
            return self._get_data(get_stadiums)
        except Exception as e:
            print "warning: could not get stadiums"
            return None

    def get_team_game_stats_by_date(self, date):
        try:
            return self._get_data(get_team_game_stats_by_date, [date])
        except Exception as e:
            print "warning: could not get team game stats by date"
            return None

    def get_team_season_stats(self, season):
        try:
            return self._get_data(get_team_season_stats, [season])
        except Exception as e:
            print "warning: could not get team season stats"
            return None

    def get_play_by_play(self, gameid):
        try:
            return self._get_data(get_play_by_play, [str(gameid)])
        except Exception as e:
            print "warning: could not get play by play"
            return None

    def _get_data(self, request_type, params=()):
        """
        General function for polling fantasydata api. Returns json formatted data
        :param request_type: The type of request. Ex: 'GetPlayByPlay'
        :param params: extra parameters like date, playerid, etc
        :return: json formatted api data
        """

        # Create request url
        request_url = self._create_request_url(request_type, params)

        # Poll api
        self.conn.request("GET", request_url)
        response = self.conn.getresponse()
        data = response.read()
        return data

    def _create_request_url(self, request, parameters):
        """
        General function for creating a url for polling fantasydata.com
        :param request: The type of request. Ex: 'GetPlayByPlay'
        :param parameters: extra parameters like date, playerid, etc
        :return: a url string that we will generate request for
        """
        base = self.mlb_path + request

        # Check whether there are any parameters
        if len(parameters) > 0:
            url = base + "/" + "/".join(parameters) + "?key=" + Connection.OcpApimSubscriptionKey
        else:
            url = base + "?key=" + Connection.OcpApimSubscriptionKey
        return url


    def close_connection(self):
        """
        Close connection to api
        """
        self.conn.close()


if __name__ == '__main__':
    conn = Connection()
    data = conn.get_stadiums()
    data2 = conn.get_projected_player_game_stats_by_date('07-07-2015')
    data3 = conn.get_play_by_play(18373)
    pass