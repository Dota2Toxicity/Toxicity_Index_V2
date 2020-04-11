from __future__ import print_function
import od_python
from od_python.rest import ApiException
from pprint import pprint
import time
import sqlite3

account_ids = 130865744
api_instance = od_python.PlayersApi()
api_response = api_instance.players_account_id_matches_get(account_ids, limit=1)
dict1=eval(str(api_response[0]))

match_id = dict1['match_id']

#Get all 10 players from the match

player_list = []
api_instance = od_python.MatchesApi()
api_response = api_instance.matches_match_id_get(match_id)
dict2 = eval(str(api_response))
list1 = eval(str(dict2['players']))
for x in list1:
    if x['account_id'] != None:
        player_list.append(x['account_id'])
    else:
        player_list.append('Anonymous')
# create a player id to personaname dictionary
persona_dict = {}
for x in list1:
    if x['account_id'] == 'None':
        persona_dict.update({'anonymous': 'none'})
    else:
        persona_dict.update({x['account_id']: x['personaname']})

#get SQL variables ready
sqliteConnection = sqlite3.connect('toxicity_database.db')
cursor = sqliteConnection.cursor()
query = "SELECT * FROM toxicity WHERE account_id=?"
final_dict={}
running_list=[]
for player in player_list:
        cursor.execute(query, (player,))
        for row in cursor:
            running_list.append(player)
            final_dict.update({persona_dict[player]:'Lifetime Toxicity: ' + row[1]})

players_not_in_db = [x for x in player_list if x not in running_list]

# define word point values
half_point_words = ['shit', 'shitting', 'shitter', 'ass', 'asshole']
one_point_words = ['fuck', 'fck', 'fucked', 'fucking', 'fucker', 'fuckr', 'fucks', 'jaja', 'fuckd', 'dick', 'dicking',
                   'dicked', 'bastard', 'bastards', 'twat', 'twats']
two_point_words = ['bitch', 'ez', 'easy', 'jew', 'jews']
three_point_words = ['rape', 'raped', 'raping', 'cunt', 'cunts', 'retard', 'retards', 'retarded', 'slut', 'sluts']
four_point_words = ['nigga', 'niggas', 'autism', 'autistic', 'autist', 'autists']
five_point_words = ['chink', 'chinks', 'spic', 'spics', 'wetback']
six_point_words = ['fag', 'fags', 'faggot', 'faggots']
ten_point_words = ['nigger', 'niger', 'niggers', 'nygger', 'nyggers', 'niglet', 'nigglet']

#create a word cloud dictionary for each player on the list of players not in DB

word_cloud_master_dict = {}
api_instance = od_python.PlayersApi()

for player in players_not_in_db:
    if player != 'Anonymous':
        #time.sleep(2)
        api_response = api_instance.players_account_id_wordcloud_get(player, significant=0)
        string = str(api_response)
        dicti = eval(string)
        my_dicti = dicti['my_word_counts']
        word_cloud_master_dict.update({player: my_dicti})
    else:
        continue

#create a toxicity index for each player this is the main loop
for player in players_not_in_db:
    if player != 'Anonymous':
        #get a BBDS numerator
        BBDS_numerator = 0
        word_cloud = word_cloud_master_dict[player]
        word_cloud = eval(str(word_cloud))
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
        final_dict.update({persona_dict[player]:'Lifetime Toxicity: ' + str(BBDS_numerator)})


finallist = list(final_dict.items())
for x in range(0,11):
    if len(finallist) < x:
        finallist.append('Anonymous Player')

print(finallist)