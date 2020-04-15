from __future__ import print_function
import od_python
from od_python.rest import ApiException
from pprint import pprint
import time
import sqlite3

account_ids = 113139328
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
# create a player id to personaname dictionary with hero id as well and player slot
persona_dict = {}
for x in list1:
    if x['account_id'] == 'None':
        persona_dict.update({'anonymous': 'none'})
    else:
        persona_dict.update({x['account_id']: [x['personaname'],x['hero_id'],x['player_slot']]})

#get SQL variables ready
sqliteConnection = sqlite3.connect('toxicity_database.db')
cursor = sqliteConnection.cursor()
query = "SELECT * FROM toxicity WHERE account_id=?"
final_dict={}
final_dict_rad={}
final_dict_dire={}
running_list=[]
for player in player_list:
        cursor.execute(query, (player,))
        for row in cursor:
            running_list.append(player)
            if persona_dict[player][2] < 5:
                final_dict_rad.update({persona_dict[player][0]:[row[1],persona_dict[player][1]]})
            else:
                final_dict_dire.update({persona_dict[player][0]: [row[1], persona_dict[player][1]]})


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

#create a hero name to number dict

hero_dict = {1: 'Anti-Mage', 'Anonymous': 'Anonymous', 2: 'Axe', 3: 'Bane', 4: 'Bloodseeker', 5: 'Crystal Maiden', 6: 'Drow Ranger', 7: 'Earthshaker', 8: 'Juggernaut', 9: 'Mirana', 10: 'Morphling', 11: 'Shadow Fiend', 12: 'Phantom Lancer', 13: 'Puck', 14: 'Pudge', 15: 'Razor', 16: 'Sand King', 17: 'Storm Spirit', 18: 'Sven', 19: 'Tiny', 20: 'Vengeful Spirit', 21: 'Windranger', 22: 'Zeus', 23: 'Kunkka', 25: 'Lina', 26: 'Lion', 27: 'Shadow Shaman', 28: 'Slardar', 29: 'Tidehunter', 30: 'Witch Doctor', 31: 'Lich', 32: 'Riki', 33: 'Enigma', 34: 'Tinker', 35: 'Sniper', 36: 'Necrophos', 37: 'Warlock', 38: 'Beastmaster', 39: 'Queen of Pain', 40: 'Venomancer', 41: 'Faceless Void', 42: 'Wraith King', 43: 'Death Prophet', 44: 'Phantom Assassin', 45: 'Pugna', 46: 'Templar Assassin', 47: 'Viper', 48: 'Luna', 49: 'Dragon Knight', 50: 'Dazzle', 51: 'Clockwerk', 52: 'Leshrac', 53: "Nature's Prophet", 54: 'Lifestealer', 55: 'Dark Seer', 56: 'Clinkz', 57: 'Omniknight', 58: 'Enchantress', 59: 'Huskar', 60: 'Night Stalker', 61: 'Broodmother', 62: 'Bounty Hunter', 63: 'Weaver', 64: 'Jakiro', 65: 'Batrider', 66: 'Chen', 67: 'Spectre', 68: 'Ancient Apparition', 69: 'Doom', 70: 'Ursa', 71: 'Spirit Breaker', 72: 'Gyrocopter', 73: 'Alchemist', 74: 'Invoker', 75: 'Silencer', 76: 'Outworld Devourer', 77: 'Lycan', 78: 'Brewmaster', 79: 'Shadow Demon', 80: 'Lone Druid', 81: 'Chaos Knight', 82: 'Meepo', 83: 'Treant Protector', 84: 'Ogre Magi', 85: 'Undying', 86: 'Rubick', 87: 'Disruptor', 88: 'Nyx Assassin', 89: 'Naga Siren', 90: 'Keeper of the Light', 91: 'Io', 92: 'Visage', 93: 'Slark', 94: 'Medusa', 95: 'Troll Warlord', 96: 'Centaur Warrunner', 97: 'Magnus', 98: 'Timbersaw', 99: 'Bristleback', 100: 'Tusk', 101: 'Skywrath Mage', 102: 'Abaddon', 103: 'Elder Titan', 104: 'Legion Commander', 105: 'Techies', 106: 'Ember Spirit', 107: 'Earth Spirit', 108: 'Underlord', 109: 'Terrorblade', 110: 'Phoenix', 111: 'Oracle', 112: 'Winter Wyvern', 113: 'Arc Warden', 114: 'Monkey King', 128: 'Snapfire', 129: 'Mars', 126: 'Void Spirit'}

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
        #final_dict.update({persona_dict[player][0]:[str(BBDS_numerator),persona_dict[player][1]]})
        if persona_dict[player][2] < 5:
            final_dict_rad.update({persona_dict[player][0]: [row[1], persona_dict[player][1]]})
        else:
            final_dict_dire.update({persona_dict[player][0]: [row[1], persona_dict[player][1]]})


finallist = list(final_dict_rad.items())
for x in range(0,6):
    if len(finallist) < x:
        finallist.append(('Anonymous', ['Anonymous', 'Anonymous']))
final_dict_dire = list(final_dict_dire.items())
for y in final_dict_dire:
    finallist.append(y)
for x in range(0,11):
    if len(finallist) < x:
        finallist.append(('Anonymous', ['Anonymous', 'Anonymous']))


print(finallist[0][1][1], finallist[0][0], finallist[0][1][0], finallist[1][1][1], finallist[1][0], finallist[1][1][0], finallist[2][1][1], finallist[2][0], finallist[2][1][0], finallist[3][1][1], finallist[3][0], finallist[3][1][0], finallist[4][1][1], finallist[4][0], finallist[4][1][0], finallist[5][1][1], finallist[5][0], finallist[5][1][0], finallist[6][1][1], finallist[6][0], finallist[6][1][0], finallist[7][1][1], finallist[7][0], finallist[7][1][0], finallist[8][1][1], finallist[8][0], finallist[8][1][0], finallist[9][1][1], finallist[9][0], finallist[9][1][0])