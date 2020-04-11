from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint
import time
import sqlite3

fhand = open('match_list_4.txt')

match_id_list = list(fhand)

match_id_str = str(match_id_list[0])

#the following is a list of all the (collected?) matches on US West and east from March 28,2020 to april 4 2020

match_id_list = eval(match_id_str)

api_instance = od_python.MatchesApi()

#we will set up 4 SQLite databases and run 4 instances at once we'll comment it out for now
#create SQL Database


conn = sqlite3.connect('account_id_db_4.db')
c = conn.cursor()

#create SQL table
c.execute('''CREATE TABLE IF NOT EXISTS account_ids
             (account_id text)''')

master_account_id_list = []

#we will get a list of all 10 players in a match
progress = 1
for y in match_id_list:
    try:

        api_response = api_instance.matches_match_id_get(y, limit=99999999)

        api_response_str = str(api_response)

        api_response_dict = eval(api_response_str)

        players_list = api_response_dict['players']

        players_str = str(players_list)

        players_list = eval(players_str)

        for x in range(0,9):
            players_str = str(players_list[x])
            players_dict = eval(players_str)
            # insert variables into SQL Database
            value = str(players_dict['account_id'])
            c.execute('INSERT INTO account_ids VALUES (?)', (value,))
            conn.commit()
            progress = progress + 1
            print(str(progress) + ' of about 25,000')

    except:
        time.sleep(2)
        continue

conn.close()

