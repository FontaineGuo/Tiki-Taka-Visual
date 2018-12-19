import json
import os
from data_process import config
current_path = os.path.dirname(__file__)





def select_round_gameinfo(league, season, round):
    json_data = open(current_path + '\\DataSrc\\config-json\\game\\' + config.nameDict[league] + '_game.json').read()
    data = json.loads(json_data)
    templist = []
    for game in data:
        if game['round'] == round and game['season'] == season:
           templist.append(game)
           # print(game)
    return templist


def get_team_season_info(league, team):
    json_data = open(current_path + '\\DataSrc\\config-json\\team_season\\' + config.nameDict[league] + '_team_season.json').read()
    data = json.loads(json_data)
    return data[str(team)]

def get_team_list(league):
    json_data = open(current_path + '\\DataSrc\\config-json\\team_season\\' + config.nameDict[league] + '_team_season.json').read()
    data = json.loads(json_data)
    teamlist = []
    for key in data.keys():
        teamlist.append(key)
    return teamlist
# test get_team_season_info
get_team_season_info('Bundesliga', 'Dortmund')

# get_team_list('Bundesliga')