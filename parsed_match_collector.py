from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint
import time
import sqlite3

'''

We ran this all once to get a nice organized txt of all players with no duplicates

#we will want to make the player list DB's useful, and then eliminate redundancy
#connect to SQL databases for player ids
sqliteConnection0 = sqlite3.connect('account_id_db_0.db')
cursor0 = sqliteConnection0.cursor()
sqliteConnection1 = sqlite3.connect('account_id_db_1.db')
cursor1 = sqliteConnection1.cursor()
sqliteConnection2 = sqlite3.connect('account_id_db_2.db')
cursor2 = sqliteConnection2.cursor()
sqliteConnection3 = sqlite3.connect('account_id_db_3.db')
cursor3 = sqliteConnection3.cursor()
sqliteConnection4 = sqlite3.connect('account_id_db_4.db')
cursor4 = sqliteConnection4.cursor()

#Set up database variables
sqlite_select_query = """SELECT * from account_ids"""

cursor0.execute(sqlite_select_query)
records0 = cursor0.fetchone()
cursor1.execute(sqlite_select_query)
records1 = cursor1.fetchone()
cursor2.execute(sqlite_select_query)
records2 = cursor2.fetchone()
cursor3.execute(sqlite_select_query)
records3 = cursor3.fetchone()
cursor4.execute(sqlite_select_query)
records4 = cursor4.fetchone()

#loop through the DB and create a list of player ids
account_id_list = []
while records0 is not None:
    account_id = records0[0]
    account_id_list.append(account_id)
    records0 = cursor0.fetchone()

print(len(account_id_list))
account_id_list = list(set(account_id_list))
print(len(account_id_list))

while records1 is not None:
    account_id = records1[0]
    account_id_list.append(account_id)
    records1 = cursor1.fetchone()

print(len(account_id_list))
account_id_list = list(set(account_id_list))
print(len(account_id_list))

while records2 is not None:
    account_id = records2[0]
    account_id_list.append(account_id)
    records2 = cursor2.fetchone()

print(len(account_id_list))
account_id_list = list(set(account_id_list))
print(len(account_id_list))

while records3 is not None:
    account_id = records3[0]
    account_id_list.append(account_id)
    records3 = cursor3.fetchone()

print(len(account_id_list))
account_id_list = list(set(account_id_list))
print(len(account_id_list))

while records4 is not None:
    account_id = records4[0]
    account_id_list.append(account_id)
    records4 = cursor4.fetchone()

print(len(account_id_list))
account_id_list = list(set(account_id_list))
print(len(account_id_list))

with open("master_player_list.txt", "w") as output:
    output.write(str(account_id_list))
    
'''

#we make the text file usable

fhand = open('player_list_0.txt')
master_player_list = list(fhand)
master_player_list = str(master_player_list[0])
master_player_list = eval(master_player_list)

#we get the SQL database ready
conn = sqlite3.connect('parsed_match_db0.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS parsed_matches
             (parsed_match_id text)''')

#main loop

apiinstance = od_python.PlayersApi()

progress = 0

for player in master_player_list:
    try:
        apiresponse = apiinstance.players_account_id_matches_get(player, limit=99999999)
        total_match_list = list(apiresponse)
        print(str(progress) + ' of about 75,000 players')
        progress = progress + 1
        for x in range(len(total_match_list)):
            dicti = eval(str(total_match_list[x]))
            if dicti['version'] == None:
                continue
            else:
                c.execute('INSERT INTO parsed_matches VALUES (?)', (dicti['match_id'],))
                conn.commit()
    except:
        time.sleep(2)
        continue
conn.close()