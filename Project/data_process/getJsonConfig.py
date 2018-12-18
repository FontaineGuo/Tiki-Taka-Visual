import json
import os
from data_process import config
current_path = os.path.dirname(__file__)





def select_round_gameinfo(league, season, round):
    json_data = open(current_path + '\\DataSrc\\game-simple-info\\' + config.nameDict[league] + '_game.json').read()
    data = json.loads(json_data)
    templist = []
    for game in data:
        if game['round'] == round and game['season'] == season:
           templist.append(game)
           # print(game)
    return templist


