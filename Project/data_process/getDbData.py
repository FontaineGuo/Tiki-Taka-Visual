import sqlite3
import os

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


# matches = pd.read_sql_query("SELECT * from bundesliga_game limit 0,1", conn)
data = get_single_game_db_data('Serie A','2')
print(data[3])