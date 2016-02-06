import api_connect
import json
from datetime import datetime
import sys
import Results

class factors:

    def __init__(self, factor_list):
        self.factors = factor_list
        now = datetime.now()
        #self.date = '%s-%s-%s' % (now.year, now.month, now.day)
        self.date = '07-07-2015'
        try:
            self.conn = api_connect.Connection()
        except:
            print("Could not open api connection. Will Exit")
            sys.exit(0)

    def __del__(self):
        try:
            self.conn.close_connection()
        except Exception as e:
            print e

    def _get_todays_games(self):
        #returns a list of todays games
        json_games = json.loads(self.conn.get_games_by_date(self.date))

        return json_games

    def run(self):
        #run through the list of tests
        todays_games = self._get_todays_games()

        for game in todays_games:
            for factor in self.factors:
                tests = [f for _, f in Results.__dict__.iteritems() if callable(f)]
                pass


if __name__ == "__main__":
    fact = factors([1])
    fact.run()
    pass