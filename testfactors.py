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

    def __del__(self):
        try:
            self.conn.close_connection()
        except Exception as e:
            print e

    def _get_todays_games(self):
        #returns a list of team_id tuples representing todays games
        json_games = json.loads(self.conn.get_games_by_date(self.date))
        games = []
        for game in json_games:
            games.append((game['HomeTeamID'], game['AwayTeamID']))
        return games

    def run(self):
        """ Runs through all specified factors and returns a dictionary of results with factor names as keys """
        todays_games = self._get_todays_games()
        #matchups = dict.fromkeys(todays_games)

        matchup = dict.fromkeys(defaults.FACTORS)
        for game in todays_games[:1]:
            for factor in self.factors:
                matchup[factor.func_name] = factor(game[0], game[1], self.conn, self.date)

        return matchup



if __name__ == "__main__":
    fact = Test()
    fact.run()