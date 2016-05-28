import test
import test_functions
from inspect import isfunction

# A list of all functions in results.py
F_FACTORS = [f for _, f in test.__dict__.iteritems() if isfunction(f) and f.func_name.startswith('test')]
#F_FACTORS = [f for _, f in test_functions.__dict__.iteritems() if isfunction(f) and f.func_name.startswith('test')]

# A list of all tests between two teams in results.py
FACTORS = [f.func_name for f in F_FACTORS if f.func_name.startswith('test')]

DATETIME = 'DateTime'
AWAYTEAM = 'AwayTeam'
HOMETEAM = 'HomeTeam'
HOMETEAMPROBABLEPITCHER = 'HomeTeamProbablePitcher'
AWAYTEAMPROBABLEPITCHER = 'AwayTeamProbablePitcher'
STADIUM = 'Stadium'
HEATRATING = 'HeatRating'
HEATRATINGDICT = 'HeatRatingDict'
GAMEID = 'GameID'

# Key values for dictionary that is produced for each game on a given night
GAME_KEYS = [HOMETEAM, AWAYTEAM, DATETIME, HOMETEAMPROBABLEPITCHER, AWAYTEAMPROBABLEPITCHER, STADIUM, HEATRATING,
             HEATRATINGDICT, GAMEID]

