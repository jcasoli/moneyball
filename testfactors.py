import apiconnect
import json
import sys
from operator import itemgetter

import defaults

from datetime import datetime

class Test:

    def __init__(self, factor_list=defaults.F_FACTORS):
        self.factors = factor_list
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

    def _get_todays_games(self, date):
        """returns dictionary formatted list of games """
        return json.loads(self.conn.get_games_by_date(date))

    def _get_player_by_id(self, playerid):
        """
        :param playerid: player_id
        :return: Actual Player Name (string)
        """
        player = json.loads(self.conn.get_player_details_by_player(playerid))

    def _get_str_date(self, dt):
        """
        :param datetime: datetime object
        :return: string 'dd-mm-yyyy'
        """
        return dt.strftime('%m-%d-%Y')

    def _get_stadium_by_id(self, stadiumid):
        """
        :param stadiumid: stadium_id
        :return: Stadium Name (string)
        """
        return None

    def run(self, dt):
        """ Runs through all specified factors and returns a dictionary of results with factor names as keys """
        results = []

        heat_rating_dict = dict.fromkeys(defaults.FACTORS)

        # Get dictionary version of todays games from the fantasy data api
        days_games = self._get_todays_games(self._get_str_date(dt))


        # Populate matchup dictionary by running through every matchup. This is the main computation
        for game in days_games:

            # Initialize matchup dict. It will contain results from each game played today
            matchup = dict.fromkeys(defaults.GAME_KEYS)

            # Each matchup has a heatrating calculated for it depending on which way we think the
            heat_rating = 0
            # Run through every test in results.py and store result in dict
            for factor in self.factors:

                # Compute result for current test factor
                heat_rating_dict[factor.func_name], rating = factor(game['HomeTeam'], game['AwayTeam'], self.conn, dt)

                # Add current factors rating to heat_rating
                heat_rating += rating

            matchup[defaults.HEATRATING] = heat_rating
            matchup[defaults.HEATRATINGDICT] = heat_rating_dict
            matchup[defaults.STADIUM] = self._get_stadium_by_id(game['StadiumID'])
            matchup[defaults.AWAYTEAM] = game['AwayTeam']
            matchup[defaults.HOMETEAM] = game['HomeTeam']
            matchup[defaults.DATETIME] = game['DateTime'].split('T')[1]
            matchup[defaults.AWAYTEAMPROBABLEPITCHER] = game['AwayTeamProbablePitcherID']
            matchup[defaults.HOMETEAMPROBABLEPITCHER] = game['HomeTeamProbablePitcherID']
            matchup[defaults.GAMEID] = game['GameID']
            results.append(matchup)

        # Sort results by how much we feel each game will be swayed.
        sorted_results = sorted(results, key=itemgetter(defaults.HEATRATING))
        return sorted_results



if __name__ == "__main__":
    fact = Test()
    fact.run(datetime.now())