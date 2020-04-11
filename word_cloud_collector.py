from __future__ import print_function
import shelve
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint
import time
import sqlite3


#create SQL Database
conn = sqlite3.connect('Word_Cloud_Database.db')
c = conn.cursor()

#create SQL table
c.execute('''CREATE TABLE IF NOT EXISTS wordcloudtable
             (account_id text, word_cloud text)''')

#Make the account text file useful
fhand = open('master_player_list.txt')
player_id_list = list(fhand)
player_id_string = str(player_id_list[0])
player_id_list = eval(player_id_string)

#Get ODpython ready
api_instance = od_python.PlayersApi()
progress = 1

#Main Loop

for x in player_id_list:
    try:

        api_response = api_instance.players_account_id_wordcloud_get(x, limit=99999999, significant=0)
        string = str(api_response)
        dicti = eval(string)
        my_dicti = dicti['my_word_counts']
        string2 = str(my_dicti)
        xstring = str(x)

        # insert variables into SQL Database
        c.execute('INSERT INTO wordcloudtable VALUES (?,?)', (xstring, string2))
        conn.commit()

        #print out a progress report
        print(str(progress) + " of approx 75,000")
        progress = progress + 1
    except:
        time.sleep(2)
        continue

#close SQL database
conn.close()