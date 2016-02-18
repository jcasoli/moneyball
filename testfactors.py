import apiconnect
import json
from datetime import datetime
import sys
import results
import defaults
class Test:

    def __init__(self, factor_list=defaults.F_FACTORS):
        self.factors = factor_list
        now = datetime.now()
        #self.date = '%s-%s-%s' % (now.year, now.month, now.day)
        self.date = '07-07-2015'
        try:
            self.conn = apiconnect.Connection()
        except:
            print("Could not open api connection. Will Exit")
            sys.exit(0)
        self.stadiums = self.conn.get_stadiums()

    def __del__(self):
        try:
            self.conn.close_connection()
        except Exception as e:
            print e

    def _get_todays_games(self):
        """returns dictionary formatted list of games """
        return json.loads(self.conn.get_games_by_date(self.date))

    def _get_player_by_id(self, playerid):
        """
        :param playerid: player_id
        :return: Actual Player Name (string)
        """
        player = json.loads(self.conn.get_player_details_by_player(playerid))

    def _get_stadium_by_id(self, stadiumid):
        """
        :param stadiumid: stadium_id
        :return: Stadium Name (string)
        """
        stadium =

    def run(self):
        """ Runs through all specified factors and returns a dictionary of results with factor names as keys """
        results = []

        # Initialize matchup dict. It will contain results from each game played today
        matchup = dict.fromkeys(defaults.GAME_KEYS)
        heat_rating_dict = dict.fromkeys(defaults.FACTORS)

        # Get dictionary version of todays games from the fantasy data api
        days_games = self._get_todays_games()


        # Populate matchup dictionary by running through every matchup. This is the main computation
        for game in days_games:

            # Run through every test in results.py and store result in dict
            for factor in self.factors:

                # Compute result for current test factor
                heat_rating_dict[factor.func_name] = factor(game['HomeTeamID'], game['AwayTeamID'], self.conn, self.date)

            matchup[defaults.HEATRATING] = heat_rating_dict
            matchup[defaults.STADIUM] = self._get_stadium_by_id(game['StadiumID'])

        return matchup



if __name__ == "__main__":
    fact = Test()
    fact.run()