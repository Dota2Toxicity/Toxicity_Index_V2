from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint
import time
import sqlite3


'''
#We ran this all once to get a nice organized txt of all parsed matches with no duplicates

#we will want to make the player list DB's useful, and then eliminate redundancy
#connect to SQL databases for parsed match ids
sqliteConnection0 = sqlite3.connect('parsed_match_db0.db')
cursor0 = sqliteConnection0.cursor()

sqliteConnection1 = sqlite3.connect('parsed_match_db1.db')
cursor1 = sqliteConnection1.cursor()

sqliteConnection2 = sqlite3.connect('parsed_match_db2.db')
cursor2 = sqliteConnection2.cursor()

sqliteConnection3 = sqlite3.connect('parsed_match_db3.db')
cursor3 = sqliteConnection3.cursor()

#Set up database variables
sqlite_select_query = """SELECT * from parsed_matches"""

cursor0.execute(sqlite_select_query)
records0 = cursor0.fetchone()
cursor1.execute(sqlite_select_query)
records1 = cursor1.fetchone()
cursor2.execute(sqlite_select_query)
records2 = cursor2.fetchone()
cursor3.execute(sqlite_select_query)
records3 = cursor3.fetchone()

#loop through the DB and create a list of player ids
parsed_match_ids = []
while records0 is not None:
    parsed_match = records0[0]
    parsed_match_ids.append(parsed_match)
    records0 = cursor0.fetchone()

print(len(parsed_match_ids))
parsed_match_ids = list(set(parsed_match_ids))
print(len(parsed_match_ids))

while records1 is not None:
    parsed_match = records1[0]
    parsed_match_ids.append(parsed_match)
    records1 = cursor1.fetchone()

print(len(parsed_match_ids))
parsed_match_ids = list(set(parsed_match_ids))
print(len(parsed_match_ids))

while records2 is not None:
    parsed_match = records2[0]
    parsed_match_ids.append(parsed_match)
    records2 = cursor2.fetchone()

print(len(parsed_match_ids))
parsed_match_ids = list(set(parsed_match_ids))
print(len(parsed_match_ids))

while records3 is not None:
    parsed_match = records3[0]
    parsed_match_ids.append(parsed_match)
    records3 = cursor3.fetchone()

print(len(parsed_match_ids))
parsed_match_ids = list(set(parsed_match_ids))
print(len(parsed_match_ids))



with open("master_parsed_match_list.txt", "w") as output:
    output.write(str(parsed_match_ids))

'''