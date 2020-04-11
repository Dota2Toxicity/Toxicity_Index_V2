from __future__ import print_function
import shelve
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint
import time
import sqlite3

#set up lists of point values
half_point_words = ['shit', 'shitting', 'shitter', 'ass', 'asshole']
one_point_words = ['fuck', 'fck', 'fucked', 'fucking', 'fucker', 'fuckr', 'fucks', 'jaja', 'fuckd','dick', 'dicking', 'dicked', 'bastard', 'bastards', 'twat', 'twats']
two_point_words = ['bitch', 'ez', 'easy', 'jew', 'jews', '?']
three_point_words = ['rape', 'raped', 'raping', 'cunt', 'cunts', 'retard', 'retards', 'retarded', 'slut', 'sluts']
four_point_words = ['nigga', 'niggas', 'autism', 'autistic', 'autist', 'autists']
five_point_words = ['chink', 'chinks', 'spic', 'spics', 'wetback']
six_point_words = ['fag', 'fags', 'faggot', 'faggots']
ten_point_words = ['nigger', 'niger', 'niggers', 'nygger', 'nyggers', 'niglet', 'nigglet']

#set up Database
#create new Database to store account ids and BBDS index
conn = sqlite3.connect('toxicity_database.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS toxicity
             (account_id text, lifetime_toxicity text)''')

#connect to SQL database for wordcloud
sqliteConnection = sqlite3.connect('Word_Cloud_Database.db')
cursor = sqliteConnection.cursor()
#Set up database variables
sqlite_select_query = """SELECT * from wordcloudtable"""
cursor.execute(sqlite_select_query)
records = cursor.fetchone()

#Loop to go through whole database
while records is not None:
    BBDS_numerator = 0
    account_id = records[0]
    word_cloud = records[1]
    word_cloud = eval(word_cloud)
    #create a list of all the keys in the word cloud dictionary
    word_list = list(word_cloud.keys())
    #print(word_cloud)
    for halfword in half_point_words:
        if halfword in word_list:
            BBDS_numerator = BBDS_numerator + (0.5*word_cloud[halfword])
    for word in one_point_words:
        if word in word_list:
            BBDS_numerator = BBDS_numerator + (1*word_cloud[word])
    for wordtwo in two_point_words:
        if wordtwo in word_list:
            BBDS_numerator = BBDS_numerator + (2*word_cloud[wordtwo])
    for wordthree in three_point_words:
        if wordthree in word_list:
            BBDS_numerator = BBDS_numerator + (3*word_cloud[wordthree])
    for wordfour in four_point_words:
        if wordfour in word_list:
            BBDS_numerator = BBDS_numerator + (4*word_cloud[wordfour])
    for wordfive in five_point_words:
        if wordfive in word_list:
            BBDS_numerator = BBDS_numerator + (5*word_cloud[wordfive])
    for wordsix in six_point_words:
        if wordsix in word_list:
            BBDS_numerator = BBDS_numerator + (6*word_cloud[wordsix])
    for wordten in ten_point_words:
        if wordten in word_list:
            BBDS_numerator = BBDS_numerator + (10*word_cloud[wordten])
    #print(BBDS_numerator)
    try:
        BBDS_index = BBDS_numerator
        #print(BBDS_index)
        # insert player id and BBDS index into new SQL Database
        c.execute('INSERT INTO toxicity VALUES (?,?)', (account_id, BBDS_index))
        conn.commit()
        records = cursor.fetchone()
    except:
        #continue the big loop
        records = cursor.fetchone()


cursor.close()
