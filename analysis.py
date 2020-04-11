from __future__ import print_function
import od_python
from od_python.rest import ApiException
from pprint import pprint
import time
import matplotlib.pyplot as plt
import numpy as np
import sqlite3

#connect to SQL database
sqliteConnection = sqlite3.connect('toxicity_database.db')
cursor = sqliteConnection.cursor()

#Set up database variables
sqlite_select_query = """SELECT * from toxicity"""
cursor.execute(sqlite_select_query)
records = cursor.fetchone()

#create a list of all BBDS indexes
toxicity_index_scores = []

while records is not None:
    account_id = records[0]
    toxicity_index = records[1]
    toxicity_index_scores.append(toxicity_index)
    records = cursor.fetchone()

sorted_toxicity_index_scores = sorted(toxicity_index_scores, reverse=True)
numeric_scores =[]
for x in sorted_toxicity_index_scores:
    x = eval(x)
    numeric_scores.append(x)
numeric_scores = sorted(numeric_scores, reverse=True)
x=1
y=0
while x < 11:
    print(numeric_scores[y])
    x=x+1
    y=y+1

plt.hist(numeric_scores, 2000)
plt.xlabel('Lifetime Toxicity')
plt.ylabel('Number of Players')
plt.title('North America Toxicity Distribution')
plt.xticks(np.arange(0, max(numeric_scores)+1, 50.0))
plt.axis([0, 500, 0, 35000])
plt.show()
cursor.close()