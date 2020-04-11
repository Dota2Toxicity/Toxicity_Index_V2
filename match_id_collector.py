from __future__ import print_function
import od_python
from od_python.rest import ApiException
from pprint import pprint
import time
import json

#the following is a list of all the (collected?) matches on US West and US East from 3/21/20 to 3/28/20
fhand = open('USWESTANDUSEAST_032120TO032820.json')
json_list = json.load(fhand)

master_list1 = []

for x in range(len(json_list)):
    result = json_list[x]['match_id']
    master_list1.append(result)

#the following is a list of all the collected matches on US west and us east from 3/28/20 to 04/04/20

fhand = open('OD_03282020_to_04042020_USWESTANDEAST.json')
json_list = json.load(fhand)

master_list2 = []

for y in range(len(master_list2)):
    result = json_list[y]['match_id']
    master_list2.append(result)

#combine them
master_list = master_list1 + master_list2

#print to file

with open("full_data.txt", "w") as output:
    output.write(str(master_list))

#break this giant list into 4 smaller ones so we can run a few instances at the next step
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

list_of_lists = list(chunks(master_list, 10000))

print(len(list_of_lists))

with open("match_list_4.txt", "w") as output:
    output.write(str(list_of_lists[4]))