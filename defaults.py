import results

# A list of all functions in results.py
F_FACTORS = [f for _, f in results.__dict__.iteritems() if callable(f)]

# A list of all tests between two teams in results.py
FACTORS = [f.func_name for f in F_FACTORS if f.func_name.startswith('test')]

DATETIME = 'DateTime'
AWAYTEAM = 'AwayTeam'
HOMETEAM = 'HomeTeam'
HOMETEAMPROBABLEPITCHER = 'HomeTeamProbablePitcher'
AWAYTEAMPROBABLEPITCHER = 'AwayTeamProbablePitcher'
STADIUM = 'Stadium'
HEATRATING = 'HeatRating'

GAME_KEYS = [HOMETEAM, AWAYTEAM, DATETIME, HOMETEAMPROBABLEPITCHER, AWAYTEAMPROBABLEPITCHER, STADIUM, HEATRATING]

