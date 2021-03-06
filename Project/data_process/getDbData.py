import sqlite3
import os
import json

from data_process import config
current_path = os.path.dirname(__file__)




def get_single_game_db_data(league, id):
    conn = sqlite3.connect(current_path + '\\DataSrc\\game.db')
    cursor = conn.cursor()
    league_name = config.nameDict[league]
    data = []
    cursor.execute("SELECT * from " + league_name + "_game limit " + str(id) + ",1")
    for game in cursor:
        for item in game:
            data.append(item)

    cursor.close()
    return data


def get_player_db_data(name):
    conn = sqlite3.connect(current_path + '\\DataSrc\\player_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM player where player.Name='"+ name + "'")
    data = cursor.fetchall()
    player = []
    if len(data) == 0:
        return []
    else:
        for item in data:
            for i in item:
                player.append(i)

    # cursor.execute("SELECT Name From player")
    # for item in cursor:
    #     print(item)
    cursor.close()
    return player

def get_team_season_data(league, team):
    league_name = config.nameDict[league]
    data = open(current_path + '\\DataSrc\\config-json\\team_season\\' + league_name + '_team_season.json').read()
    season_list = json.loads(data)
    seasons = season_list[str(team)]
    conn = sqlite3.connect(current_path + '\\DataSrc\\league_table.db')
    cursor = conn.cursor()
    season_data = []
    for season in seasons:
        single_season = cursor.execute("SELECT * from '" + league_name + "_" + season + "_table' where Team='" + team + "'" )
        temp = []
        for item in single_season:
            for i in item:
                temp.append(i)
        season_data.append(temp)
    cursor.close()
    return season_data


def get_team_games_data(league, team):
    conn = sqlite3.connect(current_path + '\\DataSrc\\game.db')
    cursor = conn.cursor()
    league_name = config.nameDict[league]
    games = []
    cursor.execute("SELECT * from " + league_name + "_game where " + league_name + "_game.HomeTeam=" + "'"+ team +
                   "' or " +
                   league_name + "_game.AwayTeam=" + "'" + team + "'")
    for data in cursor:
        tempList = []
        for item in data:
            tempList.append(item)
        games.append(tempList)

    cursor.close()
    return games





# test for get_single_game_db_data
# data = get_single_game_db_data('Serie A','2')
# print(data[3])

#  test for get player db
# data = get_player_db_data('L. Messi')
# index = 0
# for d in data:
#     print(str(index) + " : " + str(d))
#     index = index + 1

# print(len(data))

# test for get team season data
# print(get_team_season_data('Bundesliga', 'Dortmund'))

# test for get team games data
# get_team_games_data('Bundesliga', 'Dortmund')