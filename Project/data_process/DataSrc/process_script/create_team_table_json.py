import sqlite3

conn = sqlite3.connect('..\\league_table.db')
cursor = conn.cursor()
year = '2010-2011'
league = 'bundesliga'
cursor.execute("SELECT Team from '" + league + "_" + year + "_table'")
for item in cursor:
    print(item)